#!/usr/bin/env python3
"""Append measured agent effort and outcomes to the separate autonomous log."""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.mine.autonomous_work import (  # noqa: E402
    AutonomousWorkError,
    LOG_PATH,
    append_run,
)


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key {key!r} in work-items file")
        value[key] = item
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in (
        "run-id", "agent", "model", "cohort-id", "manifest-digest",
        "repo-id", "repository-url", "source-pin", "wave-id",
        "started-at", "completed-at",
    ):
        parser.add_argument(f"--{name}", required=True)
    for name in (
        "reviewed-sites", "contracts-adopted", "proof-questions-attempted",
        "decided-faithful-questions", "unsat-guarantees", "sat-candidates",
        "replayed-witnesses", "reachable-violations", "security-impact-confirmed",
        "local-runnable-gates", "consumer-adopted-gates", "mutation-checks-passed",
        "differential-cases", "third-party-reports-sent", "maintainer-confirmations",
        "third-party-fixes", "human-interventions",
    ):
        parser.add_argument(f"--{name}", type=int, default=0)
    parser.add_argument("--input-tokens", type=int)
    parser.add_argument("--output-tokens", type=int)
    parser.add_argument("--cost-usd", help="decimal string; omit when unknown")
    parser.add_argument("--human-active-minutes", type=float)
    parser.add_argument(
        "--work-items",
        type=Path,
        help="JSON array of reviewed sites and attempted question IDs for this run",
    )
    parser.add_argument(
        "--elapsed-basis",
        choices=("wall_clock", "phase_sum"),
        default="wall_clock",
        help="phase_sum records measured active phases; timestamps bound the observation window",
    )
    parser.add_argument(
        "--elapsed-seconds",
        type=float,
        help="required with phase_sum; otherwise derived from started-at and completed-at",
    )
    parser.add_argument("--log", type=Path, default=LOG_PATH)
    args = parser.parse_args(argv)
    try:
        started = datetime.fromisoformat(args.started_at.replace("Z", "+00:00"))
        completed = datetime.fromisoformat(args.completed_at.replace("Z", "+00:00"))
        if args.elapsed_basis == "phase_sum" and args.elapsed_seconds is None:
            raise ValueError("--elapsed-seconds is required when --elapsed-basis=phase_sum")
        elapsed_seconds = (
            (completed - started).total_seconds()
            if args.elapsed_seconds is None
            else args.elapsed_seconds
        )
        work_items = []
        if args.work_items is not None:
            work_items = json.loads(
                args.work_items.read_text(encoding="utf-8"),
                object_pairs_hook=_unique_object,
            )
            if not isinstance(work_items, list):
                raise ValueError("--work-items must name a JSON array")
        row = {
            "schema_version": "3",
            "measurement_id": str(uuid.uuid4()),
            "policy_version": "autonomous-contracts-v1",
            "run_id": args.run_id,
            "agent": args.agent,
            "model": args.model,
            "cohort_id": args.cohort_id,
            "manifest_digest": args.manifest_digest,
            "repo_id": args.repo_id,
            "repository_url": args.repository_url,
            "source_pin": args.source_pin,
            "wave_id": args.wave_id,
            "started_at": args.started_at,
            "completed_at": args.completed_at,
            "elapsed_seconds": elapsed_seconds,
            "elapsed_basis": args.elapsed_basis,
            "input_tokens": args.input_tokens,
            "output_tokens": args.output_tokens,
            "cost_usd": args.cost_usd,
            "human_active_minutes": args.human_active_minutes,
            "recorded_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "work_items": work_items,
        }
        for name in (
            "reviewed_sites", "contracts_adopted", "proof_questions_attempted",
            "decided_faithful_questions", "unsat_guarantees", "sat_candidates",
            "replayed_witnesses", "reachable_violations", "security_impact_confirmed",
            "local_runnable_gates", "consumer_adopted_gates", "mutation_checks_passed",
            "differential_cases", "third_party_reports_sent", "maintainer_confirmations",
            "third_party_fixes", "human_interventions",
        ):
            row[name.replace("-", "_")] = getattr(args, name.replace("-", "_"))
        saved = append_run(row, args.log)
    except (OSError, AutonomousWorkError, ValueError, OverflowError) as exc:
        print(f"record-autonomous-run: error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(saved, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
