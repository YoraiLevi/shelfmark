"""shelfmark-dl: search a Shelfmark node and optionally queue a download."""

from __future__ import annotations

import argparse
import asyncio
import getpass
import json
import os
import re
import sys
import time
from contextlib import asynccontextmanager
from urllib.parse import unquote

from . import __version__

DEFAULT_HOST = "http://127.0.0.1:8084"
DONE_STATES = frozenset({"complete", "completed", "done", "available"})
FAILED_STATES = frozenset({"error", "failed", "cancelled", "canceled"})
ALREADY_QUEUED = "release is already in the download queue"
_UNSAFE_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
_RESERVED_NAMES = frozenset(
    ["con", "prn", "aux", "nul"]
    + ["com%d" % i for i in range(1, 10)]
    + ["lpt%d" % i for i in range(1, 10)]
)


class CliError(Exception):
    """User-facing CLI failure."""


class _HelpFormatter(argparse.RawDescriptionHelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = "Usage: "
        return super().add_usage(usage, actions, groups, prefix)


def _add_general(parser):
    group = parser.add_argument_group("General")
    group.add_argument("-h", "--help", action="help", help="Print this help text and exit")
    group.add_argument("--version", action="version", version="%(prog)s " + __version__, help="Print program version and exit")
    group.add_argument("--host", metavar="URL", default=DEFAULT_HOST, help="Node base URL (default: %s)" % DEFAULT_HOST)
    group.add_argument("-q", "--quiet", action="store_true", help="Print only results")
    group.add_argument("-v", "--verbose", action="store_true", help="Print extra progress")
    group.add_argument("--status", action="store_true", help="Print download queue JSON and exit")


def _add_search(parser):
    group = parser.add_argument_group("Search")
    kind = group.add_mutually_exclusive_group()
    kind.add_argument("--isbn", action="store_true", help="Treat QUERY as an ISBN")
    kind.add_argument("--title", action="store_true", help="Treat QUERY as a title (default)")
    group.add_argument("--provider", metavar="NAME", default="openlibrary", help="Metadata provider (default: openlibrary)")
    group.add_argument("--source", metavar="NAME", default="direct_download", help="Release source (default: direct_download)")
    group.add_argument("--limit", metavar="N", type=int, default=10, help="Metadata hits (default: 10)")


def _add_download(parser):
    group = parser.add_argument_group("Download")
    group.add_argument("-n", "--simulate", action="store_true", help="Search only; do not queue")
    group.add_argument("-o", "--output", metavar="DIR", help="Copy the finished file into DIR")
    group.add_argument("--wait", metavar="SECONDS", type=int, default=None, help="Poll the queue (default: 300 with -o, else 0)")


def _add_auth(parser):
    group = parser.add_argument_group("Auth")
    group.add_argument("-u", "--username", metavar="USER", help="Login when AUTH_METHOD is not none")
    group.add_argument("-p", "--password", metavar="PASS", help="Prompt if --username is set and this is omitted")


def _build_parser():
    parser = argparse.ArgumentParser(
        prog="shelfmark-dl",
        usage="shelfmark-dl [OPTIONS] QUERY [QUERY ...]",
        description="Search a Shelfmark node and optionally queue a download.",
        add_help=False,
        formatter_class=_HelpFormatter,
    )
    parser.add_argument("query", nargs="*", metavar="QUERY", help="ISBN digits or title text")
    _add_general(parser)
    _add_search(parser)
    _add_download(parser)
    _add_auth(parser)
    return parser


def parse_args(argv=None):
    parser = _build_parser()
    args = parser.parse_args(argv)
    if args.wait is None:
        args.wait = 300 if args.output else 0
    if not args.status and not args.query:
        parser.error("the following arguments are required: QUERY")
    return args


def _unsafe_cookie_session(rest):
    """A session whose cookie jar keeps cookies set by bare-IP hosts."""
    import aiohttp

    return aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(limit=rest.maxsize, ssl=rest.ssl_context),
        cookie_jar=aiohttp.CookieJar(unsafe=True),
        trust_env=True,
    )


@asynccontextmanager
async def connect_api(host):
    from shelfmark_client import ApiClient, Configuration, DefaultApi

    async with ApiClient(Configuration(host=host)) as client:
        rest = client.rest_client
        rest.pool_manager = _unsafe_cookie_session(rest)
        yield DefaultApi(client)


def _json_body(status, body):
    if status >= 400:
        raise CliError("HTTP %s: %s" % (status, body[:300]))
    if not body:
        return {}
    try:
        payload = json.loads(body.decode("utf-8"))
    except ValueError as exc:
        raise CliError("invalid JSON: %s" % exc)
    return payload if isinstance(payload, dict) else {}


async def _read_json(raw):
    return _json_body(raw.status, await raw.read())


async def _status_payload(api):
    raw = await api.api_status_get_without_preload_content()
    return await _read_json(raw)


async def maybe_login(api, username, password):
    if not username:
        return
    from shelfmark_client import ApiLoginPostRequest

    request = ApiLoginPostRequest(username=username, password=password or "")
    raw = await api.api_login_post_without_preload_content(api_login_post_request=request)
    await _read_json(raw)


async def search_metadata(api, query, provider, limit):
    raw = await api.api_metadata_search_get_without_preload_content(
        query=query, provider=provider, limit=limit
    )
    payload = await _read_json(raw)
    return (payload or {}).get("books") or []


async def search_releases(api, hit, query, isbn, source):
    raw = await api.api_releases_get_without_preload_content(
        provider=str(hit.get("provider") or "openlibrary"),
        book_id=str(hit.get("provider_id") or hit.get("id") or ""),
        source=source,
        isbn=[query] if isbn else None,
        title=None if isbn else query,
    )
    payload = await _read_json(raw)
    return (payload or {}).get("releases") or []


def _already_queued(status, body):
    if status < 400:
        return False
    return ALREADY_QUEUED in body.decode("utf-8", "replace").lower()


def _download_request(release):
    from shelfmark_client import ApiDownloadReleasePostRequest

    extra = release.get("extra")
    return ApiDownloadReleasePostRequest(
        source=str(release.get("source") or ""),
        source_id=str(release.get("source_id") or ""),
        title=release.get("title"),
        format=release.get("format"),
        extra=extra if isinstance(extra, dict) else None,
    )


async def queue_download(api, release):
    raw = await api.api_download_release_post_without_preload_content(
        api_download_release_post_request=_download_request(release)
    )
    body = await raw.read()
    if _already_queued(raw.status, body):
        source_id = str(release.get("source_id") or "")
        return {"status": "already_queued", "source_id": source_id, "id": source_id}
    return _json_body(raw.status, body)


def _entry_matches(entry, wanted):
    if not isinstance(entry, dict):
        return False
    for key in ("id", "task_id", "book_id", "source_id"):
        if str(entry.get(key) or "") in wanted:
            return True
    return False


def _find_nested(payload, wanted):
    for state, group in payload.items():
        if not isinstance(group, dict):
            continue
        for book_id, entry in group.items():
            if str(book_id) in wanted or _entry_matches(entry, wanted):
                return state, entry if isinstance(entry, dict) else {"id": book_id}
    return None


def _find_entry(payload, task_key):
    keys = task_key if isinstance(task_key, (list, tuple, set)) else [task_key]
    wanted = {str(item) for item in keys if item}
    if not isinstance(payload, dict) or not wanted:
        return None
    nested = _find_nested(payload, wanted)
    if nested:
        return nested
    for book_id, entry in payload.items():
        if str(book_id) in wanted or _entry_matches(entry, wanted):
            state = entry.get("status") if isinstance(entry, dict) else None
            return state, entry if isinstance(entry, dict) else {"id": book_id}
    return None


def _is_done(state, entry):
    status = str((entry or {}).get("status") or state or "").lower()
    return status in DONE_STATES


def _is_failed(state, entry):
    status = str((entry or {}).get("status") or state or "").lower()
    return status in FAILED_STATES


def _resolved_id(found, task_key):
    _state, entry = found
    for key in ("id", "book_id", "source_id"):
        if entry.get(key):
            return str(entry.get(key))
    keys = task_key if isinstance(task_key, (list, tuple, set)) else [task_key]
    return str(keys[0]) if keys else ""


def _task_keys(queued, release):
    keys = []
    for collection in (queued or {}, release or {}):
        for key in ("id", "task_id", "book_id", "source_id"):
            value = collection.get(key)
            if value:
                keys.append(str(value))
    return keys


async def wait_for_task(api, task_key, timeout, verbose):
    deadline = time.monotonic() + timeout
    while True:
        payload = await _status_payload(api)
        found = _find_entry(payload, task_key)
        if found and _is_done(found[0], found[1]):
            return _resolved_id(found, task_key)
        if found and _is_failed(found[0], found[1]):
            raise CliError("download failed")
        if timeout <= 0 or time.monotonic() >= deadline:
            return None
        if verbose:
            print_status(payload, False)
        await asyncio.sleep(1)


def _header_filename(header):
    starred = re.search(r"filename\*=UTF-8''([^;]+)", header, flags=re.I)
    if starred:
        return unquote(starred.group(1))
    quoted = re.search(r'filename\s*=\s*"([^"]*)"', header, flags=re.I)
    if quoted:
        return quoted.group(1)
    plain = re.search(r"filename\s*=\s*([^;]+)", header, flags=re.I)
    return plain.group(1).strip() if plain else ""


def _sanitize_name(name):
    base = name.replace("\\", "/").rsplit("/", 1)[-1]
    cleaned = _UNSAFE_CHARS.sub("_", base).strip().rstrip(". ")
    if not cleaned:
        return "download"
    if os.path.splitext(cleaned)[0].lower() in _RESERVED_NAMES:
        cleaned = "_" + cleaned
    return cleaned


def _unique_path(outdir, name):
    stem, ext = os.path.splitext(name)
    path = os.path.join(outdir, name)
    index = 2
    while os.path.exists(path):
        path = os.path.join(outdir, "%s-%d%s" % (stem, index, ext))
        index += 1
    return path


def _filename_from_headers(raw, task_id):
    name = _header_filename(raw.headers.get("Content-Disposition") or "")
    return _sanitize_name(name or str(task_id))


def _assert_complete_body(body, headers, task_id, filename=""):
    declared = headers.get("Content-Length")
    if declared and int(declared) != len(body):
        raise CliError("local download truncated for %s: got %s of %s bytes" % (task_id, len(body), declared))
    ext = os.path.splitext(filename)[1].lower()
    if ext not in {".epub", ".zip", ".cbz"} and not body.startswith(b"PK"):
        return
    import io
    import zipfile
    try:
        bad = zipfile.ZipFile(io.BytesIO(body)).testzip()
    except zipfile.BadZipFile as exc:
        raise CliError("local download is not a complete archive for %s: %s" % (task_id, exc))
    if bad:
        raise CliError("corrupt archive member %s for %s" % (bad, task_id))


async def save_local_download(api, task_id, outdir):
    raw = await api.api_local_download_get_without_preload_content(id=str(task_id))
    body = await raw.read()
    if raw.status >= 400:
        raise CliError("local download failed: HTTP %s" % raw.status)
    if not body:
        raise CliError("local download returned an empty body for %s" % task_id)
    name = _filename_from_headers(raw, task_id)
    _assert_complete_body(body, raw.headers, task_id, name)
    os.makedirs(outdir, exist_ok=True)
    path = _unique_path(outdir, name)
    with open(path, "wb") as handle:
        handle.write(body)
    return path


def print_status(payload, quiet):
    indent = None if quiet else 2
    print(json.dumps(payload, indent=indent, default=str))


def _show(rows, quiet):
    indent = None if quiet else 2
    print(json.dumps(rows, indent=indent, default=str))


async def _run_download(api, args, release):
    queued = await queue_download(api, release)
    if not args.quiet:
        print(json.dumps(queued, indent=2, default=str))
    keys = _task_keys(queued, release)
    if queued.get("status") == "already_queued":
        return await _finish_existing(api, args, keys)
    return await _wait_and_save(api, args, keys)


async def _finish_existing(api, args, keys):
    payload = await _status_payload(api)
    found = _find_entry(payload, keys)
    if found and _is_failed(found[0], found[1]):
        raise CliError("download failed")
    if found and not _is_done(found[0], found[1]):
        return await _wait_and_save(api, args, keys)
    task_id = _resolved_id(found, keys) if found else (keys[0] if keys else "")
    return await _save_if_requested(api, args, task_id)


async def _wait_and_save(api, args, keys):
    task_id = await wait_for_task(api, keys, args.wait, args.verbose)
    return await _save_if_requested(api, args, task_id)


async def _save_if_requested(api, args, task_id):
    if not args.output:
        return 0
    if not task_id:
        raise CliError("download did not finish in time")
    path = await save_local_download(api, task_id, args.output)
    if not args.quiet:
        print(path)
    return 0


async def _run_search(api, args):
    query = " ".join(args.query)
    books = await search_metadata(api, query, args.provider, args.limit)
    if not books:
        raise CliError("no metadata hits for %r" % query)
    _show(books, args.quiet)
    releases = await search_releases(api, books[0], query, args.isbn, args.source)
    if not releases:
        raise CliError("no releases for %r" % query)
    _show(releases, args.quiet)
    if args.simulate:
        return 0
    return await _run_download(api, args, releases[0])


async def async_main(args):
    async with connect_api(args.host) as api:
        await maybe_login(api, args.username, args.password)
        if args.status:
            print_status(await _status_payload(api), args.quiet)
            return 0
        return await _run_search(api, args)


def _error_types():
    import aiohttp
    from shelfmark_client.exceptions import ApiException

    return (CliError, OSError, TimeoutError, aiohttp.ClientError, ApiException)


def _fail(exc):
    sys.stderr.write("%s\n" % exc)
    return 1


def _prompt_password(args):
    if args.username and args.password is None:
        args.password = getpass.getpass("Password: ")


def main(argv=None):
    args = parse_args(argv)
    errors = _error_types()
    try:
        _prompt_password(args)
        return asyncio.run(async_main(args))
    except KeyboardInterrupt:
        return 130
    except EOFError:
        return _fail(CliError("password required: pass --password or use a TTY"))
    except errors as exc:
        return _fail(exc)


if __name__ == "__main__":
    sys.exit(main())
