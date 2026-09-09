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



def test_human_summary_replaces_identifier_docstrings() -> None:
    app = Flask(__name__)

    @app.route("/api/activity/dismiss", methods=["POST"])
    def api_activity_dismiss() -> str:
        """api_activity_dismiss"""
        return "ok"

    spec = build_openapi_spec(app)
    assert spec["paths"]["/api/activity/dismiss"]["post"]["summary"] == (
        "Dismiss one activity item"
    )


def test_download_release_has_json_request_body(main_module) -> None:
    spec = build_openapi_spec(main_module.app)
    body = spec["paths"]["/api/releases/download"]["post"]["requestBody"]
    props = body["content"]["application/json"]["schema"]["properties"]
    assert "source" in props
    assert "source_id" in props
    assert "title" in props

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
