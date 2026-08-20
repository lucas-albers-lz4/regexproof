"""LuCI plan-time probe decision (Gate 0) — schema + admission honesty."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from regexproof.schemas import gate_decision_schema

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "properties" / "generated"
PROBE = GENERATED / "openwrt_luci_probe_decision.json"
PLAN = ROOT / "sweep" / "openwrt-luci-conversion" / "plan.md"
PROBE_MD = ROOT / "sweep" / "openwrt-luci-conversion" / "probe.md"
NDJSON = ROOT / "sweep" / "openwrt-luci-conversion" / "probe_records.ndjson"


def test_luci_probe_decision_exists_and_validates():
    assert PROBE.is_file()
    artifact = json.loads(PROBE.read_text(encoding="utf-8"))
    jsonschema.validate(instance=artifact, schema=gate_decision_schema())


def test_luci_probe_go_on_security_boundary_not_new_surface():
    artifact = json.loads(PROBE.read_text(encoding="utf-8"))
    assert artifact["decision"] == "go"
    assert artifact["decision_basis"] == "admission_conditions"
    assert artifact["escape_hatch_applied"] is False
    assert artifact["corpus"] == "openwrt_luci"
    assert artifact["corpus_pin"] == "77dad3f31405bc11f8384d742f7ad95314179694"
    met = {c["id"]: c["met"] for c in artifact["conditions"]}
    assert met["security-boundary"] is True
    assert met["new-surface"] is False
    assert met["large-under-saturated"] is False
    assert artifact["probe"]["regex_sites"] == 895
    assert artifact["probe"]["dialect"] == {"ecma": 895}
    assert artifact["probe"]["security_boundary"] == "deterministic-true"


def test_luci_probe_artifacts_present():
    assert PLAN.is_file()
    assert PROBE_MD.is_file()
    assert NDJSON.is_file()
    lines = [ln for ln in NDJSON.read_text(encoding="utf-8").splitlines() if ln.strip()]
    assert len(lines) == 895
