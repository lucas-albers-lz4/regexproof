#!/usr/bin/env python3
"""Wave 11 (#580): print yesterday's drain, queue pressure, survival, backlog.

Assembles committed artifacts only (conversion-ledger hop/starvation tables,
candidate ledger, mine queue, batch/state.json). No writes.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.pipeline_status import (  # noqa: E402
    render_status,
    render_weekly,
    snapshot,
)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true", help="Emit the snapshot as JSON")
    ap.add_argument(
        "--weekly",
        action="store_true",
        help="Markdown weekly projection (daily-mine job summary)",
    )
    ap.add_argument("--generated", type=Path, default=None)
    ap.add_argument("--state", type=Path, default=None)
    ap.add_argument("--ledger", type=Path, default=None)
    ap.add_argument("--queue", type=Path, default=None)
    ap.add_argument("--conversion-ledger", type=Path, default=None)
    ap.add_argument("--baseline", type=Path, default=None)
    args = ap.parse_args(argv)
    snap = snapshot(
        generated=args.generated,
        state_path=args.state,
        ledger_path=args.ledger,
        queue_path=args.queue,
        conversion_ledger=args.conversion_ledger,
        baseline_path=args.baseline,
    )
    if args.json:
        print(json.dumps(snap, indent=2, sort_keys=True, default=str))
        return 0
    if args.weekly:
        sys.stdout.write(render_weekly(snap))
        return 0
    sys.stdout.write(render_status(snap))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
