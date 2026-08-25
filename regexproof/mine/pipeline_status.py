"""Wave 11 (#580): assemble operator pipeline status from committed artifacts.

Pure projection — no writes. Numbers come from ``batch/state.json``,
``candidate-ledger.json``, ``mine-queue.json``, and the conversion-ledger
hop / starvation tables.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

from regexproof.mine import batch_state, escape_window

ROOT = Path(__file__).resolve().parents[2]
GEN = ROOT / "properties" / "generated"
LEDGER_JSON = GEN / "conversion-ledger.json"
CANDIDATE_LEDGER = GEN / "candidate-ledger.json"
QUEUE_PATH = GEN / "mine-queue.json"
BASELINE_PATH = GEN / "escape_baseline.json"


def _load_json(path: Path, *, required: bool = False) -> dict[str, Any]:
    if not path.exists():
        if required:
            raise SystemExit(f"pipeline-status: missing {path}")
        return {}
    if not path.is_file():
        raise SystemExit(f"pipeline-status: {path} is not a regular file")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, TypeError) as exc:
        raise SystemExit(f"pipeline-status: unreadable/invalid {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"pipeline-status: {path} is not a JSON object")
    return data


def _require_list_field(doc: dict[str, Any], key: str, path: Path) -> list[Any]:
    value = doc.get(key)
    if not isinstance(value, list):
        raise SystemExit(
            f"pipeline-status: {path} missing list field {key!r}"
        )
    return value


def _require_dict_field(doc: dict[str, Any], key: str, path: Path) -> dict[str, Any]:
    value = doc.get(key)
    if not isinstance(value, dict):
        raise SystemExit(
            f"pipeline-status: {path} missing object field {key!r}"
        )
    return value


def _nogo_reason(payload: dict[str, Any]) -> str:
    basis = str(payload.get("decision_basis") or "")
    if basis == "author_auto":
        return "auto-nogo"
    for cond in payload.get("conditions") or []:
        if isinstance(cond, dict) and cond.get("met") is False:
            cid = str(cond.get("id") or "").strip()
            if cid:
                return cid
    return basis or "unspecified"


def _latest_mine_day_drain(candidates: list[Any]) -> dict[str, Any]:
    """Admits on the latest ``first_seen`` UTC date (artifact clock, not wall yesterday)."""
    dates: list[str] = []
    by_date: Counter[str] = Counter()
    for cand in candidates:
        if not isinstance(cand, dict):
            continue
        seen = str(cand.get("first_seen") or "").strip()
        if len(seen) < 10:
            continue
        day = seen[:10]
        dates.append(day)
        by_date[day] += 1
    if not dates:
        return {"date": None, "admitted": 0}
    latest = max(dates)
    return {"date": latest, "admitted": int(by_date[latest])}


def _needs_human(candidates: list[Any]) -> int:
    n = 0
    for cand in candidates:
        if not isinstance(cand, dict):
            continue
        audit = cand.get("audit") if isinstance(cand.get("audit"), dict) else {}
        if audit.get("needs_human_review") is True:
            n += 1
    return n


def _nogo_counts(gen: Path) -> dict[str, int]:
    counts: Counter[str] = Counter()
    if not gen.is_dir():
        return {}
    for path in sorted(gen.glob("*_gate_decision.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError, TypeError):
            continue
        if not isinstance(payload, dict):
            continue
        status = str(payload.get("status") or payload.get("decision") or "")
        if status != "no-go":
            continue
        counts[_nogo_reason(payload)] += 1
    return dict(counts.most_common())


def _escape(state_path: Path, gen: Path, baseline: Path) -> dict[str, Any]:
    return escape_window.escape_window(
        state_path=state_path,
        gen=gen,
        baseline_path=baseline,
    )


def _format_rate(rate: Any) -> str:
    return f"{rate:.4f}" if isinstance(rate, (int, float)) else "n/a"


def _drain_line(drain: dict[str, Any]) -> str:
    base = f"latest mine-day drain: {drain.get('admitted', 0)} ledger admits"
    if drain.get("date"):
        return f"{base} (UTC {drain.get('date')})"
    return base


def snapshot(
    *,
    generated: Path | None = None,
    state_path: Path | None = None,
    ledger_path: Path | None = None,
    queue_path: Path | None = None,
    conversion_ledger: Path | None = None,
    baseline_path: Path | None = None,
) -> dict[str, Any]:
    gen = generated if generated is not None else GEN
    conv_path = conversion_ledger if conversion_ledger is not None else LEDGER_JSON
    conv = _load_json(conv_path, required=True)
    starvation = _require_dict_field(conv, "starvation", conv_path)
    hops = _require_list_field(conv, "per_wave", conv_path)
    ledger_p = ledger_path if ledger_path is not None else CANDIDATE_LEDGER
    cand_doc = _load_json(ledger_p, required=True)
    candidates = _require_list_field(cand_doc, "candidates", ledger_p)
    queue_p = queue_path if queue_path is not None else QUEUE_PATH
    queue_doc = _load_json(queue_p, required=True)
    items = _require_list_field(queue_doc, "items", queue_p)
    state = state_path if state_path is not None else (ROOT / "batch" / "state.json")
    proj = batch_state.projection(state)
    baseline = baseline_path if baseline_path is not None else BASELINE_PATH
    esc = _escape(state, gen, baseline)
    nogo = _nogo_counts(gen)
    drain = _latest_mine_day_drain(candidates)
    return {
        "latest_mine_day_drain": drain,
        "queue_pressure": starvation.get("mine_queue_pressure"),
        "queue_len": starvation.get("mine_queue_len", len(items)),
        "queue_cap": starvation.get("mine_queue_cap"),
        "week_survival": {
            "n": esc.get("n_window"),
            "k": esc.get("k_window"),
            "rate": esc.get("rate"),
            "baseline": esc.get("baseline"),
            "fires": esc.get("fires"),
        },
        "backlog_weeks": starvation.get("backlog_weeks"),
        "demand_open": starvation.get("demand_open_gated_go_no_closed_wave"),
        "admission_per_week": starvation.get("admission_per_week"),
        "needs_human_backlog": _needs_human(candidates),
        "nogo_by_reason": nogo,
        "nogo_dominant": next(iter(nogo), None),
        "probe_projection": proj,
        "hops": [
            {
                "wave_id": w.get("wave_id"),
                "idiom_bucket": w.get("idiom_bucket"),
                "asked": w.get("properties_asked"),
                "sat": w.get("properties_sat"),
                "gt": w.get("sat_ground_truthed"),
                "filed": w.get("filed"),
                "accepted": w.get("accepted"),
            }
            for w in hops
            if isinstance(w, dict)
        ],
    }


def render_status(snap: dict[str, Any]) -> str:
    drain = snap.get("latest_mine_day_drain") or {}
    week = snap.get("week_survival") or {}
    rate_s = _format_rate(week.get("rate"))
    lines = [
        "regexproof pipeline status",
        _drain_line(drain),
        f"queue pressure: {snap.get('queue_pressure')} "
        f"({snap.get('queue_len')}/{snap.get('queue_cap')})",
        f"this week's survival: k={week.get('k')} / n={week.get('n')} "
        f"rate={rate_s} baseline={week.get('baseline')} fires={week.get('fires')}",
        f"backlog weeks: {snap.get('backlog_weeks')} "
        f"(demand_open={snap.get('demand_open')}, "
        f"admission_per_week={snap.get('admission_per_week')})",
        f"needs_human backlog: {snap.get('needs_human_backlog')}",
        f"NO-GO dominant reason: {snap.get('nogo_dominant') or 'n/a'}",
    ]
    return "\n".join(lines) + "\n"


def render_weekly(snap: dict[str, Any]) -> str:
    """Markdown block for the daily-mine job summary (no side effects)."""
    drain = snap.get("latest_mine_day_drain") or {}
    week = snap.get("week_survival") or {}
    nogo = snap.get("nogo_by_reason") or {}
    nogo_lines = ", ".join(f"{k}={v}" for k, v in list(nogo.items())[:8]) or "none"
    rate_s = _format_rate(week.get("rate"))
    return "\n".join(
        [
            "### What changed this week",
            "",
            f"- probed (7-day window): `{week.get('n')}`",
            f"- survivor trend: k=`{week.get('k')}` rate=`{rate_s}` "
            f"baseline=`{week.get('baseline')}` fires=`{week.get('fires')}`",
            f"- NO-GO by dominant reason: {nogo_lines}",
            f"- needs_human backlog: `{snap.get('needs_human_backlog')}`",
            f"- backlog weeks: `{snap.get('backlog_weeks')}`",
            f"- latest mine-day drain: `{drain.get('admitted', 0)}` "
            f"(UTC `{drain.get('date')}`)",
            "",
        ]
    )
