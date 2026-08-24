#!/usr/bin/env python3
"""Wave E (#562): conversion scheduler over GO clusters.

Selects the NEXT UNUSED idiom bucket per cluster at close-out, reserves
capacity (productive buckets + novel-idiom exploration + a small unbiased
slice), NEVER re-ranks the mine by converted-pattern similarity, and feeds
wont-file pattern classes into bucket selection (deterministic deny-list:
a wont-file-heavy target blocks the named-next selection).

Usage::

  python3 scripts/conversion-scheduler.py \\
      --gate-decisions properties/generated \\
      --dispositions docs/conversion-upstream.jsonl \\
      --queues-dir properties/conversion_queue \\
      [--out properties/generated/conversion_schedule.json]
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

PRODUCTIVE_SHARE = 0.7   # productive (used) buckets get 70% of reserved capacity
NOVEL_SHARE = 0.2        # novel-idiom exploration
UNBIASED_SHARE = 0.1     # small unbiased exploration slice (always >= 1)

# CodeRabbit #582 + Luna r4: the ledger's committed idiom_bucket values are
# the ONLY vocabulary the scheduler may emit. Ordered per-cluster progression
# (first unused wins). DESIGN_TAIL_BUCKETS are the #551 Phase E named nexts
# (qosify/network.js/firewall DSCP) that are NOT yet registered in the
# committed ledger — the scheduler REFUSES to emit them until they appear
# (fail closed: an unregistered bucket is never a valid selected_bucket).
BUCKET_PROGRESSION: dict[str, list[str]] = {
    "openwrt_packages": [
        "validator-charsets-and-captures",
        "image-and-ddns-json",
        "ddns-query-and-escape-image",
    ],
    "openwrt_luci": [
        "form-validator-alphabets",
    ],
}

DESIGN_TAIL_BUCKETS: dict[str, list[str]] = {
    "openwrt_packages": ["qosify-network-dscp"],
    "openwrt_luci": ["network-js-dscp", "firewall-dscp"],
}

DEFAULT_QUEUES_DIR = ROOT / "properties" / "conversion_queue"
PENDING_SITE_STATUSES = frozenset({"emitted", "claimed"})
# Luna r4: the queue's own vocabulary (regexproof/mine/conversion_queue.py)
# — ANY status outside it is malformed and must fail closed.
KNOWN_SITE_STATUSES = PENDING_SITE_STATUSES | frozenset({
    "contracted",
    "skipped_unreachable",
    "skipped_out_of_scope",
    "skipped_no_response",
    "skipped_duplicate",
})
# Luna r2 #1: a wont-file pattern class that recurs this many times on a
# target CORPUS denies it as the named-next bucket (deterministic policy;
# single occurrences are noise, not a pattern).
WONT_FILE_DENY_THRESHOLD = 2


def go_clusters(gate_decisions_dir: pathlib.Path) -> list[str]:
    """Source clusters from validated gated:go gate-decision artifacts
    (Luna r1 #4: empty/missing input must NOT fabricate cluster selections;
    the named-bucket map is not a cluster inventory). Malformed artifacts
    are skipped, never fatal (Luna r2 #3)."""
    clusters: set[str] = set()
    if gate_decisions_dir.is_dir():
        for f in sorted(gate_decisions_dir.glob("*_gate_decision.json")):
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if not isinstance(d, dict):
                continue  # e.g. a JSON list — skip, not crash
            if str(d.get("decision") or "") == "go":
                corpus = str(d.get("corpus") or "").strip()
                if corpus:
                    clusters.add(corpus)
    return sorted(clusters)


def wont_file_classes(dispositions_path: pathlib.Path) -> dict[str, int]:
    """wont-file pattern classes from the REAL disposition source
    (docs/conversion-upstream.jsonl — status=wont_file rows), aggregated by
    pattern class, sorted desc (Luna r1 #3). Reporting summary only —
    selection uses wont_file_corpora()."""
    return _wont_file_agg(dispositions_path, key="class")


def wont_file_corpora(dispositions_path: pathlib.Path) -> dict[str, int]:
    """wont-file rows keyed by CORPUS (the target bucket/cluster name) —
    the deny-list key (Luna r2 #1: classes like 'third_party' never match
    bucket names like 'openwrt_luci'; the row's corpus does)."""
    return _wont_file_agg(dispositions_path, key="corpus")


def _wont_file_agg(dispositions_path: pathlib.Path, *, key: str) -> dict[str, int]:
    if not dispositions_path.exists():
        return {}
    out: dict[str, int] = {}
    for line in dispositions_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        if not isinstance(rec, dict) or str(rec.get("status") or "") != "wont_file":
            continue
        k = str(rec.get(key) or "no-corpus").strip() or "no-corpus"
        out[k] = out.get(k, 0) + 1
    return dict(sorted(out.items(), key=lambda kv: (-kv[1], kv[0])))


def used_buckets_per_cluster(rows: list[dict]) -> dict[str, set[str]]:
    """(cluster -> set of idiom buckets that already have conversion rows).
    Cluster = wave_id with a trailing ``_w<digits>`` generation stripped
    (openwrt_packages_w2 -> openwrt_packages); an exact-suffix regex only —
    ``foo_west`` is never mangled (Luna r1 #5)."""
    gen_re = re.compile(r"_w[0-9]+$")
    out: dict[str, set[str]] = {}
    for rec in rows:
        wave = str(rec.get("wave_id") or rec.get("cluster") or "").strip()
        bucket = str(rec.get("idiom_bucket") or "").strip()
        if not wave:
            continue
        cluster = gen_re.sub("", wave)
        out.setdefault(cluster, set())
        if bucket:
            out[cluster].add(bucket)
    return out


def _queue_has_pending(queues_dir: pathlib.Path, cluster: str, bucket: str) -> bool:
    """The cluster's queue (<cluster>.json — the canonical emit layout) has
    a PENDING row for this BUCKET (row.idiom_bucket == bucket, status
    emitted/claimed) → blocks selection. Empty queue / no matching rows /
    only closed-status rows → does not block. ANY malformed row FOR THE
    BUCKET (non-dict, status-less, unknown status) FAILS CLOSED — malformed
    site data must never permit selection (CodeRabbit #582, Luna r4/r5)."""
    qpath = queues_dir / f"{cluster}.json"
    if not qpath.exists():
        return False
    try:
        q = json.loads(qpath.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return True  # unreadable queue — fail closed, treat as blocking
    sites = q.get("candidate_sites") if isinstance(q, dict) else None
    if not isinstance(sites, list):
        return True  # queue present with no rows — conservatively blocking
    for s in sites:
        if not isinstance(s, dict):
            return True  # malformed entry (e.g. null) — fail closed
        row_bucket = str(s.get("idiom_bucket") or "").strip()
        if not row_bucket:
            # Luna r6: a site-only row (no idiom_bucket — emit() accepts
            # site-only ranked items) is UN-ATTRIBUTABLE: fail closed like
            # null rows, never skip as 'unrelated'.
            return True
        if row_bucket != bucket:
            continue  # a different bucket's row — irrelevant here
        status = str(s.get("status") or "").strip()
        if not status:
            return True  # status-less entry for this bucket — fail closed
        if status not in KNOWN_SITE_STATUSES:
            return True  # unknown status — fail closed (Luna r4)
        if status in PENDING_SITE_STATUSES:
            return True
    return False  # no pending/malformed rows for this bucket — does not block


def next_unused_bucket(
    cluster: str,
    used: set[str],
    queues_dir: pathlib.Path,
) -> tuple[str | None, str]:
    """(bucket, basis) for the cluster's next bucket. Registered progression
    buckets (committed ledger vocabulary) win first; DESIGN_TAIL_BUCKETS
    (qosify/network-js/firewall-dscp) are NEVER emitted until they appear
    in the committed ledger — their basis is 'unregistered-next' (Luna r4).
    No wrap-around: progression exhausted -> none-available."""
    for candidate in BUCKET_PROGRESSION.get(cluster, []):
        if candidate not in used and not _queue_has_pending(queues_dir, cluster, candidate):
            return candidate, "named-next-unused"
    if DESIGN_TAIL_BUCKETS.get(cluster):
        return None, "unregistered-next"
    return None, "none-available"


def build_schedule(
    rows: list[dict],
    *,
    queues_dir: pathlib.Path,
    gate_decisions_dir: pathlib.Path,
    dispositions_path: pathlib.Path,
    clusters: list[str] | None = None,
) -> dict:
    used = used_buckets_per_cluster(rows)
    wont = wont_file_classes(dispositions_path)
    wont_by_corpus = wont_file_corpora(dispositions_path)
    clusters = clusters if clusters is not None else go_clusters(gate_decisions_dir)
    selections: list[dict] = []
    for cluster in clusters:
        used_set = used.get(cluster, set())
        nxt, nxt_basis = next_unused_bucket(cluster, used_set, queues_dir)
        # #551 Phase E / Luna r1 #3 + r2 #1: wont-file pattern classes feed
        # selection via a DETERMINISTIC deny-list keyed on the target's
        # CORPUS (the row's corpus IS the bucket name — classes like
        # 'third_party' never match buckets). A corpus whose wont-file
        # count reaches the threshold is denied as the named-next pick.
        wont_blocked = (
            nxt is not None
            and wont_by_corpus.get(nxt, 0) >= WONT_FILE_DENY_THRESHOLD
        )
        selections.append(
            {
                "cluster": cluster,
                "used_buckets": sorted(used_set),
                "selected_bucket": None if wont_blocked else nxt,
                "selection_basis": (
                    "wont-file-blocked" if wont_blocked else nxt_basis
                ),
                # #550/#551: NO mine re-rank by converted-pattern similarity —
                # the scheduler never touches ranking; only bucket selection.
                "mine_re_ranked": False,
            }
        )
    return {
        "schema_version": "1",
        "generated_at": None,  # deterministic callers pass --at
        "capacity_reservation": {
            "productive_share": PRODUCTIVE_SHARE,
            "novel_exploration_share": NOVEL_SHARE,
            "unbiased_slice_share": UNBIASED_SHARE,
        },
        "selections": selections,
        "wont_file_classes": wont,
        "cache_interplay_note": (
            "GO-cluster utilization accelerates #550 lease pressure — "
            "leased clone count + byte caps apply; there is NO immortal "
            "lease set. Each conversion wave must fit within the current "
            "cache budget and release leases on close-out."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ledger", type=pathlib.Path,
                    default=ROOT / "properties" / "generated" / "conversion-ledger.json",
                    help="conversion ledger aggregate (per_wave rows)")
    ap.add_argument("--gate-decisions", type=pathlib.Path,
                    default=ROOT / "properties" / "generated",
                    help="dir of *_gate_decision.json (GO cluster inventory)")
    ap.add_argument("--dispositions", type=pathlib.Path,
                    default=ROOT / "docs" / "conversion-upstream.jsonl",
                    help="wont-file disposition source")
    ap.add_argument("--queues-dir", type=pathlib.Path, default=DEFAULT_QUEUES_DIR)
    ap.add_argument("--out", type=pathlib.Path,
                    default=ROOT / "properties" / "generated" / "conversion_schedule.json")
    ap.add_argument("--at", default="", help="ISO timestamp for determinism")
    args = ap.parse_args(argv)

    rows = _load_ledger_rows(args.ledger)
    sched = build_schedule(
        rows,
        queues_dir=args.queues_dir,
        gate_decisions_dir=args.gate_decisions,
        dispositions_path=args.dispositions,
    )
    sched["generated_at"] = args.at or sched["generated_at"]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(sched, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8")
    for sel in sched["selections"]:
        print(f"{sel['cluster']}: used={sel['used_buckets']} "
              f"-> next={sel['selected_bucket']} ({sel['selection_basis']})")
    print(f"wont-file classes: {len(sched['wont_file_classes'])}")
    return 0


def _load_ledger_rows(ledger_path: pathlib.Path) -> list[dict]:
    """Load conversion rows from the COMMITTED conversion-ledger.json
    aggregate (per_wave section: (wave_id, idiom_bucket, ...) rows) — the
    scheduler's used-bucket source. Falls back to raw ndjson if the path
    ends in .ndjson. Final-gate #4 (MEDIUM): MISSING or MALFORMED input
    FAILS CLOSED — a silently-empty history would let the scheduler
    re-select a first bucket already consumed by a prior wave (duplicate
    selection)."""
    if not ledger_path.exists():
        raise SystemExit(
            f"conversion-scheduler: ledger {ledger_path} is missing — "
            "refusing to schedule with empty history (fail closed)"
        )
    if ledger_path.suffix == ".ndjson":
        rows: list[dict] = []
        for i, line in enumerate(
            ledger_path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except ValueError as exc:
                raise SystemExit(
                    f"conversion-scheduler: malformed ledger line in "
                    f"{ledger_path}: {exc} — refusing to schedule (fail closed)"
                ) from exc
            if not isinstance(rec, dict):
                raise SystemExit(
                    f"conversion-scheduler: ledger {ledger_path} line {i} is "
                    f"{type(rec).__name__}, not an object — refusing to "
                    "schedule (fail closed)"
                )
            if not str(rec.get("idiom_bucket") or "").strip():
                raise SystemExit(
                    f"conversion-scheduler: ledger {ledger_path} line {i} has "
                    "no idiom_bucket — a consumed bucket would be silently "
                    "ignored (duplicate selection risk), refusing (fail closed)"
                )
            if not str(rec.get("wave_id") or rec.get("cluster") or "").strip():
                raise SystemExit(
                    f"conversion-scheduler: ledger {ledger_path} line {i} has "
                    "neither wave_id nor cluster — the consumed bucket's "
                    "cluster is unattributable (duplicate selection risk), "
                    "refusing (fail closed)"
                )
            rows.append(rec)
        return rows
    try:
        data = json.loads(ledger_path.read_text(encoding="utf-8"))
    except ValueError as exc:
        raise SystemExit(
            f"conversion-scheduler: ledger {ledger_path} is not valid JSON: "
            f"{exc} — refusing to schedule (fail closed)"
        ) from exc
    per_wave = data.get("per_wave") if isinstance(data, dict) else None
    if not isinstance(per_wave, list):
        raise SystemExit(
            f"conversion-scheduler: ledger {ledger_path} has no per_wave list — "
            "refusing to schedule with empty history (fail closed)"
        )
    # CodeRabbit #583: STRUCTURALLY invalid rows fail closed too — a row
    # without idiom_bucket would silently drop a consumed bucket (re-select
    # it), and a scalar/list row would crash used_buckets_per_cluster.
    for i, rec in enumerate(per_wave):
        if not isinstance(rec, dict):
            raise SystemExit(
                f"conversion-scheduler: ledger {ledger_path} per_wave[{i}] is "
                f"{type(rec).__name__}, not an object — refusing to schedule "
                "(fail closed)"
            )
        if not str(rec.get("idiom_bucket") or "").strip():
            raise SystemExit(
                f"conversion-scheduler: ledger {ledger_path} per_wave[{i}] "
                "has no idiom_bucket — a consumed bucket would be silently "
                "ignored (duplicate selection risk), refusing (fail closed)"
            )
        if not str(rec.get("wave_id") or rec.get("cluster") or "").strip():
            # Luna r4 #2: a row without CLUSTER identity is dropped by
            # used_buckets_per_cluster (its `if not wave: continue`), so
            # its consumed bucket would be silently ignored and re-selected.
            raise SystemExit(
                f"conversion-scheduler: ledger {ledger_path} per_wave[{i}] "
                "has neither wave_id nor cluster — the consumed bucket's "
                "cluster is unattributable (duplicate selection risk), "
                "refusing (fail closed)"
            )
    return per_wave


if __name__ == "__main__":
    raise SystemExit(main())
