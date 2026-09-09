#!/usr/bin/env bash
# Export OpenAPI JSON and generate the asyncio Python client.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ "${GITHUB_REF:-}" == refs/tags/v* ]]; then
  PACKAGE_VERSION="${GITHUB_REF_NAME#v}"
else
  COUNT="$(git rev-list --count HEAD)"
  SHA="$(git rev-parse --short HEAD)"
  PACKAGE_VERSION="0.1.${COUNT}+g${SHA}"
fi

if command -v uv >/dev/null 2>&1; then
  uv run python scripts/export_openapi.py
elif [[ -x "$ROOT/.venv/bin/python" ]]; then
  "$ROOT/.venv/bin/python" scripts/export_openapi.py
elif [[ -x "$ROOT/.venv/Scripts/python.exe" ]]; then
  "$ROOT/.venv/Scripts/python.exe" scripts/export_openapi.py
else
  python3 scripts/export_openapi.py
fi

GENERATOR_IMAGE="${OPENAPI_GENERATOR_IMAGE:-docker.io/openapitools/openapi-generator-cli:v7.16.0}"
if [[ -n "${CONTAINER_ENGINE:-}" ]]; then
  ENGINE="$CONTAINER_ENGINE"
elif command -v podman >/dev/null 2>&1; then
  ENGINE=podman
elif command -v podman.exe >/dev/null 2>&1; then
  ENGINE=podman.exe
elif command -v docker >/dev/null 2>&1; then
  ENGINE=docker
else
  echo "Need podman or docker to run OpenAPI Generator." >&2
  exit 1
fi
rm -rf generated/python
"$ENGINE" run --rm \
  -v "$ROOT:/local" \
  "$GENERATOR_IMAGE" generate \
  -g python \
  --library asyncio \
  -i /local/generated/openapi.json \
  -o /local/generated/python \
  --additional-properties="packageName=shelfmark_client,projectName=shelfmark-client,packageVersion=${PACKAGE_VERSION},usePyproject=true"

# Drop generator boilerplate that does not belong in this repo.
rm -rf generated/python/.github generated/python/.gitlab-ci.yml \
  generated/python/.travis.yml generated/python/git_push.sh

echo "Generated shelfmark-client ${PACKAGE_VERSION}"
