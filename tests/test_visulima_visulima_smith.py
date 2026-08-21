"""Smith GO for visulima-visulima (#398)."""

from __future__ import annotations

import json
from pathlib import Path

from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.manifests import CORPUS_MANIFESTS, WAVE_CORPORA

ROOT = Path(__file__).resolve().parents[1]
CORPUS = "visulima-visulima"
PIN = "50ce4889c75d82b4d7ad5f54a0fdf5142b06c710"


def test_visulima_manifest_and_disclose_sync():
    assert CORPUS in CORPUS_MANIFESTS
    meta = CORPUS_MANIFESTS[CORPUS]
    assert meta["security_tool"] is False
    assert meta["dialect"] == "ecma"
    assert meta["extractor"] == "js_precise_dir"
    assert len(meta["files"]) == 548
    assert CORPUS not in SECURITY_TOOL_CORPORA
    assert CORPUS not in WAVE_CORPORA


def test_visulima_smith_decision_go():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_smith_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == CORPUS
    assert data["smith_decision"] == "go"
    assert data["corpus_pin"] == PIN


def test_visulima_fraction_complete():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_encodable_fraction.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["complete_run"] is True
    assert data["sample_size"] == 1704
    assert data["encodable"] == 1006
    assert abs(float(data["fraction"]) - 0.5904) < 1e-4


def test_visulima_gate_corpus_matches_filename():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_gate_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == CORPUS
    assert data["decision"] == "go"


def test_visulima_dry_run_no_public():
    path = ROOT / "properties" / "generated" / f"{CORPUS}-pr-dry-run.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["would_open_public_upstream_issue"] is False
    assert data["finding_count"] == 596
    assert data["private_first_count"] == 0
