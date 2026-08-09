"""P2 (#87): pattern-final ``(?:...|$)`` A1B lowering."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
import z3

from regexproof.compiler import compile_pattern
from regexproof.compiler.re2 import replay_argv
from regexproof.compiler.trailing_alt_dollar import (
    A1B_SUFFIX_BOUND,
    split_trailing_dollar,
)
from regexproof.fuzz.adapters import real_accepts_argv

ROOT = Path(__file__).resolve().parents[1]
FROZEN = ROOT / "properties" / "generated" / "gitleaks-frozen-ids.ndjson"

TOYS_ENCODE = [
    ("(?:a|$)", "search", ["", "a", "foo", "xa"], []),
    ("foo(?:bar|$)", "search", ["foo", "foobar", "xfoo", "foobarz"], ["bar", "fooba"]),
    ("x(?:a|b|$)", "search", ["x", "xa", "xb", "zxa"], ["a", "b"]),
    ("foo(?:x(?:y)|$)", "search", ["foo", "fooxy", "xfoo"], ["foox", "xy"]),
]

REJECT_CONTROLS = [
    ("^a|b", "search", ("per-alternative-anchor",)),
    # Mid-pattern $: py_re BRANCH → per-alternative-anchor; others → internal-anchor.
    ("a(?:$|b)c", "search", ("internal-anchor", "per-alternative-anchor")),
    ("(?:^|a)", "search", ("per-alternative-anchor",)),
    # Leading ^ in X is outside A1B (caret-in-X is a separate shape — #103).
]


def test_a1b_does_not_claim_caret_in_x():
    """A1B refuse caret-in-X; dispatcher may encode via caret_in_x instead."""
    from regexproof.compiler.trailing_alt_dollar import try_compile_trailing_alt_dollar
    from regexproof.compiler import _compile_dialect

    def bare(p, f, d, c):
        return _compile_dialect(p, f, d, c, max_length=256, domain="ascii")

    a1b = try_compile_trailing_alt_dollar(
        "^0+(?:&|$)", "", "pcre", "search", compile_bare=bare
    )
    assert a1b is None
    cr = compile_pattern("^0+(?:&|$)", dialect="pcre", call_kind="search")
    assert cr.encodable
    assert "caret_in_x" in cr.declared_domain


def _membership(mirror, s: str, *, timeout_ms: int = 10000) -> bool:
    sol = z3.Solver()
    sol.set("timeout", timeout_ms)
    sol.add(z3.InRe(z3.StringVal(s), mirror))
    r = sol.check()
    if r == z3.unknown:
        raise TimeoutError(s)
    return r == z3.sat


def test_split_nested_noncap():
    sp = split_trailing_dollar("foo(?:x(?:y)|$)")
    assert sp is not None
    assert sp["x_bare"] == "foo"
    assert sp["r_alt"] == "x(?:y)"


@pytest.mark.parametrize("pattern,call_kind,accept,reject", TOYS_ENCODE)
@pytest.mark.parametrize("dialect", ["re2", "py_re", "pcre", "ecma"])
def test_toys_encode_and_membership(pattern, call_kind, accept, reject, dialect):
    cr = compile_pattern(pattern, dialect=dialect, call_kind=call_kind)
    assert cr.encodable, cr.unencodable_reason
    assert f"a1b_suffix_bound={A1B_SUFFIX_BOUND}" in cr.declared_domain
    for s in accept:
        assert _membership(cr.mirror, s) is True, (dialect, pattern, s)
    for s in reject:
        assert _membership(cr.mirror, s) is False, (dialect, pattern, s)


@pytest.mark.parametrize("pattern,call_kind,reasons", REJECT_CONTROLS)
@pytest.mark.parametrize("dialect", ["re2", "py_re", "pcre", "ecma"])
def test_controls_still_rejected(pattern, call_kind, reasons, dialect):
    cr = compile_pattern(pattern, dialect=dialect, call_kind=call_kind)
    assert not cr.encodable
    assert cr.unencodable_reason in reasons


def test_wb_short_tok_encode_re2():
    pattern = r"\b(TOK[A-Z0-9]{8})(?:[\x60'\"\s;]|$)"
    cr = compile_pattern(pattern, dialect="re2", call_kind="search")
    assert cr.encodable, cr.unencodable_reason
    assert _membership(cr.mirror, "TOKABCDEF12") is True
    assert _membership(cr.mirror, "TOKABCDEF12;") is True
    assert _membership(cr.mirror, "xTOKABCDEF12") is False
    # Mid-string junk after a non-suffix X must not false-SAT.
    assert _membership(cr.mirror, r"\TOKXBEJ17HT]_abc") is False


def test_mirror_vs_re2_toy():
    pattern = "foo(?:bar|$)"
    cr = compile_pattern(pattern, dialect="re2", call_kind="search")
    assert cr.encodable
    argv = replay_argv(pattern, "")
    for s in ["foo", "foobar", "xfoo", "bar", "fooba"]:
        mirror = _membership(cr.mirror, s)
        real = real_accepts_argv(argv, s)
        assert mirror == real, (s, mirror, real)


def test_mirror_vs_py_re_toy():
    pattern = "x(?:a|b|$)"
    cr = compile_pattern(pattern, dialect="py_re", call_kind="search")
    assert cr.encodable
    cre = re.compile(pattern)
    for s in ["x", "xa", "xb", "zxa", "a", ""]:
        assert _membership(cr.mirror, s) == (cre.search(s) is not None), s


def _frozen_pattern(prefix: str) -> str:
    for line in FROZEN.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        if row["regex_id"].startswith(prefix):
            return row["pattern"]
    raise AssertionError(prefix)


@pytest.mark.parametrize(
    "rid_prefix",
    ["7e1b515f", "3d5d72fe", "ac8604fc"],
)
def test_gitleaks_solvable_ids_encode(rid_prefix):
    pattern = _frozen_pattern(rid_prefix)
    cr = compile_pattern(pattern, dialect="re2", call_kind="search")
    assert cr.encodable, (rid_prefix, cr.unencodable_reason)


@pytest.mark.parametrize("rid_prefix", ["41131f39", "da53e982"])
def test_gitleaks_boundary_ids_encode(rid_prefix):
    """Perf-boundary samples must still be encodable (TIMEOUT ≠ unencodable)."""
    pattern = _frozen_pattern(rid_prefix)
    cr = compile_pattern(pattern, dialect="re2", call_kind="search")
    assert cr.encodable, (rid_prefix, cr.unencodable_reason)


def test_fix_wave_caret_alt_still_locked():
    """Regression lock from test_fix_wave_p2 — must not regress."""
    for dialect in ("re2", "ecma", "pcre", "py_re"):
        cr = compile_pattern("^a|b", dialect=dialect, call_kind="search")
        assert cr.unencodable_reason == "per-alternative-anchor"


def test_mutation_guard_drop_dollar_branch_changes_language():
    """Weakening ``(?:bar|$)`` → ``(?:bar)`` must flip some suffix-only accepts."""
    full = compile_pattern("foo(?:bar|$)", dialect="re2", call_kind="search")
    weak = compile_pattern("foo(?:bar)", dialect="re2", call_kind="search")
    assert full.encodable and weak.encodable
    # "foo" at EOS: accepted by full ($ branch), rejected by weak.
    assert _membership(full.mirror, "foo") is True
    assert _membership(weak.mirror, "foo") is False


def test_differential_fuzz_toy_foo_bar():
    """Mirror ≡ go-re2 on short inputs (membership timeout ≥15s per #86)."""
    import itertools

    from z3 import InRe, StringVal

    pattern = "foo(?:bar|$)"
    cr = compile_pattern(pattern, dialect="re2", call_kind="search")
    assert cr.encodable
    argv = replay_argv(pattern, "")
    alphabet = "abforxyz"
    for n in range(0, 4):
        for tup in itertools.product(alphabet, repeat=n):
            s = "".join(tup)
            sol = z3.Solver()
            sol.set("timeout", 15000)
            sol.add(InRe(StringVal(s), cr.mirror))
            r = sol.check()
            if r == z3.unknown:
                continue
            mirror = r == z3.sat
            real = real_accepts_argv(argv, s, timeout=5.0)
            assert mirror == real, (s, mirror, real)
