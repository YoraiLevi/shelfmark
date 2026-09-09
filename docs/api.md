# HTTP API

Shelfmark has no separately published OpenAPI catalog. The live description is generated from Flask routes on the running app.

## Spec Endpoints

Both URLs return the same OpenAPI 3.0 JSON. They do not require authentication.

```text
GET /openapi.json
GET /api/openapi.json
```

Example:

```bash
curl -sS http://localhost:8084/openapi.json
```

Most other `/api/*` routes use `login_required` when `AUTH_METHOD` is not `none`. Check `GET /api/auth/check` for the current mode.

## ISBN Search

Metadata (catalog) lookup. `query` is a general text search; `search_type` is not a query parameter:

```http
GET /api/metadata/search?query=9780747532699&provider=openlibrary&limit=10
```

UI deep link (browser hash only, not sent to the server):

```text
http://localhost:8084/#search_by=isbn&q=9780747532699
```

Release (file) search against a source:

```http
GET /api/releases?source=direct_download&query=9780747532699&isbn=9780747532699
```

Confirm source names with `GET /api/release-sources` and providers with `GET /api/metadata/providers`.
