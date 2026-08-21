"""Smith GO for lintendo-Axhub-Make (#390)."""

from __future__ import annotations

import json
from pathlib import Path

from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.manifests import CORPUS_MANIFESTS, WAVE_CORPORA
from regexproof.batch.runner import check_admission_gates

ROOT = Path(__file__).resolve().parents[1]
CORPUS = "lintendo-Axhub-Make"
PIN = "bc10e311028d5e72752de97187ff690b2095f466"


def test_axhub_manifest_and_disclose_sync():
    assert CORPUS in CORPUS_MANIFESTS
    meta = CORPUS_MANIFESTS[CORPUS]
    assert meta["security_tool"] is False
    assert meta["dialect"] == "ecma"
    assert meta["extractor"] == "js_precise_dir"
    assert meta["corpus_pin"] == PIN
    assert meta["commit"] == PIN
    assert len(meta["files"]) == 314
    assert CORPUS not in SECURITY_TOOL_CORPORA
    assert CORPUS not in WAVE_CORPORA


def test_axhub_smith_decision_go():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_smith_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == CORPUS
    assert data["smith_decision"] == "go"
    assert data["corpus_pin"] == PIN


def test_axhub_fraction_complete():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_encodable_fraction.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["complete_run"] is True
    assert data["sample_size"] == 2596
    assert data["encodable"] == 790
    assert abs(float(data["fraction"]) - 0.3043) < 1e-4


def test_axhub_gate_corpus_matches_filename():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_gate_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == CORPUS
    assert data["corpus_pin"] == PIN
    assert data["decision"] == "go"
    assert check_admission_gates([CORPUS], out_dir=ROOT / "properties" / "generated") == []


def test_axhub_dry_run_no_public():
    path = ROOT / "properties" / "generated" / f"{CORPUS}-pr-dry-run.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["would_open_public_upstream_issue"] is False
    assert data["finding_count"] == 571
    assert data["private_first_count"] == 0
