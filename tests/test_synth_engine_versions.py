from __future__ import annotations

import pytest

from regexproof.batch.synth_emit import _guard_row, _property_row


def _row(engine_versions=None):
    return {
        "regex_id": "a" * 32,
        "pattern": "a+",
        "dialect": "java",
        "call_kind": "fullmatch",
        "domain": "ascii",
        "engine_versions": engine_versions or {"java": "Eclipse Adoptium 17.0.20+8"},
    }


def test_synthesized_property_preserves_compile_and_replay_versions():
    emitted = _property_row(
        corpus="fixture",
        row=_row(),
        question={"id": "q1"},
        bad_char="x",
        shape=1,
        result="sat",
        witness="x",
        domain_note="all-lengths",
        ground_truth_status="reproduced",
        replay_engine_versions={"java": "Eclipse Adoptium 17.0.20+8"},
    )
    assert emitted["engine_versions"]["java"] == "Eclipse Adoptium 17.0.20+8"
    assert "python" in emitted["engine_versions"]
    assert "z3" in emitted["engine_versions"]


def test_synthesized_guard_preserves_compile_versions():
    emitted = _guard_row(
        corpus="fixture",
        row=_row(),
        question_id="q1",
        bad_char="x",
        shape=1,
        witness="x",
    )
    assert emitted["engine_versions"]["java"] == "Eclipse Adoptium 17.0.20+8"


def test_synthesized_property_rejects_compile_replay_version_conflict():
    with pytest.raises(ValueError, match="conflicting java engine versions"):
        _property_row(
            corpus="fixture",
            row=_row(),
            question={"id": "q1"},
            bad_char="x",
            shape=1,
            result="sat",
            witness="x",
            domain_note="all-lengths",
            ground_truth_status="reproduced",
            replay_engine_versions={"java": "Eclipse Adoptium 21.0.2"},
        )
