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

NEXT_BUCKET_BY_CLUSTER = {
    # #551 Phase E: named next buckets per cluster after the current one
    # (real cluster names from the committed conversion ledger).
    "openwrt_packages": "openwrt_luci",
    "openwrt_luci": "form-validators",
    "form-validators": "qosify-network-dscp",
    "qosify-network-dscp": "openwrt_packages",  # cycle sentinel — never selected
}

DEFAULT_QUEUES_DIR = ROOT / "properties" / "conversion_queue"
PENDING_SITE_STATUSES = frozenset({"emitted", "claimed"})


def go_clusters(gate_decisions_dir: pathlib.Path) -> list[str]:
    """Source clusters from validated gated:go gate-decision artifacts
    (Luna r1 #4: empty/missing input must NOT fabricate cluster selections;
    the named-bucket map is not a cluster inventory)."""
    clusters: set[str] = set()
    if gate_decisions_dir.is_dir():
        for f in sorted(gate_decisions_dir.glob("*_gate_decision.json")):
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if str(d.get("decision") or "") == "go":
                corpus = str(d.get("corpus") or "").strip()
                if corpus:
                    clusters.add(corpus)
    return sorted(clusters)


def wont_file_classes(dispositions_path: pathlib.Path) -> dict[str, int]:
    """wont-file pattern classes from the REAL disposition source
    (docs/conversion-upstream.jsonl — status=wont_file rows), aggregated by
    pattern class, sorted desc (Luna r1 #3)."""
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
        if str(rec.get("status") or "") != "wont_file":
            continue
        cls = str(rec.get("class") or "no-class").strip() or "no-class"
        out[cls] = out.get(cls, 0) + 1
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


def _queue_has_pending(queues_dir: pathlib.Path, bucket: str) -> bool:
    """A queue artifact for the bucket blocks selection only when it has
    PENDING sites (emitted/claimed) — a fully contracted/skipped queue is
    closed work and does not block (Luna r1 #2: file existence alone is
    wrong)."""
    qpath = queues_dir / f"{bucket}.json"
    if not qpath.exists():
        return False
    try:
        q = json.loads(qpath.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return True  # unreadable queue — fail closed, treat as blocking
    sites = q.get("candidate_sites") if isinstance(q, dict) else None
    if not isinstance(sites, list) or not sites:
        return True  # queue present with no rows — conservatively blocking
    return any(
        str(s.get("status") or "") in PENDING_SITE_STATUSES for s in sites
    )


def next_unused_bucket(
    cluster: str,
    used: set[str],
    queues_dir: pathlib.Path,
) -> str | None:
    """The named next bucket for the cluster that is NOT yet used and has no
    PENDING queue. The traversal terminates at the STARTING cluster — the
    cycle sentinel is never selected (Luna r1 #1)."""
    start = cluster
    candidate = NEXT_BUCKET_BY_CLUSTER.get(cluster)
    while candidate and candidate != start:
        if candidate not in used and not _queue_has_pending(queues_dir, candidate):
            return candidate
        candidate = NEXT_BUCKET_BY_CLUSTER.get(candidate)
    return None  # full cycle or self-loop — no unused bucket available


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
    clusters = clusters if clusters is not None else go_clusters(gate_decisions_dir)
    selections: list[dict] = []
    for cluster in clusters:
        used_set = used.get(cluster, set())
        nxt = next_unused_bucket(cluster, used_set, queues_dir)
        # #551 Phase E / Luna r1 #3: wont-file pattern classes feed selection
        # via a DETERMINISTIC deny-list — a wont-file-heavy next target is
        # blocked (never the named-next pick) and reported for the operator.
        wont_blocked = False
        if nxt is not None and nxt in wont and wont[nxt] > 0:
            wont_blocked = True
        selections.append(
            {
                "cluster": cluster,
                "used_buckets": sorted(used_set),
                "selected_bucket": None if wont_blocked else nxt,
                "selection_basis": (
                    "wont-file-blocked" if wont_blocked
                    else ("named-next-unused" if nxt else "none-available")
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
    ends in .ndjson."""
    if not ledger_path.exists():
        return []
    if ledger_path.suffix == ".ndjson":
        rows: list[dict] = []
        for line in ledger_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
        return rows
    try:
        data = json.loads(ledger_path.read_text(encoding="utf-8"))
    except ValueError:
        return []
    per_wave = data.get("per_wave") if isinstance(data, dict) else None
    if isinstance(per_wave, list):
        return per_wave
    return []


if __name__ == "__main__":
    raise SystemExit(main())
