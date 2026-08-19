"""P3-B: probe-decision artifact validation (the consumer story test).

The OpenWrt probe decision is a PLAN-TIME admission artifact — consumed by
(a) this validator (schema + ACs), (b) the wave-close review, (c) the
follow-on stream kickoff that registers OpenWrt as a manifest corpus.  It is
NOT a runtime gate artifact (``check_admission_gates`` reads only
``{manifest_key}_gate_decision.json`` for manifest corpora).
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import jsonschema

from regexproof.batch.runner import check_admission_gates
from regexproof.schemas import gate_decision_schema

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "properties" / "generated"
PROBE_DECISION = GENERATED / "openwrt_packages_probe_decision.json"
GATE_DECISION = GENERATED / "openwrt_packages_gate_decision.json"

# Keys the runtime gate may add relative to the plan-time probe copy.
_GATE_ONLY_TOP = frozenset({"related", "rationale"})


def test_probe_decision_exists():
    assert PROBE_DECISION.exists(), (
        "P3-B authoring missing: properties/generated/"
        "openwrt_packages_probe_decision.json")


def test_probe_decision_validates_against_gate_schema():
    artifact = json.loads(PROBE_DECISION.read_text(encoding="utf-8"))
    jsonschema.validate(instance=artifact, schema=gate_decision_schema())


def test_probe_decision_go_new_surface_has_nonempty_buckets():
    """AC4: a go with condition new-surface carries NON-EMPTY
    probe.predicted_buckets (enforced at the tool — author-gate-decision.py
    refuses an empty-bucket go)."""
    artifact = json.loads(PROBE_DECISION.read_text(encoding="utf-8"))
    assert artifact["decision"] == "go"
    met = {c["id"] for c in artifact["conditions"] if c.get("met")}
    assert "new-surface" in met
    assert artifact["probe"]["predicted_buckets"], (
        "go + new-surface must carry non-empty predicted_buckets (AC4)")


def test_probe_decision_records_shell_evidence():
    """The merged-draft evidence survived authoring (regex_sites + the
    _shell_evidence provenance recorded by merge-probe-draft)."""
    artifact = json.loads(PROBE_DECISION.read_text(encoding="utf-8"))
    assert artifact["probe"]["regex_sites"] >= 680  # 688-site fold-adjusted count
    assert "posix-shell" in artifact["probe"]["dialect"]


def test_probe_decision_path_unchanged():
    """Consumer story: the plan-time probe stays at the probe filename."""
    assert PROBE_DECISION.name == "openwrt_packages_probe_decision.json"
    assert PROBE_DECISION.is_file()


def test_runtime_gate_exists_and_check_admission_gates_reads_it(tmp_path):
    """Runtime gate is openwrt_packages_gate_decision.json, not the probe."""
    assert GATE_DECISION.is_file()
    gate = json.loads(GATE_DECISION.read_text(encoding="utf-8"))
    jsonschema.validate(instance=gate, schema=gate_decision_schema())
    assert gate["decision"] == "go"
    assert gate["decision_date"] == "2026-08-12"
    assert gate["corpus"] == "openwrt_packages"
    related = gate["related"]
    assert related.get("backfilled") is not True
    assert related["probe_path"] == (
        "properties/generated/openwrt_packages_probe_decision.json"
    )
    assert related["snapshot"] == "dated-2026-08-12"
    assert related["conversion_wave"] == "sweep/openwrt-conversion/plan.md"
    digest = hashlib.sha256(PROBE_DECISION.read_bytes()).hexdigest()
    assert related["probe_sha256"] == digest

    # Sandbox copy — check_admission_gates reads out_dir, not GENERATED.
    (tmp_path / GATE_DECISION.name).write_bytes(GATE_DECISION.read_bytes())
    assert not (tmp_path / PROBE_DECISION.name).exists()
    assert check_admission_gates(["openwrt_packages"], out_dir=tmp_path) == []
    # Missing the gate filename (probe alone) must fail closed.
    probe_only = tmp_path / "probe_only"
    probe_only.mkdir()
    (probe_only / PROBE_DECISION.name).write_bytes(PROBE_DECISION.read_bytes())
    violations = check_admission_gates(["openwrt_packages"], out_dir=probe_only)
    assert violations and "openwrt_packages_gate_decision.json" in violations[0]


def test_runtime_gate_matches_probe_aside_from_related_xref():
    """Gate equals probe aside from related xref (+ rationale one-liner)."""
    probe = json.loads(PROBE_DECISION.read_text(encoding="utf-8"))
    gate = json.loads(GATE_DECISION.read_text(encoding="utf-8"))
    for key in set(probe) | set(gate):
        if key in _GATE_ONLY_TOP:
            continue
        assert gate.get(key) == probe.get(key), f"drift on {key}"
    assert "related" in gate
    assert gate["related"].get("backfilled") is not True


def test_probe_decision_is_not_a_runtime_gate_artifact():
    """Consumer story: check_admission_gates reads the gate file, not probe."""
    assert GATE_DECISION.name == "openwrt_packages_gate_decision.json"
    assert PROBE_DECISION.name != GATE_DECISION.name
