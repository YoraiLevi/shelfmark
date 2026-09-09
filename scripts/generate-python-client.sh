#!/usr/bin/env bash
# Export OpenAPI JSON and generate the asyncio Python client.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

run_python() {
  if command -v uv >/dev/null 2>&1; then
    uv run python "$@"
  elif command -v python3 >/dev/null 2>&1; then
    python3 "$@"
  else
    python "$@"
  fi
}

origin_owner_repo() {
  if [[ -n "${GITHUB_REPOSITORY:-}" ]]; then
    printf '%s\n' "${GITHUB_REPOSITORY%/*}" "${GITHUB_REPOSITORY#*/}"
    return
  fi
  local origin
  origin="$(git remote get-url origin 2>/dev/null || true)"
  origin="${origin%.git}"
  origin="${origin%/}"
  local repo="${origin##*/}"
  local owner="${origin%/*}"
  owner="${owner##*/}"
  owner="${owner##*:}"
  printf '%s\n' "$owner" "$repo"
}

GIT_USER_ID="$(origin_owner_repo | awk 'NR==1' | tr -d '\r')"
GIT_REPO_ID="$(origin_owner_repo | awk 'NR==2' | tr -d '\r')"
GIT_REPO_ID="${GIT_REPO_ID:-shelfmark}"

run_python scripts/export_openapi.py

SPEC_VERSION="$(run_python -c "import json; print(json.load(open('generated/openapi.json', encoding='utf-8'))['info']['version'].lstrip('v'))" | tr -d '\r')"
if [[ "${GITHUB_REF:-}" == refs/tags/v* ]]; then
  PACKAGE_VERSION="${GITHUB_REF_NAME#v}"
else
  SHA="$(git rev-parse --short HEAD | tr -d '\r')"
  PACKAGE_VERSION="${SPEC_VERSION}+g${SHA}"
fi

GENERATOR_IMAGE="${OPENAPI_GENERATOR_IMAGE:-docker.io/openapitools/openapi-generator-cli:v7.16.0}"
RUNTIME="${CONTAINER_RUNTIME:-}"
if [[ -z "$RUNTIME" ]]; then
  if command -v docker >/dev/null 2>&1 && docker info >/dev/null 2>&1; then
    RUNTIME=docker
  else
    RUNTIME=podman
  fi
fi

rm -rf generated/python
"$RUNTIME" run --rm \
  -v "$ROOT:/local" \
  "$GENERATOR_IMAGE" generate \
  -g python \
  --library asyncio \
  -i /local/generated/openapi.json \
  -o /local/generated/python \
  --git-user-id "$GIT_USER_ID" \
  --git-repo-id "$GIT_REPO_ID" \
  --additional-properties="packageName=shelfmark_client,projectName=shelfmark-client,packageVersion=${PACKAGE_VERSION},usePyproject=true"

rm -rf generated/python/.github generated/python/.gitlab-ci.yml \
  generated/python/.travis.yml generated/python/git_push.sh

echo "Generated shelfmark-client ${PACKAGE_VERSION} (git ${GIT_USER_ID}/${GIT_REPO_ID})"
