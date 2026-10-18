#!/usr/bin/env python3
"""Freeze the repository's known conversion-question and review history."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.mine.question_history import (  # noqa: E402
    QuestionHistoryError,
    build_question_history_index,
    validate_question_history_index,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=ROOT / "properties" / "calibration" / "question-history-index.json",
    )
    args = parser.parse_args(argv)
    try:
        index = validate_question_history_index(build_question_history_index(ROOT))
        atomic_write_text(
            args.output,
            json.dumps(index, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        )
    except (OSError, QuestionHistoryError, ValueError) as exc:
        print(f"freeze-question-history-index: error: {exc}", file=sys.stderr)
        return 2
    audit = index["audit"]
    print(
        f"history index -> {args.output}: sources={audit['source_count']} "
        f"asked={audit['asked_site_count']} reserved={audit['reserved_site_count']} "
        f"unbound={audit['unbound_record_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
