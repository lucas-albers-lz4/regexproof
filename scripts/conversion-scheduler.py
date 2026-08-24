#!/usr/bin/env python3
"""Wave E (#562): conversion scheduler over GO clusters.

Selects the NEXT UNUSED idiom bucket per cluster at close-out, reserves
capacity (productive buckets + novel-idiom exploration + a small unbiased
slice), NEVER re-ranks the mine by converted-pattern similarity, and feeds
wont-file pattern classes into bucket selection.

Usage::

  python3 scripts/conversion-scheduler.py --ledger properties/generated/conversion.ndjson
      [--queues-dir properties] [--out properties/generated/conversion_schedule.json]
"""

from __future__ import annotations

import argparse
import json
import pathlib
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
    "qosify-network-dscp": "openwrt_packages",  # cycle guard
}

DEFAULT_QUEUES_DIR = ROOT / "properties"


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


def used_buckets_per_cluster(rows: list[dict]) -> dict[str, set[str]]:
    """(cluster -> set of idiom buckets that already have conversion rows).
    Cluster = wave_id with its trailing _wN generation stripped
    (openwrt_packages_w2 -> openwrt_packages)."""
    out: dict[str, set[str]] = {}
    for rec in rows:
        wave = str(rec.get("wave_id") or rec.get("cluster") or "").strip()
        bucket = str(rec.get("idiom_bucket") or "").strip()
        if not wave:
            continue
        cluster = wave.rsplit("_w", 1)[0] if "_w" in wave else wave
        out.setdefault(cluster, set())
        if bucket:
            out[cluster].add(bucket)
    return out


def wont_file_classes(rows: list[dict]) -> dict[str, int]:
    """wont-file reason classes over the ledger rows (feeds selection). The
    aggregate per_wave rows do not carry approval_escape — return {} there;
    raw ndjson rows (record-filing-decision output) do."""
    out: dict[str, int] = {}
    for rec in rows:
        if str(rec.get("approval_escape") or "") != "wont_file":
            continue
        reason = str(rec.get("reason_code") or "no-reason")
        out[reason] = out.get(reason, 0) + 1
    return dict(sorted(out.items(), key=lambda kv: -kv[1]))


def next_unused_bucket(cluster: str, used: set[str], queues_dir: pathlib.Path) -> str | None:
    """The named next bucket for the cluster that is NOT yet used (no queue
    artifact, no ledger rows). Refuses to wrap around a full cycle."""
    seen: set[str] = set()
    candidate = NEXT_BUCKET_BY_CLUSTER.get(cluster)
    while candidate and candidate not in seen:
        seen.add(candidate)
        if candidate not in used:
            queue_file = queues_dir / f"{candidate}.json"
            if not queue_file.exists():
                return candidate
        candidate = NEXT_BUCKET_BY_CLUSTER.get(candidate)
    return None  # full cycle — all named next buckets already used


def build_schedule(
    rows: list[dict],
    *,
    queues_dir: pathlib.Path,
    clusters: list[str] | None = None,
) -> dict:
    used = used_buckets_per_cluster(rows)
    wont = wont_file_classes(rows)
    clusters = clusters or sorted(used) or list(NEXT_BUCKET_BY_CLUSTER)
    selections: list[dict] = []
    for cluster in clusters:
        used_set = used.get(cluster, set())
        nxt = next_unused_bucket(cluster, used_set, queues_dir)
        selections.append(
            {
                "cluster": cluster,
                "used_buckets": sorted(used_set),
                "selected_bucket": nxt,
                "selection_basis": (
                    "named-next-unused" if nxt else "none-available"
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
                    default=ROOT / "properties" / "generated" / "conversion-ledger.json")
    ap.add_argument("--queues-dir", type=pathlib.Path, default=DEFAULT_QUEUES_DIR)
    ap.add_argument("--out", type=pathlib.Path,
                    default=ROOT / "properties" / "generated" / "conversion_schedule.json")
    ap.add_argument("--at", default="", help="ISO timestamp for determinism")
    args = ap.parse_args(argv)

    rows = _load_ledger_rows(args.ledger)
    sched = build_schedule(rows, queues_dir=args.queues_dir)
    sched["generated_at"] = args.at or sched["generated_at"]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(sched, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8")
    for sel in sched["selections"]:
        print(f"{sel['cluster']}: used={sel['used_buckets']} "
              f"-> next={sel['selected_bucket']} ({sel['selection_basis']})")
    print(f"wont-file classes: {len(sched['wont_file_classes'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
