"""Wave 12 (#581): regexproof newgate cookie-cutter."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

from regexproof.cli import main as dispatcher_main
from regexproof.fuzz.adapters import reject_shell_subprocess_usage
from regexproof.newgate.cli import main as newgate_main
from regexproof.newgate.mirror_expr import mirror_to_py
from regexproof.newgate.scaffold import default_slug, family_ident

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "regexproof" / "newgate"


def test_docs_are_consumer_adoption_not_a_third_funnel():
    newgate = (ROOT / "docs" / "NEWGATE.md").read_text(encoding="utf-8")
    pipeline = (ROOT / "docs" / "PIPELINE.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "docs/NEWGATE.md" in readme
    assert "regexproof.newgate" in readme
    assert "NEWGATE.md" in pipeline
    assert "mine → rank → probe → gate → wave" in pipeline
    assert "not a substitute" in pipeline.lower() or "not a third" in pipeline.lower()
    assert "consumer" in newgate.lower()
    assert "PIPELINE.md" in newgate
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert "regexproof.cli:main" in pyproject


def test_help_exits_zero():
    assert newgate_main(["--help"]) == 0
    assert newgate_main([]) == 0
    assert dispatcher_main(["--help"]) == 0
    assert dispatcher_main(["newgate", "--help"]) == 0


def test_dispatcher_rejects_unknown_command(capsys):
    assert dispatcher_main(["batch"]) == 2
    assert "unknown command" in capsys.readouterr().err


def test_missing_file_fails_closed():
    with pytest.raises(SystemExit, match="not a file"):
        newgate_main(["/no/such/validators.py", r"^[a-z]+$"])


def test_empty_pattern_fails_closed(tmp_path: Path):
    src = tmp_path / "validators.py"
    src.write_text("USERNAME = r'^[a-z]+$'\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="empty pattern"):
        newgate_main([str(src), ""])


def test_unencodable_pattern_fails_closed(tmp_path: Path):
    src = tmp_path / "validators.py"
    src.write_text("pat = r'(?<=x)y'\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="not encodable"):
        newgate_main(["--out", str(tmp_path / "out"), str(src), r"(?<=x)y"])


def test_non_py_re_dialect_fails_closed(tmp_path: Path):
    src = tmp_path / "validators.py"
    src.write_text("pat = r'[a-z]+'\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="py_re"):
        newgate_main(
            ["--dialect", "ecma", "--out", str(tmp_path / "out"), str(src), r"[a-z]+"]
        )


def test_file_colon_pattern_split(tmp_path: Path):
    src = tmp_path / "validators.py"
    src.write_text("USERNAME = r'^[a-z0-9._-]+$'\n", encoding="utf-8")
    out = tmp_path / "gate"
    token = f"{src}:^[a-z0-9._-]+$"
    assert newgate_main(["--out", str(out), "--fuzz-runs", "1", token]) == 0
    assert (out / "gate.py").is_file()
    text = (out / "gate.py").read_text(encoding="utf-8")
    assert "py_re" in text
    assert "mutation_guard" in text
    assert "ALPHABET_CHARS" in text
    assert "InRe(s, ALPHABET)" in text
    assert "shell=True" not in text
    assert (out / "fuzz.py").is_file()
    assert (out / "ci.yml").is_file()
    ci = (out / "ci.yml").read_text(encoding="utf-8")
    assert "regexproof-src" in ci
    assert "REGEXPROOF_ROOT" in ci
    assert "lucas-albers-lz4/regexproof" in ci
    assert "github.workspace" in ci
    assert "ref:" in ci
    assert "pip install" in ci and "-e ./regexproof-src" in ci
    fuzz = (out / "fuzz.py").read_text(encoding="utf-8")
    assert "differential-fuzz.py" in fuzz
    assert "shell=False" in fuzz
    assert "shell=True" not in fuzz.replace("shell=False", "")


def test_out_path_drives_ci_workdir(tmp_path: Path):
    src = tmp_path / "validators.py"
    src.write_text("USERNAME = r'^[a-z]+$'\n", encoding="utf-8")
    # Absolute --out: CI stub falls back to gates/<slug>.
    out_abs = tmp_path / "gates" / "username"
    assert (
        newgate_main(
            [
                "--out",
                str(out_abs),
                "--slug",
                "username",
                "--fuzz-runs",
                "1",
                str(src),
                r"^[a-z]+$",
            ]
        )
        == 0
    )
    ci = (out_abs / "ci.yml").read_text(encoding="utf-8")
    assert "working-directory: gates/username" in ci
    assert "name: regexproof-gate-username" in ci
    assert "ref:" in ci


def test_relative_out_matches_ci_workdir(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    src = Path("validators.py")
    src.write_text("USERNAME = r'^[a-z]+$'\n", encoding="utf-8")
    assert (
        newgate_main(
            [
                "--out",
                "gates/username",
                "--slug",
                "username",
                "--fuzz-runs",
                "1",
                str(src),
                r"^[a-z]+$",
            ]
        )
        == 0
    )
    ci = Path("gates/username/ci.yml").read_text(encoding="utf-8")
    assert "working-directory: gates/username" in ci
    assert "name: regexproof-gate-username" in ci


def test_bad_slug_fails_closed(tmp_path: Path):
    src = tmp_path / "validators.py"
    src.write_text("x = r'[a-z]+'\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="--slug"):
        newgate_main(
            [
                "--slug",
                "bad slug!",
                "--out",
                str(tmp_path / "out"),
                str(src),
                r"[a-z]+",
            ]
        )


def test_exhaust_ge_max_len_fails_closed(tmp_path: Path):
    src = tmp_path / "validators.py"
    src.write_text("x = r'[a-z]+'\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="exhaust-max-len"):
        newgate_main(
            [
                "--out",
                str(tmp_path / "out"),
                "--exhaust-max-len",
                "8",
                "--fuzz-max-len",
                "8",
                str(src),
                r"[a-z]+",
            ]
        )


def test_wide_range_fails_closed(tmp_path: Path):
    src = tmp_path / "validators.py"
    # [\x01-\x81] spans 129 code points with single-char Z3 bounds.
    src.write_text("WIDE = r'^[\\x01-\\x81]+$'\n", encoding="utf-8")
    with pytest.raises(SystemExit, match=r"spans|false UNSAT"):
        newgate_main(
            [
                "--out",
                str(tmp_path / "out"),
                "--fuzz-runs",
                "1",
                str(src),
                r"^[\x01-\x81]+$",
            ]
        )


def test_newline_in_charset_not_false_unsat(tmp_path: Path):
    """Charset that admits ``\\n`` must not emit excludes-newline UNSAT."""
    src = tmp_path / "validators.py"
    src.write_text("NL = r'^[\\n;]+$'\n", encoding="utf-8")
    out = tmp_path / "out"
    assert (
        newgate_main(
            [
                "--out",
                str(out),
                "--fuzz-runs",
                "1",
                "--chars",
                "\n;",
                str(src),
                r"^[\n;]+$",
            ]
        )
        == 0
    )
    text = (out / "gate.py").read_text(encoding="utf-8")
    assert "excludes-newline" not in text


def test_no_forbidden_outside_alphabet_fails_closed():
    from regexproof.newgate.scaffold import pick_forbidden

    alphabet = set(";\x00 |`$\x7f")
    with pytest.raises(SystemExit, match="nothing to prove"):
        pick_forbidden(alphabet, "\x00;")


def test_inexact_mirror_fails_closed(tmp_path: Path):
    src = tmp_path / "validators.py"
    src.write_text(r"WORD = r'^\w+$'" + "\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="mirror_exact"):
        newgate_main(
            [
                "--out",
                str(tmp_path / "out"),
                "--fuzz-runs",
                "1",
                str(src),
                r"^\w+$",
            ]
        )


def test_mutation_sentinel_outside_star_alphabet(tmp_path: Path):
    src = tmp_path / "validators.py"
    src.write_text("GLOB = r'^[a-z*]+$'\n", encoding="utf-8")
    out = tmp_path / "out"
    assert newgate_main(["--out", str(out), "--fuzz-runs", "1", str(src), r"^[a-z*]+$"]) == 0
    text = (out / "gate.py").read_text(encoding="utf-8")
    assert "MUTATION_CH" in text
    assert "MUTATION_CH = '*'" not in text


def test_min_length_quantifier_uses_alphabet_not_full_mirror(tmp_path: Path):
    """`{{8,}}` must not vacuous-pass via InRe(full_mirror) ∧ Length==1."""
    src = tmp_path / "validators.py"
    src.write_text("PIN = r'^[0-9]{8,}$'\n", encoding="utf-8")
    out = tmp_path / "gate"
    rc = newgate_main(
        [
            "--out",
            str(out),
            "--fuzz-runs",
            "1",
            "--chars",
            ";",
            str(src),
            r"^[0-9]{8,}$",
        ]
    )
    assert rc == 0
    gate = out / "gate.py"
    text = gate.read_text(encoding="utf-8")
    assert "ALPHABET_CHARS" in text
    assert "InRe(s, MIRROR)" not in text
    proc = subprocess.run(
        [
            sys.executable,
            str(gate),
            "--all",
            "--require-ground-truth",
            "--require-domain",
            "--fail-on-property-failure",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=60,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "UNSAT" in proc.stdout


def test_no_singleton_alphabet_fails_closed(tmp_path: Path):
    src = tmp_path / "validators.py"
    src.write_text("EMPTY = r'^$'\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="singleton char alphabet"):
        newgate_main(
            ["--out", str(tmp_path / "out"), "--fuzz-runs", "1", str(src), r"^$"]
        )


def test_refuse_overwrite_without_force(tmp_path: Path):
    src = tmp_path / "validators.py"
    src.write_text("x = r'[a-z]+'\n", encoding="utf-8")
    out = tmp_path / "gate"
    args = ["--out", str(out), "--fuzz-runs", "1", str(src), r"[a-z]+"]
    assert newgate_main(args) == 0
    with pytest.raises(SystemExit, match="refusing to overwrite"):
        newgate_main(args)
    assert newgate_main([*args, "--force"]) == 0


def test_no_shell_true_in_newgate_package():
    violations = reject_shell_subprocess_usage([PKG])
    assert violations == [], "\n".join(violations)


def test_slug_and_family_are_stable():
    path = Path("app/validators.py")
    slug = default_slug(path, r"^[a-z]+$")
    assert slug.startswith("validators_")
    fam = family_ident(slug)
    assert fam.startswith("NG_")
    assert fam.replace("_", "").isalnum()


def test_mirror_to_py_roundtrip_charset():
    from regexproof.compiler import compile_pattern
    import z3

    compiled = compile_pattern(
        r"^[a-z0-9._-]+$", flags="", dialect="py_re", call_kind="fullmatch"
    )
    assert compiled.encodable and compiled.mirror is not None
    expr = mirror_to_py(compiled.mirror)
    ns = {
        "Concat": z3.Concat,
        "Union": z3.Union,
        "Range": z3.Range,
        "Re": z3.Re,
        "Star": z3.Star,
        "Plus": z3.Plus,
        "Loop": z3.Loop,
    }
    rebuilt = eval(expr, {"__builtins__": {}}, ns)
    assert isinstance(rebuilt, z3.ReRef)


def test_scaffold_gate_passes_harness(tmp_path: Path):
    src = tmp_path / "validators.py"
    src.write_text("USERNAME = r'^[a-z0-9._-]+$'\n", encoding="utf-8")
    out = tmp_path / "gates" / "username"
    rc = newgate_main(
        [
            "--out",
            str(out),
            "--fuzz-runs",
            "1",
            "--exhaust-max-len",
            "1",
            "--fuzz-max-len",
            "3",
            "--mutations",
            ";",
            "--chars",
            " ;|",
            str(src),
            r"^[a-z0-9._-]+$",
        ]
    )
    assert rc == 0
    gate = out / "gate.py"
    proc = subprocess.run(
        [
            sys.executable,
            str(gate),
            "--all",
            "--require-ground-truth",
            "--require-domain",
            "--fail-on-property-failure",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=60,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "UNSAT" in proc.stdout
    cov = subprocess.run(
        [sys.executable, str(gate), "--check-mutation-coverage"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert cov.returncode == 0, cov.stderr
    fuzz = subprocess.run(
        [sys.executable, str(out / "fuzz.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=90,
        env={**os.environ, "REGEXPROOF_ROOT": str(ROOT)},
    )
    assert fuzz.returncode == 0, fuzz.stdout + fuzz.stderr


def test_module_entry_help():
    proc = subprocess.run(
        [sys.executable, "-m", "regexproof.newgate", "--help"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=20,
    )
    assert proc.returncode == 0, proc.stderr
    assert "FILE PATTERN" in proc.stdout
    probe = subprocess.run(
        [sys.executable, "-m", "regexproof.probe", "--help"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=20,
    )
    assert probe.returncode == 0, probe.stderr
