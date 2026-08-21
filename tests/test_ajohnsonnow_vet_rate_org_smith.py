"""Smith GO for ajohnsonnow-vet-rate-org (#408)."""

from __future__ import annotations

import json
from pathlib import Path

from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.manifests import CORPUS_MANIFESTS, WAVE_CORPORA
from regexproof.batch.runner import check_admission_gates

ROOT = Path(__file__).resolve().parents[1]
CORPUS = "ajohnsonnow-vet-rate-org"
PIN = "1e9b252ca541f7a6b7f9eff7f82a99a4a055b8a7"


def test_vet_rate_manifest_and_disclose_sync():
    assert CORPUS in CORPUS_MANIFESTS
    meta = CORPUS_MANIFESTS[CORPUS]
    assert meta["security_tool"] is False
    assert meta["dialect"] == "ecma"
    assert meta["extractor"] == "js_precise_dir"
    assert meta["corpus_pin"] == PIN
    assert meta["commit"] == PIN
    assert len(meta["files"]) == 214
    assert CORPUS not in SECURITY_TOOL_CORPORA
    assert CORPUS not in WAVE_CORPORA


def test_vet_rate_smith_decision_go():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_smith_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == CORPUS
    assert data["smith_decision"] == "go"
    assert data["corpus_pin"] == PIN


def test_vet_rate_fraction_complete():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_encodable_fraction.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["complete_run"] is True
    assert data["sample_size"] == 2342
    assert data["encodable"] == 1408
    assert abs(float(data["fraction"]) - 0.6012) < 1e-4


def test_vet_rate_gate_corpus_matches_filename():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_gate_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == CORPUS
    assert data["corpus_pin"] == PIN
    assert data["decision"] == "go"
    assert check_admission_gates([CORPUS], out_dir=ROOT / "properties" / "generated") == []


def test_vet_rate_dry_run_no_public():
    path = ROOT / "properties" / "generated" / f"{CORPUS}-pr-dry-run.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["would_open_public_upstream_issue"] is False
    assert data["finding_count"] == 246
    assert data["private_first_count"] == 0
