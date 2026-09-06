"""Smith GO for pass-culture-pass-culture-main (#391)."""

from __future__ import annotations

import json
from pathlib import Path

from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.manifests import CORPUS_MANIFESTS, WAVE_CORPORA

ROOT = Path(__file__).resolve().parents[1]
CORPUS = "pass-culture-pass-culture-main"
PIN = "14917fd0f8753933083fd379a7f9a0cc90bcc473"


def test_passculture_manifest_and_disclose_sync():
    assert CORPUS in CORPUS_MANIFESTS
    meta = CORPUS_MANIFESTS[CORPUS]
    assert meta["security_tool"] is False
    assert meta["dialect"] == "ecma"
    assert meta["extractor"] == "js_precise_dir"
    assert len(meta["files"]) == 361
    assert CORPUS not in SECURITY_TOOL_CORPORA
    assert CORPUS not in WAVE_CORPORA


def test_passculture_smith_decision_go():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_smith_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == CORPUS
    assert data["smith_decision"] == "go"
    assert data["corpus_pin"] == PIN


def test_passculture_fraction_complete():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_encodable_fraction.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["complete_run"] is True
    assert data["sample_size"] == 1589
    assert data["encodable"] == 1526
    assert abs(float(data["fraction"]) - 0.9604) < 1e-4


def test_passculture_gate_corpus_matches_filename():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_gate_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == "pass-culture-main"
    assert data["decision"] == "go"


def test_passculture_dry_run_no_private_no_public():
    path = ROOT / "properties" / "generated" / f"{CORPUS}-pr-dry-run.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["would_open_public_upstream_issue"] is False
    assert data["private_first_count"] == 0
    assert data["finding_count"] == 75
