"""Issue #103: caret-in-X ``^X(?:R|$)`` lowering (separate from A1B)."""

from __future__ import annotations

import z3
import pytest

from regexproof.compiler import compile_pattern
from regexproof.compiler.caret_in_x import CARET_IN_X_DOMAIN, is_caret_in_x_candidate
from regexproof.compiler.pcre import replay_argv
from regexproof.compiler.trailing_alt_dollar import try_compile_trailing_alt_dollar
from regexproof.compiler import _compile_dialect
from regexproof.fuzz.adapters import real_accepts_argv

TOYS_ENCODE = [
    ("^0+(?:&|$)", "search", ["0", "00", "0&", "00&z"], ["1", "x0", "&"]),
    ("^[a-f0-9]{4}(?:&|$)", "search", ["abcd", "abcd&"], ["abc", "xabcd"]),
    ("^(?:;|$)", "search", ["", ";", ";x"], ["x"]),
]

REJECT_CONTROLS = [
    ("^a|b", ("per-alternative-anchor",)),
    ("a(?:$|b)c", ("internal-anchor", "per-alternative-anchor")),
    ("(?:^|a)", ("per-alternative-anchor",)),
    ("(&|$)", ("per-alternative-anchor",)),
]


def _membership(mirror, s: str, *, timeout_ms: int = 10000) -> bool:
    sol = z3.Solver()
    sol.set("timeout", timeout_ms)
    sol.add(z3.InRe(z3.StringVal(s), mirror))
    r = sol.check()
    if r == z3.unknown:
        raise TimeoutError(s)
    return r == z3.sat


def _bare(pat, fl, dia, ck):
    return _compile_dialect(pat, fl, dia, ck, max_length=256, domain="ascii")


@pytest.mark.parametrize("pattern,call_kind,accept,reject", TOYS_ENCODE)
@pytest.mark.parametrize("dialect", ["pcre", "re2", "py_re"])
def test_toys_encode_and_membership(pattern, call_kind, accept, reject, dialect):
    cr = compile_pattern(pattern, dialect=dialect, call_kind=call_kind)
    assert cr.encodable, cr.unencodable_reason
    assert CARET_IN_X_DOMAIN in cr.declared_domain
    for s in accept:
        assert _membership(cr.mirror, s) is True, (dialect, pattern, s)
    for s in reject:
        assert _membership(cr.mirror, s) is False, (dialect, pattern, s)


@pytest.mark.parametrize("pattern,reasons", REJECT_CONTROLS)
def test_controls_still_rejected(pattern, reasons):
    cr = compile_pattern(pattern, dialect="pcre", call_kind="search")
    assert not cr.encodable
    assert cr.unencodable_reason in reasons


def test_a1b_still_refuses_caret_in_x():
    pat = "^0+(?:&|$)"
    assert is_caret_in_x_candidate(pat)
    a1b = try_compile_trailing_alt_dollar(
        pat, "", "pcre", "search", compile_bare=_bare
    )
    assert a1b is None


def test_bare_a1b_still_encodes_without_caret():
    cr = compile_pattern("foo(?:bar|$)", dialect="pcre", call_kind="search")
    assert cr.encodable
    assert "a1b_suffix_bound" in cr.declared_domain


def test_mirror_vs_pcre2_nonempty():
    pattern = "^0+(?:&|$)"
    cr = compile_pattern(pattern, dialect="pcre", call_kind="search")
    assert cr.encodable
    argv = replay_argv(pattern, "")
    for s in ["0", "00", "0&", "00&x", "1", "x0"]:
        assert _membership(cr.mirror, s) == real_accepts_argv(argv, s), s


def test_mutation_drop_dollar_branch():
    """Dropping the ``$`` branch must change the language (sensitivity)."""
    full = compile_pattern("^ab(?:cd|$)", dialect="pcre", call_kind="search")
    narrow = compile_pattern("^abcd", dialect="pcre", call_kind="search")
    assert full.encodable and narrow.encodable
    # "ab" accepted by full ($ branch) but not by XR-only.
    assert _membership(full.mirror, "ab") is True
    assert _membership(narrow.mirror, "ab") is False
