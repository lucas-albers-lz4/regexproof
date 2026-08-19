"""Shape-5 batch admission and search/pad SAT gate (#477)."""

from __future__ import annotations

import json

from regexproof.rule_diff.batch_shape5 import (
    _PAD_GATE_MODEL_CAP,
    admit_shape5_for_batch,
    filter_batch_pairs,
    run_batch_shape5_pairs,
)
from regexproof.rule_diff.search_replay import search_pad_confirms_gap


def test_sibling_family_not_admitted():
    pair = {
        "pair_kind": "sibling_family",
        "provenance": "sibling_family",
        "family_contract": {"R1": "a", "R2": "b", "provenance": "cross_engine"},
    }
    assert admit_shape5_for_batch(pair) is False


def test_version_diff_requires_family_contract():
    pair = {
        "pair_kind": "version_diff",
        "provenance": "version_diff",
        "family_contract": {"R1": "old", "R2": "new", "provenance": "version_diff"},
    }
    assert admit_shape5_for_batch(pair) is True
    pair["family_contract"] = {}
    assert admit_shape5_for_batch(pair) is False


def test_filter_drops_gitleaks_independent_spec():
    pairs = [
        {"provenance": "independent-spec", "family_contract": {"R1": "a", "R2": "b", "provenance": "human"}},
        {
            "provenance": "cross_engine",
            "family_contract": {"R1": "pcre", "R2": "re2", "provenance": "cross_engine"},
        },
    ]
    out = filter_batch_pairs(pairs)
    assert len(out) == 1
    assert out[0]["provenance"] == "cross_engine"


def test_search_pad_confirms_unanchored_gap():
    assert search_pad_confirms_gap(r"^keep-alive", r"keep-alive", "keep-alive")
    assert not search_pad_confirms_gap(r"keep-alive", r"keep-alive", "keep-alive")


def _toy_pair(pair_id: str, r1: str, r2: str, *, pair_kind: str = "version_diff") -> dict:
    return {
        "pair_id": pair_id,
        "pair_kind": pair_kind,
        "provenance": pair_kind,
        "family_contract": {"R1": r1, "R2": r2, "provenance": pair_kind},
        "max_len": 4,
        "r1": {"pattern": r1, "flags": "", "dialect": "py_re"},
        "r2": {"pattern": r2, "flags": "", "dialect": "py_re"},
    }


def test_run_executes_sat_gate_and_skips_independent_spec():
    rows = run_batch_shape5_pairs(
        [
            _toy_pair("toy-sat", "a", "a|b"),
            _toy_pair("toy-unsat", "a|b", "a"),
            {
                **_toy_pair("toy-gitleaks", "a", "a|b", pair_kind="independent-spec"),
                "provenance": "independent-spec",
            },
        ],
        timeout_ms=8000,
    )
    assert {r["pair_id"] for r in rows} == {"toy-sat", "toy-unsat"}
    by_id = {r["pair_id"]: r for r in rows}
    assert by_id["toy-sat"]["result"] == "sat"
    assert by_id["toy-sat"]["search_pad_gate"] is True
    assert by_id["toy-sat"]["ground_truth_status"] == "reproduced"
    assert by_id["toy-sat"]["witness"]["s"]
    assert by_id["toy-unsat"]["result"] == "unsat"


def test_sat_fullmatch_only_when_pad_gate_rejects(monkeypatch):
    from regexproof.rule_diff import batch_shape5 as bs

    monkeypatch.setattr(
        bs,
        "_bounded_gate_sat_witness",
        lambda pair, witness, remaining_ms: False,
    )
    rows = run_batch_shape5_pairs([_toy_pair("toy-fm", "a", "a|b")], timeout_ms=8000)
    assert len(rows) == 1
    assert rows[0]["result"] == "sat_fullmatch_only"
    assert rows[0]["search_pad_gate"] is False
    assert rows[0]["ground_truth_status"] == "fullmatch-only-not-search-gap"


def test_pad_gate_model_cap_exceeds_five():
    assert _PAD_GATE_MODEL_CAP > 5


def test_compile_bound_is_pattern_length_not_witness_max_len():
    long_a = "a" * 20
    pair = _toy_pair("long-pat", long_a, long_a + "|b")
    assert pair["max_len"] == 4
    rows = run_batch_shape5_pairs([pair], timeout_ms=8000)
    assert len(rows) == 1
    assert rows[0]["result"] != "skipped_unencodable"
    assert rows[0]["result"] == "sat"


def test_write_batch_shape5_strips_nondeterministic_witness(tmp_path):
    from regexproof.batch.runner import _write_batch_shape5_artifact

    rows = [
        {
            "pair_id": "a",
            "result": "sat",
            "ground_truth_status": "reproduced",
            "witness": {"s": "volatile"},
        }
    ]
    summary = {"executed": 1, "sat_search_gap": 1}
    _write_batch_shape5_artifact("demo", tmp_path, rows=rows, summary=summary)
    data = json.loads((tmp_path / "demo_batch_shape5.json").read_text(encoding="utf-8"))
    assert data["rows"][0]["witness"] is None
    assert data["rows"][0]["witness_present"] is True
    # In-memory row still has the witness for callers that GT'd already.
    assert rows[0]["witness"] == {"s": "volatile"}


def test_timeout_gate_fails_batch(tmp_path, monkeypatch):
    import pytest

    from regexproof.batch.runner import _run_and_record_shape5

    monkeypatch.setattr(
        "regexproof.rule_diff.batch_shape5.run_batch_shape5_pairs",
        lambda pairs, timeout_ms=30000: [{"pair_id": "hung", "result": "timeout"}],
    )
    with pytest.raises(SystemExit, match="timeout gate"):
        _run_and_record_shape5(
            "gitleaks",
            [_toy_pair("hung", "a", "a|b")],
            tmp_path,
            admitted=1,
            dropped=0,
            note="test",
        )


def test_require_ground_truth_fails_sat_without_gt(tmp_path, monkeypatch):
    import pytest

    from regexproof.batch.runner import _run_and_record_shape5

    monkeypatch.setattr(
        "regexproof.rule_diff.batch_shape5.run_batch_shape5_pairs",
        lambda pairs, timeout_ms=30000: [
            {
                "pair_id": "gap",
                "result": "sat",
                "search_pad_gate": True,
                "ground_truth_status": None,
            }
        ],
    )
    with pytest.raises(SystemExit, match="require-ground-truth"):
        _run_and_record_shape5(
            "coreruleset",
            [_toy_pair("gap", "a", "a|b")],
            tmp_path,
            admitted=1,
            dropped=0,
            note="test",
            require_ground_truth=True,
        )


def test_deadline_exhaustion_fails_closed_to_timeout(monkeypatch):
    """luna r1/r2 (issue #524): a hard wall-clock deadline must not convert an
    un-finished model-enumeration search into a confident sat/sat_fullmatch_only
    result — deadline exhaustion is TIMEOUT / not_proven, which timeout_gate
    then hard-fails. This locks in the fail-closed boundary on _solve_one."""
    from regexproof.rule_diff import batch_shape5 as bs

    pair = _toy_pair("dl", "a", "a|b")
    pair["r1"] = {"pattern": "^a$", "flags": "", "dialect": "py_re"}
    pair["r2"] = {"pattern": "^a+$", "flags": "", "dialect": "py_re"}

    real_monotonic = bs.time.monotonic
    calls = {"n": 0}

    def _fast_deadline_forwards() -> float:
        # First call (deadline = now + 240s) is real; every loop check sees a
        # timestamp far beyond the deadline so the guard trips immediately,
        # before any solver.check() can complete.
        calls["n"] += 1
        if calls["n"] == 1:
            return real_monotonic()
        return real_monotonic() + 100_000.0

    monkeypatch.setattr(bs.time, "monotonic", _fast_deadline_forwards)
    rec = bs._solve_one(pair, timeout_ms=120_000)
    assert rec["result"] == "timeout"
    assert rec.get("not_proven") is True
    # Fail-closed means it must NOT claim a confident sat/sat_fullmatch_only.
    assert rec["result"] not in ("sat", "sat_fullmatch_only")


def test_deadline_clamped_unknown_fails_closed(monkeypatch):
    """luna r4 (issue #524): when the wall-clock deadline shrinks a check's
    timeout below the nominal per-check budget, a resulting `unknown` is a
    deadline-induced timeout — it must fail closed to time not/not_proven, NOT
    be mistaken for a genuine solver-terminal `unknown` (which would keep a
    confident sat_fullmatch_only from a search the deadline cut short)."""
    from regexproof.rule_diff import batch_shape5 as bs

    pair = _toy_pair("dlc", "a", "a|b")
    pair["r1"] = {"pattern": "^a$", "flags": "", "dialect": "py_re"}
    pair["r2"] = {"pattern": "^a+$", "flags": "", "dialect": "py_re"}

    real_monotonic = bs.time.monotonic
    # Deadline is set from the FIRST call (real start). To keep the mock
    # simple, fix the deadline relative to the real start: deadline = start+240s.
    start_real = [real_monotonic()]
    deadline_value = [start_real[0] + 240.0]

    def _clamped_monotonic() -> float:
        # The deadline computation called us first — that call must be the real
        # start so deadline lands at start+240s. Every loop checkpoint then
        # returns ~20s BEFORE the deadline => ~20s remaining (< 120s nominal),
        # so each check is deadline_clamped.
        if calls["n"] == 0:
            calls["n"] += 1
            return start_real[0]
        return deadline_value[0] - 20.0  # 20s remaining (< 120s) -> clamped

    calls = {"n": 0}
    monkeypatch.setattr(bs.time, "monotonic", _clamped_monotonic)

    # Force the first check to complete a witness so `best` is set, then force
    # the ENUMERATION check (with a blocking constraint) to return `unknown`.
    # Under a deadline clamp that unknown must fail closed to timeout.
    class _FakeSolver:
        def __init__(self):
            self.calls = 0
            self.constraints = []
            self.timeout_seen = []

        def set(self, key, value):
            if key == "timeout":
                self.timeout_seen.append(value)
            return None

        def add(self, c):
            self.constraints.append(c)
            return None

        def check(self):
            self.calls += 1
            if self.calls == 1:
                return bs.sat
            return bs.unknown

        def model(self):
            import z3

            class _M:
                def eval(self, a, model_completion=False):
                    return z3.StringVal("a")

            return _M()

    fake = _FakeSolver()
    # _fresh_solver is a closure calling the module-level Solver() constructor;
    # patch Solver so every build returns the fake.
    monkeypatch.setattr(bs, "Solver", lambda: fake)
    # Force the pad-gate to NOT confirm the fake witness, so check 0 establishes
    # a `best` = sat_fullmatch_only; the following clamped `unknown` must then
    # fail closed to timeout rather than keep that confident (but deadline-cut)
    # result.
    monkeypatch.setattr(bs, "_bounded_gate_sat_witness", lambda pair, w, ms: False)
    rec = bs._solve_one(pair, timeout_ms=120_000)
    assert rec["result"] == "timeout", rec
    assert rec.get("not_proven") is True
    # The per-check timeout must never be 0 (Z3 treats 0 as unbounded).
    assert all(t >= 1 for t in fake.timeout_seen), fake.timeout_seen


def test_retry_budget_clamped_to_deadline(monkeypatch):
    """luna r6 (issue #524): the transient first-check retry must recreate the
    solver with the budget clamped to the *remaining* wall-clock deadline, never
    a fresh full timeout_ms that would run past the hard ceiling."""
    from regexproof.rule_diff import batch_shape5 as bs

    pair = _toy_pair("retry", "a", "a|b")
    pair["r1"] = {"pattern": "^a$", "flags": "", "dialect": "py_re"}
    pair["r2"] = {"pattern": "^a+$", "flags": "", "dialect": "py_re"}

    real_monotonic = bs.time.monotonic
    start_real = [real_monotonic()]
    calls = {"n": 0}

    def _monotonic() -> float:
        # 1st call sets deadline=start+240s. Loop checkpoints stay at ~10s
        # before the deadline so every check is clamped; the retry must inherit
        # that clamp, not jump back to the full 120s.
        if calls["n"] == 0:
            calls["n"] += 1
            return start_real[0]
        return start_real[0] + 230.0  # deadline=start+240 -> ~10s remaining

    monkeypatch.setattr(bs.time, "monotonic", _monotonic)

    timeouts = []

    class _FakeSolver:
        def __init__(self):
            self.calls = 0

        def set(self, key, value):
            if key == "timeout":
                timeouts.append(value)
            return None

        def add(self, c):
            return None

        def check(self):
            self.calls += 1
            # retry path: 1st & 2nd checks return unknown (transient), then the
            # retried solver's check also returns unknown -> timeout result.
            return bs.unknown

        def model(self):
            raise AssertionError("unknown never yields a model")

    monkeypatch.setattr(bs, "Solver", lambda: _FakeSolver())
    monkeypatch.setattr(bs, "_bounded_gate_sat_witness", lambda pair, w, ms: False)
    rec = bs._solve_one(pair, timeout_ms=120_000)
    assert rec["result"] == "timeout", rec
    # The very first entry is the initial solver setup (full timeout_ms) before
    # the loop clamps. Every subsequent per-check/retry timeout must be clamped
    # to the ~10s remaining budget, never a fresh full 120s.
    assert timeouts[0] == 120_000, timeouts  # initial setup (nominal)
    assert all(t < 120_000 for t in timeouts[1:]), timeouts
    assert timeouts, "retry should have engaged"



