"""Batch evidence gates + {1} compiler crash regression + toolkit-fix gates."""

from __future__ import annotations

import pytest
from z3 import InRe, String

from regexproof.batch.evidence import evidence_gate_errors, enforce_evidence_gates
from regexproof.compiler import compile_pattern


@pytest.mark.parametrize(
    "pattern,dialect",
    [
        ("x{1}", "ecma"),
        ("ab{1,1}c", "pcre"),
        ("a{1}", "re2"),
        ("(?:xy){1}", "pcre"),
        ("z{1,1}", "py_re"),
    ],
)
def test_exact_single_quantifier_no_longer_crashes(pattern, dialect):
    cr = compile_pattern(pattern, "", dialect, "fullmatch")
    assert cr.encodable, (dialect, pattern, cr.unencodable_reason)


def test_negated_class_encodes_without_complement_star():
    from z3 import sat, unsat

    cr = compile_pattern(r"^[^ab]$", "", "pcre", "fullmatch")
    assert cr.encodable, cr.unencodable_reason
    s = String("s")
    z3 = __import__("z3")
    solver = z3.Solver()
    solver.add(InRe(s, cr.mirror))
    solver.add(s == "c")
    assert solver.check() == sat
    solver2 = z3.Solver()
    solver2.add(InRe(s, cr.mirror))
    solver2.add(s == "a")
    assert solver2.check() == unsat


def test_scoped_inline_i_fold():
    from z3 import sat

    cr = compile_pattern(r"x(?i:ab)y", "", "pcre", "fullmatch")
    assert cr.encodable, cr.unencodable_reason
    s = String("s")
    z3 = __import__("z3")
    for witness, expect_sat in [("xABy", True), ("xaby", True), ("xACy", False)]:
        solver = z3.Solver()
        solver.add(InRe(s, cr.mirror))
        solver.add(s == witness)
        assert (solver.check() == sat) is expect_sat, witness


def test_hex_escape_soundness_codepoint_not_literal_text():
    """TRAPS #23: [\\x22] must accept '"' and reject literal 'x22'."""
    from z3 import InRe, String, sat, unsat

    for dialect, pattern in (
        ("pcre", r"^[\x22]$"),
        ("pcre", r"^[\x{22}]$"),
        ("re2", r"^[\x22]$"),
        ("ecma", r"^[\x22]$"),
        ("py_re", r"^[\x22]$"),
    ):
        cr = compile_pattern(pattern, "", dialect, "fullmatch")
        assert cr.encodable, (dialect, pattern, cr.unencodable_reason)
        s = String("s")
        z3 = __import__("z3")
        ok = z3.Solver()
        ok.add(InRe(s, cr.mirror))
        ok.add(s == '"')
        assert ok.check() == sat, (dialect, pattern)
        bad = z3.Solver()
        bad.add(InRe(s, cr.mirror))
        bad.add(s == "x22")
        assert bad.check() == unsat, (dialect, pattern)
        bad2 = z3.Solver()
        bad2.add(InRe(s, cr.mirror))
        bad2.add(s == "x2")
        assert bad2.check() == unsat, (dialect, pattern)


def test_hex_range_in_class():
    from z3 import InRe, String, sat

    cr = compile_pattern(r"^[\x21-\x7e]$", "", "pcre", "fullmatch")
    assert cr.encodable, cr.unencodable_reason
    s = String("s")
    z3 = __import__("z3")
    for ch, expect in [("!", True), ("~", True), (" ", False), ("\x7f", False)]:
        solver = z3.Solver()
        solver.add(InRe(s, cr.mirror))
        solver.add(s == ch)
        assert (solver.check() == sat) is expect, repr(ch)


def test_lazy_strip_preserves_optional_hex_brace():
    from regexproof.compiler.pcre_strip import strip_language_transparent

    assert strip_language_transparent(r"\x{2f}?") == r"\x{2f}?"
    assert strip_language_transparent(r"a{2,3}?") == r"a{2,3}"
    cr = compile_pattern(r"^\x{41}?$", "", "pcre", "fullmatch")
    assert cr.encodable, cr.unencodable_reason


def test_ecma_rejects_scoped_i():
    cr = compile_pattern(r"(?i:a)", "", "ecma", "search")
    assert not cr.encodable
    assert cr.unencodable_reason == "inline-flag"


def test_timeout_on_z3_kind_is_error():
    errs = evidence_gate_errors(
        [{"regex_id": "a" * 32, "kind": "rule_diff", "result": "timeout"}]
    )
    assert errs and "timeout" in errs[0]


def test_redos_timeout_not_z3_gate():
    errs = evidence_gate_errors(
        [{"regex_id": "a" * 32, "kind": "redos", "result": "timeout"}]
    )
    assert errs == []


def test_require_ground_truth_sat():
    errs = evidence_gate_errors(
        [
            {
                "regex_id": "b" * 32,
                "kind": "rule_diff",
                "result": "sat",
                "ground_truth_status": None,
            }
        ],
        require_ground_truth=True,
    )
    assert errs
    errs_ok = evidence_gate_errors(
        [
            {
                "regex_id": "b" * 32,
                "kind": "rule_diff",
                "result": "sat",
                "ground_truth_status": "reproduced",
            }
        ],
        require_ground_truth=True,
    )
    assert errs_ok == []


def test_fail_planned_lists_question_ids():
    errs = evidence_gate_errors(
        [
            {
                "regex_id": "inventory:v-shape1",
                "kind": "property",
                "result": "planned",
                "detail": {"question_id": "v-shape1-injection-chars"},
            }
        ],
        fail_planned=True,
    )
    assert any("v-shape1-injection-chars" in e for e in errs)


def test_enforce_raises():
    with pytest.raises(SystemExit):
        enforce_evidence_gates(
            [{"regex_id": "c" * 32, "kind": "property", "result": "unknown"}]
        )
