"""Ledger audit helpers + weekly auto-NO-GO sampler (P3 / #132)."""

from __future__ import annotations

import json
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
    if audit.get("re_evaluate"):
        raise ValueError(
            f"candidate {url} has re_evaluate=true; human decision required before auto-file"
        )
    # Successful auto-file clears eligibility-routing flags only.
    audit["auto_filed"] = True
    audit["template_fired"] = template_fired
    audit["needs_human_review"] = False
    audit.pop("human_review_reason", None)
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


def append_model_call(
    ledger_path: Path | str,
    url: str,
    call: dict[str, Any],
    *,
    clock: Clock | None = None,
) -> dict[str, Any]:
    """Append one model-call record to ``audit.model_calls`` (P3b)."""
    path = Path(ledger_path)
    ledger = load_ledger(path)
    cand = find_candidate(ledger, url)
    if cand is None:
        raise ValueError(f"candidate not in ledger: {url}")
    audit = cand.setdefault("audit", {})
    if not isinstance(audit, dict):
        raise ValueError("candidate audit must be an object")
    calls = audit.setdefault("model_calls", [])
    if not isinstance(calls, list):
        raise ValueError("audit.model_calls must be a list")
    now = (clock or default_clock)()
    row = dict(call)
    row.setdefault("at", now.strftime("%Y-%m-%dT%H:%M:%SZ"))
    calls.append(row)
    audit["updated_at"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    save_ledger(path, ledger)
    return cand


def mark_llm_template_fired(
    ledger_path: Path | str,
    url: str,
    *,
    template_fired: str,
    model_call: dict[str, Any] | None = None,
    clock: Clock | None = None,
) -> dict[str, Any]:
    """Record LLM draft template use — never sets ``auto_filed`` (C4)."""
    path = Path(ledger_path)
    ledger = load_ledger(path)
    cand = find_candidate(ledger, url)
    if cand is None:
        raise ValueError(f"candidate not in ledger: {url}")
    audit = cand.setdefault("audit", {})
    if not isinstance(audit, dict):
        raise ValueError("candidate audit must be an object")
    if audit.get("re_evaluate"):
        raise ValueError(
            f"candidate {url} has re_evaluate=true; human decision required before llm-draft"
        )
    now = (clock or default_clock)()
    ts = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    audit["template_fired"] = template_fired
    audit["template_fired_at"] = ts
    audit["updated_at"] = ts
    # Explicit: LLM draft is never an auto-file (C4), and clears prior review flags.
    audit["auto_filed"] = False
    audit["needs_human_review"] = False
    audit.pop("human_review_reason", None)
    if model_call is not None:
        calls = audit.setdefault("model_calls", [])
        if not isinstance(calls, list):
            raise ValueError("audit.model_calls must be a list")
        row = dict(model_call)
        row.setdefault("at", ts)
        calls.append(row)
    save_ledger(path, ledger)
    return cand


def mark_human_resolved(
    ledger_path: Path | str,
    url: str,
    *,
    decision: str | None = None,
    clock: Clock | None = None,
) -> dict[str, Any]:
    """Clear sampler/human-routing flags after a successful human decision.

    GO / triage-trial also clear ``auto_filed`` so the weekly sampler does not
    keep sampling a superseded auto-NO-GO.
    """
    updates: dict[str, Any] = {
        "needs_human_review": False,
        "re_evaluate": False,
        "human_resolved": True,
    }
    if decision in {"go", "triage-trial"}:
        updates["auto_filed"] = False
    return ensure_candidate_audit(
        ledger_path,
        url,
        updates=updates,
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
    """Week's auto-filed population, extended (#560 Wave 3): ALSO includes
    bulk-CLI-promoted decisions (``promoted_via == "bulk-review"``); excludes
    ``provenance=stub`` rows at schema level (a stub is never contract
    material, so it cannot join the audit population)."""
    year, w = _parse_iso_week(week)
    out: list[dict[str, Any]] = []
    for c in ledger.get("candidates", []):
        if str(c.get("provenance") or "") == "stub":
            continue  # schema-level exclusion (stub is queue-only)
        audit = c.get("audit") or {}
        is_bulk = str(audit.get("promoted_via") or "") == "bulk-review"
        if not (audit.get("auto_filed") or is_bulk):
            continue
        # Prefer auto_filed_at so later audit updates do not move week
        # membership; bulk promotions carry their own promoted_at.
        ts = str(audit.get("auto_filed_at") or audit.get("promoted_at")
                 or audit.get("updated_at") or "")
        if _in_iso_week(ts, year, w):
            out.append(c)
    return out


def _archive_gate_decision(generated_dir: Path, url: str) -> None:
    """Archive a candidate's gate decision file (audit-failure recovery reset).

    Renames ``<slug>_gate_decision.json`` to ``<slug>_gate_decision.audit-failed.json``
    so the read-only sync has nothing to reapply and rank treats the URL as
    eligible for re-probe. A NEW decision file written after recovery applies
    normally (P7 fold, luna re-gates 5+6). The file is located by its
    ``candidate_url`` field (decision files are named from the SANITIZED
    corpus slug, which is not the URL's last path segment).
    """
    if not generated_dir.is_dir():
        return
    want = normalize_repo_url(str(url or ""))
    if not want:
        return
    for f in generated_dir.glob("*_gate_decision.json"):
        try:
            payload = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if normalize_repo_url(str(payload.get("candidate_url") or "")) == want:
            f.rename(f.with_name(f"{f.stem}.audit-failed.json"))
            return


def run_audit_sampler(
    ledger_path: Path | str,
    *,
    week: str,
    seed: int | None = None,
    fail_urls: set[str] | None = None,
    clock: Clock | None = None,
    generated_dir: Path | str | None = None,
) -> dict[str, Any]:
    """Sample week's auto-filed NO-GOs; failed URLs re-queue via transition API.

    *fail_urls* simulates reviewer failures (tests / dry ops). Selection is a
    random draw of N from the week's auto-filed population. When
    *generated_dir* is given, a requeued candidate's gate decision file is
    archived (``<slug>_gate_decision.audit-failed.json``) so the read-only
    sync cannot reapply the old decision and rank surfaces the URL again
    (P7 fold, luna re-gate 5).
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
        if generated_dir:
            _archive_gate_decision(Path(generated_dir), url)
        failed.append(url)

    return {
        "week": week,
        "population": len(population),
        "sample_size": n,
        "sampled_urls": [str(c.get("url")) for c in selected],
        "failed_urls": failed,
    }
