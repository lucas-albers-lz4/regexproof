"""Unit tests for ``strip_verbose_x`` (Wave 3 / #114)."""

from __future__ import annotations

import pytest

from regexproof.compiler.re2 import compile_re2, parse_with_helper
from regexproof.compiler.xflag_strip import strip_verbose_x


def test_class_hash_stays_literal():
    stripped, lifted = strip_verbose_x(r"(?x)a[ #]b")
    assert stripped == "a[ #]b"
    assert "x" in lifted


def test_mid_pattern_disable_x():
    stripped, lifted = strip_verbose_x(r"(?x)a b(?-x) c d")
    # With x on: "a b" → "ab"; after (?-x) spaces are literal.
    assert stripped == "ab c d"
    # Net-on flags: x was disabled → not reported.
    assert "x" not in lifted


def test_disable_i_not_reported_as_compile_flag():
    stripped, lifted = strip_verbose_x(r"(?i)foo(?-i)bar")
    assert stripped == "foobar"
    assert "i" not in lifted


def test_combined_xi_consumed():
    stripped, lifted = strip_verbose_x(r"(?xi) a b")
    assert stripped == "ab"
    assert lifted == "ix"
    assert "(?x" not in stripped
    assert "(?i" not in stripped


def test_hash_comment_to_eol_outside_class():
    stripped, _ = strip_verbose_x("(?x)a b  # comment\nc d")
    assert stripped == "abcd"


def test_paren_comment_stripped():
    stripped, _ = strip_verbose_x(r"(?x)a(?# client ID )b")
    assert stripped == "ab"
    assert "(?#" not in stripped


def test_no_residual_x_group():
    stripped, lifted = strip_verbose_x(r"(?x)(?i)\bfoo\b")
    assert "(?" not in stripped or "(?:" in stripped or "(?=" in stripped
    assert "(?x" not in stripped
    assert "x" in lifted
    assert "i" in lifted
    assert stripped == r"\bfoo\b"


def test_go_re2_parse_stripped_form():
    raw = "(?x) a b"
    stripped, _ = strip_verbose_x(raw)
    assert stripped == "ab"
    gate = parse_with_helper(stripped)
    if gate.get("helper") == "go-missing":
        pytest.skip("go-re2 helper missing")
    assert gate.get("ok") is True


def test_mutation_unstripped_fails_go_re2_or_compile():
    """Deliberately-unstripped ``(?x) a b`` must not silently encode."""
    raw = "(?x) a b"
    gate = parse_with_helper(raw)
    if gate.get("helper") != "go-missing":
        assert gate.get("ok") is False
    # Residual x in flags is fail-closed at compile_re2.
    result = compile_re2("a b", flags="x")
    assert result.mirror is None
    assert result.unencodable_reason == "x-flag-unstripped"


def test_s_flag_rejected_fail_closed():
    result = compile_re2("a.b", flags="s")
    assert result.mirror is None
    assert result.unencodable_reason == "s-flag"
