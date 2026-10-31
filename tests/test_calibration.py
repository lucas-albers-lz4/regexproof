"""Tests for the fail-closed PR5 calibration artifact."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace

import pytest

from regexproof.mine import calibration
from regexproof.mine.cohort_manifest import build_manifest
from regexproof.mine.conversion_checkpoint import build_report as build_conversion_report

ROOT = Path(__file__).resolve().parents[1]


def _manifest(*repo_ids: str):
    candidates = [
        {
            "repo_id": repo_id,
            "url": f"https://github.com/example/{repo_id}",
            "pin": (str(index + 1) * 40)[:40],
            "dialect_family": "py_re" if index < 2 else "ecma",
            "boundary_family": "validator",
            "score": len(repo_ids) - index,
            "sites": 2,
            "fork": False,
            "duplicate_of": None,
            "partial": False,
        }
        for index, repo_id in enumerate(repo_ids)
    ]
    return build_manifest({"candidates": candidates}, "calibration", len(candidates))


def test_observation_binds_pin_and_counts_canonical_site_novelty(monkeypatch, tmp_path):
    manifest = _manifest("one", "two", "three")

    class FakeDogfood:
        @staticmethod
        def _ident_of(record, *, canon_pat):
            return (record["pattern"], record.get("flags", ""), record["dialect"])

        @staticmethod
        def extract_repo(repo_id, path, *, dir_mode, exts=None):
            records = {
                "one": [{"pattern": "a1", "flags": "", "dialect": "py_re"},
                        {"pattern": "b", "flags": "", "dialect": "py_re"}],
                "two": [{"pattern": "a1", "flags": "", "dialect": "py_re"},
                        {"pattern": "c", "flags": "", "dialect": "py_re"}],
                "three": [{"pattern": "a", "flags": "", "dialect": "ecma"},
                          {"pattern": "b", "flags": "", "dialect": "ecma"}],
            }[repo_id]
            return SimpleNamespace(records=records, oversized_files=0)

    monkeypatch.setattr(calibration, "_dogfood_module", lambda: FakeDogfood)
    pin_by_repo = {repo["repo_id"]: repo["pin"] for repo in manifest["repos"]}
    monkeypatch.setattr(calibration, "_git_head", lambda path: pin_by_repo[path.name])
    paths = {repo_id: tmp_path / repo_id for repo_id in ("one", "two", "three")}
    for path in paths.values():
        path.mkdir()
    # The fake pin resolver uses directory names only to avoid invoking git.
    artifact = calibration.build_observation_artifact(manifest, paths)
    assert artifact["failures"] == []
    assert [row["repo_id"] for row in artifact["observations"]] == [
        row["repo_id"] for row in manifest["repos"]
    ]
    by_id = {row["repo_id"]: row for row in artifact["observations"]}
    assert by_id["one"]["novel_sites"] == 2
    assert by_id["two"]["novel_sites"] == 1
    assert by_id["three"]["novel_sites"] == 2
    closeout = calibration.build_closeout(artifact)
    assert closeout["families"]["ecma"]["status"] == "insufficient_data"
    assert closeout["continue_to_20"] is True


def test_missing_checkout_is_logged_and_cannot_project_to_saturation():
    manifest = _manifest("one", "two")
    artifact = calibration.build_observation_artifact(manifest, {})
    assert len(artifact["failures"]) == 2
    closeout = calibration.build_closeout(artifact)
    assert closeout["decision"] == "inconclusive"
    assert closeout["continue_to_20"] is True
    assert closeout["families"]["py_re"]["status"] == "insufficient_data"
    with pytest.raises(calibration.CalibrationError, match="incomplete"):
        calibration.saturation_envelope(artifact)


def test_extractor_exception_is_recorded_not_silently_counted(monkeypatch, tmp_path):
    manifest = _manifest("one", "two")

    class BrokenDogfood:
        @staticmethod
        def extract_repo(repo_id, path, *, dir_mode, exts=None):
            raise SyntaxError(f"bad source in {repo_id}")

    monkeypatch.setattr(calibration, "_dogfood_module", lambda: BrokenDogfood)
    pin_by_repo = {repo["repo_id"]: repo["pin"] for repo in manifest["repos"]}
    monkeypatch.setattr(calibration, "_git_head", lambda path: pin_by_repo[path.name])
    paths = {repo_id: tmp_path / repo_id for repo_id in ("one", "two")}
    for path in paths.values():
        path.mkdir()
    artifact = calibration.build_observation_artifact(manifest, paths)
    assert {failure["repo_id"] for failure in artifact["failures"]} == {"one", "two"}
    assert artifact["observations"] == []


def test_unsupported_dialect_is_recorded_before_counting_records(monkeypatch, tmp_path):
    manifest = build_manifest(
        {
            "candidates": [
                {
                    "repo_id": "go-repo",
                    "url": "https://github.com/example/go-repo",
                    "pin": "a" * 40,
                    "dialect_family": "go_re",
                    "boundary_family": "validator",
                    "score": 1,
                    "sites": 1,
                    "fork": False,
                    "duplicate_of": None,
                    "partial": False,
                }
            ]
        },
        "calibration",
        1,
    )

    class ShellOnlyDogfood:
        @staticmethod
        def extract_repo(repo_id, path, *, dir_mode, exts=None):
            return SimpleNamespace(
                records=[{"pattern": "[a-z]+", "dialect": "posix-shell"}],
                oversized_files=0,
            )

    monkeypatch.setattr(calibration, "_dogfood_module", lambda: ShellOnlyDogfood)
    monkeypatch.setattr(calibration, "_git_head", lambda path: "a" * 40)
    checkout = tmp_path / "go-repo"
    checkout.mkdir()

    artifact = calibration.build_observation_artifact(
        manifest, {"go-repo": checkout}
    )

    assert artifact["observations"] == []
    assert artifact["failures"] == [
        {
            "repo_id": "go-repo",
            "url": "https://github.com/example/go-repo",
            "pin": "a" * 40,
            "status": "unsupported_dialect",
            "reason": (
                "dialect family 'go_re' requires extractor dialect(s) ['re2'], "
                "but inventory returned ['posix-shell']"
            ),
        }
    ]


def test_mixed_inventory_counts_only_manifest_family(monkeypatch, tmp_path):
    manifest = _manifest("one")

    class MixedDogfood:
        @staticmethod
        def _ident_of(record, *, canon_pat):
            return (record["pattern"], "", record["dialect"])

        @staticmethod
        def extract_repo(repo_id, path, *, dir_mode, exts=None):
            return SimpleNamespace(
                records=[
                    {"pattern": "shell", "dialect": "posix-shell"},
                    {"pattern": "python", "dialect": "py_re"},
                ],
                oversized_files=0,
            )

    monkeypatch.setattr(calibration, "_dogfood_module", lambda: MixedDogfood)
    monkeypatch.setattr(calibration, "_git_head", lambda path: "1" * 40)
    checkout = tmp_path / "one"
    checkout.mkdir()

    artifact = calibration.build_observation_artifact(manifest, {"one": checkout})

    assert artifact["failures"] == []
    assert artifact["observations"][0]["sites"] == 1
    assert artifact["observations"][0]["canonical_ids"] == [["python", "", "py_re"]]


def test_artifact_rejects_reordered_observations(monkeypatch, tmp_path):
    manifest = _manifest("one", "two")

    class FakeDogfood:
        @staticmethod
        def _ident_of(record, *, canon_pat):
            return (record["pattern"], "", "py_re")

        @staticmethod
        def extract_repo(repo_id, path, *, dir_mode, exts=None):
            return SimpleNamespace(
                records=[{"pattern": repo_id, "dialect": "py_re"}],
                oversized_files=0,
            )

    monkeypatch.setattr(calibration, "_dogfood_module", lambda: FakeDogfood)
    monkeypatch.setattr(calibration, "_git_head", lambda path: manifest["repos"][0]["pin"] if path.name == "one" else manifest["repos"][1]["pin"])
    paths = {repo_id: tmp_path / repo_id for repo_id in ("one", "two")}
    for path in paths.values():
        path.mkdir()
    artifact = calibration.build_observation_artifact(manifest, paths)
    artifact["observations"] = list(reversed(artifact["observations"]))
    with pytest.raises(calibration.CalibrationError, match="frozen cohort order"):
        calibration.validate_artifact(artifact)


def test_closeout_binds_and_reports_conversion_checkpoint_separately():
    manifest = _manifest("one", "two")
    artifact = {
        "schema_version": "1",
        "canonicalization_version": calibration.CANONICALIZATION_VERSION,
        "cohort_id": manifest["cohort_id"],
        "manifest_digest": manifest["manifest_digest"],
        "cohort": manifest,
        "observations": [
            {
                "repo_id": repo["repo_id"],
                "url": repo["url"],
                "pin": repo["pin"],
                "dialect_family": repo["dialect_family"],
                "sites": 2,
                "novel_sites": 1,
                "new_reject_buckets": [],
                "canonical_ids": [
                    [repo["repo_id"], "", "py_re"],
                    [repo["repo_id"] + "-second", "", "py_re"],
                ],
                "product_properties": [],
            }
            for repo in manifest["repos"]
        ],
        "failures": [],
    }
    checkpoint = {
        "schema_version": "2",
        "cohort_id": manifest["cohort_id"],
        "manifest_digest": manifest["manifest_digest"],
        "product_coverage_digest": "a" * 64,
        "counts": {
            "asked": 2,
            "sat": 2,
            "ground_truthed": 2,
            "filed": 2,
            "private_first": 2,
            "accepted": 0,
        },
        "disposition_breakdown": {"private_first": 2},
        "reconciliation": {
            "schema_version": "1",
            "result_breakdown": {"sat": 2, "unsat": 0},
            "ground_truth_status_breakdown": {"reproduced": 2},
        "filed_disposition_breakdown": {"private_first": 2},
            "ground_truth_identities": [
                {
                    "repo_id": repo["repo_id"],
                    "url": repo["url"],
                    "pin": repo["pin"],
                    "site": f"{repo['repo_id']}:{index}",
                    "question_id": f"question-{index}",
                    "ground_truth_status": "reproduced",
                }
                for index, repo in enumerate(manifest["repos"])
            ],
        },
    }
    closeout = calibration.build_closeout(artifact, conversion_report=checkpoint)
    conversion = closeout["conversion_checkpoint"]
    assert closeout["conversion_checkpoint_supplied"] is True
    assert closeout["product_denominator"] == 2
    assert closeout["observation_product_denominator"] == 0
    assert conversion["counts"] == checkpoint["counts"]
    assert conversion["disposition_breakdown"] == {"private_first": 2}
    assert conversion["report_sha256"] == calibration.dumps_digest(checkpoint)
    assert closeout["ground_truth_replay"] == {
        "status": "unavailable", "reported_rows": 2, "verified_rows": 0
    }
    assert "Asked: 2; SAT: 2; ground-truthed: 2; filed: 2" in calibration.render_closeout(closeout)
    assert "Replay verification unavailable: 0 verified; 2 reported" in calibration.render_closeout(closeout)

    unknown_disposition = deepcopy(checkpoint)
    unknown_disposition["disposition_breakdown"] = {"totally_fake": 2}
    with pytest.raises(calibration.CalibrationError, match="disposition breakdown is invalid"):
        calibration.build_closeout(artifact, conversion_report=unknown_disposition)

    contradictory_private = deepcopy(checkpoint)
    contradictory_private["counts"]["private_first"] = 0
    with pytest.raises(calibration.CalibrationError, match="private_first count does not match"):
        calibration.build_closeout(
            artifact,
            conversion_report=contradictory_private,
        )
    contradictory_accepted = deepcopy(checkpoint)
    contradictory_accepted["counts"]["accepted"] = 2
    with pytest.raises(calibration.CalibrationError, match="accepted count does not match"):
        calibration.build_closeout(
            artifact,
            conversion_report=contradictory_accepted,
        )


def test_closeout_rejects_conversion_checkpoint_from_another_cohort():
    manifest = _manifest("one", "two")
    artifact = {
        "schema_version": "1",
        "canonicalization_version": calibration.CANONICALIZATION_VERSION,
        "cohort_id": manifest["cohort_id"],
        "manifest_digest": manifest["manifest_digest"],
        "cohort": manifest,
        "observations": [],
        "failures": [],
    }
    checkpoint = {
        "schema_version": "2",
        "cohort_id": "other-cohort",
        "manifest_digest": manifest["manifest_digest"],
        "product_coverage_digest": "a" * 64,
        "counts": {
            "asked": 0,
            "sat": 0,
            "ground_truthed": 0,
            "filed": 0,
            "private_first": 0,
            "accepted": 0,
        },
        "disposition_breakdown": {},
    }
    with pytest.raises(calibration.CalibrationError, match="cohort_id"):
        calibration.build_closeout(artifact, conversion_report=checkpoint)


def test_committed_twenty_repo_closeout_reconciles_conversion_evidence():
    evidence = ROOT / "properties" / "calibration" / "2026-09-12-calibration-20-r2"
    checkpoint = json.loads((evidence / "conversion-checkpoint.json").read_text())
    report = build_conversion_report(checkpoint)
    assert report == json.loads((evidence / "conversion-report.json").read_text())
    assert report["counts"] == {
        "asked": 2,
        "sat": 2,
        "ground_truthed": 2,
        "filed": 2,
        "private_first": 2,
        "accepted": 0,
    }
    assert report["disposition_breakdown"] == {"private_first": 2}

    source_rows = [
        json.loads(line)
        for line in (ROOT / "properties" / "generated" / "Doberman-Core_conversion.ndjson")
        .read_text()
        .splitlines()
        if line.strip()
    ]
    assert [row["canonical"] for row in checkpoint["rows"]] == source_rows
    upstream_rows = [
        json.loads(line)
        for line in (ROOT / "docs" / "conversion-upstream.jsonl").read_text().splitlines()
        if line.strip()
    ]
    upstream_by_key = {
        (row["site"], row["question_id"]): row
        for row in upstream_rows
        if row.get("site") and row.get("question_id")
    }
    for row in checkpoint["rows"]:
        upstream = upstream_by_key[(row["site"], row["question_id"])]
        assert row["disposition"]["status"] == upstream["status"]
        assert row["disposition"]["filed_at"] == upstream["filed_at"]

    observation = json.loads((evidence / "canonical-observations.json").read_text())
    closeout = calibration.build_closeout(observation, conversion_report=report)
    assert closeout == json.loads((evidence / "closeout.json").read_text())
    assert calibration.render_closeout(closeout) == (evidence / "closeout.md").read_text()
