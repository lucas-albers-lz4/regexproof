"""Phase 2 registration gates (PR A): the \p gate + D7 structural checks.

AC coverage (issue #218):
- \p gate: real \p{}/\P{ tokens rejected (both cases, in-class, quantified);
  escaped literals pass.
- D7 anchored-definition: `^abc$` passes; partial anchors (`^abc`, `abc$`) and
  `^a$|^b$` (the documented conservative false-positive) FAIL registration.
- D7 wrap-validity: `.*abc.*` passes; unparenthesized `.*a|b` and unwrapped
  `abc` FAIL.
- Parser fixtures pass: escaped parens, non-capturing groups, anchor-looking
  chars in classes.
- Registry: prop() carries the new fields with correct defaults; the CLI runs
  the gate (validate_registry) and exits 2 on failures.
"""

from __future__ import annotations

import pytest

from regexproof.harness import core
from regexproof.harness.gates import (
    RegistrationError,
    check_anchored,
    check_p_gate,
    check_wrap,
    validate_pattern,
)


# --- \p gate ----------------------------------------------------------------
def test_p_gate_rejects_real_tokens():
    for pat in (r"\p{L}", r"\P{L}", r"[\p{L}]", r"[\p{L}\d]", r"\p{L}+", r"\p{Lu}"):
        with pytest.raises(RegistrationError, match=r"\\p"):
            check_p_gate(pat)


def test_p_gate_accepts_escaped_literals():
    for pat in (r"\\p{L}", r"[\\p{L}]"):
        check_p_gate(pat)  # no raise


# --- D7 anchored-definition -------------------------------------------------
def test_anchored_pass():
    check_anchored(r"^abc$")


def test_anchored_partial_fails():
    for pat in (r"^abc", r"abc$"):
        with pytest.raises(RegistrationError, match="anchored"):
            check_anchored(pat)


def test_anchored_top_level_alternation_fails_conservative():
    # ^a$|^b$ — every branch anchored, but top-level alternation: the
    # documented conservative false-positive (rewrite: ^(?:a|b)$).
    with pytest.raises(RegistrationError, match="alternation"):
        check_anchored(r"^a$|^b$")


# --- D7 wrap-validity -------------------------------------------------------
def test_wrap_pass():
    check_wrap(r".*abc.*")


def test_wrap_unparenthesized_fails():
    with pytest.raises(RegistrationError, match="wrap"):
        check_wrap(r".*a|b")


def test_wrap_unwrapped_fails():
    with pytest.raises(RegistrationError, match="wrap"):
        check_wrap(r"abc")


# --- parser fixtures --------------------------------------------------------
def test_parser_fixtures_pass():
    for pat in (r"\(a\)", r"(?:abc)", r"[a^b]"):
        validate_pattern(pat)  # no raise


def test_parser_rejects_unbalanced():
    # balanced grouping is enforced as part of the D7 checks: a wrapped pattern
    # must parse (regexpp throws on unterminated groups).
    with pytest.raises(RegistrationError, match="not encodable"):
        validate_pattern(r".*(abc.*", search_wrapped=True)


# --- registry fields --------------------------------------------------------
def test_prop_defaults():
    @core.prop("t-phase2-defaults", "test")
    def _p():
        # never run — registration-only test
        return [], True

    e = core.REGISTRY["t-phase2-defaults"]
    assert e["backend"] == "seq"
    assert e["decomposition_trace"] is None
    assert e["search_wrapped"] is False
    assert e["pattern"] is None
    del core.REGISTRY["t-phase2-defaults"]


def test_validate_registry_local():
    reg = {
        "ok-anchored": {
            "pattern": r"^abc$",
            "pattern_flags": "",
            "search_wrapped": False,
            "kind": "property",
        },
        "ok-wrapped": {
            "pattern": r".*abc.*",
            "pattern_flags": "",
            "search_wrapped": True,
            "kind": "property",
        },
        "bad-partial": {
            "pattern": r"^abc",
            "pattern_flags": "",
            "search_wrapped": False,
            "kind": "property",
        },
        "bad-p": {
            "pattern": r"\p{L}",
            "pattern_flags": "",
            "search_wrapped": False,
            "kind": "property",
        },
    }
    failures, checked = core.validate_registry(reg)
    assert checked == 4
    assert len(failures) == 2
    assert any("bad-partial" in f for f in failures)
    assert any("bad-p" in f for f in failures)


def test_validate_registry_real_registry_no_failures():
    # Built-ins declare no source patterns yet → gate is a no-op (backward
    # compatible: the golden suite is unaffected).
    failures, checked = core.validate_registry()
    assert checked == 0
    assert failures == []


def test_validate_registry_empty_pattern_validated():
    # An explicitly declared EMPTY pattern must still run the gates (a "" source
    # pattern is a valid regex — the empty string language — and must not
    # bypass registration). With search_wrapped it fails wrap-validity.
    reg = {
        "empty-wrapped": {
            "pattern": "",
            "pattern_flags": "",
            "search_wrapped": True,
            "kind": "property",
        },
        "empty-plain": {
            "pattern": "",
            "pattern_flags": "",
            "search_wrapped": False,
            "kind": "property",
        },
    }
    failures, checked = core.validate_registry(reg)
    assert checked == 2
    # empty-wrapped fails wrap-validity (no .* prefix/suffix); empty-plain fails
    # anchored-definition (no ^/$) — neither bypasses the gates.
    assert len(failures) == 2
    assert any("empty-wrapped" in f for f in failures)
    assert any("empty-plain" in f for f in failures)


def test_cli_gate_failure_exits_2(monkeypatch, capsys):
    from regexproof.harness import cli

    def _bad_registry(registry=None):
        return ["demo: bad pattern"], 1

    monkeypatch.setattr(cli, "validate_registry", _bad_registry)
    rc = cli.main(["--list"])
    assert rc == 2
    assert "REGISTRATION GATE FAILURE" in capsys.readouterr().err
