"""Source-bound counterexample for Panther's pre-commit Claude review filter."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import Contains, Not, Or, String, StringVal, SuffixOf
from regexproof.groundtruth.panther_claude_review_replay import (
    EXCLUDE_PATTERN,
    mutated_exclusion_allows_secret_py,
    secret_path_reaches_prompt,
)
from regexproof.harness.core import prop

PIN = "0cd0f5bd33469c9f03b578fe0104a4ebf23d9f4a"
FAMILY = "PA-panther-claude-review-secret-exclusion"
SITE = f"panther-labs/panther-analysis@{PIN}:.scripts/claude_review.py:21:EXCLUDE_PATTERNS"
QUESTION_ID = "PA-panther-staged-secrets-file-excluded-from-review-prompt"
MUTATION_ID = "PA-panther-exclusion-mutation-secret-file-pass-through"

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-p2-panther-source-review"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))


def _excluded_by_pinned_pattern(path):
    """Mirror Python search for the pinned branches on line-free Git paths.

    The three ``$`` branches are suffix checks; the other three are substring
    checks. The concrete counterexample ``secrets.py`` contains no newline, so
    Python's special ``$``-before-final-newline behavior is outside this query.
    """
    return Or(
        SuffixOf(StringVal(".env"), path),
        SuffixOf(StringVal(".pem"), path),
        SuffixOf(StringVal(".key"), path),
        Contains(path, StringVal("credentials.json")),
        Contains(path, StringVal("secrets.json")),
        Contains(path, StringVal(".secret")),
    )


def _secret_path_replays(witness: dict) -> bool:
    path = witness.get("path", "")
    return path == "secrets.py" and secret_path_reaches_prompt(path)


@prop(
    QUESTION_ID,
    "Counterexample domain: the concrete staged path secrets.py, a reviewable "
    "ASCII Git path containing the literal lower-case substring secrets.",
    expect_unsat=False,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=EXCLUDE_PATTERN,
    ground_truth=_secret_path_replays,
    contract=CONTRACT,
)
def panther_secrets_python_file_reaches_review_prompt():
    path = String("path")
    witness = StringVal("secrets.py")
    return [path == witness], Not(_excluded_by_pinned_pattern(path))


def _mutated_exclusion_replays(witness: dict) -> bool:
    path = witness.get("path", "")
    return path == "password.secret.py" and mutated_exclusion_allows_secret_py(witness)


@prop(
    MUTATION_ID,
    "MUTATION GUARD: replacing the exclusion regex with an empty matcher lets "
    "password.secret.py reach the real staged review-content helper",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=r"^$",
    ground_truth=_mutated_exclusion_replays,
)
def panther_empty_exclusion_mutation_allows_secret_py():
    path = String("path")
    witness = StringVal("password.secret.py")
    return [path == witness], path != StringVal("")


__all__ = ["CONTRACT", "FAMILY", "MUTATION_ID", "PIN", "QUESTION_ID", "SITE"]
