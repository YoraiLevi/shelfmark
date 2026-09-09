"""Print a markdown catalog of every path+method in generated/openapi.json."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "generated" / "openapi.json"

GROUPS: list[tuple[str, tuple[str, ...]]] = [
    ("Spec and health", ("/openapi.json", "/api/openapi.json", "/api/health")),
    ("Auth", ("/api/auth",)),
    ("Metadata search", ("/api/metadata",)),
    ("Releases and files", ("/api/release", "/api/localdownload", "/api/covers")),
    ("Queue and downloads", ("/api/status", "/api/download", "/api/queue")),
    ("Activity", ("/api/activity",)),
    ("Requests (multi-user)", ("/api/request",)),
    ("Settings and onboarding", ("/api/config", "/api/settings", "/api/onboarding")),
    ("Users", ("/api/users", "/api/admin")),
]


def _group_for(path: str) -> str:
    for title, prefixes in GROUPS:
        if any(path == prefix or path.startswith(prefix) for prefix in prefixes):
            return title
    return "Other"


def main() -> int:
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    rows: list[tuple[str, str, str, str, str]] = []
    identifier_only = 0
    for path, methods in spec["paths"].items():
        for method, operation in methods.items():
            if method not in {"get", "post", "put", "patch", "delete"}:
                continue
            op_id = str(operation.get("operationId") or "")
            summary = str(operation.get("summary") or op_id)
            if summary.replace("_", "").isalnum() and " " not in summary:
                identifier_only += 1
            rows.append((path, method.upper(), op_id, summary, _group_for(path)))
    rows.sort(key=lambda item: (item[4], item[0], item[1]))
    grouped: dict[str, list[tuple[str, str, str, str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row[4]].append(row)

    print(f"<!-- catalog: {len(rows)} method/path pairs, {len(spec['paths'])} paths -->")
    if identifier_only:
        print(f"<!-- warning: {identifier_only} summaries are still identifier-only -->")
    for title, _prefixes in GROUPS:
        section = grouped.get(title)
        if not section:
            continue
        print(f"### {title}")
        print()
        print("| Method | Path | operationId | Use |")
        print("| :--- | :--- | :--- | :--- |")
        for path, method, op_id, summary, _group in section:
            print(f"| {method} | `{path}` | `{op_id}` | {summary} |")
        print()
    other = grouped.get("Other")
    if other:
        print("### Other")
        print()
        print("| Method | Path | operationId | Use |")
        print("| :--- | :--- | :--- | :--- |")
        for path, method, op_id, summary, _group in other:
            print(f"| {method} | `{path}` | `{op_id}` | {summary} |")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
