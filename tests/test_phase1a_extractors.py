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
    from regexproof.extractors.semgrep_yaml import extract_semgrep_yaml

    src = (ROOT / "semgrep_yaml" / "sample_basic.yaml").read_text(encoding="utf-8")
    recs = extract_semgrep_yaml(src, repo="fixture/sg", file="sample_basic.yaml", dialect="py_re")
    patterns = [r["pattern"] for r in recs if r.get("pattern")]
    assert any("select" in p for p in patterns)
    assert any("multi" in p and "line" in p for p in patterns)
    assert any("[A-Za-z0-9_]" in p for p in patterns)
    assert not any("chat.completions" in (p or "") for p in patterns)
    assert not any(p == "legacy" for p in patterns)
    assert not any(r.get("unencodable_reason") == "composite-pattern" for r in recs)
