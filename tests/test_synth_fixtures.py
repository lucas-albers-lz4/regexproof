"""P3 synthesizer regression fixtures and fail-closed mutation gates."""

from __future__ import annotations

import pytest
from z3 import Re, Star

import regexproof.batch.synthesize as synth
from regexproof.batch.evidence import evidence_gate_errors
from regexproof.batch.synthesize import SynthesisError, synthesize_compiled
from regexproof.compiler import compile_pattern


def _row(pattern: str, regex_id: str = "a" * 32) -> dict:
    return {
        "regex_id": regex_id,
        "pattern": pattern,
        "flags": "",
        "dialect": "ecma",
        "call_kind": "search",
        "site": "fixture.js:1:0",
        "file": "fixture.js",
        "domain": "ascii",
        "encodable": True,
    }


def _question(bad_char: str = ";") -> dict:
    return {
        "id": "fixture-shape1",
        "shape": 1,
        "bad_chars": [bad_char],
        "threat": "fixture",
        "encoding_hint": "single-char InRe",
    }


def test_weakened_mirror_guard_stays_unsat_and_fails_gate(monkeypatch):
    """A guard result other than SAT is a production failure, not a report."""
    row = _row("^a+$")
    compiled = compile_pattern(row["pattern"], "", "ecma", "search")

    def weakened_guard(*args, **kwargs):
        return "unsat", None

    monkeypatch.setattr(synth, "_widened_guard", weakened_guard)
    with pytest.raises(SynthesisError, match="expected sat"):
        synthesize_compiled(
            "fixture",
            [(row, compiled.mirror, compiled.meta)],
            {"questions": [_question()]},
            {"synth_max_sites": 1, "synth_diff_fuzz_sample": 0},
        )

    errors = evidence_gate_errors(
        [
            {
                "regex_id": row["regex_id"],
                "kind": "mutation_guard",
                "result": "unsat",
                "ground_truth_status": "mutation-guard-sat-expected",
            }
        ]
    )
    assert any("expected 'sat'" in error for error in errors)


def test_certified_but_empty_class_fails_nonvacuity():
    row = _row("^a+$", "b" * 32)
    compiled = compile_pattern(row["pattern"], "", "ecma", "search")
    with pytest.raises(SynthesisError, match="vacuous"):
        synthesize_compiled(
            "fixture",
            [(row, Star(Re("")), compiled.meta)],
            {"questions": [_question()]},
            {"synth_max_sites": 1, "synth_diff_fuzz_sample": 0},
        )


def test_bad_char_accepting_validator_replays_sat_witness():
    row = _row("^[a;]+$", "c" * 32)
    compiled = compile_pattern(row["pattern"], "", "ecma", "search")
    result = synthesize_compiled(
        "fixture",
        [(row, compiled.mirror, compiled.meta)],
        {"questions": [_question()]},
        {"synth_max_sites": 1, "synth_diff_fuzz_sample": 0},
    )
    properties = [finding for finding in result.findings if finding["kind"] == "property"]
    assert len(properties) == 1
    assert properties[0]["result"] == "sat"
    assert properties[0]["witness"] == ";"
    assert properties[0]["ground_truth_status"] == "reproduced"
