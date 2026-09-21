"""Forge CLI conversion-wave registration and sensitivity checks."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from regexproof.harness import REGISTRY, check_mutation_coverage, run_one
from regexproof.harness.contract import product_reportable
from regexproof.schemas import load_schema


FAMILY = "FC-forge-cli"
ROOT = Path(__file__).resolve().parents[1]
PRODUCT_NAMES = (
    "FC-forge-cli-url-userinfo-coverage",
    "FC-forge-cli-jaas-escaped-quote-coverage",
    "FC-forge-cli-sensitive-env-key-coverage",
    "FC-forge-cli-dmm-error-secret-coverage",
    "FC-forge-cli-llm-query-secret-coverage",
)


def test_forge_cli_contracts_are_registered_and_human_adopted():
    entries = [entry for entry in REGISTRY.values() if entry["family"] == FAMILY]
    assert len(entries) == 6
    properties = [entry for entry in entries if entry["kind"] == "property"]
    assert len(properties) == 5
    assert all(entry["contract"]["provenance"] == "human" for entry in properties)
    assert all(entry["input_domain"] == "ascii" for entry in entries)
    schema = load_schema("property_contract.schema.json")
    for entry in properties:
        jsonschema.validate(instance=entry["contract"], schema=schema)
        assert product_reportable(entry) is True


def test_forge_cli_properties_hold_and_mutation_guard_flips():
    for name in sorted(REGISTRY):
        if REGISTRY[name]["family"] != FAMILY:
            continue
        result = run_one(name, REGISTRY[name])
        assert result["result"] == ("sat" if REGISTRY[name]["kind"] == "mutation_guard" else "unsat")
        assert result["not_proven"] is False


def test_forge_cli_family_has_mutation_coverage():
    assert check_mutation_coverage() == 0


def test_committed_conversion_rows_match_registry():
    path = ROOT / "properties" / "generated" / "forge-cli_conversion.ndjson"
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert [row["name"] for row in rows] == sorted(PRODUCT_NAMES)
    for row in rows:
        assert row["family"] == FAMILY
        assert row["corpus"] == "forge-cli"
        assert row["wave_id"] == "forge-cli_w1"
        assert row["idiom_bucket"] == "secret-redaction"
        assert row["product_reportable"] is True
        assert row["result"] == "unsat"
        assert row["ground_truth_status"] is None
        assert row["engine_versions"]["z3"].startswith("5.0.")


def test_wave_closeout_records_scope_and_next_step():
    path = ROOT / "properties" / "generated" / "forge-cli_conversion_wave.md"
    text = path.read_text(encoding="utf-8")
    assert "FC-forge-cli" in text
    assert "secret-redaction" in text
    assert "0 SAT" in text
    assert "source checkout" in text
