#!/usr/bin/env python3
"""Replay Inhale's URL-derived file and directory destinations under -o.

All HTTP and URL-opening calls are replaced with synthetic responses. The
gate verifies the exact source pin, compares the helper's filesystem result
with Python's scheme-substitution/path-join model, and runs a real matcher
mutation. It never uses the network.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import platform
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.groundtruth.inhale_directory_replay import (  # noqa: E402
    MUTATED_PATH_PATTERN,
    OUTPUT_PATH_PATTERN,
    PIN,
    REPOSITORY,
    SOURCE_FILE,
    run_directory_root_replay,
    run_file_url_replay,
    source_root,
    verify_checkout,
    widened_file_path_mutation_replays,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402

FILE_QUESTION = "IH-inhale-file-url-output-root-confinement"
DIRECTORY_QUESTION = "IH-inhale-directory-url-output-root-confinement"
MUTATION_ID = "IH-inhale-weakened-url-strip-traversal-mutation"
CASES = {
    "file": {
        FILE_QUESTION: [
            ("https://downloads.example/sample.bin", True),
            ("https://downloads.example/../escape.bin", True),
            ("https://downloads.example/../../escape.bin", False),
        ]
    },
    "directory": {
        DIRECTORY_QUESTION: [
            ("https://downloads.example/sample.bin", True),
            ("https://downloads.example/../directory.bin", True),
            ("https://downloads.example/../../directory.bin", False),
        ]
    },
}


def _git_version() -> str:
    completed = subprocess.run(
        ["git", "--version"], capture_output=True, text=True,
        timeout=10, check=True, shell=False,
    )
    return completed.stdout.strip()


def _mode_replay(mode: str, url: str, checkout: Path) -> dict:
    if mode == "file":
        return run_file_url_replay(url, checkout=checkout)
    with contextlib.redirect_stdout(io.StringIO()):
        return run_directory_root_replay(url, checkout=checkout)


def run(source: Path) -> dict:
    checkout = source.expanduser().resolve()
    source_evidence = verify_checkout(checkout)
    rows: dict[str, dict] = {}
    failures: list[str] = []
    for mode, questions in CASES.items():
        for question_id, values in questions.items():
            question_rows = []
            for url, expected_under_root in values:
                replay = _mode_replay(mode, url, checkout)
                stripped = re.sub(OUTPUT_PATH_PATTERN, "", url.strip().strip("/"))
                output_root = Path(replay["output_root"]).resolve()
                model_path = (output_root / stripped).resolve()
                model_under_root = model_path.is_relative_to(output_root)
                agrees = model_path == Path(replay["resolved_path"]).resolve()
                row = {
                    "url": url,
                    "expected_under_output_root": expected_under_root,
                    "model_resolved_path": str(model_path),
                    "helper_resolved_path": replay["resolved_path"],
                    "model_under_output_root": model_under_root,
                    "helper_under_output_root": replay["under_output_root"],
                    "model_matches_pinned_helper": agrees,
                    "synthetic_content_written": replay["synthetic_content_written"],
                    "under_temporary_root": replay["under_temporary_root"],
                    "network_used": replay["network_used"],
                }
                question_rows.append(row)
                if not agrees:
                    failures.append(f"{question_id}: helper/model path mismatch for {url}")
                if replay["under_output_root"] is not expected_under_root:
                    failures.append(f"{question_id}: unexpected output-root result for {url}")
                if not replay["under_temporary_root"]:
                    failures.append(f"{question_id}: replay wrote outside its temporary fixture")
                if not replay["synthetic_content_written"]:
                    failures.append(f"{question_id}: synthetic bytes did not reach the target for {url}")
                if replay["network_used"]:
                    failures.append(f"{question_id}: replay reported network use")
            rows[question_id] = {
                "mode": mode,
                "case_count": len(question_rows),
                "cases": question_rows,
                "candidate_reproduced": any(
                    not row["helper_under_output_root"] for row in question_rows
                ),
            }

    mutation_url = "https://downloads.example/../escape.bin"
    baseline = run_file_url_replay(mutation_url, checkout=checkout)
    mutated = run_file_url_replay(
        mutation_url, checkout=checkout, pattern_override=MUTATED_PATH_PATTERN
    )
    mutation_passed = bool(
        baseline["under_output_root"]
        and mutated["under_temporary_root"]
        and not mutated["under_output_root"]
        and mutated["synthetic_content_written"]
        and widened_file_path_mutation_replays()
    )
    if not mutation_passed:
        failures.append("widened URL-strip regex mutation did not reproduce the expected escape")

    return {
        "schema_version": "1",
        "gate_id": "inhale-url-output-path-confinement",
        "question_ids": [FILE_QUESTION, DIRECTORY_QUESTION],
        "mutation_guard_id": MUTATION_ID,
        "repository": REPOSITORY,
        "source_pin": PIN,
        "source_checkout": str(checkout),
        "source_verification": source_evidence,
        "source_file": SOURCE_FILE,
        "source_pattern": OUTPUT_PATH_PATTERN,
        "engines": {"python": platform.python_version(), "git": _git_version()},
        "case_count": sum(row["case_count"] for row in rows.values()),
        "question_case_counts": {
            question_id: row["case_count"] for question_id, row in rows.items()
        },
        "questions": rows,
        "mutation": {
            "url": mutation_url,
            "pattern": MUTATED_PATH_PATTERN,
            "baseline_under_output_root": baseline["under_output_root"],
            "mutated_under_output_root": mutated["under_output_root"],
            "mutated_under_temporary_root": mutated["under_temporary_root"],
            "synthetic_content_written": mutated["synthetic_content_written"],
            "ground_truth_reproduced": mutation_passed,
            "network_used": False,
        },
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
        print(f"inhale-output-path-regression-gate: error: {exc}", file=sys.stderr)
        return 2
    print(
        f"{report['result']}: {report['case_count']} exact-helper URL path cases; "
        f"mutation={'passed' if report['mutation']['ground_truth_reproduced'] else 'failed'}; "
        "network_used=false"
    )
    return 0 if report["result"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
