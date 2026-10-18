#!/usr/bin/env python3
"""Run exact-pin Base64URL encoder differentials for Magic JS."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.groundtruth.magic_js_base64url_replay import (  # noqa: E402
    QUESTION_IDS,
    run_differential_gate,
)
from regexproof.io_atomic import atomic_write_text  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        report = run_differential_gate(args.source_root)
        encoded = json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n"
        if args.output:
            atomic_write_text(args.output, encoded)
        print(
            f"Magic JS Base64URL gate: {report['differential_cases']} exact-source cases, "
            f"Node {report['node_version']}, {len(QUESTION_IDS)} product questions, "
            "0 mismatches; weakened plus mutation replay passed"
        )
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError, TimeoutError) as exc:
        print(f"Magic JS Base64URL gate failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
