"""ReDoS schema validation + regex_id preservation."""

from __future__ import annotations

import jsonschema

from regexproof.redos.schema import make_finding
from regexproof.regex_id import make_regex_id
from regexproof.schemas import redos_finding_schema


def test_redos_schema_validates():
    rid = make_regex_id(
        repo="r",
        pattern="a+",
        flags="",
        dialect="ecma",
        call_kind="search",
        site="a.js:1:0",
    )
    finding = make_finding(
        regex_id=rid,
        tool="recheck",
        tool_version="4.5.0",
        result="vulnerable",
        dialect="ecma",
        pattern="a+",
        flags="",
        site="a.js:1:0",
        severity="exponential",
    )
    jsonschema.validate(finding, redos_finding_schema())


def test_error_not_coerced_to_safe():
    rid = make_regex_id("r", "bad", "", "ecma", "search", "a.js:1:0")
    f = make_finding(
        regex_id=rid,
        tool="recheck",
        tool_version="4.5.0",
        result="error",
        dialect="ecma",
        pattern="bad",
        flags="",
        site="a.js:1:0",
        error_message="boom",
    )
    assert f["result"] == "error"


def test_regex_id_preserved_from_extractor_fields():
    fields = dict(
        repo="demo/repo",
        pattern=r"^(a+)+$",
        flags="",
        dialect="ecma",
        call_kind="search",
        site="x.js:2:0",
    )
    rid = make_regex_id(**fields)
    finding = make_finding(
        regex_id=rid,
        tool="recheck",
        tool_version="4.5.0",
        result="vulnerable",
        dialect=fields["dialect"],
        pattern=fields["pattern"],
        flags=fields["flags"],
        site=fields["site"],
    )
    assert finding["regex_id"] == rid
    assert finding["regex_id"] == make_regex_id(**fields)
