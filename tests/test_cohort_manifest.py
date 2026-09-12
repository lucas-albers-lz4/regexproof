"""Tests for the strict offline frozen-cohort manifest builder."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

from regexproof.mine.cohort_manifest import (
    CohortManifestError,
    build_manifest,
    dumps_manifest,
)

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "cohort-manifest.py"


def _candidate(repo_id: str, **overrides):
    row = {
        "repo_id": repo_id,
        "url": f"https://example.test/{repo_id}",
        "pin": "a" * 40,
        "dialect_family": "py",
        "boundary_family": "validator",
        "score": 1.0,
        "sites": 10,
        "fork": False,
        "duplicate_of": None,
        "partial": False,
    }
    row.update(overrides)
    return row


def _input(*rows):
    return {"candidates": list(rows)}


def test_deterministic_order_and_digest_matches_canonical_content():
    rows = [
        _candidate("z", score=2, dialect_family="js"),
        _candidate("b", score=2, boundary_family="parser"),
        _candidate("a", score=2, boundary_family="parser"),
        _candidate("low", score=1),
    ]
    manifest = build_manifest(_input(*reversed(rows)), "cohort-1", 10)
    assert [row["repo_id"] for row in manifest["repos"]] == ["z", "a", "b", "low"]
    content = {
        key: manifest[key] for key in ("schema_version", "cohort_id", "repos")
    }
    expected = hashlib.sha256(
        json.dumps(content, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert manifest["manifest_digest"] == expected
    assert manifest == build_manifest(_input(*rows), "cohort-1", 10)


def test_excludes_forks_duplicates_and_partial_and_applies_limit():
    manifest = build_manifest(
        _input(
            _candidate("fork", fork=True, score=99),
            _candidate("dupe", duplicate_of="owner/original", score=98),
            _candidate("partial", partial=True, score=97),
            _candidate("one", score=2),
            _candidate("two", score=1),
        ),
        "cohort",
        1,
    )
    assert [row["repo_id"] for row in manifest["repos"]] == ["one"]


def test_duplicate_identity_and_malformed_input_fail_closed():
    with pytest.raises(CohortManifestError, match="duplicate repo_id"):
        build_manifest(_input(_candidate("same"), _candidate("same")), "c", 1)
    with pytest.raises(CohortManifestError, match="duplicate repository attempt"):
        build_manifest(
            _input(
                _candidate("one"),
                _candidate("two", url="https://example.test/one"),
            ),
            "c",
            1,
        )
    for field, value, message in (
        ("pin", "abc", "exactly 40"),
        ("score", float("inf"), "finite"),
        ("sites", 0, "positive"),
        ("fork", "no", "boolean"),
    ):
        row = _candidate("bad", **{field: value})
        with pytest.raises(CohortManifestError, match=message):
            build_manifest(_input(row), "c", 1)


def test_invalid_limit_and_empty_selection_fail():
    with pytest.raises(CohortManifestError, match="positive integer"):
        build_manifest(_input(_candidate("ok")), "c", 0)
    with pytest.raises(CohortManifestError, match="no eligible"):
        build_manifest(_input(_candidate("fork", fork=True)), "c", 1)


def test_cli_writes_readable_manifest_without_changing_input(tmp_path: Path):
    spec = importlib.util.spec_from_file_location("cohort_manifest_script", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    source = tmp_path / "candidates.json"
    output = tmp_path / "manifest.json"
    source_text = json.dumps(_input(_candidate("repo")), indent=2) + "\n"
    source.write_text(source_text, encoding="utf-8")
    assert module.main(
        [str(source), "--cohort-id", "cli", "--limit", "1", "--output", str(output)]
    ) == 0
    assert source.read_text(encoding="utf-8") == source_text
    document = json.loads(output.read_text(encoding="utf-8"))
    assert document["cohort_id"] == "cli"
    assert len(document["repos"]) == 1
    assert dumps_manifest(document) == output.read_text(encoding="utf-8")
