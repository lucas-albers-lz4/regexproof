"""Unit tests for scripts/dogfood-singleton-analysis.py (P1: scanner fixes +
--dir/--ext/--dry-run/--ndjson probe counter)."""

from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "dogfood_singleton_analysis",
        ROOT / "scripts" / "dogfood-singleton-analysis.py",
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


dsa = _load()


# --- pure-function scanner tests (from the plan) ----------------------------

def test_canon_vars_and_digits():
    assert dsa.canon(r"option syn_flood '1'") == r"option syn_flood '#'"
    assert dsa.canon(r"${index_url}") == "$V"
    assert dsa.canon(r"$_u") == "$V"


def test_sed_search_rejects_numeric_address():
    assert dsa._sed_search("1,20p") is None  # line address, not a regex
    assert dsa._sed_search("s/foo/bar/") == "foo"
    assert dsa._sed_search("s#foo#bar#") == "foo"  # alternate delimiter
    assert dsa._sed_search("/listen_https/d") == "listen_https"


def test_bash_ere_unquoted_only():
    assert dsa.extract_bash_ere("[[ $x =~ ^[0-9]+$ ]]") == ["^[0-9]+$"]
    assert dsa.extract_bash_ere('[[ $x =~ "^[0-9]+$" ]]') == []


def test_fgrep_and_F_are_literal():
    assert dsa.extract_shell_patterns("fgrep 'a.b' f") == []
    assert dsa.extract_shell_patterns("grep -F 'a.b' f") == []
    assert dsa.extract_shell_patterns("grep 'a.b' f") == ["a.b"]


def test_grep_i_maps_to_flags():
    recs = dsa.scan_shell("grep -i 'foo' f", repo="t", file="x.sh")
    assert recs[0]["flags"] == "i"


# --- awk forms ----------------------------------------------------------------

def test_awk_address_and_field_separator_extracted():
    assert dsa.extract_shell_patterns("awk '/listen_https/' f") == ["listen_https"]
    assert dsa.extract_shell_patterns("awk -F'[, ]' '{print $1}'") == ["[, ]"]
    assert dsa.extract_shell_patterns("awk -F '[, ]' '{print $1}'") == ["[, ]"]


def test_awk_program_text_not_extracted():
    assert dsa.extract_shell_patterns("awk '{print $1}' f") == []


# --- filters, flag runs, syntax selector -------------------------------------

def test_empty_pattern_dropped():
    assert dsa.scan_shell("grep '' f", repo="t", file="x.sh") == []
    assert dsa.scan_shell("sed 's//x/' f", repo="t", file="x.sh") == []


def test_length_two_filter():
    assert dsa.extract_shell_patterns("grep 'a' f") == []
    assert dsa.extract_shell_patterns("grep 'ab' f") == ["ab"]


def test_flag_runs():
    recs = dsa.scan_shell("grep -q 'foo' f", repo="t", file="x.sh")
    assert [r["pattern"] for r in recs] == ["foo"]
    assert recs[0]["flags"] == ""
    recs = dsa.scan_shell("grep -i -q 'foo' f", repo="t", file="x.sh")
    assert recs[0]["flags"] == "i"
    recs = dsa.scan_shell("grep -qi 'foo' f", repo="t", file="x.sh")
    assert recs[0]["flags"] == "i"
    # sed -i is in-place editing, NOT case-insensitive — must not set flags
    recs = dsa.scan_shell("sed -i 's/foo/bar/' f", repo="t", file="x.sh")
    assert recs[0]["flags"] == ""


def test_shell_flags_syntax_selector():
    def sf(src):
        recs = dsa.scan_shell(src, repo="t", file="x.sh")
        assert len(recs) == 1, src
        return recs[0]["shell_flags"]

    assert sf("sed 's/foo/bar/' f") == {"syntax": "bre", "grep_mode": "basic"}
    assert sf("grep 'foo' f") == {"syntax": "bre", "grep_mode": "basic"}
    assert sf("grep -E 'foo' f") == {"syntax": "ere", "grep_mode": "extended"}
    assert sf("egrep 'foo' f") == {"syntax": "ere", "grep_mode": "extended"}
    assert sf("awk '/foo/'") == {"syntax": "ere", "grep_mode": None}
    assert sf("[[ $x =~ ^[0-9]+$ ]]") == {"syntax": "bash_ksh", "grep_mode": None}
    # fixed-string greps are literals — no record at all
    assert dsa.scan_shell("grep -F 'a.b' f", repo="t", file="x.sh") == []
    assert dsa.scan_shell("fgrep 'a.b' f", repo="t", file="x.sh") == []


def test_known_bash_ere_sites_have_bash_ksh_provenance():
    # The 3 real sites: setup-hermes.sh (x2, unquoted LHS) and
    # node-bootstrap.sh (quoted LHS, unquoted RHS).
    src = (
        "    if [[ $REPLY =~ ^[Yy]$ ]] || [[ -z $REPLY ]]; then\n"
        "if [[ $REPLY =~ ^[Yy]$ ]] || [[ -z $REPLY ]]; then\n"
        '    [[ "$v" =~ ^[0-9]+$ ]] && echo "$v" || echo 0\n'
    )
    recs = dsa.scan_shell(src, repo="t", file="setup-hermes.sh")
    assert [r["pattern"] for r in recs] == ["^[Yy]$", "^[Yy]$", "^[0-9]+$"]
    assert all(r["shell_flags"] == {"syntax": "bash_ksh", "grep_mode": None}
               for r in recs)
    assert all(r["dialect"] == "posix-shell" for r in recs)
    assert [r["line"] for r in recs] == [1, 2, 3]


def test_var_grep_kept():
    recs = dsa.scan_shell('grep "$pattern" "$file"', repo="t", file="x.sh")
    assert [r["pattern"] for r in recs] == ["$pattern"]


# --- repo walk: --dir surface, --ext, MAX_FILE_BYTES --------------------------

def _write_fixture(root: Path) -> None:
    (root / "etc" / "init.d").mkdir(parents=True)
    (root / "etc" / "init.d" / "firewall").write_text(
        "#!/bin/sh\ngrep -i 'syn_flood' /tmp/x\n", encoding="utf-8")
    (root / "a.sh").write_text(
        "#!/bin/sh\ngrep 'foo' /tmp/x\nsed 's/bar/baz/' /tmp/y\n",
        encoding="utf-8")
    (root / "b.bash").write_text(
        "[[ $x =~ ^[0-9]+$ ]] && echo ok\n", encoding="utf-8")
    (root / "c.init").write_text("egrep 'baz|qux' /tmp/z\n", encoding="utf-8")
    (root / "tool").write_text(
        "#!/usr/bin/env bash\n[[ $REPLY =~ ^[Yy]$ ]] && exit 0\n",
        encoding="utf-8")
    (root / "notes.txt").write_text("grep 'notascript' f\n", encoding="utf-8")
    (root / "x.py").write_text(
        "import re\nre.compile(r'py_pat')\n", encoding="utf-8")


_FIXTURE_COUNTS = {
    "a.sh": 2,
    "b.bash": 1,
    "c.init": 1,
    "etc/init.d/firewall": 1,
    "tool": 1,
    "x.py": 1,
}


def test_dir_mode_shell_surface(tmp_path):
    _write_fixture(tmp_path)
    scan = dsa.extract_repo("t", str(tmp_path), dir_mode=True)
    assert dict(scan.per_file) == _FIXTURE_COUNTS


def test_default_mode_scans_sh_only(tmp_path):
    _write_fixture(tmp_path)
    scan = dsa.extract_repo("t", str(tmp_path), dir_mode=False)
    assert dict(scan.per_file) == {"a.sh": 2, "x.py": 1}


def test_ext_filter(tmp_path):
    _write_fixture(tmp_path)
    scan = dsa.extract_repo("t", str(tmp_path), dir_mode=True, exts={".py"})
    assert [rel for rel, _ in scan.per_file] == ["x.py"]
    scan = dsa.extract_repo("t", str(tmp_path), dir_mode=True, exts={".sh"})
    assert [rel for rel, _ in scan.per_file] == ["a.sh"]
    # normalization: bare names and comma-separated lists work
    assert dsa._norm_exts(["sh", ".py,js"]) == {".sh", ".py", ".js"}
    assert dsa._norm_exts(None) is None


def test_max_file_bytes_guard(tmp_path):
    (tmp_path / "big.sh").write_bytes(b"#" * (dsa.MAX_FILE_BYTES + 1))
    (tmp_path / "small.sh").write_text("grep 'foo' f\n", encoding="utf-8")
    scan = dsa.extract_repo("t", str(tmp_path), dir_mode=True)
    assert scan.oversized_files == 1  # documented skip — file never read
    assert dict(scan.per_file) == {"small.sh": 1}
    assert dsa.MAX_FILE_BYTES == 2_000_000


# --- CLI: --dry-run / --ndjson -------------------------------------------------

def _parse_dry_run(out: str, name: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for line in out.splitlines():
        m = re.match(rf"^{re.escape(name)}:(.+): (\d+)$", line)
        if m:
            counts[m.group(1)] = int(m.group(2))
    return counts


def test_dry_run_per_file_counts(tmp_path, capsys):
    _write_fixture(tmp_path)
    dsa.main(["--dir", str(tmp_path), "--name", "t", "--dry-run"])
    out = capsys.readouterr().out
    assert _parse_dry_run(out, "t") == _FIXTURE_COUNTS
    assert "TOTAL records=7" in out
    assert "oversized_skipped=0" in out
    # dry-run must not write the export
    assert not (tmp_path / dsa.NDJSON_NAME).exists()


def test_ndjson_export_schema_and_counts_match_dry_run(tmp_path, monkeypatch, capsys):
    repo = tmp_path / "repo"
    repo.mkdir()
    _write_fixture(repo)
    monkeypatch.chdir(tmp_path)

    dsa.main(["--dir", str(repo), "--name", "t", "--ndjson"])
    capsys.readouterr()

    lines = (tmp_path / dsa.NDJSON_NAME).read_text(encoding="utf-8").splitlines()
    assert len(lines) == 7  # one NDJSON object per site

    recs = [json.loads(line) for line in lines]
    agg: dict[str, int] = {}
    for rec in recs:
        # EXACT field contract
        assert set(rec) == {"pattern", "flags", "dialect",
                            "shell_flags", "file", "line"}
        assert isinstance(rec["pattern"], str) and rec["pattern"]
        assert isinstance(rec["flags"], str)
        assert isinstance(rec["dialect"], str)
        assert rec["shell_flags"] is None or isinstance(rec["shell_flags"], dict)
        assert isinstance(rec["file"], str)
        assert isinstance(rec["line"], int) and rec["line"] >= 1
        agg[rec["file"]] = agg.get(rec["file"], 0) + 1

    # shell records carry full provenance; project-extractor records null it
    shell = [r for r in recs if r["dialect"] == "posix-shell"]
    assert len(shell) == 6
    assert all(r["shell_flags"]["syntax"] in ("bre", "ere", "bash_ksh")
               for r in shell)
    assert all(r["shell_flags"]["grep_mode"] in ("basic", "extended", "fixed", None)
               for r in shell)
    py = [r for r in recs if r["file"] == "x.py"]
    assert len(py) == 1 and py[0]["shell_flags"] is None

    by_pattern = {r["pattern"]: r for r in recs}
    assert by_pattern["syn_flood"]["flags"] == "i"
    assert by_pattern["baz|qux"]["shell_flags"] == {
        "syntax": "ere", "grep_mode": "extended"}
    assert by_pattern["^[Yy]$"]["shell_flags"] == {
        "syntax": "bash_ksh", "grep_mode": None}
    assert by_pattern["^[0-9]+$"]["shell_flags"] == {
        "syntax": "bash_ksh", "grep_mode": None}

    # per-file aggregation of records matches --dry-run counts
    dsa.main(["--dir", str(repo), "--name", "t", "--dry-run"])
    counts = _parse_dry_run(capsys.readouterr().out, "t")
    assert counts == agg == _FIXTURE_COUNTS


def test_name_requires_dir():
    with pytest.raises(SystemExit):
        dsa.main(["--name", "t"])


# --- snapshot mode (P1 Step 4) ---

def _fixed_records(*, repo: str, file: str) -> list[dict]:
    return [{
        "pattern": "^[0-9]+$", "flags": "", "dialect": "posix-shell",
        "shell_flags": {"syntax": "bash_ksh", "grep_mode": None},
        "file": "a.sh", "line": 2, "extractor": "shell-heuristic",
    }, {
        "pattern": "a+b", "flags": "", "dialect": "posix-shell",
        "shell_flags": {"syntax": "ere", "grep_mode": "extended"},
        "file": "b.sh", "line": 3, "extractor": "shell-heuristic",
    }, {
        "pattern": "a+b", "flags": "", "dialect": "posix-shell",
        "shell_flags": {"syntax": "bre", "grep_mode": "basic"},
        "file": "b.sh", "line": 4, "extractor": "shell-heuristic",
    }]


def test_snapshot_rerun_byte_identical(monkeypatch, tmp_path):
    """AC2: rerun against the same pins is byte-identical (sha256)."""
    monkeypatch.setattr(dsa, "SNAPSHOT_PATH", tmp_path / "snap.json")
    monkeypatch.setattr(dsa, "DOGFOOD", {"t": "/tmp/fakerepo"})
    monkeypatch.setattr(dsa, "_repo_head", lambda path: "a" * 40)
    monkeypatch.setattr(dsa, "extract_repo", lambda name, path: type(
        "S", (), {"records": _fixed_records(repo=name, file="f")})())

    dsa._snapshot()
    first = (tmp_path / "snap.json").read_bytes()
    dsa._snapshot()
    assert (tmp_path / "snap.json").read_bytes() == first

    # BRE a+b and ERE a+b must NOT collapse (shell_flags-aware identity)
    data = json.loads(first)
    assert data["stats"]["global"]["distinct_exact"] == 3
    assert data["site_counts_per_file"]["t"]["b.sh"] == 2  # both a+b records
    assert data["file_lists"]["t"] == ["a.sh", "b.sh"]


def test_snapshot_refuses_on_head_mismatch(monkeypatch, tmp_path):
    """AC2: script refuses to snapshot when a repo HEAD != recorded SHA."""
    snap = tmp_path / "snap.json"
    snap.write_text(json.dumps({"repos": {"t": {"sha": "b" * 40}}}))
    monkeypatch.setattr(dsa, "SNAPSHOT_PATH", snap)
    monkeypatch.setattr(dsa, "DOGFOOD", {"t": "/tmp/fakerepo"})
    monkeypatch.setattr(dsa, "_repo_head", lambda path: "a" * 40)

    with pytest.raises(SystemExit):
        dsa._snapshot()


# --- precision guards (luna gate round 1 folds) ---

def test_command_word_boundary_no_mygrep():
    """'mygrep'/'xsed'/'awkward' must not produce phantom sites."""
    assert dsa.extract_shell_patterns("mygrep 'foo' f") == []
    assert dsa.extract_shell_patterns("xsed 's/a/b/' f") == []
    assert dsa.extract_shell_patterns("echo awk 'x'") == []
    assert dsa.extract_shell_patterns("grep 'foo' f") == ["foo"]


def test_comment_and_string_context_skipped():
    """Matches inside comments or quoted strings are not real sites."""
    assert dsa.extract_shell_patterns("# grep 'foo' f") == []
    assert dsa.extract_shell_patterns('echo "use grep \'foo\' here"') == []
    assert dsa.extract_shell_patterns("echo 'sed s/a/b/ in doc'") == []
    assert dsa.extract_shell_patterns("grep 'foo' # grep 'bar'") == ["foo"]


def test_bash_ere_quoted_rhs_no_partial_capture():
    """A quoted RHS is a literal string match — no partial capture."""
    assert dsa.extract_bash_ere('[[ "$v" =~ "^[0-9]+$" ]]') == []
    assert dsa.extract_bash_ere('[[ $x =~ "pat with spaces" ]]') == []
    # quoted LHS + unquoted RHS still extracts (node-bootstrap form)
    assert dsa.extract_bash_ere('[[ "$v" =~ ^[0-9]+$ ]]') == ["^[0-9]+$"]


def test_main_identity_keeps_bre_ere_distinct(capsys, tmp_path):
    """Normal-path identity must NOT collapse BRE vs ERE a+b."""
    repo = tmp_path / "r"
    repo.mkdir()
    (repo / "a.sh").write_text(
        "grep 'a+b' f\ngrep -E 'a+b' f\n")  # BRE literal vs ERE one-or-more
    dsa.main(["--dir", str(repo), "--name", "t"])
    out = capsys.readouterr().out
    assert "total distinct: 2" in out, out


# --- r2 precision folds (escaped quotes, separators, token boundary) ---

def test_context_guard_escaped_quotes():
    """Escaped quotes inside strings do not leak a phantom quote state."""
    assert dsa.extract_shell_patterns('echo "a\\""; grep \'foo\' f') == ["foo"]
    assert dsa.extract_shell_patterns("echo \\'grep \\'foo\\'\\'") == []


def test_comment_after_separator():
    """`#` after a shell separator starts a comment (echo ok;# grep ...)."""
    assert dsa.extract_shell_patterns("echo ok;# grep 'foo' f") == []
    assert dsa.extract_shell_patterns("grep 'foo' f # real") == ["foo"]


def test_token_boundary_excludes_hyphen():
    """my-grep / my-awk are shell words, not grep invocations."""
    assert dsa.extract_shell_patterns("my-grep 'foo' f") == []
    assert dsa.extract_shell_patterns("my-awk -F'[, ]' f") == []
    assert dsa.extract_shell_patterns("grep 'foo' f") == ["foo"]


def test_bash_ere_partial_quoted_rhs_rejected():
    """RHS starting unquoted but containing a quote is not a regex
    (pre-fold extracted 'foo"bar"' — this test discriminates)."""
    assert dsa.extract_bash_ere('[[ $x =~ foo"bar" ]]') == []
    assert dsa.extract_bash_ere("[[ $x =~ foo'bar' ]]") == []
