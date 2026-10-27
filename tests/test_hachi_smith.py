"""Smith intake invariants for the pinned Kart1keya/Hachi corpus."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import pytest

from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.manifests import CORPUS_MANIFESTS, WAVE_CORPORA
from regexproof.batch.runner import _admission_gate_path, check_admission_gates

ROOT = Path(__file__).resolve().parents[1]
CORPUS = "Hachi"
PIN = "73e083e22f020ffa18ca5f09321ea19c4f7c4da4"


def test_hachi_manifest_matches_admitted_pin_and_private_first_policy():
    gate_path = ROOT / "properties" / "generated" / "Kart1keya-Hachi_gate_decision.json"
    gate = json.loads(gate_path.read_text(encoding="utf-8"))
    meta = CORPUS_MANIFESTS[CORPUS]

    assert gate["corpus"] == CORPUS
    assert gate["corpus_pin"] == PIN
    assert meta["repo"] == "Kart1keya/Hachi"
    assert meta["corpus_pin"] == PIN
    assert meta.get("commit") == PIN
    assert meta["dialect"] == "yara"
    assert meta["extractor"] == "yara"
    assert meta["security_tool"] is True
    assert CORPUS in SECURITY_TOOL_CORPORA
    assert CORPUS not in WAVE_CORPORA
    assert meta["path"] == ROOT / "batch" / "corpora" / CORPUS / "rules"
    readme = (ROOT / "batch" / "corpora" / CORPUS / "README.md").read_text(
        encoding="utf-8"
    )
    assert PIN in readme
    assert "--assert-determinism" in readme


def test_hachi_admission_check_uses_owner_prefixed_gate_without_copying_it():
    assert CORPUS_MANIFESTS[CORPUS].get("gate_decision_file") == (
        "Kart1keya-Hachi_gate_decision.json"
    )
    assert check_admission_gates(
        [CORPUS], out_dir=ROOT / "properties" / "generated"
    ) == []


@pytest.mark.parametrize(
    "filename",
    ["../outside.json", ".." + chr(92) + "outside.json", "C:" + chr(92) + "outside.json"],
)
def test_gate_decision_file_override_rejects_path_traversal(tmp_path, filename):
    with pytest.raises(ValueError, match="invalid gate_decision_file"):
        _admission_gate_path(CORPUS, {"gate_decision_file": filename}, tmp_path)


def test_hachi_smith_decision_and_fraction_are_complete():
    smith = json.loads(
        (ROOT / "properties" / "generated" / "Hachi_smith_decision.json").read_text(
            encoding="utf-8"
        )
    )
    fraction = json.loads(
        (ROOT / "properties" / "generated" / "Hachi_encodable_fraction.json").read_text(
            encoding="utf-8"
        )
    )

    assert smith["smith_decision"] == "go"
    assert smith["corpus_pin"] == PIN
    assert fraction["complete_run"] is True
    assert fraction["corpus_pin"] == PIN
    assert fraction["sample_size"] == 3087
    assert fraction["encodable"] == 2995
    assert fraction["unclassified_parse_errors"] == 0
    assert abs(float(fraction["fraction"]) - 0.9702) < 1e-4


def test_hachi_batch_triage_and_dry_run_stay_private():
    generated = ROOT / "properties" / "generated"
    summary = json.loads(
        (generated / "Hachi_batch_summary.json").read_text(encoding="utf-8")
    )
    findings = [
        json.loads(line)
        for line in (generated / "Hachi.ndjson").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    triage = [
        json.loads(line)
        for line in (ROOT / "properties" / "triage" / "Hachi.ndjson")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    dry_run = json.loads(
        (generated / "Hachi-pr-dry-run.json").read_text(encoding="utf-8")
    )

    assert summary["complete_run"] is True
    assert summary["extracted"] == 3087
    assert summary["encodable"] == 2995
    assert summary["triage"] == 92
    assert len(findings) == 4
    assert all(row["result"] == "planned" for row in findings)
    assert all(row["disclosure"] == "private_first" for row in findings)
    assert Counter(row["unencodable_reason"] for row in triage) == {
        "fullword-boundary": 62,
        "wide-non-literal": 29,
        "pattern-too-long": 1,
    }
    assert dry_run["finding_count"] == 4
    assert dry_run["private_first_count"] == 4
    assert dry_run["publish"] is False
    assert dry_run["would_open_public_upstream_issue"] is False
