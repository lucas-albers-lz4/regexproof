"""Wave P0 (#555): freeze artifact determinism + population integrity.

The committed ``phase0_freeze.json`` / ``escape_baseline.json`` must be
byte-stable under regeneration (golden drift check in CI) and must match the
real gate-decision population (n=854, pos=121, Wilson 95% ~[12.0%, 16.7%],
with (url, pin) supersession dedup — older-pin decisions removed per
#560 Wave 3; funnel drain 2026-08-27 added 10 NO-GOs)."""

from __future__ import annotations

import importlib.util
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
    assert ds["n"] == 854
    assert ds["positive_count"] == 121
    assert ds["positive_rate"] == pytest.approx(121 / 854, abs=1e-6)
    assert ds["status_counts"]["go"] == 81
    assert ds["status_counts"]["triage-trial"] == 40


def test_escape_baseline_matches_design(freeze: dict, baseline: dict):
    lo, hi = baseline["wilson_ci_95"]
    assert lo == pytest.approx(0.1199, abs=0.001)
    assert hi == pytest.approx(0.1667, abs=0.001)
    # The baseline is the same fixed constant referenced by the freeze.
    assert baseline["survivor_rate"] == freeze["escape_baseline"]["value"]


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
    assert "p~=0.0488" in rev["effect"]
    assert "p~=0.0730" in rev["effect"]
    assert "0.0386" not in rev["effect"]


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


def test_snapshot_hash_detects_any_decision_mutation():
    """Any change to a decision file's contents must change the hash — the
    reproducibility claim (status, url, pin, rationale, probe, conditions)."""
    import copy
    import hashlib

    freeze = json.loads((GEN / "phase0_freeze.json").read_text(encoding="utf-8"))
    original = freeze["dataset"]["snapshot_sha256"]
    files = sorted(GEN.glob("*_gate_decision.json"))
    assert files, "expected committed decision files"

    first = json.loads(files[0].read_text(encoding="utf-8"))
    mutated = copy.deepcopy(first)
    # Mutate a NON-status field that the old hash would have ignored.
    mutated["rationale"] = "MUTATED-for-hash-test"
    mutated_bytes = json.dumps(mutated, sort_keys=True).encode("utf-8")
    h = hashlib.sha256()
    for f in sorted(files):
        payload = (
            json.loads(mutated_bytes)
            if f.name == files[0].name
            else json.loads(f.read_text(encoding="utf-8"))
        )
        h.update(f.name.encode("utf-8"))
        h.update(b"\x00")
        h.update(json.dumps(payload, sort_keys=True).encode("utf-8"))
        h.update(b"\n")
    assert h.hexdigest() != original, "hash must change when a decision mutates"


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
            mod.load_decision_population()
    finally:
        bad.unlink()

    # Status-less file → SystemExit.
    (GEN / "_zz_test_gate_decision.json").write_text(
        json.dumps({"candidate_url": "https://x/y"}), encoding="utf-8"
    )
    try:
        with pytest.raises(SystemExit, match="neither 'status'"):
            mod.load_decision_population()
    finally:
        (GEN / "_zz_test_gate_decision.json").unlink()
