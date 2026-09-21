"""Forge CLI conversion-wave registration and sensitivity checks."""

from __future__ import annotations

import json
import re
from pathlib import Path

import jsonschema
from z3 import InRe, Length, Solver, String, StringVal, sat

from regexproof.harness import REGISTRY, check_mutation_coverage, run_one
from regexproof.harness.contract import product_reportable
from regexproof.harness.forge_cli import (
    DMM_VALUE_CHAR,
    DMM_VALUE_PATTERN,
    ENV_MATCH,
    ENV_PATTERN,
    ENV_POLICY_KEYS,
    ENV_PRODUCT,
    JAAS_MATCH,
    JAAS_PATTERN,
    JAAS_PRODUCT,
    LLM_USERINFO_CHAR,
    LLM_USERINFO_PATTERN,
    URL_PASSWORD_CHAR,
    URL_PASSWORD_PATTERN,
)
from regexproof.schemas import load_schema


FAMILY = "FC-forge-cli"
ROOT = Path(__file__).resolve().parents[1]
PRODUCT_NAMES = (
    "FC-forge-cli-url-password-no-space",
    "FC-forge-cli-dmm-value-no-semicolon",
    "FC-forge-cli-llm-userinfo-no-at",
    "FC-forge-cli-jaas-escaped-quote-covered",
    "FC-forge-cli-sensitive-env-key-covered",
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
    assert REGISTRY["FC-forge-cli-llm-userinfo-no-at"]["contract"]["site"].endswith(
        "providers.py:287:LlmConfig.redacted_endpoint"
    )


def test_forge_cli_properties_hold_and_mutation_guard_flips():
    for name in sorted(REGISTRY):
        if REGISTRY[name]["family"] != FAMILY:
            continue
        result = run_one(name, REGISTRY[name], require_ground_truth=True)
        assert result["result"] == (
            "sat" if REGISTRY[name]["kind"] == "mutation_guard" else "unsat"
        )
        assert result["not_proven"] is False
        if REGISTRY[name]["kind"] == "mutation_guard":
            assert result["ground_truth"] == "mutation-guard-sat-expected"


def test_forge_cli_family_has_mutation_coverage():
    assert check_mutation_coverage() == 0


def test_product_match_are_not_aliases():
    assert JAAS_PRODUCT is not JAAS_MATCH
    assert ENV_PRODUCT is not ENV_MATCH


def test_source_alphabets_agree_with_cpython_re():
    cases = (
        (URL_PASSWORD_PATTERN, URL_PASSWORD_CHAR, " "),
        (DMM_VALUE_PATTERN, DMM_VALUE_CHAR, ";"),
        (LLM_USERINFO_PATTERN, LLM_USERINFO_CHAR, "@"),
    )
    for pattern, alphabet, forbidden in cases:
        compiled = re.compile(pattern)
        for code in range(0x20, 0x7F):
            token = chr(code)
            source_ok = compiled.fullmatch(token) is not None
            solver = Solver()
            char = String("c")
            solver.add(InRe(char, alphabet), Length(char) == 1, char == StringVal(token))
            in_mirror = solver.check() == sat
            assert in_mirror is source_ok, (pattern, repr(token), in_mirror, source_ok)
            if token == forbidden:
                assert source_ok is False


def test_env_policy_keys_match_source_regex():
    compiled = re.compile(ENV_PATTERN)
    for key in ENV_POLICY_KEYS:
        assert compiled.search(key), key
        assert compiled.search(key.upper()), key


def test_jaas_escaped_quote_product_matches_source_and_not_naive():
    sample = 'sasl.jaas.config="secret\\"value"'
    assert re.compile(JAAS_PATTERN).search(sample)
    naive = re.compile(
        r'(?i)([\w.]{,64}sasl\.jaas\.config"?\s{,8}[:=]\s{,8}")([^"]{,2048})(")\Z'
    )
    assert naive.search(sample) is None


def test_committed_conversion_rows_match_registry():
    path = ROOT / "properties" / "generated" / "forge-cli_conversion.ndjson"
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    schema = load_schema("scanner_finding.schema.json")
    assert [row["name"] for row in rows] == sorted(PRODUCT_NAMES)
    for row in rows:
        jsonschema.validate(instance=row, schema=schema)
        assert row["family"] == FAMILY
        assert row["corpus"] == "forge-cli"
        assert row["wave_id"] == "forge-cli_w1"
        assert row["idiom_bucket"] == "secret-redaction"
        assert row["product_reportable"] is True
        assert row["result"] == "unsat"
        assert row["ground_truth_status"] is None
        assert row["engine_versions"]["z3"].startswith("5.0.")
        assert row["name"] in REGISTRY
        fresh = run_one(row["name"], REGISTRY[row["name"]])
        assert fresh["result"] == row["result"]


def test_wave_closeout_records_scope_and_next_step():
    path = ROOT / "properties" / "generated" / "forge-cli_conversion_wave.md"
    text = path.read_text(encoding="utf-8")
    assert "FC-forge-cli" in text
    assert "secret-redaction" in text
    assert "0 SAT" in text
    assert "providers.py:280" in text
    assert "Concat-identity" in text
