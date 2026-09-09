"""Copy shelfmark-dl into a generated client tree and register the console script.

OpenAPI Generator overwrites generated/python. Call this after generate so
`uvx --from ...#subdirectory=generated/python shelfmark-dl` keeps working.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI_SRC = ROOT / "cli" / "shelfmark_dl"
SCRIPTS_BLOCK = '[project.scripts]\nshelfmark-dl = "shelfmark_dl.__main__:main"\n'
SETUP_ENTRY = (
    '    entry_points={\n'
    '        "console_scripts": [\n'
    '            "shelfmark-dl=shelfmark_dl.__main__:main",\n'
    '        ],\n'
    '    },\n'
)


def _inject_pyproject(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if "shelfmark-dl" in text:
        return
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n" + SCRIPTS_BLOCK, encoding="utf-8")


def _inject_setup(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if "shelfmark-dl=" in text:
        return
    needle = "    include_package_data=True,\n"
    if needle not in text:
        raise SystemExit(f"Could not find inject point in {path}")
    path.write_text(text.replace(needle, needle + SETUP_ENTRY, 1), encoding="utf-8")


def main(argv: list[str]) -> int:
    dest = Path(argv[1] if len(argv) > 1 else ROOT / "generated" / "python")
    if not CLI_SRC.is_dir():
        raise SystemExit(f"Missing CLI source {CLI_SRC}")
    target = dest / "shelfmark_dl"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(CLI_SRC, target)
    _inject_pyproject(dest / "pyproject.toml")
    setup_py = dest / "setup.py"
    if setup_py.exists():
        _inject_setup(setup_py)
    print(f"Installed shelfmark-dl into {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
