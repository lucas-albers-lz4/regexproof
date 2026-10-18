"""Append-only run, resource, useful-gate, and downstream-outcome metrics."""

from __future__ import annotations

import fcntl
import json
import math
import pathlib
import re
from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any

from regexproof.contract_adoption import POLICY_VERSION

LOG_PATH = (
    pathlib.Path(__file__).resolve().parents[2]
    / "properties"
    / "generated"
    / "autonomous_work.jsonl"
)
PIN_RE = re.compile(r"^[0-9a-f]{40}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
RUN_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
COUNT_FIELDS = (
    "reviewed_sites",
    "contracts_adopted",
    "proof_questions_attempted",
    "decided_faithful_questions",
    "unsat_guarantees",
    "sat_candidates",
    "replayed_witnesses",
    "reachable_violations",
    "security_impact_confirmed",
    "local_runnable_gates",
    "consumer_adopted_gates",
    "mutation_checks_passed",
    "differential_cases",
    "third_party_reports_sent",
    "maintainer_confirmations",
    "third_party_fixes",
    "human_interventions",
)
RUN_FIELDS_V1 = {
    "schema_version", "measurement_id", "policy_version", "run_id", "agent",
    "model", "cohort_id", "manifest_digest", "repo_id", "repository_url",
    "source_pin", "wave_id", "started_at", "completed_at", "elapsed_seconds",
    *COUNT_FIELDS, "input_tokens", "output_tokens", "cost_usd",
    "human_active_minutes", "recorded_at",
}
RUN_FIELDS_V2 = RUN_FIELDS_V1 | {"elapsed_basis"}
RUN_FIELDS_V3 = RUN_FIELDS_V2 | {"work_items"}


class AutonomousWorkError(ValueError):
    """Invalid or duplicate autonomous run measurement."""


def _text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise AutonomousWorkError(f"{name} must be a non-empty trimmed string")
    if "\x00" in value or "\n" in value or "\r" in value:
        raise AutonomousWorkError(f"{name} may not contain control line breaks")
    return value


def _instant(value: Any, name: str) -> datetime:
    text = _text(value, name)
    try:
        result = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError as exc:
        raise AutonomousWorkError(f"{name} must be an ISO timestamp") from exc
    if result.tzinfo is None or result.utcoffset() is None:
        raise AutonomousWorkError(f"{name} must include a timezone")
    return result


def _nonnegative_int(value: Any, name: str) -> int:
    if type(value) is not int or value < 0:
        raise AutonomousWorkError(f"{name} must be a non-negative integer")
    return value


def _validate(row: Any, index: int) -> dict[str, Any]:
    context = f"row {index}"
    if not isinstance(row, dict):
        raise AutonomousWorkError(f"{context} must be an object")
    version = row.get("schema_version")
    expected_fields = (
        RUN_FIELDS_V1 if version == "1"
        else RUN_FIELDS_V2 if version == "2"
        else RUN_FIELDS_V3 if version == "3"
        else set()
    )
    missing = sorted(expected_fields - set(row))
    extra = sorted(set(row) - expected_fields)
    if missing or extra:
        message = []
        if missing:
            message.append(f"missing {', '.join(missing)}")
        if extra:
            message.append(f"unknown {', '.join(extra)}")
        raise AutonomousWorkError(f"{context}: {'; '.join(message)}")
    if version not in {"1", "2", "3"} or row["policy_version"] != POLICY_VERSION:
        raise AutonomousWorkError(f"{context} has unsupported schema or policy version")
    _text(row["measurement_id"], f"{context}.measurement_id")
    run_id = _text(row["run_id"], f"{context}.run_id")
    if not RUN_ID_RE.fullmatch(run_id):
        raise AutonomousWorkError(f"{context}.run_id must be a plain identifier")
    for field in ("agent", "model", "cohort_id", "repo_id", "wave_id"):
        _text(row[field], f"{context}.{field}")
    url = _text(row["repository_url"], f"{context}.repository_url")
    if not re.fullmatch(r"https://github\.com/[^/\s]+/[^/\s]+", url):
        raise AutonomousWorkError(f"{context}.repository_url must be canonical GitHub URL")
    if not isinstance(row["manifest_digest"], str) or not SHA_RE.fullmatch(row["manifest_digest"]):
        raise AutonomousWorkError(f"{context}.manifest_digest must be a SHA-256 digest")
    if not isinstance(row["source_pin"], str) or not PIN_RE.fullmatch(row["source_pin"]):
        raise AutonomousWorkError(f"{context}.source_pin must be a 40-character lowercase pin")
    started = _instant(row["started_at"], f"{context}.started_at")
    completed = _instant(row["completed_at"], f"{context}.completed_at")
    _instant(row["recorded_at"], f"{context}.recorded_at")
    elapsed = row["elapsed_seconds"]
    if isinstance(elapsed, bool) or not isinstance(elapsed, (int, float)) or not math.isfinite(elapsed) or elapsed <= 0:
        raise AutonomousWorkError(f"{context}.elapsed_seconds must be finite and > 0")
    measured = (completed - started).total_seconds()
    basis = row.get("elapsed_basis", "wall_clock")
    if basis not in {"wall_clock", "phase_sum"}:
        raise AutonomousWorkError(f"{context}.elapsed_basis must be wall_clock or phase_sum")
    if completed < started:
        raise AutonomousWorkError(f"{context}.completed_at cannot precede started_at")
    if basis == "wall_clock" and (measured <= 0 or abs(measured - elapsed) > 1.0):
        raise AutonomousWorkError(f"{context}.elapsed_seconds must match its timestamps")
    for field in COUNT_FIELDS:
        _nonnegative_int(row[field], f"{context}.{field}")
    if version == "3":
        work_items = row["work_items"]
        if not isinstance(work_items, list):
            raise AutonomousWorkError(f"{context}.work_items must be an array")
        seen_sites: set[str] = set()
        seen_questions: set[tuple[str, str]] = set()
        reviewed_count = 0
        question_count = 0
        for item_index, item in enumerate(work_items):
            item_context = f"{context}.work_items[{item_index}]"
            if not isinstance(item, dict) or set(item) != {"site", "reviewed", "question_ids"}:
                raise AutonomousWorkError(
                    f"{item_context} requires site, reviewed, and question_ids"
                )
            site = _text(item["site"], f"{item_context}.site")
            if site in seen_sites:
                raise AutonomousWorkError(f"{item_context}.site duplicates a work item")
            seen_sites.add(site)
            if type(item["reviewed"]) is not bool:
                raise AutonomousWorkError(f"{item_context}.reviewed must be boolean")
            reviewed_count += int(item["reviewed"])
            question_ids = item["question_ids"]
            if not isinstance(question_ids, list):
                raise AutonomousWorkError(f"{item_context}.question_ids must be an array")
            for question_index, question_id in enumerate(question_ids):
                question_id = _text(
                    question_id, f"{item_context}.question_ids[{question_index}]"
                )
                identity = (site, question_id)
                if identity in seen_questions:
                    raise AutonomousWorkError(
                        f"{item_context}.question_ids[{question_index}] duplicates a question"
                    )
                seen_questions.add(identity)
                question_count += 1
        if reviewed_count != row["reviewed_sites"]:
            raise AutonomousWorkError(
                f"{context}.work_items reviewed count differs from reviewed_sites"
            )
        if question_count != row["proof_questions_attempted"]:
            raise AutonomousWorkError(
                f"{context}.work_items question count differs from proof_questions_attempted"
            )
    for field in ("input_tokens", "output_tokens"):
        if row[field] is not None:
            _nonnegative_int(row[field], f"{context}.{field}")
    cost = row["cost_usd"]
    if cost is not None:
        if not isinstance(cost, str):
            raise AutonomousWorkError(f"{context}.cost_usd must be a decimal string or null")
        try:
            cost_value = Decimal(cost)
        except InvalidOperation as exc:
            raise AutonomousWorkError(f"{context}.cost_usd must be a decimal string") from exc
        if not cost_value.is_finite() or cost_value < 0:
            raise AutonomousWorkError(f"{context}.cost_usd must be finite and non-negative")
    human_minutes = row["human_active_minutes"]
    if human_minutes is not None and (
        isinstance(human_minutes, bool)
        or not isinstance(human_minutes, (int, float))
        or not math.isfinite(human_minutes)
        or human_minutes < 0
    ):
        raise AutonomousWorkError(f"{context}.human_active_minutes must be non-negative or null")
    if row["human_interventions"] == 0 and human_minutes not in {None, 0}:
        raise AutonomousWorkError(f"{context}.human_active_minutes requires a human intervention")

    limits = (
        ("contracts_adopted", "reviewed_sites"),
        ("decided_faithful_questions", "proof_questions_attempted"),
        ("unsat_guarantees", "decided_faithful_questions"),
        ("sat_candidates", "decided_faithful_questions"),
        ("replayed_witnesses", "sat_candidates"),
        ("reachable_violations", "replayed_witnesses"),
        ("security_impact_confirmed", "reachable_violations"),
        ("consumer_adopted_gates", "local_runnable_gates"),
        ("third_party_reports_sent", "security_impact_confirmed"),
        ("maintainer_confirmations", "third_party_reports_sent"),
        ("third_party_fixes", "maintainer_confirmations"),
    )
    for numerator, denominator in limits:
        if row[numerator] > row[denominator]:
            raise AutonomousWorkError(
                f"{context}.{numerator} cannot exceed {denominator}"
            )
    return dict(row)


def load_rows(path: pathlib.Path | None = None) -> list[dict[str, Any]]:
    source = pathlib.Path(path) if path is not None else LOG_PATH
    if not source.is_file():
        return []
    rows = []
    ids: set[str] = set()
    run_ids: set[str] = set()
    for index, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = _validate(json.loads(line), index)
        except json.JSONDecodeError as exc:
            raise AutonomousWorkError(f"{source}:{index}: invalid JSON: {exc.msg}") from exc
        if row["measurement_id"] in ids:
            raise AutonomousWorkError(f"{source}:{index}: duplicate measurement_id")
        if row["run_id"] in run_ids:
            raise AutonomousWorkError(f"{source}:{index}: duplicate run_id")
        ids.add(row["measurement_id"])
        run_ids.add(row["run_id"])
        rows.append(row)
    return rows


def append_run(row: dict[str, Any], path: pathlib.Path | None = None) -> dict[str, Any]:
    """Validate and append one measured run while serializing duplicate checks."""
    normalized = _validate(row, 1)
    dest = pathlib.Path(path) if path is not None else LOG_PATH
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("a+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        handle.seek(0)
        ids = set()
        run_ids = set()
        for index, line in enumerate(handle.read().splitlines(), 1):
            if not line.strip():
                continue
            try:
                old = _validate(json.loads(line), index)
            except (json.JSONDecodeError, AutonomousWorkError) as exc:
                raise AutonomousWorkError(f"cannot append to invalid {dest}:{index}: {exc}") from exc
            ids.add(old["measurement_id"])
            run_ids.add(old["run_id"])
        if normalized["measurement_id"] in ids:
            raise AutonomousWorkError("measurement_id already exists")
        if normalized["run_id"] in run_ids:
            raise AutonomousWorkError("run_id already exists")
        handle.seek(0, 2)
        handle.write(json.dumps(normalized, sort_keys=True, ensure_ascii=True) + "\n")
        handle.flush()
        return normalized


def summarize(
    path: pathlib.Path | None = None,
    *,
    cohort_ids: set[str] | None = None,
) -> dict[str, Any]:
    """Summarize resource, useful-gate, bug, and external-outcome tracks."""
    rows = load_rows(path)
    if cohort_ids is not None:
        if not cohort_ids or any(not isinstance(value, str) or not value.strip() for value in cohort_ids):
            raise AutonomousWorkError("cohort_ids must contain non-empty cohort IDs")
        rows = [row for row in rows if row["cohort_id"] in cohort_ids]
    totals = {field: sum(row[field] for row in rows) for field in COUNT_FIELDS}
    elapsed = sum(float(row["elapsed_seconds"]) for row in rows)
    elapsed_by_basis = {
        basis: round(
            sum(
                float(row["elapsed_seconds"])
                for row in rows
                if row.get("elapsed_basis", "wall_clock") == basis
            ),
            3,
        )
        for basis in ("wall_clock", "phase_sum")
    }

    def complete_total(field: str) -> str | None:
        values = [row[field] for row in rows]
        if not values or any(value is None for value in values):
            return None
        if field == "cost_usd":
            return str(sum((Decimal(value) for value in values), Decimal(0)))
        return str(sum(values))

    def rate(numerator: str, denominator: str) -> float | None:
        den = totals[denominator]
        return totals[numerator] / den if den else None

    return {
        "schema_version": "2",
        "policy_version": POLICY_VERSION,
        "run_count": len(rows),
        "cohort_filter": sorted(cohort_ids) if cohort_ids is not None else None,
        "resource_totals": {
            "elapsed_seconds": round(elapsed, 3),
            "elapsed_seconds_by_basis": elapsed_by_basis,
            "input_tokens": complete_total("input_tokens"),
            "input_token_rows_missing": sum(row["input_tokens"] is None for row in rows),
            "output_tokens": complete_total("output_tokens"),
            "output_token_rows_missing": sum(row["output_tokens"] is None for row in rows),
            "cost_usd": complete_total("cost_usd"),
            "cost_rows_missing": sum(row["cost_usd"] is None for row in rows),
            "human_active_minutes": complete_total("human_active_minutes"),
            "human_time_rows_missing": sum(row["human_active_minutes"] is None for row in rows),
        },
        "counts": totals,
        "rates": {
            "contracts_per_agent_hour": (
                totals["contracts_adopted"] / (elapsed / 3600) if elapsed else None
            ),
            "decided_per_attempted": rate("decided_faithful_questions", "proof_questions_attempted"),
            "unsat_per_decided": rate("unsat_guarantees", "decided_faithful_questions"),
            "replayed_per_sat_candidate": rate("replayed_witnesses", "sat_candidates"),
            "reachable_violation_per_replayed": rate("reachable_violations", "replayed_witnesses"),
            "impact_confirmed_per_reachable": rate("security_impact_confirmed", "reachable_violations"),
            "consumer_adopted_per_local_gate": rate("consumer_adopted_gates", "local_runnable_gates"),
            "third_party_confirmation_per_report_sent": rate("maintainer_confirmations", "third_party_reports_sent"),
            "third_party_fix_per_confirmation": rate("third_party_fixes", "maintainer_confirmations"),
        },
        "track_order": ["useful_proofs_and_gates", "bug_discovery", "external_outcomes"],
        "rates_are_null_when_denominator_is_zero": True,
    }
