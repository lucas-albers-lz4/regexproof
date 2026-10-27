"""Evidence and disclosure checks for the first four #619 admissions."""

from __future__ import annotations

import json
from collections import Counter

import pytest

from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.manifests import CORPUS_MANIFESTS, ROOT, WAVE_CORPORA


EXPECTED = {
    "Yara-Rules": {
        "pin": "9034e24193b38aad1fbc0912ace3683eb5728a92",
        "gate": "The-DFIR-Report-Yara-Rules_gate_decision.json",
        "decision": "no-go",
        "sample_size": 3565,
        "encodable": 681,
    },
    "lw-yara": {
        "pin": "efd3cdaecae091357087fea6ecffded2eb6dba85",
        "gate": "Hestat-lw-yara_gate_decision.json",
        "decision": "go",
        "sample_size": 4394,
        "encodable": 1410,
    },
    "bernstein": {
        "pin": "be3b073da9bb44e4c4bb35faed634380d5a9936f",
        "gate": "sipyourdrink-ltd-bernstein_gate_decision.json",
        "decision": "go",
        "sample_size": 1002,
        "encodable": 549,
        "files": 302,
    },
    "lyrie-ai": {
        "pin": "96048f6727c01760850e5ef5e1526c8cb9061db8",
        "gate": "OTT-Cybersecurity-LLC-lyrie-ai_gate_decision.json",
        "decision": "go",
        "sample_size": 1589,
        "encodable": 913,
        "files": 191,
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
    assert meta["path"] == ROOT / "batch" / "corpora" / corpus / "rules"
    if "files" in expected:
        assert len(meta["files"]) == expected["files"]


@pytest.mark.parametrize("corpus", EXPECTED)
def test_smith_fraction_batch_and_disclosure_artifacts_reconcile(corpus: str):
    expected = EXPECTED[corpus]
    generated = ROOT / "properties" / "generated"
    fraction = json.loads(
        (generated / f"{corpus}_encodable_fraction.json").read_text(encoding="utf-8")
    )
    smith = json.loads(
        (generated / f"{corpus}_smith_decision.json").read_text(encoding="utf-8")
    )
    summary = json.loads(
        (generated / f"{corpus}_batch_summary.json").read_text(encoding="utf-8")
    )
    findings = [
        json.loads(line)
        for line in (generated / f"{corpus}.ndjson").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    triage = [
        json.loads(line)
        for line in (ROOT / "properties" / "triage" / f"{corpus}.ndjson")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    dry_run = json.loads(
        (generated / f"{corpus}-pr-dry-run.json").read_text(encoding="utf-8")
    )

    assert fraction["complete_run"] is True
    assert fraction["corpus_pin"] == expected["pin"]
    assert fraction["sample_size"] == expected["sample_size"]
    assert fraction["encodable"] == expected["encodable"]
    assert fraction["unclassified_parse_errors"] == 0
    assert fraction["decision"] == expected["decision"]
    assert smith["corpus_pin"] == expected["pin"]
    assert smith["regex_sites"] == expected["sample_size"]
    assert smith["smith_decision"] == expected["decision"]

    assert summary["complete_run"] is True
    assert summary["extracted"] == expected["sample_size"]
    assert summary["encodable"] == expected["encodable"]
    assert len(triage) == expected["sample_size"] - expected["encodable"]
    assert findings
    assert Counter(row.get("disclosure") for row in findings) == {
        "private_first": len(findings)
    }
    assert all(
        row["result"] == "planned"
        for row in findings
        if row["kind"] == "property"
    )
    assert dry_run["finding_count"] == len(findings)
    assert dry_run["private_first_count"] == len(findings)
    assert dry_run["publish"] is False
    assert dry_run["would_open_public_upstream_issue"] is False
