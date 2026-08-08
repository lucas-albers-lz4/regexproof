"""Phase 3 rule_diff schemas, integrity, and pair discovery."""

from __future__ import annotations

from pathlib import Path

import jsonschema

from regexproof.extractors.rule_file import extract_rule_file
from regexproof.rule_diff.pairs import MIN_ADMITTED_PAIRS, discover_pairs
from regexproof.rule_diff.specs import (
    gitleaks_rule_patterns,
    load_canonical_specs,
    reject_rule_derived_r1,
)
from regexproof.schemas import admitted_pair_schema, rule_diff_report_schema

ROOT = Path(__file__).resolve().parents[1]
TOML = ROOT / "pilots" / "gitleaks" / "config" / "gitleaks.toml"
SPECS = ROOT / "pilots" / "gitleaks" / "canonical_specs" / "catalog.json"


def test_rule_file_sites_are_unique_per_rule():
    src = TOML.read_text(encoding="utf-8")
    recs = extract_rule_file(
        src, repo="gitleaks/gitleaks", file="pilots/gitleaks/config/gitleaks.toml"
    )
    sites = [r["site"] for r in recs]
    assert len(set(sites)) == len(sites)
    github = next(r for r in recs if r["context_snippet"] == "github-pat")
    assert github["line"] > 7


def test_canonical_specs_reject_rule_derived_r1():
    specs = load_canonical_specs(SPECS)
    assert len(specs) >= MIN_ADMITTED_PAIRS
    violations = reject_rule_derived_r1(
        specs, rule_patterns=gitleaks_rule_patterns(TOML)
    )
    assert violations == []


def test_reject_rule_derived_detects_copy():
    specs = load_canonical_specs(SPECS)
    patterns = gitleaks_rule_patterns(TOML)
    # Inject a copy of a real rule pattern
    bad = dict(specs[0])
    bad["pattern"] = next(iter(patterns))
    violations = reject_rule_derived_r1([bad], rule_patterns=patterns)
    assert violations


def test_pair_discovery_meets_floor_and_schema():
    discovered = discover_pairs(toml_path=TOML, specs_path=SPECS)
    assert discovered["floor_ok"]
    assert discovered["admitted_count"] >= MIN_ADMITTED_PAIRS
    schema = admitted_pair_schema()
    for pair in discovered["admitted_pairs"]:
        jsonschema.validate(pair, schema)


def test_rule_diff_report_schema_shape():
    schema = rule_diff_report_schema()
    sample = {
        "schema_version": "1",
        "pilot": "gitleaks",
        "admitted_pairs": 20,
        "timeouts": 0,
        "timeout_rate": 0.0,
        "engine_versions": {"z3": "5.0.0"},
        "results": [
            {
                "regex_id": "a" * 32,
                "pair_id": "x",
                "shape": 5,
                "result": "unsat",
                "declared_domain": "len 1..40",
                "ground_truth_status": "N/A",
                "wall_ms": 1.0,
                "schema_version": "1",
            }
        ],
    }
    jsonschema.validate(sample, schema)


def test_redact_witness_idempotent():
    import importlib.util

    path = ROOT / "scripts" / "rule-diff-pilot.py"
    spec = importlib.util.spec_from_file_location("rule_diff_pilot", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    once = mod._redact_witness({"s": "ghp_" + "A" * 36})
    assert once == {"s": "<redacted len=40>"}
    twice = mod._redact_witness(once)
    assert twice == once
