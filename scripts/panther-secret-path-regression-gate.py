#!/usr/bin/env python3
"""Replay Panther's pinned staged-path filter against synthetic Git files.

This gate checks only the exact local helper and its path policy. It never
invokes the Claude CLI or sends a network request.
"""

from __future__ import annotations

import argparse
import json
import platform
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.groundtruth.panther_claude_review_replay import (  # noqa: E402
    EXCLUDE_PATTERN,
    PIN,
    REPOSITORY,
    run_review_filter,
    source_root,
    verify_checkout,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402

QUESTION_ID = "PA-panther-staged-secrets-file-excluded-from-review-prompt"
MUTATION_ID = "PA-panther-exclusion-mutation-secret-file-pass-through"
CASES = {
    "secrets.py": True,
    "pkg/api_secrets.py": True,
    "credentials.py": True,
    ".env.local.py": True,
    "private.pem.py": True,
    "password.secret.py": False,
    "credentials.json.py": False,
    "normal.py": True,
    "README.md": False,
}


def _git_version() -> str:
    completed = subprocess.run(
        ["git", "--version"], capture_output=True, text=True,
        timeout=10, check=True, shell=False,
    )
    return completed.stdout.strip()


def run(source: Path) -> dict:
    checkout = source.expanduser().resolve()
    source_evidence = verify_checkout(checkout)
    replay = run_review_filter(list(CASES), checkout=checkout)
    rows: dict[str, dict] = {}
    failures: list[str] = []
    reviewable_suffixes = {".py", ".yml", ".yaml", ".sql"}
    for path, expected_selected in CASES.items():
        observation = replay["paths"][path]
        selected = observation["selected_for_review"]
        sentinel_present = observation["sentinel_in_prompt"]
        # Compare the exact Python search matcher with the exact helper result
        # for supported path suffixes; unsupported suffixes are filtered by
        # the helper's independent allowlist before the regex is consulted.
        suffix = Path(path).suffix
        regex_excluded = re.search(EXCLUDE_PATTERN, path) is not None
        model_selected = suffix in reviewable_suffixes and not regex_excluded
        agrees = selected == model_selected
        row = {
            "expected_selected_for_review": expected_selected,
            "selected_for_review": selected,
            "sentinel_in_prompt": sentinel_present,
            "python_regex_excludes_path": regex_excluded,
            "helper_matches_python_regex_and_suffix_model": agrees,
        }
        rows[path] = row
        if selected != expected_selected:
            failures.append(f"{path}: selected={selected}, expected={expected_selected}")
        if selected != sentinel_present:
            failures.append(f"{path}: selection and prompt sentinel disagree")
        if not agrees:
            failures.append(f"{path}: helper disagrees with exact Python regex/suffix model")

    mutated = run_review_filter(
        ["password.secret.py"], checkout=checkout, pattern_override=r"^$"
    )
    mutation_row = mutated["paths"]["password.secret.py"]
    if not (
        mutation_row["selected_for_review"]
        and mutation_row["sentinel_in_prompt"]
    ):
        failures.append("empty-regex mutation did not pass password.secret.py to prompt")

    return {
        "schema_version": "1",
        "gate_id": "panther-precommit-secret-path-review-filter",
        "question_id": QUESTION_ID,
        "mutation_guard_id": MUTATION_ID,
        "repository": REPOSITORY,
        "source_pin": PIN,
        "source_checkout": str(checkout),
        "source_verification": source_evidence,
        "engines": {"python": platform.python_version(), "git": _git_version()},
        "case_count": len(CASES),
        "cases": rows,
        "mutation": {
            "pattern": "^$",
            "path": "password.secret.py",
            "selected_for_review": mutation_row["selected_for_review"],
            "sentinel_in_prompt": mutation_row["sentinel_in_prompt"],
            "claude_invoked": False,
            "network_used": False,
        },
        "claude_invoked": False,
        "network_used": False,
        "failures": failures,
        "result": "pass" if not failures else "fail",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=source_root())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        report = run(args.source_root)
        atomic_write_text(
            args.output,
            json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        )
    except (OSError, ValueError, subprocess.SubprocessError, RuntimeError) as exc:
        print(f"panther-secret-path-regression-gate: error: {exc}", file=sys.stderr)
        return 2
    print(f"{report['result']}: {len(CASES)} pinned-helper path cases; "
          f"mutation={'passed' if report['mutation']['sentinel_in_prompt'] else 'failed'}; "
          f"claude_invoked=false; network_used=false")
    return 0 if report["result"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
