"""kind / call_kind validation and mutation-coverage for rule_diff."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

from regexproof.kinds import (
    KINDS_NEEDING_MUTATION_GUARD,
    validate_call_kind,
    validate_kind,
)


def test_validate_kind_accepts_rule_diff():
    assert validate_kind("rule_diff") == "rule_diff"


def test_validate_kind_rejects_unknown():
    with pytest.raises(ValueError):
        validate_kind("not-a-kind")


@pytest.mark.parametrize("ck", ["fullmatch", "match", "search", "exec", "substitution"])
def test_validate_call_kind_ok(ck):
    assert validate_call_kind(ck) == ck


def test_validate_call_kind_none():
    assert validate_call_kind(None) is None


def test_validate_call_kind_rejects():
    with pytest.raises(ValueError):
        validate_call_kind("stateful")


def test_rule_diff_in_needing_set():
    assert "rule_diff" in KINDS_NEEDING_MUTATION_GUARD


def _load_harness():
    path = Path(__file__).resolve().parents[1] / "scripts" / "z3-verify.py"
    spec = importlib.util.spec_from_file_location("z3_verify", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_mutation_coverage_requires_guard_for_rule_diff():
    mod = _load_harness()
    # Snapshot and inject a synthetic rule_diff family without a guard.
    saved = dict(mod.REGISTRY)
    try:
        mod.REGISTRY.clear()
        mod.REGISTRY["RD-base"] = {
            "fn": lambda: ([], None),
            "domain": "test",
            "expect_unsat": True,
            "timeout_ms": 1000,
            "ground_truth": None,
            "kind": "rule_diff",
            "family": "RD",
            "input_domain": "ascii",
            "call_kind": "search",
        }
        assert mod.check_mutation_coverage() == 1

        mod.REGISTRY["RD-widen"] = {
            **mod.REGISTRY["RD-base"],
            "kind": "mutation_guard",
            "expect_unsat": False,
        }
        assert mod.check_mutation_coverage() == 0
    finally:
        mod.REGISTRY.clear()
        mod.REGISTRY.update(saved)


def test_prop_rejects_invalid_kind_at_registration():
    mod = _load_harness()
    with pytest.raises(ValueError):
        mod.prop("X-bad", "d", kind="not-real")(lambda: ([], None))


def test_prop_rejects_invalid_call_kind_at_registration():
    mod = _load_harness()
    with pytest.raises(ValueError):
        mod.prop("X-bad2", "d", call_kind="nope")(lambda: ([], None))
