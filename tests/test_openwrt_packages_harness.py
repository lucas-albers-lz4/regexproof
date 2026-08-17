"""OpenWrt packages conversion-wave harness family + ledger join."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from regexproof.harness.contract import product_reportable
from regexproof.harness.core import REGISTRY, check_mutation_coverage
import regexproof.harness.openwrt_packages  # noqa: F401 — register family
from regexproof.schemas import load_schema

ROOT = Path(__file__).resolve().parents[1]
FAMILY = "OW-packages"
PRODUCT_NAMES = (
    "OW-packages-hostname-no-semicolon",
    "OW-packages-hostname-no-space",
    "OW-packages-banip-expiry-no-semicolon",
    "OW-packages-transip-token-truncation",
    "OW-packages-wan-mark-hex-capture",
)


def test_ow_packages_family_in_registry_and_mutation_coverage():
    assert any(e.get("family") == FAMILY for e in REGISTRY.values())
    for name in PRODUCT_NAMES:
        assert name in REGISTRY
        assert REGISTRY[name]["family"] == FAMILY
        assert product_reportable(REGISTRY[name]) is True
    guard = "OW-packages-mutated-hostname-semicolon"
    assert REGISTRY[guard]["family"] == FAMILY
    assert REGISTRY[guard]["kind"] == "mutation_guard"
    assert product_reportable(REGISTRY[guard]) is False
    assert check_mutation_coverage() == 0


def test_ow_contracts_validate_schema():
    schema = load_schema("property_contract.schema.json")
    for name in PRODUCT_NAMES:
        contract = REGISTRY[name]["contract"]
        jsonschema.validate(instance=contract, schema=schema)
        assert contract["provenance"] == "human"


def test_proof_job_installs_busybox_and_require_contract():
    yml = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    proof = yml.split("name: Z3 proof harness", 1)[1].split("golden:", 1)[0]
    assert "busybox" in proof
    assert "--require-contract" in proof
    assert "BusyBox OpenWrt dual replay" in yml
    assert "ci-check-busybox-openwrt.py" in yml


def test_committed_conversion_ndjson_matches_registry():
    path = ROOT / "properties" / "generated" / "openwrt_packages_conversion.ndjson"
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    schema = load_schema("scanner_finding.schema.json")
    names = {r["name"] for r in rows}
    assert names == set(PRODUCT_NAMES)
    assert 1 <= len(rows) <= 5
    for rec in rows:
        jsonschema.validate(instance=rec, schema=schema)
        assert rec.get("domain")
        assert rec["contract"]["provenance"] == "human"
        assert rec["product_reportable"] is True
        assert rec.get("synthesized") is False
        assert rec["name"] in REGISTRY
        assert rec["result"] == (
            "sat" if not REGISTRY[rec["name"]]["expect_unsat"] else "unsat"
        )


def test_incomplete_contract_is_not_product_reportable():
    entry = {
        "kind": "property",
        "domain": "ascii labels",
        "contract": {
            "schema_version": "1",
            "site": "x",
            "guarantee": "",
            "input_source": "y",
            "trust": "config",
            "declared_domain": "ascii",
            "provenance": "human",
        },
    }
    assert product_reportable(entry) is False
    entry["contract"]["guarantee"] = "no semicolon"
    entry["contract"]["provenance"] = "agent_derived"
    assert product_reportable(entry) is False
