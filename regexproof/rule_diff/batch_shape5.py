"""Admit and run shape-5 pairs in batch (#477).

Admission is only ``version_diff`` / ``cross_engine`` with a ``family_contract``.
Independent-spec gitleaks pairs stay out. Fullmatch SAT is then gated by the
search/pad matrix; a fullmatch-only SAT is recorded, not a search gap.
"""

from __future__ import annotations

import time
from typing import Any

from z3 import Solver, StringVal, sat, unsat, unknown

from regexproof.compiler import compile_pattern
from regexproof.harness.core import z3_str
from regexproof.rule_diff.encode import shape5_constraints
from regexproof.rule_diff.search_replay import gate_sat_witness

SCALE_PROVENANCE = frozenset({"version_diff", "cross_engine"})
# compile_pattern(max_length=) caps *pattern text*, not witness length.
_PATTERN_CHAR_CAP = 256
# CRS 941140/942220: five models still flipped sat↔fullmatch on Python 3.13.
# Issue #524: 16 was still flaky under load — the model enumeration loop stops
# at the first `unknown` (timeout) once `best` is set, so a borderline solve
# flipping between sat and sat_fullmatch_only changed the batch summaries
# between the two reproducibility runs. A larger cap gives the pad-gate more
# distinct witnesses to confirm on before the loop settles.
_PAD_GATE_MODEL_CAP = 64
# Issue #524: crs-941140 solves in ~9–26s on a quiet machine but crossed the
# 30s per-check budget under CI load → `unknown` → `timeout` classification.
# 120s is a 4–13x headroom over the observed solve time, so the batch outcome
# is deterministic rather than load-dependent.
_BATCH_SOLVE_TIMEOUT_MS = 120_000
# Hard wall-clock deadline for the whole solve of a single pair, independent of
# the per-check timeout and the model cap. The enumeration loop can issue up to
# _PAD_GATE_MODEL_CAP checks, each with a fresh _BATCH_SOLVE_TIMEOUT_MS budget;
# without a ceiling that product (64 × 120s ≈ 128 min/pair) could exceed the
# Golden CI job's 60-minute limit (luna r1, issue #524). This deadline bounds
# every pair, and with 3 admitted CRS pairs the shape-5 batch stays well under
# the job budget.
_BATCH_SOLVE_DEADLINE_MS = 240_000


def provenance_token(pair: dict[str, Any]) -> str:
    raw = pair.get("provenance")
    if isinstance(raw, str) and raw.strip():
        return raw.strip()
    if isinstance(raw, dict):
        for key in ("kind", "pair_kind"):
            val = str(raw.get(key) or "").strip()
            if val:
                return val
    return str(pair.get("pair_kind") or "").strip()


def valid_family_contract(fc: Any) -> bool:
    if not isinstance(fc, dict):
        return False
    return bool(
        str(fc.get("R1") or "").strip()
        and str(fc.get("R2") or "").strip()
        and str(fc.get("provenance") or "").strip()
    )


def admit_shape5_for_batch(pair: dict[str, Any]) -> bool:
    if provenance_token(pair) not in SCALE_PROVENANCE:
        return False
    return valid_family_contract(pair.get("family_contract"))


def filter_batch_pairs(pairs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [p for p in pairs if admit_shape5_for_batch(p)]


def summarize_shape5_rows(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts = {
        "executed": len(rows),
        "sat_search_gap": 0,
        "sat_fullmatch_only": 0,
        "unsat": 0,
        "timeout": 0,
        "skipped": 0,
    }
    for rec in rows:
        result = rec.get("result")
        if result == "sat":
            counts["sat_search_gap"] += 1
        elif result == "sat_fullmatch_only":
            counts["sat_fullmatch_only"] += 1
        elif result == "unsat":
            counts["unsat"] += 1
        elif result == "timeout":
            counts["timeout"] += 1
        else:
            counts["skipped"] += 1
    return counts


def run_batch_shape5_pairs(
    pairs: list[dict[str, Any]],
    *,
    timeout_ms: int = _BATCH_SOLVE_TIMEOUT_MS,
) -> list[dict[str, Any]]:
    """Fullmatch solve + search/pad SAT gate for admitted pairs only."""
    return [_solve_one(pair, timeout_ms=timeout_ms) for pair in filter_batch_pairs(pairs)]


def _solve_one(pair: dict[str, Any], *, timeout_ms: int) -> dict[str, Any]:
    r1 = pair.get("r1") or {}
    r2 = pair.get("r2") or {}
    max_len = int(pair.get("max_len") or 16)
    rec: dict[str, Any] = {
        "schema_version": "1",
        "kind": "rule_diff",
        "pair_id": pair.get("pair_id"),
        "family": pair.get("family"),
        "search_pad_gate": None,
        "witness": None,
        "result": None,
    }
    r1_pat = str(r1.get("pattern") or "")
    r2_pat = str(r2.get("pattern") or "")
    r1_c = compile_pattern(
        r1_pat,
        str(r1.get("flags") or ""),
        str(r1.get("dialect") or "py_re"),
        "fullmatch",
        max_length=max(_PATTERN_CHAR_CAP, len(r1_pat)),
    )
    r2_c = compile_pattern(
        r2_pat,
        str(r2.get("flags") or ""),
        str(r2.get("dialect") or r1.get("dialect") or "py_re"),
        "fullmatch",
        max_length=max(_PATTERN_CHAR_CAP, len(r2_pat)),
    )
    if not r1_c.encodable or not r2_c.encodable:
        rec["result"] = "skipped_unencodable"
        rec["detail"] = {
            "r1": r1_c.unencodable_reason,
            "r2": r2_c.unencodable_reason,
        }
        return rec
    constraints, bad, s = shape5_constraints(
        r1_c.mirror, r2_c.mirror, min_len=1, max_len=max_len
    )
    # Enumerate distinct models: Z3 seq witnesses vary across runs and
    # Python re pad-gate can flip sat ↔ sat_fullmatch_only across 3.12/3.13
    # (Golden conversion-ledger / two-run drift). Prefer any pad-confirmed
    # search gap. Five models was not enough to stabilize CRS 941140/942220
    # on Python 3.13.
    # Issue #524 (luna r1): the per-check timeout is NOT the whole-pair budget —
    # the loop can issue up to _PAD_GATE_MODEL_CAP checks, each with a fresh
    # timeout_ms. A hard wall-clock deadline keeps the worst case (64 × 120s ≈
    # 128 min/pair) bounded under the Golden CI job's 60-minute limit. The Z3
    # solve itself is deterministic given random_seed=0 — a fresh process
    # returns the same first witness (verified across 6 processes) — so once a
    # solve completes within the deadline the classification is reproducible;
    # the only load-dependence was a first-check timeout, which the deadline +
    # transient retry below eliminate.
    deadline = time.monotonic() + _BATCH_SOLVE_DEADLINE_MS / 1000.0

    def _fresh_solver(per_check_ms: int) -> Solver:
        """Build the solve with an explicit per-check timeout and random_seed=0.

        random_seed=0 makes the solve deterministic across processes (verified:
        a fresh process returns the same first witness), which is what the
        two-run reproducibility gate needs. The per-check timeout is parameterised
        so the caller can clamp it to the remaining wall-clock deadline.
        """
        s = Solver()
        s.set("timeout", per_check_ms)
        s.set("random_seed", 0)
        for constraint in constraints:
            s.add(constraint)
        s.add(bad)
        return s

    solver = _fresh_solver(timeout_ms)
    seen: set[str] = set()
    best: dict[str, Any] | None = None
    transient_retried = False
    for _ in range(_PAD_GATE_MODEL_CAP):
        # luna r3 (issue #524): clamp the per-check timeout to the remaining
        # wall-clock budget so a check cannot run a full timeout_ms past the
        # deadline — the deadline is a hard ceiling, not a coarse guard.
        remaining_ms = int((deadline - time.monotonic()) * 1000.0)
        if remaining_ms <= 0:
            # Hard whole-pair budget exhausted (luna r1, issue #524). Fail
            # closed: an artificial wall-clock cutoff must not be converted into
            # a confident `sat`/`sat_fullmatch_only` — a pad-confirmed gap or a
            # proven fullmatch-only verdict requires the solver to have reached
            # its own terminal condition. Deadline exhaustion is TIMEOUT /
            # not-proven, which the timeout_gate then hard-fails (AGENTS.md).
            rec["result"] = "timeout"
            rec["not_proven"] = True
            return rec
        per_check_ms = min(timeout_ms, remaining_ms)
        # luna r4 (issue #524): never floor to 0ms — Z3 treats timeout=0 as
        # unbounded, which would silently defeat the deadline. Clamp to >=1.
        per_check_ms = max(1, per_check_ms)
        # True when the deadline shrank this check's budget below the nominal
        # per-check timeout. An `unknown` under that clamp is deadline-induced,
        # not a solver terminal verdict — it must fail closed, not be mistaken
        # for a completed search (luna r4).
        deadline_clamped = per_check_ms < timeout_ms
        solver.set("timeout", per_check_ms)
        verdict = solver.check()
        if verdict == unknown:
            if best is None:
                # A first-check timeout is almost always a transient scheduling
                # spike (the solve completes in ~9-26s on a quiet machine) that
                # Z3's internal re-check would resolve. Retry once with a fresh
                # solver to turn a load-dependent `timeout` into the
                # deterministic classification (problem #524). Exact Z3 state
                # (timeout, seed, constraints) is reproduced, so the retried
                # solve is the same deterministic one.
                if not transient_retried and time.monotonic() < deadline:
                    transient_retried = True
                    solver = _fresh_solver(timeout_ms)
                    seen = set()
                    best = None
                    continue
                rec["result"] = "timeout"
                rec["not_proven"] = True
                return rec
            if deadline_clamped:
                # The check was cut short by the remaining wall-clock budget;
                # its `unknown` is a deadline-induced timeout, not a genuine
                # solver terminal verdict. Fail closed (luna r4) — we must not
                # claim a confident sat/sat_fullmatch_only from an incomplete
                # search that the carrier deadline forced to stop early.
                rec["result"] = "timeout"
                rec["not_proven"] = True
                return rec
            # Z3 returned unknown AFTER at least one fullmatch witness was
            # confirmed on a completed check (best is set) AND this check had
            # the full per-check budget (no deadline clamp). The fullmatch gap
            # is proven; the solver's own terminal unknown only failed to
            # upgrade it to a search gap. Keep the proven fullmatch-only result
            # (not a timeout) — this is the deliberate sat_fullmatch_only
            # boundary that the committed golden artifacts depend on.
            break
        if verdict == unsat:
            break
        if verdict != sat:
            if best is None:
                rec["result"] = "skipped_unknown"
                return rec
            break
        witness = z3_str(solver.model().eval(s, model_completion=True))
        if witness in seen:
            break
        seen.add(witness)
        gated = gate_sat_witness(pair, witness)
        cand = {
            "witness": {"s": witness},
            "search_pad_gate": gated,
            "result": "sat" if gated else "sat_fullmatch_only",
            "ground_truth_status": (
                "reproduced" if gated else "fullmatch-only-not-search-gap"
            ),
        }
        if best is None or (gated and not best.get("search_pad_gate")):
            best = cand
        if gated:
            break
        solver.add(s != StringVal(witness))
    if best is None:
        rec["result"] = "unsat"
        return rec
    rec.update(best)
    return rec
