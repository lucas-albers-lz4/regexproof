"""Phase 5 handoff pilot (PR, #221): the D14 fuzz + fwlive handoff contract.

AC coverage (issue #221, U9-amended):
- D14 fuzz suite runs with ZERO in-domain divergences on the pilot's probe set
  within the declared ASCII domain (regression evidence only)
- divergences OUTSIDE the domain are the documented boundary (NBSP/U+2028 \s
  gap) — recorded, not failures
- p5-pilot.md: every result carries property id, route, raw evidence, derived
  tier, and the destination mapping into the #120 pipeline
- U9 reopen trigger evaluated (six-pattern inventory unchanged → NOT hit)
- the full suite stays green (run via scripts/z3-verify.py --all)
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "sweep" / "harness-backends" / "p5-pilot.md"


def _run_pilot():
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "p5-handoff.py")],
        cwd=ROOT, check=False, capture_output=True, text=True, timeout=600,
    )


def test_d14_zero_in_domain_divergences():
    proc = _run_pilot()
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "- total in-domain divergences: 0" in proc.stdout


def test_pilot_contract_fields():
    # the committed pilot must carry the #120 handoff contract per result:
    # property id, route, raw evidence, derived tier, destination mapping —
    # ALL 12 records, ground-truthed by the real engine
    text = PILOT.read_text()
    assert "| property | pattern | probe | expect | route | result | tier | destination |" in text
    ids = ["fwlive-NON_FIREWALL_PREFIX-accept", "fwlive-NON_FIREWALL_PREFIX-reject",
           "fwlive-FIREWALL_HINT-accept", "fwlive-FIREWALL_HINT-reject",
           "fwlive-ACTION_RE-accept", "fwlive-ACTION_RE-reject",
           "fwlive-DENY_ACTION-accept", "fwlive-DENY_ACTION-reject",
           "fwlive-TCP_FLAG_TAIL-accept", "fwlive-TCP_FLAG_TAIL-reject",
           "fwlive-NETFILTER_KV_GLUE-accept", "fwlive-NETFILTER_KV_GLUE-reject"]
    for pid in ids:
        assert pid in text, pid
    assert "→ #120" in text
    assert "seq-only" in text  # every route is mirror; tier present
    assert "ground-truthed by the real JS engine" in text
    assert "reopen trigger: NOT hit" in text


def test_boundary_divergences_documented():
    proc = _run_pilot()
    assert "- boundary divergences: 7" in proc.stdout  # the measured \s gap


def test_full_suite_green():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "z3-verify.py"), "--all",
         "--require-ground-truth"],
        cwd=ROOT, check=False, capture_output=True, text=True, timeout=600,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
