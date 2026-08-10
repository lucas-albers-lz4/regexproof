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
    gate = pcre_mod._helper_parse("a+")
    if gate.get("helper") not in ("pcre2-bindings", "pcre2grep"):
        pytest.skip("real PCRE2 engine not installed (bindings or pcre2grep)")
    assert pcre_mod.helper_used_for_parse_and_replay() is True
    assert gate.get("ok") is True


def test_pcre2_match_refuses_python_re_fallback():
    """Without a real engine, match must exit 2 — never Python re."""
    import subprocess
    import sys
    from pathlib import Path

    helper = Path(__file__).resolve().parents[1] / "helpers" / "pcre2" / "match.py"
    # Force no bindings path by checking the helper's own refusal message when
    # neither engine exists; if an engine exists, skip this negative test.
    if pcre_mod.helper_used_for_parse_and_replay():
        pytest.skip("real PCRE2 present — negative fallback test N/A")
    proc = subprocess.run(
        [sys.executable, str(helper), "match", "a+", ""],
        input="aaa",
        capture_output=True,
        text=True,
        shell=False,
        check=False,
    )
    assert proc.returncode == 2
    assert "refusing Python re" in proc.stderr


def test_ecma_helper_when_node_present():
    from regexproof.compiler import ecma as ecma_mod

    gate = ecma_mod._run_regexpp("a+", "")
    # Fail-closed (#172): missing node → ok False + *-missing helper.
    assert "ok" in gate
    if str(gate.get("helper") or "").endswith("-missing"):
        assert gate.get("ok") is False
    else:
        assert gate.get("ok") is True

