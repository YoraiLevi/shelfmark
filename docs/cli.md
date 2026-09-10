# shelfmark-dl CLI

`shelfmark-dl` searches a Shelfmark node and optionally queues a download. It ships as a console script on the generated client package (`aiohttp` / `pydantic` only).

Flow: metadata search (ISBN or title) → release search → queue download on the node → wait until the queue is done → copy the file off the node via `GET /api/localdownload`. The CLI never reads the node's filesystem.

`QUERY` is positional (`ISBN` digits or title text). `--isbn` / `--title` only say how to treat it.

## Usage tutorial

### 1. Prerequisites

You need three things before the first command:

- **`uv`** — provides `uvx`, which runs the CLI straight from git without installing anything permanently. Install it from [astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/).
- **`git`** — `uvx` shells out to it to fetch the source.
- **A running Shelfmark node** — the CLI is a pure HTTP client; it does nothing useful on its own.

Confirm the node answers `GET http://127.0.0.1:8084/api/health` before you go further:

```bash
curl http://127.0.0.1:8084/api/health
```

A healthy node returns `200` with JSON such as `{"status":"ok"}`. If this call fails or hangs, fix the node (or your `--host` URL) first — every later step talks to that same base URL.

### 2. Print the help text

```bash
uvx --from "git+https://github.com/YoraiLevi/shelfmark.git@feature/python-client#subdirectory=generated/python" shelfmark-dl --help
```

The first run resolves the git dependency and builds the client, so it takes noticeably longer than later runs. If this prints the four flag groups, your toolchain is good.

Pin a commit or tag instead of `feature/python-client` when you want a frozen CLI:

```bash
uvx --from "git+https://github.com/YoraiLevi/shelfmark.git@<tag-or-commit-sha>#subdirectory=generated/python" shelfmark-dl --help
```

### 3. Search without queueing anything

`-n` / `--simulate` stops after the search stage. Use it to see what the node would pick before you commit to a download:

```bash
uvx --from "git+https://github.com/YoraiLevi/shelfmark.git@feature/python-client#subdirectory=generated/python" \
  shelfmark-dl --host http://127.0.0.1:8084 --isbn -n 9780140449136
```

You get two JSON blocks: the metadata hits (`GET /api/metadata/search`) and the releases for the first hit (`GET /api/releases`). Nothing is queued and no file is written. The CLI acts on the **first** release in that list, so this is your chance to check that it is the edition you want — narrow it with `--source`, `--provider`, or `--limit` if it is not.

### 4. Look at the queue

```bash
uvx --from "git+https://github.com/YoraiLevi/shelfmark.git@feature/python-client#subdirectory=generated/python" \
  shelfmark-dl --host http://127.0.0.1:8084 --status
```

This prints the node's `GET /api/status` payload — the download queue, grouped by state — and exits. `--status` is the only mode that does not need `QUERY`.

### 5. Search, queue, and copy the file back

```bash
mkdir downloads
uvx --from "git+https://github.com/YoraiLevi/shelfmark.git@feature/python-client#subdirectory=generated/python" \
  shelfmark-dl --host http://127.0.0.1:8084 --isbn -o ./downloads -v --wait 180 9780140449136
```

- `-o ./downloads` is what turns the run into a real download; the directory must be writable by you (the CLI writes locally, not on the node).
- `-v` prints queue-polling progress so a long wait does not look like a hang.
- `--wait 180` caps the poll at three minutes. Without `--wait`, `-o` implies `300`.

On success the last line printed is the path of the file that was written into `./downloads`.

> The command above uses `\` line continuations, which is POSIX shell syntax. In PowerShell use a backtick (`` ` ``), in `cmd.exe` use `^`, or just join it into one line.

### What actually happens

- `POST /api/releases/download` **queues the release on the node**. It never streams bytes back to the caller; a `200` here only means "accepted for download".
- `GET /api/localdownload` is the copy step. Once the queue entry reports a finished state (`complete` / `completed` / `done` / `available`), the CLI fetches the bytes through this endpoint and writes them into `-o`. This is the only path that produces a local file.
- `-n` / `--simulate` never queues. It stops right after the release search.
- `-o` / `--output` both queues **and** pulls: queue → poll `GET /api/status` → `GET /api/localdownload` → write the file.
- With neither `-n` nor `-o`, the CLI queues and reports status, but writes no file.

**Re-running the same ISBN.** If that release is still on the node — queued, downloading, or already downloaded and not yet cleared — the second queue attempt is an *already-queued* case, not a new download. The node answers `POST /api/releases/download` with `{"error":"Release is already in the download queue"}`, because the work it is being asked to schedule is already scheduled. This is an expected, benign condition: the release is still on its way (or already there), so re-queueing would be a no-op anyway. The CLI treats already-queued as success and continues wait-and-copy.

## Install

```bash
uvx --from "git+https://github.com/YoraiLevi/shelfmark.git@feature/python-client#subdirectory=generated/python" shelfmark-dl --help
uvx --from "git+https://github.com/YoraiLevi/shelfmark.git@feature/python-client#subdirectory=generated/python" \
  shelfmark-dl --host http://127.0.0.1:8084 --isbn --output ./downloads 9780140449136
```

## `--help` groups

`shelfmark-dl --help` lists flags in four groups:

| Group | Flags |
| :--- | :--- |
| General | `-h` / `--help`, `--version`, `--host`, `-q` / `--quiet`, `-v` / `--verbose`, `--status` |
| Search | `--isbn`, `--title`, `--provider`, `--source`, `--limit` |
| Download | `-n` / `--simulate`, `-o` / `--output`, `--wait`, `--force-download` |
| Auth | `-u` / `--username`, `-p` / `--password` |

## Flags

| Flag | Role |
| :--- | :--- |
| `--isbn` | Treat `QUERY` as an ISBN |
| `--title` | Treat `QUERY` as a title (default) |
| `--host` | Node base URL (default `http://127.0.0.1:8084`) |
| `-o` / `--output` `DIR` | Copy the finished file into `DIR` |
| `-n` / `--simulate` | Search only; do not queue |
| `--status` | Print download queue JSON and exit |
| `--provider` | Metadata provider (default `openlibrary`) |
| `--source` | Release source (default `direct_download`) |
| `--limit` | Metadata hits (default `10`) |
| `--wait` | Poll the queue (default `300` with `-o`, else `0`) |
| `--force-download` | On already-queued, `POST /api/download/<id>/retry` instead of copying the stored file |
| `-u` / `--username`, `-p` / `--password` | Login when `AUTH_METHOD` is not `none`. Prompt if `--username` is set and `--password` is omitted |

`--status` does not require `QUERY`. Every other mode does.

## Finished files

`POST /api/releases/download` queues work on the **node**. It does not stream the file to the caller. Pull bytes through `GET /api/localdownload` after the queue reports completion (`complete` / `completed` / `done` / `available`). That is the only path the CLI uses to write a file.

When `--output` is omitted, the CLI queues (unless `--simulate`) and prints status only.

When `AUTH_METHOD` is not `none`, pass `-u` / `-p` so the CLI can call `api_login_post` and reuse the cookie jar.

`--force-download` is for an already-queued `source_id`: it calls `POST /api/download/<id>/retry` instead of copying the stored file. The node only retries tasks in **error** or **cancelled** state. A completed download, including a corrupt stored file, returns `409` with the node's reason. The CLI prints that and exits; it cannot delete history or cancel a completed task.

