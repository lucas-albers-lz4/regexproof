"""P3 tests: reconcile_probe.py — plan denominator, exit status, tolerance."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _load_cli():
    spec = importlib.util.spec_from_file_location(
        "reconcile_probe_cli",
        ROOT / "scripts" / "reconcile_probe.py",
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_plan_denominator_probe_undercount_fails():
    """|probe - extractor| / probe (plan.md:535): 90 vs 100 = 11.11% — a
    10% tolerance must FAIL (the max() denominator would pass it)."""
    m = _load_cli()
    report, violations = m.reconcile_per_file(
        {"a.sh": 90}, {"a.sh": 100}, tolerance_pct=10.0)
    assert report["a.sh"]["delta_pct"] == 11.11
    assert report["a.sh"]["over"] is True
    assert violations == ["a.sh"]


def test_plan_denominator_within_tolerance_passes():
    m = _load_cli()
    report, violations = m.reconcile_per_file(
        {"a.sh": 95}, {"a.sh": 100}, tolerance_pct=10.0)
    assert report["a.sh"]["delta_pct"] == 5.26
    assert violations == []


def test_probe_zero_registered_nonzero_fails():
    """Probe missed everything in a file the extractor sees: 100% delta."""
    m = _load_cli()
    report, violations = m.reconcile_per_file(
        {}, {"a.sh": 3}, tolerance_pct=10.0)
    assert report["a.sh"]["over"] is True
    assert violations == ["a.sh"]


def test_union_of_files_and_identical_passes():
    m = _load_cli()
    report, violations = m.reconcile_per_file(
        {"a.sh": 5, "b.sh": 2}, {"a.sh": 5, "c.sh": 7}, tolerance_pct=10.0)
    assert set(report) == {"a.sh", "b.sh", "c.sh"}
    assert report["a.sh"]["over"] is False
    assert violations == ["b.sh", "c.sh"]


def test_tolerance_rejects_nan_inf_and_out_of_range():
    m = _load_cli()
    for bad in ("nan", "inf", "-inf", "0", "100.1", "abc"):
        with pytest.raises(SystemExit):
            m.main(["--probe-ndjson", "p.ndjson", "--now-ndjson", "n.ndjson",
                    "--tolerance-pct", bad, "-o", "/tmp/x.json"])


def test_cli_exit_status_and_report_persistence(tmp_path):
    m = _load_cli()
    (tmp_path / "p.ndjson").write_text(
        json.dumps({"pattern": "x", "flags": "", "file": "a.sh", "line": 1})
        + "\n")
    (tmp_path / "n.ndjson").write_text(
        json.dumps({"pattern": "x", "flags": "", "file": "a.sh", "line": 1})
        + "\n" + json.dumps({"pattern": "y", "flags": "", "file": "a.sh",
                             "line": 2}) + "\n")
    # 1 vs 2 = 100% over tolerance -> exit 1, report still written
    rc = m.main(["--probe-ndjson", str(tmp_path / "p.ndjson"),
                 "--now-ndjson", str(tmp_path / "n.ndjson"),
                 "--tolerance-pct", "10", "-o", str(tmp_path / "r.json")])
    assert rc == 1
    report = json.loads((tmp_path / "r.json").read_text())
    assert report["summary"]["over_tolerance_files"] == 1
    # within tolerance -> exit 0
    (tmp_path / "n2.ndjson").write_text(
        json.dumps({"pattern": "x", "flags": "", "file": "a.sh", "line": 1})
        + "\n")
    rc = m.main(["--probe-ndjson", str(tmp_path / "p.ndjson"),
                 "--now-ndjson", str(tmp_path / "n2.ndjson"),
                 "--tolerance-pct", "10", "-o", str(tmp_path / "r2.json")])
    assert rc == 0
