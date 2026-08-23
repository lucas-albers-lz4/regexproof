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
# Context files above this size are refused (Luna r2 #7 — unbounded reads).
MAX_FILE_BYTES = 8 * 1024 * 1024


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
    token: str = "",
    *,
    min_window: int = MIN_WINDOW,
    max_window: int = MAX_WINDOW,
) -> dict:
    """Return a bounded 50-150 line window centered on ``line`` (Luna r1
    #8: the window NEVER exceeds ``max_window``, even at file edges — a
    200-line file with target line 1 yields ≤150 lines, not the whole
    file). The checkout is protected against escapes (#9: absolute paths,
    ``..``, and symlinks may not read outside the resolved checkout)."""
    # #9: resolve both sides and require the target beneath the checkout.
    resolved_checkout = checkout.resolve()
    raw_target = (resolved_checkout / path).resolve()
    try:
        raw_target.relative_to(resolved_checkout)
    except ValueError:
        sys.exit(
            f"error: {path} resolves outside the checkout "
            f"({resolved_checkout}) — escape refused"
        )
    if line < 1:
        sys.exit(f"error: line {line} is out of range (must be >= 1)")
    if not raw_target.is_file():
        sys.exit(f"error: {path} not found under {checkout}")
    full = raw_target
    # Size cap (Luna r2 #7): never read+split an unbounded file — the
    # repository's other extraction paths are capped too.
    if full.stat().st_size > MAX_FILE_BYTES:
        sys.exit(f"error: {path} is {full.stat().st_size} bytes (> {MAX_FILE_BYTES})")
    lines = full.read_text(encoding="utf-8", errors="replace").splitlines()
    total = len(lines)
    if line > total:
        sys.exit(f"error: line {line} exceeds file length {total}")
    half = max(1, min(max_window, max(min_window, 8)) // 2)
    start = max(1, line - half)
    end = min(total, line + half)
    # Hard bound: never exceed max_window even at edges. If the centered
    # window is too short (edge), extend to the other side up to the cap.
    if end - start + 1 < min_window:
        shortfall = min_window - (end - start + 1)
        extend = min(shortfall, max(0, start - 1))
        start -= extend
        shortfall -= extend
        end += min(shortfall, max(0, total - end))
    if end - start + 1 > max_window:
        excess = end - start + 1 - max_window
        # Trim from the side farther from the target first, then evenly.
        above = end - line
        below = line - start
        if above > below:
            end -= min(excess, above)
            excess -= min(excess, above)
        start += excess
    window = [
        {"line": i + 1, "text": lines[i], "is_target": (i + 1 == line)}
        for i in range(start - 1, end)
    ]
    return {
        "path": str(full.relative_to(resolved_checkout)),
        "target_line": line,
        "token": token or pathlib.Path(path).name,
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
    """Structurally enforce the required review fields (Luna r1 #7:
    ``input_format_constraint`` is required, not optional; ``unverified``
    derives ``claimed`` — a real queue-vocabulary state, never an
    off-vocabulary ``claimed_unverified``)."""
    r = str(form.get("witness_reachability") or "")
    if r not in REACHABILITY:
        sys.exit(
            f"error: witness_reachability required, one of {sorted(REACHABILITY)}"
        )
    if not str(form.get("evidence_ref") or "").strip():
        sys.exit("error: evidence_ref required (window slice or format spec)")
    if not str(form.get("input_format_constraint") or "").strip():
        sys.exit("error: input_format_constraint required (the human states "
                 "what input format the property constrains)")
    # Structural window validation (CodeRabbit #569: window must be an
    # OBJECT — a list passes the key check then crashes on .get()).
    window = form.get("window")
    if not isinstance(window, dict):
        sys.exit("error: review form window must be an object")
    for key in ("path", "target_line", "window_lines", "lines"):
        if key not in window:
            sys.exit(f"error: review form missing window.{key} (structural)")
    # Type/range validation (Luna r2 #6 / r3 #5): target_line int >= 1,
    # window_lines positive, lines non-empty and target present. Strict
    # isinstance — int(1.9) coercion must NOT pass a float (Luna r3 #5).
    target_raw = window.get("target_line")
    window_raw = window.get("window_lines")
    if not isinstance(target_raw, int) or isinstance(target_raw, bool):
        sys.exit("error: review form window.target_line must be an integer")
    if not isinstance(window_raw, int) or isinstance(window_raw, bool):
        sys.exit("error: review form window.window_lines must be an integer")
    target_line = target_raw
    window_lines = window_raw
    if target_line < 1:
        sys.exit("error: review form window.target_line must be >= 1")
    if window_lines < 1:
        sys.exit("error: review form window.window_lines must be positive")
    if not isinstance(window.get("lines"), list) or not window["lines"]:
        sys.exit("error: review form window.lines must be a non-empty list")

    # EVERY line entry must be a strict int (Luna r8 #4: a malformed
    # non-target entry must not pass just because the target is valid).
    for entry in window["lines"]:
        line_val = entry.get("line") if isinstance(entry, dict) else None
        if not isinstance(line_val, int) or isinstance(line_val, bool):
            sys.exit(
                "error: review form window.lines entries must be objects "
                "with an integer 'line'"
            )

    def _is_target(entry: object) -> bool:
        # line is strict int (already validated above) — target search.
        if not isinstance(entry, dict):
            return False
        line_val = entry.get("line")
        if not isinstance(line_val, int) or isinstance(line_val, bool):
            return False
        return line_val == target_line

    if not any(_is_target(entry) for entry in window["lines"]):
        sys.exit("error: review form window.lines must contain the target line")
    if r == "unreachable":
        form["queue_action"] = "skipped_unreachable"
    elif r == "unverified":
        form["queue_action"] = "claimed"  # queue vocabulary — stays a queue state
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

    path, line, token = parse_site(args.site)
    window = extract_window(args.checkout, path, line, token=token)
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
