"""Phase 3 cross-check leg (PR A): cvc5 runner, tier derivation, S3 guard.

AC coverage (issue #219, U9-amended):
- abstain-aware derivation: abstention never yields cross-checked (D5)
- S3 authority guard: a non-mirror route fails cross-checked assignment
  (synthetic-route unit test — the ECMA leg no longer exists post-U9-DROP)
- leg ABSENT → tier capped escalated-unconfirmed (never a silent skip)
- decomposed forms consumed from the property's own sexpr with D12 bounded-loop
  expansion (cap n <= 16); capped loops → cross_check_abstained
- verification tier DERIVED at report time; NDJSON storage raw-only (S15)
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from regexproof.harness import core
from regexproof.harness.cvc5_runner import expand_loops
from regexproof.harness.tiers import (
    TIER_CROSS_CHECKED,
    TIER_ESCALATED,
    TIER_SEQ_ONLY,
    derive_tier,
)

ROOT = Path(__file__).resolve().parents[1]
CVC5_PY = "/tmp/cvc5venv/bin/python"
HAVE_CVC5 = os.path.isfile(CVC5_PY)


# --- tier derivation ---------------------------------------------------------
def test_derive_seq_only():
    assert derive_tier({"backend": "seq", "not_proven": False}) == TIER_SEQ_ONLY


def test_derive_escalated_leg_absent():
    r = {"backend": "noodler", "route": "mirror", "not_proven": False,
         "noodler_verdict": "unsat", "state": "decided"}
    assert derive_tier(r) == TIER_ESCALATED  # cross-check leg absent


def test_derive_cross_checked_agree():
    r = {"backend": "noodler", "route": "mirror", "not_proven": False,
         "noodler_verdict": "unsat", "cross_check_verdict": "unsat"}
    assert derive_tier(r) == TIER_CROSS_CHECKED


def test_derive_abstain_never_cross_checked():
    r = {"backend": "noodler", "route": "mirror", "not_proven": True,
         "noodler_verdict": "ABSTAIN-TIMEOUT"}
    assert derive_tier(r) == TIER_ESCALATED
    r2 = {"backend": "noodler", "route": "mirror", "not_proven": False,
          "noodler_verdict": "unsat", "cross_check_abstained": True}
    assert derive_tier(r2) == TIER_ESCALATED


def test_derive_s3_guard_non_mirror_route():
    # S3 authority guard: cross-checked REQUIRES route:"mirror" — a synthetic
    # non-mirror record must fail the assignment even with agreeing verdicts.
    r = {"backend": "noodler", "route": "ecma", "not_proven": False,
         "noodler_verdict": "unsat", "cross_check_verdict": "unsat"}
    assert derive_tier(r) == TIER_ESCALATED


def test_derive_disagreement_never_cross_checked():
    r = {"backend": "noodler", "route": "mirror", "not_proven": False,
         "noodler_verdict": "sat", "cross_check_verdict": "unsat"}
    assert derive_tier(r) == TIER_ESCALATED


# --- D12 bounded-loop expansion ---------------------------------------------
def test_expand_loops_within_cap():
    smt = "(assert (str.in_re s (re.loop (str.to_re \"a\") 2 3)))\n(check-sat)\n"
    out, capped = expand_loops(smt)
    assert capped == []
    assert "(re.loop" not in out
    assert "re.union" in out  # the 2..3 repetition union


def test_expand_loops_over_cap_abstains():
    smt = "(assert (str.in_re s (re.loop (str.to_re \"a\") 17)))\n(check-sat)\n"
    out, capped = expand_loops(smt)
    assert len(capped) == 1  # bound > 16 → capped, left untouched
    assert "(re.loop" in out


# --- NDJSON raw-only + legacy report tier -----------------------------------
def test_ndjson_still_raw_only():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "z3-verify.py"), "--json",
         "P1-space"],
        cwd=ROOT, check=False, capture_output=True, text=True,
    )
    rec = json.loads(proc.stdout.splitlines()[0])
    assert "verification_tier" not in rec  # NDJSON storage is raw (S15)


def test_legacy_report_has_derived_tier():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "z3-verify.py"), "--json-legacy",
         "P1-space"],
        cwd=ROOT, check=False, capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stderr
    report = json.loads(proc.stdout)
    assert report[0]["verification_tier"] == TIER_SEQ_ONLY


# --- real cvc5 cross-check (skip if the cvc5 venv is absent) ----------------
@pytest.mark.skipif(not HAVE_CVC5, reason="cvc5 venv not present")
def test_cross_check_leg_decides_with_cvc5(monkeypatch):
    import regexproof.harness.properties  # noqa: F401

    old = os.environ.get("PYTHONPATH")
    os.environ["PYTHONPATH"] = "/tmp/cvc5venv/lib/python3.13/site-packages"
    try:
        entry = dict(core.REGISTRY["P1-space"])
        entry["backend"] = "noodler"
        r = core.run_one("P1-space", entry)
    finally:
        if old is None:
            os.environ.pop("PYTHONPATH", None)
        else:
            os.environ["PYTHONPATH"] = old
    assert r["result"] in ("unsat", "sat")
    assert r.get("cross_check_backend") == "cvc5"
    # either agreed (verdict present) or honestly abstained — never a lie
    if r.get("cross_check_abstained"):
        assert r["cross_check_reason"]
    else:
        assert r["cross_check_verdict"] in ("sat", "unsat", "unknown")
    assert derive_tier(r) in (TIER_CROSS_CHECKED, TIER_ESCALATED)
