"""Fix-wave P1 (#69): {1}-quantifier crash + lazy-quantifier regression tests.

Test-first per the wave gate: these fail on pre-fix code — `{1}`/`{1,1}`
crashes lower.py `_repeat` (Z3Exception) and lazy quantifiers reject as
parse-error — and must be green after the fixes.
"""

from __future__ import annotations

import pytest

from regexproof.compiler import compile_pattern
from tests.golden.cases import membership

DIALECTS = ["py_re", "ecma", "re2", "pcre"]

EXACT_SINGLE = [r"x{1}", r"(?:ab){1}", r"x{1,1}"]
LAZY = [r"a*?", r"a+?", r"a??", r"a{2,3}?"]


@pytest.mark.parametrize("dialect", DIALECTS)
@pytest.mark.parametrize("pat", EXACT_SINGLE)
def test_exact_single_quantifier_compiles(dialect, pat):
    """A compiler must REJECT, never crash. Regression: lower.py `_repeat`
    built `Concat(body)` at lo==1 → Z3Exception 'At least two arguments'."""
    cr = compile_pattern(pat, "", dialect, "search")
    assert cr.encodable, f"{dialect} {pat}: {cr.unencodable_reason}"


@pytest.mark.parametrize("dialect", DIALECTS)
@pytest.mark.parametrize("pat", LAZY)
def test_lazy_quantifiers_encodable(dialect, pat):
    """Laziness is a matching strategy, not language: a*? ≡ a* for
    membership. Was rejected as parse-error in ecma/re2/pcre."""
    cr = compile_pattern(pat, "", dialect, "fullmatch")
    assert cr.encodable, f"{dialect} {pat}: {cr.unencodable_reason}"


def test_lazy_star_mirror_equivalent_to_greedy():
    """a*? accepts exactly what a* accepts (bounded membership probes)."""
    for dialect in DIALECTS:
        lazy = compile_pattern("a*?", "", dialect, "fullmatch")
        greedy = compile_pattern("a*", "", dialect, "fullmatch")
        assert lazy.encodable and greedy.encodable, dialect
        for s in ["", "a", "aaa", "b", "ab"]:
            assert membership(lazy.mirror, s) == membership(greedy.mirror, s), (
                dialect,
                s,
            )


def test_lazy_plus_mirror_equivalent_to_greedy():
    """a+? accepts exactly what a+ accepts (luna review: uncovered branch)."""
    for dialect in DIALECTS:
        lazy = compile_pattern("a+?", "", dialect, "fullmatch")
        greedy = compile_pattern("a+", "", dialect, "fullmatch")
        assert lazy.encodable and greedy.encodable, dialect
        for s in ["", "a", "aaa", "b"]:
            assert membership(lazy.mirror, s) == membership(greedy.mirror, s), (
                dialect,
                s,
            )


def test_lazy_optional_mirror_equivalent_to_greedy():
    """a?? accepts exactly what a? accepts (luna review: uncovered branch)."""
    for dialect in DIALECTS:
        lazy = compile_pattern("a??", "", dialect, "fullmatch")
        greedy = compile_pattern("a?", "", dialect, "fullmatch")
        assert lazy.encodable and greedy.encodable, dialect
        for s in ["", "a", "aa", "b"]:
            assert membership(lazy.mirror, s) == membership(greedy.mirror, s), (
                dialect,
                s,
            )


def test_lazy_exact_bound_mirror_equivalent_to_greedy():
    """a{2}? accepts exactly what a{2} accepts (luna review: uncovered branch)."""
    for dialect in DIALECTS:
        lazy = compile_pattern("a{2}?", "", dialect, "fullmatch")
        greedy = compile_pattern("a{2}", "", dialect, "fullmatch")
        assert lazy.encodable and greedy.encodable, dialect
        for s in ["", "a", "aa", "aaa", "b"]:
            assert membership(lazy.mirror, s) == membership(greedy.mirror, s), (
                dialect,
                s,
            )


def test_lazy_bound_mirror_equivalent_to_greedy():
    """a{2,3}? accepts exactly what a{2,3} accepts."""
    for dialect in DIALECTS:
        lazy = compile_pattern("a{2,3}?", "", dialect, "fullmatch")
        greedy = compile_pattern("a{2,3}", "", dialect, "fullmatch")
        assert lazy.encodable and greedy.encodable, dialect
        for s in ["a", "aa", "aaa", "aaaa", "b"]:
            assert membership(lazy.mirror, s) == membership(greedy.mirror, s), (
                dialect,
                s,
            )
