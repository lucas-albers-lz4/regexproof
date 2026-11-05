"""Wave 6 (#575): operator-minutes log — never the freeze artifact."""

from __future__ import annotations

import json
import math
import pathlib
import statistics
import uuid
from datetime import date, datetime, timezone
from typing import Any

LOG_PATH = pathlib.Path(__file__).resolve().parents[2] / "properties" / "generated" / "operator_minutes.jsonl"
SURVIVOR = frozenset({"go", "triage-trial"})
SOURCES = frozenset({"seed-artifact-timestamps", "stopwatch"})


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def append_row(
    *,
    url: str,
    pin: str,
    decision: str,
    source: str,
    wall_minutes: float | None = None,
    active_minutes: float | None = None,
    decision_date: str = "",
    path: pathlib.Path | None = None,
) -> dict[str, Any]:
    if decision not in SURVIVOR:
        raise SystemExit(
            f"operator_minutes: {decision!r} is not a human-reviewed survivor"
        )
    if source not in SOURCES:
        raise SystemExit(f"operator_minutes: unknown source {source!r}")
    if active_minutes is not None and (active_minutes < 0 or not math.isfinite(active_minutes)):
        raise SystemExit("operator_minutes: active_minutes must be a finite number >= 0")
    if wall_minutes is not None and (wall_minutes < 0 or not math.isfinite(wall_minutes)):
        raise SystemExit("operator_minutes: wall_minutes must be a finite number >= 0")
    if not url:
        raise SystemExit("operator_minutes: url is required")
    pin = pin.strip().lower()
    if len(pin) != 40 or any(c not in "0123456789abcdef" for c in pin):
        raise SystemExit("operator_minutes: pin must be a 40-char lowercase hex SHA")
    row = {
        "measurement_id": str(uuid.uuid4()),
        "url": url,
        "pin": pin,
        "decision": decision,
        "source": source,
        "wall_minutes": wall_minutes,
        "active_minutes": active_minutes,
        "recorded_at": _utc_now(),
        "decision_date": decision_date,
    }
    dest = pathlib.Path(path) if path is not None else LOG_PATH
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")
    return row


def load_rows(path: pathlib.Path | None = None) -> list[dict[str, Any]]:
    dest = pathlib.Path(path) if path is not None else LOG_PATH
    if not dest.is_file():
        return []
    rows = []
    for line in dest.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _median_mean(values: list[float]) -> dict[str, float | None]:
    if not values:
        return {"median": None, "mean": None, "n": 0}
    ordered = sorted(values)
    middle = len(ordered) // 2
    median = ordered[middle]
    if len(ordered) % 2 == 0:
        lower = ordered[middle - 1]
        median = lower + (median - lower) / 2
    return {
        "median": median,
        "mean": statistics.mean(values),
        "n": len(values),
    }


def _active_sample(row: dict[str, Any]) -> tuple[float | None, str | None]:
    """Return a valid stopwatch value, or why a supplied value is excluded."""
    value = row.get("active_minutes")
    if value is None:
        return None, None
    if row.get("source") != "stopwatch":
        return None, "not_stopwatch"
    if row.get("decision") not in SURVIVOR:
        return None, "non_survivor"
    if isinstance(value, bool):
        return None, "invalid_value"
    try:
        minutes = float(value)
    except (TypeError, ValueError):
        return None, "invalid_value"
    if not math.isfinite(minutes) or minutes < 0:
        return None, "invalid_value"
    return minutes, None


def summarize(
    path: pathlib.Path | None = None,
    *,
    rollout_cutoff_date: date | str | None = None,
    rollout_cutoff_evidence: str | None = None,
) -> dict[str, Any]:
    """Summarize provenance and active-time evidence without inventing timing.

    Only finite, nonnegative ``active_minutes`` from stopwatch rows for human
    survivors (GO/triage-trial) are active-time observations. Periods remain
    unclassified unless the caller supplies an evidence-backed cutoff. The
    cutoff is an operator assertion, not a rollout date inferred by this code.
    With date-only decision dates, the cutoff date and its adjacent days stay
    unclassified. Seed records remain part of the historical row-count floor,
    but never contribute an active-time value.
    """
    if rollout_cutoff_date is None:
        if rollout_cutoff_evidence:
            raise ValueError("rollout_cutoff_evidence requires rollout_cutoff_date")
        cutoff = None
    else:
        if isinstance(rollout_cutoff_date, datetime):
            raise ValueError("rollout_cutoff_date must be a date, not a datetime")
        if isinstance(rollout_cutoff_date, date):
            cutoff = rollout_cutoff_date
        elif isinstance(rollout_cutoff_date, str):
            try:
                cutoff = date.fromisoformat(rollout_cutoff_date)
            except ValueError as exc:
                raise ValueError("rollout_cutoff_date must be YYYY-MM-DD") from exc
            if cutoff.isoformat() != rollout_cutoff_date:
                raise ValueError("rollout_cutoff_date must be YYYY-MM-DD")
        else:
            raise ValueError("rollout_cutoff_date must be a date or YYYY-MM-DD string")
        if not rollout_cutoff_evidence or not rollout_cutoff_evidence.strip():
            raise ValueError(
                "an explicit rollout_cutoff_evidence reference is required with the cutoff date"
            )

    rows = load_rows(path)
    wall = [float(r["wall_minutes"]) for r in rows if r.get("wall_minutes") is not None]
    seeds = [r for r in rows if r.get("source") == "seed-artifact-timestamps"]
    stopwatch_rows = [r for r in rows if r.get("source") == "stopwatch"]
    active = []
    excluded_active = {"non_survivor": 0, "invalid_value": 0, "not_stopwatch": 0}
    for row in rows:
        value, exclusion = _active_sample(row)
        if value is not None:
            active.append(value)
        elif exclusion is not None:
            excluded_active[exclusion] += 1

    periods: dict[str, list[dict[str, Any]]] = {
        "pre_cutoff": [],
        "post_cutoff": [],
        "unclassified": [],
    }
    for row in rows:
        try:
            decision_date = date.fromisoformat(str(row.get("decision_date") or ""))
        except ValueError:
            periods["unclassified"].append(row)
            continue
        if cutoff is None:
            periods["unclassified"].append(row)
        elif (decision_date - cutoff).days < -1:
            periods["pre_cutoff"].append(row)
        elif (decision_date - cutoff).days > 1:
            periods["post_cutoff"].append(row)
        else:
            periods["unclassified"].append(row)

    period_report: dict[str, Any] = {}
    for name, period_rows in periods.items():
        measured = []
        excluded = {"non_survivor": 0, "invalid_value": 0, "not_stopwatch": 0}
        for row in period_rows:
            value, why = _active_sample(row)
            if value is not None:
                measured.append(value)
            elif why is not None:
                excluded[why] += 1
        period_report[name] = {
            "records": len(period_rows),
            "seed_records": sum(
                r.get("source") == "seed-artifact-timestamps" for r in period_rows
            ),
            "stopwatch_records": sum(
                r.get("source") == "stopwatch" for r in period_rows
            ),
            "active_minutes": _median_mean(measured),
            "excluded_active_values": excluded,
        }

    pre = period_report["pre_cutoff"]["active_minutes"]
    post = period_report["post_cutoff"]["active_minutes"]
    if pre["n"] and post["n"] and post["median"] != 0:
        ratio = pre["median"] / post["median"]
        if ratio == 0 and pre["median"] > 0:
            comparison: dict[str, Any] = {
                "ratio": None,
                "status": "undefined_ratio_underflow",
                "reason": "The measured ratio is below the positive floating-point range.",
            }
        elif math.isfinite(ratio):
            comparison = {
                "ratio": ratio,
                "status": "measured",
                "interpretation": "active_time_ratio_conditional_on_operator_cutoff",
            }
        else:
            comparison = {
                "ratio": None,
                "status": "undefined_ratio_overflow",
                "reason": "The measured ratio exceeds the finite floating-point range.",
            }
    elif pre["n"] and post["n"]:
        comparison = {
            "ratio": None,
            "status": "undefined_zero_post_median",
            "reason": "The post-cutoff measured median is zero, so the ratio is undefined.",
        }
    else:
        comparison = {
            "ratio": None,
            "status": "insufficient_measured_samples",
            "reason": (
                "A pre/post comparison requires non-null stopwatch active_minutes "
                "in both periods; seed rows and wall-clock timings do not count."
            ),
        }
    return {
        "rows": len(rows),
        "wall_minutes": _median_mean(wall),
        "active_minutes": _median_mean(active),
        "provenance": {
            "seed_records": len(seeds),
            "stopwatch_records": len(stopwatch_rows),
            "stopwatch_active_samples": len(active),
            "excluded_active_values": excluded_active,
            "period_cutoff_date": cutoff.isoformat() if cutoff else None,
            "period_cutoff_evidence": rollout_cutoff_evidence,
            "period_cutoff_is_operator_assumption": cutoff is not None,
            "period_basis": (
                "operator-supplied cutoff, not inferred from merge; decision_date; "
                "cutoff date and adjacent days unclassified"
                if cutoff
                else "not classified: supply an evidence-backed rollout cutoff"
            ),
        },
        "periods": period_report,
        "pre_post_active_ratio": comparison,
        "baseline_floor_met": len(rows) >= 5,
    }
