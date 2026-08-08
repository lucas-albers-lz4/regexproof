"""Invoke argv-only ReDoS tool wrappers (no shell=True)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

HELPER_DIR = Path(__file__).resolve().parents[2] / "helpers" / "redos"


def _run_json(argv: list[str], timeout: float = 60.0) -> dict[str, Any]:
    try:
        proc = subprocess.run(
            argv,
            capture_output=True,
            text=True,
            shell=False,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return {
            "tool": argv[0],
            "tool_version": "unknown",
            "result": "timeout",
            "error_message": f"timeout after {timeout}s",
        }
    except FileNotFoundError as exc:
        return {
            "tool": argv[0],
            "tool_version": "unknown",
            "result": "error",
            "error_message": f"executable not found: {exc}",
        }
    line = (proc.stdout or "").strip().splitlines()
    if not line:
        return {
            "tool": argv[0],
            "tool_version": "unknown",
            "result": "error",
            "error_message": f"empty stdout (stderr={proc.stderr!r})",
        }
    try:
        return json.loads(line[-1])
    except json.JSONDecodeError as exc:
        return {
            "tool": argv[0],
            "tool_version": "unknown",
            "result": "error",
            "error_message": f"invalid JSON: {exc}; raw={line[-1][:200]!r}",
        }


def run_recheck(pattern: str, flags: str = "") -> dict[str, Any]:
    script = HELPER_DIR / "recheck.cjs"
    return _run_json(["node", str(script), pattern, flags])


def run_safe_regex2(pattern: str) -> dict[str, Any]:
    script = HELPER_DIR / "safe-regex2.cjs"
    return _run_json(["node", str(script), pattern])


def run_python_detector(pattern: str, flags: str = "") -> dict[str, Any]:
    script = HELPER_DIR / "vuln_regex_detector_cli.py"
    return _run_json([sys.executable, str(script), pattern, flags])
