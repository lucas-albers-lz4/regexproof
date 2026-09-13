"""Smith triage-trial for semgrep ENGINE (#386)."""

from __future__ import annotations

import json
from pathlib import Path

from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.manifests import CORPUS_MANIFESTS, WAVE_CORPORA

ROOT = Path(__file__).resolve().parents[1]
CORPUS = "semgrep-semgrep"
PIN = "cc97b5c47dacabe76be343ef981204b8c1f60e07"


def test_semgrep_engine_manifest_and_disclose_sync():
    assert CORPUS in CORPUS_MANIFESTS
    meta = CORPUS_MANIFESTS[CORPUS]
    assert meta["security_tool"] is True
    assert meta["dialect"] == "ecma"
    assert meta["extractor"] == "js_precise_dir"
    assert len(meta["files"]) == 10
    assert CORPUS in SECURITY_TOOL_CORPORA
    assert CORPUS not in WAVE_CORPORA


def test_semgrep_engine_smith_decision_go():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_smith_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == CORPUS
    assert data["smith_decision"] == "go"
    assert data["corpus_pin"] == PIN


def test_semgrep_engine_fraction_complete():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_encodable_fraction.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["complete_run"] is True
    assert data["sample_size"] == 12
    assert data["encodable"] == 5
    assert abs(float(data["fraction"]) - 0.4167) < 1e-4


def test_semgrep_engine_gate_corpus_matches_filename():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_gate_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == "semgrep"
    assert data["decision"] == "triage-trial"


def test_semgrep_engine_dry_run_private_first():
    path = ROOT / "properties" / "generated" / f"{CORPUS}-pr-dry-run.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["would_open_public_upstream_issue"] is False
    assert data["private_first_count"] == data["finding_count"] == 4
