#!/usr/bin/env python3
"""Aggregate the independently-run CI corpus batch artifacts."""

from __future__ import annotations

import argparse
from pathlib import Path

from regexproof.batch.manifests import ROOT
from regexproof.batch.runner import PILOT_CORPORA, aggregate_batch


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        type=Path,
        default=ROOT / "properties" / "generated",
        help="directory containing per-corpus generated artifacts",
    )
    parser.add_argument(
        "--require-ground-truth",
        action="store_true",
        help="require reproduced ground truth for shared shape-5 SAT rows",
    )
    args = parser.parse_args(argv)
    aggregate_batch(
        list(PILOT_CORPORA),
        out_dir=args.out,
        require_ground_truth=args.require_ground_truth,
    )
    print("batch aggregate ok:", ", ".join(PILOT_CORPORA))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
