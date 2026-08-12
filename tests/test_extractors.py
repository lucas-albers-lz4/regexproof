"""Extractor accuracy: ≥20 fixtures/dialect with exact fields."""

from __future__ import annotations

from pathlib import Path

import jsonschema
import pytest

from regexproof.extractors.js_babel import extract_js, extract_js_precise
from regexproof.extractors.python_ast import extract_python
from regexproof.extractors.rule_file import extract_rule_file
from regexproof.schemas import extractor_schema

ROOT = Path(__file__).resolve().parent / "fixtures"


def _validate(recs):
    schema = extractor_schema()
    for r in recs:
        jsonschema.validate(r, schema)


def test_python_fixtures_count_and_accuracy():
    files = sorted((ROOT / "py_re").glob("sample_*.py"))
    assert len(files) >= 20
    all_recs = []
    for f in files:
        recs = extract_python(f.read_text(encoding="utf-8"), repo="fixture/py", file=f.name)
        assert recs, f"no records for {f}"
        all_recs.extend(recs)
        for r in recs:
            assert r["dialect"] == "py_re"
            assert r["call_kind"] in {"fullmatch", "match", "search", "substitution"}
            assert r["site"].startswith(f.name)
            if r.get("unencodable_reason") == "composite-pattern":
                assert r["pattern"] == ""
            elif not r.get("unencodable_reason"):
                assert r["pattern"]
    _validate(all_recs)
    assert any(r.get("unencodable_reason") == "composite-pattern" for r in all_recs)


def test_ecma_fixtures_count_and_accuracy():
    files = sorted((ROOT / "ecma").glob("sample_*.js"))
    assert len(files) >= 20
    all_recs = []
    for f in files:
        recs = extract_js(f.read_text(encoding="utf-8"), repo="fixture/js", file=f.name)
        assert recs, f"no records for {f}"
        all_recs.extend(recs)
        for r in recs:
            assert r["dialect"] == "ecma"
            assert r["site"].startswith(f.name)
    _validate(all_recs)
    assert any(r.get("unencodable_reason") == "composite-pattern" for r in all_recs)


def test_re2_rule_fixtures():
    files = sorted((ROOT / "re2").glob("sample_*.txt"))
    assert len(files) >= 20
    all_recs = []
    for f in files:
        recs = extract_rule_file(
            f.read_text(encoding="utf-8"), repo="fixture/re2", file=f.name, dialect="re2"
        )
        assert recs
        all_recs.extend(recs)
        for r in recs:
            assert r["dialect"] == "re2"
            assert r["call_kind"] == "search"
            assert r["pattern"]
    _validate(all_recs)


def test_toml_rule_fixtures():
    files = sorted((ROOT / "toml_rule").glob("sample_*.toml"))
    assert len(files) >= 20
    all_recs = []
    for f in files:
        recs = extract_rule_file(
            f.read_text(encoding="utf-8"), repo="fixture/toml", file=f.name, dialect="re2"
        )
        assert recs, f"no records for {f}"
        all_recs.extend(recs)
    _validate(all_recs)
    # composites must be explicit when present — sample_20 may parse oddly;
    # ensure no silent skip: every file produced ≥1 record
    assert len(all_recs) >= 20
    assert any(r.get("unencodable_reason") == "composite-pattern" for r in all_recs)


def test_toml_concat_not_literal_pattern():
    src = '[[rules]]\nid = "x"\nregex = "compos" + "ite"\n'
    recs = extract_rule_file(src, repo="t", file="bad.toml", dialect="re2")
    assert recs
    assert recs[0].get("unencodable_reason") == "composite-pattern"
    assert recs[0]["pattern"] == ""


def test_new_regexp_two_arg_string_flags():
    """Two-arg `new RegExp('pat', 'g')` must not swallow `, 'g'` into the pattern,
    must decode JS string escapes to the runtime value, and must classify `g/y`
    flags as stateful (the luna-gate catch on PR #258 / xibo-cms)."""
    src = (
        "const a = new RegExp('\\\\[.*?\\\\]', 'g');\n"
        'const b = new RegExp("[\\\\A]", "u");\n'
        'const c = new RegExp("^[a-z]+$");\n'
        "const d = new RegExp(/foo/i);\n"
        "const e = new RegExp('\\\\d+', 'i');\n"
    )
    recs = extract_js_precise(src, repo="t", file="x.js")
    by_line: dict[int, list] = {}
    for r in recs:
        by_line.setdefault(r["line"], []).append(r)
    assert len(recs) == 6, [(r["line"], r["column"]) for r in recs]
    a = by_line[1][0]
    assert a["pattern"] == r"\[.*?\]", a["pattern"]
    assert a["flags"] == "g"
    assert a["unencodable_reason"] == "stateful"
    b = by_line[2][0]
    assert b["pattern"] == r"[\A]", b["pattern"]
    assert b["flags"] == "u"
    assert b["unencodable_reason"] == "u-flag"
    c = by_line[3][0]
    assert c["pattern"] == "^[a-z]+$" and c["flags"] == "" and c.get("unencodable_reason") is None
    # new RegExp(/foo/i) emits BOTH the literal record and the composite wrapper.
    d_wrap, d_lit = by_line[4]
    assert d_wrap["pattern"] == "" and d_wrap["unencodable_reason"] == "composite-pattern"
    assert d_lit["pattern"] == "foo" and d_lit["flags"] == "i"
    e = by_line[5][0]
    assert e["pattern"] == r"\d+" and e["flags"] == "i", (e["pattern"], e["flags"])


def test_new_regexp_concat_is_composite():
    """Non-literal first args (and literal + concat) stay composite-pattern."""
    src = (
        'const r = new RegExp(prefix + "x20");\n'
        'const s = new RegExp("a" + x, "g");\n'
    )
    recs = extract_js(src, repo="t", file="x.js")
    assert len(recs) == 2, [r["line"] for r in recs]
    for r in recs:
        assert r["pattern"] == ""
        assert r["unencodable_reason"] == "composite-pattern"


def test_new_regexp_dynamic_args_composite():
    """Comment-separated concat, variable flags, and template interpolation are
    all dynamic — must be composite, never a fixed literal (luna r2 F1/F4)."""
    src = (
        'const a = new RegExp("a" /* c */ + x, "i");\n'
        'const b = new RegExp("a", flags);\n'
        "const c = new RegExp(`foo${x}`, 'g');\n"
    )
    recs = extract_js_precise(src, repo="t", file="x.js")
    assert len(recs) == 3, [r["line"] for r in recs]
    for r in recs:
        assert r["pattern"] == ""
        assert r["unencodable_reason"] == "composite-pattern"


def test_new_regexp_backtick_flags():
    """Plain template-literal first arg with a literal flags arg is static."""
    recs = extract_js_precise("const r = new RegExp(`foo`, \"i\");", repo="t", file="x.js")
    assert len(recs) == 1
    assert recs[0]["pattern"] == "foo"
    assert recs[0]["flags"] == "i"
    assert recs[0].get("unencodable_reason") is None


def test_unescape_js_string_escapes():
    """JS escape decoding: octal, \\u{...} code points, \\xHH, NUL, unknown-drop."""
    from regexproof.extractors.js_babel import _unescape_js_string

    assert _unescape_js_string(r"\141") == "a"          # octal
    assert _unescape_js_string(r"\u{1F600}") == "😀"     # code point
    assert _unescape_js_string(r"\0") == "\0"           # lone NUL
    assert _unescape_js_string(r"\08") == "\0" + "8"    # NUL + literal 8
    assert _unescape_js_string(r"\x41") == "A"          # hex
    assert _unescape_js_string(r"\u0041") == "A"        # uHHHH
    assert _unescape_js_string(r"\d+") == "d+"          # unknown escape drops backslash
    assert _unescape_js_string(r"\\[") == r"\["         # escaped backslash stays


def test_new_regexp_two_arg_legacy_extract_js():
    """The legacy extract_js path shares _NEW_REGEXP — same two-arg contract."""
    src = "const a = new RegExp('\\\\d+', 'g');\n"
    recs = extract_js(src, repo="t", file="x.js")
    assert len(recs) == 1
    assert recs[0]["pattern"] == r"\d+"
    assert recs[0]["flags"] == "g"
    assert recs[0]["unencodable_reason"] == "stateful"
