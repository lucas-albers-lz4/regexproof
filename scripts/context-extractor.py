#!/usr/bin/env python3
"""Wave C (#558): context extractor + review form.

Extracts a 50-150 line window around a canonical site (``file:line:token``)
from a corpus checkout, and emits the REVIEW FORM for a human reviewer:
sink context + the REQUIRED ``witness_reachability`` enum with an evidence
reference (the extracted window itself or a cited format spec).

``witness_reachability`` is schema-controlled (reachable / unreachable /
unverified) and structurally enforced: the review form requires it and an
``evidence_ref``. ``unverified`` never becomes a contract ledger row (it
stays a queue state); ``unreachable`` is a queue ``skipped_unreachable``
reason, never a contract.

Usage::

  python3 scripts/context-extractor.py --corpus openwrt_packages \\
      --checkout /path/to/tree \\
      --site net/ddns-scripts/files/usr/lib/ddns/update_aliyun_com.sh:115:RecordId \\
      --review-form -o /tmp/review-aliyun.json
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

REACHABILITY = frozenset({"reachable", "unreachable", "unverified"})

MIN_WINDOW = 50
MAX_WINDOW = 150


def parse_site(site: str) -> tuple[str, int, str]:
    """Split ``path:line:token`` (line 1-based)."""
    parts = str(site or "").rsplit(":", 2)
    if len(parts) != 3:
        sys.exit(f"error: site {site!r} must be path:line:token")
    path, line_s, token = parts
    try:
        line = int(line_s)
    except ValueError:
        sys.exit(f"error: site {site!r} line {line_s!r} is not an integer")
    return path, line, token


def extract_window(
    checkout: pathlib.Path,
    path: str,
    line: int,
    *,
    min_window: int = MIN_WINDOW,
    max_window: int = MAX_WINDOW,
) -> dict:
    """Return a 50-150 line window centered on ``line`` (clamped to file
    bounds) with the line itself flagged."""
    full = checkout / path
    if not full.is_file():
        sys.exit(f"error: {path} not found under {checkout}")
    lines = full.read_text(encoding="utf-8", errors="replace").splitlines()
    total = len(lines)
    half = max(min_window, min(max_window, max(min_window, 8))) // 2
    start = max(1, line - half)
    end = min(total, line + half)
    if end - start + 1 < min_window:
        # File smaller than the window: take the whole file.
        start, end = 1, total
    window = [
        {"line": i + 1, "text": lines[i], "is_target": (i + 1 == line)}
        for i in range(start - 1, end)
    ]
    return {
        "path": path,
        "target_line": line,
        "token": str(pathlib.Path(path).name),
        "window_start": start,
        "window_end": end,
        "window_lines": len(window),
        "lines": window,
    }


def review_form(
    corpus: str,
    site: str,
    window: dict,
    *,
    input_format_constraint: str = "",
) -> dict:
    """The review form: context + required witness_reachability + evidence
    ref. ``input_format_constraint`` is a REQUIRED structural field at
    adoption (the human states what input format the property constrains)."""
    return {
        "schema_version": "1",
        "corpus": corpus,
        "site": site,
        "window": window,
        "witness_reachability": None,  # required: reachable|unreachable|unverified
        "evidence_ref": "",  # required: the window slice or a cited format spec
        "input_format_constraint": input_format_constraint,
        "review_notes": "",
    }


def validate_form(form: dict) -> None:
    """Structurally enforce the required review fields."""
    r = str(form.get("witness_reachability") or "")
    if r not in REACHABILITY:
        sys.exit(
            f"error: witness_reachability required, one of {sorted(REACHABILITY)}"
        )
    if not str(form.get("evidence_ref") or "").strip():
        sys.exit("error: evidence_ref required (window slice or format spec)")
    if r == "unreachable":
        form["queue_action"] = "skipped_unreachable"
    elif r == "unverified":
        form["queue_action"] = "claimed_unverified"  # stays a queue state
    else:
        form["queue_action"] = "contractable"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--corpus", default="")
    ap.add_argument("--checkout", type=pathlib.Path, default=None)
    ap.add_argument("--site", default="", help="path:line:token")
    ap.add_argument("--input-format-constraint", default="")
    ap.add_argument("--review-form", action="store_true", help="emit review form")
    ap.add_argument("-o", "--output", type=pathlib.Path)
    ap.add_argument("--validate", metavar="FILE", help="validate a review form JSON")
    args = ap.parse_args(argv)

    if args.validate:
        form = json.loads(pathlib.Path(args.validate).read_text(encoding="utf-8"))
        validate_form(form)
        print(json.dumps(form, indent=2, sort_keys=True))
        return 0

    if not args.corpus or args.checkout is None or not args.site:
        ap.error("--corpus, --checkout and --site are required (unless --validate)")

    path, line, _token = parse_site(args.site)
    window = extract_window(args.checkout, path, line)
    out: dict = window
    if args.review_form:
        out = review_form(
            args.corpus,
            args.site,
            window,
            input_format_constraint=args.input_format_constraint,
        )
        if args.output is None:
            sys.exit(
                "error: --review-form requires -o (a human fills the form "
                "before it can be validated)"
            )
    text = json.dumps(out, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(f"context -> {args.output}: {window['window_lines']} lines "
              f"(target {window['target_line']})")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
