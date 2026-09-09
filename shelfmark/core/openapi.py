"""Build an OpenAPI 3 document from the live Flask route map."""

from __future__ import annotations

import inspect
import os
import re
from typing import Any

from flask import Flask, Response, jsonify

OPENAPI_PATHS: tuple[str, ...] = ("/openapi.json", "/api/openapi.json")

_CONVERTER = re.compile(r"<(?:(?P<type>string|int|path|float|uuid):)?(?P<name>[^>]+)>")
_QUERY_LINE = re.compile(
    r"^\s+(?P<name>[A-Za-z_][\w-]*)\s*(?:\((?P<type>[^)]+)\))?:\s+(?P<desc>.+)$",
    re.MULTILINE,
)
_PYTHON_TO_OPENAPI = {
    "str": "string",
    "int": "integer",
    "float": "number",
    "bool": "boolean",
    "string": "string",
    "integer": "integer",
    "number": "number",
    "boolean": "boolean",
}
_CONVERTER_TO_OPENAPI = {
    "int": "integer",
    "float": "number",
    "path": "string",
    "string": "string",
    "uuid": "string",
}

# Query parameters that exist in the handlers but are missing from docstrings.
_EXTRA_QUERY_PARAMETERS: dict[str, list[dict[str, Any]]] = {
    "/api/metadata/search": [
        {
            "name": "provider",
            "in": "query",
            "required": False,
            "schema": {"type": "string"},
            "description": "Metadata provider name (openlibrary, hardcover, googlebooks, moly).",
        },
        {
            "name": "page",
            "in": "query",
            "required": False,
            "schema": {"type": "integer", "minimum": 1, "default": 1},
            "description": "Result page (1-based).",
        },
        {
            "name": "content_type",
            "in": "query",
            "required": False,
            "schema": {"type": "string", "default": "ebook"},
            "description": "ebook, audiobook, or combined.",
        },
    ],
    "/api/releases": [
        {
            "name": "query",
            "in": "query",
            "required": False,
            "schema": {"type": "string"},
            "description": "Browse/manual query text. With source=, used instead of provider+book_id.",
        },
        {
            "name": "isbn",
            "in": "query",
            "required": False,
            "schema": {"type": "array", "items": {"type": "string"}},
            "style": "form",
            "explode": True,
            "description": "ISBN-10 or ISBN-13 filter. Repeat the parameter for multiple values.",
        },
        {
            "name": "title",
            "in": "query",
            "required": False,
            "schema": {"type": "string"},
            "description": "Title override or browse title filter.",
        },
        {
            "name": "author",
            "in": "query",
            "required": False,
            "schema": {"type": "string"},
            "description": "Author override or browse author filter.",
        },
        {
            "name": "content_type",
            "in": "query",
            "required": False,
            "schema": {"type": "string", "default": "ebook"},
        },
        {
            "name": "expand_search",
            "in": "query",
            "required": False,
            "schema": {"type": "boolean", "default": False},
            "description": "Skip ISBN-first matching and search by title/author.",
        },
        {
            "name": "languages",
            "in": "query",
            "required": False,
            "schema": {"type": "string"},
            "description": "Comma-separated ISO 639-1 language codes.",
        },
        {
            "name": "manual_query",
            "in": "query",
            "required": False,
            "schema": {"type": "string"},
        },
        {
            "name": "indexers",
            "in": "query",
            "required": False,
            "schema": {"type": "string"},
            "description": "Comma-separated Prowlarr indexer names.",
        },
    ],
}

_REQUEST_BODIES: dict[tuple[str, str], dict[str, Any]] = {
    ("/api/releases/download", "post"): {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "required": ["source", "source_id"],
                    "properties": {
                        "source": {"type": "string", "description": "Release source name."},
                        "source_id": {
                            "type": "string",
                            "description": "ID within the source, such as an MD5.",
                        },
                        "title": {"type": "string"},
                        "format": {"type": "string"},
                        "size": {"type": "string"},
                        "extra": {"type": "object"},
                        "priority": {"type": "integer", "default": 0},
                    },
                }
            }
        },
    },
}


def flask_rule_to_openapi_path(rule: str) -> str:
    """Convert a Flask URL rule to an OpenAPI path template."""
    return _CONVERTER.sub(r"{\g<name>}", rule)


def _path_parameters(rule: str) -> list[dict[str, Any]]:
    parameters: list[dict[str, Any]] = []
    for match in _CONVERTER.finditer(rule):
        converter = match.group("type") or "string"
        parameters.append(
            {
                "name": match.group("name"),
                "in": "path",
                "required": True,
                "schema": {"type": _CONVERTER_TO_OPENAPI.get(converter, "string")},
            }
        )
    return parameters


def query_parameters_from_docstring(doc: str) -> list[dict[str, Any]]:
    """Parse a Google-style Query Parameters section into OpenAPI parameters."""
    marker = "Query Parameters:"
    if marker not in doc:
        return []
    section = doc.split(marker, 1)[1]
    if "\n    Returns:" in section:
        section = section.split("\n    Returns:", 1)[0]
    elif "\nReturns:" in section:
        section = section.split("\nReturns:", 1)[0]

    parameters: list[dict[str, Any]] = []
    for match in _QUERY_LINE.finditer(section):
        name = match.group("name")
        if name.startswith("["):
            continue
        raw_type = (match.group("type") or "string").strip().lower()
        description = match.group("desc").strip()
        lowered = description.lower()
        required = "required" in lowered and "optional" not in lowered
        parameters.append(
            {
                "name": name,
                "in": "query",
                "required": required,
                "schema": {"type": _PYTHON_TO_OPENAPI.get(raw_type, "string")},
                "description": description,
            }
        )
    return parameters


def _merge_parameters(*groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[tuple[str, str], dict[str, Any]] = {}
    for group in groups:
        for parameter in group:
            merged[(parameter["name"], parameter["in"])] = parameter
    return list(merged.values())


def _should_include_rule(rule: str) -> bool:
    if rule in OPENAPI_PATHS:
        return True
    return rule.startswith("/api/")


_ENDPOINT_SUMMARIES: dict[str, str] = {
    "api_activity_dismiss": "Dismiss one activity item",
    "api_activity_dismiss_many": "Dismiss many activity items",
    "api_activity_history": "List activity history",
    "api_activity_history_clear": "Clear activity history",
    "api_activity_snapshot": "Current activity snapshot",
    "admin_booklore_options": "List Booklore libraries for admin settings",
    "admin_download_defaults": "Default download destination for new users",
    "api_admin_list_requests": "Admin list of book requests",
    "api_admin_request_counts": "Admin counts of pending book requests",
    "admin_settings_overrides_summary": "Summary of per-user settings overrides",
    "admin_get_delivery_preferences": "Delivery preferences for one user",
    "admin_get_effective_settings": "Merged settings for one user",
    "admin_get_notification_preferences": "Notification preferences for one user",
    "admin_get_search_preferences": "Search preferences for one user",
    "admin_test_notification_preferences": "Send a test notification for one user",
    "api_request_policy": "Request policy for the current user",
    "api_list_requests": "List the current user's book requests",
    "api_create_request": "Submit a book request",
    "api_create_requests_batch": "Submit many book requests",
    "api_cancel_request": "Cancel one of the current user's requests",
    "api_inspect_release": "Inspect a release before queueing a download",
    "users_me_edit_context": "Edit-form context for the current user",
    "users_me_test_notification_preferences": "Send a test notification to the current user",
    "users_me_update": "Update the current user",
    "api_admin_fulfil_request": "Fulfil a book request",
    "api_admin_reject_request": "Reject a book request",
}


def _human_summary(endpoint: str, doc: str) -> str:
    """Prefer a real sentence over a bare function name."""
    first = doc.split("\n", 1)[0].strip() if doc else ""
    if first and " " in first:
        return first
    return _ENDPOINT_SUMMARIES.get(endpoint, first or endpoint)


def build_openapi_spec(app: Flask) -> dict[str, Any]:
    """Return an OpenAPI 3.0 document covering HTTP API routes."""
    paths: dict[str, Any] = {}
    for rule in app.url_map.iter_rules():
        if not _should_include_rule(rule.rule):
            continue
        methods = sorted((rule.methods or set()) - {"HEAD", "OPTIONS"})
        if not methods:
            continue

        view = app.view_functions.get(rule.endpoint)
        doc = inspect.getdoc(view) or ""
        summary = _human_summary(rule.endpoint, doc)
        openapi_path = flask_rule_to_openapi_path(rule.rule)
        parameters = _merge_parameters(
            _path_parameters(rule.rule),
            query_parameters_from_docstring(doc),
            _EXTRA_QUERY_PARAMETERS.get(rule.rule, []),
        )
        item = paths.setdefault(openapi_path, {})
        for method in methods:
            operation: dict[str, Any] = {
                "operationId": f"{rule.endpoint}_{method.lower()}".replace(".", "_"),
                "summary": summary,
                "description": doc,
                "parameters": parameters,
                "responses": {
                    "200": {"description": "Success"},
                    "400": {"description": "Bad request"},
                    "401": {"description": "Authentication required when AUTH_METHOD is not none"},
                    "404": {"description": "Not found"},
                },
            }
            request_body = _REQUEST_BODIES.get((rule.rule, method.lower()))
            if request_body is not None:
                operation["requestBody"] = request_body
            item[method.lower()] = operation

    version = os.environ.get("RELEASE_VERSION") or os.environ.get("BUILD_VERSION") or "0.1.0"
    return {
        "openapi": "3.0.3",
        "info": {
            "title": "Shelfmark API",
            "version": version,
            "description": (
                "HTTP API for the running Shelfmark instance. Generated from Flask routes. "
                "There is no separate published spec. GET /openapi.json and GET /api/openapi.json "
                "are unauthenticated. Most other /api/* routes use login_required when "
                "authentication is enabled. ISBN metadata search is GET /api/metadata/search?query=; "
                "the handler does not accept search_type. ISBN file search is GET /api/releases "
                "with isbn= and source=direct_download."
            ),
        },
        "servers": [{"url": "/"}],
        "paths": paths,
    }


def register_openapi_routes(app: Flask) -> None:
    """Expose the generated spec at /openapi.json and /api/openapi.json."""

    def openapi_json() -> Response:
        """OpenAPI 3 description of the live HTTP API.

        No authentication required.
        """
        return jsonify(build_openapi_spec(app))

    openapi_json.__name__ = "openapi_json"
    app.add_url_rule(
        "/openapi.json",
        endpoint="openapi_json",
        view_func=openapi_json,
        methods=["GET"],
    )
    app.add_url_rule(
        "/api/openapi.json",
        endpoint="api_openapi_json",
        view_func=openapi_json,
        methods=["GET"],
    )
