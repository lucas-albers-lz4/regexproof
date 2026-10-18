#!/usr/bin/env python3
"""Freeze a complete source review of one exact-pin P2 inventory member."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib
import subprocess
import sys
from collections import Counter
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.mine.cohort_manifest import (  # noqa: E402
    CohortManifestError,
    validate_manifest,
)

CONTEXT_EXTRACTOR = ROOT / "scripts" / "context-extractor.py"
DECISIONS = {"adopted", "skip", "unresolved"}


class ReviewEvidenceError(ValueError):
    """Invalid or incomplete source-review evidence."""


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load_context_extractor():
    spec = importlib.util.spec_from_file_location(
        "context_extractor_for_p2_review", CONTEXT_EXTRACTOR
    )
    if spec is None or spec.loader is None:
        raise ReviewEvidenceError("cannot load context-extractor.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _read_sites(path: pathlib.Path) -> tuple[list[dict[str, Any]], bytes]:
    raw = path.read_bytes()
    rows: list[dict[str, Any]] = []
    for number, line in enumerate(raw.splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ReviewEvidenceError(
                f"{path}:{number}: invalid NDJSON: {exc.msg}"
            ) from exc
        if not isinstance(row, dict):
            raise ReviewEvidenceError(f"{path}:{number}: row must be an object")
        rows.append(row)
    return rows, raw


def _load_reviews(path: pathlib.Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ReviewEvidenceError(f"{path}: invalid JSON: {exc.msg}") from exc
    if not isinstance(value, dict) or value.get("schema_version") != "1":
        raise ReviewEvidenceError("review source must use schema_version 1")
    author = value.get("author")
    reviewer = value.get("reviewer")
    second_pass = value.get("second_pass")
    if not isinstance(author, str) or not author.strip():
        raise ReviewEvidenceError("review source author must be non-empty")
    if not isinstance(reviewer, str) or not reviewer.strip():
        raise ReviewEvidenceError("review source reviewer must be non-empty")
    if type(second_pass) is not bool or not isinstance(value.get("reviews"), list):
        raise ReviewEvidenceError("review source needs second_pass and reviews")
    if type(value.get("same_model_or_agent")) is not bool:
        raise ReviewEvidenceError("review source must state whether the author/reviewer were the same model")
    if not second_pass:
        raise ReviewEvidenceError("P2 review evidence requires a recorded second pass")
    return value, raw


def build_evidence(
    *,
    cohort_path: pathlib.Path,
    inventory_path: pathlib.Path,
    sites_path: pathlib.Path,
    reviews_path: pathlib.Path,
    checkout: pathlib.Path,
    repo_id: str,
    pin: str,
) -> dict[str, Any]:
    context = _load_context_extractor()
    cohort_raw = cohort_path.read_bytes()
    try:
        cohort = validate_manifest(json.loads(cohort_raw))
    except (json.JSONDecodeError, CohortManifestError) as exc:
        raise ReviewEvidenceError(f"invalid frozen cohort manifest: {exc}") from exc
    inventory_raw = inventory_path.read_bytes()
    try:
        inventory = json.loads(inventory_raw)
    except json.JSONDecodeError as exc:
        raise ReviewEvidenceError(f"invalid source inventory JSON: {exc.msg}") from exc
    cohort_sha = _sha256(cohort_raw)
    if (
        inventory.get("cohort_id") != cohort["cohort_id"]
        or inventory.get("manifest_digest") != cohort["manifest_digest"]
        or inventory.get("cohort_manifest_sha256") != cohort_sha
    ):
        raise ReviewEvidenceError("source inventory is not bound to the supplied cohort")

    sites, sites_raw = _read_sites(sites_path)
    sites_sha = _sha256(sites_raw)
    if (
        inventory.get("summary", {}).get("source_sites") != len(sites)
        or inventory.get("summary", {}).get("source_sites_ndjson_sha256") != sites_sha
    ):
        raise ReviewEvidenceError("source-site rows do not match inventory count/digest")

    members = [
        member for member in cohort["repos"]
        if member["repo_id"] == repo_id and member["pin"] == pin
    ]
    if len(members) != 1:
        raise ReviewEvidenceError("repo and pin must identify one frozen cohort member")
    member = members[0]
    selected = [
        row for row in sites
        if row.get("repo_id") == repo_id and row.get("pin") == pin
    ]
    if not selected:
        raise ReviewEvidenceError("no source sites exist for the selected cohort member")
    review_doc, reviews_raw = _load_reviews(reviews_path)
    review_rows = review_doc["reviews"]
    by_id: dict[str, dict[str, Any]] = {}
    required = {"regex_id", "site", "pattern", "decision", "reason_code", "rationale", "review_refs"}
    for number, review in enumerate(review_rows, 1):
        if not isinstance(review, dict) or not required.issubset(review):
            raise ReviewEvidenceError(f"review row {number} is missing required fields")
        regex_id = review["regex_id"]
        if not isinstance(regex_id, str) or not regex_id or regex_id in by_id:
            raise ReviewEvidenceError(f"review row {number} has an empty or duplicate regex_id")
        if review["decision"] not in DECISIONS:
            raise ReviewEvidenceError(
                f"review row {number} decision must be adopted, skip, or unresolved"
            )
        for field in ("site", "pattern", "reason_code", "rationale"):
            if not isinstance(review[field], str) or not review[field].strip():
                raise ReviewEvidenceError(f"review row {number} {field} must be non-empty")
        if not isinstance(review["review_refs"], list) or not review["review_refs"]:
            raise ReviewEvidenceError(f"review row {number} needs source review_refs")
        if type(review.get("product_question_asked", False)) is not bool:
            raise ReviewEvidenceError(f"review row {number} product_question_asked must be boolean")
        if review["decision"] == "adopted" and not review.get("product_question_asked", False):
            raise ReviewEvidenceError(f"review row {number} adopted contract has no attempted question")
        by_id[regex_id] = review

    selected_ids = {row.get("regex_id") for row in selected}
    if len(selected_ids) != len(selected) or selected_ids != set(by_id):
        missing = sorted(str(item) for item in selected_ids - set(by_id))
        extra = sorted(set(by_id) - selected_ids)
        raise ReviewEvidenceError(
            f"reviews must cover the complete exact-pin member; missing={missing}, extra={extra}"
        )

    repo_url = member["url"].rstrip("/")
    source_bindings: dict[str, dict[str, Any]] = {}
    reviewed_sites: list[dict[str, Any]] = []
    for source in sorted(selected, key=lambda row: row["regex_id"]):
        review = by_id[source["regex_id"]]
        if review["site"] != source["site"] or review["pattern"] != source["pattern"]:
            raise ReviewEvidenceError(
                f"review identity/pattern differs from source inventory: {source['regex_id']}"
            )
        source_file = source["source_file"]
        if source_file not in source_bindings:
            binding = context.pinned_source_binding(checkout, repo_url, pin, source_file)
            if binding["sha256"] != source["source_file_sha256"]:
                raise ReviewEvidenceError(f"source file hash differs from inventory: {source_file}")
            blob = subprocess.run(
                ["git", "-C", str(checkout), "rev-parse", f"{pin}:{source_file}"],
                check=True,
                capture_output=True,
                text=True,
                timeout=10,
            ).stdout.strip()
            if blob != source["git_blob_oid"]:
                raise ReviewEvidenceError(f"Git blob differs from inventory: {source_file}")
            source_bindings[source_file] = binding | {"git_blob_oid": blob}

        source_path, source_line, token = context.parse_site(source["site"])
        windows = [
            {
                "purpose": "regex_site",
                "window": context.extract_window(
                    checkout, source_path, source_line, token=token
                ),
            }
        ]
        for ref in review["review_refs"]:
            if not isinstance(ref, dict) or not isinstance(ref.get("path"), str):
                raise ReviewEvidenceError("review_refs must contain path/line/why objects")
            if type(ref.get("line")) is not int or not isinstance(ref.get("why"), str) or not ref["why"].strip():
                raise ReviewEvidenceError("review_refs need an integer line and non-empty why")
            path = ref["path"]
            if path not in source_bindings:
                source_bindings[path] = context.pinned_source_binding(checkout, repo_url, pin, path)
            windows.append({
                "purpose": ref["why"],
                "window": context.extract_window(checkout, path, ref["line"]),
            })
        reviewed_sites.append({
            "regex_id": source["regex_id"],
            "source_site_id": source["source_site_id"],
            "site": source["site"],
            "source_file": source_file,
            "source_file_sha256": source["source_file_sha256"],
            "git_blob_oid": source["git_blob_oid"],
            "pattern": source["pattern"],
            "dialect_family": source["dialect_family"],
            "call_kind": source["call_kind"],
            "decision": review["decision"],
            "reason_code": review["reason_code"],
            "rationale": review["rationale"],
            "source_windows": windows,
            "product_question_asked": review.get("product_question_asked", False),
        })

    counts = Counter(row["decision"] for row in reviewed_sites)
    return {
        "schema_version": "1",
        "artifact_kind": "p2-exact-pin-source-review",
        "observed_at": review_doc.get("observed_at", ""),
        "cohort_id": cohort["cohort_id"],
        "manifest_digest": cohort["manifest_digest"],
        "repository": {
            "repo_id": repo_id,
            "url": repo_url,
            "pin": pin,
            "dialect_family": member["dialect_family"],
            "inventory_status": next(
                row["status"] for row in inventory["repositories"]
                if row["repo_id"] == repo_id and row["pin"] == pin
            ),
        },
        "source_inventory": {
            "inventory_sha256": _sha256(inventory_raw),
            "sites_ndjson_sha256": sites_sha,
            "source_site_count_total": len(sites),
            "member_site_count": len(selected),
        },
        "review_process": {
            "author": review_doc["author"],
            "reviewer": review_doc["reviewer"],
            "second_pass_recorded": review_doc["second_pass"],
            "same_model_or_agent": review_doc.get("same_model_or_agent"),
            "review_source_sha256": _sha256(reviews_raw),
        },
        "coverage": {
            "source_sites_reviewed": len(reviewed_sites),
            "source_sites_unreviewed_in_scope": 0,
            "skip": counts.get("skip", 0),
            "unresolved": counts.get("unresolved", 0),
            "adopted_contracts": counts.get("adopted", 0),
            "product_questions_asked": sum(
                1 for row in reviewed_sites if row["product_question_asked"]
            ),
            "interpretation": "complete raw-site review for this member only; unresolved rows remain outside product-question denominators",
        },
        "source_files": [source_bindings[key] for key in sorted(source_bindings)],
        "sites": reviewed_sites,
        "limitations": review_doc.get("limitations", []),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cohort", type=pathlib.Path, required=True)
    parser.add_argument("--inventory", type=pathlib.Path, required=True)
    parser.add_argument("--sites", type=pathlib.Path, required=True)
    parser.add_argument("--reviews", type=pathlib.Path, required=True)
    parser.add_argument("--checkout", type=pathlib.Path, required=True)
    parser.add_argument("--repo-id", required=True)
    parser.add_argument("--pin", required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args(argv)
    try:
        evidence = build_evidence(
            cohort_path=args.cohort,
            inventory_path=args.inventory,
            sites_path=args.sites,
            reviews_path=args.reviews,
            checkout=args.checkout,
            repo_id=args.repo_id,
            pin=args.pin,
        )
        atomic_write_text(
            args.output,
            json.dumps(evidence, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        )
        args.output.chmod(0o644)
    except (OSError, subprocess.SubprocessError, ReviewEvidenceError, SystemExit) as exc:
        message = str(exc)
        if message:
            print(f"build-p2-source-review-evidence: {message}", file=sys.stderr)
        return 2
    coverage = evidence["coverage"]
    print(
        f"P2 source review -> {args.output}: "
        f"{coverage['source_sites_reviewed']} sites; "
        f"{coverage['skip']} skipped; {coverage['unresolved']} unresolved; "
        f"{coverage['adopted_contracts']} adopted; "
        f"{coverage['product_questions_asked']} product questions asked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
