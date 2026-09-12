"""Focused tests for the deterministic cohort saturation report."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from regexproof.mine.saturation import ManifestError, build_report, dumps_report, load_manifest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "saturation-report.py"


def _repo(repo_id: str, family: str, **overrides):
    row = {
        "repo_id": repo_id,
        "dialect_family": family,
        "sites": 100,
        "novel_sites": 2,
        "new_reject_buckets": [],
        "properties_asked": 25,
        "properties_sat": 5,
        "properties_ground_truthed": 4,
        "properties_filed": 2,
        "properties_accepted": 1,
    }
    row.update(overrides)
    return row


def _manifest(*repos):
    return {"schema_version": "1", "repos": list(repos)}


def test_partitions_by_family_and_preserves_trailing_order():
    report = build_report(
        _manifest(
            _repo("py-1", "py", sites=100, novel_sites=1),
            _repo("js-1", "js", sites=100, novel_sites=20),
            _repo("py-2", "py", sites=200, novel_sites=4),
            _repo("py-3", "py", sites=100, novel_sites=2),
            _repo("js-2", "js", sites=100, novel_sites=3),
        )
    )

    assert list(report["families"]) == ["js", "py"]
    assert report["families"]["py"]["repo_ids"] == ["py-1", "py-2", "py-3"]
    assert [row["repo_id"] for row in report["families"]["py"]["trailing_two"]] == [
        "py-2",
        "py-3",
    ]
    assert report["families"]["py"]["trailing_two_novelty_rate"] == "0.02"
    assert report["cohort_totals"]["repo_count"] == 5
    assert report["cohort_totals"]["sites"] == 600
    assert report["cohort_totals"]["novel_sites"] == 30


def test_trailing_window_stop_requires_two_repos_below_strict_threshold_and_no_buckets():
    stopped = build_report(
        _manifest(
            _repo("a", "family", sites=100, novel_sites=2),
            _repo("b", "family", sites=100, novel_sites=2),
        )
    )
    assert stopped["families"]["family"]["compiler_stop"] is True
    assert stopped["compiler_stop"] is True

    at_threshold = build_report(
        _manifest(
            _repo("a", "family", sites=100, novel_sites=2),
            _repo("b", "family", sites=100, novel_sites=3),
        )
    )
    assert at_threshold["families"]["family"]["compiler_stop"] is False

    with_new_bucket = build_report(
        _manifest(
            _repo("a", "family", sites=100, novel_sites=2),
            _repo("b", "family", sites=100, novel_sites=2, new_reject_buckets=["lookbehind"]),
        )
    )
    assert with_new_bucket["families"]["family"]["compiler_stop"] is False


@pytest.mark.parametrize(
    ("bad_row", "message"),
    [
        (_repo("bad", "py", sites=-1), "must be non-negative"),
        (_repo("bad", "py", sites=0), "greater than zero"),
        (_repo("bad", "py", novel_sites=101), "cannot exceed sites"),
        (_repo("bad", "py", properties_asked=1.5), "finite JSON integer"),
        (_repo("bad", "py", new_reject_buckets="none"), "must be a list"),
        (_repo("bad", "py", properties_asked=1, properties_sat=2),
         "properties_sat cannot exceed properties_asked"),
        (_repo("bad", "py", properties_sat=1, properties_ground_truthed=2),
         "properties_ground_truthed cannot exceed properties_sat"),
        (_repo("bad", "py", properties_ground_truthed=1, properties_filed=2),
         "properties_filed cannot exceed properties_ground_truthed"),
        (_repo("bad", "py", properties_filed=1, properties_accepted=2),
         "properties_accepted cannot exceed properties_filed"),
    ],
)
def test_malformed_and_unsafe_observations_fail_closed(bad_row, message):
    with pytest.raises(ManifestError, match=message):
        build_report(_manifest(bad_row))


def test_nonfinite_json_fails_with_clear_error(tmp_path: Path):
    path = tmp_path / "manifest.json"
    path.write_text(
        json.dumps(_manifest(_repo("bad", "py"))).replace("25", "NaN", 1),
        encoding="utf-8",
    )
    with pytest.raises(ManifestError, match="non-finite"):
        load_manifest(path)


def test_denominator_thresholds_are_inclusive_and_use_properties_asked():
    report = build_report(
        _manifest(
            _repo("a", "py", properties_asked=50),
            _repo("b", "py", properties_asked=50),
        )
    )
    assert report["product_denominator"] == 100
    assert report["target_denominator"] == 100
    assert report["product_denominator_met"] is True
    assert report["target_denominator_met"] is True

    below = build_report(_manifest(_repo("a", "py", properties_asked=49)))
    assert below["product_denominator_met"] is False
    assert below["target_denominator_met"] is False


def test_cli_help_documents_schema_and_script_is_read_only(capsys):
    spec = importlib.util.spec_from_file_location("saturation_report", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with pytest.raises(SystemExit) as exc_info:
        module.main(["--help"])
    assert exc_info.value.code == 0
    help_text = capsys.readouterr().out
    assert "dialect_family" in help_text
    assert "properties_asked" in help_text
    assert "never writes" in help_text


def test_serialization_is_deterministic():
    report = build_report(_manifest(_repo("a", "py"), _repo("b", "py")))
    assert dumps_report(report) == dumps_report(report)
    assert "0.02" in dumps_report(report)
