"""claude-code-plugins conversion-wave harness family + ledger join."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from regexproof.harness.contract import product_reportable
from regexproof.harness.core import REGISTRY, check_mutation_coverage
import regexproof.harness.claude_code_plugins  # noqa: F401 — register family
from regexproof.schemas import load_schema

ROOT = Path(__file__).resolve().parents[1]
FAMILY = "AI-claude-plugins"
PRODUCT_NAMES = (
    "AI-claude-plugins-cli-flag-no-semicolon",
    "AI-claude-plugins-skill-ref-no-semicolon",
    "AI-claude-plugins-git-clean-e-bundle-no-semicolon",
)


def test_ai_claude_plugins_family_in_registry_and_mutation_coverage():
    assert any(e.get("family") == FAMILY for e in REGISTRY.values())
    for name in PRODUCT_NAMES:
        assert name in REGISTRY
        assert REGISTRY[name]["family"] == FAMILY
        assert product_reportable(REGISTRY[name]) is True
    guard = "AI-claude-plugins-mutated-cli-flag-semicolon"
    assert REGISTRY[guard]["family"] == FAMILY
    assert REGISTRY[guard]["kind"] == "mutation_guard"
    assert product_reportable(REGISTRY[guard]) is False
    assert check_mutation_coverage() == 0


def test_ai_claude_plugins_contracts_validate_schema():
    schema = load_schema("property_contract.schema.json")
    for name in PRODUCT_NAMES:
        contract = REGISTRY[name]["contract"]
        jsonschema.validate(instance=contract, schema=schema)
        assert contract["provenance"] == "human"


def test_proof_job_runs_busybox_claude_code_plugins_checker():
    yml = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "ci-check-busybox-claude-code-plugins.py" in yml
    assert "BusyBox claude-code-plugins hook replay" in yml
    proof = yml.split("name: Z3 proof harness", 1)[1].split("golden:", 1)[0]
    assert "--require-contract" in proof
    assert "--require-ground-truth" in proof


def test_committed_conversion_ndjson_matches_registry():
    path = ROOT / "properties" / "generated" / "claude-code-plugins_conversion.ndjson"
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
        assert row["corpus"] == "claude-code-plugins"
        assert row["product_reportable"] is True
        ev = row.get("engine_versions")
        assert isinstance(ev, dict)
        assert ev.get("python")
        assert ev.get("z3")
        assert row["idiom_bucket"] == "plugin-hook-guards"
        assert row["wave_id"] == "claude-code-plugins_w1"


def test_rank_json_frozen():
    path = ROOT / "properties" / "generated" / "claude-code-plugins_rank.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == "claude-code-plugins"
    assert len(data["keep"]) == 15
    assert data["path_filter"] == "plugins/guardrails/hooks/"
    assert data["bucket"] == "plugin-hook-guards"
    assert all(
        "plugins/guardrails/hooks/" in str(k.get("file") or k.get("site") or "")
        for k in data["keep"]
    )
    assert all(
        ".test.sh" not in str(k.get("file") or k.get("site") or "")
        for k in data["keep"]
    )


def test_wave_closeout_exists():
    path = ROOT / "properties" / "generated" / "claude-code-plugins_conversion_wave.md"
    text = path.read_text(encoding="utf-8")
    assert "AI-claude-plugins" in text
    assert "asked" in text.lower()
    assert "plugin-hook-guards" in text
    assert "ECMA" in text
    assert "ecma-plugins" in text
