"""Phase 2 pilot smoke: manifests exist, runner + properties exit 0."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_manifests_pinned():
    for name in ("validatorjs", "gitleaks"):
        m = json.loads((ROOT / "pilots" / name / "manifest.json").read_text())
        assert m["commit"]
        assert m["repo_url"]
        assert (ROOT / m["corpus_path"]).exists()


def test_pilot_run_and_properties():
    # Ensure go helper built
    go_dir = ROOT / "helpers" / "go-re2"
    if not (go_dir / "go-re2").is_file():
        subprocess.run(["go", "build", "-o", "go-re2", "."], cwd=go_dir, check=True, shell=False)

    run = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "pilot-run.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert run.returncode == 0, run.stdout + run.stderr
    summary = json.loads((ROOT / "properties/generated/phase2_pilot_summary.json").read_text())
    assert summary["shell_true_violations"] == []
    assert "validatorjs" in summary["pilots"]
    assert "gitleaks" in summary["pilots"]

    props = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "pilot-properties.py"), "--require-ground-truth"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert props.returncode == 0, props.stdout + props.stderr
    results = json.loads(
        (ROOT / "properties/generated/phase2_pilot_properties.json").read_text()
    )
    assert results
    assert all(r.get("result") != "timeout" or not r["ok"] for r in results)
