"""Property contract schema (#474 / #496)."""

from __future__ import annotations

import jsonschema

from regexproof.schemas import property_contract_schema


def test_property_contract_requires_provenance():
    schema = property_contract_schema()
    rec = {
        "schema_version": "1",
        "site": "a.py:1:0",
        "guarantee": "no semicolon reaches the shell",
        "input_source": "argv",
        "trust": "untrusted-input",
        "declared_domain": "ascii",
        "provenance": "human",
    }
    jsonschema.validate(rec, schema)
    bad = dict(rec)
    bad["provenance"] = "sibling_family"
    try:
        jsonschema.validate(bad, schema)
    except jsonschema.ValidationError:
        return
    raise AssertionError("sibling_family must not be a provenance")
