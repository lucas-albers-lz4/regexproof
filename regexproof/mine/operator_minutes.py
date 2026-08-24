"""Wave 6 (#575): operator-minutes log — never the freeze artifact."""

from __future__ import annotations

import json
import pathlib
import statistics
import uuid
from datetime import datetime, timezone
from typing import Any

LOG_PATH = pathlib.Path("properties/generated/operator_minutes.jsonl")
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
    if active_minutes is not None and active_minutes < 0:
        raise SystemExit("operator_minutes: active_minutes must be >= 0")
    if wall_minutes is not None and wall_minutes < 0:
        raise SystemExit("operator_minutes: wall_minutes must be >= 0")
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
    if dest.is_file() and source == "stopwatch":
        for existing in load_rows(dest):
            if (
                existing.get("url") == url
                and existing.get("pin") == pin
                and existing.get("source") == "stopwatch"
            ):
                return existing
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
    return {
        "median": statistics.median(values),
        "mean": statistics.mean(values),
        "n": len(values),
    }


def summarize(path: pathlib.Path | None = None) -> dict[str, Any]:
    """Median-primary / mean-secondary, wall vs active never mixed."""
    rows = load_rows(path)
    wall = [float(r["wall_minutes"]) for r in rows if r.get("wall_minutes") is not None]
    active = [
        float(r["active_minutes"]) for r in rows if r.get("active_minutes") is not None
    ]
    return {
        "rows": len(rows),
        "wall_minutes": _median_mean(wall),
        "active_minutes": _median_mean(active),
        "baseline_floor_met": len(rows) >= 5,
    }
