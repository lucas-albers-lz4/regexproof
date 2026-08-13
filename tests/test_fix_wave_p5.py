"""Fix-wave Phase 5 (#73): consolidation + golden hardening."""

from __future__ import annotations

from regexproof.compiler import compile_pattern
from regexproof.compiler.base import repeat_z3
from regexproof.compiler.reject_markers import PCRE_REJECT_MARKERS
from regexproof.compiler.pcre import _local_reject


def test_repeat_z3_identity_lo_hi_one():
    from z3 import Re

    body = Re("x")
    assert repeat_z3(body, 1, 1) is body


def test_pcre_helper_shares_reject_markers():
    reasons = {r for _, r in PCRE_REJECT_MARKERS}
    assert "r-escape" in reasons and "x-escape" in reasons and "c-escape" in reasons
    assert _local_reject(r"a\R") == "r-escape"
    assert _local_reject(r"(?=x)") == "lookaround"


def test_unicode_prop_rejected_on_pcre_re2_perl():
    """#362: real \\p{}/\\P{} must not silently literalize in RE2/PCRE mirrors."""
    from regexproof.compiler.reject_markers import unicode_prop_unencodable

    assert unicode_prop_unencodable(r"\p{L}") == "unicode-prop"
    assert unicode_prop_unencodable(r"\P{N}") == "unicode-prop"
    assert unicode_prop_unencodable(r"\pL") == "unicode-prop"
    assert unicode_prop_unencodable(r"\\p{L}") is None  # escaped literal
    assert compile_pattern(r"^\p{L}+$", "", "pcre", "fullmatch").unencodable_reason == (
        "unicode-prop"
    )
    assert compile_pattern(r"^\p{L}+$", "", "re2", "fullmatch").unencodable_reason == (
        "unicode-prop"
    )
    assert compile_pattern(r"^\p{L}+$", "", "perl", "fullmatch").unencodable_reason == (
        "unicode-prop"
    )
    # ECMA without u is a real identity-escape; still encodable.
    assert compile_pattern(r"^\p{L}+$", "", "ecma", "fullmatch").encodable
    # Escaped literal still encodes on PCRE/RE2.
    assert compile_pattern(r"^\\\\p{L}$", "", "pcre", "fullmatch").encodable
    assert compile_pattern(r"^\\\\p{L}$", "", "re2", "fullmatch").encodable


def test_p1_p2_goldens_still_green():
    """Hardening: Phase 1–2 probes must remain encodable/rejected as locked."""
    assert compile_pattern("x{1}", "", "ecma", "fullmatch").encodable
    assert compile_pattern("a*?", "", "pcre", "fullmatch").encodable
    assert (
        compile_pattern("^a|b", "", "ecma", "search").unencodable_reason
        == "per-alternative-anchor"
    )
    assert compile_pattern("(?i:ab)", "", "py_re", "fullmatch").encodable
    assert compile_pattern("a}+", "", "pcre", "fullmatch").encodable
    assert compile_pattern(r"[^\S]", "", "ecma", "fullmatch").encodable
    assert compile_pattern(r"^[^ab]$", "", "re2", "fullmatch").encodable
