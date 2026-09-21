"""Forge CLI conversion-wave registration and sensitivity checks."""

from __future__ import annotations

from regexproof.harness import REGISTRY, check_mutation_coverage, run_one


FAMILY = "FC-forge-cli"


def test_forge_cli_contracts_are_registered_and_human_adopted():
    entries = [entry for entry in REGISTRY.values() if entry["family"] == FAMILY]
    assert len(entries) == 6
    properties = [entry for entry in entries if entry["kind"] == "property"]
    assert len(properties) == 5
    assert all(entry["contract"]["provenance"] == "human" for entry in properties)
    assert all(entry["input_domain"] == "ascii" for entry in entries)


def test_forge_cli_properties_hold_and_mutation_guard_flips():
    for name in sorted(REGISTRY):
        if REGISTRY[name]["family"] != FAMILY:
            continue
        result = run_one(name, REGISTRY[name])
        assert result["result"] == ("sat" if REGISTRY[name]["kind"] == "mutation_guard" else "unsat")
        assert result["not_proven"] is False


def test_forge_cli_family_has_mutation_coverage():
    assert check_mutation_coverage() == 0
