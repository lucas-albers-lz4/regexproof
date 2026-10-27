"""Gate-scoped evidence for the largest #619 YARA admission (#419)."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from regexproof.batch.budgets import BUDGET_HEAVY_60K, budget_as_dict
from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.manifests import CORPUS_MANIFESTS, ROOT, WAVE_CORPORA


CORPUS = "Inboxscanner"
PIN = "cafc3dcc92557192204c0479450731a3e7528388"
GATE_FILE = "ag-michael-Inboxscanner_gate_decision.json"
EXPECTED_SITES = 51250
EXPECTED_ENCODABLE = 30553
EXPECTED_FILES = 1860
EXPECTED_FINDINGS = 189
EXPECTED_TRIAGE_ROWS = EXPECTED_SITES - EXPECTED_ENCODABLE


def _gate() -> dict:
    return json.loads(
        (ROOT / "properties" / "generated" / GATE_FILE).read_text(encoding="utf-8")
    )


def test_manifest_allowlist_matches_gate_yara_inventory_and_budget():
    gate = _gate()
    meta = CORPUS_MANIFESTS[CORPUS]
    expected_files = sorted(
        path
        for path in gate["probe"]["regex_sites_per_file"]
        if Path(path).suffix.lower() in {".yar", ".yara"}
    )

    assert gate["corpus"] == CORPUS
    assert gate["corpus_pin"] == PIN
    assert meta["corpus_pin"] == PIN
    assert meta["commit"] == PIN
    assert meta["gate_decision_file"] == GATE_FILE
    assert meta["path"] == ROOT / "batch" / "corpora" / CORPUS / "rules"
    assert meta["files"] == expected_files
    assert len(meta["files"]) == EXPECTED_FILES
    assert sum(gate["probe"]["regex_sites_per_file"][p] for p in expected_files) == EXPECTED_SITES
    assert all(Path(path).suffix.lower() in {".yar", ".yara"} for path in meta["files"])
    assert all("vendor" not in Path(path).parts for path in meta["files"])
    assert any(Path(path).suffix == ".YAR" for path in meta["files"])
    assert meta["budget"] == budget_as_dict(BUDGET_HEAVY_60K)
    assert meta["security_tool"] is True
    assert CORPUS in SECURITY_TOOL_CORPORA
    assert CORPUS not in WAVE_CORPORA


def test_measured_inventory_matches_gate_per_file_and_private_first_triage():
    generated = ROOT / "properties" / "generated"
    gate_files = {
        path: count
        for path, count in _gate()["probe"]["regex_sites_per_file"].items()
        if Path(path).suffix.lower() in {".yar", ".yara"}
    }
    inventory = [
        json.loads(line)
        for line in (generated / f"{CORPUS}-inventory.ndjson")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    actual_files: Counter[str] = Counter()
    prefix = f"batch/corpora/{CORPUS}/rules/"
    for row in inventory:
        path = row["site"].rsplit(":", 2)[0]
        assert path.startswith(prefix), path
        actual_files[path[len(prefix) :]] += 1
    fraction = json.loads(
        (generated / f"{CORPUS}_encodable_fraction.json").read_text(encoding="utf-8")
    )
    smith = json.loads(
        (generated / f"{CORPUS}_smith_decision.json").read_text(encoding="utf-8")
    )
    summary = json.loads(
        (generated / f"{CORPUS}_batch_summary.json").read_text(encoding="utf-8")
    )
    findings = [
        json.loads(line)
        for line in (generated / f"{CORPUS}.ndjson").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    triage = [
        json.loads(line)
        for line in (ROOT / "properties" / "triage" / f"{CORPUS}.ndjson")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    dry_run = json.loads(
        (generated / f"{CORPUS}-pr-dry-run.json").read_text(encoding="utf-8")
    )

    assert actual_files == Counter(gate_files)
    assert len(inventory) == EXPECTED_SITES
    assert fraction["complete_run"] is True
    assert fraction["corpus_pin"] == PIN
    assert fraction["sample_size"] == EXPECTED_SITES
    assert fraction["encodable"] == EXPECTED_ENCODABLE
    assert fraction["unclassified_parse_errors"] == 0
    assert fraction["budget_breaches"] is None
    assert fraction["decision"] == "go"
    assert smith["corpus_pin"] == PIN
    assert smith["regex_sites"] == EXPECTED_SITES
    assert smith["smith_decision"] == "go"
    assert summary["complete_run"] is True
    assert summary["extracted"] == EXPECTED_SITES
    assert summary["encodable"] == EXPECTED_ENCODABLE
    assert summary["findings"] == EXPECTED_FINDINGS
    assert summary["inventory_questions"] == 4
    assert summary["redos_findings"] == 0
    assert len(triage) == EXPECTED_TRIAGE_ROWS
    assert len(findings) == EXPECTED_FINDINGS
    assert Counter(row.get("disclosure") for row in findings) == {
        "private_first": EXPECTED_FINDINGS
    }
    planned_properties = [row for row in findings if row["kind"] == "property"]
    assert len(planned_properties) == 4
    assert all(row["result"] == "planned" for row in planned_properties)
    assert dry_run["private_first_count"] == EXPECTED_FINDINGS
    assert dry_run["publish"] is False
    assert dry_run["would_open_public_upstream_issue"] is False
