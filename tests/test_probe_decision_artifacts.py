"""P3-B: probe-decision artifact validation (the consumer story test).

The OpenWrt probe decision is a PLAN-TIME admission artifact — consumed by
(a) this validator (schema + ACs), (b) the wave-close review, (c) the
follow-on stream kickoff that registers OpenWrt as a manifest corpus.  It is
NOT a runtime gate artifact (``check_admission_gates`` reads only
``{manifest_key}_gate_decision.json`` for manifest corpora — the shell
corpus's own admission lives in ``dogfood_shell_gate_decision.json``).
"""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

from regexproof.schemas import gate_decision_schema

PROBE_DECISION = (
    Path(__file__).resolve().parents[1]
    / "properties" / "generated" / "openwrt_packages_probe_decision.json"
)


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
    assert artifact["probe"]["regex_sites"] >= 700  # the 713-site feed count
    assert "posix-shell" in artifact["probe"]["dialect"]


def test_probe_decision_is_not_a_runtime_gate_artifact():
    """Consumer story: the probe decision is plan-time — the runtime gate
    reads the SHELL corpus's manifest gate decision, not this file."""
    gate = (
        Path(__file__).resolve().parents[1]
        / "properties" / "generated" / "dogfood_shell_gate_decision.json"
    )
    if not gate.exists():
        pytest.skip("dogfood_shell gate decision lands with P2c (#273)")
    g = json.loads(gate.read_text(encoding="utf-8"))
    assert g["corpus"] == "dogfood_shell"
    assert g["decision"] == "go"
