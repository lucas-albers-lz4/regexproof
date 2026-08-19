"""Fix-wave Phase 2 (#70): false-UNSAT compiler soundness regressions."""

from __future__ import annotations

import re

from z3 import InRe, String, sat

from regexproof.compiler import compile_pattern
from regexproof.compiler.pcre_strip import strip_atomic_and_possessive, strip_lazy_quantifiers


def _membership(mirror, s: str) -> bool:
    z3 = __import__("z3")
    solver = z3.Solver()
    solver.add(InRe(String("s"), mirror))
    solver.add(String("s") == s)
    return solver.check() == sat


def test_per_alternative_anchor_rejected_not_hoisted():
    """^a|b must never silently compile as ^(a|b) under search."""
    for dialect in ("ecma", "pcre", "re2"):
        cr = compile_pattern("^a|b", "", dialect, "search")
        assert not cr.encodable, dialect
        assert cr.unencodable_reason == "per-alternative-anchor", (
            dialect,
            cr.unencodable_reason,
        )
    py = compile_pattern("^a|b", "", "py_re", "search")
    assert not py.encodable
    assert py.unencodable_reason == "per-alternative-anchor"


def test_py_re_inline_ignorecase_leading_and_scoped():
    for pattern, accept, reject in (
        ("(?i)ab", ["ab", "AB", "Ab"], ["ac", "a"]),
        ("(?i:ab)", ["ab", "AB"], ["ac"]),
        ("x(?i:ab)y", ["xaby", "xABy"], ["xACy", "Xaby"]),
    ):
        cr = compile_pattern(pattern, "", "py_re", "fullmatch")
        assert cr.encodable, (pattern, cr.unencodable_reason)
        for s in accept:
            assert _membership(cr.mirror, s), (pattern, s)
            assert re.fullmatch(pattern, s) is not None, (pattern, s)
        for s in reject:
            assert not _membership(cr.mirror, s), (pattern, s)


def test_strip_preserves_literal_brace_plus():
    assert strip_atomic_and_possessive("a}+") == "a}+"
    assert strip_atomic_and_possessive("a{2,3}+") == "a{2,3}"
    assert strip_lazy_quantifiers("a}?") == "a}?"
    assert strip_lazy_quantifiers("a{2,3}?") == "a{2,3}"


def test_a_brace_plus_encodes_one_or_more_brace():
    cr = compile_pattern("a}+", "", "pcre", "fullmatch")
    assert cr.encodable, cr.unencodable_reason
    assert _membership(cr.mirror, "a}")
    assert _membership(cr.mirror, "a}}")
    assert not _membership(cr.mirror, "a")


def test_ecma_negated_S_accepts_nbsp():
    """Dialect space codes on complement — ECMA \\s includes NBSP."""
    cr = compile_pattern(r"[^\S]", "", "ecma", "fullmatch")
    assert cr.encodable, cr.unencodable_reason
    assert _membership(cr.mirror, "\u00a0")
    assert _membership(cr.mirror, " ")
    assert not _membership(cr.mirror, "a")


def test_negated_class_literal_ranges_all_dialects():
    for dialect in ("py_re", "ecma", "re2", "pcre"):
        cr = compile_pattern(r"^[^ab]$", "", dialect, "fullmatch")
        assert cr.encodable, (dialect, cr.unencodable_reason)
        assert _membership(cr.mirror, "c")
        assert not _membership(cr.mirror, "a")
