"""Pin the AlienVaultLabs measurement and Smith no-go (#405)."""

from __future__ import annotations

import json
from pathlib import Path

from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.manifests import CORPUS_MANIFESTS, WAVE_CORPORA

ROOT = Path(__file__).resolve().parents[1]
CORPUS = "AlienVaultLabs"
PIN = "347a57b31829b6f8e3280e0fd6a0ed49e5453c67"


def test_alienvaultlabs_measurement_is_pinned_and_distinct_from_smith_decision():
    meta = CORPUS_MANIFESTS[CORPUS]
    generated = ROOT / "properties" / "generated"
    gate = json.loads(
        (generated / f"{CORPUS}_gate_decision.json").read_text(encoding="utf-8")
    )
    smith = json.loads(
        (generated / f"{CORPUS}_smith_decision.json").read_text(encoding="utf-8")
    )
    fraction = json.loads(
        (generated / f"{CORPUS}_encodable_fraction.json").read_text(encoding="utf-8")
    )

    assert meta["repo"] == "AlienVault-Labs/AlienVaultLabs"
    assert meta["corpus_pin"] == PIN
    assert meta.get("commit") == PIN
    assert meta["path"] == ROOT / "batch" / "corpora" / CORPUS / "rules"
    assert meta["security_tool"] is True
    assert CORPUS in SECURITY_TOOL_CORPORA
    assert CORPUS not in WAVE_CORPORA

    assert gate["corpus"] == CORPUS
    assert gate["corpus_pin"] == PIN
    assert gate["decision"] == "go"
    assert smith["corpus"] == CORPUS
    assert smith["corpus_pin"] == PIN
    assert smith["smith_decision"] == "no-go"
    assert "novelty collapse" in smith["reason"].lower()

    assert fraction["pilot"] == CORPUS
    assert fraction["corpus_pin"] == PIN
    assert fraction["commit"] == PIN
    assert fraction["scope"] == "full_corpus"
    assert fraction["complete_run"] is True
    assert fraction["sample_size"] == 1463
    assert fraction["encodable"] == 1447
    assert fraction["fraction"] == 0.9891
    assert fraction["decision"] == "go"
    assert fraction["budget_breaches"] is None
    assert fraction["unclassified_parse_errors"] == 0
    inventory = [
        json.loads(line)
        for line in (ROOT / fraction["inventory_path"])
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    assert len(inventory) == fraction["sample_size"]
    assert sum(bool(row["encodable"]) for row in inventory) == fraction["encodable"]
    assert all(row["corpus"] == CORPUS for row in inventory)

    # The high compiler-coverage result is not a reversal of the later Smith
    # no-go, which is based on cross-corpus novelty collapse.
    readme = (ROOT / "batch" / "corpora" / CORPUS / "README.md").read_text(
        encoding="utf-8"
    )
    assert PIN in readme
    assert "## Materialize" in readme
    assert "## Measure" in readme
    assert "--corpus AlienVaultLabs --assert-determinism" in readme
    assert "Do not run" in readme
