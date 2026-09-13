"""Tests for the fail-closed PR5 calibration artifact."""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from regexproof.mine import calibration
from regexproof.mine.cohort_manifest import build_manifest


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
