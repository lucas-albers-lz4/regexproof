"""Pinned corpus, fraction, and disclosure checks for #619's YARA phase."""

from __future__ import annotations

import json
from pathlib import Path
from collections import Counter

import pytest

from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.manifests import CORPUS_MANIFESTS, ROOT, WAVE_CORPORA


EXPECTED = {
    "freki": {
        "issue": 404,
        "pin": "08d593d447d27dc0794d0db68256fb1d6aecb607",
        "gate": "cristianzsh-freki_gate_decision.json",
        "path": ("freki", "app", "core", "yara_rules"),
        "sample_size": 11190,
        "encodable": 6187,
        "findings": 51,
        "triage": 5003,
        "max_patterns": 30000,
    },
    "BlueBox": {
        "issue": 416,
        "pin": "ff1563bc6e297247e30bb1509cf9c4f7385ac5af",
        "gate": "svdwi-BlueBox_gate_decision.json",
        "path": ("App", "yarascripts", "YaraScan", "rules"),
        "sample_size": 17525,
        "encodable": 11502,
        "findings": 71,
        "triage": 6023,
        "max_patterns": 30000,
    },
    "SentinelX": {
        "issue": 406,
        "pin": "9168547df5232067ac68eb9413f7248f89ccf8c1",
        "gate": "jaytiwari05-SentinelX_gate_decision.json",
        "path": (),
        "sample_size": 21287,
        "encodable": 13117,
        "findings": 86,
        "triage": 8170,
        "max_patterns": 30000,
    },
    "NetDefender": {
        "issue": 420,
        "pin": "88a81e76b19354f4e09fe47f153335da279458d4",
        "gate": "nipunsw1999-NetDefender_gate_decision.json",
        "path": (),
        "sample_size": 24310,
        "encodable": 14136,
        "findings": 98,
        "triage": 10174,
        "max_patterns": 30000,
    },
    "AegisMind": {
        "issue": 403,
        "pin": "cbb0b153216a4464c927bb3b84cb609fc8a41867",
        "gate": "Thinking-builder-AegisMind_gate_decision.json",
        "path": ("yara_rules",),
        "sample_size": 38309,
        "encodable": 23021,
        "findings": 155,
        "triage": 15288,
        "max_patterns": 50000,
    },
}


@pytest.mark.parametrize("corpus", EXPECTED)
def test_manifest_matches_gate_and_private_first_policy(corpus: str):
    expected = EXPECTED[corpus]
    meta = CORPUS_MANIFESTS[corpus]
    gate_path = ROOT / "properties" / "generated" / expected["gate"]
    gate = json.loads(gate_path.read_text(encoding="utf-8"))

    assert gate["corpus"] == corpus
    assert gate["corpus_pin"] == expected["pin"]
    assert meta["corpus_pin"] == expected["pin"]
    assert meta["commit"] == expected["pin"]
    assert meta["gate_decision_file"] == expected["gate"]
    assert meta["security_tool"] is True
    assert corpus in SECURITY_TOOL_CORPORA
    assert corpus not in WAVE_CORPORA
    assert meta["path"] == ROOT / "batch" / "corpora" / corpus / "rules" / Path(*expected["path"])
    assert meta["dialect"] == "yara"
    assert meta["budget"]["max_patterns"] == expected["max_patterns"]
    assert (ROOT / "batch" / "corpora" / corpus / "README.md").exists()
    assert (
        "## Compiler coverage buckets"
        in (ROOT / "batch" / "corpora" / corpus / "README.md").read_text()
    )


@pytest.mark.parametrize("corpus", EXPECTED)
def test_smith_fraction_batch_and_disclosure_artifacts_reconcile(corpus: str):
    expected = EXPECTED[corpus]
    generated = ROOT / "properties" / "generated"
    fraction = json.loads((generated / f"{corpus}_encodable_fraction.json").read_text())
    smith = json.loads((generated / f"{corpus}_smith_decision.json").read_text())
    summary = json.loads((generated / f"{corpus}_batch_summary.json").read_text())
    findings = [
        json.loads(line)
        for line in (generated / f"{corpus}.ndjson").read_text().splitlines()
        if line.strip()
    ]
    triage = [
        json.loads(line)
        for line in (ROOT / "properties" / "triage" / f"{corpus}.ndjson").read_text().splitlines()
        if line.strip()
    ]
    dry_run = json.loads((generated / f"{corpus}-pr-dry-run.json").read_text())

    assert fraction["complete_run"] is True
    assert fraction["corpus_pin"] == expected["pin"]
    assert fraction["sample_size"] == expected["sample_size"]
    assert fraction["encodable"] == expected["encodable"]
    assert fraction["unclassified_parse_errors"] == 0
    assert fraction["decision"] == "go"
    assert smith["corpus_pin"] == expected["pin"]
    assert smith["regex_sites"] == expected["sample_size"]
    assert smith["smith_decision"] == "go"

    assert summary["complete_run"] is True
    assert summary["extracted"] == expected["sample_size"]
    assert summary["encodable"] == expected["encodable"]
    assert summary["findings"] == expected["findings"]
    assert summary["inventory_questions"] == 4
    assert summary["redos_findings"] == 0
    assert len(triage) == expected["triage"]
    assert len(findings) == expected["findings"]
    assert Counter(row.get("disclosure") for row in findings) == {"private_first": len(findings)}
    assert all(row["result"] == "planned" for row in findings if row["kind"] == "property")
    assert dry_run["finding_count"] == len(findings)
    assert dry_run["private_first_count"] == len(findings)
    assert dry_run["publish"] is False
    assert dry_run["would_open_public_upstream_issue"] is False
