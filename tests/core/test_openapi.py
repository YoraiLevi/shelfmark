"""OpenAPI spec generation and public endpoint tests."""

from __future__ import annotations

import importlib
from unittest.mock import patch

import pytest
from flask import Flask

from shelfmark.core.openapi import (
    build_openapi_spec,
    flask_rule_to_openapi_path,
    query_parameters_from_docstring,
    register_openapi_routes,
    request_body_from_docstring,
)


def test_flask_rule_to_openapi_path_converts_converters() -> None:
    assert flask_rule_to_openapi_path("/api/download/<path:book_id>/retry") == (
        "/api/download/{book_id}/retry"
    )
    assert flask_rule_to_openapi_path("/api/admin/users/<int:user_id>") == (
        "/api/admin/users/{user_id}"
    )


def test_query_parameters_from_docstring_marks_required() -> None:
    doc = """Search books.

    Query Parameters:
        query (str): Search query (required)
        limit (int): Maximum number of results (default: 40)
        source (str): Release source to search (optional, default: all)

    Returns:
        flask.Response: JSON.
    """
    params = {item["name"]: item for item in query_parameters_from_docstring(doc)}
    assert params["query"]["required"] is True
    assert params["query"]["schema"]["type"] == "string"
    assert params["limit"]["required"] is False
    assert params["limit"]["schema"]["type"] == "integer"
    assert params["source"]["required"] is False


def test_build_openapi_spec_includes_api_routes_only() -> None:
    app = Flask(__name__)

    @app.route("/api/health", methods=["GET"])
    def health() -> str:
        """Health check endpoint for container orchestration."""
        return "ok"

    @app.route("/secret-ui")
    def ui() -> str:
        return "nope"

    register_openapi_routes(app)
    spec = build_openapi_spec(app)
    assert spec["openapi"] == "3.0.3"
    assert "/api/health" in spec["paths"]
    assert "get" in spec["paths"]["/api/health"]
    assert "/secret-ui" not in spec["paths"]
    assert "/openapi.json" in spec["paths"]
    assert "/api/openapi.json" in spec["paths"]


def test_request_body_from_docstring_marks_optional_fields() -> None:
    doc = """Login.

    Request Body (JSON):
        username (str): Username
        password (str): Password
        remember_me (bool, optional): Extend the session
    """
    body = request_body_from_docstring(doc)
    assert body is not None
    schema = body["content"]["application/json"]["schema"]
    assert schema["required"] == ["username", "password"]
    assert schema["properties"]["remember_me"]["type"] == "boolean"
    list_doc = """Batch.

    Request Body (JSON):
        requests (list): Request objects (required)
    """
    list_schema = request_body_from_docstring(list_doc)["content"]["application/json"]["schema"]
    assert list_schema["properties"]["requests"]["type"] == "array"
    assert "items" in list_schema["properties"]["requests"]
    prose = request_body_from_docstring(
        """Update settings.

    Request Body:
        JSON object with setting keys and values to update.
    """
    )
    assert prose is not None
    assert prose["content"]["application/json"]["schema"]["additionalProperties"] is True


def test_operation_summary_uses_handler_docstring() -> None:
    app = Flask(__name__)

    @app.route("/api/activity/dismiss", methods=["POST"])
    def api_activity_dismiss() -> str:
        """Dismiss one activity item."""
        return "ok"

    spec = build_openapi_spec(app)
    assert spec["paths"]["/api/activity/dismiss"]["post"]["summary"] == (
        "Dismiss one activity item."
    )


def test_download_and_login_have_json_request_bodies(main_module) -> None:
    spec = build_openapi_spec(main_module.app)
    download = spec["paths"]["/api/releases/download"]["post"]["requestBody"]
    schema = download["content"]["application/json"]["schema"]
    props = schema["properties"]
    assert schema["required"] == ["source", "source_id"]
    assert "source" in props
    assert "source_id" in props
    assert "title" in props
    assert "force_download" in props
    assert props["force_download"]["type"] == "boolean"
    assert "force_download" not in schema["required"]
    login = spec["paths"]["/api/auth/login"]["post"]["requestBody"]
    login_schema = login["content"]["application/json"]["schema"]
    login_props = login_schema["properties"]
    assert "username" in login_props
    assert "password" in login_props
    assert login_schema["required"] == ["username", "password"]
    requests_body = spec["paths"]["/api/requests"]["post"]["requestBody"]
    assert "book_data" in requests_body["content"]["application/json"]["schema"]["properties"]
    settings = spec["paths"]["/api/settings/{tab_name}"]["put"]["requestBody"]
    assert settings["content"]["application/json"]["schema"]["additionalProperties"] is True


@pytest.fixture(scope="module")
def main_module():
    """Import `shelfmark.main` with background startup disabled."""
    with patch("shelfmark.download.orchestrator.start"):
        import shelfmark.main as main

        importlib.reload(main)
        return main


def test_openapi_json_is_public_even_when_auth_is_required(main_module) -> None:
    client = main_module.app.test_client()
    with patch.object(main_module, "get_auth_mode", return_value="builtin"):
        response = client.get("/openapi.json")
        aliased = client.get("/api/openapi.json")

    assert response.status_code == 200
    assert response.content_type.startswith("application/json")
    spec = response.get_json()
    assert spec["info"]["title"] == "Shelfmark API"
    assert "/api/health" in spec["paths"]
    assert "/api/metadata/search" in spec["paths"]
    assert "/api/releases" in spec["paths"]
    isbn_names = {p["name"] for p in spec["paths"]["/api/releases"]["get"]["parameters"]}
    assert "isbn" in isbn_names
    assert aliased.status_code == 200
    assert aliased.get_json()["paths"].keys() == spec["paths"].keys()
