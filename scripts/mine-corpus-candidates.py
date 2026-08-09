#!/usr/bin/env python3
"""Mine corpus candidates via GitHub Code Search (P2 B5).

Usage:
  python scripts/mine-corpus-candidates.py --dry-run
  python scripts/mine-corpus-candidates.py --ledger PATH --queue PATH
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.exclusions import is_excluded, load_admitted_urls
from regexproof.mine.ledger import empty_ledger, find_candidate, load_ledger, save_ledger
from regexproof.mine.queue import (
    daily_mine_cap,
    drain,
    enqueue,
    evict_stale,
    load_queue,
    save_queue,
)
from regexproof.mine.search import AuthError, SearchRunResult, run_search


def _http_session():
    try:
        import requests
    except ImportError as e:  # pragma: no cover
        raise SystemExit("requests is required for live mining") from e
    return requests.Session()


def assimilate(
    *,
    search_result: SearchRunResult,
    ledger: dict[str, Any],
    queue: dict[str, Any],
    admitted: set[str],
    dry_run: bool,
    now_iso: str | None = None,
) -> list[dict[str, Any]]:
    """Merge search hits into ledger/queue respecting calendar-day cap (overflow first)."""
    now_iso = now_iso or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    day = now_iso[:10]
    cap = daily_mine_cap()
    already = sum(
        1
        for c in ledger.get("candidates", [])
        if str(c.get("first_seen") or "")[:10] == day
    )
    room = max(0, cap - already)
    accepted: list[dict[str, Any]] = []

    evict_stale(queue)
    # Overflow first — pull one-at-a-time so exclusions do not waste the day budget
    while room > 0 and queue.get("items"):
        item = drain(queue, 1)[0]
        url = item.get("url")
        if not url or is_excluded(url, ledger=ledger, admitted=admitted):
            continue
        if find_candidate(ledger, url):
            continue
        entry = {
            "url": url,
            "default_branch": item.get("default_branch") or "main",
            "pin": item.get("pin") or "",
            "pushed_date": item.get("pushed_date") or "",
            "stars": int(item.get("stars") or 0),
            "source_query": item.get("source_query") or "",
            "first_seen": now_iso,
            "status": "mined",
        }
        if item.get("capped"):
            entry["capped"] = True
        ledger["candidates"].append(entry)
        accepted.append(entry)
        room -= 1

    queue_dropped = 0
    for cand in search_result.candidates:
        url = cand["url"]
        if is_excluded(url, ledger=ledger, admitted=admitted):
            continue
        if find_candidate(ledger, url):
            continue
        if room > 0:
            entry = {
                "url": url,
                "default_branch": cand.get("default_branch") or "main",
                "pin": cand.get("pin") or "",
                "pushed_date": cand.get("pushed_date") or "",
                "stars": int(cand.get("stars") or 0),
                "source_query": cand.get("source_query") or "",
                "first_seen": now_iso,
                "status": "mined",
            }
            # Cap flag is search-run provenance only — never stamp overflow drains.
            if cand.get("capped") or search_result.capped:
                entry["capped"] = True
            ledger["candidates"].append(entry)
            accepted.append(entry)
            room -= 1
        else:
            status = enqueue(queue, cand)
            if status == "full":
                queue_dropped += 1

    if queue_dropped:
        print(
            f"warning: mine-queue full; dropped {queue_dropped} overflow candidate(s)",
            file=sys.stderr,
        )

    return accepted


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="Print candidates; no writes")
    ap.add_argument(
        "--ledger",
        type=Path,
        default=ROOT / "properties" / "generated" / "candidate-ledger.json",
    )
    ap.add_argument(
        "--queue",
        type=Path,
        default=ROOT / "properties" / "generated" / "mine-queue.json",
    )
    ap.add_argument("--generated", type=Path, default=ROOT / "properties" / "generated")
    args = ap.parse_args(argv)

    ledger_path = args.ledger.expanduser().resolve()
    queue_path = args.queue.expanduser().resolve()

    ledger = load_ledger(ledger_path) if ledger_path.exists() else empty_ledger()
    queue = load_queue(queue_path)
    admitted = load_admitted_urls(args.generated.expanduser().resolve())

    try:
        result = run_search(_http_session())
    except AuthError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    if result.errors:
        for err in result.errors:
            print(f"warning: search error: {err}", file=sys.stderr)

    accepted = assimilate(
        search_result=result,
        ledger=ledger,
        queue=queue,
        admitted=admitted,
        dry_run=args.dry_run,
    )

    for c in accepted:
        print(
            json.dumps(
                {
                    "url": c["url"],
                    "stars": c["stars"],
                    "pushed_date": c["pushed_date"],
                    "source_query": c["source_query"],
                    "pin": c.get("pin"),
                },
                sort_keys=True,
            )
        )

    if args.dry_run:
        if result.errors and not result.candidates and not accepted:
            return 1
        return 0

    run_meta: dict[str, Any] = {
        "capped": bool(result.capped),
        "search_errors": list(result.errors),
    }
    ledger["run"] = run_meta
    save_ledger(ledger_path, ledger)
    save_queue(queue_path, queue)
    if result.errors and not result.candidates and not accepted:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
