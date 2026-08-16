"""Admit and run shape-5 pairs in batch (#477).

Admission is only ``version_diff`` / ``cross_engine`` with a ``family_contract``.
Independent-spec gitleaks pairs stay out. Fullmatch SAT is then gated by the
search/pad matrix; a fullmatch-only SAT is recorded, not a search gap.
"""

from __future__ import annotations

from typing import Any

from z3 import Solver, sat, unsat, unknown

from regexproof.compiler import compile_pattern
from regexproof.harness.core import z3_str
from regexproof.rule_diff.encode import shape5_constraints
from regexproof.rule_diff.search_replay import gate_sat_witness

SCALE_PROVENANCE = frozenset({"version_diff", "cross_engine"})


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
    timeout_ms: int = 30000,
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
    r1_c = compile_pattern(
        str(r1.get("pattern") or ""),
        str(r1.get("flags") or ""),
        str(r1.get("dialect") or "py_re"),
        "fullmatch",
        max_length=max_len,
    )
    r2_c = compile_pattern(
        str(r2.get("pattern") or ""),
        str(r2.get("flags") or ""),
        str(r2.get("dialect") or r1.get("dialect") or "py_re"),
        "fullmatch",
        max_length=max_len,
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
    solver = Solver()
    solver.set("timeout", timeout_ms)
    for constraint in constraints:
        solver.add(constraint)
    solver.add(bad)
    verdict = solver.check()
    if verdict == unknown:
        rec["result"] = "timeout"
        rec["not_proven"] = True
        return rec
    if verdict == unsat:
        rec["result"] = "unsat"
        return rec
    if verdict != sat:
        rec["result"] = "skipped_unknown"
        return rec
    witness = z3_str(solver.model().eval(s, model_completion=True))
    rec["witness"] = {"s": witness}
    gated = gate_sat_witness(pair, witness)
    rec["search_pad_gate"] = gated
    rec["result"] = "sat" if gated else "sat_fullmatch_only"
    return rec
