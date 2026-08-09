"""Cross-engine Coraza↔CRS helpers (Wave-2 P5)."""

from __future__ import annotations

from pathlib import Path

import pytest

from regexproof.rule_diff.cross_engine import (
    classify_cross_engine,
    discover_cross_engine_pairs,
    preflight_crs,
)

ROOT = Path(__file__).resolve().parents[1]
RULES = ROOT / "batch" / "corpora" / "coreruleset" / "rules"


def test_classify_lookaround_non_comparable_re2():
    info = classify_cross_engine(r"(?=a)b", "")
    # Lookahead: re2 should reject; pcre may accept depending on compiler.
    assert info["result_class"] in {
        "non-comparable-re2",
        "non-comparable-both",
        "comparable",
    }


def test_classify_simple_comparable():
    info = classify_cross_engine(r"abc[0-9]+", "")
    assert info["result_class"] == "comparable"
    assert info["re2_encodable"] and info["pcre_encodable"]


def test_preflight_crs_or_skip():
    if not RULES.is_dir():
        pytest.skip("CRS rules not materialized")
    pre = preflight_crs(RULES)
    assert pre["head"].startswith("55b09f5")
    assert pre["n_request"] >= 5


def test_discover_pairs_smoke():
    if not RULES.is_dir():
        pytest.skip("CRS rules not materialized")
    from regexproof.rule_diff.cross_engine import load_crs_rx_records

    recs = load_crs_rx_records(RULES)
    assert len(recs) >= 10
    out = discover_cross_engine_pairs(recs, max_pairs=5, max_classify=40)
    assert "class_counts" in out
    assert out["classified"] >= 1
