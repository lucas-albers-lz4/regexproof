"""OpenWrt LuCI conversion-wave harness family + ledger join."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from regexproof.harness.contract import product_reportable
from regexproof.harness.core import REGISTRY, check_mutation_coverage
import regexproof.harness.openwrt_luci  # noqa: F401 — register family
from regexproof.schemas import load_schema

ROOT = Path(__file__).resolve().parents[1]
FAMILY = "OW-luci"
PRODUCT_NAMES = (
    "OW-luci-adblock-tcpdump-filter-no-semicolon",
    "OW-luci-netdevname-semicolon-admitted",
    "OW-luci-firewall-mark-no-semicolon",
    "OW-luci-dockerman-publish-host-capture",
)


def test_ow_luci_family_in_registry_and_mutation_coverage():
    assert any(e.get("family") == FAMILY for e in REGISTRY.values())
    for name in PRODUCT_NAMES:
        assert name in REGISTRY
        assert REGISTRY[name]["family"] == FAMILY
        assert product_reportable(REGISTRY[name]) is True
    guard = "OW-luci-mutated-adblock-filter-semicolon"
    assert REGISTRY[guard]["family"] == FAMILY
    assert REGISTRY[guard]["kind"] == "mutation_guard"
    assert product_reportable(REGISTRY[guard]) is False
    assert check_mutation_coverage() == 0


def test_ow_luci_contracts_validate_schema():
    schema = load_schema("property_contract.schema.json")
    for name in PRODUCT_NAMES:
        contract = REGISTRY[name]["contract"]
        jsonschema.validate(instance=contract, schema=schema)
        assert contract["provenance"] == "human"


def test_proof_job_runs_node_luci_checker():
    yml = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "ci-check-node-openwrt-luci.py" in yml
    assert "Node OpenWrt LuCI RegExp replay" in yml
    proof = yml.split("name: Z3 proof harness", 1)[1].split("golden:", 1)[0]
    assert "--require-contract" in proof
    assert "--require-ground-truth" in proof


def test_committed_conversion_ndjson_matches_registry():
    path = ROOT / "properties" / "generated" / "openwrt_luci_conversion.ndjson"
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert len(rows) == len(PRODUCT_NAMES)
    names = {r["name"] for r in rows}
    assert names == set(PRODUCT_NAMES)
    for row in rows:
        assert row["family"] == FAMILY
        assert row["corpus"] == "openwrt_luci"
        assert row["product_reportable"] is True


def test_rank_json_frozen():
    path = ROOT / "properties" / "generated" / "openwrt_luci_rank.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == "openwrt_luci"
    assert len(data["keep"]) == 15
    assert "validation-netdevname" in data["seeds"]


def test_wave_closeout_exists():
    path = ROOT / "properties" / "generated" / "openwrt_luci_conversion_wave.md"
    text = path.read_text(encoding="utf-8")
    assert "OW-luci" in text
    assert "asked" in text.lower()
