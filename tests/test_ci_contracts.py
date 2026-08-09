"""Phase 6 CI contracts: NDJSON / json-legacy, mutation coverage, toolchain pins."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _load_harness():
    path = ROOT / "scripts" / "z3-verify.py"
    spec = importlib.util.spec_from_file_location("z3_verify_ci", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_mutation_coverage_named_exit():
    harness = _load_harness()
    assert harness.check_mutation_coverage() == 0
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "z3-verify.py"), "--check-mutation-coverage"],
        cwd=ROOT,
        check=False,
    )
    assert proc.returncode == 0


def test_json_and_json_legacy_mutual_exclusion():
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "z3-verify.py"),
            "--json",
            "--json-legacy",
            "P2-actor-whitelist",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 2
    assert "mutually exclusive" in proc.stderr


def test_json_ndjson_and_legacy_identical_results():
    props = ["P2-actor-whitelist", "P1-mutated-star"]
    nd = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "z3-verify.py"), "--json", *props],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert nd.returncode == 0, nd.stderr
    legacy = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "z3-verify.py"), "--json-legacy", *props],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert legacy.returncode == 0, legacy.stderr
    nd_recs = [json.loads(line) for line in nd.stdout.splitlines() if line.strip()]
    leg_recs = json.loads(legacy.stdout)
    assert [r["name"] for r in nd_recs] == [r["name"] for r in leg_recs]
    # Compare facts that matter (ignore wall_ms jitter).
    for a, b in zip(nd_recs, leg_recs, strict=True):
        for key in (
            "schema_version",
            "name",
            "kind",
            "family",
            "result",
            "ok",
            "not_proven",
            "ground_truth",
            "expect_unsat",
        ):
            assert a[key] == b[key], key
        assert a["engine_versions"]["z3"] == b["engine_versions"]["z3"]
        assert a["engine_versions"]["python"] == b["engine_versions"]["python"]


def test_ndjson_records_sorted_and_schema_fields():
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "z3-verify.py"),
            "--json",
            "P1-space",
            "P2-actor-whitelist",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    recs = [json.loads(line) for line in proc.stdout.splitlines() if line.strip()]
    # CLI order preserved; deterministic when using --all (sorted). Partial stream valid.
    assert len(recs) == 2
    for rec in recs:
        assert rec["schema_version"] == "1"
        assert "engine_versions" in rec
        assert "python" in rec["engine_versions"]
        assert "z3" in rec["engine_versions"]
        assert rec["not_proven"] is False
        assert rec["result"] in ("sat", "unsat", "timeout")


def test_all_json_sorted_by_name():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "z3-verify.py"), "--json", "P1-tab", "P1-space"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    # Named CLI keeps caller order; --all sorts. Check --all sorting:
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "z3-verify.py"), "--all", "--json"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    names = [json.loads(line)["name"] for line in proc.stdout.splitlines() if line.strip()]
    assert names == sorted(names)


def test_timeout_surfaces_not_proven():
    harness = _load_harness()
    from z3 import InRe, Length, Re, Star, String

    def fn():
        s = String("s")
        r = Star(Star(Re("a")))
        return [InRe(s, r), Length(s) >= 30], Length(s) == 80

    harness.REGISTRY["CI-timeout-probe"] = {
        "fn": fn,
        "domain": "synthetic",
        "expect_unsat": True,
        "timeout_ms": 1,
        "ground_truth": None,
        "kind": "property",
        "family": "CI-timeout",
        "input_domain": None,
        "call_kind": None,
    }
    try:
        res = harness.run_one("CI-timeout-probe", harness.REGISTRY["CI-timeout-probe"])
    finally:
        harness.REGISTRY.pop("CI-timeout-probe", None)
    if res["result"] == "timeout":
        assert res["not_proven"] is True
        assert res["ok"] is False
    else:
        pytest.skip("solver finished within 1ms; timeout field not exercised")


def test_toolchain_config_loads_and_matrix_aligned():
    import tomllib

    tool = tomllib.loads((ROOT / "ci" / "toolchain.toml").read_text())
    matrix = tomllib.loads((ROOT / "ci" / "python-matrix.toml").read_text())
    assert tool["python"]["minors"] == matrix["minors"]
    assert tool["pcre2"]["status"] == "required"
    assert tool["yara"]["status"] == "required"
    subset = tomllib.loads((ROOT / "ci" / "property-subset.toml").read_text())
    assert subset["families"] == ["P1", "P2", "P3", "P4"]
    assert subset["rule_diff_family"].startswith("RD-")


def test_ci_assert_toolchain_proof_job():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "ci-assert-toolchain.py"), "--job", "proof"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    # Local python may be 3.12 or 3.13; proof pin is 3.13.
    if f"{sys.version_info.major}.{sys.version_info.minor}" != "3.13":
        assert proc.returncode == 1
    else:
        assert proc.returncode == 0, proc.stderr + proc.stdout


def test_property_subset_resolves_names():
    import tomllib

    path = ROOT / "scripts" / "ci-run-property-subset.py"
    spec = importlib.util.spec_from_file_location("ci_run_property_subset", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    cfg = tomllib.loads((ROOT / "ci" / "property-subset.toml").read_text())
    names = mod._subset_property_names(cfg["families"])
    assert any(n.startswith("P1-") for n in names)
    assert any(n.startswith("P2-") for n in names)
    assert "P1-mutated-star" in names
    assert "P5-handle-safe" not in names
