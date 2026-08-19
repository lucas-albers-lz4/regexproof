"""Phase 3 D15 verdict resolution (PR B): the total order, the mechanical
disagreement rule, wrong-verdict events, disagreement exit 2.

AC coverage (issue #219):
- D15 table unit-tested on ALL 27 triples (3^3 over sat/unsat/unknown primary,
  cross, reproduction-outcome); abstain-involving combinations are the
  separate abstention fixtures (never a disagreement)
- Synthetic disagreement fixture → HARD FAIL + exit 2
- Mechanical disagreement definition tested: one pair where reproduction fails
  (genuine disagreement), one where reproduction succeeds but the
  wrong-verdict event is still recorded
- Backend absence and cross-check-leg absence remain distinct recorded states
"""

from __future__ import annotations

from pathlib import Path

import pytest

from regexproof.harness import core
from regexproof.harness.d15 import order, resolve

ROOT = Path(__file__).resolve().parents[1]


# --- the D15 27-triple table (3^3) -----------------------------------------
def test_d15_total_order():
    assert order("sat") < order("unsat")
    with pytest.raises(ValueError):
        order("unknown")  # abstentions are OUTSIDE the order (S16)
    with pytest.raises(ValueError):
        order(None)


def test_d15_27_triple_table():
    # axes: primary ∈ {sat, unsat, unknown}; cross ∈ {sat, unsat, unknown};
    # reproduction outcome ∈ {sat, unsat, unknown} (tri-state — luna r1 on #233:
    # a reproduction abstention is OUTSIDE the order, never a disagreement)
    expected = {}
    for p in ("sat", "unsat", "unknown"):
        for c in ("sat", "unsat", "unknown"):
            for r in ("sat", "unsat", "unknown"):
                key = (p, c, r)
                if p == "unknown" or c == "unknown":
                    expected[key] = "abstain-involved"
                elif p == c:
                    expected[key] = "agree"
                elif r == "unknown":
                    expected[key] = "abstain-involved"  # reproduction abstained
                else:  # concrete disagreement with a concrete reproduction
                    expected[key] = ("wrong-verdict-event" if r == "sat"
                                     else "disagreement")
    for (p, c, r), want in expected.items():
        res = resolve(p, c, reproduce=(lambda: r))
        assert res["kind"] == want, (p, c, r, res)
        assert res["disagreement"] == (want == "disagreement"), (p, c, r)
        assert res["wrong_verdict_event"] == (want == "wrong-verdict-event"), \
            (p, c, r)


def test_d15_no_callback_conservative_disagreement():
    # The unavailable-reproduction case (cvc5-sat witness not captured) is a
    # conservative genuine disagreement — the conflict cannot be cleared.
    res = resolve("unsat", "sat")
    assert res["kind"] == "disagreement"
    assert res["disagreement"] is True


def test_d15_reproduction_fails_genuine_disagreement():
    res = resolve("sat", "unsat", reproduce=lambda: "unsat")
    assert res["disagreement"] is True
    assert "NOT reproduced" in res["detail"]


def test_d15_reproduction_succeeds_wrong_verdict_event():
    res = resolve("sat", "unsat", reproduce=lambda: "sat")
    assert res["disagreement"] is False
    assert res["wrong_verdict_event"] is True


def test_d15_reproduction_abstention_not_disagreement():
    # a timeout/sigsegv/no-verdict reproduction is OUTSIDE the order (S16) —
    # never a disagreement and never a wrong-verdict event (luna r1 on #233)
    res = resolve("sat", "unsat", reproduce=lambda: "unknown")
    assert res["kind"] == "abstain-involved"
    assert res["disagreement"] is False
    assert res["wrong_verdict_event"] is False
    assert "abstained" in res["detail"]


# --- synthetic disagreement through the runner (exit 2) ----------------------
def _noodler_sat_stub(monkeypatch, tmp_path, witness='"_*"'):
    """Monkeypatch the runner's binary_path to a stub printing sat + a model,
    and run_cvc5 to a controllable fake. The default witness '_*' satisfies
    P1-mutated-star's constraints (first char [a-z_]) AND its bad (contains
    '*') — a valid D16 witness (measured)."""
    import regexproof.harness.noodler_runner as nr

    stub = tmp_path / "sat.sh"
    stub.write_text(
        "#!/bin/bash\necho 'sat'\n"
        f"echo '(define-fun u () String {witness})'\n"
    )
    stub.chmod(stub.stat().st_mode | 0o111)
    monkeypatch.setattr(nr, "binary_path", lambda: str(stub))
    monkeypatch.setattr(nr, "_VERIFIED_PATH", str(stub))
    monkeypatch.setattr(nr, "noodler_version", lambda b=None: "stub")
    import regexproof.harness.properties  # noqa: F401
    return stub


def test_disagreement_hard_fail_via_runner(monkeypatch, tmp_path):
    from regexproof.harness import cvc5_runner as cr

    _noodler_sat_stub(monkeypatch, tmp_path)
    calls = {"n": 0}

    def _cvc5(smt, timeout_ms, **kw):
        calls["n"] += 1
        # first call: the cross-check → unsat; second: the reproduction →
        # unsat again (witness NOT reproduced) → genuine disagreement
        return {"verdict": "unsat", "wall_ms": 1.0, "state": "decided",
                "reason": None}

    monkeypatch.setattr(cr, "run_cvc5", _cvc5)
    entry = dict(core.REGISTRY["P1-mutated-star"])
    entry["backend"] = "noodler"
    r = core.run_one("P1-mutated-star", entry)
    assert r["d15"] == "disagreement"
    assert r["disagreement"] is True
    assert r["wrong_verdict_event"] is False
    assert calls["n"] == 2  # cross-check + reproduction


def test_wrong_verdict_event_via_runner(monkeypatch, tmp_path):
    from regexproof.harness import cvc5_runner as cr

    _noodler_sat_stub(monkeypatch, tmp_path)

    def _cvc5(smt, timeout_ms, **kw):
        # cross-check → unsat; reproduction → sat (the unsat side was wrong)
        return {"verdict": "unsat" if "(assert (= u" not in smt else "sat",
                "wall_ms": 1.0, "state": "decided", "reason": None}

    monkeypatch.setattr(cr, "run_cvc5", _cvc5)
    entry = dict(core.REGISTRY["P1-mutated-star"])
    entry["backend"] = "noodler"
    r = core.run_one("P1-mutated-star", entry)
    assert r["d15"] == "wrong-verdict-event"
    assert r["disagreement"] is False
    assert r["wrong_verdict_event"] is True


def test_witness_unvalidated_gates_d15(monkeypatch, tmp_path):
    # D16 runs BEFORE D15 (luna r1 on #233): an invalid sat witness must be
    # rejected as witness-unvalidated (exit 1) — the cross-check leg and the
    # disagreement machinery never run.
    from regexproof.harness import cvc5_runner as cr

    _noodler_sat_stub(monkeypatch, tmp_path, witness='"x"')  # 'x' lacks '*': bad fails → D16 rejects
    calls = {"n": 0}

    def _cvc5(*a, **kw):
        calls["n"] += 1
        raise AssertionError("cross-check must NOT run on an invalid witness")

    monkeypatch.setattr(cr, "run_cvc5", _cvc5)
    entry = dict(core.REGISTRY["P1-mutated-star"])
    entry["backend"] = "noodler"
    r = core.run_one("P1-mutated-star", entry)
    assert r["state"] == "witness-unvalidated"
    assert r["not_proven"] is True
    assert r["ok"] is False
    assert r["d16_revalidated"] is False
    assert "d15" not in r and "disagreement" not in r  # D15 never ran
    assert calls["n"] == 0


def test_cli_exit_2_on_disagreement(monkeypatch, tmp_path, capsys):
    """The actual CLI exits 2 when any record has disagreement (D15)."""
    from regexproof.harness import cli

    _noodler_sat_stub(monkeypatch, tmp_path)
    from regexproof.harness import cvc5_runner as cr

    monkeypatch.setattr(cr, "run_cvc5",
                        lambda smt, timeout_ms, **kw:
                        {"verdict": "unsat", "wall_ms": 1.0, "state": "decided",
                         "reason": None})
    # the registry entry must be noodler-backed for the escalation path
    core.REGISTRY["P1-mutated-star"]["backend"] = "noodler"
    try:
        rc = cli.main(["P1-mutated-star"])
    finally:
        core.REGISTRY["P1-mutated-star"]["backend"] = "seq"
    assert rc == 2
