"""Rebuild and verify only the independently generated public demo."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> None:
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)


def main() -> None:
    run("scripts/export_v3_contracts.py")
    run("scripts/export_v31_contracts.py")
    run("scripts/export_v311_wallet_surface.py")
    run("scripts/export_v32_contracts.py")
    run("scripts/export_v32_workbench_fixture.py")
    run("-m", "pytest", "-q", "tests")
    manifest = json.loads(
        (ROOT / "public-mirror-manifest.json").read_text(encoding="utf-8")
    )
    if manifest["status"] != "PASS":
        raise SystemExit("public mirror manifest is not PASS")
    shutil.rmtree(ROOT / "outputs", ignore_errors=True)
    print(json.dumps({
        "status": "PASS", "version": "3.2.0-safe", "cells": 100,
        "promotion_mode": "SYNTHETIC_REHEARSAL",
    }, indent=2))


if __name__ == "__main__":
    main()
