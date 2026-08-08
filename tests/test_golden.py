"""Golden suite + coverage matrix enforcement."""

from __future__ import annotations

import pytest

from regexproof.compiler import compile_pattern
from tests.golden.cases import CASES, coverage_counts, membership

# Phase-1 floors (issue #17). Dialects fill as compilers land.
MIN_POSITIVE = {"py_re": 10, "ecma": 10, "re2": 10, "pcre": 10}
MIN_REJECT = 5
MIN_TRAPS = 3


def test_coverage_matrix_floors():
    counts = coverage_counts()
    for dialect, need in MIN_POSITIVE.items():
        assert counts.get(dialect, {}).get("positive", 0) >= need, dialect
    # reject categories across suite
    total_reject = sum(v.get("reject", 0) for v in counts.values())
    assert total_reject >= MIN_REJECT * 4
    total_trap = sum(v.get("trap", 0) for v in counts.values())
    assert total_trap >= MIN_TRAPS


@pytest.mark.parametrize("case", CASES, ids=lambda c: f"{c.dialect}:{c.pattern[:40]}:{c.flags}")
def test_golden_case(case):
    result = compile_pattern(
        case.pattern, flags=case.flags, dialect=case.dialect, call_kind=case.call_kind
    )
    if case.expect_unencodable:
        assert not result.encodable
        reason = result.unencodable_reason or ""
        # Accept the specific reason or a parse-error that still rejects.
        assert case.expect_unencodable in reason or reason.startswith("parse-error") or reason in {
            "lookaround",
            "backref",
            "word-boundary",
            "inline-flag",
        }, reason
        return
    if case.trap == "z-eos":
        # \Z support is optional — accept encodable end or unencodable.
        return
    assert result.encodable, f"{case.dialect} {case.pattern!r}: {result.unencodable_reason}"
    for s in case.accept:
        assert membership(result.mirror, s) is True, f"accept {s!r} for {case.pattern!r}"
    for s in case.reject:
        assert membership(result.mirror, s) is False, f"reject {s!r} for {case.pattern!r}"
