"""Issue #448: bounded retries are failures, never zero-site probe facts."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from regexproof.admission import clone

ROOT = Path(__file__).resolve().parents[1]
URL = "https://github.com/owner/repo.git"


def load_cli():
    spec = importlib.util.spec_from_file_location(
        "probe_448", ROOT / "scripts/probe-corpus-admission.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def phase_of(argv):
    return argv[1] if argv[1] == "clone" else argv[3]


@pytest.mark.parametrize("timeout", [300, 900])
def test_all_git_commands_get_same_explicit_limit(tmp_path, timeout):
    calls = []

    def run(argv, **kwargs):
        calls.append((phase_of(argv), kwargs["timeout"]))
        if phase_of(argv) == "clone":
            Path(argv[-1]).mkdir()
        return SimpleNamespace(returncode=0, stdout="head\n", stderr="")

    kwargs = {} if timeout == 300 else {"timeout_sec": timeout}
    result = clone.partial_clone(URL, dest=tmp_path / "repo", pin="mined", run=run, **kwargs)
    assert calls == [(p, timeout) for p in ["clone", "rev-parse", "fetch", "checkout"]]
    assert result == clone.CloneResult(pin="mined", default_head="head")
    assert (tmp_path / "repo").is_dir()  # Successful materializations persist.


@pytest.mark.parametrize("phase", ["clone", "rev-parse", "fetch", "checkout"])
def test_timeout_preserves_phase_budget_elapsed_and_cause(tmp_path, monkeypatch, phase):
    calls = []
    dest = tmp_path / "repo"
    sibling = tmp_path / "keep"
    sibling.write_text("unrelated")
    clock = iter(range(20))
    monkeypatch.setattr(clone.time, "monotonic", lambda: next(clock))

    def run(argv, **kwargs):
        calls.append(phase_of(argv))
        if calls[-1] == "clone":
            dest.mkdir()
            (dest / "partial-pack").write_text("incomplete clone")
        if calls[-1] == phase:
            raise subprocess.TimeoutExpired(argv, kwargs["timeout"])
        return SimpleNamespace(returncode=0, stdout="head\n", stderr="")

    with pytest.raises(clone.CloneTimeoutError) as err:
        clone.partial_clone(URL, dest=tmp_path / "repo", pin="abc", timeout_sec=900, run=run)
    assert calls[-1] == phase
    assert err.value.phase == phase
    assert err.value.timeout_sec == 900
    assert err.value.elapsed_sec == 1
    assert isinstance(err.value.__cause__, subprocess.TimeoutExpired)
    assert "probe incomplete, not NO-GO" in str(err.value)
    assert not dest.exists()
    assert sibling.read_text() == "unrelated"


@pytest.mark.parametrize(
    "timeout", [0, -1, float("nan"), float("inf"), True, None, "900"]
)
def test_invalid_api_budget_rejected_before_destination_mutation(tmp_path, timeout):
    dest = tmp_path / "repo"
    dest.mkdir()
    marker = dest / "keep"
    marker.write_text("keep")
    with pytest.raises(clone.CloneError, match="finite and positive"):
        clone.partial_clone(URL, dest=dest, timeout_sec=timeout)
    assert marker.read_text() == "keep"


def test_default_runner_enforces_real_subprocess_timeout():
    with pytest.raises(subprocess.TimeoutExpired):
        clone._default_run([sys.executable, "-c", "import time; time.sleep(10)"], timeout=0.05)


@pytest.mark.parametrize("value", ["0", "-1", "nan", "inf", "1.5"])
def test_cli_invalid_budget_is_usage_error(value):
    with pytest.raises(SystemExit) as err:
        load_cli().main([URL, "--pin", "abc", "--clone-timeout-sec", value])
    assert err.value.code == 2


@pytest.mark.parametrize("allow_stale", [False, True])
@pytest.mark.parametrize("override", [False, True])
def test_canonical_cli_timeout_cleans_up_without_draft(
    tmp_path, monkeypatch, capsys, allow_stale, override
):
    from regexproof.probe import cli

    mod = load_cli()
    monkeypatch.setattr(cli, "_load_script", lambda _filename: mod)
    limits = []

    def run(argv, **kwargs):
        limits.append(kwargs["timeout"])
        Path(argv[-1]).mkdir()
        raise subprocess.TimeoutExpired(argv, kwargs["timeout"])

    def partial(url, **kwargs):
        return clone.partial_clone(url, run=run, **kwargs)

    def unexpected_walk(*args, **kwargs):
        pytest.fail("an incomplete clone must not become zero-site facts")

    monkeypatch.setattr(mod, "partial_clone", partial)
    monkeypatch.setattr(mod, "build_draft", unexpected_walk)
    out = tmp_path / "draft.json"
    args = ["--single", URL, "--pin", "abc", "--clone-root", str(tmp_path), "-o", str(out)]
    if allow_stale:
        args += ["--allow-stale-pin"]
    if override:
        args += ["--clone-timeout-sec", "900"]
    assert cli.main(args) == 1
    assert limits == [900 if override else 300]
    assert not out.exists()
    assert not (tmp_path / "repo").exists()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "git clone timed out" in captured.err
    assert "not NO-GO" in captured.err


@pytest.mark.parametrize("phase", ["clone", "rev-parse", "fetch", "checkout"])
def test_materialize_timeout_removes_partial_clone_without_publishing_link(
    tmp_path, monkeypatch, capsys, phase
):
    spec = importlib.util.spec_from_file_location(
        "materialize_448", ROOT / "scripts/materialize-corpus.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    dest = tmp_path / "persistent-clone"
    corpora = tmp_path / "corpora"
    monkeypatch.setattr(mod, "ROOT", tmp_path)
    monkeypatch.setattr(mod, "CORPORA_ROOT", corpora)
    monkeypatch.setattr(mod, "_from_manifest", lambda _: ("test", URL, "abc", {}))
    monkeypatch.setattr(mod, "clone_dest", lambda *_: dest)

    def run(argv, **kwargs):
        current = phase_of(argv)
        if current == "clone":
            dest.mkdir()
            (dest / "partial-pack").write_text("incomplete clone")
        if current == phase:
            raise subprocess.TimeoutExpired(argv, kwargs["timeout"])
        return SimpleNamespace(returncode=0, stdout="head\n", stderr="")

    monkeypatch.setattr(
        mod, "partial_clone", lambda url, **kwargs: clone.partial_clone(url, run=run, **kwargs)
    )
    assert mod.main(["--corpus", "test"]) == 1
    assert not dest.exists()
    assert not corpora.exists()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert f"git {phase} timed out" in captured.err
    assert "increase the per-command cap" in captured.err
    assert "--clone-timeout-sec" not in captured.err


def test_existing_output_untouched_on_timeout(tmp_path, monkeypatch):
    mod = load_cli()
    out = tmp_path / "existing.json"
    out.write_text("previous successful draft")

    def timeout(*args, **kwargs):
        raise clone.CloneTimeoutError("fetch", 300, 300.1)

    monkeypatch.setattr(mod, "partial_clone", timeout)
    assert mod.main([URL, "--pin", "abc", "-o", str(out), "--clone-root", str(tmp_path)]) == 1
    assert out.read_text() == "previous successful draft"
