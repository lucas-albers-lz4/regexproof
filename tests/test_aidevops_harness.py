"""aidevops conversion-wave harness family + ledger join."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from regexproof.harness.contract import product_reportable
from regexproof.harness.core import REGISTRY, check_mutation_coverage
import regexproof.harness.aidevops  # noqa: F401 — register family
from regexproof.schemas import load_schema

ROOT = Path(__file__).resolve().parents[1]
FAMILY = "AI-aidevops"
PRODUCT_NAMES = (
    "AI-aidevops-brief-tid-no-semicolon",
    "AI-aidevops-cred-ident-no-semicolon",
    "AI-aidevops-scope-heading-no-semicolon",
    "AI-aidevops-brief-tid-capture",
    "AI-aidevops-gh-issue-digit-capture",
)


def test_ai_aidevops_family_in_registry_and_mutation_coverage():
    assert any(e.get("family") == FAMILY for e in REGISTRY.values())
    for name in PRODUCT_NAMES:
        assert name in REGISTRY
        assert REGISTRY[name]["family"] == FAMILY
        assert product_reportable(REGISTRY[name]) is True
    guard = "AI-aidevops-mutated-brief-tid-semicolon"
    assert REGISTRY[guard]["family"] == FAMILY
    assert REGISTRY[guard]["kind"] == "mutation_guard"
    assert product_reportable(REGISTRY[guard]) is False
    assert check_mutation_coverage() == 0


def test_ai_aidevops_contracts_validate_schema():
    schema = load_schema("property_contract.schema.json")
    for name in PRODUCT_NAMES:
        contract = REGISTRY[name]["contract"]
        jsonschema.validate(instance=contract, schema=schema)
        assert contract["provenance"] == "human"


def test_proof_job_runs_busybox_aidevops_checker():
    yml = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "ci-check-busybox-aidevops.py" in yml
    assert "BusyBox aidevops hook replay" in yml
    proof = yml.split("name: Z3 proof harness", 1)[1].split("golden:", 1)[0]
    assert "--require-contract" in proof
    assert "--require-ground-truth" in proof


def test_committed_conversion_ndjson_matches_registry():
    path = ROOT / "properties" / "generated" / "aidevops_conversion.ndjson"
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
        assert row["corpus"] == "aidevops"
        assert row["product_reportable"] is True
        assert row["idiom_bucket"] == "shell-hook-guards"
        assert row["wave_id"] == "aidevops_w1"


def test_rank_json_frozen():
    path = ROOT / "properties" / "generated" / "aidevops_rank.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == "aidevops"
    assert len(data["keep"]) == 15
    assert data["path_filter"] == ".agents/hooks/"
    assert data["bucket"] == "shell-hook-guards"
    assert all(".agents/hooks/" in str(k.get("file") or k.get("site") or "") for k in data["keep"])


def test_wave_closeout_exists():
    path = ROOT / "properties" / "generated" / "aidevops_conversion_wave.md"
    text = path.read_text(encoding="utf-8")
    assert "AI-aidevops" in text
    assert "asked" in text.lower()
    assert "shell-hook-guards" in text
    assert "ECMA" in text
    assert ".agents/plugins" in text
