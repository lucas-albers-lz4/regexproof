"""P4 batch evidence and synthesized mutation-guard gates."""

from __future__ import annotations

import jsonschema
import pytest

from regexproof.batch.evidence import (
    check_guard_coverage,
    enforce_evidence_gates,
    evidence_gate_errors,
)
from regexproof.schemas import scanner_finding_schema


def _property(*, result: str = "sat", **extra: object) -> dict[str, object]:
    return {
        "regex_id": "a" * 32,
        "kind": "property",
        "family": "synth:fixture:a",
        "bad_char": ";",
        "result": result,
        "synthesized": True,
        **extra,
    }


def _guard(*, result: str = "sat", **extra: object) -> dict[str, object]:
    return {
        "regex_id": "a" * 32,
        "kind": "mutation_guard",
        "family": "synth:fixture:a",
        "bad_char": ";",
        "result": result,
        "expected_result": "sat",
        "ground_truth_status": "mutation-guard-sat-expected",
        "synthesized": True,
        **extra,
    }


def test_unsat_mutation_guard_is_a_batch_gate_failure():
    findings = [_property(), _guard(result="unsat")]

    assert any("expected 'sat'" in error for error in check_guard_coverage(findings))
    with pytest.raises(SystemExit, match="evidence gate failed"):
        enforce_evidence_gates(findings)


def test_synthesized_sat_property_requires_reproduced_ground_truth():
    findings = [_property(), _guard()]

    errors = evidence_gate_errors(findings, require_ground_truth=True)

    assert any("ground_truth_status=None" in error for error in errors)
    assert evidence_gate_errors(
        [_property(ground_truth_status="reproduced"), _guard()],
        require_ground_truth=True,
    ) == []


def test_planned_and_non_synthesized_rows_do_not_count_toward_coverage():
    planned = {
        "regex_id": "inventory:v-shape1",
        "kind": "property",
        "result": "planned",
        "family": "inventory:v-shape1",
        "bad_char": ";",
    }
    ordinary = _property(synthesized=False)

    assert check_guard_coverage([planned, ordinary]) == []


def test_schema_kinds_are_additive_and_version_stays_one():
    schema = scanner_finding_schema()

    assert schema["properties"]["schema_version"]["const"] == "1"
    assert {
        "counterexample_finder",
        "bug_demo",
        "mutation_guard",
    } <= set(schema["properties"]["kind"]["enum"])
    jsonschema.validate(
        {
            "schema_version": "1",
            "regex_id": "a" * 32,
            "kind": "mutation_guard",
            "corpus": "fixture",
            "result": "sat",
            "site": "fixture.js:1:0",
        },
        schema,
    )


def test_missing_guard_fails_the_coverage_floor():
    """P4 (luna gate 1): a real synthesized property without its matching
    guard must fail the 100% coverage floor — the primary red path of the
    gate."""
    errors = check_guard_coverage([_property()])
    assert any("missing mutation guard" in e for e in errors), errors
    try:
        enforce_evidence_gates([_property()])
    except SystemExit as exc:
        assert "missing mutation guard" in str(exc)
    else:
        raise AssertionError("enforce_evidence_gates did not fail without a guard")


def test_synthesized_planned_row_is_excluded_by_status():
    """P4 (luna gate 1): a row marked synthesized=True but result=planned is
    excluded by the result!=planned branch — the explicit status exclusion,
    not only the synthesized-marker exclusion."""
    # Only a planned row: no coverage claim -> no errors.
    planned = _property(result="planned", synthesized=True)
    assert check_guard_coverage([planned]) == []
    # A real property + a planned guard for the same key: the planned guard
    # must NOT count, so the floor still fails.
    errors = check_guard_coverage([_property(), _guard(result="planned", synthesized=True)])
    assert any("missing mutation guard" in e for e in errors), errors
