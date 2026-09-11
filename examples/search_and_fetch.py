"""Search a Shelfmark node, queue a release, and fetch the finished file.

The file is always pulled through ``GET /api/localdownload``; the script never
touches the node's filesystem.
"""

from __future__ import annotations

import argparse
import asyncio
import re
import time
from contextlib import asynccontextmanager
from pathlib import Path

from shelfmark_client import (
    ApiClient,
    ApiDownloadReleasePostRequest,
    Configuration,
    DefaultApi,
)

DEFAULT_HOST = "http://127.0.0.1:8084"
DONE_STATES = {"complete", "completed", "done", "available"}


def parse_args(argv=None):
    """Parse --isbn/--title/--host/--output."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    query = parser.add_mutually_exclusive_group(required=True)
    query.add_argument("--isbn", help="ISBN digits to search for")
    query.add_argument("--title", help="Title text to search for")
    parser.add_argument("--host", default=DEFAULT_HOST, help=f"node base URL (default: {DEFAULT_HOST})")
    parser.add_argument("--output", type=Path, help="directory to write the finished file into")
    return parser.parse_args(argv)


@asynccontextmanager
async def connect_client(host):
    """Yield a DefaultApi bound to an ApiClient for ``host``."""
    async with ApiClient(Configuration(host=host)) as client:
        yield DefaultApi(client)


async def find_book(api, args):
    """Return the first metadata hit for the ISBN or title."""
    query = args.isbn or args.title
    books = await api.api_metadata_search_get(query=query, provider="openlibrary", limit=10)
    hits = (books or {}).get("books") or []
    if not hits:
        raise SystemExit(f"no metadata hits for {query!r}")
    return hits[0]


async def find_release(api, book, args):
    """Return the first downloadable release for a metadata hit."""
    releases = await api.api_releases_get(
        provider=book["provider"],
        book_id=book["provider_id"],
        isbn=[args.isbn] if args.isbn else None,
        title=args.title,
        source="direct_download",
    )
    items = (releases or {}).get("releases") or []
    if not items:
        raise SystemExit("no releases (source may be blocked or unconfigured)")
    return items[0]


async def queue_release(api, release, book):
    """Queue the release on the node and return its task id."""
    request = ApiDownloadReleasePostRequest(
        source=release.get("source") or "direct_download",
        source_id=release["source_id"],
        title=release.get("title") or book.get("title"),
        format=release.get("format"),
        extra=release.get("extra") or {},
    )
    queued = await api.api_download_release_post(api_download_release_post_request=request)
    print("queued", queued)
    return release["source_id"]


def find_task_entry(status, task_id):
    """Find a queue entry whether the map is flat or grouped by state."""
    for key, value in (status or {}).items():
        if not isinstance(value, dict):
            continue
        if key == task_id:
            return value
        nested = value.get(task_id)
        if isinstance(nested, dict):
            entry = dict(nested)
            entry.setdefault("status", key)
            return entry
    return {}


async def wait_until_done(api, task_id, timeout=300, interval=5):
    """Poll the queue until the task reports a done state."""
    deadline = time.monotonic() + timeout
    while True:
        entry = find_task_entry(await api.api_status_get(), task_id)
        state = str(entry.get("status") or "").lower()
        if state in DONE_STATES:
            return state
        if time.monotonic() >= deadline:
            raise SystemExit(f"timed out waiting for {task_id} (last state: {state or 'unknown'})")
        print("waiting", state or "queued")
        await asyncio.sleep(interval)


def download_filename(task_id, release):
    """Build a safe filename from the release title and format."""
    stem = re.sub(r"[^\w.-]+", "_", str(release.get("title") or task_id)).strip("_")
    suffix = str(release.get("format") or "bin").lstrip(".")
    return f"{stem or task_id}.{suffix}"


async def save_download(api, task_id, release, output):
    """Write the finished bytes into ``output`` via /api/localdownload."""
    output.mkdir(parents=True, exist_ok=True)
    raw = await api.api_local_download_get_without_preload_content(id=task_id)
    body = await raw.read()
    dest = output / download_filename(task_id, release)
    dest.write_bytes(body)
    print("saved via /api/localdownload", dest)
    return dest


async def main(argv=None):
    """Search, queue, and optionally download one release."""
    args = parse_args(argv)
    async with connect_client(args.host) as api:
        book = await find_book(api, args)
        print("book", book.get("title"), book.get("provider"), book.get("provider_id"))
        release = await find_release(api, book, args)
        task_id = await queue_release(api, release, book)
        if args.output is None:
            print("queued only; pass --output DIR to download the file")
            return 0
        await wait_until_done(api, task_id)
        await save_download(api, task_id, release, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
