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


class _Spinner:
    """Single-line stderr progress indicator; inert when stderr is not a TTY."""

    FRAMES = "|/-\\"
    INTERVAL = 0.12

    def __init__(self, stream):
        self._stream = stream
        self._tty = bool(getattr(stream, "isatty", None) and stream.isatty())
        self._label = ""
        self._task = None
        self._frame = 0
        self._width = 0

    def start(self, label):
        self._label = label
        if self._tty:
            if self._task is None:
                self._task = asyncio.ensure_future(self._spin())
            return
        self._stream.write("%s\n" % label)
        self._stream.flush()

    def update(self, label):
        if label == self._label:
            return
        self._label = label
        if not self._tty:
            self._stream.write("%s\n" % label)
            self._stream.flush()

    def relabel(self, label):
        self._label = label

    async def stop(self):
        task, self._task = self._task, None
        if task is not None:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        self.clear()

    def clear(self):
        if not self._tty or not self._width:
            return
        self._stream.write("\r%s\r" % (" " * self._width))
        self._stream.flush()
        self._width = 0

    async def _spin(self):
        while True:
            frame = self.FRAMES[self._frame % len(self.FRAMES)]
            self._frame += 1
            text = "%s %s" % (frame, self._label)
            self._width = max(self._width, len(text))
            self._stream.write("\r%s" % text.ljust(self._width))
            self._stream.flush()
            await asyncio.sleep(self.INTERVAL)


class Out:
    """Output policy: human lines, quiet results only, or JSONL debug events."""

    def __init__(self, mode, verbose=False, stream=None):
        self.mode = mode
        self.verbose = bool(verbose) and mode == "human"
        self.stream = sys.stderr if stream is None else stream
        self._spinner = _Spinner(self.stream) if mode == "human" else None

    def say(self, text):
        if self.mode != "human":
            return
        self._spinner.clear()
        self.stream.write("%s\n" % text)
        self.stream.flush()

    def detail(self, text):
        if self.verbose:
            self.say(text)

    def event(self, kind, **fields):
        if self.mode != "jsonl":
            return
        record = {"event": kind}
        record.update(fields)
        sys.stdout.write(json.dumps(record, default=str, separators=(",", ":")) + "\n")
        sys.stdout.flush()

    def result(self, text):
        if self.mode == "jsonl":
            return
        print(text)

    def begin(self, label):
        if self._spinner is not None:
            self._spinner.start(label)

    def progress(self, label):
        if self.verbose:
            self.say(label)
            if self._spinner is not None:
                self._spinner.relabel(label)
            return
        if self._spinner is not None:
            self._spinner.update(label)

    async def end(self):
        if self._spinner is not None:
            await self._spinner.stop()

    def close(self):
        if self._spinner is not None:
            self._spinner.clear()


class _HelpFormatter(argparse.RawDescriptionHelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = "Usage: "
        return super().add_usage(usage, actions, groups, prefix)


def _add_general(parser):
    group = parser.add_argument_group("General")
    group.add_argument("-h", "--help", action="help", help="Print this help text and exit")
    group.add_argument(
        "--version",
        action="version",
        version="%(prog)s " + __version__,
        help="Print program version and exit",
    )
    group.add_argument(
        "--host",
        metavar="URL",
        default=DEFAULT_HOST,
        help="Node base URL (default: %s)" % DEFAULT_HOST,
    )
    group.add_argument(
        "-q", "--quiet", action="store_true", help="No progress; print only the saved file path"
    )
    group.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Extra human detail on stderr (every metadata hit and wait status change)",
    )
    group.add_argument(
        "--jsonl", action="store_true", help="One JSON event per line on stdout (debug)"
    )
    group.add_argument("--status", action="store_true", help="Print download queue JSON and exit")


def _add_search(parser):
    group = parser.add_argument_group("Search")
    kind = group.add_mutually_exclusive_group()
    kind.add_argument("--isbn", action="store_true", help="Treat QUERY as an ISBN")
    kind.add_argument("--title", action="store_true", help="Treat QUERY as a title (default)")
    group.add_argument(
        "--provider",
        metavar="NAME",
        default="openlibrary",
        help="Metadata provider (default: openlibrary)",
    )
    group.add_argument(
        "--source",
        metavar="NAME",
        default="direct_download",
        help="Release source (default: direct_download)",
    )
    group.add_argument(
        "--limit", metavar="N", type=int, default=10, help="Metadata hits (default: 10)"
    )


def _add_download(parser):
    group = parser.add_argument_group("Download")
    group.add_argument("-n", "--simulate", action="store_true", help="Search only; do not queue")
    group.add_argument("-o", "--output", metavar="DIR", help="Copy the finished file into DIR")
    group.add_argument(
        "--wait",
        metavar="SECONDS",
        type=int,
        default=None,
        help="Poll the queue (default: 300 with -o, else 0)",
    )
    group.add_argument(
        "--force-download",
        action="store_true",
        help="Re-queue a completed release (POST force_download=true)",
    )


def _add_auth(parser):
    group = parser.add_argument_group("Auth")
    group.add_argument(
        "-u", "--username", metavar="USER", help="Login when AUTH_METHOD is not none"
    )
    group.add_argument(
        "-p", "--password", metavar="PASS", help="Prompt if --username is set and this is omitted"
    )


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
    if args.quiet and args.jsonl:
        parser.error("argument --jsonl: not allowed with argument -q/--quiet")
    if args.quiet and args.verbose:
        parser.error("argument -v/--verbose: not allowed with argument -q/--quiet")
    args.mode = "jsonl" if args.jsonl else "quiet" if args.quiet else "human"
    return args


def _unsafe_cookie_session(rest):
    """A session whose cookie jar keeps cookies set by bare-IP hosts."""
    import aiohttp

    return aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(limit=rest.maxsize, ssl=rest.ssl_context),
        cookie_jar=aiohttp.CookieJar(unsafe=True),
        trust_env=True,
        timeout=aiohttp.ClientTimeout(sock_connect=15, sock_read=120),
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


def _hit_isbns(hit):
    """ISBNs carried by a metadata hit, longest form first, de-duplicated."""
    hit = hit if isinstance(hit, dict) else {}
    found = []
    for key in ("isbn_13", "isbn_10", "isbn"):
        value = hit.get(key)
        values = value if isinstance(value, (list, tuple)) else [value]
        for item in values:
            text = str(item).strip() if item else ""
            if text and text not in found:
                found.append(text)
    return found


async def search_releases(api, hit, query, isbn, source):
    hit = hit if isinstance(hit, dict) else {}
    kwargs = {
        "provider": str(hit.get("provider") or "openlibrary"),
        "book_id": str(hit.get("provider_id") or hit.get("id") or ""),
        "source": source,
    }
    if isbn:
        kwargs["isbn"] = [query]
    else:
        isbns = _hit_isbns(hit)
        if isbns:
            kwargs["isbn"] = isbns
        else:
            # Direct download is ISBN-first; without one it needs title/author search.
            kwargs["expand_search"] = True
        kwargs["title"] = _text(hit.get("title")) or query
        author = _text(hit.get("author") or hit.get("authors"))
        if author:
            kwargs["author"] = author
    raw = await api.api_releases_get_without_preload_content(**kwargs)
    payload = await _read_json(raw)
    return (payload or {}).get("releases") or []


def _already_queued(status, body):
    if status < 400:
        return False
    return ALREADY_QUEUED in body.decode("utf-8", "replace").lower()


def _download_request(release, *, force_download=False):
    from shelfmark_client import ApiDownloadReleasePostRequest

    extra = release.get("extra")
    request_kwargs = {
        "source": str(release.get("source") or ""),
        "source_id": str(release.get("source_id") or ""),
        "title": release.get("title"),
        "format": release.get("format"),
        "extra": extra if isinstance(extra, dict) else None,
    }
    if force_download:
        request_kwargs["force_download"] = True
    return ApiDownloadReleasePostRequest(**request_kwargs)


async def queue_download(api, release, *, force_download=False):
    raw = await api.api_download_release_post_without_preload_content(
        api_download_release_post_request=_download_request(release, force_download=force_download)
    )
    body = await raw.read()
    if _already_queued(raw.status, body):
        source_id = str(release.get("source_id") or "")
        return {"status": "already_queued", "source_id": source_id, "id": source_id}
    if force_download and raw.status == 409:
        source_id = str(release.get("source_id") or "")
        return {"status": "already_queued", "source_id": source_id, "id": source_id}
    if force_download and raw.status >= 400:
        raise CliError("force-download refused: HTTP %s: %s" % (raw.status, body[:300]))
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


def _entry_state(found):
    if not found:
        return "pending", None
    state, entry = found
    entry = entry if isinstance(entry, dict) else {}
    status = str(entry.get("status") or state or "") or "pending"
    progress = entry.get("progress")
    if progress is None:
        progress = entry.get("percent")
    return status, progress


def _wait_label(state, progress):
    if progress in (None, ""):
        return "waiting: %s" % state
    return "waiting: %s (%s)" % (state, progress)


async def wait_for_task(api, task_key, timeout, out):
    deadline = time.monotonic() + timeout
    seen = None
    out.begin(_wait_label("pending", None))
    try:
        while True:
            payload = await _status_payload(api)
            found = _find_entry(payload, task_key)
            state, progress = _entry_state(found)
            if (state, progress) != seen:
                seen = (state, progress)
                out.progress(_wait_label(state, progress))
                out.event("wait", state=state, progress=progress)
            if found and _is_done(found[0], found[1]):
                return _resolved_id(found, task_key)
            if found and _is_failed(found[0], found[1]):
                raise CliError("download failed")
            if timeout <= 0 or time.monotonic() >= deadline:
                return None
            await asyncio.sleep(1)
    finally:
        await out.end()


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
        raise CliError(
            "local download truncated for %s: got %s of %s bytes" % (task_id, len(body), declared)
        )
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


def print_status(payload, mode):
    if mode == "jsonl":
        print(json.dumps(payload, default=str, separators=(",", ":")))
        return
    indent = None if mode == "quiet" else 2
    print(json.dumps(payload, indent=indent, default=str))


def _text(value):
    if isinstance(value, (list, tuple)):
        return ", ".join(str(item) for item in value if item)
    return "" if value is None else str(value)


def _book_fields(book):
    book = book if isinstance(book, dict) else {}
    return {
        "title": _text(book.get("title")),
        "author": _text(book.get("author") or book.get("authors")),
        "provider": _text(book.get("provider")),
        "provider_id": _text(book.get("provider_id") or book.get("id")),
    }


def _book_line(book):
    fields = _book_fields(book)
    parts = [fields["title"] or "(untitled)"]
    if fields["author"]:
        parts.append("by %s" % fields["author"])
    ident = "/".join(part for part in (fields["provider"], fields["provider_id"]) if part)
    if ident:
        parts.append("[%s]" % ident)
    return " ".join(parts)


def _release_fields(release):
    release = release if isinstance(release, dict) else {}
    return {
        "title": _text(release.get("title")),
        "format": _text(release.get("format")),
        "size": _text(release.get("size") or release.get("filesize")),
        "source": _text(release.get("source")),
        "source_id": _text(release.get("source_id")),
    }


def _release_line(release):
    fields = _release_fields(release)
    parts = [fields["title"] or "(untitled)"]
    meta = [item for item in (fields["format"], fields["size"], fields["source"]) if item]
    if meta:
        parts.append("(%s)" % ", ".join(meta))
    if fields["source_id"]:
        parts.append("source_id=%s" % fields["source_id"])
    return " ".join(parts)


async def _run_download(api, args, release, out):
    out.say("Queueing %s" % _release_line(release))
    queued = await queue_download(
        api, release, force_download=getattr(args, "force_download", False)
    )
    state = str(queued.get("status") or "queued")
    out.say("Node accepted the release (%s)" % state)
    out.event("queued", status=state, id=queued.get("id"), **_release_fields(release))
    keys = _task_keys(queued, release)
    if queued.get("status") == "already_queued":
        return await _finish_existing(api, args, keys, out)
    return await _wait_and_save(api, args, keys, out)


async def _finish_existing(api, args, keys, out):
    payload = await _status_payload(api)
    found = _find_entry(payload, keys)
    if found and _is_failed(found[0], found[1]):
        raise CliError("download failed")
    if found and not _is_done(found[0], found[1]):
        return await _wait_and_save(api, args, keys, out)
    task_id = _resolved_id(found, keys) if found else (keys[0] if keys else "")
    return await _save_if_requested(api, args, task_id, out)


async def _wait_and_save(api, args, keys, out):
    task_id = await wait_for_task(api, keys, args.wait, out)
    return await _save_if_requested(api, args, task_id, out)


async def _save_if_requested(api, args, task_id, out):
    if not args.output:
        return 0
    if not task_id:
        raise CliError("download did not finish in time")
    out.say("Copying the finished file into %s" % args.output)
    out.begin("copying file")
    try:
        path = await save_local_download(api, task_id, args.output)
    finally:
        await out.end()
    out.event("saved", id=str(task_id), path=path)
    out.result(path)
    return 0


async def _run_search(api, args, out):
    query = " ".join(args.query)
    out.say("Searching %s metadata for %s" % (args.provider, query))
    out.event(
        "metadata_search",
        query=query,
        provider=args.provider,
        isbn=bool(args.isbn),
        limit=args.limit,
    )
    out.begin("searching metadata")
    try:
        books = await search_metadata(api, query, args.provider, args.limit)
    finally:
        await out.end()
    if not books:
        raise CliError("no metadata hits for %r" % query)
    for book in books:
        out.event("metadata_hit", **_book_fields(book))
        out.detail(_book_line(book))
    out.say("%d metadata hit(s); using %s" % (len(books), _book_line(books[0])))
    out.say("Searching %s releases (this can take a while)" % args.source)
    out.event("release_search", source=args.source, **_book_fields(books[0]))
    out.begin("searching releases")
    try:
        releases = await search_releases(api, books[0], query, args.isbn, args.source)
    finally:
        await out.end()
    if not releases:
        fields = _book_fields(books[0])
        using = " / ".join(part for part in (fields["title"], fields["provider_id"]) if part)
        if using:
            raise CliError("no releases for %r (using %s)" % (query, using))
        raise CliError("no releases for %r" % query)
    for release in releases:
        out.detail(_release_line(release))
    out.say("%d release(s); picking %s" % (len(releases), _release_line(releases[0])))
    if args.simulate:
        return 0
    return await _run_download(api, args, releases[0], out)


async def async_main(args, out):
    async with connect_api(args.host) as api:
        await maybe_login(api, args.username, args.password)
        if args.status:
            print_status(await _status_payload(api), out.mode)
            return 0
        return await _run_search(api, args, out)


def _error_types():
    import aiohttp
    from shelfmark_client.exceptions import ApiException

    return (CliError, OSError, TimeoutError, aiohttp.ClientError, ApiException)


def _fail(exc, out=None):
    if out is not None:
        out.close()
        out.event("error", type=type(exc).__name__, message=str(exc))
    sys.stderr.write("%s\n" % exc)
    return 1


def _prompt_password(args):
    if args.username and args.password is None:
        args.password = getpass.getpass("Password: ")


def main(argv=None):
    args = parse_args(argv)
    out = Out(args.mode, verbose=args.verbose)
    errors = _error_types()
    try:
        _prompt_password(args)
        return asyncio.run(async_main(args, out))
    except KeyboardInterrupt:
        out.close()
        return 130
    except EOFError:
        return _fail(CliError("password required: pass --password or use a TTY"), out)
    except errors as exc:
        return _fail(exc, out)


if __name__ == "__main__":
    sys.exit(main())
