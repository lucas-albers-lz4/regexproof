#!/usr/bin/env python3
"""Merge a P1 ``--dir --ndjson`` shell record export into a probe draft (P3-A).

Thin CLI over ``regexproof.admission.merge_probe``.  The construct-counting
path matches walk.py exactly (see the module docstring); the AC4 under-report
preflight is ENFORCED here — an empty ``predicted_buckets`` result exits 2
and writes nothing.

Usage:
    python scripts/merge-probe-draft.py DRAFT.json --ndjson EXPORT.ndjson -o MERGED.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.admission.merge_probe import merge_draft  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="merge-probe-draft.py",
        description="Merge a P1 --dir --ndjson shell export into a probe "
                    "draft (populates probe.regex_sites + "
                    "probe.predicted_buckets via the walk.py construct path).",
    )
    ap.add_argument("draft", metavar="DRAFT.json",
                    help="probe-corpus-admission.py draft (positional)")
    ap.add_argument("--ndjson", required=True, metavar="EXPORT.ndjson",
                    help="P1 script --dir --ndjson FULL-record export")
    ap.add_argument("-o", "--output", required=True, metavar="MERGED.json")
    args = ap.parse_args(argv)

    draft = json.loads(Path(args.draft).read_text(encoding="utf-8"))
    records = [
        json.loads(line)
        for line in Path(args.ndjson).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    merged = merge_draft(draft, records)
    buckets = merged["probe"]["predicted_buckets"]
    if not buckets:
        print("merge-probe-draft: EMPTY predicted_buckets — under-report "
              "forces triage-trial/no-go (AC4); refusing to emit a go-able "
              "draft", file=sys.stderr)
        return 2
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(merged, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    print(f"merged -> {out}: regex_sites={merged['probe']['regex_sites']} "
          f"predicted_buckets={dict(buckets)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
