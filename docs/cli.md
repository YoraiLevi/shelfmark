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

Human mode (the default) prints action lines on stderr — including a “searching releases” line *before* the slow `GET /api/releases` call — and one-line summaries of the first metadata hit and the picked release (title, provider id, format, size, source_id). It does not dump full metadata or release JSON. Pass `-v` / `--verbose` for a one-line listing of every metadata hit and every wait status change (still human mode, still on stderr). Pass `--jsonl` for one JSON object per event on stdout. `-q` / `--quiet` stays silent on simulate (no file is written). `-q` conflicts with both `-v` and `--jsonl`.

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
  shelfmark-dl --host http://127.0.0.1:8084 --isbn -o ./downloads --wait 180 9780140449136
```

- `-o ./downloads` is what turns the run into a real download; the directory must be writable by you (the CLI writes locally, not on the node).
- Default **human** mode prints progress on stderr (and a TTY spinner while waiting) so a long queue poll does not look like a hang. `-q` / `--quiet` prints only the saved path on stdout. `-v` / `--verbose` stays in human mode and adds extra stderr detail. `--jsonl` emits JSON-line events on stdout instead.
- `--wait 180` caps the poll at three minutes. Without `--wait`, `-o` implies `300`.

On success, human and quiet modes print the saved path on stdout.

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
| General | `-h` / `--help`, `--version`, `--host`, `-q` / `--quiet`, `-v` / `--verbose`, `--jsonl`, `--status` |
| Search | `--isbn`, `--title`, `--provider`, `--source`, `--limit` |
| Download | `-n` / `--simulate`, `-o` / `--output`, `--wait`, `--force-download` |
| Auth | `-u` / `--username`, `-p` / `--password` |


## Output modes

`--jsonl`, `-v` / `--verbose`, and the human/quiet UX below are local CLI changes. `uvx --from git+…@feature/python-client` still serves the last pushed branch until this lands.

| Mode | How to get it | stdout | stderr |
| :--- | :--- | :--- | :--- |
| **human** (default) | no flag | saved path only (when `-o`) | action lines, one-line hit/release summaries, TTY spinner while waiting |
| **human + verbose** | `-v` / `--verbose` | saved path only (when `-o`) | human lines plus every metadata hit, every release candidate, and every wait status change |
| **quiet** | `-q` / `--quiet` | saved path only (when `-o`); otherwise nothing | errors only |
| **jsonl** | `--jsonl` | one compact JSON object per event | errors only |

`-q` / `--quiet` cannot be combined with `-v` / `--verbose` or `--jsonl` (argparse error). `-v` is not an alias for `--jsonl`.


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
| `--force-download` | On already-queued, `POST /api/releases/download` with `force_download=true` instead of copying the stored file |
| `-u` / `--username`, `-p` / `--password` | Login when `AUTH_METHOD` is not `none`. Prompt if `--username` is set and `--password` is omitted |
| `-q` / `--quiet` | No progress; stdout is only the saved path (when `-o`). Conflicts with `-v` and `--jsonl` |
| `-v` / `--verbose` | Extra human detail on stderr (every metadata hit, every release, every wait status change). Stays in human mode; not `--jsonl`. Conflicts with `-q` |
| `--jsonl` | One JSON event per line on stdout (debug). Conflicts with `-q` |


`--status` does not require `QUERY`. Every other mode does.

## Finished files

`POST /api/releases/download` queues work on the **node**. It does not stream the file to the caller. Pull bytes through `GET /api/localdownload` after the queue reports completion (`complete` / `completed` / `done` / `available`). That is the only path the CLI uses to write a file.

When `--output` is omitted, the CLI queues (unless `--simulate`) and prints status only.

When `AUTH_METHOD` is not `none`, pass `-u` / `-p` so the CLI can call `api_login_post` and reuse the cookie jar.

`--force-download` is for an already-queued `source_id`: it calls `POST /api/releases/download` with `force_download=true` instead of copying the stored file. The node re-queues a **completed** release and asks the download client to add it again. A live download returns `409` `download_active`; the CLI then waits. Request-linked downloads stay forbidden. For torrents the client entry is removed with the data left on disk, so qBittorrent (and similar) will often recheck those files and finish without pulling new bytes. Direct-download and usenet paths do not have that recheck shortcut.

