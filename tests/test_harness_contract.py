"""Harness product-reportability (#476)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import FormatChecker, ValidationError, validate

from regexproof.harness.contract import contract_is_adopted, product_reportable
from regexproof.harness.core import REGISTRY
from regexproof.schemas import load_schema
import regexproof.harness.properties  # noqa: F401

ROOT = Path(__file__).resolve().parents[1]


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
        "site": "src/validator.py:12",
        "guarantee": "no semicolon",
        "input_source": "untrusted username",
        "trust": "untrusted-input",
        "declared_domain": "ascii",
        "provenance": "human",
    }
    assert product_reportable(entry) is True
    entry["contract"]["provenance"] = "agent_derived"
    assert product_reportable(entry) is False


def test_agent_contract_requires_a_valid_adoption_record():
    entry = {
        "kind": "property",
        "domain": "ascii",
        "contract": {
            "schema_version": "1",
            "site": "src/validator.py:12",
            "guarantee": "no semicolon",
            "input_source": "untrusted username",
            "trust": "untrusted-input",
            "declared_domain": "ascii",
            "provenance": "agent_derived",
        },
    }
    assert not contract_is_adopted(entry["contract"])
    assert not product_reportable(entry)

    entry["contract"]["adoption"] = {
        "status": "approved",
        "authority": "standing_user_delegation",
        "approved_on": "2026-10-09",
        "rationale": "The guarantee matches the source boundary and its declared domain.",
        "evidence": ["src/validator.py:12", "tests/test_validator.py::test_separator_blocked"],
    }
    assert contract_is_adopted(entry["contract"])
    assert product_reportable(entry)

    entry["contract"]["adoption"]["approved_on"] = "not-a-date"
    assert not contract_is_adopted(entry["contract"])
    assert not product_reportable(entry)
    with pytest.raises(ValidationError):
        validate(
            entry["contract"],
            load_schema("property_contract.schema.json"),
            format_checker=FormatChecker(),
        )


def test_product_contract_requires_complete_schema_and_matching_site():
    contract = {
        "schema_version": "1",
        "site": "src/validator.py:12",
        "guarantee": "no semicolon",
        "input_source": "untrusted username",
        "trust": "untrusted-input",
        "declared_domain": "ascii",
        "provenance": "human",
    }
    entry = {
        "kind": "property",
        "domain": "ascii",
        "site": "src/validator.py:12",
        "contract": contract,
    }
    assert product_reportable(entry)

    entry["site"] = "src/other.py:4"
    assert not product_reportable(entry)
    entry["site"] = None
    assert not product_reportable(entry)
    entry["site"] = contract["site"]

    for field in ("schema_version", "site", "input_source", "trust"):
        malformed = {**contract}
        malformed.pop(field)
        entry["contract"] = malformed
        assert not product_reportable(entry), field
        assert not contract_is_adopted(malformed), field

    malformed = {**contract}
    malformed.pop("declared_domain")
    entry["contract"] = malformed
    assert not product_reportable(entry)
    # A top-level solver domain cannot fill in a missing contract declaration.
    assert entry["domain"] == "ascii"


def test_modsecurity_contract_records_the_user_approval():
    candidate = json.loads(
        (ROOT / "properties/generated/wordpress_modsecurity_ruleset_contract_candidate.json")
        .read_text(encoding="utf-8")
    )
    validate(
        candidate,
        load_schema("property_contract.schema.json"),
        format_checker=FormatChecker(),
    )
    assert candidate["provenance"] == "agent_derived"
    assert candidate["adoption"]["authority"] == "direct_user_approval"


def test_certgraveyard_contract_records_delegated_adoption():
    candidate = json.loads(
        (
            ROOT
            / "properties/generated/certgraveyard-yara-generator_contract_candidate.json"
        ).read_text(encoding="utf-8")
    )
    validate(
        candidate,
        load_schema("property_contract.schema.json"),
        format_checker=FormatChecker(),
    )
    assert candidate["provenance"] == "agent_derived"
    assert candidate["adoption"]["authority"] == "standing_user_delegation"
    assert "no length claim" in candidate["declared_domain"]


def test_adoption_record_requires_agent_authorship():
    contract = {
        "schema_version": "1",
        "site": "src/validator.py:1:0",
        "guarantee": "safe alphabet",
        "input_source": "external field",
        "trust": "untrusted-input",
        "declared_domain": "arbitrary string",
        "provenance": "human",
        "adoption": {
            "status": "approved",
            "authority": "standing_user_delegation",
            "approved_on": "2026-10-09",
            "rationale": "The source supports this claim.",
            "evidence": ["src/validator.py@0123456789abcdef0123456789abcdef01234567"],
        },
    }
    with pytest.raises(ValidationError):
        validate(
            contract,
            load_schema("property_contract.schema.json"),
            format_checker=FormatChecker(),
        )
