"""Smith GO for SveltyCMS-SveltyCMS (#396)."""

from __future__ import annotations

import json
from pathlib import Path

from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.manifests import CORPUS_MANIFESTS, WAVE_CORPORA
from regexproof.batch.runner import check_admission_gates

ROOT = Path(__file__).resolve().parents[1]
CORPUS = "SveltyCMS-SveltyCMS"
PIN = "c48326afe2a9d429f105af9aa786738d970af848"


def test_svelty_manifest_and_disclose_sync():
    assert CORPUS in CORPUS_MANIFESTS
    meta = CORPUS_MANIFESTS[CORPUS]
    assert meta["security_tool"] is False
    assert meta["dialect"] == "ecma"
    assert meta["extractor"] == "js_precise_dir"
    assert meta["corpus_pin"] == PIN
    assert meta["commit"] == PIN
    assert len(meta["files"]) == 231
    assert CORPUS not in SECURITY_TOOL_CORPORA
    assert CORPUS not in WAVE_CORPORA


def test_svelty_smith_decision_go():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_smith_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == CORPUS
    assert data["smith_decision"] == "go"
    assert data["corpus_pin"] == PIN


def test_svelty_fraction_complete():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_encodable_fraction.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["complete_run"] is True
    assert data["sample_size"] == 1275
    assert data["encodable"] == 701
    assert abs(float(data["fraction"]) - 0.5498) < 1e-4


def test_svelty_gate_corpus_matches_filename():
    path = ROOT / "properties" / "generated" / f"{CORPUS}_gate_decision.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["corpus"] == CORPUS
    assert data["corpus_pin"] == PIN
    assert data["decision"] == "go"
    assert check_admission_gates([CORPUS], out_dir=ROOT / "properties" / "generated") == []


def test_svelty_dry_run_no_public():
    path = ROOT / "properties" / "generated" / f"{CORPUS}-pr-dry-run.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["would_open_public_upstream_issue"] is False
    assert data["finding_count"] == 242
    assert data["private_first_count"] == 0
