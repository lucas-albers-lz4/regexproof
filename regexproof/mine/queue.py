"""FIFO overflow mine queue (P2 B2)."""

from __future__ import annotations

import json
import os
import tempfile
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

DEFAULT_QUEUE_CAP = 100
DEFAULT_TTL_DAYS = 90
DEFAULT_DAILY_CAP = 10

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
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(queue, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    fd, tmp = tempfile.mkstemp(prefix=f".{p.name}.", suffix=".tmp", dir=p.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, p)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


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
) -> str:
    """Append *item* FIFO. Returns ``enqueued``, ``duplicate``, or ``full``."""
    from regexproof.mine.exclusions import normalize_repo_url

    url = item.get("url")
    if url:
        target = normalize_repo_url(str(url))
        for existing in queue["items"]:
            eu = existing.get("url")
            if eu and normalize_repo_url(str(eu)) == target:
                return "duplicate"
    if len(queue["items"]) >= cap:
        return "full"
    row = dict(item)
    if not row.get("queued_at"):
        row["queued_at"] = (now or datetime.now(timezone.utc).date()).isoformat()
    queue["items"].append(row)
    return "enqueued"


def drain(queue: dict[str, Any], max_n: int) -> list[dict[str, Any]]:
    """Pop up to *max_n* items from the front (FIFO)."""
    n = max(0, min(max_n, len(queue["items"])))
    out = queue["items"][:n]
    queue["items"] = queue["items"][n:]
    return out
