"""ReDoS runner: extractor JSONL → findings JSONL (deterministic by regex_id)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from regexproof.redos.schema import make_finding
from regexproof.redos.tools import run_python_detector, run_recheck, run_safe_regex2

# USENIX Sec'22: non-backtracking engines can still have super-linear cases;
# we do not claim safe — we mark unsupported for stock RE2 ReDoS tooling.
RE2_UNSUPPORTED_REASON = (
    "linear-time-engine: Go RE2 has no backtracking ReDoS check; "
    "see USENIX Sec'22 super-linear caveat (docs/REDOS.md)"
)


def analyze_record(rec: dict[str, Any], *, triage: bool = True) -> list[dict[str, Any]]:
    """Return one or more findings for an extractor record."""
    dialect = rec.get("dialect") or ""
    pattern = rec.get("pattern") or ""
    flags = rec.get("flags") or ""
    site = rec.get("site") or ""
    regex_id = rec["regex_id"]
    source = {
        "repo": rec.get("repo"),
        "file": rec.get("file"),
        "call_kind": rec.get("call_kind"),
    }
    findings: list[dict[str, Any]] = []

    if dialect in ("re2",):
        findings.append(
            make_finding(
                regex_id=regex_id,
                tool="redos-stage",
                tool_version="1",
                result="unsupported",
                dialect=dialect,
                pattern=pattern,
                flags=flags,
                site=site,
                severity=None,
                confidence=None,
                source=source,
                error_message=RE2_UNSUPPORTED_REASON,
            )
        )
        return findings

    if dialect == "ecma":
        raw = run_recheck(pattern, flags)
        findings.append(_tool_to_finding(raw, rec, source, default_tool="recheck"))
        if triage:
            triage_raw = run_safe_regex2(pattern)
            findings.append(
                _tool_to_finding(triage_raw, rec, source, default_tool="safe-regex2")
            )
        return findings

    if dialect == "py_re":
        raw = run_python_detector(pattern, flags)
        findings.append(_tool_to_finding(raw, rec, source, default_tool="regexploit"))
        return findings

    if dialect == "pcre":
        findings.append(
            make_finding(
                regex_id=regex_id,
                tool="redos-stage",
                tool_version="1",
                result="unsupported",
                dialect=dialect,
                pattern=pattern,
                flags=flags,
                site=site,
                source=source,
                error_message="pcre ReDoS not wired in Phase 4; use JS/Python detectors",
            )
        )
        return findings

    findings.append(
        make_finding(
            regex_id=regex_id,
            tool="redos-stage",
            tool_version="1",
            result="error",
            dialect=dialect or "py_re",
            pattern=pattern,
            flags=flags,
            site=site,
            source=source,
            error_message=f"unknown dialect {dialect!r}",
        )
    )
    return findings


def _tool_to_finding(
    raw: dict[str, Any],
    rec: dict[str, Any],
    source: dict[str, Any],
    *,
    default_tool: str,
) -> dict[str, Any]:
    result = raw.get("result") or "error"
    if result not in ("vulnerable", "safe", "error", "timeout", "unsupported"):
        result = "error"
    return make_finding(
        regex_id=rec["regex_id"],
        tool=str(raw.get("tool") or default_tool),
        tool_version=str(raw.get("tool_version") or "unknown"),
        result=result,
        dialect=rec.get("dialect") or "ecma",
        pattern=rec.get("pattern") or "",
        flags=rec.get("flags") or "",
        site=rec.get("site") or "",
        severity=raw.get("severity"),
        confidence=raw.get("confidence"),
        source=source,
        error_message=raw.get("error_message"),
        detail=raw.get("detail"),
    )


def run_file(input_path: Path, output_path: Path, *, triage: bool = True) -> int:
    records: list[dict[str, Any]] = []
    with input_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))

    findings: list[dict[str, Any]] = []
    for rec in records:
        findings.extend(analyze_record(rec, triage=triage))

    findings.sort(key=lambda f: (f["regex_id"], f["tool"]))
    with output_path.open("w", encoding="utf-8") as out:
        for f in findings:
            out.write(json.dumps(f, sort_keys=True) + "\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path, required=True, help="extractor JSONL")
    ap.add_argument("--out", type=Path, required=True, help="ReDoS findings JSONL")
    ap.add_argument(
        "--no-triage",
        action="store_true",
        help="skip safe-regex2 triage for ECMA patterns",
    )
    args = ap.parse_args(argv)
    return run_file(args.input, args.out, triage=not args.no_triage)


if __name__ == "__main__":
    raise SystemExit(main())
