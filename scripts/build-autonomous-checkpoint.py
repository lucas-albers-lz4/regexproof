#!/usr/bin/env python3
"""Build a v3 checkpoint from a frozen roster, full attempts, and conversion rows."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.mine.conversion_checkpoint import (  # noqa: E402
    ConversionCheckpointError,
    canonical_row_to_checkpoint,
    checkpoint_from_attempts,
)
from regexproof.mine.cohort_manifest import validate_manifest  # noqa: E402


def _records(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        value = [json.loads(line) for line in text.splitlines() if line.strip()]
    if not isinstance(value, list) or any(not isinstance(row, dict) for row in value):
        raise ValueError(f"{path} must contain a JSON array or object NDJSON rows")
    return value


def _identity(row: dict) -> tuple[str, str, str, str, str]:
    return tuple(str(row.get(field) or "") for field in ("repo_id", "url", "pin", "site", "question_id"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cohort", type=Path, required=True)
    parser.add_argument("--roster", type=Path, required=True)
    parser.add_argument("--attempts", type=Path, required=True)
    parser.add_argument("--conversion-rows", type=Path, required=True)
    parser.add_argument("--dispositions", type=Path, help="JSON array keyed by stable identity")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        cohort = validate_manifest(json.loads(args.cohort.read_text(encoding="utf-8")))
        roster = json.loads(args.roster.read_text(encoding="utf-8"))
        attempts = _records(args.attempts)
        conversion_rows = _records(args.conversion_rows)
        raw_dispositions = _records(args.dispositions) if args.dispositions else []
        disposition_by_identity = {}
        for item in raw_dispositions:
            if set(item) != {"repo_id", "url", "pin", "site", "question_id", "disposition"}:
                raise ValueError("disposition rows require identity fields and disposition")
            key = _identity(item)
            if key in disposition_by_identity:
                raise ValueError(f"duplicate disposition identity {key!r}")
            disposition_by_identity[key] = item["disposition"]

        attempt_by_identity = {_identity(item): item for item in attempts}
        result_rows = []
        seen = set()
        for rec in conversion_rows:
            if rec.get("result") not in {"sat", "unsat", "gap"}:
                continue
            qid = rec.get("question_id") or rec.get("name")
            identity = (
                str(rec.get("repo_id") or ""),
                str(rec.get("url") or ""),
                str(rec.get("pin") or ""),
                str(rec.get("site") or ""),
                str(qid or ""),
            )
            # Conversion NDJSON carries corpus/site but source repo URL/pin
            # are bound by the attempt roster; locate by stable question/site.
            matching = [
                key for key in attempt_by_identity
                if key[3:] == identity[3:] and (not identity[0] or key[0] == identity[0])
            ]
            if len(matching) != 1:
                raise ValueError(f"conversion result has no unique attempt identity: {identity!r}")
            key = matching[0]
            if key in seen:
                raise ValueError(f"duplicate conversion result identity: {key!r}")
            seen.add(key)
            canonical = {
                "schema_version": rec.get("schema_version", "1"),
                "site": rec["site"],
                "question_id": qid,
                "contract": rec["contract"],
                "domain": rec["domain"],
                "kind": rec["kind"],
                "synthesized": rec.get("synthesized", False),
                "result": rec["result"],
                "ground_truth_status": rec.get("ground_truth_status"),
                "name": rec.get("name") or qid,
            }
            status = canonical["ground_truth_status"]
            if canonical["result"] == "unsat":
                disposition = disposition_by_identity.get(key, {
                    "status": "not_applicable", "filed_at": None,
                    "resolved_at": None, "approval_escape": None,
                    "approval_ref": None, "reason_code": "unsat_guarantee",
                    "backfilled": False, "disposition_date": None,
                })
            elif status not in {"reproduced", "PASS"}:
                disposition = disposition_by_identity.get(key, {
                    "status": "pending_ground_truth", "filed_at": None,
                    "resolved_at": None, "approval_escape": None,
                    "approval_ref": None, "reason_code": "replay_not_complete",
                    "backfilled": False, "disposition_date": None,
                })
            else:
                if key not in disposition_by_identity:
                    raise ValueError(f"ground-truthed SAT needs an explicit disposition: {key!r}")
                disposition = disposition_by_identity[key]
            attempt = attempt_by_identity[key]
            result_rows.append(
                canonical_row_to_checkpoint(
                    canonical,
                    repo_id=attempt["repo_id"], url=attempt["url"], pin=attempt["pin"],
                    disposition=disposition,
                )
            )
        document = checkpoint_from_attempts(
            attempts,
            result_rows,
            cohort=cohort,
            product_coverage_manifest=roster,
        )
        atomic_write_text(args.out, json.dumps(document, ensure_ascii=True, indent=2, sort_keys=True) + "\n")
    except (OSError, ValueError, KeyError, ConversionCheckpointError) as exc:
        print(f"build-autonomous-checkpoint: error: {exc}", file=sys.stderr)
        return 2
    print(f"checkpoint -> {args.out}: {len(attempts)} attempts, {len(result_rows)} decided rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
