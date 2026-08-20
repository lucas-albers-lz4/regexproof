"""LuCI runtime gate + js_precise_dir htdocs glob (conversion PR B)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import jsonschema

from regexproof.batch.manifests import CORPUS_MANIFESTS, WAVE_CORPORA
from regexproof.batch.runner import check_admission_gates
from regexproof.schemas import gate_decision_schema

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "properties" / "generated"
PROBE = GENERATED / "openwrt_luci_probe_decision.json"
GATE = GENERATED / "openwrt_luci_gate_decision.json"
_GATE_ONLY_TOP = frozenset({"related", "rationale"})


def test_luci_not_in_wave_corpora():
    assert "openwrt_luci" in CORPUS_MANIFESTS
    assert "openwrt_luci" not in WAVE_CORPORA
    meta = CORPUS_MANIFESTS["openwrt_luci"]
    assert meta["extractor"] == "js_precise_dir"
    assert meta["dialect"] == "ecma"
    assert meta["security_tool"] is False
    assert "htdocs" in str(meta.get("glob") or "")


def test_luci_runtime_gate_matches_probe_aside_from_related():
    assert GATE.is_file()
    probe = json.loads(PROBE.read_text(encoding="utf-8"))
    gate = json.loads(GATE.read_text(encoding="utf-8"))
    jsonschema.validate(instance=gate, schema=gate_decision_schema())
    for key in set(probe) | set(gate):
        if key in _GATE_ONLY_TOP:
            continue
        assert gate.get(key) == probe.get(key), f"drift on {key}"
    related = gate["related"]
    assert related.get("backfilled") is not True
    assert related["probe_path"] == "properties/generated/openwrt_luci_probe_decision.json"
    assert related["snapshot"] == "dated-2026-08-20"
    assert related["conversion_wave"] == "sweep/openwrt-luci-conversion/plan.md"
    digest = hashlib.sha256(PROBE.read_bytes()).hexdigest()
    assert related["probe_sha256"] == digest


def test_luci_check_admission_gates_reads_runtime_gate(tmp_path):
    (tmp_path / GATE.name).write_bytes(GATE.read_bytes())
    assert check_admission_gates(["openwrt_luci"], out_dir=tmp_path) == []
    probe_only = tmp_path / "probe_only"
    probe_only.mkdir()
    (probe_only / PROBE.name).write_bytes(PROBE.read_bytes())
    violations = check_admission_gates(["openwrt_luci"], out_dir=probe_only)
    assert violations and "openwrt_luci_gate_decision.json" in violations[0]


def test_luci_batch_summary_reconciles_with_probe():
    """Aggregate reconcile: |batch − probe| / probe ≤ 10%."""
    summary = json.loads(
        (GENERATED / "openwrt_luci_batch_summary.json").read_text(encoding="utf-8")
    )
    probe = json.loads(PROBE.read_text(encoding="utf-8"))
    extracted = int(summary["extracted"])
    probe_n = int(probe["probe"]["regex_sites"])
    delta = abs(extracted - probe_n) / probe_n
    assert delta <= 0.10, f"extracted={extracted} probe={probe_n} delta={delta}"
    assert summary["complete_run"] is True
    assert summary["encodable"] / extracted >= 0.30


def test_js_precise_dir_glob_walks_nested(tmp_path, monkeypatch):
    """Regression: glob (not flat *.js) finds nested htdocs files."""
    from regexproof.batch import extract as extract_mod

    root = tmp_path / "repo"
    htdocs = root / "applications" / "luci-app-x" / "htdocs" / "luci-static"
    htdocs.mkdir(parents=True)
    (htdocs / "view.js").write_text("const re = /abc/;\n", encoding="utf-8")
    (htdocs / "skip.min.js").write_text("const re = /minned/;\n", encoding="utf-8")
    (root / "top.js").write_text("const re = /top/;\n", encoding="utf-8")
    monkeypatch.setattr(extract_mod, "ROOT", tmp_path)
    meta = {
        "repo": "test/luci",
        "extractor": "js_precise_dir",
        "glob": "**/htdocs/**/*.js,**/htdocs/**/*.mjs",
        "dialect": "ecma",
    }
    recs = extract_mod.extract_corpus("demo", {**meta, "path": root})
    pats = {r.get("pattern") for r in recs}
    assert "abc" in pats
    assert "minned" not in pats
    assert "top" not in pats
