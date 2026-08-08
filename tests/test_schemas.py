"""Fixture-compat tests for Phase-1 versioned schemas."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

from regexproof.regex_id import make_regex_id
from regexproof.schemas import (
    COMPILED_SCHEMA_VERSION,
    EXTRACTOR_SCHEMA_VERSION,
    compiled_pattern_schema,
    extractor_schema,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "schema"


@pytest.fixture(scope="module")
def extractor_sample(tmp_path_factory):
    rid = make_regex_id(
        repo="demo/repo",
        pattern=r"^[a-z]+$",
        flags="",
        dialect="py_re",
        call_kind="fullmatch",
        site="a.py:1:0",
    )
    return {
        "schema_version": EXTRACTOR_SCHEMA_VERSION,
        "regex_id": rid,
        "repo": "demo/repo",
        "pattern": r"^[a-z]+$",
        "flags": "",
        "dialect": "py_re",
        "call_kind": "fullmatch",
        "site": "a.py:1:0",
        "file": "a.py",
        "line": 1,
        "column": 0,
        "context_snippet": "def f(): pass",
    }


def test_extractor_schema_validates(extractor_sample):
    jsonschema.validate(extractor_sample, extractor_schema())


def test_compiled_schema_encodable():
    rid = make_regex_id(
        repo="demo/repo",
        pattern=r"a+",
        flags="",
        dialect="py_re",
        call_kind="search",
        site="b.py:2:0",
    )
    rec = {
        "schema_version": COMPILED_SCHEMA_VERSION,
        "regex_id": rid,
        "pattern": r"a+",
        "flags": "",
        "dialect": "py_re",
        "call_kind": "search",
        "declared_domain": {"alphabet": "ascii", "description": "test"},
        "mirror_expr": "Plus(Re('a'))",
    }
    jsonschema.validate(rec, compiled_pattern_schema())


def test_compiled_schema_unencodable():
    rid = make_regex_id(
        repo="demo/repo",
        pattern=r"(?<=x)y",
        flags="",
        dialect="py_re",
        call_kind="search",
        site="c.py:3:0",
    )
    rec = {
        "schema_version": COMPILED_SCHEMA_VERSION,
        "regex_id": rid,
        "pattern": r"(?<=x)y",
        "flags": "",
        "dialect": "py_re",
        "call_kind": "search",
        "declared_domain": {"alphabet": "unicode"},
        "unencodable_reason": "lookbehind",
    }
    jsonschema.validate(rec, compiled_pattern_schema())


def test_schemas_are_loadable_json():
    for name in ("extractor_record.schema.json", "compiled_pattern.schema.json"):
        path = Path(__file__).resolve().parents[1] / "regexproof" / "schemas" / name
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["$schema"]
