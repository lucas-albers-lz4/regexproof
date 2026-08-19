"""Phase 2–4 corpus-wave gate tests."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_remeasure_script_imports():
    import importlib.util

    path = ROOT / "scripts" / "remeasure-frozen-ids.py"
    spec = importlib.util.spec_from_file_location("remeasure", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    assert hasattr(mod, "measure")


def test_redos_cap_cli_rejected():
    from regexproof.batch import runner

    rc = runner.main(["--corpus", "detect-secrets", "--redos-cap", "5"])
    assert rc == 2


def test_phase2_closeout_exists():
    p = ROOT / "properties" / "generated" / "phase2_toolkit_fix_closeout.md"
    assert p.is_file()
    assert "Hex-escape" in p.read_text(encoding="utf-8") or "hex" in p.read_text(
        encoding="utf-8"
    ).lower()


def test_final_report_exists():
    assert (ROOT / "docs" / "final-report.md").is_file()
