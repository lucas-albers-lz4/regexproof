"""P1 walker / draft / clone tests (A3–A7)."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest

from regexproof.admission.clone import CloneError, cleanup_clone, partial_clone
from regexproof.admission.constructs import accumulate_constructs, count_constructs
from regexproof.admission.draft import FIELDS_REMAINING, build_draft, emit_draft_text
from regexproof.admission.walk import count_java_pattern_compile, walk_repo
from regexproof.schemas import gate_decision_schema

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "admission"


def test_count_constructs_flags_and_lookarounds():
    c = count_constructs(r"(?x)(?i)foo(?=bar)\K\g{1}\1[[:digit:]]")
    assert c.get("(?x)", 0) >= 1
    assert c.get("(?i)", 0) >= 1
    assert c.get("lookaround", 0) >= 1
    assert c.get("\\K", 0) >= 1
    assert c.get("\\g{", 0) == 1
    assert c.get("backref", 0) == 1  # only \\1 — \\g{ counted separately
    assert c.get("posix-class", 0) >= 1


def test_accumulate_constructs_additive():
    total = accumulate_constructs(["(?x)a", "(?x)(?i)b", "(?i)c"])
    assert total["(?x)"] == 2
    assert total["(?i)"] == 2


def test_ecma_noise_fixture_counts_two_real_literals():
    root = FIXTURES / "ecma_noise"
    walked = walk_repo(root, repo_name="ecma_noise")
    assert walked["regex_sites"] == 2
    assert walked["dialect"].get("ecma") == 2


def test_java_fixture_twenty_two_sites_dialect_agnostic():
    root = FIXTURES / "java_sites"
    text_a = (root / "src/main/java/com/example/A.java").read_text()
    assert len(count_java_pattern_compile(text_a)) == 14
    walked = walk_repo(root, repo_name="java-html-sanitizer")
    assert walked["dialect"] == {"java": 22}
    assert walked["regex_sites"] == 22


def test_build_draft_flagged_not_schema_valid():
    root = FIXTURES / "ecma_noise"
    draft = build_draft(root, pin="abc123", repo_name="ecma_noise")
    assert draft["draft"] is True
    assert draft["fields_remaining"] == FIELDS_REMAINING
    assert draft["probe"]["pin"] == "abc123"
    assert draft["probe"]["security_boundary"] in {
        "deterministic-true",
        "deterministic-false",
        "unknown",
    }
    schema = gate_decision_schema()
    with pytest.raises(Exception):
        __import__("jsonschema").validate(instance=draft, schema=schema)


def test_draft_byte_identical_two_runs():
    root = FIXTURES / "ecma_noise"
    a = emit_draft_text(build_draft(root, pin="deadbeef", repo_name="ecma_noise"))
    b = emit_draft_text(build_draft(root, pin="deadbeef", repo_name="ecma_noise"))
    assert a == b


def test_partial_clone_passes_filter_blob_none(tmp_path: Path):
    calls: list[list[str]] = []

    def fake_run(argv, **kwargs):
        calls.append(list(argv))
        if argv[:2] == ["git", "clone"]:
            dest = Path(argv[-1])
            dest.mkdir(parents=True)
            (dest / "README.md").write_text("hi\n", encoding="utf-8")
            return SimpleNamespace(returncode=0, stdout="", stderr="")
        if argv[:3] == ["git", "-C", str(tmp_path / "repo")] and "checkout" in argv:
            return SimpleNamespace(returncode=0, stdout="", stderr="")
        if "rev-parse" in argv:
            return SimpleNamespace(returncode=0, stdout="abc\n", stderr="")
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    pin = partial_clone(
        "https://example.com/repo.git",
        dest=tmp_path / "repo",
        pin="abc",
        run=fake_run,
    )
    assert pin == "abc"
    assert any("--filter=blob:none" in c for c in calls)
    assert not any("--single-branch" in c for c in calls)
    assert any("fetch" in c and "abc" in c for c in calls)
    cleanup_clone(tmp_path / "repo")
    assert not (tmp_path / "repo").exists()


def test_partial_clone_rejects_batch_corpora(tmp_path: Path):
    bad = tmp_path / "batch" / "corpora" / "x"
    # Make path contain batch/corpora segment after resolve — use symlink structure
    # Simpler: pass a dest whose resolve string includes the forbidden segment.
    dest = ROOT / "batch" / "corpora" / "probe-tmp-should-fail"
    with pytest.raises(CloneError, match="batch/corpora"):
        partial_clone("https://example.com/r.git", dest=dest, pin="x", run=lambda *a, **k: None)


def test_cli_local_path(tmp_path: Path):
    import importlib.util

    out = tmp_path / "draft.json"
    root = FIXTURES / "ecma_noise"
    spec = importlib.util.spec_from_file_location(
        "probe_cli", ROOT / "scripts" / "probe-corpus-admission.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    assert mod._repo_name_from_target("https://github.com/pallets/wtforms.git") == "wtforms"
    assert mod._repo_name_from_target(str(root)) == "ecma_noise"
    rc = mod.main(
        [str(root), "--pin", "localpin", "-o", str(out), "--repo-name", "ecma_noise"]
    )
    assert rc == 0
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["draft"] is True
    assert data["probe"]["regex_sites"] == 2


def test_boundary_path_sample_skips_git(tmp_path: Path):
    from regexproof.admission.draft import build_boundary_signals

    (tmp_path / ".git" / "objects").mkdir(parents=True)
    (tmp_path / ".git" / "objects" / "pack").write_text("x", encoding="utf-8")
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "sanitizer.py").write_text("x", encoding="utf-8")
    sigs = build_boundary_signals(repo_name="x", root=tmp_path)
    assert any("sanitizer" in p for p in sigs.paths)
    assert not any(".git" in p for p in sigs.paths)
