"""Perl ground-truth helper (Wave 3 P1)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from tests.toolchain import require_perl_pin

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "helpers" / "perl" / "match.py"


@pytest.fixture(autouse=True)
def _perl_pin():
    require_perl_pin()


def test_perl_helper_version():
    proc = subprocess.run(
        [sys.executable, str(HELPER), "version"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr + proc.stdout
    meta = json.loads(proc.stdout)
    assert meta["ok"] is True
    assert meta["version"].startswith("5.")
    assert "pin" in meta


def test_perl_helper_parse_and_match():
    proc = subprocess.run(
        [sys.executable, str(HELPER), "parse", "a+"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert json.loads(proc.stdout)["ok"] is True

    m = subprocess.run(
        [sys.executable, str(HELPER), "match", "a+", ""],
        input="aaa",
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert m.returncode == 0
    n = subprocess.run(
        [sys.executable, str(HELPER), "match", "a+", ""],
        input="bbb",
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert n.returncode == 1


def test_perl_helper_preserves_dollar_and_at():
    """Patterns with $ / @ must not be double-interpolated by qr/$p/."""
    # End-anchor $
    m = subprocess.run(
        [sys.executable, str(HELPER), "match", r"^foo$", ""],
        input="foo",
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert m.returncode == 0, m.stderr
    n = subprocess.run(
        [sys.executable, str(HELPER), "match", r"^foo$", ""],
        input="foobar",
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert n.returncode == 1
    # Literal @ in character class / pattern
    p = subprocess.run(
        [sys.executable, str(HELPER), "parse", r"a@b"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert p.returncode == 0, p.stderr
    a = subprocess.run(
        [sys.executable, str(HELPER), "match", r"a@b", ""],
        input="a@b",
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert a.returncode == 0, a.stderr


def test_perl_match_compile_fail_exit_2():
    """Compile failures must be exit 2 (not 3 / helper-unavailable)."""
    proc = subprocess.run(
        [sys.executable, str(HELPER), "match", "(", ""],
        input="x",
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 2, proc.stderr


def test_regex_id_formula_version_gate():
    from regexproof.batch.inventory import check_corpus_coverage
    from regexproof.regex_id import REGEX_ID_FORMULA_VERSION

    assert REGEX_ID_FORMULA_VERSION == "v2-domain-optional-ascii-default"
    assert check_corpus_coverage() == []
