"""#488 skip-vs-CI-fail for pinned helpers."""

from __future__ import annotations

import pytest

from tests.toolchain import PERL_PIN_HINT, _fail_or_skip, in_ci, perl_pin_ok


def test_fail_or_skip_skips_outside_ci(monkeypatch):
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    monkeypatch.delenv("CI", raising=False)
    assert in_ci() is False
    with pytest.raises(pytest.skip.Exception, match="hint"):
        _fail_or_skip("missing hint")


def test_fail_or_skip_fails_in_github_actions(monkeypatch):
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    with pytest.raises(pytest.fail.Exception, match="missing hint"):
        _fail_or_skip("missing hint")


def test_fail_or_skip_fails_when_ci_set(monkeypatch):
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    monkeypatch.setenv("CI", "true")
    with pytest.raises(pytest.fail.Exception, match="missing hint"):
        _fail_or_skip("missing hint")


def test_perl_pin_probe_returns_bool():
    ok, msg = perl_pin_ok()
    assert isinstance(ok, bool)
    if not ok:
        assert "perl" in msg.lower() or PERL_PIN_HINT[:10] in msg
