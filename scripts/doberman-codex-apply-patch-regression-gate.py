#!/usr/bin/env python3
"""Replay Doberman's exact pinned Codex apply_patch target extractor."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.groundtruth.doberman_codex_apply_patch_replay import (  # noqa: E402
    PIN,
    QUESTION_IDS,
    REPOSITORY,
    REPO_ID,
    run_regression_gate,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--roster", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        raw_roster = args.roster.read_bytes()
        roster = json.loads(raw_roster)
        identities = {
            row["question_id"]: row
            for row in roster.get("identities", [])
            if isinstance(row, dict) and isinstance(row.get("question_id"), str)
        }
        if set(identities) != set(QUESTION_IDS):
            raise ValueError("frozen roster does not contain exactly both Doberman questions")
        report = run_regression_gate(args.source_root)
        source_sites = {
            QUESTION_IDS[0]: f"{REPO_ID}@{PIN}:src/doberman/hosthooks/codex.py:69:_APPLY_PATCH_FILE_RE",
            QUESTION_IDS[1]: f"{REPO_ID}@{PIN}:src/doberman/hosthooks/codex.py:70:_APPLY_PATCH_MOVE_RE",
        }
        for question_id in QUESTION_IDS:
            identity = identities[question_id]
            if identity.get("contract_sha256") != report["contract_sha256s"][question_id]:
                raise ValueError(f"{question_id}: roster contract hash differs from replay")
            if (
                identity.get("site") != source_sites[question_id]
                or identity.get("repo_id") != REPO_ID
                or identity.get("url") != REPOSITORY
                or identity.get("pin") != PIN
            ):
                raise ValueError(f"{question_id}: roster site differs from exact adopted contract")
        report["cohort"] = {
            "cohort_id": roster["cohort_id"],
            "manifest_digest": roster["cohort_manifest_digest"],
            "roster_sha256": hashlib.sha256(raw_roster).hexdigest(),
        }
        report["result_rows"] = [
            {
                "name": question_id,
                "status": "reproduced",
                "contract_sha256": report["contract_sha256s"][question_id],
                "differential_cases": report["differential_case_counts"][question_id],
            }
            for question_id in QUESTION_IDS
        ]
        atomic_write_text(
            args.output,
            json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        )
        print(
            f"Doberman Codex apply_patch gate: {report['differential_cases']} exact-source cases, "
            f"{len(QUESTION_IDS)} questions, 0 mismatches; weakened Delete mutation replay passed"
        )
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError, KeyError) as exc:
        print(f"Doberman Codex apply_patch gate failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
