"""Write generated/openapi.json from the live Flask route map."""

from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def _prepare_test_env() -> None:
    """Point Shelfmark at temp dirs so importing main.py does not touch /config."""
    os.environ.setdefault("RELEASE_VERSION", "1.3.15")
    temp_base = tempfile.mkdtemp(prefix="shelfmark_openapi_")
    os.environ.setdefault("LOG_ROOT", temp_base)
    os.environ.setdefault("CONFIG_DIR", str(Path(temp_base) / "config"))
    os.environ.setdefault("INGEST_DIR", str(Path(temp_base) / "ingest"))
    os.environ.setdefault("TMP_DIR", str(Path(temp_base) / "tmp"))
    Path(os.environ["LOG_ROOT"], "shelfmark").mkdir(parents=True, exist_ok=True)
    Path(os.environ["CONFIG_DIR"]).mkdir(parents=True, exist_ok=True)
    Path(os.environ["INGEST_DIR"]).mkdir(parents=True, exist_ok=True)
    Path(os.environ["TMP_DIR"]).mkdir(parents=True, exist_ok=True)


def main() -> int:
    """Export the OpenAPI document next to the generated Python client."""
    _prepare_test_env()
    sys.path.insert(0, str(ROOT))
    with patch("shelfmark.download.orchestrator.start"), patch("shelfmark.download.warmup.start"):
        import shelfmark.main as shelfmark_main
        from shelfmark.core.openapi import build_openapi_spec

        spec = build_openapi_spec(shelfmark_main.app)

    out = ROOT / "generated" / "openapi.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(spec, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size} bytes, {len(spec.get('paths', {}))} paths)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
