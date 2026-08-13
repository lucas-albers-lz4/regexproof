"""Fix-wave Phase 4 (#72): ModSecurity negation reject-unsupported."""

from __future__ import annotations

from regexproof.batch.negation_policy import (
    NEGATED_UNSUPPORTED_REASON,
    NEGATION_POLICY,
    should_reject_negated,
)
from regexproof.batch.runner import _compile_all
from regexproof.batch.triage import triage_records_from_compiled


def test_all_dialects_reject_negation():
    assert set(NEGATION_POLICY) == {"py_re", "ecma", "re2", "pcre"}
    for d in NEGATION_POLICY:
        assert should_reject_negated(d)


def test_compile_all_rejects_negated_records():
    records = [
        {
            "regex_id": "n" * 32,
            "pattern": "evil",
            "flags": "",
            "dialect": "pcre",
            "call_kind": "search",
            "site": "rules/x.conf:1:0",
            "negated": True,
            "selector": False,
        },
        {
            "regex_id": "s" * 32,
            "pattern": "ARGS:/foo/",
            "flags": "",
            "dialect": "pcre",
            "call_kind": "search",
            "site": "rules/x.conf:2:0",
            "negated": True,
            "selector": True,
        },
        {
            "regex_id": "p" * 32,
            "pattern": "ok",
            "flags": "",
            "dialect": "pcre",
            "call_kind": "search",
            "site": "rules/x.conf:3:0",
            "negated": False,
        },
    ]
    compiled = _compile_all(records, lift_inline=False, corpus_slug="coreruleset")
    compiled = [pair[0] for pair in compiled]
    by_id = {r["regex_id"]: r for r in compiled}
    assert by_id["n" * 32]["encodable"] is False
    assert by_id["n" * 32]["compile_reason"] == NEGATED_UNSUPPORTED_REASON
    assert by_id["s" * 32]["compile_reason"] == NEGATED_UNSUPPORTED_REASON
    assert by_id["p" * 32]["encodable"] is True

    triage = triage_records_from_compiled(compiled)
    neg_rows = [r for r in triage if r.get("negated")]
    assert len(neg_rows) == 2
    assert all(r["unencodable_reason"] == NEGATED_UNSUPPORTED_REASON for r in neg_rows)
    assert any(r.get("selector") for r in neg_rows)
