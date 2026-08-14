"""Emit phase: synthesized property/guard rows and SynthesisResult."""

from __future__ import annotations

import platform
from dataclasses import dataclass
from typing import Any

import z3

SYNTHESIZER_VERSION = "1"


@dataclass
class SynthesisResult:
    findings: list[dict[str, Any]]
    stats: dict[str, Any]
    executed_questions: set[str]


def _engine_versions() -> dict[str, str]:
    return {"python": platform.python_version(), "z3": z3.get_version_string()}


def _property_row(
    *,
    corpus: str,
    row: dict[str, Any],
    question: dict[str, Any],
    bad_char: str,
    shape: int,
    result: str,
    witness: str | None,
    domain_note: str,
    ground_truth_status: str | None,
) -> dict[str, Any]:
    regex_id = str(row["regex_id"])
    family = f"synth:{corpus}:{regex_id}"
    return {
        "schema_version": "1",
        "regex_id": regex_id,
        "corpus": corpus,
        "kind": "property",
        "family": family,
        "question_id": str(question["id"]),
        "bad_char": bad_char,
        "shape": shape,
        "result": result,
        "domain_note": domain_note,
        "input_domain": str(row.get("domain") or "ascii"),
        "witness": witness,
        "ground_truth_status": ground_truth_status,
        "wall_ms": 0,
        "engine_versions": _engine_versions(),
        "site": row.get("site") or "",
        "pattern": row.get("pattern") or "",
        "dialect": row.get("dialect") or "",
        "call_kind": row.get("call_kind") or "",
        "disclosure": None,
        "synthesized": True,
        "synth": {
            "synthesizer_version": SYNTHESIZER_VERSION,
            "encoding": "shape1-charclass" if shape == 1 else "shape2-bounded-mirror",
        },
        "detail": {
            "question_id": str(question["id"]),
            "threat": question.get("threat"),
            "bad_char": bad_char,
            "domain_note": domain_note,
        },
    }


def _guard_row(
    *,
    corpus: str,
    row: dict[str, Any],
    question_id: str,
    bad_char: str,
    shape: int,
    witness: str | None,
) -> dict[str, Any]:
    regex_id = str(row["regex_id"])
    family = f"synth:{corpus}:{regex_id}"
    return {
        "schema_version": "1",
        "regex_id": regex_id,
        "corpus": corpus,
        "kind": "mutation_guard",
        "family": family,
        "question_id": question_id,
        "bad_char": bad_char,
        "shape": shape,
        "result": "sat",
        "expected_result": "sat",
        "input_domain": str(row.get("domain") or "ascii"),
        "witness": witness,
        "ground_truth_status": "mutation-guard-sat-expected",
        "wall_ms": 0,
        "engine_versions": _engine_versions(),
        "site": row.get("site") or "",
        "pattern": row.get("pattern") or "",
        "dialect": row.get("dialect") or "",
        "call_kind": row.get("call_kind") or "",
        "disclosure": None,
        "synthesized": True,
        "synth": {
            "synthesizer_version": SYNTHESIZER_VERSION,
            "encoding": "widened-mirror",
        },
        "detail": {
            "question_id": question_id,
            "bad_char": bad_char,
            "mutation": "union bad_char into mirror",
        },
    }
