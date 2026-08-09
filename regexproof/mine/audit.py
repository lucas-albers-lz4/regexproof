"""Ledger audit helpers + weekly auto-NO-GO sampler (P3 / #132)."""

from __future__ import annotations

import math
import random
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Callable

from regexproof.mine.exclusions import normalize_repo_url
from regexproof.mine.ledger import find_candidate, load_ledger, save_ledger
from regexproof.mine.transition import transition_candidate

Clock = Callable[[], datetime]


def default_clock() -> datetime:
    return datetime.now(timezone.utc)


def ensure_candidate_audit(
    ledger_path: Path | str,
    url: str,
    *,
    updates: dict[str, Any],
    clock: Clock | None = None,
) -> dict[str, Any]:
    """Merge *updates* into candidate ``audit`` and atomically save."""
    path = Path(ledger_path)
    ledger = load_ledger(path)
    cand = find_candidate(ledger, url)
    if cand is None:
        raise ValueError(f"candidate not in ledger: {url}")
    audit = cand.setdefault("audit", {})
    if not isinstance(audit, dict):
        raise ValueError("candidate audit must be an object")
    audit.update(updates)
    now = (clock or default_clock)()
    audit["updated_at"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    save_ledger(path, ledger)
    return cand


def mark_auto_filed(
    ledger_path: Path | str,
    url: str,
    *,
    template_fired: str = "below-scale",
    clock: Clock | None = None,
) -> dict[str, Any]:
    now = (clock or default_clock)()
    ts = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    # auto_filed_at is set once for week membership; updated_at may move later.
    path = Path(ledger_path)
    ledger = load_ledger(path)
    cand = find_candidate(ledger, url)
    if cand is None:
        raise ValueError(f"candidate not in ledger: {url}")
    audit = cand.setdefault("audit", {})
    if not isinstance(audit, dict):
        raise ValueError("candidate audit must be an object")
    if not audit.get("auto_filed_at"):
        audit["auto_filed_at"] = ts
    # Do not clear needs_human_review / re_evaluate — sampler failures must stick
    # until a human decision explicitly resolves them.
    audit["auto_filed"] = True
    audit["template_fired"] = template_fired
    audit["updated_at"] = ts
    save_ledger(path, ledger)
    return cand


def mark_needs_human_review(
    ledger_path: Path | str,
    url: str,
    *,
    reason: str = "",
    clock: Clock | None = None,
) -> dict[str, Any]:
    updates: dict[str, Any] = {"needs_human_review": True}
    if reason:
        updates["human_review_reason"] = reason
    return ensure_candidate_audit(ledger_path, url, updates=updates, clock=clock)


def mark_human_resolved(
    ledger_path: Path | str,
    url: str,
    *,
    clock: Clock | None = None,
) -> dict[str, Any]:
    """Clear sampler/human-routing flags after a successful human decision."""
    return ensure_candidate_audit(
        ledger_path,
        url,
        updates={
            "needs_human_review": False,
            "re_evaluate": False,
            "human_resolved": True,
        },
        clock=clock,
    )


def sample_size(population: int) -> int:
    """``N = min(population, max(5, ceil(10% of population)))``; pop 0 → 0."""
    if population <= 0:
        return 0
    return min(population, max(5, math.ceil(0.1 * population)))


def _parse_iso_week(week: str) -> tuple[int, int]:
    # YYYY-Www
    if len(week) < 8 or week[4:6] != "-W":
        raise ValueError(f"week must look like YYYY-Www, got {week!r}")
    year = int(week[:4])
    w = int(week[6:])
    return year, w


def _in_iso_week(iso_ts: str, year: int, week: int) -> bool:
    if not iso_ts:
        return False
    try:
        day = date.fromisoformat(iso_ts[:10])
    except ValueError:
        return False
    y, w, _ = day.isocalendar()
    return y == year and w == week


def auto_filed_in_week(ledger: dict[str, Any], week: str) -> list[dict[str, Any]]:
    year, w = _parse_iso_week(week)
    out: list[dict[str, Any]] = []
    for c in ledger.get("candidates", []):
        audit = c.get("audit") or {}
        if not audit.get("auto_filed"):
            continue
        # Prefer auto_filed_at so later audit updates do not move week membership.
        ts = str(audit.get("auto_filed_at") or audit.get("updated_at") or "")
        if _in_iso_week(ts, year, w):
            out.append(c)
    return out


def run_audit_sampler(
    ledger_path: Path | str,
    *,
    week: str,
    seed: int | None = None,
    fail_urls: set[str] | None = None,
    clock: Clock | None = None,
) -> dict[str, Any]:
    """Sample week's auto-filed NO-GOs; failed URLs re-queue via transition API.

    *fail_urls* simulates reviewer failures (tests / dry ops). Selection is a
    random draw of N from the week's auto-filed population.
    """
    path = Path(ledger_path).expanduser().resolve()
    ledger = load_ledger(path)
    population = auto_filed_in_week(ledger, week)
    n = sample_size(len(population))
    rng = random.Random(seed)
    selected = population if n >= len(population) else rng.sample(population, n)

    fail_norm = {normalize_repo_url(u) for u in (fail_urls or set())}
    failed: list[str] = []
    for cand in selected:
        url = str(cand.get("url") or "")
        if normalize_repo_url(url) not in fail_norm:
            continue
        ensure_candidate_audit(
            path,
            url,
            updates={"re_evaluate": True, "needs_human_review": True},
            clock=clock,
        )
        transition_candidate(
            path,
            url,
            to="queued",
            reason="audit-sampler-fail",
        )
        failed.append(url)

    return {
        "week": week,
        "population": len(population),
        "sample_size": n,
        "sampled_urls": [str(c.get("url")) for c in selected],
        "failed_urls": failed,
    }
