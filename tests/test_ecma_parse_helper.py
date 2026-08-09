r"""ECMA parse helper (helpers/ecma/parse.mjs) regression tests — issue #141.

Guard 1: pre-escaped slashes must survive literal construction (the
js/incomplete-sanitization bug: `\/` became `\\/` → "Invalid flag '/'").
Guard 2: the AST walk must terminate (regexpp ASTs are cyclic via
parent/resolved back-edges — the walk stack-overflowed on every pattern).
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from regexproof.compiler import ecma as ecma_mod

HELPER_DIR = Path(__file__).resolve().parents[1] / "helpers" / "ecma"
PARSE = HELPER_DIR / "parse.mjs"
MATCH = HELPER_DIR / "match.mjs"

_HELPER_AVAILABLE = (
    shutil.which("node") is not None and (HELPER_DIR / "node_modules" / "regexpp").is_dir()
)

pytestmark = pytest.mark.skipif(
    not _HELPER_AVAILABLE, reason="node or helpers/ecma deps not installed"
)


def _parse(pattern: str, flags: str = "") -> dict:
    proc = subprocess.run(
        ["node", str(PARSE), pattern, flags],
        capture_output=True,
        text=True,
        shell=False,
        timeout=30,
        check=False,
    )
    return json.loads(proc.stdout.strip() or "{}")


def _matches(pattern: str, s: str, flags: str = "") -> bool:
    proc = subprocess.run(
        ["node", str(MATCH), pattern, flags],
        input=s,
        capture_output=True,
        text=True,
        shell=False,
        timeout=30,
        check=False,
    )
    return proc.returncode == 0


def test_escaped_slash_pattern_parses():
    r = _parse(r"\/")
    assert r.get("ok") is True
    assert r.get("helper") == "ecma-regexpp"
    assert r.get("ast_type") == "RegExpLiteral"


def test_digit_pattern_parses():
    """Guards the findReject stack-overflow (cyclic AST walk)."""
    r = _parse(r"\d+")
    assert r.get("ok") is True


def test_plain_slash_pattern_parses():
    r = _parse("a/b")
    assert r.get("ok") is True


def test_escaped_slash_roundtrip_meaning():
    r"""Real-engine replay: `\/` denotes a plain slash; `\\/` denotes backslash+slash."""
    assert _matches(r"\/", "/")
    assert not _matches(r"\/", "a")
    assert _matches(r"\\/", "\\/")
    assert not _matches(r"\\/", "/")
    assert _matches("a/b", "a/b")
    assert not _matches("a/b", "ab")


def test_reject_reasons_intact():
    assert _parse(r"(?=a)b").get("unencodable_reason") == "lookaround"
    assert _parse(r"(a)\1").get("unencodable_reason") == "backref"
    assert _parse("a+", "u").get("unencodable_reason") == "u-flag"
    assert _parse("(").get("unencodable_reason") == "parse-error"


def test_compile_ecma_word_boundary_still_encodes():
    r"""The working gate must not pre-empt the compiler's ASCII edge-\b encode
    (word-boundary wave, #67): \b is handled in the compiler, not the helper."""
    cr = ecma_mod.compile_ecma(r"\bfoo\b", "")
    assert cr.mirror is not None
    cr_mid = ecma_mod.compile_ecma(r"foo\bbar", "")
    assert cr_mid.mirror is None
    assert cr_mid.unencodable_reason == "word-boundary"
