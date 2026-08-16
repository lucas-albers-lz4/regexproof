"""Harness product-reportability (#476)."""

from __future__ import annotations

from regexproof.harness.contract import product_reportable
from regexproof.harness.core import REGISTRY
import regexproof.harness.properties  # noqa: F401


def test_registry_properties_are_product_reportable():
    p1 = REGISTRY["P1-space"]
    assert product_reportable(p1)
    guards = [e for e in REGISTRY.values() if e["kind"] == "mutation_guard"]
    assert guards
    assert all(not product_reportable(e) for e in guards)


def test_unsat_without_contract_is_not_product():
    entry = {
        "kind": "property",
        "domain": "ascii",
        "contract": None,
    }
    assert product_reportable(entry) is False
    entry["contract"] = {
        "guarantee": "no semicolon",
        "declared_domain": "ascii",
        "provenance": "human",
    }
    assert product_reportable(entry) is True
