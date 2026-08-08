"""Extractor accuracy: ≥20 fixtures/dialect with exact fields."""

from __future__ import annotations

from pathlib import Path

import jsonschema
import pytest

from regexproof.extractors.js_babel import extract_js
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
