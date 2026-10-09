"""Wave P0 (#555): freeze artifact determinism + population integrity.

The committed ``phase0_freeze.json`` / ``escape_baseline.json`` must be
byte-stable under regeneration (golden drift check in CI) and must match the
frozen gate-decision population (n=875, pos=121, Wilson 95% ~[11.7%, 16.3%],
with (url, pin) supersession dedup — older-pin decisions removed per
#560 Wave 3; funnel drain batch 4 removed 19 empty-walk auto-NO-GOs)."""

from __future__ import annotations

import importlib.util
import hashlib
import json
import pathlib
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
GEN = ROOT / "properties" / "generated"


def _load_bpf():
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "bpf", ROOT / "scripts" / "build-phase0-freeze.py",
    )
    bpf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bpf)  # type: ignore[union-attr]
    return bpf


@pytest.fixture(scope="module")
def freeze() -> dict:
    return json.loads((GEN / "phase0_freeze.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def baseline() -> dict:
    return json.loads((GEN / "escape_baseline.json").read_text(encoding="utf-8"))


def test_freeze_pins_the_pinned_population(freeze: dict):
    ds = freeze["dataset"]
    assert ds["n"] == 875
    assert ds["positive_count"] == 121
    assert ds["positive_rate"] == pytest.approx(121 / 875, abs=1e-6)
    assert ds["status_counts"]["go"] == 81
    assert ds["status_counts"]["triage-trial"] == 40


def test_escape_baseline_matches_design(freeze: dict, baseline: dict):
    lo, hi = baseline["wilson_ci_95"]
    assert lo == pytest.approx(0.11699, abs=0.001)
    assert hi == pytest.approx(0.162744, abs=0.001)
    # The baseline is the same fixed constant referenced by the freeze.
    assert baseline["survivor_rate"] == freeze["escape_baseline"]["value"]
    names = freeze["dataset"]["snapshot_files"]
    names_sha256 = hashlib.sha256("\n".join(names).encode("utf-8")).hexdigest()
    assert "phase0_freeze.json dataset.snapshot_files" in baseline["query"]
    assert f"n={len(names)}" in baseline["query"]
    assert names_sha256 in baseline["query"]
    assert "*_gate_decision.json" not in baseline["query"]


def test_freeze_k_is_frozen_a_priori(freeze: dict):
    assert freeze["eval"]["k_frozen"] == 30
    assert "no K search" in freeze["eval"]["k_note"]


def test_escape_protocol_is_predeclared(baseline: dict):
    t = baseline["test"]
    assert t["h0"] == "window_rate >= baseline"
    assert t["h1"].startswith("window_rate < baseline")
    assert t["significance"] == 0.05
    assert t["n_floor"] == 50
    assert "no low-yield unlock" in t["fire_action"]


def test_escape_protocol_records_test_revision(baseline: dict):
    rev = baseline["test_revision"]
    assert rev["date"] == "2026-08-24"
    assert "1/(2n)" in rev["to"]
    assert rev["implementation"] == "regexproof.stats.intervals.two_proportion_test"
    assert "p~=0.0544" in rev["effect"]
    assert "p~=0.0809" in rev["effect"]
    assert "0.0386" not in rev["effect"]
    assert "121/875" in rev["effect"]


def test_regeneration_is_byte_stable():
    """Regenerate and diff — the golden CI check must not drift."""
    before = {
        "freeze": (GEN / "phase0_freeze.json").read_bytes(),
        "baseline": (GEN / "escape_baseline.json").read_bytes(),
        "anchor": (GEN / "phase0_freeze.json.sha256").read_bytes(),
    }
    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build-phase0-freeze.py")],
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stderr
    after = {
        "freeze": (GEN / "phase0_freeze.json").read_bytes(),
        "baseline": (GEN / "escape_baseline.json").read_bytes(),
        "anchor": (GEN / "phase0_freeze.json.sha256").read_bytes(),
    }
    assert after == before, "freeze artifacts drift on regeneration"


def test_snapshot_hash_is_reproducible(freeze: dict):
    """The dataset hash must be reproducible from the committed files —
    via the SAME deduped population path the freeze uses (#560 Wave 3:
    (url, pin) supersession dedup applies to the hash too)."""
    import hashlib

    rows = _load_bpf().load_decision_population()
    h = hashlib.sha256()
    for r in sorted(rows, key=lambda r: r["file"]):
        h.update(r["file"].encode("utf-8"))
        h.update(b"\x00")
        h.update(json.dumps(r["payload"], sort_keys=True).encode("utf-8"))
        h.update(b"\n")
    assert h.hexdigest() == freeze["dataset"]["snapshot_sha256"]


def test_frozen_population_excludes_later_gate_decisions(freeze: dict):
    names = freeze["dataset"]["snapshot_files"]
    rows = _load_bpf().load_decision_population()
    live_names = {path.name for path in GEN.glob("*_gate_decision.json")}

    assert len(names) == 875
    assert names == sorted(set(names))
    assert {row["file"] for row in rows} <= set(names)
    assert set(names) < live_names
    assert "semgrep_rules_manager_gate_decision.json" not in names
    assert "wordpress_modsecurity_ruleset_gate_decision.json" not in names


def test_snapshot_hash_detects_any_decision_mutation():
    """Any change to a decision file's contents must change the hash — the
    reproducibility claim (status, url, pin, rationale, probe, conditions)."""
    import copy
    bpf = _load_bpf()
    rows = bpf.load_decision_population()
    original = bpf.snapshot_hash(rows)
    mutated_rows = copy.deepcopy(rows)
    assert mutated_rows, "expected frozen decision files"
    # Mutate a NON-status field that the old hash would have ignored.
    mutated_rows[0]["payload"]["rationale"] = "MUTATED-for-hash-test"
    assert bpf.snapshot_hash(mutated_rows) != original


def test_sha256_anchor_matches_freeze():
    anchor = (GEN / "phase0_freeze.json.sha256").read_text(encoding="utf-8").strip()
    import hashlib

    actual = hashlib.sha256(
        (GEN / "phase0_freeze.json").read_bytes()
    ).hexdigest()
    assert anchor == actual


def test_builder_fails_loud_on_malformed_decision(tmp_path: Path):
    """A malformed or status-less decision file must abort the build — the
    frozen population must never silently shrink (CodeRabbit)."""
    spec = importlib.util.spec_from_file_location(
        "build_p0", ROOT / "scripts" / "build-phase0-freeze.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # Malformed JSON → SystemExit.
    bad = GEN / "_zz_test_gate_decision.json"
    bad.write_text("{not json", encoding="utf-8")
    try:
        with pytest.raises(SystemExit, match="unreadable/invalid"):
            mod.load_decision_population(gen=GEN)
    finally:
        bad.unlink()

    # Status-less file → SystemExit.
    (GEN / "_zz_test_gate_decision.json").write_text(
        json.dumps({"candidate_url": "https://x/y"}), encoding="utf-8"
    )
    try:
        with pytest.raises(SystemExit, match="neither 'status'"):
            mod.load_decision_population(gen=GEN)
    finally:
        (GEN / "_zz_test_gate_decision.json").unlink()


def test_missing_freeze_requires_explicit_bootstrap(tmp_path: Path, monkeypatch):
    mod = _load_bpf()
    gen = tmp_path / "generated"
    gen.mkdir()
    (gen / "first_gate_decision.json").write_text(
        json.dumps(
            {
                "candidate_url": "https://example.test/repo",
                "corpus_pin": "abc",
                "decision": "no-go",
                "decision_date": "2026-10-01",
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(mod, "GEN", gen)
    monkeypatch.setattr(mod, "FREEZE_OUT", gen / "phase0_freeze.json")
    monkeypatch.setattr(mod, "BASELINE_OUT", gen / "escape_baseline.json")

    with pytest.raises(SystemExit, match="--bootstrap"):
        mod.main([])
    assert not (gen / "phase0_freeze.json").exists()

    assert mod.main(["--bootstrap"]) == 0
    freeze = json.loads((gen / "phase0_freeze.json").read_text(encoding="utf-8"))
    baseline = json.loads((gen / "escape_baseline.json").read_text(encoding="utf-8"))
    assert freeze["dataset"]["snapshot_files"] == ["first_gate_decision.json"]
    assert "phase0_freeze.json dataset.snapshot_files" in baseline["query"]

    with pytest.raises(SystemExit, match="only valid when"):
        mod.main(["--bootstrap"])
