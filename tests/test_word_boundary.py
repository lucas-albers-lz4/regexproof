"""ASCII-domain \\b encode tests (word-boundary wave)."""

from __future__ import annotations

import re

import z3

from regexproof.compiler import compile_pattern


def _in_re(mirror, s: str) -> bool:
    sol = z3.Solver()
    sol.set("timeout", 8000)
    sol.add(z3.InRe(z3.StringVal(s), mirror))
    r = sol.check()
    assert r != z3.unknown, s
    return r == z3.sat


def test_re2_word_boundary_encodes():
    cr = compile_pattern(r"\bword\b", "", "re2", "search")
    assert cr.encodable
    assert cr.declared_domain == "ascii"
    assert _in_re(cr.mirror, "word")
    assert _in_re(cr.mirror, " word ")
    assert not _in_re(cr.mirror, "awordb")


def test_py_re_unicode_word_boundary_rejects():
    cr = compile_pattern(r"\bword\b", "", "py_re", "search")
    assert not cr.encodable
    assert cr.unencodable_reason == "word-boundary"


def test_mid_pattern_word_boundary_rejects():
    cr = compile_pattern(r"foo\bbar", "", "re2", "search")
    assert not cr.encodable
    assert cr.unencodable_reason == "word-boundary"


def test_negated_boundary_rejects():
    cr = compile_pattern(r"\Bword\B", "", "re2", "search")
    assert not cr.encodable
    assert cr.unencodable_reason == "word-boundary"


def test_ascii_mirror_agrees_with_re_ascii():
    pat = r"\b[a-z]{3}\b"
    cr = compile_pattern(pat, "", "re2", "search")
    assert cr.encodable
    eng = re.compile(pat, re.ASCII)
    for s in ["abc", " abc ", "xabcy", "ab", "abcd", "!abc!"]:
        assert _in_re(cr.mirror, s) == bool(eng.search(s)), s


def test_unicode_probe_diverges_from_python_default():
    """Documents TRAPS #17: ASCII mirror ≠ Python Unicode \\b (domain gate)."""
    pat = r"\bword\b"
    cr = compile_pattern(pat, "", "re2", "search")
    assert cr.encodable
    s = "中word"
    # RE2/ASCII: 中 is non-word → boundary → match. Python default: 中 is word → no match.
    assert _in_re(cr.mirror, s) is True
    assert re.search(pat, s) is None
    assert re.search(pat, s, re.ASCII) is not None
