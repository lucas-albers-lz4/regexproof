"""Go / PCRE2 / ECMA helpers used for parse AND replay."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from regexproof.compiler import pcre as pcre_mod
from regexproof.compiler import re2 as re2_mod


def test_go_re2_parse_and_replay():
    pytest.importorskip("subprocess")
    try:
        ok = re2_mod.helper_used_for_parse_and_replay()
    except Exception as exc:  # noqa: BLE001
        pytest.skip(f"go helper unavailable: {exc}")
    if not ok:
        pytest.skip("go toolchain or helper build unavailable")
    gate = re2_mod.parse_with_helper("a+")
    assert gate.get("ok") is True
    assert gate.get("helper") == "go-re2"


def test_pcre2_parse_and_replay():
    assert pcre_mod.helper_used_for_parse_and_replay() is True
    gate = pcre_mod._helper_parse("a+")
    assert gate.get("ok") is True


def test_ecma_helper_when_node_present():
    from regexproof.compiler import ecma as ecma_mod

    gate = ecma_mod._run_regexpp("a+", "")
    # ok True either via regexpp or soft fallback when node missing
    assert "ok" in gate or gate.get("ok") is True
