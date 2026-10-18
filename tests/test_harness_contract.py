"""Harness product-reportability (#476)."""

from __future__ import annotations

from regexproof.harness.contract import product_reportable
from regexproof.harness.core import REGISTRY
from regexproof.contract_adoption import contract_digest
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
        "schema_version": "1",
        "site": "src/file.py:1:0",
        "guarantee": "no semicolon",
        "input_source": "request parameter",
        "trust": "untrusted-input",
        "declared_domain": "ascii",
        "provenance": "human",
    }
    assert product_reportable(entry) is True
    entry["contract"]["provenance"] = "agent_derived"
    assert product_reportable(entry) is False
    contract = entry["contract"]
    pin = "a" * 40
    url = "https://github.com/example/project"
    contract["adoption"] = {
        "policy_version": "autonomous-contracts-v1",
        "status": "approved",
        "authority": "standing_user_delegation",
        "approved_on": "2026-10-13",
        "rationale": "The pinned implementation and caller establish this input boundary.",
        "evidence": [f"{url}/blob/{pin}/src/file.py"],
        "source_url": url,
        "source_pin": pin,
        "source_file": "src/file.py",
        "source_sha256": "b" * 64,
        "contract_sha256": "0" * 64,
        "review": {"author": "agent-a", "reviewer": "agent-b", "same_model": True},
    }
    contract["adoption"]["contract_sha256"] = contract_digest(contract)
    assert product_reportable(entry) is True
    contract["guarantee"] = "different guarantee"
    assert product_reportable(entry) is False
