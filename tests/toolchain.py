"""Local-vs-CI toolchain gates (#488).

Pinned helpers (Perl 5.38.2, recheck, yara) are hard failures in CI. On a
developer or agent laptop they skip with an install hint so the rest of the
suite can still prove the change under test.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

PERL_PIN_HINT = (
    "perl helper pin 5.38.2 missing (install perl@5.38 so "
    "`python helpers/perl/match.py version` returns ok; "
    "CI still hard-fails on pin drift)"
)
RECHECK_HINT = (
    "recheck helper missing (cd helpers/redos && npm install; "
    "CI still hard-fails)"
)
YARA_HINT = (
    "yara helper missing (install yara / yara-python so "
    "`python helpers/yara/match.py version` returns ok; "
    "CI still hard-fails)"
)


def in_ci() -> bool:
    return os.environ.get("GITHUB_ACTIONS") == "true"


def _fail_or_skip(message: str) -> None:
    if in_ci():
        pytest.fail(message)
    pytest.skip(message)


def perl_pin_ok() -> tuple[bool, str]:
    helper = ROOT / "helpers" / "perl" / "match.py"
    proc = subprocess.run(
        [sys.executable, str(helper), "version"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return False, PERL_PIN_HINT + f" rc={proc.returncode} {proc.stdout.strip()}"
    try:
        meta = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return False, PERL_PIN_HINT
    if meta.get("ok") is True:
        return True, ""
    return False, PERL_PIN_HINT + f" {meta}"


def recheck_ok() -> tuple[bool, str]:
    script = ROOT / "helpers" / "redos" / "recheck.cjs"
    if not script.is_file():
        return False, RECHECK_HINT
    node = shutil.which("node")
    if node is None:
        return False, RECHECK_HINT
    proc = subprocess.run(
        [node, str(script), "a+", ""],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0 or not (proc.stdout or "").strip():
        return False, RECHECK_HINT
    return True, ""


def yara_ok() -> tuple[bool, str]:
    helper = ROOT / "helpers" / "yara" / "match.py"
    proc = subprocess.run(
        [sys.executable, str(helper), "version"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return False, YARA_HINT + f" rc={proc.returncode} {proc.stdout.strip()}"
    try:
        meta = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return False, YARA_HINT
    if meta.get("ok") is True:
        return True, ""
    return False, YARA_HINT + f" {meta}"


def require_perl_pin() -> None:
    ok, msg = perl_pin_ok()
    if not ok:
        _fail_or_skip(msg)


def require_recheck() -> None:
    ok, msg = recheck_ok()
    if not ok:
        _fail_or_skip(msg)


def require_yara() -> None:
    ok, msg = yara_ok()
    if not ok:
        _fail_or_skip(msg)
