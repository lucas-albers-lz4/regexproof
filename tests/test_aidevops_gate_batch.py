"""aidevops runtime gate + shell_posix manifest (conversion PR1)."""

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
PROBE = GENERATED / "marcusquinn-aidevops_gate_decision.json"
GATE = GENERATED / "aidevops_gate_decision.json"
# related/rationale are the xref; decision_date is the runtime-gate
# authoring date (probe stays 2026-08-13 / snapshot dated-2026-08-13).
_GATE_ONLY_TOP = frozenset({"related", "rationale", "decision_date"})


def test_aidevops_not_in_wave_corpora():
    assert "aidevops" in CORPUS_MANIFESTS
    assert "aidevops" not in WAVE_CORPORA
    meta = CORPUS_MANIFESTS["aidevops"]
    assert meta["extractor"] == "shell_posix"
    assert meta["dialect"] == "posix-shell"
    assert meta["security_tool"] is False
    assert meta["repo"] == "marcusquinn/aidevops"
    assert meta["corpus_pin"] == "8666b6c6c52472b5535aa295f2df593918152cb1"


def test_aidevops_runtime_gate_matches_probe_aside_from_related():
    assert GATE.is_file()
    probe = json.loads(PROBE.read_text(encoding="utf-8"))
    gate = json.loads(GATE.read_text(encoding="utf-8"))
    jsonschema.validate(instance=gate, schema=gate_decision_schema())
    assert gate["decision_date"] == "2026-08-26"
    for key in set(probe) | set(gate):
        if key in _GATE_ONLY_TOP:
            continue
        assert gate.get(key) == probe.get(key), f"drift on {key}"
    related = gate["related"]
    assert related.get("backfilled") is not True
    assert related["probe_path"] == (
        "properties/generated/marcusquinn-aidevops_gate_decision.json"
    )
    assert related["snapshot"] == "dated-2026-08-13"
    assert related["conversion_wave"] == "sweep/aidevops-conversion/plan.md"
    digest = hashlib.sha256(PROBE.read_bytes()).hexdigest()
    assert related["probe_sha256"] == digest


def test_aidevops_check_admission_gates_reads_runtime_gate(tmp_path):
    (tmp_path / GATE.name).write_bytes(GATE.read_bytes())
    assert check_admission_gates(["aidevops"], out_dir=tmp_path) == []
    probe_only = tmp_path / "probe_only"
    probe_only.mkdir()
    (probe_only / PROBE.name).write_bytes(PROBE.read_bytes())
    violations = check_admission_gates(["aidevops"], out_dir=probe_only)
    assert violations and "aidevops_gate_decision.json" in violations[0]


def test_aidevops_batch_summary_reconciles_with_probe():
    """Aggregate reconcile: |batch − probe posix-shell| / probe ≤ 10%.

    Probe ``regex_sites`` is mixed-dialect (12,880). P1 extractor is
    ``shell_posix``, so the denominator is ``probe.dialect.posix-shell``.
    """
    summary = json.loads(
        (GENERATED / "aidevops_batch_summary.json").read_text(encoding="utf-8")
    )
    probe = json.loads(PROBE.read_text(encoding="utf-8"))
    extracted = int(summary["extracted"])
    probe_n = int(probe["probe"]["dialect"]["posix-shell"])
    delta = abs(extracted - probe_n) / probe_n
    assert delta <= 0.10, f"extracted={extracted} probe={probe_n} delta={delta}"
    if summary.get("complete_run") is True:
        assert extracted > 0
        assert summary["encodable"] / extracted >= 0.30
