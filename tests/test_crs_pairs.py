"""CRS pair-builder unit tests (version-diff + sibling-family)."""

from __future__ import annotations

from pathlib import Path

import jsonschema

from regexproof.rule_diff.crs_pairs import (
    discover_crs_pairs,
    discover_crs_sibling_pairs,
    discover_crs_version_pairs,
)
from regexproof.schemas import admitted_pair_schema

ROOT = Path(__file__).resolve().parents[1]
V28 = Path("/tmp/coreruleset-v4.28.0/rules")
V27 = Path("/tmp/coreruleset-v4.27.0/rules")


def _have_corpus() -> bool:
    return V28.is_dir() and V27.is_dir()


import pytest


@pytest.mark.skipif(not _have_corpus(), reason="CRS corpus not materialized under /tmp")
def test_version_diff_admits_changed_encodable_pairs():
    report = discover_crs_version_pairs(older_rules=V27, newer_rules=V28)
    assert report["admitted_count"] >= 1
    # 942220 is a known encodable widening (optional json. prefix) within DEFAULT_MAX_LEN
    families = {p["family"] for p in report["admitted"]}
    assert "RD-crs-942220-version" in families
    for p in report["admitted"]:
        jsonschema.validate(p, admitted_pair_schema())
        assert p["direction"] == "r2_minus_r1"
        assert p["provenance"]["adapter"] == "crs_rule_derived_r1"


@pytest.mark.skipif(not _have_corpus(), reason="CRS corpus not materialized under /tmp")
def test_sibling_family_dedupes_and_directions():
    report = discover_crs_sibling_pairs(rules_dir=V28, max_pairs_per_family=3)
    assert report["admitted_count"] >= 1
    seen = set()
    for p in report["admitted"]:
        jsonschema.validate(p, admitted_pair_schema())
        assert p["pair_id"] not in seen
        seen.add(p["pair_id"])
        assert p["r1"]["rule_id"] != p["r2"]["rule_id"]


@pytest.mark.skipif(not _have_corpus(), reason="CRS corpus not materialized under /tmp")
def test_combined_discovery_counts():
    report = discover_crs_pairs(older_rules=V27, newer_rules=V28)
    assert report["version_diff_admitted"] >= 1
    assert report["admitted_count"] == len({p["family"] for p in report["admitted"]})


def test_unchanged_id_dropped_on_tiny_fixture(tmp_path: Path):
    older = tmp_path / "old"
    newer = tmp_path / "new"
    older.mkdir()
    newer.mkdir()
    older.joinpath("r.conf").write_text(
        'SecRule ARGS "@rx ^abc$" "id:100,phase:2,deny"\n', encoding="utf-8"
    )
    newer.joinpath("r.conf").write_text(
        'SecRule ARGS "@rx ^abc$" "id:100,phase:2,deny"\n'
        'SecRule ARGS "@rx ^abcd$" "id:101,phase:2,deny"\n',
        encoding="utf-8",
    )
    report = discover_crs_version_pairs(older_rules=older, newer_rules=newer)
    assert any(d.get("reason") == "unchanged-id" for d in report["dropped"])
