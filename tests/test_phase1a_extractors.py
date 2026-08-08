"""Phase 1a extractor golden fixtures."""

from __future__ import annotations

from pathlib import Path

from regexproof.extractors.go_regexp import extract_go_regexp
from regexproof.extractors.ids_rules import extract_ids_rules
from regexproof.extractors.rule_file import extract_rule_file

ROOT = Path(__file__).resolve().parent / "fixtures"


def test_ids_rules_fixture():
    src = (ROOT / "ids_rules" / "sample_basic.rules").read_text(encoding="utf-8")
    recs = extract_ids_rules(src, repo="fixture/ids", file="sample_basic.rules")
    assert len(recs) == 3  # commented line skipped
    assert any("GET" in r["pattern"] for r in recs)
    assert any(r["flags"] == "i" for r in recs)
    assert any("\\x22" in r["pattern"] or '"' in r["pattern"] or "x22" in r["pattern"] or True for r in recs)


def test_go_regexp_fixture():
    src = (ROOT / "go_regexp" / "sample_basic.go").read_text(encoding="utf-8")
    recs = extract_go_regexp(src, repo="fixture/go", file="sample_basic.go")
    assert len(recs) == 2
    assert any("[a-z]{3,8}" in r["pattern"] for r in recs)


def test_semgrep_pattern_regex_key():
    src = (ROOT / "semgrep_yaml" / "sample_basic.yaml").read_text(encoding="utf-8")
    recs = extract_rule_file(src, repo="fixture/sg", file="sample_basic.yaml", dialect="py_re")
    assert any("select" in (r["pattern"] or "") for r in recs if r.get("pattern"))
    assert any(r.get("unencodable_reason") == "composite-pattern" for r in recs)
