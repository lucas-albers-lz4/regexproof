"""Ground-truth replay adapters (P1 #425 A2) — wrap semantics + batch framing.

docs/SEMANTICS.md call_kind contract: fullmatch = bare whole-string match,
match = prefix-anchored, search = substring; the adapter must reproduce those
semantics on top of helper transports that are bare ``.test()``/``MatchString``
(substring) runners.
"""

from __future__ import annotations

import importlib.util
import shutil
from pathlib import Path

import pytest

from regexproof.groundtruth import adapters
from regexproof.groundtruth.adapters import (
    ReplayVerdict,
    has_adapter,
    replay,
    replay_batch,
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


def test_batch_py_re_framing_round_trip():
    witnesses = ["a", "ba", "a\x00b", "", "aa"]
    results = replay_batch("a", "", "py_re", "fullmatch", witnesses)
    assert [r.verdict for r in results] == [
        ReplayVerdict.ACCEPTED,
        ReplayVerdict.REJECTED,
        ReplayVerdict.REJECTED,
        ReplayVerdict.REJECTED,
        ReplayVerdict.REJECTED,
    ]
    assert len(results) == len(witnesses)
    assert all(isinstance(r, adapters.ReplayResult) for r in results)


@pytest.mark.skipif(not _node_available(), reason="node not available")
def test_batch_ecma_subprocess_nul_safe():
    # NUL witnesses must not corrupt the argv/stdin framing.
    witnesses = ["a", "a\x00b"]
    results = replay_batch("a", "", "ecma", "fullmatch", witnesses)
    assert results[0].verdict is ReplayVerdict.ACCEPTED
    assert results[1].verdict is ReplayVerdict.REJECTED


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
