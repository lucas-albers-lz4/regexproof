#!/usr/bin/env python3
"""Create a deterministic frozen cohort manifest from a local JSON file."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.cohort_manifest import (  # noqa: E402
    CohortManifestError,
    build_manifest_from_path,
    dumps_manifest,
    write_manifest_atomic,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="offline JSON candidate file")
    parser.add_argument("--cohort-id", required=True, help="stable cohort identifier")
    parser.add_argument("--limit", required=True, type=int, help="maximum repositories")
    parser.add_argument("--output", required=True, type=Path, help="manifest output path")
    args = parser.parse_args(argv)
    try:
        input_path = args.input.resolve()
        output_path = args.output.resolve()
        if input_path == output_path:
            raise CohortManifestError("input and output paths must be different")
        if args.output.exists() and os.path.samefile(args.input, args.output):
            raise CohortManifestError("input and output paths must not alias the same file")
        manifest = build_manifest_from_path(args.input, args.cohort_id, args.limit)
        write_manifest_atomic(args.output, dumps_manifest(manifest))
    except (CohortManifestError, OSError) as exc:
        print(f"cohort-manifest: error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
