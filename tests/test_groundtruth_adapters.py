"""Ground-truth replay adapters (P1 #425 A2) — wrap semantics + batch framing.

docs/SEMANTICS.md call_kind contract: fullmatch = bare whole-string match,
match = prefix-anchored, search = substring; the adapter must reproduce those
semantics on top of helper transports that are bare ``.test()``/``MatchString``
(substring) runners.

P1 rework coverage (luna findings 1-5):
- finding 1: real single-session NUL-framed batch protocol for ecma + py_re
  (round-trips witnesses containing NUL; mixed verdicts; one helper process).
- finding 3: py_re runs in a timed subprocess — catastrophic patterns surface
  as TIMEOUT, never a gate-blocking hang.
- finding 4: absolute-end fullmatch (``\\z`` for perl/pcre/re2, NUL sentinel for
  ecma) — ``a\\n`` is rejected per dialect, a pattern matching ``a\\n`` is
  accepted.
- finding 5: invalid patterns surface as engine-error, not rejected.
"""

from __future__ import annotations

import importlib.util
import shutil
import time
from pathlib import Path

import pytest

from regexproof.groundtruth import adapters
from regexproof.groundtruth.adapters import (
    RefusedNoCallbackError,
    ReplayResult,
    ReplayVerdict,
    Replayability,
    classify_replayability,
    has_adapter,
    replay,
    replay_batch,
    require_replayable,
    skip_reason,
    status_for_claim,
)

ROOT = Path(__file__).resolve().parents[1]


def _node_available() -> bool:
    return shutil.which("node") is not None


def _go_re2_available() -> bool:
    return shutil.which("go") is not None or (
        ROOT / "helpers" / "go-re2" / "go-re2"
    ).is_file()


def _pcre2_available() -> bool:
    if importlib.util.find_spec("pcre2") is not None:
        return True
    return shutil.which("pcre2grep") is not None


def _perl_available() -> bool:
    return shutil.which("perl") is not None


def _yara_available() -> bool:
    return shutil.which("yara") is not None


@pytest.mark.parametrize(
    ("call_kind", "witness", "expected"),
    [
        ("fullmatch", "a", ReplayVerdict.ACCEPTED),
        ("fullmatch", "ba", ReplayVerdict.REJECTED),
        ("match", "abc", ReplayVerdict.ACCEPTED),
        ("match", "ba", ReplayVerdict.REJECTED),
        ("search", "cba", ReplayVerdict.ACCEPTED),
        ("search", "bbb", ReplayVerdict.REJECTED),
    ],
)
def test_py_re_call_kind_semantics(call_kind, witness, expected):
    assert replay("a", "", "py_re", call_kind, witness).verdict is expected


def test_py_re_ignores_flag():
    assert replay("a", "i", "py_re", "fullmatch", "A").verdict is ReplayVerdict.ACCEPTED
    assert replay("a", "", "py_re", "fullmatch", "A").verdict is ReplayVerdict.REJECTED


@pytest.mark.skipif(not _node_available(), reason="node not available")
def test_ecma_fullmatch_vs_search_wrap():
    # helpers/ecma/match.mjs is a bare .test() runner — the adapter emulates
    # fullmatch/match by wrapping the pattern string (SEMANTICS.md).
    assert replay("a", "", "ecma", "fullmatch", "a").verdict is ReplayVerdict.ACCEPTED
    assert replay("a", "", "ecma", "fullmatch", "ba").verdict is ReplayVerdict.REJECTED
    assert replay("a", "", "ecma", "search", "ba").verdict is ReplayVerdict.ACCEPTED
    assert replay("a", "", "ecma", "match", "ba").verdict is ReplayVerdict.REJECTED
    assert replay("a", "", "ecma", "match", "cba").verdict is ReplayVerdict.REJECTED


@pytest.mark.skipif(not _go_re2_available(), reason="go-re2 helper not available")
def test_re2_fullmatch_wrap():
    # go-re2 match = Go MatchString (substring) — fullmatch needs the wrap.
    assert replay("abc", "", "re2", "fullmatch", "abc").verdict is ReplayVerdict.ACCEPTED
    assert replay("abc", "", "re2", "fullmatch", "xabc").verdict is ReplayVerdict.REJECTED
    assert replay("abc", "", "re2", "search", "xabc").verdict is ReplayVerdict.ACCEPTED


@pytest.mark.skipif(not _pcre2_available(), reason="pcre2 helper not available")
def test_pcre_fullmatch_wrap():
    assert replay("a+", "", "pcre", "search", "aaa").verdict is ReplayVerdict.ACCEPTED
    assert replay("a+", "", "pcre", "search", "bbb").verdict is ReplayVerdict.REJECTED
    assert replay("abc", "", "pcre", "fullmatch", "abc").verdict is ReplayVerdict.ACCEPTED
    assert replay("abc", "", "pcre", "fullmatch", "xabc").verdict is ReplayVerdict.REJECTED


@pytest.mark.skipif(not _perl_available(), reason="perl not available")
def test_perl_search_and_fullmatch():
    assert replay("a+", "", "perl", "search", "aaa").verdict is ReplayVerdict.ACCEPTED
    assert replay("a+", "", "perl", "search", "bbb").verdict is ReplayVerdict.REJECTED
    assert replay("abc", "", "perl", "fullmatch", "abc").verdict is ReplayVerdict.ACCEPTED
    assert replay("abc", "", "perl", "fullmatch", "xabc").verdict is ReplayVerdict.REJECTED


@pytest.mark.skipif(not _yara_available(), reason="yara not available")
def test_yara_substring_only():
    assert replay("abc", "", "yara", "search", "xxabcxx").verdict is ReplayVerdict.ACCEPTED
    assert replay("abc", "", "yara", "search", "xxabxx").verdict is ReplayVerdict.REJECTED
    assert replay("abc", "i", "yara", "search", "xxABCxx").verdict is ReplayVerdict.ACCEPTED
    assert replay("abc", "", "yara", "fullmatch", "abc").verdict is ReplayVerdict.NO_ADAPTER


# ---------------------------------------------------------------------------
# finding 1 — single-session NUL-framed batch protocol (ecma + py_re)
# ---------------------------------------------------------------------------
def test_batch_py_re_framing_round_trip():
    """py_re batch: compile once, NUL-framed stdin, per-witness verdicts."""
    witnesses = ["a", "ba", "a\x00b", "", "aa", "\x00", "b\x00a"]
    results = replay_batch("a", "", "py_re", "fullmatch", witnesses)
    assert [r.verdict for r in results] == [
        ReplayVerdict.ACCEPTED,
        ReplayVerdict.REJECTED,
        ReplayVerdict.REJECTED,
        ReplayVerdict.REJECTED,
        ReplayVerdict.REJECTED,
        ReplayVerdict.REJECTED,
        ReplayVerdict.REJECTED,
    ]
    assert len(results) == len(witnesses)
    assert all(isinstance(r, ReplayResult) for r in results)


def test_batch_py_re_mixed_verdicts_aligned_by_index():
    witnesses = ["a", "bb", "a", "a\x00a"]
    results = replay_batch("a", "", "py_re", "fullmatch", witnesses)
    assert [r.verdict for r in results] == [
        ReplayVerdict.ACCEPTED,
        ReplayVerdict.REJECTED,
        ReplayVerdict.ACCEPTED,
        ReplayVerdict.REJECTED,
    ]


@pytest.mark.skipif(not _node_available(), reason="node not available")
def test_batch_ecma_framing_round_trip_nul_and_mixed_verdicts():
    """ecma batch: ONE node subprocess, NUL-escaped witnesses round-trip,
    mixed verdicts come back indexed on the per-witness stdout channel."""
    witnesses = ["a", "b\x00a", "x\x00", "b", "", "a\x00", "\x00a"]
    results = replay_batch("a", "", "ecma", "search", witnesses)
    assert [r.verdict for r in results] == [
        ReplayVerdict.ACCEPTED,  # "a"
        ReplayVerdict.ACCEPTED,  # "b\x00a" contains a
        ReplayVerdict.REJECTED,  # "x\x00"
        ReplayVerdict.REJECTED,  # "b"
        ReplayVerdict.REJECTED,  # ""
        ReplayVerdict.ACCEPTED,  # "a\x00"
        ReplayVerdict.ACCEPTED,  # "\x00a"
    ]


@pytest.mark.skipif(not _node_available(), reason="node not available")
def test_batch_ecma_fullmatch_sentinel_framed():
    """The fullmatch NUL sentinel survives framing; 'a\\n' is rejected."""
    results = replay_batch("a", "", "ecma", "fullmatch", ["a", "a\n", "ba"])
    assert [r.verdict for r in results] == [
        ReplayVerdict.ACCEPTED,
        ReplayVerdict.REJECTED,
        ReplayVerdict.REJECTED,
    ]


def test_batch_empty_witness_list_returns_empty():
    assert replay_batch("a", "", "py_re", "search", []) == []
    assert replay_batch("a", "", "posix-shell", "search", []) == []


def test_batch_ecma_compile_error_broadcast():
    """A batch whose pattern fails to compile broadcasts engine-error."""
    if not _node_available():
        pytest.skip("node not available")
    results = replay_batch("(", "", "ecma", "search", ["a", "b"])
    assert [r.verdict for r in results] == [
        ReplayVerdict.ENGINE_ERROR,
        ReplayVerdict.ENGINE_ERROR,
    ]


# ---------------------------------------------------------------------------
# finding 4 — absolute-end fullmatch for multiline witnesses
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "dialect,skip",
    [
        ("ecma", lambda: not _node_available()),
        ("re2", lambda: not _go_re2_available()),
        ("pcre", lambda: not _pcre2_available()),
        ("perl", lambda: not _perl_available()),
    ],
)
def test_fullmatch_rejects_trailing_newline(dialect, skip):
    """$ matches before a trailing line terminator in Perl/PCRE/ECMA/RE2 — the
    absolute-end wrap (\\z / NUL sentinel) must reject the same 'a\\n' Python
    fullmatch rejects, and accept a pattern that legitimately matches 'a\\n'."""
    if skip():
        pytest.skip(f"{dialect} helper not available")
    assert replay("a", "", dialect, "fullmatch", "a\n").verdict is ReplayVerdict.REJECTED
    assert replay("a\n", "", dialect, "fullmatch", "a\n").verdict is ReplayVerdict.ACCEPTED


@pytest.mark.skipif(not _node_available(), reason="node not available")
def test_ecma_fullmatch_sentinel_witnesses():
    # Sentinel encoding forces end-of-input: witness with a trailing NUL must
    # not be treated as matching, and "a\n\u0000" is rejected too.
    assert replay("a", "", "ecma", "fullmatch", "a\n\x00").verdict is ReplayVerdict.REJECTED
    assert replay("a", "", "ecma", "fullmatch", "a\n").verdict is ReplayVerdict.REJECTED
    assert replay("a", "", "ecma", "fullmatch", "a").verdict is ReplayVerdict.ACCEPTED


def test_py_re_fullmatch_rejects_trailing_newline():
    # Reference: Python re.fullmatch is whole-string — "a\n" rejected.
    assert replay("a", "", "py_re", "fullmatch", "a\n").verdict is ReplayVerdict.REJECTED
    assert replay("a\n", "", "py_re", "fullmatch", "a\n").verdict is ReplayVerdict.ACCEPTED


# ---------------------------------------------------------------------------
# finding 5 — invalid patterns are engine-error, never rejected
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "dialect,skip",
    [
        ("py_re", lambda: False),
        ("ecma", lambda: not _node_available()),
        ("re2", lambda: not _go_re2_available()),
        ("pcre", lambda: not _pcre2_available()),
        ("perl", lambda: not _perl_available()),
        ("yara", lambda: not _yara_available()),
    ],
)
def test_invalid_pattern_is_engine_error_not_rejected(dialect, skip):
    if skip():
        pytest.skip(f"{dialect} helper not available")
    r = replay("(", "", dialect, "search", "x")
    assert r.verdict is ReplayVerdict.ENGINE_ERROR, r
    assert r.ground_truth_status == "failed"


# ---------------------------------------------------------------------------
# finding 3 — py_re runs in a timed subprocess (timeout always honored)
# ---------------------------------------------------------------------------
def test_py_re_catastrophic_pattern_times_out_bounded():
    """A catastrophic pattern must surface as TIMEOUT within the timeout, not
    block the gate (in-process re would run for minutes on this witness)."""
    start = time.monotonic()
    result = replay(r"(a+)+$", "", "py_re", "search", "a" * 30 + "!", timeout_s=1.0)
    elapsed = time.monotonic() - start
    assert result.verdict is ReplayVerdict.TIMEOUT
    assert elapsed < 30


# ---------------------------------------------------------------------------
# finding 2 — classify_replayability + require_replayable (P3's selector seam)
# ---------------------------------------------------------------------------
def test_classify_replayability_matrix():
    assert (
        classify_replayability("py_re", "search") is Replayability.REPLAYABLE
    )
    assert (
        classify_replayability("pcre", "fullmatch") is Replayability.REPLAYABLE
    )
    assert (
        classify_replayability("posix-shell", "search")
        is Replayability.SKIPPED_NO_GT_ADAPTER
    )
    assert (
        classify_replayability("py_re", "substitution")
        is Replayability.SKIPPED_SUBSTITUTION
    )
    # yara fullmatch/match wrap is not expressible — skipped with the note.
    assert (
        classify_replayability("yara", "fullmatch")
        is Replayability.SKIPPED_NO_GT_ADAPTER
    )
    assert (
        classify_replayability("yara", "match")
        is Replayability.SKIPPED_NO_GT_ADAPTER
    )
    assert (
        classify_replayability("yara", "search") is Replayability.REPLAYABLE
    )
    assert (
        classify_replayability("not-a-dialect", "search")
        is Replayability.SKIPPED_NO_GT_ADAPTER
    )


def test_skip_reason_notes_are_descriptive():
    assert "posix-shell" in skip_reason("posix-shell", "search")
    assert "substitution" in skip_reason("py_re", "substitution")
    assert "substring" in skip_reason("yara", "fullmatch")
    assert "not-a-dialect" in skip_reason("not-a-dialect", "search")
    assert skip_reason("py_re", "search") is None


def test_require_replayable_hard_fail_on_refused(monkeypatch):
    """A synthetic handler returning no callback → replay surfaces
    refused-no-callback → require_replayable raises the hard-fail exception."""
    def _no_callback(*args, **kwargs):
        return None

    monkeypatch.setitem(adapters._DISPATCH, "py_re", _no_callback)
    result = replay("a", "", "py_re", "search", "a")
    assert result.verdict is ReplayVerdict.REFUSED_NO_CALLBACK
    assert result.ground_truth_status == "refused-no-callback"
    with pytest.raises(RefusedNoCallbackError):
        require_replayable(result)
    with pytest.raises(RefusedNoCallbackError):
        require_replayable(ReplayVerdict.REFUSED_NO_CALLBACK)


def test_require_replayable_passes_other_verdicts():
    require_replayable(replay("a", "", "py_re", "fullmatch", "a"))
    require_replayable(ReplayVerdict.REJECTED)
    require_replayable(ReplayVerdict.ENGINE_ERROR)
    require_replayable(ReplayVerdict.TIMEOUT)


# ---------------------------------------------------------------------------
# legacy behaviors preserved
# ---------------------------------------------------------------------------
def test_posix_shell_no_adapter():
    r = replay("a", "", "posix-shell", "search", "a")
    assert r.verdict is ReplayVerdict.NO_ADAPTER
    assert r.ground_truth_status == "no-adapter"
    assert has_adapter("posix-shell") is False
    batch = replay_batch("a", "", "posix-shell", "search", ["a", "b"])
    assert [r.verdict for r in batch] == [
        ReplayVerdict.NO_ADAPTER,
        ReplayVerdict.NO_ADAPTER,
    ]


def test_substitution_no_adapter():
    r = replay("a", "", "py_re", "substitution", "a")
    assert r.verdict is ReplayVerdict.NO_ADAPTER
    assert "substitution" in r.detail


def test_handler_returning_none_surfaces_refused(monkeypatch):
    def _no_callback(*args, **kwargs):
        return None

    monkeypatch.setitem(adapters._DISPATCH, "py_re", _no_callback)
    r = replay("a", "", "py_re", "search", "a")
    assert r.verdict is ReplayVerdict.REFUSED_NO_CALLBACK
    assert r.ground_truth_status == "refused-no-callback"


def test_status_for_claim_mapping():
    acc = replay("a", "", "py_re", "fullmatch", "a")
    rej = replay("a", "", "py_re", "fullmatch", "b")
    assert status_for_claim(acc, True) == "reproduced"
    assert status_for_claim(acc, False) == "failed"
    assert status_for_claim(rej, False) == "reproduced"
    assert status_for_claim(rej, True) == "failed"


def test_timeout_outcome_distinct():
    """A hung transport is TIMEOUT, never silently REJECTED."""
    res = adapters._subprocess_verdict(
        ["sleep", "5"], data=None, text=True, timeout_s=0.2
    )
    assert isinstance(res, adapters.ReplayResult)
    assert res.verdict is ReplayVerdict.TIMEOUT
