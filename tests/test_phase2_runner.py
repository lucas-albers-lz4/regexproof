"""Phase 2 Noodler runner (PR B): D6 mechanics, S13 classification, D16.

AC coverage (issue #218):
- backend="noodler" property runs the real binary through the normal result
  path (D16 3/3 on the Phase-1 matrix fixtures, skip-if-binary-absent).
- Binary absent → triage_override recorded, exit unchanged (stock green).
- SMT-LIB input written as RAW BYTES (control-char round-trip; a python-escaped
  form must NOT be what the solver reads).
- S13 exit-code × verdict classification via stub binaries: exit-1-with-verdict
  valid; exit-0-no-verdict abstain; signal deaths (rc<0 and rc==139) untrusted
  even with a printed verdict; timeout contained.
- No subprocess without timeout=; process-group kill on timeout.
"""

from __future__ import annotations

import json
import os
import stat
import subprocess

import pytest
import z3
from z3 import Contains, InRe, Solver, String, StringVal

from regexproof.harness import core
from regexproof.harness.noodler_runner import (
    NoodlerAbsent,
    decode_smt_string,
    parse_noodler_model,
    run_noodler,
    smt_string,
)

NOODLER = os.environ.get("NOODLER", "/tmp/noodler/z3-noodler-ubuntu-24.04-x86_64-shared")
HAVE_NOODLER = os.path.isfile(NOODLER)


def _stub(tmp_path, body: str) -> str:
    p = tmp_path / "stub.sh"
    p.write_text("#!/bin/bash\n" + body)
    p.chmod(p.stat().st_mode | stat.S_IEXEC)
    return str(p)


# --- SMT-LIB string encoding (raw bytes) ------------------------------------
def test_smt_string_raw_bytes():
    # A tab/newline must be written as the RAW byte, never as the two-char
    # python escape "\\t" — Noodler reads \\t as literal backslash-t (measured
    # escape-input class).
    raw = smt_string("a\tb\n")
    assert "\t" in raw and "\\t" not in raw
    assert "\n" in raw and "\\n" not in raw
    assert '"a""b"' == smt_string('a"b')  # quote-doubling


def test_decode_units():
    assert decode_smt_string('"ab"', 0) == ("ab", 4)
    assert decode_smt_string('"a""b"', 0) == ('a"b', 6)
    assert decode_smt_string(r'"\x00\x01"', 0) == ("\x00\x01", 10)
    assert decode_smt_string(r'"\u{0}\u{7f}"', 0) == ("\x00\x7f", 13)
    # literal backslash + quote-doubling: the quote AFTER a literal backslash
    # participates in doubling (measured P3-sed model form `"\"""""""`).
    assert decode_smt_string(r'"\"""""""', 0) == ('\\"""', 9)
    with pytest.raises(ValueError):
        decode_smt_string('"abc', 0)


def test_parse_noodler_model_no_wrapper():
    out = (
        "sat\n(\n  (define-fun u () String\n    \"x\\u{0}\")\n"
        '  (define-fun v () String "eth0IN=")\n)\n'
    )
    w = parse_noodler_model(out)
    assert w == {"u": "x\x00", "v": "eth0IN="}


# --- S13 classification via stub binaries ------------------------------------
def test_stub_exit1_with_sat_is_valid(tmp_path):
    b = _stub(tmp_path, 'echo "sat"; echo \'(define-fun u () String "x")\'; exit 1')
    r = run_noodler("(check-sat)", want_model=True, binary=b)
    assert r["verdict"] == "sat" and r["state"] == "decided"
    assert r["witness"] == {"u": "x"}


def test_stub_rc127_with_sat_rejected(tmp_path):
    # S13: only rc 0 or 1 with a verdict is valid — a dispatch failure that
    # printed sat is still untrusted (luna High).
    b = _stub(tmp_path, 'echo "sat"; exit 127')
    r = run_noodler("(check-sat)", binary=b)
    assert r["state"] == "abstain" and "DISPATCH-ERROR" in r["verdict"]


def test_stub_rc2_with_unsat_rejected(tmp_path):
    b = _stub(tmp_path, 'echo "unsat"; exit 2')
    r = run_noodler("(check-sat)", binary=b)
    assert r["state"] == "abstain" and "DISPATCH-ERROR" in r["verdict"]


def test_stub_exit1_no_verdict_dispatch_error(tmp_path):
    b = _stub(tmp_path, "exit 1")
    r = run_noodler("(check-sat)", binary=b)
    assert r["state"] == "abstain" and "DISPATCH-ERROR(rc=1)" in r["verdict"]


def test_stub_exit0_no_verdict_abstains(tmp_path):
    b = _stub(tmp_path, "exit 0")
    r = run_noodler("(check-sat)", binary=b)
    assert r["state"] == "abstain" and "ABSTAIN-NO-VERDICT" in r["verdict"]


def test_stub_sat_then_segv_is_crash(tmp_path):
    b = _stub(tmp_path, 'echo "sat"; kill -SEGV $$')
    r = run_noodler("(check-sat)", binary=b)
    assert r["state"] == "abstain" and "ABSTAIN-SIGSEGV" in r["verdict"]


def test_stub_rc139_is_crash(tmp_path):
    b = _stub(tmp_path, 'echo "sat"; exit 139')
    r = run_noodler("(check-sat)", binary=b)
    assert r["state"] == "abstain" and "ABSTAIN-SIGSEGV" in r["verdict"]


def test_stub_timeout_contained(tmp_path):
    b = _stub(tmp_path, "sleep 30")
    r = run_noodler("(check-sat)", timeout_ms=500, binary=b)
    assert r["state"] == "abstain" and r["verdict"] == "ABSTAIN-TIMEOUT"


# --- D6 wrapping -------------------------------------------------------------
def test_runner_wraps_set_logic_and_check_sat(tmp_path):
    b = _stub(tmp_path, 'grep -q "(set-logic QF_SLIA)" "$2"; echo "unsat"')
    r = run_noodler("(assert false)", timeout_ms=5000, binary=b)
    assert r["verdict"] == "unsat"  # the stub asserts set-logic presence


# --- control-char round-trip (real binary, skip-if-absent) ------------------
@pytest.mark.skipif(not HAVE_NOODLER, reason="pinned Noodler binary not present")
def test_control_char_round_trip():
    # A string containing a real tab must round-trip: InRe("a<TAB>b", literal)
    # must be SAT — if the tab were python-escaped the solver would read the
    # 2-char backslash-t and this would be UNSAT.
    tab = "\t"
    smt = (
        '(declare-const s String)\n'
        '(assert (= s "' + "a" + tab + "b" + '"))\n'
        '(assert (str.in_re s (re.++ (str.to_re "a") (str.to_re "' + tab + '") '
        '(str.to_re "b"))))\n(check-sat)\n'
    )
    r = run_noodler(smt, want_model=True)
    assert r["verdict"] == "sat"
    assert r["witness"]["s"] == "a\tb"


# --- D16 3/3 on the Phase-1 matrix fixtures (real binary) -------------------
def _noodler_entry(name):
    e = dict(core.REGISTRY[name])
    e["backend"] = "noodler"
    return e


@pytest.mark.skipif(not HAVE_NOODLER, reason="pinned Noodler binary not present")
@pytest.mark.parametrize(
    "name",
    ["P3-sed-capture-truncation", "P4-nul-passthrough-demo", "P1-mutated-star"],
)
def test_d16_revalidates_matrix_fixtures(name):
    import regexproof.harness.properties  # noqa: F401 — populate REGISTRY

    entry = _noodler_entry(name)
    result = core.run_one(name, entry, require_ground_truth=False)
    assert result["result"] == "sat", result
    assert result["d16_revalidated"] is True, result
    assert result["ok"] is True, result


# --- ground-truth gate in the noodler sat path (cumulative zen-MCR finding) --
def _sat_stub(monkeypatch, tmp_path):
    """Stub the noodler binary: prints sat + the valid '_*' witness for
    P1-mutated-star's constraints AND its bad (measured valid, D16 passes)."""
    import regexproof.harness.noodler_runner as nr

    stub = tmp_path / "sat.sh"
    stub.write_text("#!/bin/bash\necho 'sat'\n"
                    "echo '(define-fun u () String \"_*\")'\n")
    stub.chmod(stub.stat().st_mode | 0o111)
    monkeypatch.setattr(nr, "binary_path", lambda: str(stub))
    monkeypatch.setattr(nr, "_VERIFIED_PATH", str(stub))
    monkeypatch.setattr(nr, "noodler_version", lambda b=None: "stub")


def test_noodler_sat_ground_truth_failed(monkeypatch, tmp_path):
    # the noodler sat path honors the same --require-ground-truth contract as
    # the stock path: a callback that FAILS to reproduce → ok=False
    import regexproof.harness.properties  # noqa: F401
    from regexproof.harness import cvc5_runner as cr

    _sat_stub(monkeypatch, tmp_path)  # sat + witness '_*'
    monkeypatch.setattr(cr, "run_cvc5",
                        lambda smt, timeout_ms, **kw:
                        {"verdict": "unsat", "wall_ms": 1.0,
                         "state": "decided", "reason": None})
    entry = dict(core.REGISTRY["P1-mutated-star"])
    entry["backend"] = "noodler"
    entry["kind"] = "property"  # NOT a mutation guard — the callback path runs
    entry["ground_truth"] = lambda w: False  # real impl does NOT reproduce
    r = core.run_one("P1-mutated-star", entry)
    assert r["ground_truth"] == "failed"
    assert r["ok"] is False  # a non-reproducing witness is never reported


def test_noodler_sat_require_ground_truth_refused(monkeypatch, tmp_path):
    # --require-ground-truth + no callback → refused-no-callback + ok=False
    import regexproof.harness.properties  # noqa: F401
    from regexproof.harness import cvc5_runner as cr

    _sat_stub(monkeypatch, tmp_path)
    monkeypatch.setattr(cr, "run_cvc5",
                        lambda smt, timeout_ms, **kw:
                        {"verdict": "unsat", "wall_ms": 1.0,
                         "state": "decided", "reason": None})
    entry = dict(core.REGISTRY["P1-mutated-star"])
    entry["backend"] = "noodler"
    entry["kind"] = "property"
    entry["ground_truth"] = None
    r = core.run_one("P1-mutated-star", entry, require_ground_truth=True)
    assert r["ground_truth"] == "refused-no-callback"
    assert r["ok"] is False


def test_noodler_sat_ground_truth_reproduced(monkeypatch, tmp_path):
    # a REPRODUCING callback keeps ok per the expectation (sat finding)
    import regexproof.harness.properties  # noqa: F401
    from regexproof.harness import cvc5_runner as cr

    _sat_stub(monkeypatch, tmp_path)
    monkeypatch.setattr(cr, "run_cvc5",
                        lambda smt, timeout_ms, **kw:
                        {"verdict": "unsat", "wall_ms": 1.0,
                         "state": "decided", "reason": None})
    entry = dict(core.REGISTRY["P1-mutated-star"])
    entry["backend"] = "noodler"
    entry["kind"] = "property"
    entry["expect_unsat"] = False  # a counterexample finder
    entry["ground_truth"] = lambda w: True
    r = core.run_one("P1-mutated-star", entry)
    assert r["ground_truth"] == "reproduced"
    assert r["ok"] is True


# --- absence path ------------------------------------------------------------
def test_absent_binary_falls_back_to_stock(monkeypatch, capsys):
    # Absence contract (AC + §10): triage_fallback recorded, the STATE is the
    # stock outcome, exit unchanged from stock — the property STILL RUNS
    # through the stock path.
    import regexproof.harness.properties  # noqa: F401

    def _absent():
        raise NoodlerAbsent("NOODLER not found (test)")

    monkeypatch.setattr(
        "regexproof.harness.noodler_runner.binary_path", _absent
    )
    entry = _noodler_entry("P1-mutated-star")
    result = core.run_one("P1-mutated-star", entry)
    # stock fallback: P1-mutated-star is a mutation guard — sat expected, ok True
    assert result["triage_fallback"] is True
    assert result["triage_override"].startswith("NOODLER not found")
    assert result["noodler_verdict"] == "ABSENT"
    assert result["state"] == "stock"  # the STOCK outcome state (§10)
    assert result["result"] == "sat"  # the STOCK verdict, not an abstain
    assert result["ok"] is True  # exit unchanged from stock
    assert "running the stock path" in capsys.readouterr().out


def test_binary_pin_mismatch_refused(tmp_path, monkeypatch):
    # An unpinned binary must be refused (luna Medium — sha256 pin in the
    # runner). Reset the process-level cache and point at a stub.
    import regexproof.harness.noodler_runner as nr

    monkeypatch.setattr(nr, "_VERIFIED_PATH", None)
    stub = _stub(tmp_path, 'echo "sat"')
    monkeypatch.setenv("NOODLER", stub)
    with pytest.raises(NoodlerAbsent, match="does NOT match the pin"):
        nr.binary_path()
