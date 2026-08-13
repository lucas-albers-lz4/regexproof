"""Batch evidence gates for Z3 findings and synthesized mutation guards."""

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
GUARD_COVERAGE_FLOOR = 1.0


def check_guard_coverage(
    findings: list[dict[str, Any]],
    *,
    floor: float = GUARD_COVERAGE_FLOOR,
) -> list[str]:
    """Return violations for the synthesized mutation-guard coverage floor.

    Only rows explicitly marked ``synthesized`` participate.  In particular,
    inventory ``planned`` stubs and ordinary scanner findings must not affect
    either side of the coverage calculation.  A run with no real synthesized
    property rows has no coverage claim and therefore passes this gate.
    """
    if not 0.0 <= floor <= 1.0:
        raise ValueError("guard coverage floor must be between 0 and 1")

    properties = {
        (str(f.get("family")), str(f.get("bad_char")))
        for f in findings
        if (
            f.get("kind") == "property"
            and f.get("synthesized") is True
            and f.get("result") != "planned"
        )
    }
    guards = {
        (str(f.get("family")), str(f.get("bad_char")))
        for f in findings
        if (
            f.get("kind") == "mutation_guard"
            and f.get("synthesized") is True
            and f.get("result") != "planned"
        )
    }
    errors: list[str] = []
    for finding in findings:
        if finding.get("kind") != "mutation_guard" or finding.get("synthesized") is not True:
            continue
        family = finding.get("family")
        bad_char = finding.get("bad_char")
        if finding.get("result") != "sat":
            errors.append(
                f"mutation guard {family}/{bad_char!r} result="
                f"{finding.get('result')!r}, expected 'sat'"
            )
        if finding.get("expected_result") != "sat":
            errors.append(
                f"mutation guard {family}/{bad_char!r} "
                "missing expected_result='sat'"
            )
        if finding.get("ground_truth_status") != "mutation-guard-sat-expected":
            errors.append(
                f"mutation guard {family}/{bad_char!r} "
                "has invalid ground_truth_status"
            )
    if not properties:
        return errors

    covered = properties & guards
    coverage = len(covered) / len(properties)
    if coverage < floor:
        errors.append(
            "mutation guard coverage "
            f"{len(covered)}/{len(properties)}={coverage:.3f} is below "
            f"floor={floor:.3f}"
        )
        errors.extend(
            f"missing mutation guard for family={family} bad_char={bad_char!r}"
            for family, bad_char in sorted(properties - guards)
        )
    return errors


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
        # P3 fold (luna gate 1 minor): expected_result must be enforced in the
        # evidence gate itself, not only by the synthesized-path coverage check.
        if kind == "mutation_guard" and f.get("expected_result") != "sat":
            errors.append(f"{rid}: mutation_guard expected_result must be 'sat'")
            continue
        # Mutation guards have their own exact status contract; they are not
        # witness claims and therefore do not require property replay status.
        if kind == "mutation_guard":
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
        required_gt = {"reproduced"} if f.get("synthesized") is True else GT_OK
        if gt not in required_gt:
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
    errs = check_guard_coverage(findings)
    errs.extend(evidence_gate_errors(
        findings,
        require_ground_truth=require_ground_truth,
        fail_planned=fail_planned,
    ))
    if errs:
        raise SystemExit("evidence gate failed:\n  - " + "\n  - ".join(errs))
