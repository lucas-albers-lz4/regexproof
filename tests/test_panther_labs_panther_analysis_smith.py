"""Smith GO for panther-labs-panther-analysis (#387)."""

from __future__ import annotations

import json
from pathlib import Path

from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.manifests import CORPUS_MANIFESTS, WAVE_CORPORA

ROOT = Path(__file__).resolve().parents[1]
CORPUS = "panther-labs-panther-analysis"


def test_panther_manifest_and_disclose_sync():
    assert CORPUS in CORPUS_MANIFESTS
    meta = CORPUS_MANIFESTS[CORPUS]
    assert meta["security_tool"] is True
    assert meta["dialect"] == "py_re"
    assert meta["extractor"] == "python_dir"
    assert CORPUS in SECURITY_TOOL_CORPORA
    assert CORPUS not in WAVE_CORPORA


def test_panther_smith_decision_go():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_smith_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == CORPUS
    assert data["smith_decision"] == "go"
    assert data["corpus_pin"] == meta_pin()


def meta_pin() -> str:
    return str(CORPUS_MANIFESTS[CORPUS]["corpus_pin"])


def test_panther_fraction_complete():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_encodable_fraction.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["complete_run"] is True
    assert data["sample_size"] == 57
    assert data["encodable"] == 37
    assert abs(float(data["fraction"]) - 0.6491) < 1e-4


def test_panther_gate_corpus_matches_filename():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_gate_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == CORPUS
    assert data["decision"] == "triage-trial"


def test_panther_dry_run_private_first():
    path = ROOT / "properties" / "generated" / f"{CORPUS}-pr-dry-run.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["would_open_public_upstream_issue"] is False
    assert data["private_first_count"] == data["finding_count"] == 22
