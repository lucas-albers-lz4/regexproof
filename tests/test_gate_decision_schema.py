"""Corpus admission gate: gate_decision.schema.json validity + sweep examples."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SCHEMA = ROOT / "regexproof" / "schemas" / "gate_decision.schema.json"
SWEEP_EXAMPLES = sorted((ROOT / "sweep").glob("example-gate-decision-*.json"))


def _load_schema() -> dict:
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def test_schema_is_valid_json_and_declares_required_fields():
    schema = _load_schema()
    required = schema["required"]
    assert "schema_version" in required
    for field in ("corpus", "decision", "probe", "conditions", "rationale"):
        assert field in required, f"{field} must be required"
    assert schema["properties"]["decision"]["enum"] == [
        "go",
        "no-go",
        "triage-trial",
    ]


def test_schema_requires_exactly_three_conditions():
    schema = _load_schema()
    items = schema["properties"]["conditions"]["items"]
    assert schema["properties"]["conditions"]["minItems"] == 3
    assert items["required"] == ["id", "met", "evidence"]
    assert items["properties"]["id"]["enum"] == [
        "new-surface",
        "security-boundary",
        "large-under-saturated",
    ]


def test_sweep_examples_have_required_shape():
    schema = _load_schema()
    try:
        import jsonschema

        validator = jsonschema
    except ImportError:  # pragma: no cover - environment-dependent
        validator = None
    assert SWEEP_EXAMPLES, "no example-gate-decision-*.json under sweep/"
    for path in SWEEP_EXAMPLES:
        ex = json.loads(path.read_text(encoding="utf-8"))
        if validator is not None:
            validator.validate(instance=ex, schema=schema)
        else:  # minimal fallback so the test still guards shape without jsonschema
            assert ex["decision"] in ("go", "no-go", "triage-trial")
            assert len(ex["conditions"]) == 3
            assert all(
                c["id"] in ("new-surface", "security-boundary", "large-under-saturated")
                for c in ex["conditions"]
            )
        assert ex["probe"]["regex_sites"] >= 0
        assert ex["rationale"]
