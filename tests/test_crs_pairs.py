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
FIXTURE = ROOT / "tests" / "fixtures" / "crs_pairs"
V_OLDER = FIXTURE / "older" / "rules"
V_NEWER = FIXTURE / "newer" / "rules"


def test_version_diff_admits_changed_encodable_pairs():
    report = discover_crs_version_pairs(
        older_rules=V_OLDER,
        newer_rules=V_NEWER,
        older_tag="fixture-older",
        newer_tag="fixture-newer",
    )
    assert report["admitted_count"] >= 1
    # 942220 is a known encodable widening (optional json. prefix)
    families = {p["family"] for p in report["admitted"]}
    assert "RD-crs-942220-version" in families
    for p in report["admitted"]:
        jsonschema.validate(p, admitted_pair_schema())
        assert p["direction"] == "r2_minus_r1"
        assert p["provenance"]["adapter"] == "crs_rule_derived_r1"


def test_sibling_family_requires_family_contract():
    blocked = discover_crs_sibling_pairs(
        rules_dir=V_NEWER, tag="fixture-newer", max_pairs_per_family=3
    )
    assert blocked["admitted_count"] == 0
    assert blocked["dropped"][0]["reason"] == "missing-family-contract"
    placeholder = discover_crs_sibling_pairs(
        rules_dir=V_NEWER,
        tag="fixture-newer",
        family_contract={"R1": "", "R2": "x", "provenance": "x"},
    )
    assert placeholder["admitted_count"] == 0


def test_sibling_family_dedupes_and_directions():
    report = discover_crs_sibling_pairs(
        rules_dir=V_NEWER,
        tag="fixture-newer",
        max_pairs_per_family=3,
        family_contract={
            "R1": "lower rule id in family",
            "R2": "higher rule id in family",
            "provenance": "fixture",
        },
    )
    assert report["admitted_count"] >= 1
    seen = set()
    for p in report["admitted"]:
        jsonschema.validate(p, admitted_pair_schema())
        assert p["pair_id"] not in seen
        seen.add(p["pair_id"])
        assert p["r1"]["rule_id"] != p["r2"]["rule_id"]


def test_combined_discovery_counts():
    report = discover_crs_pairs(
        older_rules=V_OLDER,
        newer_rules=V_NEWER,
        older_tag="fixture-older",
        newer_tag="fixture-newer",
    )
    assert report["version_diff_admitted"] >= 1
    assert report["admitted_count"] == len({p["family"] for p in report["admitted"]})
    assert report["sibling_admitted"] == 0


def test_generated_crs_report_has_no_sibling_pairs():
    import json

    path = ROOT / "properties" / "generated" / "crs_rule_diff_report.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    blob = json.dumps(data)
    assert "RD-crs-901" not in blob
    # The retraction counter is the only remaining "sibling" token.
    assert data.get("retracted_sibling_pairs", 0) >= 1
    assert data.get("sat_gaps") == sum(
        1 for r in data.get("results") or []
        if r.get("kind") == "rule_diff" and r.get("result") == "sat"
    )


def test_crs_report_witnesses_are_redacted():
    import json

    path = ROOT / "properties" / "generated" / "crs_rule_diff_report.json"
    blob = path.read_text(encoding="utf-8")
    assert "JSon" not in blob
    assert "1E309" not in blob
    data = json.loads(blob)
    for rec in data.get("results") or []:
        w = rec.get("witness")
        if isinstance(w, dict):
            for v in w.values():
                if isinstance(v, str):
                    assert v.startswith("<redacted")


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
