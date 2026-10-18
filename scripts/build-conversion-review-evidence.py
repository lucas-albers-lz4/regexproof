#!/usr/bin/env python3
"""Bind every ranked conversion review to exact source windows and file hashes."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_text  # noqa: E402

CONTEXT_EXTRACTOR = ROOT / "scripts" / "context-extractor.py"
ALLOWED_DECISIONS = {"adopted", "skipped", "unresolved"}
REQUIRED_FIELDS = {
    "rank", "site", "pattern", "call_kind", "decision", "reason_code",
    "rationale", "regex_id",
}


class ReviewEvidenceError(ValueError):
    """Invalid review or source material for a frozen conversion shortlist."""


def _load_context_extractor():
    spec = importlib.util.spec_from_file_location(
        "context_extractor_for_review_evidence", CONTEXT_EXTRACTOR
    )
    if spec is None or spec.loader is None:
        raise ReviewEvidenceError("cannot load context-extractor.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_reviews(
    path: pathlib.Path,
    *,
    pin: str,
    cohort_id: str,
    sample_size: int,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    ranks: set[int] = set()
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise ReviewEvidenceError(f"cannot read review file {path}: {exc}") from exc
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ReviewEvidenceError(f"review row {number} is invalid JSON: {exc.msg}") from exc
        if not isinstance(row, dict) or not REQUIRED_FIELDS.issubset(row):
            raise ReviewEvidenceError(f"review row {number} is missing required fields")
        if type(row["rank"]) is not int or not 1 <= row["rank"] <= sample_size:
            raise ReviewEvidenceError(
                f"review row {number} rank must be in 1..{sample_size}"
            )
        if row["rank"] in ranks:
            raise ReviewEvidenceError(f"duplicate review rank {row['rank']}")
        ranks.add(row["rank"])
        if row["decision"] not in ALLOWED_DECISIONS:
            raise ReviewEvidenceError(f"review row {number} has an unsupported decision")
        for field in ("site", "pattern", "call_kind", "reason_code", "rationale", "regex_id"):
            if not isinstance(row[field], str) or not row[field].strip():
                raise ReviewEvidenceError(f"review row {number} {field} must be non-empty")
        if row.get("source_pin", pin) != pin:
            raise ReviewEvidenceError(f"review row {number} pin differs from the frozen source")
        if row.get("cohort_id", cohort_id) != cohort_id:
            raise ReviewEvidenceError(f"review row {number} cohort differs from --cohort-id")
        rows.append(row)
    if ranks != set(range(1, sample_size + 1)):
        raise ReviewEvidenceError(
            f"review file must contain the complete ranked top-{sample_size} sample rows (ranks 1..{sample_size})"
        )
    return sorted(rows, key=lambda row: row["rank"])


def build_evidence(
    *,
    reviews_path: pathlib.Path,
    shortlist_path: pathlib.Path,
    run_context_path: pathlib.Path,
    checkout: pathlib.Path,
    repository_url: str,
    pin: str,
    cohort_id: str,
    site_path_prefix: str = "",
    sample_size: int = 15,
) -> dict[str, Any]:
    context = _load_context_extractor()
    if type(sample_size) is not int or not 1 <= sample_size <= 15:
        raise ReviewEvidenceError("sample_size must be in 1..15")
    rows = _load_reviews(
        reviews_path, pin=pin, cohort_id=cohort_id, sample_size=sample_size
    )
    try:
        shortlist_raw = shortlist_path.read_bytes()
        shortlist = json.loads(shortlist_raw)
        run_context_raw = run_context_path.read_bytes()
        run_context = json.loads(run_context_raw)
    except (OSError, json.JSONDecodeError) as exc:
        raise ReviewEvidenceError(f"cannot read shortlist/run context: {exc}") from exc
    if not isinstance(shortlist, dict) or not isinstance(shortlist.get("keep"), list):
        raise ReviewEvidenceError("shortlist must contain a keep list")
    if len(shortlist["keep"]) != sample_size:
        raise ReviewEvidenceError(
            f"shortlist must contain complete ranked top-{sample_size} candidates"
        )
    context_url = run_context.get("repository_url") if isinstance(run_context, dict) else None
    if (
        not isinstance(context_url, str)
        or run_context.get("source_pin") != pin
        or run_context.get("cohort_id") != cohort_id
        or context_url.rstrip("/") != repository_url.rstrip("/")
    ):
        raise ReviewEvidenceError("run context does not bind this cohort, repository, and pin")
    prefix = site_path_prefix.strip("/")
    if prefix and any(part in {"", ".", ".."} for part in prefix.split("/")):
        raise ReviewEvidenceError("site path prefix must be a safe relative path")
    shortlist_sites: dict[int, str] = {}
    for rank, (short, review) in enumerate(zip(shortlist["keep"], rows), start=1):
        if not isinstance(short, dict):
            raise ReviewEvidenceError(f"shortlist rank {rank} must be an object")
        try:
            short_path, short_line, short_token = context.parse_site(short.get("site", ""))
            review_path, review_line, review_token = context.parse_site(review["site"])
        except SystemExit as exc:
            raise ReviewEvidenceError(f"invalid site at shortlist rank {rank}: {exc}") from exc
        expected_path = f"{prefix}/{review_path}" if prefix else review_path
        file_matches = "file" not in short or short.get("file") == expected_path
        if (
            short_path != expected_path
            or (short_line, short_token) != (review_line, review_token)
            or not file_matches
            or any(short.get(field) != review.get(field) for field in ("pattern", "call_kind"))
        ):
            raise ReviewEvidenceError(f"review rank {rank} does not match the frozen shortlist")
        shortlist_sites[rank] = str(short["site"])
    candidates = []
    source_files: dict[str, dict[str, str]] = {}
    for row in rows:
        path, line, token = context.parse_site(row["site"])
        window = context.extract_window(checkout, path, line, token=token)
        binding = context.pinned_source_binding(checkout, repository_url, pin, path)
        source_files[path] = binding
        candidates.append({
            "rank": row["rank"],
            "site": row["site"],
            "shortlist_site": shortlist_sites[row["rank"]],
            "pattern": row["pattern"],
            "call_kind": row["call_kind"],
            "decision": row["decision"],
            "reason_code": row["reason_code"],
            "rationale": row["rationale"],
            "regex_id": row["regex_id"],
            "source_pin": pin,
            "source_binding": binding,
            "window": window,
        })
    return {
        "schema_version": "1",
        "cohort_id": cohort_id,
        "repository_url": repository_url.rstrip("/"),
        "source_pin": pin,
        "shortlist_site_path_prefix": prefix,
        "review_source": {
            "sha256": hashlib.sha256(reviews_path.read_bytes()).hexdigest(),
            "row_count": len(candidates),
        },
        "shortlist_source": {
            "sha256": hashlib.sha256(shortlist_raw).hexdigest(),
            "row_count": len(shortlist["keep"]),
        },
        "run_context_sha256": hashlib.sha256(run_context_raw).hexdigest(),
        "source_files": [source_files[path] for path in sorted(source_files)],
        "candidates": candidates,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reviews", type=pathlib.Path, required=True)
    parser.add_argument("--shortlist", type=pathlib.Path, required=True)
    parser.add_argument("--run-context", type=pathlib.Path, required=True)
    parser.add_argument("--checkout", type=pathlib.Path, required=True)
    parser.add_argument("--repository-url", required=True)
    parser.add_argument("--pin", required=True)
    parser.add_argument("--cohort-id", required=True)
    parser.add_argument(
        "--site-path-prefix",
        default="",
        help="explicit path prefix present in shortlist sites but absent from source checkout sites",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=15,
        help="number of ranked shortlist/review rows (1..15; default: 15)",
    )
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args(argv)
    try:
        evidence = build_evidence(
            reviews_path=args.reviews,
            shortlist_path=args.shortlist,
            run_context_path=args.run_context,
            checkout=args.checkout,
            repository_url=args.repository_url,
            pin=args.pin,
            cohort_id=args.cohort_id,
            site_path_prefix=args.site_path_prefix,
            sample_size=args.sample_size,
        )
        atomic_write_text(
            args.output,
            json.dumps(evidence, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        )
    except (OSError, ReviewEvidenceError, SystemExit) as exc:
        message = str(exc)
        if message:
            print(f"build-conversion-review-evidence: {message}", file=sys.stderr)
        return 2
    print(
        f"source-bound review evidence -> {args.output}: "
        f"{args.sample_size} candidates"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
