# shelfmark-dl CLI

`shelfmark-dl` searches a Shelfmark node and optionally queues a download. It ships as a console script on the generated client package (`aiohttp` / `pydantic` only).

Flow: metadata search (ISBN or title) → release search → queue download on the node → wait until the queue is done → copy the file off the node via `GET /api/localdownload`. The CLI never reads the node's filesystem.

## Install

```bash
uvx --from "git+https://github.com/<github-username>/shelfmark.git@feature/python-client#subdirectory=generated/python" shelfmark-dl --help
uvx --from "git+https://github.com/<github-username>/shelfmark.git@feature/python-client#subdirectory=generated/python" \
  shelfmark-dl --host http://127.0.0.1:8084 --isbn --output ./downloads 9780140449136
```

Pin a commit or tag instead of `feature/python-client` when you want a frozen CLI:

```bash
uvx --from "git+https://github.com/<github-username>/shelfmark.git@<tag-or-commit-sha>#subdirectory=generated/python" shelfmark-dl --help
```

`QUERY` is positional (`ISBN` digits or title text). `--isbn` / `--title` only say how to treat it.

## `--help` groups

`shelfmark-dl --help` lists flags in four groups:

| Group | Flags |
| :--- | :--- |
| General | `-h` / `--help`, `--version`, `--host`, `-q` / `--quiet`, `-v` / `--verbose`, `--status` |
| Search | `--isbn`, `--title`, `--provider`, `--source`, `--limit` |
| Download | `-n` / `--simulate`, `-o` / `--output`, `--wait` |
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
| `-u` / `--username`, `-p` / `--password` | Login when `AUTH_METHOD` is not `none`. Prompt if `--username` is set and `--password` is omitted |

`--status` does not require `QUERY`. Every other mode does.

## Finished files

`POST /api/releases/download` queues work on the **node**. It does not stream the file to the caller. Pull bytes through `GET /api/localdownload` after the queue reports completion (`complete` / `completed` / `done` / `available`). That is the only path the CLI uses to write a file.

When `--output` is omitted, the CLI queues (unless `--simulate`) and prints status only.

When `AUTH_METHOD` is not `none`, pass `-u` / `-p` so the CLI can call `api_login_post` and reuse the cookie jar.
