"""cvc5 cross-check runner (design #213 D2/D12, Phase 3 PR A).

Ports the Phase-1-proven mechanics (cvc5_worker.py, merged via #222):

- Per-query process isolation (D2): the cvc5 C++ library segfaults in-process on
  re.loop text and on control-char literals (measured) — every query runs in a
  subprocess worker; the parent records abstain states and survives.
- InputParser discipline: `nextCommand()` returns a NULL command OBJECT (not
  None) — `if cmd.isNull(): break`; strip the shared text's trailing
  (check-sat) and run exactly ONE explicit checkSat (duplicated checks were a
  review finding on the Phase-1 baseline).
- tlimit-per budget per query; process-group kill on timeout.
- D12 re.loop bound cap: cvc5 cannot parse `(re.loop ...)` (measured "Symbol
  're.loop' not declared"); cross-check formulas containing a re.loop with
  bound > 16 are recorded as cross_check_abstained (reason re.loop-cap). The
  n<=16 bounded-loop expansion is the D12 spec — applied by the caller via
  expand_loops() below.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
import time

RELOOP_CAP = 16


class Cvc5Absent(Exception):
    """cvc5 is not importable in a worker (no wheel installed). The cross-check
    leg records cross_check_abstained (reason absent) — never a failure."""


def expand_loops(smt: str, cap: int = RELOOP_CAP) -> str:
    """D12 bounded-loop expansion: rewrite `(re.loop r n m)` occurrences with
    n <= cap into the explicit `(re.++ r r ...)` form cvc5 CAN parse. Loops
    with bound > cap are left untouched (the caller records the cap abstain).
    Returns (expanded_text, capped_loops_found)."""
    pattern = re.compile(
        r"\(re\.loop\s+((?:\([^()]*\)|[^()\s]+))\s+(\d+)(?:\s+(\d+))?\)"
    )
    capped = []

    def repl(m):
        r, lo = m.group(1), int(m.group(2))
        hi = int(m.group(3)) if m.group(3) else lo
        if lo > cap or hi > cap:
            capped.append(m.group(0))
            return m.group(0)
        # min..max repetition as union of concatenations (cvc5-parseable)
        parts = []
        for n in range(lo, hi + 1):
            parts.append("(re.++ " + " ".join([r] * n) + ")")
        return "(re.union " + " ".join(parts) + ")" if len(parts) > 1 else parts[0]

    out = pattern.sub(repl, smt)
    return out, capped


def run_cvc5(smt: str, timeout_ms: int = 30000, python: str | None = None) -> dict:
    """Run the cvc5 cross-check query in an isolated worker process. Returns
    the raw-evidence dict: {verdict, wall_ms, state, reason}.

    verdict: "sat" | "unsat" | "unknown" | "PARSE-ERROR" | "ABSTAIN-SIGSEGV" |
             "ABSTAIN-TIMEOUT" | "DISPATCH-ERROR"
    state: "decided" | "abstain"
    """
    worker = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "_cvc5_worker.py")
    fd, path = tempfile.mkstemp(suffix=".smt2")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(smt)
    except Exception:
        os.unlink(path)
        raise
    t0 = time.perf_counter()
    try:
        p = subprocess.Popen([python or sys.executable, worker, path,
                              str(timeout_ms)],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             text=True, start_new_session=True)
        try:
            out, _ = p.communicate(timeout=timeout_ms / 1000 + 10)
        except subprocess.TimeoutExpired:
            os.killpg(os.getpgid(p.pid), 9)
            try:
                out, _ = p.communicate()
            except Exception:
                out = ""
            return {"verdict": "ABSTAIN-TIMEOUT", "wall_ms": None,
                    "state": "abstain", "reason": "timeout"}
        rc = p.returncode
    except Exception as e:
        return {"verdict": f"DISPATCH-ERROR: {e}", "wall_ms": None,
                "state": "abstain", "reason": "dispatch"}
    finally:
        os.unlink(path)
    dt = round((time.perf_counter() - t0) * 1000, 1)
    if rc is not None and (rc < 0 or rc == 139):
        return {"verdict": f"ABSTAIN-SIGSEGV(rc={rc})", "wall_ms": dt,
                "state": "abstain", "reason": "sigsegv"}
    line = out.strip().splitlines()[-1] if out.strip() else "?"
    if line.startswith("V "):
        try:
            verdict, ms = line[2:].split()
            return {"verdict": verdict, "wall_ms": float(ms),
                    "state": "decided", "reason": None}
        except ValueError:
            pass
    if line.startswith("E "):
        return {"verdict": "PARSE-ERROR", "wall_ms": dt, "state": "abstain",
                "reason": line[2:][:100]}
    return {"verdict": f"ABSTAIN-NO-VERDICT(rc={rc})", "wall_ms": dt,
            "state": "abstain", "reason": "no-verdict"}
