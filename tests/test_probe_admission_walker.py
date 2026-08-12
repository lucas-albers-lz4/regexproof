"""P1 walker / draft / clone tests (A3–A7)."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest

from regexproof.admission.clone import (
    CloneError,
    cleanup_clone,
    partial_clone,
    validate_clone_url,
)
from regexproof.admission.constructs import accumulate_constructs, count_constructs
from regexproof.admission.draft import FIELDS_REMAINING, build_boundary_signals, build_draft, emit_draft_text
from regexproof.admission.walk import _MAX_FILE_BYTES, count_java_pattern_compile, walk_repo
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
    # Lookaround with 'x'/'i' chars must not count as inline flags
    look = count_constructs(r"(?<=x)(?<!i)(?=i)(?!x)")
    assert look.get("(?x)", 0) == 0
    assert look.get("(?i)", 0) == 0
    assert look.get("lookaround", 0) >= 4


def test_accumulate_constructs_additive():
    total = accumulate_constructs(["(?x)a", "(?x)(?i)b", "(?i)c"])
    assert total["(?x)"] == 2
    assert total["(?i)"] == 2


def test_ecma_noise_fixture_counts_two_real_literals():
    root = FIXTURES / "ecma_noise"
    walked = walk_repo(root, repo_name="ecma_noise")
    assert walked["regex_sites"] == 2
    assert walked["dialect"].get("ecma") == 2


def test_walk_prunes_skip_dirs_and_skips_non_extractor_reads(tmp_path: Path, monkeypatch):
    """Prune node_modules/.git; do not read_text files with no extractor."""
    from regexproof.admission import walk as walk_mod

    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "ok.py").write_text("import re\nre.compile(r'a')\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("# noise\n" * 5000, encoding="utf-8")
    (tmp_path / "node_modules" / "pkg").mkdir(parents=True)
    (tmp_path / "node_modules" / "pkg" / "evil.py").write_text(
        "import re\nre.compile(r'should-not-see')\n", encoding="utf-8"
    )
    (tmp_path / ".git" / "objects").mkdir(parents=True)
    (tmp_path / ".git" / "objects" / "x.py").write_text(
        "import re\nre.compile(r'git-noise')\n", encoding="utf-8"
    )

    reads: list[str] = []
    real_read = Path.read_text

    def tracking_read(self, *args, **kwargs):
        reads.append(str(self))
        return real_read(self, *args, **kwargs)

    monkeypatch.setattr(Path, "read_text", tracking_read)
    walked = walk_mod.walk_repo(tmp_path, repo_name="prune")
    assert walked["regex_sites"] >= 1
    assert all("node_modules" not in p for p in reads)
    assert all("/.git/" not in p and not p.endswith("/.git/objects/x.py") for p in reads)
    assert not any(p.endswith("README.md") for p in reads)
    assert any(p.endswith("ok.py") for p in reads)


def test_java_html_sanitizer_pin_recorded_in_spike():
    from regexproof.admission.java_pin import (
        JAVA_HTML_SANITIZER_PIN,
        JAVA_HTML_SANITIZER_URL,
    )

    assert len(JAVA_HTML_SANITIZER_PIN) == 40
    assert JAVA_HTML_SANITIZER_URL.endswith("java-html-sanitizer")
    spike = (ROOT / "sweep" / "corpus-wave4" / "java-features.md").read_text(
        encoding="utf-8"
    )
    assert JAVA_HTML_SANITIZER_PIN in spike
    assert "pcre" in spike.lower()


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
        "https://github.com/owner/repo.git",
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
        partial_clone(
            "https://github.com/owner/repo.git",
            dest=dest,
            pin="x",
            run=lambda *a, **k: None,
        )


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
    (tmp_path / ".git" / "objects").mkdir(parents=True)
    (tmp_path / ".git" / "objects" / "pack").write_text("x", encoding="utf-8")
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "sanitizer.py").write_text("x", encoding="utf-8")
    sigs = build_boundary_signals(repo_name="x", root=tmp_path)
    assert any("sanitizer" in p for p in sigs.paths)
    assert not any(".git" in p for p in sigs.paths)


def test_readme_symlink_to_passwd_yields_empty_description(tmp_path: Path):
    """Planted README → /etc/passwd must not leak host file contents (#170)."""
    passwd = Path("/etc/passwd")
    if not passwd.is_file():
        pytest.skip("/etc/passwd not available")
    (tmp_path / "README.md").symlink_to(passwd)
    sigs = build_boundary_signals(repo_name="x", root=tmp_path)
    assert sigs.description == ""
    host = passwd.read_text(encoding="utf-8", errors="replace")[:80]
    assert host not in sigs.description


def test_walk_skips_symlink_files(tmp_path: Path):
    """Symlinked sources are ignored before is_file() (#170)."""
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "evil.py").write_text(
        "import re\nre.compile(r'symlink-only-pattern')\n", encoding="utf-8"
    )
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / "ok.py").write_text("# no regex\n", encoding="utf-8")
    (repo / "evil.py").symlink_to(outside / "evil.py")
    walked = walk_repo(repo, repo_name="symlink-probe")
    assert walked["regex_sites"] == 0
    assert walked["extractor_errors"] == 0
    assert _MAX_FILE_BYTES == 2_000_000


def test_walk_counts_extractor_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Extractor exceptions are counted, not silently dropped (#188)."""
    from regexproof.admission import walk as walk_mod

    def boom(_src: str, _rel: str):
        raise RuntimeError("extractor blew up")

    monkeypatch.setattr(walk_mod, "_extractors_for", lambda _fp: [boom])
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / "x.py").write_text("import re\n", encoding="utf-8")
    walked = walk_repo(repo, repo_name="err-probe")
    assert walked["regex_sites"] == 0
    assert walked["extractor_errors"] == 1


def test_boundary_path_sample_skips_symlinks(tmp_path: Path):
    (tmp_path / "real.py").write_text("x", encoding="utf-8")
    (tmp_path / "link.py").symlink_to(tmp_path / "real.py")
    sigs = build_boundary_signals(repo_name="x", root=tmp_path)
    assert "real.py" in sigs.paths
    assert "link.py" not in sigs.paths


@pytest.mark.parametrize(
    "url",
    [
        "file:///tmp/repo.git",
        "ssh://git@github.com/owner/repo.git",
        "https://user:pass@github.com/owner/repo",
        "https://evil.com/owner/repo",
    ],
)
def test_validate_clone_url_rejects_disallowed(url: str):
    with pytest.raises(CloneError):
        validate_clone_url(url)


def test_validate_clone_url_accepts_github_https():
    validate_clone_url("https://github.com/owner/repo")
    validate_clone_url("https://www.github.com/owner/repo.git")
    validate_clone_url("https://GitHub.com/Owner/Repo")


def test_partial_clone_rejects_bad_url_before_run(tmp_path: Path):
    def boom(*_a, **_k):
        raise AssertionError("run must not be called for disallowed URL")

    with pytest.raises(CloneError, match="https"):
        partial_clone(
            "file:///tmp/x.git",
            dest=tmp_path / "repo",
            run=boom,
        )


def test_walk_repo_counts_shell_surface(tmp_path):
    """P2 AC9: the probe path yields non-zero regex_sites for shell files
    (.sh suffix, init.d/ path, extensionless shebang) — the shell dispatch
    in _extractors_for makes the authored gate artifact's shell evidence
    real."""
    (tmp_path / "init.d").mkdir()
    (tmp_path / "init.d" / "start.sh").write_text(
        "grep 'foo' f\n[[ $x =~ ^[0-9]+$ ]]\n", encoding="utf-8")
    (tmp_path / "tool").write_text(
        "#!/bin/sh\ngrep -i 'bar' f\n", encoding="utf-8")
    (tmp_path / "README").write_text("no shebang\n", encoding="utf-8")
    res = walk_repo(tmp_path)
    assert res["regex_sites"] == 3
    assert res["regex_sites_per_file"] == {
        "init.d/start.sh": 2, "tool": 1}
    assert "posix-shell" in res["dialect"]
    assert res["flags"].get("i") == 1


def test_walk_repo_suffix_precedence_over_initd(tmp_path):
    """A .py under init.d/ keeps the python extractor (P1 counter order)."""
    (tmp_path / "init.d").mkdir()
    (tmp_path / "init.d" / "app.py").write_text(
        "import re\nre.search(r'x', 'y')\n", encoding="utf-8")
    res = walk_repo(tmp_path)
    assert res["regex_sites"] == 1
    assert res["dialect"].get("py_re") == 1
    assert "posix-shell" not in res["dialect"]


def test_walk_repo_initd_component_not_substring(tmp_path):
    """P2c luna finding: 'init.d' must match a path COMPONENT, not a
    substring — not-init.d-notes/README is not a shell file."""
    (tmp_path / "not-init.d-notes").mkdir()
    (tmp_path / "not-init.d-notes" / "README").write_text(
        "grep 'phantom' f\n", encoding="utf-8")
    res = walk_repo(tmp_path)
    assert res["regex_sites"] == 0
    assert "posix-shell" not in res["dialect"]
