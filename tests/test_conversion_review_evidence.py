"""Frozen top-15 review windows are bound to exact source bytes."""

from __future__ import annotations

import importlib.util
import json
import pathlib
import subprocess

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "build_conversion_review_evidence",
    ROOT / "scripts" / "build-conversion-review-evidence.py",
)
assert SPEC is not None and SPEC.loader is not None
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)
URL = "https://github.com/example/project"
COHORT = "20-r2"


def _git(*args, cwd):
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, capture_output=True, text=True,
        timeout=10,
    ).stdout.strip()


def _fixture(tmp_path, *, ranks=None):
    ranks = range(1, 16) if ranks is None else ranks
    checkout = tmp_path / "checkout"
    source = checkout / "src" / "guard.sh"
    source.parent.mkdir(parents=True)
    source.write_text("\n".join(f"line {i}" for i in range(1, 31)) + "\n")
    _git("init", "-q", cwd=checkout)
    _git("config", "user.email", "test@example.com", cwd=checkout)
    _git("config", "user.name", "Test", cwd=checkout)
    _git("add", "src/guard.sh", cwd=checkout)
    _git("commit", "-q", "-m", "source", cwd=checkout)
    pin = _git("rev-parse", "HEAD", cwd=checkout)
    reviews = tmp_path / "review.ndjson"
    rows = []
    for rank in ranks:
        rows.append({
            "rank": rank,
            "site": f"src/guard.sh:{rank}:TOKEN_{rank}",
            "pattern": "[a-z]+",
            "call_kind": "search",
            "decision": "skipped",
            "reason_code": "out_of_scope",
            "rationale": "The call only parses a local status line.",
            "regex_id": f"regex-{rank}",
            "source_pin": pin,
            "cohort_id": COHORT,
        })
    reviews.write_text("".join(json.dumps(row) + "\n" for row in rows))
    shortlist = tmp_path / "shortlist.json"
    shortlist.write_text(json.dumps({
        "corpus": "project",
        "keep": [
            {
                "site": row["site"],
                "pattern": row["pattern"],
                "call_kind": row["call_kind"],
            }
            for row in rows
        ],
    }) + "\n")
    run_context = tmp_path / "run-context.json"
    run_context.write_text(json.dumps({
        "repository_url": URL,
        "source_pin": pin,
        "cohort_id": COHORT,
    }) + "\n")
    return checkout, pin, reviews, shortlist, run_context


def test_review_builder_authenticates_all_top15_windows(tmp_path):
    checkout, pin, reviews, shortlist, run_context = _fixture(tmp_path)
    evidence = BUILDER.build_evidence(
        reviews_path=reviews,
        shortlist_path=shortlist,
        run_context_path=run_context,
        checkout=checkout,
        repository_url=URL,
        pin=pin,
        cohort_id=COHORT,
    )
    assert evidence["review_source"]["row_count"] == 15
    assert evidence["source_pin"] == pin
    assert len(evidence["source_files"]) == 1
    for candidate in evidence["candidates"]:
        window = candidate["window"]
        assert window["window_lines"] == len(window["lines"])
        assert [line for line in window["lines"] if line["is_target"]] == [
            next(line for line in window["lines"] if line["line"] == candidate["rank"])
        ]
        assert candidate["source_binding"]["pin"] == pin
        assert candidate["source_binding"]["sha256"] == evidence["source_files"][0]["sha256"]


def test_review_builder_rejects_missing_rank_and_dirty_source(tmp_path):
    checkout, pin, reviews, shortlist, run_context = _fixture(
        tmp_path, ranks=range(1, 15)
    )
    with pytest.raises(BUILDER.ReviewEvidenceError, match="complete ranked top-15"):
        BUILDER.build_evidence(
            reviews_path=reviews,
            shortlist_path=shortlist,
            run_context_path=run_context,
            checkout=checkout,
            repository_url=URL,
            pin=pin,
            cohort_id=COHORT,
        )
    checkout, pin, reviews, shortlist, run_context = _fixture(tmp_path / "dirty")
    (checkout / "src" / "guard.sh").write_text("modified after ranking\n")
    with pytest.raises(SystemExit, match="source file bytes differ"):
        BUILDER.build_evidence(
            reviews_path=reviews,
            shortlist_path=shortlist,
            run_context_path=run_context,
            checkout=checkout,
            repository_url=URL,
            pin=pin,
            cohort_id=COHORT,
        )


def test_review_builder_requires_explicit_corpus_path_prefix(tmp_path):
    checkout, pin, reviews, shortlist, run_context = _fixture(tmp_path)
    data = json.loads(shortlist.read_text())
    for row in data["keep"]:
        row["file"] = f"batch/corpora/project/rules/{row['site'].rsplit(':', 2)[0]}"
        path, line, token = row["site"].rsplit(":", 2)
        row["site"] = f"batch/corpora/project/rules/{path}:{line}:{token}"
    shortlist.write_text(json.dumps(data) + "\n")

    evidence = BUILDER.build_evidence(
        reviews_path=reviews,
        shortlist_path=shortlist,
        run_context_path=run_context,
        checkout=checkout,
        repository_url=URL,
        pin=pin,
        cohort_id=COHORT,
        site_path_prefix="batch/corpora/project/rules",
    )
    assert evidence["review_source"]["row_count"] == 15

    with pytest.raises(BUILDER.ReviewEvidenceError, match="does not match"):
        BUILDER.build_evidence(
            reviews_path=reviews,
            shortlist_path=shortlist,
            run_context_path=run_context,
            checkout=checkout,
            repository_url=URL,
            pin=pin,
            cohort_id=COHORT,
        )
