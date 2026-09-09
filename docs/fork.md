# Fork Additions

This fork keeps upstream Shelfmark behavior and adds three things:

1. A live OpenAPI 3 document at `/openapi.json` and `/api/openapi.json`.
2. A uv-installable asyncio Python client generated from that document on every build.
3. Published container images at `ghcr.io/<github-username>/shelfmark` (`IMAGE_NAME` is `${{ github.repository_owner }}/shelfmark`).

Upstream has no API catalog. The SPA catch-all used to serve HTML for `/openapi.json`. The fork registers those paths as JSON before the catch-all.

## Images

GitHub Actions workflow **Create and publish Docker images** pushes:

| Tag | When |
| :--- | :--- |
| `dev` | Push to `main` |
| `sha-<7-char>` | Every image build |
| `latest`, `1.2.3`, `v1.2.3` | Git tag `v*` |

```text
ghcr.io/<github-username>/shelfmark:dev
ghcr.io/<github-username>/shelfmark:sha-<sha>
ghcr.io/<github-username>/shelfmark-lite:dev
```

The first package publish is private until you set **Package settings → Change package visibility → Public**.

After a prune of the local Podman store, rebuild the overlay used on this workstation:

```powershell
cd C:\Users\devic\source\testing-area\https-github.com-calibrain-shelfmark
podman build -f Dockerfile.patched -t localhost/shelfmark:patched .
```

`Dockerfile.patched` copies only `openapi.py` and `main.py` onto the pinned upstream v1.3.15 digest.

## OpenAPI

Unauthenticated:

```http
GET /openapi.json
GET /api/openapi.json
```

The document is built at request time from Flask `url_map` plus route docstrings. `search_type` is not a query parameter. ISBN metadata search is `GET /api/metadata/search?query=`.

Export without a running server:

```bash
uv run python scripts/export_openapi.py
```

## Python Client

Directory `generated/python` is produced by OpenAPI Generator (`python` + `--library asyncio` + `usePyproject=true`). CI regenerates it on every relevant push to `main` and versions the package as:

- `0.1.<commit-count>+g<short-sha>` on `main`
- the tag without the leading `v` on `v*` releases

That version tracks git history and lines up with image `sha-*` / semver tags.

Regenerate locally (Podman or Docker):

```bash
bash scripts/generate-python-client.sh
```

### Install into your own uv project

```toml
# pyproject.toml
[project]
dependencies = [
  "shelfmark-client @ git+https://github.com/<github-username>/shelfmark.git@main#subdirectory=generated/python",
]
```

Or:

```bash
uv add "shelfmark-client @ git+https://github.com/<github-username>/shelfmark.git@main#subdirectory=generated/python"
```

Pin a commit or tag instead of `main` when you want a frozen client:

```bash
uv add "shelfmark-client @ git+https://github.com/<github-username>/shelfmark.git@v1.3.15#subdirectory=generated/python"
```


The package import name is `shelfmark_client`. Requires Python 3.9+ (`aiohttp`, `pydantic`).

## Search and Download Example

Flow: metadata search (ISBN or title) → release search → queue download on the Shelfmark node → wait until the queue is done → copy the file off the node.

On this workstation the node writes under `C:\Users\devic\.services\data\shelfmark\books`. You can also pull bytes through `GET /api/localdownload?id=<task-or-md5>`.

```python
import asyncio
from pathlib import Path

from shelfmark_client import ApiClient, ApiDownloadReleasePostRequest, Configuration, DefaultApi

HOST = "http://localhost:8084"
NODE_BOOKS = Path(r"C:\Users\devic\.services\data\shelfmark\books")
LOCAL_DIR = Path.home() / "Downloads" / "shelfmark"


async def search_and_fetch(*, isbn: str | None = None, title: str | None = None) -> None:
    query = isbn or title
    if not query:
        raise SystemExit("pass isbn= or title=")

    config = Configuration(host=HOST)
    async with ApiClient(config) as client:
        api = DefaultApi(client)

        books = await api.api_metadata_search_get(
            query=query,
            provider="openlibrary",
            limit=10,
        )
        # Generated return type is untyped (spec has no response schema).
        hits = (books or {}).get("books") or []
        if not hits:
            raise SystemExit(f"no metadata hits for {query!r}")
        book = hits[0]
        provider = book["provider"]
        book_id = book["provider_id"]

        releases = await api.api_releases_get(
            provider=provider,
            book_id=book_id,
            isbn=[isbn] if isbn else None,
            title=title,
            source="direct_download",
        )
        items = (releases or {}).get("releases") or []
        if not items:
            raise SystemExit("no releases (source may be blocked or unconfigured)")
        release = items[0]

        queued = await api.api_download_release_post(
            api_download_release_post_request=ApiDownloadReleasePostRequest(
                source=release.get("source") or "direct_download",
                source_id=release["source_id"],
                title=release.get("title") or book.get("title"),
                format=release.get("format"),
                extra=release.get("extra") or {},
            )
        )
        print("queued", queued)

        task_id = release["source_id"]
        for _ in range(60):
            status = await api.api_status_get()
            entry = (status or {}).get(task_id) or {}
            state = str(entry.get("status") or "")
            if state.lower() in {"complete", "completed", "done", "available"}:
                break
            await asyncio.sleep(5)

        LOCAL_DIR.mkdir(parents=True, exist_ok=True)
        copied = False
        if NODE_BOOKS.exists():
            matches = sorted(NODE_BOOKS.rglob("*"), key=lambda p: p.stat().st_mtime, reverse=True)
            files = [p for p in matches if p.is_file()]
            if files:
                dest = LOCAL_DIR / files[0].name
                dest.write_bytes(files[0].read_bytes())
                print("copied from node hostPath", dest)
                copied = True

        if not copied:
            raw = await api.api_local_download_get_without_preload_content(id=task_id)
            body = await raw.read()
            dest = LOCAL_DIR / f"{task_id}.bin"
            dest.write_bytes(body)
            print("copied via /api/localdownload", dest)


if __name__ == "__main__":
    # ISBN general search (not a strict ISBN operator).
    asyncio.run(search_and_fetch(isbn="9780140449136"))
    # Title search:
    # asyncio.run(search_and_fetch(title="Crime and Punishment"))
```

`api_download_release_post` queues work on the **node**. It does not stream the file to the caller. Copy from `data/shelfmark/books` or `/api/localdownload` after the queue reports completion.

When `AUTH_METHOD` is not `none`, call `api_login_post` first and reuse the `ApiClient` cookie jar.

## Every HTTP Endpoint

Live list: `GET /openapi.json`. Client method names are the `operationId` values below.

### Spec and health

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/openapi.json` | `openapi_json_get` | OpenAPI 3 JSON, no auth |
| GET | `/api/openapi.json` | `api_openapi_json_get` | Same document |
| GET | `/api/health` | `api_health_get` | Orchestrator health, no auth |

### Auth

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/auth/check` | `api_auth_check_get` | Session and `auth_mode` |
| POST | `/api/auth/login` | `api_login_post` | Username/password session |
| POST | `/api/auth/logout` | `api_logout_post` | Clear session |
| GET | `/api/auth/oidc/login` | `oidc_login_get` | Start OIDC |
| GET | `/api/auth/oidc/callback` | `oidc_callback_get` | OIDC return |

### Metadata search

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/metadata/providers` | `api_metadata_providers_get` | Enabled providers |
| GET | `/api/metadata/config` | `api_metadata_config_get` | Search UI config for this session |
| GET | `/api/metadata/field-options` | `api_metadata_field_options_get` | Dynamic field options |
| GET | `/api/metadata/search` | `api_metadata_search_get` | Catalog search (`query` is general text; pass an ISBN or title here) |
| GET | `/api/metadata/book/{provider}/{book_id}` | `api_metadata_book_get` | One book from a provider |
| GET | `/api/metadata/book/{provider}/{book_id}/targets` | `api_metadata_book_targets_get` | Provider lists/shelves |
| PUT | `/api/metadata/book/{provider}/{book_id}/targets` | `api_metadata_book_targets_update_put` | Set list/shelf membership |
| POST | `/api/metadata/book/{provider}/targets/batch` | `api_metadata_book_targets_batch_post` | Targets for many books |

### Releases and files

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/release-sources` | `api_release_sources_get` | Source plugins (`direct_download`, …) |
| GET | `/api/release-sources/{source_name}/records/{record_id}` | `api_release_source_record_get` | Source-native record |
| GET | `/api/releases` | `api_releases_get` | File/release search; `isbn=` browse filter |
| POST | `/api/releases/download` | `api_download_release_post` | Queue a release on the node |
| POST | `/api/releases/inspect` | `api_inspect_release_post` | Inspect a release before queueing |
| GET | `/api/localdownload` | `api_local_download_get` | Stream a finished file to the caller |
| GET | `/api/covers/{cover_id}` | `api_cover_get` | Cached cover proxy |

### Queue and downloads

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/status` | `api_status_get` | Queue map keyed by task id |
| GET | `/api/downloads/active` | `api_active_downloads_get` | In-flight downloads |
| GET | `/api/queue/order` | `api_queue_order_get` | Display order |
| POST | `/api/queue/reorder` | `api_queue_reorder_post` | Bulk priority |
| PUT | `/api/queue/{book_id}/priority` | `api_queue_priority_put` | One item priority |
| POST | `/api/download/{book_id}/retry` | `api_retry_download_post` | Retry failed |
| DELETE | `/api/download/{book_id}/cancel` | `api_cancel_download_delete` | Cancel |

### Activity

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/activity/snapshot` | `api_activity_snapshot_get` | Current activity |
| GET | `/api/activity/history` | `api_activity_history_get` | History |
| DELETE | `/api/activity/history` | `api_activity_history_clear_delete` | Clear history |
| POST | `/api/activity/dismiss` | `api_activity_dismiss_post` | Dismiss one |
| POST | `/api/activity/dismiss-many` | `api_activity_dismiss_many_post` | Dismiss many |

### Requests (multi-user)

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/request-policy` | `api_request_policy_get` | Policy for current user |
| GET | `/api/requests` | `api_list_requests_get` | Own requests |
| POST | `/api/requests` | `api_create_request_post` | Submit one |
| POST | `/api/requests/batch` | `api_create_requests_batch_post` | Submit many |
| DELETE | `/api/requests/{request_id}` | `api_cancel_request_delete` | Cancel own |
| GET | `/api/admin/requests` | `api_admin_list_requests_get` | Admin list |
| GET | `/api/admin/requests/count` | `api_admin_request_counts_get` | Admin counts |
| POST | `/api/admin/requests/{request_id}/fulfil` | `api_admin_fulfil_request_post` | Fulfil |
| POST | `/api/admin/requests/{request_id}/reject` | `api_admin_reject_request_post` | Reject |

### Settings and onboarding

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/config` | `api_config_get` | Frontend config blob |
| GET | `/api/settings` | `api_settings_get_all_get` | All settings tabs |
| GET | `/api/settings/{tab_name}` | `api_settings_get_tab_get` | One tab |
| PUT | `/api/settings/{tab_name}` | `api_settings_update_tab_put` | Save tab |
| POST | `/api/settings/{tab_name}/action/{action_key}` | `api_settings_execute_action_post` | Test connection, etc. |
| GET | `/api/onboarding` | `api_onboarding_get_get` | Onboarding form |
| POST | `/api/onboarding` | `api_onboarding_save_post` | Complete onboarding |
| POST | `/api/onboarding/skip` | `api_onboarding_skip_post` | Skip |

### Users

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| PUT | `/api/users/me` | `users_me_update_put` | Update current user |
| GET | `/api/users/me/edit-context` | `users_me_edit_context_get` | Edit form context |
| POST | `/api/users/me/notification-preferences/test` | `users_me_test_notification_preferences_post` | Test own notifications |
| GET | `/api/admin/users` | `admin_list_users_get` | List users |
| POST | `/api/admin/users` | `admin_create_user_post` | Create user |
| GET | `/api/admin/users/{user_id}` | `admin_get_user_get` | Get user |
| PUT | `/api/admin/users/{user_id}` | `admin_update_user_put` | Update user |
| DELETE | `/api/admin/users/{user_id}` | `admin_delete_user_delete` | Delete user |
| GET | `/api/admin/users/{user_id}/delivery-preferences` | `admin_get_delivery_preferences_get` | Delivery prefs |
| GET | `/api/admin/users/{user_id}/search-preferences` | `admin_get_search_preferences_get` | Search prefs |
| GET | `/api/admin/users/{user_id}/notification-preferences` | `admin_get_notification_preferences_get` | Notification prefs |
| POST | `/api/admin/users/{user_id}/notification-preferences/test` | `admin_test_notification_preferences_post` | Test that user's notifications |
| GET | `/api/admin/users/{user_id}/effective-settings` | `admin_get_effective_settings_get` | Merged settings |
| GET | `/api/admin/download-defaults` | `admin_download_defaults_get` | Default download dest |
| GET | `/api/admin/booklore-options` | `admin_booklore_options_get` | Booklore libraries |
| GET | `/api/admin/settings/overrides-summary` | `admin_settings_overrides_summary_get` | Override summary |
| POST | `/api/admin/users/sync-cwa` | `admin_sync_cwa_users_post` | Sync Calibre-Web users |

UI hash links (`/#search_by=isbn&q=…`) are not HTTP API. See [url-search-parameters.md](url-search-parameters.md).
