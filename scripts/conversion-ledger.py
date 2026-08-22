#!/usr/bin/env python3
"""Aggregate scanner / rule_diff / upstream artifacts into a conversion ledger.

Heap's-law / singleton novelty saturates compiler coverage (new reject buckets,
new pattern types). This measure is the *product* funnel: sites → properties
asked → SAT → ground-truthed → disclosed → accepted upstream.

Input:
  properties/generated/*_batch_summary.json
  properties/generated/<corpus>.ndjson          (scanner findings)
  properties/generated/*-pr-dry-run.json
  properties/generated/*_rule_diff_report.json
  docs/conversion-upstream.jsonl                (human-curated last mile)
Output:
  properties/generated/conversion-ledger.{json,md}

Observational only. Regenerated in the golden CI job; drift fails the job.
Do not treat TIMEOUT / unknown as a pass. Toolkit VF-* rows in
docs/verified-findings.jsonl are out of this ledger (implementation traps,
not vulnerability counts).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

GEN_DIR = ROOT / "properties" / "generated"
UPSTREAM_PATH = ROOT / "docs" / "conversion-upstream.jsonl"
JSON_OUT = GEN_DIR / "conversion-ledger.json"
MD_OUT = GEN_DIR / "conversion-ledger.md"

SCHEMA_VERSION = "1"

PRODUCT_KINDS = frozenset(
    {"property", "counterexample_finder", "bug_demo", "rule_diff"}
)
CLASSIFICATION_KINDS = frozenset({"usage_mismatch", "intent_mismatch", "triage"})
HYGIENE_KINDS = frozenset({"mutation_guard"})
REDOS_KINDS = frozenset({"redos"})

SAT_RESULTS = frozenset({"sat", "gap"})
UNSAT_RESULTS = frozenset({"unsat"})
GT_PASS = frozenset({"reproduced", "PASS"})
RULE_DIFF_REPORT_GLOB = "*_rule_diff_report.json"
BATCH_SHAPE5_GLOB = "*_batch_shape5.json"
# Decided batch shape-5 outcomes that count as a property asked (#477).
BATCH_SHAPE5_ASKED = frozenset({"sat", "unsat", "sat_fullmatch_only"})
BATCH_SHAPE5_SAT = frozenset({"sat"})

# --- #554 Phase A: wave join keys, hop table, starvation -------------------
# Disposition statuses that mean the finding was actually filed somewhere.
FILED_STATUSES = frozenset({"filed", "private_first", "fixed_upstream"})
ACCEPTED_STATUSES = frozenset({"fixed_upstream"})
WAVE_FALLBACK = "(no wave)"
BUCKET_FALLBACK = "(no bucket)"
STARVATION_WINDOW_DAYS = 7
CLOSED_WAVE_GLOB = "*_conversion_wave.md"


def canonical_site(site: str) -> str:
    """Join-key canonicalization for ``site`` (#554; see checker docstring).

    Strip whitespace. URL-shaped sites get scheme+hostname lowercased with the
    remainder verbatim; everything else compares verbatim (repo-relative
    paths are case-sensitive).
    """
    s = str(site or "").strip()
    if "://" in s:
        scheme, rest = s.split("://", 1)
        host_sep = rest.find("/")
        if host_sep == -1:
            return f"{scheme.lower()}://{rest.lower()}"
        return f"{scheme.lower()}://{rest[:host_sep].lower()}{rest[host_sep:]}"
    return s


def canonical_question_id(rec: dict[str, Any]) -> str:
    """Exact-string ``question_id``; scanner rows fall back to ``name``."""
    qid = rec.get("question_id") or rec.get("name") or ""
    return str(qid).strip()


def wave_key(rec: dict[str, Any]) -> tuple[str, str]:
    """Top-level ``(wave_id, idiom_bucket)`` aggregation key with fallbacks."""
    return (
        str(rec.get("wave_id") or "").strip() or WAVE_FALLBACK,
        str(rec.get("idiom_bucket") or "").strip() or BUCKET_FALLBACK,
    )


def upstream_join_index(upstream_rows: list[dict[str, Any]]) -> dict[tuple[str, str], dict[str, Any]]:
    """Index curated rows on canonical ``(site, question_id)``."""
    index: dict[tuple[str, str], dict[str, Any]] = {}
    for row in upstream_rows:
        site = canonical_site(str(row.get("site") or ""))
        qid = str(row.get("question_id") or "").strip()
        if site and qid:
            index[(site, qid)] = row
    return index


def classify_wave_rows(rows: list[dict[str, Any]]) -> dict[tuple[str, str], dict[str, Any]]:
    """Per-(wave_id, idiom_bucket) funnel buckets + property-shape mix."""
    waves: dict[tuple[str, str], dict[str, Any]] = {}
    for rec in rows:
        if not counts_as_conversion_asked(rec):
            continue
        key = wave_key(rec)
        w = waves.setdefault(
            key,
            {
                "wave_id": key[0],
                "idiom_bucket": key[1],
                "corpora": sorted({str(rec.get("corpus") or "")} - {""}),
                "properties_asked": 0,
                "properties_sat": 0,
                "sat_ground_truthed": 0,
                "filed": 0,
                "accepted": 0,
                "shape_counts": {},
            },
        )
        corp = str(rec.get("corpus") or "")
        if corp and corp not in w["corpora"]:
            w["corpora"].append(corp)
            w["corpora"].sort()
        w["properties_asked"] += 1
        shape = rec.get("shape")
        if isinstance(shape, int):
            w["shape_counts"][str(shape)] = int(w["shape_counts"].get(str(shape) , 0)) + 1
        if rec.get("result") in SAT_RESULTS:
            w["properties_sat"] += 1
            if is_ground_truthed(rec):
                w["sat_ground_truthed"] += 1
    return waves


def join_wave_dispositions(
    waves: dict[tuple[str, str], dict[str, Any]],
    rows: list[dict[str, Any]],
    upstream_index: dict[tuple[str, str], dict[str, Any]],
) -> None:
    """Fill ``filed`` / ``accepted`` per wave from curated dispositions.

    Join runs over ground-truth-confirmed SAT rows (filing happens after GT).
    ``filed`` = curated status says filed somewhere (``filed`` /
    ``private_first`` / ``fixed_upstream``) or an explicit ``filed_at``;
    ``accepted`` = ``fixed_upstream``.
    """
    for rec in rows:
        if not counts_as_conversion_asked(rec):
            continue
        if rec.get("result") not in SAT_RESULTS or not is_ground_truthed(rec):
            continue
        row = upstream_index.get(
            (canonical_site(str(rec.get("site") or "")), canonical_question_id(rec))
        )
        if row is None:
            continue
        key = wave_key(rec)
        w = waves.get(key)
        if w is None:
            continue
        status = str(row.get("status") or "")
        if status in FILED_STATUSES or row.get("filed_at"):
            w["filed"] += 1
        if status in ACCEPTED_STATUSES:
            w["accepted"] += 1


# Canonical repo → corpus mapping for wave-close-out matching. The close-out
# artifacts are named <corpus>_conversion_wave.md, where <corpus> is the
# canonical corpus id (e.g. openwrt_packages), NOT the last URL path segment
# (e.g. packages). Repos with wave machinery must be mapped explicitly so the
# starvation demand signal does not count closed waves as open.
CANONICAL_CORPUS_BY_REPO = {
    "openwrt/packages": "openwrt_packages",
    "openwrt/luci": "openwrt_luci",
}


def corpus_key_from_url(url: str) -> str:
    """Mine-cluster identity: canonical corpus id, else lowercased last path
    segment minus .git (fallback for non-wave corpora)."""
    u = str(url or "").strip().rstrip("/")
    # repo identity = last TWO path segments (owner/name), e.g.
    # openwrt/packages — matches the canonical mapping keys.
    parts = u.rsplit("/", 2)[-2:] if u else []
    repo = "/".join(parts) if len(parts) == 2 else (parts[0] if parts else "")
    repo = repo.removesuffix(".git") if repo else ""
    if repo in CANONICAL_CORPUS_BY_REPO:
        return CANONICAL_CORPUS_BY_REPO[repo]
    return repo.rsplit("/", 1)[-1].lower()


def closed_wave_corpora(gen_dir: Path) -> set[str]:
    """Corpora with a committed conversion-wave close-out artifact."""
    return {
        p.name[: -len("_conversion_wave.md")]
        for p in gen_dir.glob(CLOSED_WAVE_GLOB)
    }


def load_go_decision_dates(gen_dir: Path) -> list[str]:
    """ISO decision dates of committed GO gate decisions (admission flow).

    Sourced from gate-decision ARTIFACTS, not the lagging candidate ledger
    (#554): every ``*_gate_decision.json`` with ``decision == "go"``
    contributes its ``decision_date``.
    """
    dates: list[str] = []
    for path in sorted(gen_dir.glob("*_gate_decision.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if str(data.get("decision") or "") == "go":
            date = str(data.get("decision_date") or "").strip()
            if date:
                dates.append(date)
    return dates


def admission_per_week(
    go_dates: list[str], window_days: int = STARVATION_WINDOW_DAYS
) -> tuple[int, str | None]:
    """GO admissions in the most recent complete 7-day window.

    Window end = latest committed GO ``decision_date`` (artifact clock, not
    wall clock, so regeneration is deterministic). Returns ``(count, window_end)``.
    """
    if not go_dates:
        return 0, None
    parsed = []
    for d in go_dates:
        try:
            parsed.append(date.fromisoformat(d[:10]))
        except ValueError:
            continue
    if not parsed:
        return 0, None
    end = max(parsed)
    start = end - timedelta(days=window_days - 1)
    count = sum(1 for d in parsed if start <= d <= end)
    return count, end.isoformat()


def starvation_metrics(
    gen_dir: Path,
    mine_ledger_path: Path,
    queue_path: Path | None = None,
    prior_history: list[dict[str, Any]] | None = None,
    queue_cap: int | None = None,
) -> dict[str, Any]:
    """Backlog_weeks stock/flow signal + mine queue pressure (#554).

    ``backlog_weeks = demand_open / admission_per_week`` where demand (stock)
    = open ``gated:go`` clusters lacking a closed wave (candidate ledger) and
    admission (flow) = GO gate-decision artifacts per 7-day window. Bounded by
    the ~10/day mine cap by design — read alongside ``mine_queue_pressure``,
    not as batch health. Alert when ``backlog_weeks`` rises for >= 2
    consecutive windows (history carried in this artifact between runs).
    """
    if queue_cap is None:
        from regexproof.mine.queue import DEFAULT_QUEUE_CAP

        queue_cap = DEFAULT_QUEUE_CAP
    go_dates = load_go_decision_dates(gen_dir)
    admission, window_end = admission_per_week(go_dates)

    closed = {c.lower() for c in closed_wave_corpora(gen_dir)}
    demand_open = 0
    if mine_ledger_path.is_file():
        try:
            ledger = json.loads(mine_ledger_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            ledger = {}
        seen: set[str] = set()
        for cand in ledger.get("candidates") or []:
            if str(cand.get("status") or "") != "gated:go":
                continue
            url = str(cand.get("url") or "")
            if url in seen:
                continue
            seen.add(url)
            if corpus_key_from_url(url) not in closed:
                demand_open += 1

    backlog_weeks: float | None = None
    if admission > 0:
        backlog_weeks = round(demand_open / admission, 4)

    queue_len = 0
    if queue_path is None:
        queue_path = gen_dir / "mine-queue.json"
    if queue_path.is_file():
        try:
            queue = json.loads(queue_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            queue = {}
        items = queue.get("items")
        if isinstance(items, list):
            queue_len = len(items)
    mine_queue_pressure = round(queue_len / queue_cap, 4) if queue_cap else None

    history = list(prior_history or [])
    if window_end is not None and (not history or history[-1].get("week_end") != window_end):
        history.append(
            {
                "week_end": window_end,
                "demand_open": demand_open,
                "admission_per_week": admission,
                "backlog_weeks": backlog_weeks,
            }
        )
    consecutive_rises = 0
    values = [h.get("backlog_weeks") for h in history]
    for i in range(len(values) - 1, 0, -1):
        prev, cur = values[i - 1], values[i]
        if prev is not None and cur is not None and cur > prev:
            consecutive_rises += 1
        else:
            break
    alert = consecutive_rises >= 2

    return {
        "demand_open_gated_go_no_closed_wave": demand_open,
        "admission_per_week": admission,
        "admission_window_days": STARVATION_WINDOW_DAYS,
        "admission_window_end": window_end,
        "backlog_weeks": backlog_weeks,
        "formula": "backlog_weeks = demand_open / admission_per_week",
        "mine_queue_pressure": mine_queue_pressure,
        "mine_queue_len": queue_len,
        "mine_queue_cap": queue_cap,
        "history": history,
        "alert_backlog_increasing": alert,
        "consecutive_increases": consecutive_rises,
    }


def contract_queue_health(gen_dir: Path, clock_iso: str | None = None) -> dict[str, Any]:
    """Contract-queue stub states (Phase C artifacts; absent today).

    Counts ``properties/conversion_queue/*.json`` by ``status`` and reports
    median stub age in days when a ``created_at`` timestamp exists. Age is
    computed against the committed artifact clock (the admission window end)
    so repeated regeneration is byte-deterministic — never ``datetime.now()``.
    The queue owns only pre-contract states; later states are derived joins
    (#551 C).
    """
    queue_dir = gen_dir.parent / "conversion_queue"
    counts = {"emitted": 0, "claimed": 0, "contracted": 0, "skipped": 0}
    ages: list[float] = []
    present = queue_dir.is_dir()
    if present:
        for path in sorted(queue_dir.glob("*.json")):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            status = str(data.get("status") or "")
            if status == "contracted":
                counts["contracted"] += 1
            elif status.startswith("skipped"):
                counts["skipped"] += 1
            elif status == "claimed":
                counts["claimed"] += 1
            elif status in {"emitted", "unassigned"}:
                counts["emitted"] += 1
            created = str(data.get("created_at") or "")
            if created and clock_iso:
                try:
                    # Normalize to naive UTC: created_at may carry an offset
                    # (…Z) while the artifact clock is a plain ISO date.
                    clock = datetime.fromisoformat(clock_iso)
                    created_dt = datetime.fromisoformat(created)
                    if created_dt.tzinfo is not None:
                        created_dt = created_dt.astimezone(timezone.utc).replace(
                            tzinfo=None
                        )
                    if clock.tzinfo is not None:
                        clock = clock.astimezone(timezone.utc).replace(tzinfo=None)
                    ages.append((clock - created_dt).total_seconds() / 86400)
                except ValueError:
                    pass
    if ages:
        ages_sorted = sorted(ages)
        n = len(ages_sorted)
        mid = n // 2
        median_age = (
            ages_sorted[mid]
            if n % 2
            else (ages_sorted[mid - 1] + ages_sorted[mid]) / 2
        )
        median_age = round(median_age, 2)
    else:
        median_age = None
    return {
        "artifacts_present": present,
        **counts,
        "median_age_days": median_age,
        "note": "" if present else "Phase C queue artifacts not yet shipped",
    }



def _load_security_tool_corpora() -> frozenset[str]:
    """Load SECURITY_TOOL_CORPORA without importing regexproof.batch (jsonschema)."""
    path = ROOT / "regexproof" / "batch" / "disclose.py"
    spec = importlib.util.spec_from_file_location("_rp_disclose", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return frozenset(mod.SECURITY_TOOL_CORPORA)


def is_scanner_ndjson(path: Path) -> bool:
    """True for batch scanner ``<corpus>.ndjson``, not inventories/probes/triage.

    Java sidecar probes are ``*_triage.ndjson`` / ``*-triage.ndjson``. Do not
    treat the substring ``triage`` as a ban — a corpus named ``triager`` is a
    valid scanner file.
    """
    name = path.name
    if not name.endswith(".ndjson"):
        return False
    stem = name[: -len(".ndjson")]
    if "-inventory" in stem or "frozen-ids" in stem:
        return False
    return not stem.endswith(("_triage", "-triage"))


def is_planned(rec: dict[str, Any]) -> bool:
    if rec.get("result") == "planned":
        return True
    rid = str(rec.get("regex_id") or "")
    return rid.startswith("inventory:")


def is_product_sat(rec: dict[str, Any]) -> bool:
    return rec.get("kind") in PRODUCT_KINDS and rec.get("result") in SAT_RESULTS


def is_ground_truthed(rec: dict[str, Any]) -> bool:
    if rec.get("ground_truth_status") in GT_PASS:
        return True
    gt = rec.get("ground_truth")
    if not isinstance(gt, dict):
        return False
    if gt.get("status") in GT_PASS:
        return True
    engines = [
        v
        for v in gt.values()
        if isinstance(v, dict) and "status" in v and "replay" in v
    ]
    return bool(engines) and all(e.get("status") in GT_PASS for e in engines)


def _ratio(num: int, den: int) -> float | None:
    if den == 0:
        return None
    return round(num / den, 6)


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _iter_ndjson(path: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        out.append(json.loads(line))
    return out


def load_upstream(path: Path | None = None) -> list[dict[str, Any]]:
    p = path if path is not None else UPSTREAM_PATH
    rows = _iter_ndjson(p)
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise ValueError(f"duplicate conversion-upstream id in {p}")
    return rows


def counts_as_conversion_asked(rec: dict[str, Any]) -> bool:
    """Conversion-wave rows count only when product_reportable + human.

    Kind alone would count smoke (agent_derived / incomplete contract).
    """
    from regexproof.harness.contract import product_reportable

    if rec.get("synthesized"):
        return False
    contract = rec.get("contract")
    if not isinstance(contract, dict) or str(contract.get("provenance") or "") != "human":
        return False
    return product_reportable(
        {
            "kind": rec.get("kind"),
            "domain": rec.get("domain"),
            "contract": contract,
        }
    )


# Conversion NDJSON joins asked/SAT/GT only. Do not merge scanner-inventory
# counters — those must stay equal to batch_summary findings.
_CONVERSION_FUNNEL_KEYS = (
    "properties_asked",
    "properties_asked_synthesized",
    "properties_asked_distinct",
    "properties_unsat",
    "properties_sat",
    "properties_sat_synthesized",
    "properties_sat_distinct",
    "sat_ground_truthed",
    "sat_unique_sites",
)


def classify_conversion_rows(rows: list[dict[str, Any]]) -> dict[str, int]:
    """Funnel buckets for ``*_conversion.ndjson`` (product_reportable gate)."""
    counts: Counter[str] = Counter(
        {
            "properties_asked": 0,
            "properties_asked_synthesized": 0,
            "properties_asked_distinct": 0,
            "properties_unsat": 0,
            "properties_sat": 0,
            "properties_sat_synthesized": 0,
            "properties_sat_distinct": 0,
            "sat_ground_truthed": 0,
            "sat_unique_sites": 0,
        }
    )
    sat_sites: set[tuple[str, str, str]] = set()
    asked_pairs: set[tuple[str, str]] = set()
    sat_pairs: set[tuple[str, str]] = set()
    for rec in rows:
        if not counts_as_conversion_asked(rec):
            continue
        qid = rec.get("question_id") or rec.get("name") or ""
        pair = (str(rec.get("site") or ""), str(qid))
        counts["properties_asked"] += 1
        asked_pairs.add(pair)
        result = rec.get("result")
        if result in UNSAT_RESULTS:
            counts["properties_unsat"] += 1
        elif result in SAT_RESULTS:
            counts["properties_sat"] += 1
            sat_pairs.add(pair)
            sat_sites.add(
                (
                    str(rec.get("corpus") or ""),
                    str(rec.get("regex_id") or ""),
                    str(rec.get("site") or ""),
                )
            )
            if is_ground_truthed(rec):
                counts["sat_ground_truthed"] += 1
    counts["sat_unique_sites"] = len(sat_sites)
    counts["properties_asked_distinct"] = len(asked_pairs)
    counts["properties_sat_distinct"] = len(sat_pairs)
    return dict(counts)


def scanner_ndjson_files(gen_dir: Path) -> list[Path]:
    """Batch scanner NDJSON: ``<corpus>.ndjson`` with a matching batch summary.

    Excludes inventories, frozen-id snapshots, Java-triage probes, and
    sidecar finding dumps (``crs_cross_engine_findings.ndjson``) whose SAT
    rows are counted from ``*_rule_diff_report.json`` instead.
    """
    summaries = {
        p.name[: -len("_batch_summary.json")]
        for p in gen_dir.glob("*_batch_summary.json")
        if p.name != "batch_summary.json"
    }
    out: list[Path] = []
    for path in sorted(gen_dir.glob("*.ndjson")):
        if not is_scanner_ndjson(path):
            continue
        stem = path.name[: -len(".ndjson")]
        if stem in summaries:
            out.append(path)
    # Special-case conversion-wave join: independent of a matching batch summary.
    # Do not broaden to a generic *.ndjson scan.
    for path in sorted(gen_dir.glob("*_conversion.ndjson")):
        if path not in out:
            out.append(path)
    return out


def classify_scanner_rows(
    rows: list[dict[str, Any]],
) -> dict[str, int]:
    """Count one scanner-NDJSON corpus (or a fixture list) into funnel buckets."""
    counts: Counter[str] = Counter(
        {
            "scanner_rows": 0,
            "planned_stubs": 0,
            "classification_rows": 0,
            "mutation_guards": 0,
            "redos_rows": 0,
            "other_rows": 0,
            "properties_asked": 0,
            "properties_asked_synthesized": 0,
            "properties_asked_distinct": 0,
            "properties_unsat": 0,
            "properties_sat": 0,
            "properties_sat_synthesized": 0,
            "properties_sat_distinct": 0,
            "scanner_rule_diff_sat": 0,
            "sat_ground_truthed": 0,
        }
    )
    sat_sites: set[tuple[str, str, str]] = set()
    asked_pairs: set[tuple[str, str]] = set()
    sat_pairs: set[tuple[str, str]] = set()
    for rec in rows:
        counts["scanner_rows"] += 1
        kind = rec.get("kind") or ""
        result = rec.get("result")
        if is_planned(rec):
            counts["planned_stubs"] += 1
            continue
        if kind in CLASSIFICATION_KINDS:
            counts["classification_rows"] += 1
            continue
        if kind in HYGIENE_KINDS:
            counts["mutation_guards"] += 1
            continue
        if kind in REDOS_KINDS:
            counts["redos_rows"] += 1
            continue
        if kind in PRODUCT_KINDS:
            qid = rec.get("question_id")
            if not qid and isinstance(rec.get("detail"), dict):
                qid = rec["detail"].get("question_id")
            pair = (str(rec.get("site") or ""), str(qid or ""))
            if rec.get("synthesized"):
                # Untargeted shape-1/2 synthesis is compiler smoke, not product (#479).
                counts["properties_asked_synthesized"] += 1
                if result in SAT_RESULTS:
                    counts["properties_sat_synthesized"] += 1
                continue
            counts["properties_asked"] += 1
            asked_pairs.add(pair)
            if result in UNSAT_RESULTS:
                counts["properties_unsat"] += 1
            elif result in SAT_RESULTS:
                counts["properties_sat"] += 1
                sat_pairs.add(pair)
                if kind == "rule_diff":
                    counts["scanner_rule_diff_sat"] += 1
                sat_sites.add(
                    (
                        str(rec.get("corpus") or ""),
                        str(rec.get("regex_id") or ""),
                        str(rec.get("site") or ""),
                    )
                )
                if is_ground_truthed(rec):
                    counts["sat_ground_truthed"] += 1
            continue
        counts["other_rows"] += 1
    counts["sat_unique_sites"] = len(sat_sites)
    counts["properties_asked_distinct"] = len(asked_pairs)
    counts["properties_sat_distinct"] = len(sat_pairs)
    return dict(counts)


def _count_disclosure(rows: list[dict[str, Any]]) -> tuple[int, int]:
    private = 0
    public_ok = 0
    for rec in rows:
        if is_planned(rec):
            continue
        if rec.get("kind") not in PRODUCT_KINDS | CLASSIFICATION_KINDS:
            continue
        d = rec.get("disclosure")
        if d == "private_first":
            private += 1
        elif d == "public_ok":
            public_ok += 1
    return private, public_ok


def _summarize_rule_diff_report(path: Path) -> dict[str, int]:
    data = _read_json(path)
    results = data.get("results") or []
    sat = 0
    sat_gt = 0
    unsat = 0
    guards = 0
    for rec in results:
        kind = rec.get("kind")
        result = rec.get("result")
        if kind == "mutation_guard":
            guards += 1
            continue
        if kind != "rule_diff":
            continue
        if result in SAT_RESULTS:
            sat += 1
            if is_ground_truthed(rec):
                sat_gt += 1
        elif result in UNSAT_RESULTS:
            unsat += 1
    return {
        "rows": len(results),
        "rule_diff_sat": sat,
        "rule_diff_sat_gt": sat_gt,
        "rule_diff_unsat": unsat,
        "mutation_guards": guards,
    }


def summarize_batch_shape5(path: Path) -> dict[str, int]:
    """Count decided batch shape-5 rows as product properties asked (#477)."""
    data = _read_json(path)
    rows = data.get("rows") if isinstance(data, dict) else None
    if not isinstance(rows, list):
        rows = []
    asked = 0
    sat = 0
    sat_gt = 0
    unsat = 0
    fullmatch_only = 0
    for rec in rows:
        if not isinstance(rec, dict):
            continue
        result = rec.get("result")
        if result not in BATCH_SHAPE5_ASKED:
            continue
        asked += 1
        if result in BATCH_SHAPE5_SAT:
            sat += 1
            if is_ground_truthed(rec):
                sat_gt += 1
        elif result in UNSAT_RESULTS:
            unsat += 1
        elif result == "sat_fullmatch_only":
            fullmatch_only += 1
    return {
        "properties_asked": asked,
        "properties_sat": sat,
        "properties_sat_gt": sat_gt,
        "properties_unsat": unsat,
        "sat_fullmatch_only": fullmatch_only,
        "executed_rows": len(rows),
    }


def _upstream_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    by_status: Counter[str] = Counter()
    lang = 0
    for rec in rows:
        by_status[str(rec.get("status") or "")] += 1
        if rec.get("language_membership"):
            lang += 1
    return {
        "rows": len(rows),
        "language_membership": lang,
        "fixed_upstream": by_status["fixed_upstream"],
        "filed_plan": by_status["filed_plan"],
        "false_positive": by_status["false_positive"],
        "out_of_scope_redos": by_status["out_of_scope_redos"],
        "private_first": by_status["private_first"],
        "wont_file": by_status["wont_file"],
        "accepted_upstream": by_status["fixed_upstream"],
        "existence_proofs": by_status["fixed_upstream"] + by_status["private_first"],
        "third_party_public": 0,
    }



def _is_yara_fraction(data: dict[str, Any], stem: str) -> bool:
    dialect = str(data.get("dialect") or "")
    if dialect == "yara":
        return True
    name = str(data.get("pilot") or data.get("corpus") or stem).lower()
    return "yara" in name


def yara_encodable_split(gen: Path) -> dict[str, Any]:
    """Encodable fraction with and without YARA corpora (#492)."""
    all_n = 0
    all_ok = 0
    yara_n = 0
    yara_ok = 0
    all_unenc_reasons: Counter[str] = Counter()
    yara_unenc_reasons: Counter[str] = Counter()
    for path in sorted(gen.glob("*_encodable_fraction.json")):
        data = _read_json(path)
        n = int(data.get("sample_size") or 0)
        ok = int(data.get("encodable") or 0)
        if n <= 0:
            continue
        reasons = data.get("reasons") or {}
        unenc: Counter[str] = Counter()
        for key, val in reasons.items():
            if key == "ok":
                continue
            unenc[str(key)] += int(val or 0)
        all_n += n
        all_ok += ok
        all_unenc_reasons.update(unenc)
        stem = path.name.replace("_encodable_fraction.json", "")
        if _is_yara_fraction(data, stem):
            yara_n += n
            yara_ok += ok
            yara_unenc_reasons.update(unenc)
    all_unenc = all_n - all_ok
    yara_unenc = yara_n - yara_ok
    non_yara_n = all_n - yara_n
    non_yara_ok = all_ok - yara_ok
    fw_all = int(all_unenc_reasons.get("fullword-boundary") or 0)
    fw_yara = int(yara_unenc_reasons.get("fullword-boundary") or 0)
    return {
        "fraction_all_n": all_n,
        "fraction_all_encodable": all_ok,
        "fraction_yara_n": yara_n,
        "fraction_yara_encodable": yara_ok,
        "fraction_excluding_yara_n": non_yara_n,
        "fraction_excluding_yara_encodable": non_yara_ok,
        "unencodable_all": all_unenc,
        "unencodable_yara": yara_unenc,
        "fullword_boundary_all": fw_all,
        "fullword_boundary_yara": fw_yara,
        "encodable_fraction_all": _ratio(all_ok, all_n),
        "encodable_fraction_excluding_yara": _ratio(non_yara_ok, non_yara_n),
        "encodable_fraction_yara": _ratio(yara_ok, yara_n),
        "yara_share_of_unencodable": _ratio(yara_unenc, all_unenc),
        "fullword_share_of_unencodable": _ratio(fw_all, all_unenc),
        "fullword_share_of_yara_unencodable": _ratio(fw_yara, yara_unenc),
    }


def aggregate(
    *,
    gen_dir: Path | None = None,
    upstream_path: Path | None = None,
    security_tools: frozenset[str] | None = None,
    mine_ledger_path: Path | None = None,
    queue_path: Path | None = None,
    prior_starvation_history: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    gen = gen_dir if gen_dir is not None else GEN_DIR
    tools = security_tools if security_tools is not None else _load_security_tool_corpora()
    upstream_rows = load_upstream(upstream_path)

    extracted = 0
    encodable = 0
    summary_findings = 0
    summary_triage = 0
    n_summaries = 0
    for path in sorted(gen.glob("*_batch_summary.json")):
        data = _read_json(path)
        if "extracted" not in data:
            continue
        n_summaries += 1
        extracted += int(data.get("extracted") or 0)
        encodable += int(data.get("encodable") or 0)
        summary_findings += int(data.get("findings") or 0)
        summary_triage += int(data.get("triage") or 0)

    scanner_files = scanner_ndjson_files(gen)
    all_rows: list[dict[str, Any]] = []
    conversion_rows: list[dict[str, Any]] = []
    per_corpus: dict[str, list[dict[str, Any]]] = defaultdict(list)
    conversion_by_corpus: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path in scanner_files:
        rows = _iter_ndjson(path)
        if path.name.endswith("_conversion.ndjson"):
            conversion_rows.extend(rows)
            for rec in rows:
                conversion_by_corpus[str(rec.get("corpus") or path.stem)].append(rec)
        else:
            all_rows.extend(rows)
            for rec in rows:
                per_corpus[str(rec.get("corpus") or path.stem)].append(rec)

    classified = classify_scanner_rows(all_rows)
    conv = classify_conversion_rows(conversion_rows)
    for key in _CONVERSION_FUNNEL_KEYS:
        classified[key] = int(classified.get(key) or 0) + int(conv.get(key) or 0)
    private, public_ok = _count_disclosure(all_rows + conversion_rows)
    yara = yara_encodable_split(gen)

    dry_runs = 0
    dry_findings = 0
    dry_private = 0
    would_open = 0
    for path in sorted(gen.glob("*-pr-dry-run.json")):
        data = _read_json(path)
        dry_runs += 1
        dry_findings += int(data.get("finding_count") or 0)
        dry_private += int(data.get("private_first_count") or 0)
        if data.get("would_open_public_upstream_issue"):
            would_open += 1

    rule_diff: dict[str, dict[str, int]] = {}
    rd_sat = 0
    rd_sat_gt = 0
    for path in sorted(gen.glob(RULE_DIFF_REPORT_GLOB)):
        summary = _summarize_rule_diff_report(path)
        rule_diff[path.name] = summary
        rd_sat += summary["rule_diff_sat"]
        rd_sat_gt += summary["rule_diff_sat_gt"]

    # Scanner NDJSON already has some rule_diff rows (result=gap). Dedicated
    # reports are extra sources; do not add them into properties_asked.
    # Batch shape-5 JSON (*_batch_shape5.json) IS product asked (#477):
    # contracted version_diff / cross_engine pairs executed in batch.
    batch_shape5: dict[str, dict[str, int]] = {}
    shape5_asked = 0
    shape5_sat = 0
    shape5_sat_gt = 0
    shape5_unsat = 0
    for path in sorted(gen.glob(BATCH_SHAPE5_GLOB)):
        summary = summarize_batch_shape5(path)
        batch_shape5[path.name] = summary
        shape5_asked += summary["properties_asked"]
        shape5_sat += summary["properties_sat"]
        shape5_sat_gt += summary.get("properties_sat_gt", 0)
        shape5_unsat += summary["properties_unsat"]

    up = _upstream_counts(upstream_rows)

    # --- #554 Phase A: per-wave hops, shape mix, starvation -----------------
    upstream_index = upstream_join_index(upstream_rows)
    waves = classify_wave_rows(conversion_rows)
    join_wave_dispositions(waves, conversion_rows, upstream_index)
    per_wave = [waves[k] for k in sorted(waves)]
    for w in per_wave:
        w["shape_mix"] = {
            f"shape_{s}": _ratio(n, w["properties_asked"])
            for s, n in sorted(w["shape_counts"].items(), key=lambda kv: int(kv[0]))
        }
    shape_by_corpus: dict[str, dict[str, int]] = defaultdict(dict)

    def _count_shape(rec: dict[str, Any], asked_here: bool) -> None:
        corp = str(rec.get("corpus") or "")
        shape = rec.get("shape")
        if asked_here and corp and isinstance(shape, int):
            key = f"shape_{shape}"
            shape_by_corpus[corp][key] = int(shape_by_corpus[corp].get(key, 0)) + 1

    for rec in conversion_rows:
        _count_shape(rec, counts_as_conversion_asked(rec))
    for rec in all_rows:
        _count_shape(
            rec,
            rec.get("kind") in PRODUCT_KINDS
            and not is_planned(rec)
            and not rec.get("synthesized"),
        )
    starvation = starvation_metrics(
        gen,
        mine_ledger_path if mine_ledger_path is not None else gen / "candidate-ledger.json",
        queue_path=queue_path,
        prior_history=prior_starvation_history,
    )
    queue_health = contract_queue_health(
        gen, clock_iso=starvation.get("admission_window_end")
    )


    sat_in_tools = 0
    sat_not_tools = 0
    asked_in_tools = 0
    asked_not_tools = 0
    for rec in all_rows:
        if is_planned(rec) or rec.get("kind") not in PRODUCT_KINDS:
            continue
        if rec.get("synthesized"):
            continue
        in_tool = rec.get("corpus") in tools
        if in_tool:
            asked_in_tools += 1
        else:
            asked_not_tools += 1
        if rec.get("result") in SAT_RESULTS:
            if in_tool:
                sat_in_tools += 1
            else:
                sat_not_tools += 1
    for rec in conversion_rows:
        if not counts_as_conversion_asked(rec):
            continue
        in_tool = rec.get("corpus") in tools
        if in_tool:
            asked_in_tools += 1
        else:
            asked_not_tools += 1
        if rec.get("result") in SAT_RESULTS:
            if in_tool:
                sat_in_tools += 1
            else:
                sat_not_tools += 1

    asked = classified.get("properties_asked", 0) + shape5_asked
    sat = classified.get("properties_sat", 0) + shape5_sat
    unsat = classified.get("properties_unsat", 0) + shape5_unsat
    gt = classified.get("sat_ground_truthed", 0) + shape5_sat_gt
    # CRS batch shape-5 is a security-tool corpus when present.
    if shape5_asked and "coreruleset_batch_shape5.json" in batch_shape5:
        asked_in_tools += batch_shape5["coreruleset_batch_shape5.json"]["properties_asked"]
        sat_in_tools += batch_shape5["coreruleset_batch_shape5.json"]["properties_sat"]
    funnel = {
        "batch_summaries": n_summaries,
        "sites_extracted": extracted,
        "sites_encodable": encodable,
        "batch_triage_rows": summary_triage,
        "batch_summary_findings": summary_findings,
        "scanner_ndjson_files": len(scanner_files),
        "scanner_rows": classified.get("scanner_rows", 0),
        "planned_stubs": classified.get("planned_stubs", 0),
        "classification_rows": classified.get("classification_rows", 0),
        "mutation_guards": classified.get("mutation_guards", 0),
        "redos_rows": classified.get("redos_rows", 0),
        "other_rows": classified.get("other_rows", 0),
        "properties_asked": asked,
        "properties_asked_synthesized": classified.get("properties_asked_synthesized", 0),
        "properties_asked_distinct": classified.get("properties_asked_distinct", 0)
        + shape5_asked,
        "properties_unsat": unsat,
        "properties_sat": sat,
        "properties_sat_synthesized": classified.get("properties_sat_synthesized", 0),
        "properties_sat_distinct": classified.get("properties_sat_distinct", 0)
        + shape5_sat,
        "sat_unique_sites": classified.get("sat_unique_sites", 0),
        "sat_ground_truthed": gt,
        "scanner_rule_diff_sat": classified.get("scanner_rule_diff_sat", 0),
        "batch_shape5_asked": shape5_asked,
        "batch_shape5_sat": shape5_sat,
        "rule_diff_report_sat": rd_sat,
        "rule_diff_report_sat_gt": rd_sat_gt,
        "disclosed_private_first": private,
        "disclosed_public_ok": public_ok,
        "pr_dry_runs": dry_runs,
        "pr_dry_run_findings": dry_findings,
        "pr_dry_run_private_first": dry_private,
        "would_open_public_upstream": would_open,
        "accepted_upstream": up["accepted_upstream"],
        "existence_proofs": up["existence_proofs"],
        "false_positives_filed": up["false_positive"],
        "third_party_public": up["third_party_public"],
    }
    rates = {
        "encodable_fraction": _ratio(encodable, extracted),
        "property_asked_per_encodable": _ratio(asked, encodable),
        "sat_per_property_asked": _ratio(sat, asked),
        "gt_per_sat": _ratio(gt, sat),
        "pipeline_accepted_per_gt": _ratio(up["accepted_upstream"], gt),
        "pipeline_accepted_per_extracted": _ratio(up["accepted_upstream"], extracted),
        # Aliases kept one release so older quotes fail the new names first.
        "accepted_per_gt": _ratio(up["accepted_upstream"], gt),
        "accepted_per_extracted": _ratio(up["accepted_upstream"], extracted),
        "encodable_fraction_all_inventories": yara["encodable_fraction_all"],
        "encodable_fraction_excluding_yara": yara["encodable_fraction_excluding_yara"],
        "encodable_fraction_yara": yara["encodable_fraction_yara"],
        "yara_share_of_unencodable": yara["yara_share_of_unencodable"],
        "fullword_share_of_unencodable": yara["fullword_share_of_unencodable"],
    }
    by_corpus = []
    for corpus in sorted(set(per_corpus) | set(conversion_by_corpus)):
        c = classify_scanner_rows(per_corpus.get(corpus) or [])
        conv = classify_conversion_rows(conversion_by_corpus.get(corpus) or [])
        asked = int(c.get("properties_asked") or 0) + int(conv.get("properties_asked") or 0)
        if asked == 0:
            continue
        by_corpus.append(
            {
                "corpus": corpus,
                "security_tool": corpus in tools,
                "scanner_rows": int(c.get("scanner_rows") or 0),
                "properties_asked": asked,
                "properties_unsat": int(c.get("properties_unsat") or 0)
                + int(conv.get("properties_unsat") or 0),
                "properties_sat": int(c.get("properties_sat") or 0)
                + int(conv.get("properties_sat") or 0),
                "sat_ground_truthed": int(c.get("sat_ground_truthed") or 0)
                + int(conv.get("sat_ground_truthed") or 0),
                "sat_unique_sites": int(c.get("sat_unique_sites") or 0)
                + int(conv.get("sat_unique_sites") or 0),
            }
        )
    by_corpus.sort(key=lambda r: (-r["properties_asked"], r["corpus"]))

    # Surface CRS batch shape-5 even when scanner NDJSON asked is still 0.
    for fname, summary in batch_shape5.items():
        if summary.get("properties_asked", 0) <= 0:
            continue
        corpus = fname[: -len("_batch_shape5.json")] if fname.endswith(
            "_batch_shape5.json"
        ) else fname
        sat_gt = int(summary.get("properties_sat_gt", 0))
        if any(row["corpus"] == corpus for row in by_corpus):
            for row in by_corpus:
                if row["corpus"] == corpus:
                    row["properties_asked"] += summary["properties_asked"]
                    row["properties_sat"] += summary["properties_sat"]
                    row["properties_unsat"] += summary["properties_unsat"]
                    row["sat_ground_truthed"] += sat_gt
            continue
        by_corpus.append(
            {
                "corpus": corpus,
                "security_tool": corpus in tools,
                "scanner_rows": 0,
                "properties_asked": summary["properties_asked"],
                "properties_unsat": summary["properties_unsat"],
                "properties_sat": summary["properties_sat"],
                "sat_ground_truthed": sat_gt,
                "sat_unique_sites": 0,
            }
        )
    by_corpus.sort(key=lambda r: (-r["properties_asked"], r["corpus"]))

    return {
        "schema_version": SCHEMA_VERSION,
        "measure": "conversion_ledger",
        "notes": [
            "Heap's-law / singleton novelty saturates compiler coverage, not this ledger.",
            "docs/verified-findings.jsonl VF-* rows are toolkit traps, not vulnerability counts.",
            "Classification rows (usage/intent/triage kinds) are not security bugs.",
            "Mutation guards prove harness sensitivity; they are not product findings.",
            "SAT + ground-truth is a candidate finding; accepted_upstream is the last mile.",
            "would_open_public_upstream must stay 0 without a human approval file (SECURITY.md).",
            "batch_shape5 contracted version_diff/cross_engine rows count as properties_asked.",
            "#554: per-wave hop rates join curated dispositions on (site, question_id);",
            "filed = curated status filed/private_first/fixed_upstream (or filed_at set);",
            "accepted = fixed_upstream. Starvation: backlog_weeks = demand_open /",
            "admission_per_week, admission from GO gate-decision artifacts (not the",
            "lagging candidate ledger). unknown_date rows are excluded from median",
            "time-to-acceptance; time-to-acceptance is Kaplan-Meier or median of",
            "closed rows only — never censored + closed mixed in a plain median.",
        ],
        "funnel": funnel,
        "rates": rates,
        "security_tool_split": {
            "properties_asked_in_tools": asked_in_tools,
            "properties_asked_not_tools": asked_not_tools,
            "properties_sat_in_tools": sat_in_tools,
            "properties_sat_not_tools": sat_not_tools,
        },
        "rule_diff_reports": rule_diff,
        "batch_shape5": batch_shape5,
        "per_wave": per_wave,
        "starvation": starvation,
        "queue_health": queue_health,
        "shape_mix_by_corpus": {
            corp: dict(sorted(counts.items(), key=lambda kv: int(kv[0].split("_")[1])))
            for corp, counts in sorted(shape_by_corpus.items())
        },
        "yara_split": yara,
        "upstream": up,
        "upstream_rows": [
            {k: r[k] for k in ("id", "corpus", "status", "kind", "language_membership") if k in r}
            for r in sorted(upstream_rows, key=lambda x: x["id"])
        ],
        "by_corpus": by_corpus,
    }


def render_md(data: dict[str, Any]) -> str:
    f = data["funnel"]
    r = data["rates"]
    up = data["upstream"]
    split = data["security_tool_split"]

    def pct(val: float | None) -> str:
        if val is None:
            return "n/a"
        if val != 0 and abs(val) < 0.0001:
            return f"{val:.2e}"
        return f"{val:.4f}"

    def n(val: int) -> str:
        return f"{val:,}"

    lines = [
        "# Conversion ledger",
        "",
        "Product funnel: sites → properties asked → SAT → ground-truthed → "
        "disclosed → accepted upstream.",
        "",
        "Heap's-law / singleton novelty saturates **compiler coverage**. This "
        "artifact saturates **conversion**. TIMEOUT / `unknown` is not a pass. "
        "`docs/verified-findings.jsonl` VF-* rows are toolkit traps, not this numerator.",
        "",
        "## Funnel",
        "",
        "| stage | count |",
        "|---|---|",
        f"| sites extracted (batch summaries) | {n(f['sites_extracted'])} |",
        f"| sites encodable | {n(f['sites_encodable'])} |",
        f"| scanner NDJSON rows | {n(f['scanner_rows'])} |",
        f"| planned inventory stubs | {n(f['planned_stubs'])} |",
        f"| classification rows (usage/intent/triage kinds) | {n(f['classification_rows'])} |",
        f"| mutation guards (hygiene) | {n(f['mutation_guards'])} |",
        f"| properties asked (non-planned product kinds) | {n(f['properties_asked'])} |",
        f"| properties asked distinct `(site, question_id)` | {n(f['properties_asked_distinct'])} |",
        f"| properties UNSAT (holds in declared domain) | {n(f['properties_unsat'])} |",
        f"| properties SAT | {n(f['properties_sat'])} |",
        f"| properties SAT distinct `(site, question_id)` | {n(f['properties_sat_distinct'])} |",
        f"| SAT unique sites | {n(f['sat_unique_sites'])} |",
        f"| SAT ground-truthed (`reproduced` / `PASS`) | {n(f['sat_ground_truthed'])} |",
        f"| rule_diff report SAT (dedicated pilots) | {n(f['rule_diff_report_sat'])} |",
        f"| rule_diff report SAT + ground-truth | {n(f['rule_diff_report_sat_gt'])} |",
        f"| disclosed `private_first` (scanner product+classification, skip planned) | {n(f['disclosed_private_first'])} |",
        f"| disclosed `public_ok` | {n(f['disclosed_public_ok'])} |",
        f"| dry-run `private_first` (includes planned stubs) | {n(f['pr_dry_run_private_first'])} |",
        f"| dry-run would open public upstream | {n(f['would_open_public_upstream'])} |",
        f"| accepted upstream (curated `fixed_upstream`) | {n(f['accepted_upstream'])} |",
        f"| existence proofs (`fixed_upstream` + `private_first`) | {n(f['existence_proofs'])} |",
        f"| filed false positives | {n(f['false_positives_filed'])} |",
        f"| third-party public accepted | {n(f['third_party_public'])} |",
        "",
        "## Rates",
        "",
        "| rate | value |",
        "|---|---|",
        f"| encodable / extracted | {pct(r['encodable_fraction'])} |",
        f"| properties asked / encodable | {pct(r['property_asked_per_encodable'])} |",
        f"| SAT / properties asked | {pct(r['sat_per_property_asked'])} |",
        f"| ground-truthed / SAT | {pct(r['gt_per_sat'])} |",
        f"| pipeline accepted (incl. own-code) / SAT GT | {pct(r['pipeline_accepted_per_gt'])} |",
        f"| pipeline accepted / extracted | {pct(r['pipeline_accepted_per_extracted'])} |",
        f"| encodable / extracted excluding YARA inventories | {pct(r['encodable_fraction_excluding_yara'])} |",
        f"| YARA share of inventory unencodable | {pct(r['yara_share_of_unencodable'])} |",
        f"| `fullword-boundary` share of inventory unencodable | {pct(r['fullword_share_of_unencodable'])} |",
        "",
        "## Security-tool split (scanner product kinds)",
        "",
        f"Asked in tools: {split['properties_asked_in_tools']}. "
        f"Asked elsewhere: {split['properties_asked_not_tools']}. "
        f"SAT in tools: {split['properties_sat_in_tools']}. "
        f"SAT elsewhere: {split['properties_sat_not_tools']}.",
        "",
        "## Upstream (curated)",
        "",
        f"Rows: {up['rows']}. Language-membership: {up['language_membership']}. "
        f"fixed_upstream: {up['fixed_upstream']}. filed_plan: {up['filed_plan']}. "
        f"false_positive: {up['false_positive']}. out_of_scope_redos: {up['out_of_scope_redos']}. "
        f"private_first: {up['private_first']}. wont_file: {up['wont_file']}.",
        "",
        "Source: [`docs/conversion-upstream.jsonl`](../../docs/conversion-upstream.jsonl).",
        "",
        "## Corpora with properties asked",
        "",
        "| corpus | security tool | asked | unsat | sat | sat GT | unique SAT sites |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in data["by_corpus"]:
        lines.append(
            f"| {row['corpus']} | {str(row['security_tool']).lower()} | "
            f"{row['properties_asked']} | {row['properties_unsat']} | "
            f"{row['properties_sat']} | {row['sat_ground_truthed']} | "
            f"{row['sat_unique_sites']} |"
        )
    lines.append("")

    per_wave = data.get("per_wave") or []
    lines.extend(
        [
            "## Per-wave conversion hops (#554)",
            "",
            "asked → SAT → GT → filed → accepted per `(wave_id, idiom_bucket)`.",
            "**GT→filed is the currently empty hop** — highlighted. Join: curated",
            "`(site, question_id)`; filed = status filed/private_first/fixed_upstream",
            "(or filed_at set); accepted = fixed_upstream.",
            "",
            "| wave | idiom bucket | asked | SAT | GT | filed | accepted | GT→filed |",
            "|---|---|---|---|---|---|---|---|",
        ]
    )
    for w in per_wave:
        gt = w["sat_ground_truthed"]
        ratio = _ratio(w["filed"], gt)
        lines.append(
            f"| {w['wave_id']} | {w['idiom_bucket']} | {w['properties_asked']} | "
            f"{w['properties_sat']} | {gt} | **{w['filed']}** | {w['accepted']} | "
            f"**{pct(ratio) if gt else 'n/a'}** |"
        )
    lines.append("")

    star = data.get("starvation") or {}
    lines.extend(
        [
            "## Starvation & queue pressure (#554)",
            "",
            f"- demand_open (open gated:go clusters lacking a closed wave): "
            f"**{n(star.get('demand_open_gated_go_no_closed_wave') or 0)}**",
            f"- admission_per_week (GO gate-decision artifacts, last "
            f"{star.get('admission_window_days')}-day window ending "
            f"{star.get('admission_window_end')}): **{n(star.get('admission_per_week') or 0)}**",
            f"- backlog_weeks = demand_open / admission_per_week = "
            f"**{star.get('backlog_weeks') if star.get('backlog_weeks') is not None else 'n/a'}**",
            f"- mine_queue_pressure = queue_len / queue_cap = "
            f"{star.get('mine_queue_len')} / {n(star.get('mine_queue_cap') or 0)} = "
            f"**{pct(star.get('mine_queue_pressure'))}**",
            f"- alert (backlog_weeks increased >= 2 consecutive windows): "
            f"**{'YES' if star.get('alert_backlog_increasing') else 'no'}** "
            f"(consecutive increases: {star.get('consecutive_increases')})",
            "",
            "Admission is bounded by the ~10/day mine cap regardless of #550 batch",
            "flush, so backlog_weeks reflects mine-cap pressure by design — read it",
            "alongside mine_queue_pressure, not as a batch-health metric.",
            "",
        ]
    )

    qh = data.get("queue_health") or {}
    lines.extend(
        [
            "## Contract-queue health (#551 Phase C states)",
            "",
            f"artifacts present: {qh.get('artifacts_present')} · emitted: "
            f"{qh.get('emitted')} · claimed: {qh.get('claimed')} · contracted: "
            f"{qh.get('contracted')} · skipped: {qh.get('skipped')} · median age: "
            f"{qh.get('median_age_days') if qh.get('median_age_days') is not None else 'n/a'} days."
            f" {qh.get('note') or ''}".rstrip(),
            "",
            "## Property-shape mix (#554)",
            "",
            "Share of asked properties per shape, per wave (conversion rows).",
            "",
            "| wave | idiom bucket | asked | shape mix (%) |",
            "|---|---|---|---|",
        ]
    )
    for w in per_wave:
        mix = ", ".join(
            f"{k.replace('_', ' ')}: {pct(v)}"
            for k, v in (w.get("shape_mix") or {}).items()
        )
        lines.append(
            f"| {w['wave_id']} | {w['idiom_bucket']} | {w['properties_asked']} | {mix or 'n/a'} |"
        )
    lines.append("")
    lines.extend(
        [
            "## Denominator notes",
            "",
            "`crs-inventory.ndjson` is the @rx-only CRS measure (346 rows) from "
            "`regexproof.batch.crs_measure`; it is **not** the batch corpus. "
            "`coreruleset-inventory.ndjson` + `coreruleset_batch_summary.json` "
            "are the batch extractor (338 extracted). Do not glob `crs-inventory` "
            "into the conversion ledger sample.",
            "",
            "Synthesis considers at most `synth_max_sites` (default 0 — untargeted",
            "synthesis is compute control; opt-in corpora set an explicit value, sort",
            "by `regex_id`) per corpus. Corpora with properties asked are listed",
            "in the table above; their batch summaries record `synth_max_sites`.",
            "",
        ]
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--generated-dir",
        type=Path,
        default=GEN_DIR,
        help="Directory of batch/scanner artifacts (default: properties/generated)",
    )
    ap.add_argument(
        "--upstream",
        type=Path,
        default=UPSTREAM_PATH,
        help="Curated upstream JSONL (default: docs/conversion-upstream.jsonl)",
    )
    ap.add_argument(
        "--output-dir",
        type=Path,
        default=GEN_DIR,
        help="Directory for conversion-ledger.{json,md}",
    )
    args = ap.parse_args(argv)

    if not args.upstream.is_file():
        print(f"FATAL: upstream file missing: {args.upstream}", file=sys.stderr)
        return 2

    # Carry the starvation history forward from the committed artifact so the
    # backlog alert can observe consecutive windows; aggregate() appends the
    # current admission window only when it advanced (same-week reruns stable).
    out_dir = args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "conversion-ledger.json"
    md_path = out_dir / "conversion-ledger.md"
    prior_history: list[dict[str, Any]] | None = None
    if json_path.is_file():
        try:
            prior = json.loads(json_path.read_text(encoding="utf-8"))
            hist = (prior.get("starvation") or {}).get("history")
            if isinstance(hist, list):
                prior_history = hist
        except (OSError, ValueError):
            prior_history = None

    data = aggregate(
        gen_dir=args.generated_dir,
        upstream_path=args.upstream,
        prior_starvation_history=prior_history,
    )

    json_path.write_text(
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_md(data), encoding="utf-8")

    f = data["funnel"]
    print(
        f"conversion-ledger -> {md_path} + {json_path}: "
        f"extracted={f['sites_extracted']} encodable={f['sites_encodable']} "
        f"asked={f['properties_asked']} sat={f['properties_sat']} "
        f"gt={f['sat_ground_truthed']} accepted={f['accepted_upstream']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
