"""Pinned ReDoS smoke fixtures → exact expected results."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from regexproof.redos.runner import analyze_record
from regexproof.regex_id import make_regex_id
from tests.toolchain import require_recheck


@pytest.fixture(autouse=True)
def _recheck():
    require_recheck()

CORPUS = Path(__file__).resolve().parent / "fixtures" / "redos" / "corpus.json"


def _materialize(fixture: dict) -> dict:
    ext = dict(fixture["extractor"])
    ext["regex_id"] = make_regex_id(
        repo=ext["repo"],
        pattern=ext["pattern"],
        flags=ext.get("flags") or "",
        dialect=ext["dialect"],
        call_kind=ext["call_kind"],
        site=ext["site"],
    )
    return ext


@pytest.fixture(scope="module")
def corpus():
    return json.loads(CORPUS.read_text(encoding="utf-8"))


@pytest.mark.parametrize(
    "fixture_id",
    [
        "moment-cve-2022-31129",
        "ansi-regex-vulnerable",
        "trim-newlines-vulnerable",
        "python-nested-quantifier",
        "control-safe",
        "re2-unsupported",
    ],
)
def test_smoke_fixture(corpus, fixture_id):
    fixture = next(f for f in corpus["fixtures"] if f["id"] == fixture_id)
    rec = _materialize(fixture)
    # Preserve id across analyze
    findings = analyze_record(rec, triage=False)
    assert findings
    assert all(f["regex_id"] == rec["regex_id"] for f in findings)
    for tool, expect in fixture["expect_tools"].items():
        hit = [f for f in findings if f["tool"] == tool]
        assert hit, f"missing tool {tool} in {[f['tool'] for f in findings]}"
        assert hit[0]["result"] == expect["result"], hit[0]
        if expect.get("severity"):
            assert hit[0].get("severity") == expect["severity"]
        # Never silently safe on error paths
        assert hit[0]["result"] != "safe" or expect["result"] == "safe"


def test_error_path_not_safe():
    rec = {
        "regex_id": make_regex_id("r", "(", "", "ecma", "search", "e.js:1:0"),
        "pattern": "(",  # invalid
        "flags": "",
        "dialect": "ecma",
        "call_kind": "search",
        "site": "e.js:1:0",
        "repo": "r",
        "file": "e.js",
    }
    findings = analyze_record(rec, triage=False)
    assert findings
    assert findings[0]["result"] in ("error", "timeout", "vulnerable", "safe")
    # Invalid pattern should not be reported as safe by recheck typically → error
    # Accept vulnerable/error/timeout — forbid only accidental silent pass without tool version
    assert findings[0]["tool_version"]
    if findings[0]["result"] == "safe":
        pytest.fail("invalid pattern must not be reported safe")
