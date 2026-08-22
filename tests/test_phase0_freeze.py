"""Wave P0 (#555): freeze artifact determinism + population integrity.

The committed ``phase0_freeze.json`` / ``escape_baseline.json`` must be
byte-stable under regeneration (golden drift check in CI) and must match the
real gate-decision population (n=853, pos=127, Wilson 95% [12.6%, 17.4%])."""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
GEN = ROOT / "properties" / "generated"


@pytest.fixture(scope="module")
def freeze() -> dict:
    return json.loads((GEN / "phase0_freeze.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def baseline() -> dict:
    return json.loads((GEN / "escape_baseline.json").read_text(encoding="utf-8"))


def test_freeze_pins_the_pinned_population(freeze: dict):
    ds = freeze["dataset"]
    assert ds["n"] == 853
    assert ds["positive_count"] == 127
    assert ds["positive_rate"] == pytest.approx(127 / 853, abs=1e-6)
    assert ds["status_counts"]["go"] == 82
    assert ds["status_counts"]["triage-trial"] == 45


def test_escape_baseline_matches_design(freeze: dict, baseline: dict):
    lo, hi = baseline["wilson_ci_95"]
    assert lo == pytest.approx(0.1266, abs=0.001)
    assert hi == pytest.approx(0.1743, abs=0.001)
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


def test_regeneration_is_byte_stable():
    """Regenerate and diff — the golden CI check must not drift."""
    before = {
        "freeze": (GEN / "phase0_freeze.json").read_bytes(),
        "baseline": (GEN / "escape_baseline.json").read_bytes(),
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
    }
    assert after == before, "freeze artifacts drift on regeneration"


def test_snapshot_hash_is_reproducible(freeze: dict):
    """The dataset hash must be reproducible from the committed files."""
    import hashlib

    files = sorted(GEN.glob("*_gate_decision.json"))
    rows = []
    for f in files:
        d = json.loads(f.read_text(encoding="utf-8"))
        status = str(d.get("status") or d.get("decision") or "")
        if status:
            rows.append(
                {"file": f.name, "url": d.get("candidate_url"), "status": status}
            )
    h = hashlib.sha256()
    for r in sorted(rows, key=lambda r: r["file"]):
        h.update(json.dumps(r, sort_keys=True).encode("utf-8"))
        h.update(b"\n")
    assert h.hexdigest() == freeze["dataset"]["snapshot_sha256"]
