#!/usr/bin/env python3
"""Select a deterministic, source-pinned 15-site conversion review sample."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.mine.conversion_allocation import (  # noqa: E402
    AllocationError,
    MAX_SAMPLE_SIZE,
    allocate_candidates,
    validate_population,
    verify_classification_binding,
    verify_inventory_binding,
)
from regexproof.mine.conversion_bucket_registry import (  # noqa: E402
    load_registry,
)
from regexproof.mine.corpus_lock import wave_status  # noqa: E402
from regexproof.mine.question_history import (  # noqa: E402
    check_candidates_new,
    validate_question_history_index,
    verify_index_current,
)

PIN_RE = re.compile(r"^[0-9a-f]{40}$")


class AllocationInputError(ValueError):
    """An allocation input is stale, mismatched, or not source authenticated."""


class DuplicateJSONKeyError(ValueError):
    """JSON input with ambiguous duplicate object keys."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateJSONKeyError(f"duplicate JSON key {key!r}")
        value[key] = item
    return value


def _json_file(path: pathlib.Path, label: str) -> tuple[Any, bytes]:
    if path.is_symlink() or not path.is_file():
        raise AllocationInputError(f"{label} is missing or a symlink: {path}")
    try:
        raw = path.read_bytes()
        value = json.loads(raw, object_pairs_hook=_unique_object)
    except (OSError, json.JSONDecodeError, DuplicateJSONKeyError) as exc:
        raise AllocationInputError(f"cannot read {label} {path}: {exc}") from exc
    return value, raw


def _digest_file(path: pathlib.Path, expected: str, label: str) -> str:
    if path.is_symlink() or not path.is_file():
        raise AllocationInputError(f"{label} is missing or a symlink: {path}")
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise AllocationInputError(f"{label} digest {actual} does not match population {expected}")
    return actual


def _bound_file_bytes(path: pathlib.Path, expected: str, label: str) -> tuple[str, bytes]:
    if path.is_symlink() or not path.is_file():
        raise AllocationInputError(f"{label} is missing or a symlink: {path}")
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise AllocationInputError(f"cannot read {label} {path}: {exc}") from exc
    actual = hashlib.sha256(raw).hexdigest()
    if actual != expected:
        raise AllocationInputError(f"{label} digest {actual} does not match population {expected}")
    return actual, raw


def _registered_site(site: str, registration: dict[str, Any]) -> str:
    """Remove the registration's repo/pin prefix from a source-site identity."""
    owner_repo = registration["repository_url"].removeprefix("https://github.com/")
    prefix = f"{owner_repo}@{registration['source_pin']}:"
    if site.startswith(prefix):
        return site[len(prefix):]
    if re.match(r"^[^/]+/[^/:]+@[0-9a-f]{40}:", site):
        raise AllocationInputError(f"registered source site uses a different repo or pin: {site}")
    return site


def _git(root: pathlib.Path, *args: str, binary: bool = False) -> str | bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=not binary,
        timeout=30,
    )
    return result.stdout if binary else result.stdout.strip()


def _verify_source_files(checkout: pathlib.Path, pin: str, candidates: list[dict[str, Any]]) -> int:
    if _git(checkout, "rev-parse", "HEAD") != pin:
        raise AllocationInputError("source checkout HEAD differs from the candidate population pin")
    if _git(checkout, "status", "--porcelain"):
        raise AllocationInputError("candidate source checkout must be clean")
    checked: dict[str, str] = {}
    for row in candidates:
        relative = row["source_file"]
        path = checkout / relative
        cursor = checkout
        for component in pathlib.PurePosixPath(relative).parts:
            cursor = cursor / component
            if cursor.is_symlink():
                raise AllocationInputError(
                    f"pinned source path has a symlink component: {relative}"
                )
        if not path.is_file():
            raise AllocationInputError(f"pinned source file is missing: {relative}")
        try:
            path.resolve().relative_to(checkout.resolve())
        except ValueError as exc:
            raise AllocationInputError(f"source path escapes checkout: {relative}") from exc
        expected = row["source_sha256"]
        prior = checked.get(relative)
        if prior is not None:
            if prior != expected:
                raise AllocationInputError(f"population gives conflicting hashes for {relative}")
            continue
        committed = _git(checkout, "show", f"{pin}:{relative}", binary=True)
        actual = hashlib.sha256(committed).hexdigest()
        if path.read_bytes() != committed or actual != expected:
            raise AllocationInputError(f"source bytes/hash mismatch for {relative}: {actual}")
        checked[relative] = expected
    return len(checked)


def build_allocation(args: argparse.Namespace) -> dict[str, Any]:
    population, population_raw = _json_file(args.population, "candidate population")
    population = validate_population(population)
    decision, decision_raw = _json_file(args.gate_decision, "GO decision")
    schedule, schedule_raw = _json_file(args.schedule, "conversion schedule")
    if not isinstance(decision, dict) or not isinstance(schedule, dict):
        raise AllocationInputError("GO decision and schedule must be JSON objects")
    if not isinstance(schedule.get("selections"), list):
        raise AllocationInputError("conversion schedule has no selections list")

    cluster = population["cluster"]
    pin = population["source_pin"]
    repository_url = population["repository_url"].rstrip("/")
    if not PIN_RE.fullmatch(pin):
        raise AllocationInputError("population has an invalid source pin")
    decision_pin = decision.get("corpus_pin") or (decision.get("probe") or {}).get("pin")
    if (
        decision.get("decision") != "go"
        or decision.get("corpus") != cluster
        or decision_pin != pin
        or str(decision.get("candidate_url") or "").rstrip("/") != repository_url
    ):
        raise AllocationInputError("GO decision does not bind this population cluster, URL, and pin")

    if any(not isinstance(row, dict) for row in schedule["selections"]):
        raise AllocationInputError("conversion schedule selections must be objects")
    selected = [row for row in schedule["selections"] if row.get("cluster") == cluster]
    if len(selected) != 1 or selected[0].get("selected_bucket") != population["idiom_bucket"]:
        raise AllocationInputError("scheduler did not select this population's idiom bucket")
    if selected[0].get("selection_basis") != "named-next-unused":
        raise AllocationInputError("scheduler selection basis does not admit allocation")

    registry = load_registry(args.bucket_registry)
    registry_digest = hashlib.sha256(
        json.dumps(registry, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if schedule.get("bucket_registry_digest") != registry_digest:
        raise AllocationInputError("schedule was built from a different bucket registry")
    entries = [
        row for row in registry.get("entries", [])
        if row.get("cluster") == cluster and row.get("bucket") == population["idiom_bucket"]
    ]
    if len(entries) != 1:
        raise AllocationInputError("population bucket must have exactly one registry entry")
    registration = entries[0]
    if (
        registration.get("source_pin") != pin
        or registration.get("repository_url", "").rstrip("/") != repository_url
        or registration.get("product_engine") != population["product_engine"]
    ):
        raise AllocationInputError("registration does not match population pin, URL, and engine")
    if args.sample_size > registration["max_candidates"]:
        raise AllocationInputError(
            f"sample-size {args.sample_size} exceeds registered candidate cap "
            f"{registration['max_candidates']}"
        )
    registered_sites = {
        _registered_site(site, registration) for site in registration["source_sites"]
    }
    representative_site = _registered_site(registration["contract_site"], registration)
    for candidate in population["candidates"]:
        if candidate["site"] not in registered_sites:
            raise AllocationInputError(
                f"candidate site is absent from the bucket registration: {candidate['site']}"
            )
        if candidate["trust_class"] not in registration["trust_map"]:
            raise AllocationInputError(
                f"candidate trust class is absent from the registration: {candidate['trust_class']}"
            )
        if candidate["site"] == representative_site:
            raise AllocationInputError(
                "candidate site is the already adopted representative contract site"
            )
    if args.events_log.is_symlink():
        raise AllocationInputError("corpus event log must not be a symlink")
    if wave_status(cluster, args.events_log) == "active":
        raise AllocationInputError("cannot allocate candidates while a corpus wave is active")

    inventory_sha, inventory_raw = _bound_file_bytes(
        args.inventory_file, population["inventory_sha256"], "inventory"
    )
    try:
        inventory_text = inventory_raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise AllocationInputError("inventory must be UTF-8 NDJSON") from exc
    inventory_rows_verified = verify_inventory_binding(population, inventory_text)
    outcome_ledger_sha = _digest_file(
        args.conversion_ledger,
        population["outcome_ledger_sha256"],
        "pre-outcome conversion ledger",
    )
    classification_sha, classification_raw = _bound_file_bytes(
        args.classification_file,
        population["classification_sha256"],
        "classification evidence",
    )
    try:
        classification = json.loads(
            classification_raw, object_pairs_hook=_unique_object
        )
    except (UnicodeDecodeError, json.JSONDecodeError, DuplicateJSONKeyError) as exc:
        raise AllocationInputError("classification evidence is not valid UTF-8 JSON") from exc
    classifications_verified = verify_classification_binding(population, classification)
    question_history_sha, question_history_raw = _bound_file_bytes(
        args.question_history_index,
        population["question_history_sha256"],
        "question-history index",
    )
    try:
        question_history = json.loads(
            question_history_raw, object_pairs_hook=_unique_object
        )
    except (UnicodeDecodeError, json.JSONDecodeError, DuplicateJSONKeyError) as exc:
        raise AllocationInputError("question-history index is not valid UTF-8 JSON") from exc
    question_history = verify_index_current(
        ROOT, validate_question_history_index(question_history)
    )
    history_sites_verified = check_candidates_new(population, question_history)
    source_files = _verify_source_files(args.checkout.resolve(), pin, population["candidates"])
    result = allocate_candidates(
        population,
        seed=args.selection_seed,
        sample_size=args.sample_size,
    )
    result.update({
        "population_sha256": hashlib.sha256(population_raw).hexdigest(),
        "gate_decision_sha256": hashlib.sha256(decision_raw).hexdigest(),
        "schedule_sha256": hashlib.sha256(schedule_raw).hexdigest(),
        "bucket_registry_sha256": registry_digest,
        "inventory_sha256_verified": inventory_sha,
        "outcome_ledger_sha256_verified": outcome_ledger_sha,
        "classification_sha256_verified": classification_sha,
        "question_history_sha256_verified": question_history_sha,
        "inventory_rows_reverified": inventory_rows_verified,
        "classifications_reverified": classifications_verified,
        "question_history_sites_reverified": history_sites_verified,
        "question_history_sources_reverified": question_history["audit"]["source_count"],
        "question_history_unbound_records": question_history["audit"]["unbound_record_count"],
        "source_checkout": str(args.checkout.resolve()),
        "source_files_reverified": source_files,
        "scheduler_selection_basis": selected[0]["selection_basis"],
        "scheduler_selected_bucket": selected[0]["selected_bucket"],
        "registered_candidate_cap": registration["max_candidates"],
        "pre_outcome_seed_required": True,
        "selection_seed_commitment_verified": True,
        "wave_opened": False,
    })
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--population", type=pathlib.Path, required=True)
    parser.add_argument("--gate-decision", type=pathlib.Path, required=True)
    parser.add_argument("--schedule", type=pathlib.Path, required=True)
    parser.add_argument("--bucket-registry", type=pathlib.Path, required=True)
    parser.add_argument("--checkout", type=pathlib.Path, required=True)
    parser.add_argument("--inventory-file", type=pathlib.Path, required=True)
    parser.add_argument("--classification-file", type=pathlib.Path, required=True)
    parser.add_argument("--conversion-ledger", type=pathlib.Path, required=True)
    parser.add_argument("--question-history-index", type=pathlib.Path, required=True)
    parser.add_argument("--selection-seed", required=True)
    parser.add_argument("--sample-size", type=int, default=MAX_SAMPLE_SIZE)
    parser.add_argument(
        "--events-log", type=pathlib.Path,
        default=ROOT / "properties" / "generated" / "corpus_events.jsonl",
    )
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args(argv)
    try:
        result = build_allocation(args)
        atomic_write_text(
            args.output,
            json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        )
    except (OSError, ValueError, AllocationError, AllocationInputError, SystemExit) as exc:
        message = str(exc)
        if message:
            print(f"allocate-conversion-candidates: {message}", file=sys.stderr)
        return 2
    print(
        f"allocation -> {args.output}: "
        f"{result['sample_size_selected']} sites; actual={result['actual_selection_counts']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
