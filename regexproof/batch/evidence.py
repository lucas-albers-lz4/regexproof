"""Batch evidence gates: TIMEOUT hard-fail + optional --require-ground-truth."""

from __future__ import annotations

from typing import Any

TIMEOUT_RESULTS = frozenset({"timeout", "unknown"})
SATISH_RESULTS = frozenset({"sat", "finding", "vulnerable"})
GT_OK = frozenset({"reproduced", "mutation-guard-sat-expected"})
# Classification / ReDoS kinds are not Z3 verdicts — absence of ground_truth_status
# is honest (see docs/REPORTING.md). Z3-side kinds need GT under the flag.
Z3_VERDICT_KINDS = frozenset(
    {"property", "rule_diff", "counterexample_finder", "bug_demo", "mutation_guard"}
)


def evidence_gate_errors(
    findings: list[dict[str, Any]],
    *,
    require_ground_truth: bool = False,
    fail_planned: bool = False,
) -> list[str]:
    """Return human-readable gate violations (empty = pass).

    - TIMEOUT/unknown on Z3-verdict kinds is always a hard failure (not proven).
    - With require_ground_truth: SAT-ish Z3 verdicts need a successful GT status.
    - With fail_planned: inventory ``result=planned`` stubs fail (P4 unexecuted IDs).
    """
    errors: list[str] = []
    unexecuted: list[str] = []
    for f in findings:
        rid = f.get("regex_id") or "?"
        kind = f.get("kind") or ""
        result = str(f.get("result") or "").lower()
        if kind in Z3_VERDICT_KINDS and result in TIMEOUT_RESULTS:
            errors.append(f"{rid}: result={result} (TIMEOUT/unknown = not proven)")
            continue
        if kind == "mutation_guard" and result != "sat":
            errors.append(f"{rid}: mutation_guard result={result!r}, expected 'sat'")
            continue
        if (
            kind == "mutation_guard"
            and f.get("ground_truth_status") != "mutation-guard-sat-expected"
        ):
            errors.append(
                f"{rid}: mutation_guard ground_truth_status must be "
                "'mutation-guard-sat-expected'"
            )
            continue
        if fail_planned and result == "planned":
            qid = (f.get("detail") or {}).get("question_id") or rid
            unexecuted.append(str(qid))
            continue
        if not require_ground_truth:
            continue
        if kind not in Z3_VERDICT_KINDS:
            continue
        if result not in SATISH_RESULTS:
            continue
        gt = f.get("ground_truth_status")
        if gt not in GT_OK:
            errors.append(
                f"{rid}: SAT-ish result={result!r} kind={kind!r} but "
                f"ground_truth_status={gt!r} (need reproduced under --require-ground-truth)"
            )
    if unexecuted:
        errors.append(
            "unexecuted question IDs (planned stubs): " + ", ".join(sorted(set(unexecuted)))
        )
    return errors


def enforce_evidence_gates(
    findings: list[dict[str, Any]],
    *,
    require_ground_truth: bool = False,
    fail_planned: bool = False,
) -> None:
    """Raise SystemExit with a non-zero message if any evidence gate fails."""
    errs = evidence_gate_errors(
        findings,
        require_ground_truth=require_ground_truth,
        fail_planned=fail_planned,
    )
    if errs:
        raise SystemExit("evidence gate failed:\n  - " + "\n  - ".join(errs))
