"""Phase 2 operator contract (PR C): the §10 base states + exit codes.

AC coverage (issue #218):
- Base states implemented and tested: stock, fallback, escalation,
  solver-abstain, not-proven — including the synthetic-crash abstain path.
- Exit-code convention: 0 = recorded, 1 = not-proven (#186); disagreement = 2
  is Phase 3 (tested there).
- Record schema unchanged for the stock-only consumer (additive backend/state
  fields only); NO verification tier in consumer-facing output (S15 — the
  schema check REJECTS a stored tier field).
- Fallback (noodler absent) keeps the exit unchanged from stock.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from regexproof.harness import core

ROOT = Path(__file__).resolve().parents[1]

TIER_FIELDS = ("tier", "verification_tier", "cross_check_tier", "trust_tier")


def cli_exit(result: dict) -> int:
    """The CLI exit mapping (cli.py): 1 if any result is not ok (incl.
    not_proven), else 0. Mirrors the §10 convention: 0 recorded / 1 not-proven."""
    return 1 if not result.get("ok") else 0


# --- base-state matrix -------------------------------------------------------
def test_state_stock_decided():
    entry = dict(core.REGISTRY["P1-space"])
    entry["backend"] = "seq"
    r = core.run_one("P1-space", entry)
    assert r["state"] == "stock"
    assert r["ok"] is True
    assert cli_exit(r) == 0  # recorded, holds


def test_state_not_proven_timeout():
    # A property that times out is not-proven → exit 1 (#186).
    entry = dict(core.REGISTRY["P2-actor-whitelist"])
    entry["timeout_ms"] = 1  # force unknown
    r = core.run_one("P2-actor-whitelist", entry)
    assert r["state"] == "not-proven"
    assert r["not_proven"] is True
    assert cli_exit(r) == 1


def test_state_solver_abstain_synthetic_crash(monkeypatch, tmp_path):
    # The synthetic-crash abstain path: a SIGSEGV'd solver is an abstain →
    # not-proven → exit 1 (recorded, never a wrong verdict).
    import regexproof.harness.noodler_runner as nr

    stub = tmp_path / "crash.sh"
    stub.write_text("#!/bin/bash\necho 'sat'\nkill -SEGV $$\n")
    stub.chmod(stub.stat().st_mode | 0o111)

    def _binary():
        return str(stub)

    monkeypatch.setattr(nr, "binary_path", _binary)
    monkeypatch.setattr(nr, "_VERIFIED_PATH", str(stub))
    import regexproof.harness.properties  # noqa: F401

    entry = dict(core.REGISTRY["P1-mutated-star"])
    entry["backend"] = "noodler"
    r = core.run_one("P1-mutated-star", entry)
    assert r["state"].startswith("ABSTAIN-SIGSEGV")
    assert r["not_proven"] is True
    assert cli_exit(r) == 1


def test_state_fallback_exit_unchanged_from_stock(monkeypatch):
    # Absence → the stock path runs; exit reflects the STOCK result (0).
    import regexproof.harness.noodler_runner as nr

    def _absent():
        raise nr.NoodlerAbsent("absent (test)")

    monkeypatch.setattr(nr, "binary_path", _absent)
    import regexproof.harness.properties  # noqa: F401

    entry = dict(core.REGISTRY["P1-mutated-star"])
    entry["backend"] = "noodler"
    r = core.run_one("P1-mutated-star", entry)
    assert r["state"] == "noodler-absent"
    assert r["ok"] is True  # the stock verdict — exit 0, unchanged from stock
    assert cli_exit(r) == 0


@pytest.mark.skipif(
    not os.path.isfile(os.environ.get("NOODLER", "/tmp/noodler/z3-noodler-ubuntu-24.04-x86_64-shared")),
    reason="pinned Noodler binary not present",
)
def test_state_escalation_recorded():
    # A noodler-decided property: recorded → exit per ok (0 when holds).
    import regexproof.harness.properties  # noqa: F401

    entry = dict(core.REGISTRY["P1-space"])
    entry["backend"] = "noodler"
    r = core.run_one("P1-space", entry)
    assert r["state"] == "decided"
    assert r["ok"] is True
    assert cli_exit(r) == 0


# --- no stored tier in consumer-facing output (S15) -------------------------
def test_ndjson_has_no_tier_field():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "z3-verify.py"), "--json", "P1-space"],
        cwd=ROOT, check=False, capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stderr
    rec = json.loads(proc.stdout.splitlines()[0])
    for t in TIER_FIELDS:
        assert t not in rec, f"stored tier field {t!r} in NDJSON (S15 violation)"


def test_schema_unchanged_for_stock_consumer():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "z3-verify.py"), "--json", "P1-space"],
        cwd=ROOT, check=False, capture_output=True, text=True,
    )
    rec = json.loads(proc.stdout.splitlines()[0])
    # additive fields only: the pre-existing schema keys must all be present
    for k in ("schema_version", "name", "kind", "family", "result", "ok",
              "not_proven", "ground_truth", "expect_unsat", "wall_ms",
              "engine_versions", "domain", "witness"):
        assert k in rec, k
