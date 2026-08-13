"""FIFO overflow mine queue (P2 B2 / D4 queue policy)."""

from __future__ import annotations

import json
import logging
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from regexproof.io_atomic import atomic_write_text

DEFAULT_QUEUE_CAP = 100
DEFAULT_TTL_DAYS = 90
DEFAULT_DAILY_CAP = 10
MAX_REPLACEMENTS_PER_RUN = 10

# Queue capacity is sourced from this module-level constant (DEFAULT_QUEUE_CAP).
# Overridable via the ``cap`` parameter on ``enqueue()``; env override is
# intentionally NOT supported to keep the capacity predictable in CI.
QUEUE_CAPACITY_SOURCE = "regexproof.mine.queue.DEFAULT_QUEUE_CAP"

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_QUEUE_PATH = REPO_ROOT / "properties" / "generated" / "mine-queue.json"


def daily_mine_cap() -> int:
    """Max new ledger admissions per UTC calendar day (env ``DAILY_MINE_CAP``).

    Enforced by counting candidates whose ``first_seen`` date is today, not
    merely per process invocation.
    """
    env = os.environ.get("DAILY_MINE_CAP")
    if env is not None and env.strip().isdigit():
        return int(env)
    return DEFAULT_DAILY_CAP


def empty_queue() -> dict[str, Any]:
    return {"schema_version": "1", "items": []}


def load_queue(path: Path | str | None = None) -> dict[str, Any]:
    p = Path(path) if path else DEFAULT_QUEUE_PATH
    if not p.exists():
        return empty_queue()
    data = json.loads(p.read_text(encoding="utf-8"))
    if "items" not in data or not isinstance(data["items"], list):
        raise ValueError("mine-queue missing items list")
    return data


def save_queue(path: Path | str, queue: dict[str, Any]) -> None:
    text = json.dumps(queue, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    atomic_write_text(path, text)


def _parse_pushed(pushed_date: str) -> date | None:
    if not pushed_date:
        return None
    try:
        return date.fromisoformat(pushed_date[:10])
    except ValueError:
        return None


def evict_stale(
    queue: dict[str, Any],
    *,
    ttl_days: int = DEFAULT_TTL_DAYS,
    today: date | None = None,
) -> int:
    """Drop items older than TTL. Prefer ``queued_at``; else ``pushed_date``.

    Rows with neither date are treated as stale so the FIFO cap cannot fill
    with immortal empty-date entries. Preferring ``queued_at`` keeps overflow
    candidates that were only just discovered even when GitHub ``pushed_date``
    is older than the TTL.
    """
    today = today or datetime.now(timezone.utc).date()
    cutoff = today - timedelta(days=ttl_days)
    kept: list[dict[str, Any]] = []
    evicted = 0
    for item in queue["items"]:
        # Prefer time-in-queue so overflow waiting is not culled by stale GitHub push dates.
        d = _parse_pushed(str(item.get("queued_at") or ""))
        if d is None:
            d = _parse_pushed(str(item.get("pushed_date") or ""))
        if d is None or d < cutoff:
            evicted += 1
            continue
        kept.append(item)
    queue["items"] = kept
    return evicted


def enqueue(
    queue: dict[str, Any],
    item: dict[str, Any],
    *,
    cap: int = DEFAULT_QUEUE_CAP,
    now: date | None = None,
    replacements_left: list[int] | None = None,
) -> str:
    """Append *item* FIFO. Returns ``enqueued``, ``duplicate``, ``full``, or ``replaced``.

    On duplicate URL, refresh pin/stars/pushed_date/source_query from *item*
    while keeping the original queue position and ``queued_at``.

    When the queue is full and *replacements_left* is provided (a mutable
    single-element list like ``[10]``), the newcomer replaces the
    lowest-scored item **only if it outscores it**. The counter is
    decremented on each replacement; when it reaches 0 no further
    replacements occur and the function returns ``full``.
    """
    from regexproof.mine.exclusions import normalize_repo_url

    url = item.get("url")
    if url:
        target = normalize_repo_url(str(url))
        for existing in queue["items"]:
            eu = existing.get("url")
            if eu and normalize_repo_url(str(eu)) == target:
                for key in (
                    "pin", "stars", "pushed_date", "source_query",
                    "default_branch", "capped",
                ):
                    if key in item:
                        existing[key] = item[key]
                return "duplicate"
    if len(queue["items"]) < cap:
        row = dict(item)
        if not row.get("queued_at"):
            row["queued_at"] = (now or datetime.now(timezone.utc).date()).isoformat()
        queue["items"].append(row)
        return "enqueued"

    # Queue full — attempt replacement of lowest-scored item.
    if replacements_left is None or replacements_left[0] <= 0:
        return "full"

    from regexproof.mine.score import candidate_score

    new_score, _ = candidate_score(item)
    worst_idx = -1
    worst_score = float("inf")
    for i, existing in enumerate(queue["items"]):
        sc, _ = candidate_score(existing)
        if sc < worst_score:
            worst_score = sc
            worst_idx = i
    if worst_idx < 0 or new_score <= worst_score:
        return "full"

    replaced_item = queue["items"][worst_idx]
    row = dict(item)
    if not row.get("queued_at"):
        row["queued_at"] = (now or datetime.now(timezone.utc).date()).isoformat()
    queue["items"][worst_idx] = row
    replacements_left[0] -= 1
    logging.getLogger(__name__).info(
        "queue replacement: evicted %s (score %.1f) for %s (score %.1f)",
        replaced_item.get("url"),
        worst_score,
        row.get("url"),
        new_score,
    )
    return "replaced"


def drain(queue: dict[str, Any], max_n: int) -> list[dict[str, Any]]:
    """Pop up to *max_n* items from the front (FIFO)."""
    n = max(0, min(max_n, len(queue["items"])))
    out = queue["items"][:n]
    queue["items"] = queue["items"][n:]
    return out
