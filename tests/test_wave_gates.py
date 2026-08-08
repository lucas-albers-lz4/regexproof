"""Batch evidence gates + {1} compiler crash regression."""

from __future__ import annotations

import pytest

from regexproof.batch.evidence import evidence_gate_errors, enforce_evidence_gates
from regexproof.compiler import compile_pattern


def test_exact_single_quantifier_no_longer_crashes():
    cr = compile_pattern("x{1}", "", "ecma", "fullmatch")
    assert cr.encodable, cr.unencodable_reason
    cr2 = compile_pattern("ab{1,1}c", "", "pcre", "fullmatch")
    assert cr2.encodable, cr2.unencodable_reason


def test_timeout_on_z3_kind_is_error():
    errs = evidence_gate_errors(
        [{"regex_id": "a" * 32, "kind": "rule_diff", "result": "timeout"}]
    )
    assert errs and "timeout" in errs[0]


def test_redos_timeout_not_z3_gate():
    errs = evidence_gate_errors(
        [{"regex_id": "a" * 32, "kind": "redos", "result": "timeout"}]
    )
    assert errs == []


def test_require_ground_truth_sat():
    errs = evidence_gate_errors(
        [
            {
                "regex_id": "b" * 32,
                "kind": "rule_diff",
                "result": "sat",
                "ground_truth_status": None,
            }
        ],
        require_ground_truth=True,
    )
    assert errs
    errs_ok = evidence_gate_errors(
        [
            {
                "regex_id": "b" * 32,
                "kind": "rule_diff",
                "result": "sat",
                "ground_truth_status": "reproduced",
            }
        ],
        require_ground_truth=True,
    )
    assert errs_ok == []


def test_fail_planned_lists_question_ids():
    errs = evidence_gate_errors(
        [
            {
                "regex_id": "inventory:v-shape1",
                "kind": "property",
                "result": "planned",
                "detail": {"question_id": "v-shape1-injection-chars"},
            }
        ],
        fail_planned=True,
    )
    assert any("v-shape1-injection-chars" in e for e in errs)


def test_enforce_raises():
    with pytest.raises(SystemExit):
        enforce_evidence_gates(
            [{"regex_id": "c" * 32, "kind": "property", "result": "unknown"}]
        )
