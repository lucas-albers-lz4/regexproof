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
    MAX_REPLACEMENTS_PER_RUN,
    daily_mine_cap,
    drain,
    enqueue,
    evict_stale,
    load_queue,
    save_queue,
)
from regexproof.mine.score import SCORE_VERSION, rank_candidates
from regexproof.mine.search import AuthError, SearchRunResult, run_search
from regexproof.mine.transition import TransitionError, set_status


_ENRICH_FIELDS = ("fork", "size", "language", "archived")


def _ledger_entry(source: dict[str, Any], *, now_iso: str, capped: bool = False) -> dict[str, Any]:
    entry = {
        "url": source.get("url"),
        "default_branch": source.get("default_branch") or "main",
        "pin": source.get("pin") or "",
        "pushed_date": source.get("pushed_date") or "",
        "stars": int(source.get("stars") or 0),
        "source_query": source.get("source_query") or "",
        "first_seen": now_iso,
        "status": "mined",
    }
    for field in _ENRICH_FIELDS:
        if field in source:
            entry[field] = source[field]
    if "pin_probed" in source:
        entry["pin_probed"] = source["pin_probed"]
    if capped:
        entry["capped"] = True
    return entry


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
    # Score-v1: highest-value overflow first (still drain one-at-a-time for exclusions).
    queue["items"] = rank_candidates(list(queue.get("items") or []))
    while room > 0 and queue.get("items"):
        item = drain(queue, 1)[0]
        url = item.get("url")
        if not url or is_excluded(url, ledger=ledger, admitted=admitted):
            continue
        if find_candidate(ledger, url):
            continue
        entry = _ledger_entry(
            {**item, "url": url},
            now_iso=now_iso,
            capped=bool(item.get("capped")),
        )
        ledger["candidates"].append(entry)
        accepted.append(entry)
        room -= 1

    queue_dropped = 0
    queue_replaced = 0
    replacements_left = [MAX_REPLACEMENTS_PER_RUN]
    ranked_hits = rank_candidates(list(search_result.candidates))
    for cand in ranked_hits:
        url = cand["url"]
        if is_excluded(url, ledger=ledger, admitted=admitted):
            continue
        if find_candidate(ledger, url):
            continue
        if room > 0:
            entry = _ledger_entry(cand, now_iso=now_iso)
            # Cap flag is search-run provenance only — never stamp overflow drains.
            if cand.get("capped") or search_result.capped:
                entry["capped"] = True
            ledger["candidates"].append(entry)
            accepted.append(entry)
            room -= 1
        else:
            status = enqueue(queue, cand, replacements_left=replacements_left)
            if status == "full":
                queue_dropped += 1
            elif status == "replaced":
                queue_replaced += 1

    if queue_dropped:
        print(
            f"warning: mine-queue full; dropped {queue_dropped} overflow candidate(s)",
            file=sys.stderr,
        )
    if queue_replaced:
        print(
            f"info: mine-queue replacement; {queue_replaced} lower-scored item(s) evicted",
            file=sys.stderr,
        )

    return accepted


def sync_gate_decisions(
    ledger_path: Path,
    generated_dir: Path,
    *,
    dry_run: bool = False,
) -> int:
    """Scan ``*_gate_decision.json`` and transition ledger rows via the P2 API.

    Returns the number of status transitions applied.  Read-only join —
    no GitHub API calls, no raw JSON writes.
    """
    if not ledger_path.is_file():
        return 0
    ledger = load_ledger(ledger_path)
    synced = 0
    for p in sorted(generated_dir.glob("*_gate_decision.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        decision = data.get("decision")
        url = data.get("candidate_url")
        if not decision or not url:
            continue
        cand = find_candidate(ledger, url)
        if cand is None:
            continue
        current = cand.get("status")
        if current and current.startswith("gated:"):
            continue
        if dry_run:
            synced += 1
            continue
        try:
            set_status(ledger_path, url, decision=decision, reason=f"sync:{p.stem}")
            synced += 1
        except TransitionError:
            continue
    return synced


def sync_and_reload(
    ledger_path: Path,
    generated_dir: Path,
    *,
    dry_run: bool = False,
) -> tuple[int, dict]:
    """Sync gate decisions into the ledger and return (synced, fresh_ledger).

    The ledger is RELOADED from disk after the sync so callers never save a
    stale pre-sync in-memory object over the applied transitions (P7 fold —
    main() uses this; the regression test calls it directly).
    """
    synced = sync_gate_decisions(ledger_path, generated_dir, dry_run=dry_run)
    return synced, load_ledger(ledger_path)


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

    synced, ledger = sync_and_reload(
        ledger_path,
        args.generated.expanduser().resolve(),
        dry_run=args.dry_run,
    )
    if synced:
        print(json.dumps({"kind": "gate_sync", "synced": synced}))

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

    summary = {
        "kind": "mine_run_summary",
        "accepted": len(accepted),
        "ledger": len(ledger.get("candidates", [])),
        "queue": len(queue.get("items", [])),
        "capped": bool(result.capped),
        "dry_run": bool(args.dry_run),
        "daily_mine_cap": daily_mine_cap(),
        "search_errors": len(result.errors),
        "allocator": f"score-{SCORE_VERSION}",
    }
    print(json.dumps(summary, sort_keys=True))

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
