#!/usr/bin/env python3
"""Aggregate exact-pin product checkpoints against the frozen P2 source inventory.

This builds a retrospective evidence checkpoint. It does not select a sample,
establish eligibility for unreviewed source sites, or estimate prospective yield.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.mine.cohort_manifest import (  # noqa: E402
    CohortManifestError,
    validate_manifest,
)
from regexproof.mine.conversion_checkpoint import (  # noqa: E402
    ConversionCheckpointError,
    build_product_roster,
    build_report,
    canonical_row_to_checkpoint,
    checkpoint_from_attempts,
    load_checkpoint,
)


class EvidenceError(ValueError):
    """Raised when an input cannot be joined to the frozen evidence set."""


_AGGREGATE_SCOPE = (
    "retrospective exact-pin attempts matched to the P2 declared-dialect "
    "source inventory"
)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def _write_json(path: Path, value: Any) -> None:
    atomic_write_text(
        path,
        json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
    )
    path.chmod(0o644)


def _identity(row: dict[str, Any]) -> tuple[str, str, str, str, str]:
    return tuple(
        str(row.get(field) or "")
        for field in ("repo_id", "url", "pin", "site", "question_id")
    )


def _source_anchor(
    site: str, *, repo_id: str, pin: str
) -> tuple[str, int, int | None]:
    prefix = f"{repo_id}@{pin}:"
    if not site.startswith(prefix):
        raise EvidenceError(f"contract site is not bound to its cohort pin: {site!r}")
    anchor = site[len(prefix) :]
    parts = anchor.rsplit(":", 2)
    if len(parts) != 3 or not parts[1].isdigit():
        raise EvidenceError(f"contract site has no stable file:line anchor: {site!r}")
    selector = parts[2]
    column: int | None = None
    if selector.startswith("column-"):
        value = selector.removeprefix("column-")
        if not value.isdigit():
            raise EvidenceError(f"contract site has an invalid source column selector: {site!r}")
        column = int(value)
    return parts[0], int(parts[1]), column


def _read_sites(path: Path) -> tuple[list[dict[str, Any]], str]:
    raw = path.read_bytes()
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(raw.splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise EvidenceError(
                f"{path}:{line_number}: invalid NDJSON: {exc.msg}"
            ) from exc
        if not isinstance(row, dict):
            raise EvidenceError(f"{path}:{line_number}: source row must be an object")
        rows.append(row)
    return rows, _sha256(raw)


def _inventory_index(
    sites: list[dict[str, Any]], cohort: dict[str, Any]
) -> dict[tuple[str, str, str, int], list[dict[str, Any]]]:
    repos = {
        (item["repo_id"], item["pin"]): item for item in cohort["repos"]
    }
    index: dict[tuple[str, str, str, int], list[dict[str, Any]]] = {}
    for number, row in enumerate(sites, 1):
        repo_id = row.get("repo_id")
        pin = row.get("pin")
        if (repo_id, pin) not in repos:
            raise EvidenceError(f"source inventory row {number} is outside the cohort")
        repo = repos[(repo_id, pin)]
        if (
            row.get("cohort_id") != cohort["cohort_id"]
            or row.get("manifest_digest") != cohort["manifest_digest"]
            or row.get("dialect_family") != repo["dialect_family"]
        ):
            raise EvidenceError(
                f"source inventory row {number} has mismatched cohort or dialect"
            )
        source_file = row.get("source_file")
        line = row.get("line")
        file_sha = row.get("source_file_sha256")
        if (
            not isinstance(source_file, str)
            or not source_file
            or isinstance(line, bool)
            or not isinstance(line, int)
            or line < 1
            or not isinstance(file_sha, str)
            or len(file_sha) != 64
        ):
            raise EvidenceError(f"source inventory row {number} has invalid source identity")
        key = (repo_id, pin, source_file, line)
        index.setdefault(key, []).append(row)
    return index


def _match_attempt(
    attempt: dict[str, Any],
    inventory: dict[tuple[str, str, str, int], list[dict[str, Any]]],
) -> tuple[dict[str, Any] | None, str | None]:
    source_file, line, column = _source_anchor(
        attempt["site"], repo_id=attempt["repo_id"], pin=attempt["pin"]
    )
    matches = inventory.get((attempt["repo_id"], attempt["pin"], source_file, line), [])
    if column is not None:
        matches = [row for row in matches if row.get("column") == column]
    if not matches:
        return None, "source_site_outside_declared_dialect_inventory"
    if len(matches) != 1:
        return None, "source_line_has_ambiguous_inventory_sites"
    contract = attempt["contract"]
    if contract.get("provenance") == "agent_derived":
        adoption = contract.get("adoption", {})
        if (
            adoption.get("source_file") != source_file
            or adoption.get("source_pin") != attempt["pin"]
            or adoption.get("source_url", "").rstrip("/")
            != attempt["url"].rstrip("/")
            or adoption.get("source_sha256") != matches[0]["source_file_sha256"]
        ):
            raise EvidenceError(
                f"agent adoption evidence does not match P2 source inventory: {attempt['site']}"
            )
    return matches[0], None


def _canonical_core(row: dict[str, Any]) -> tuple[Any, ...]:
    """Compare the product identity/evidence fields across legacy artifacts."""
    result = row.get("result")
    if result == "gap":
        result = "sat"
    ground_truth = row.get("ground_truth_status")
    if ground_truth is None:
        ground_truth = "not_applicable" if result == "unsat" else "not_run"
    return (
        row.get("site"),
        (row.get("question_id") or row.get("name")),
        row.get("kind"),
        row.get("synthesized"),
        result,
        ground_truth,
        row.get("domain"),
        row.get("contract"),
    )


def _canonical_disposition(row: dict[str, Any], result: str, ground_truth: str) -> dict[str, Any]:
    if result == "unsat":
        status = "not_applicable"
    elif ground_truth in {"reproduced", "PASS"}:
        status = "pending_product_triage"
    else:
        status = "pending_ground_truth"
    return {
        "status": status,
        "filed_at": None,
        "resolved_at": None,
        "approval_escape": None,
        "approval_ref": None,
        "reason_code": None,
        "backfilled": False,
        "disposition_date": None,
    }


def _load_inputs(
    checkpoint_root: Path,
    conversion_root: Path | None,
    out_dir: Path,
    cohort: dict[str, Any],
    inventory: dict[tuple[str, str, str, int], list[dict[str, Any]]],
    repo_root: Path,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    selected_attempts: list[dict[str, Any]] = []
    selected_rows: list[dict[str, Any]] = []
    checkpoint_sources: list[dict[str, Any]] = []
    selected_identities: set[tuple[str, str, str, str, str]] = set()
    selected_attempts_by_identity: dict[
        tuple[str, str, str, str, str], dict[str, Any]
    ] = {}
    selected_rows_by_identity: dict[
        tuple[str, str, str, str, str], dict[str, Any]
    ] = {}

    checkpoint_files = sorted(checkpoint_root.rglob("checkpoint.json"))
    for checkpoint_path in checkpoint_files:
        resolved = checkpoint_path.resolve()
        if resolved.is_relative_to(out_dir.resolve()):
            continue
        raw = checkpoint_path.read_bytes()
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise EvidenceError(f"{checkpoint_path}: invalid checkpoint JSON: {exc.msg}") from exc
        if not isinstance(parsed, dict):
            raise EvidenceError(f"{checkpoint_path}: checkpoint root must be an object")
        if parsed.get("cohort_id") != cohort["cohort_id"]:
            continue
        checkpoint_attempts = parsed.get("attempts")
        if not isinstance(checkpoint_attempts, list):
            raise EvidenceError(f"{checkpoint_path}: checkpoint attempts must be a list")
        if parsed.get("manifest_digest") != cohort["manifest_digest"]:
            raise EvidenceError(
                f"{checkpoint_path}: matching cohort ID has a different manifest digest"
            )

        # A previous run of this builder is a derived aggregate, not a source
        # run. Its sibling manifest provides a stable artifact marker without
        # depending on a directory name. Reading it as input would count every
        # source attempt twice on the next refresh.
        source_manifest_path = checkpoint_path.with_name("source-checkpoints.json")
        if source_manifest_path.is_file():
            try:
                source_manifest = json.loads(
                    source_manifest_path.read_bytes()
                )
            except json.JSONDecodeError as exc:
                raise EvidenceError(
                    f"{source_manifest_path}: invalid aggregate source manifest: "
                    f"{exc.msg}"
                ) from exc
            if (
                isinstance(source_manifest, dict)
                and source_manifest.get("scope") == _AGGREGATE_SCOPE
            ):
                inventory_digest = source_manifest.get("source_inventory_file_sha256")
                sites_digest = source_manifest.get("source_sites_file_sha256")
                cohort_file_digest = source_manifest.get("cohort_file_sha256")
                input_set_digest = source_manifest.get("input_set_sha256")
                input_set = dict(source_manifest)
                input_set.pop("input_set_sha256", None)
                artifact_kind = source_manifest.get("artifact_kind")
                hex_digests = (
                    inventory_digest,
                    sites_digest,
                    cohort_file_digest,
                    input_set_digest,
                )
                if (
                    source_manifest.get("schema_version") != "1"
                    or artifact_kind not in {
                        None,
                        "p2-retrospective-evidence-source-manifest",
                    }
                    or source_manifest.get("cohort_id") != cohort["cohort_id"]
                    or source_manifest.get("cohort_manifest_digest")
                    != cohort["manifest_digest"]
                    or source_manifest.get("matched_question_count")
                    != len(checkpoint_attempts)
                    or source_manifest.get("checkpoint_root")
                    != checkpoint_root.resolve().relative_to(repo_root.resolve()).as_posix()
                    or not isinstance(source_manifest.get("checkpoints"), list)
                    or any(
                        not isinstance(digest, str)
                        or len(digest) != 64
                        or any(char not in "0123456789abcdef" for char in digest)
                        for digest in hex_digests
                    )
                    or input_set_digest != _sha256(_canonical_json(input_set))
                ):
                    raise EvidenceError(
                        f"{checkpoint_path}: inconsistent retrospective aggregate marker"
                    )
                try:
                    load_checkpoint(checkpoint_path)
                except ConversionCheckpointError as exc:
                    raise EvidenceError(
                        f"{checkpoint_path}: invalid retrospective aggregate: {exc}"
                    ) from exc
                continue
        try:
            checkpoint = load_checkpoint(checkpoint_path)
        except ConversionCheckpointError as exc:
            raise EvidenceError(f"{checkpoint_path}: {exc}") from exc

        source_rel = checkpoint_path.resolve().relative_to(repo_root.resolve()).as_posix()
        source_entry: dict[str, Any] = {
            "path": source_rel,
            "sha256": _sha256(raw),
            "attempts": len(checkpoint["attempts"]),
            "matched_questions": [],
            "excluded_questions": [],
        }
        rows_by_identity = {
            _identity(row): row for row in checkpoint["rows"]
        }
        for attempt in checkpoint["attempts"]:
            source_row, exclusion = _match_attempt(attempt, inventory)
            question = {
                "repo_id": attempt["repo_id"],
                "pin": attempt["pin"],
                "site": attempt["site"],
                "question_id": attempt["question_id"],
                "status": attempt["status"],
            }
            if exclusion is not None:
                source_entry["excluded_questions"].append(
                    {**question, "reason": exclusion}
                )
                continue

            identity = _identity(attempt)
            if identity in selected_identities:
                raise EvidenceError(
                    "duplicate product question across source checkpoints; preserve each "
                    f"run and resolve the roster explicitly: {identity!r}"
                )
            selected_identities.add(identity)
            selected_attempt = dict(attempt)
            selected_attempts.append(selected_attempt)
            selected_attempts_by_identity[identity] = selected_attempt
            source_entry["matched_questions"].append(
                {
                    **question,
                    "source_inventory_match": {
                        "regex_id": source_row["regex_id"],
                        "source_site_id": source_row["source_site_id"],
                        "dialect_family": source_row["dialect_family"],
                        "source_file": source_row["source_file"],
                        "source_file_sha256": source_row["source_file_sha256"],
                        "git_blob_oid": source_row["git_blob_oid"],
                        "pattern": source_row["pattern"],
                    },
                }
            )
            row = rows_by_identity.get(identity)
            if row is not None:
                selected_row = dict(row)
                selected_rows.append(selected_row)
                selected_rows_by_identity[identity] = selected_row
            elif attempt["status"] in {"sat", "unsat"}:
                raise EvidenceError(
                    f"decided attempt has no proof row in {checkpoint_path}: {identity!r}"
                )
        checkpoint_sources.append(source_entry)

    # Canonical conversion rows predate complete attempt checkpoints. Import
    # only rows whose exact cohort pin and source file/line join the frozen P2
    # inventory. Rows already represented by a checkpoint are corroborating
    # evidence, not a second product question.
    cohort_by_prefix = {
        f"{repo['repo_id']}@{repo['pin']}:": repo for repo in cohort["repos"]
    }
    conversion_paths = (
        sorted(conversion_root.rglob("*_conversion.ndjson"))
        if conversion_root is not None
        else []
    )
    for conversion_path in conversion_paths:
        resolved = conversion_path.resolve()
        if resolved.is_relative_to(out_dir.resolve()):
            continue
        raw = conversion_path.read_bytes()
        relative = resolved.relative_to(repo_root.resolve()).as_posix()
        source_entry = {
            "artifact_kind": "canonical_conversion_ndjson",
            "path": relative,
            "sha256": _sha256(raw),
            "raw_rows": 0,
            "attempts": 0,
            "matched_questions": [],
            "corroborated_questions": [],
            "excluded_questions": [],
        }
        seen_in_file: set[tuple[str, str, str, str, str]] = set()
        for line_number, line in enumerate(raw.splitlines(), 1):
            if not line.strip():
                continue
            source_entry["raw_rows"] += 1
            try:
                canonical = json.loads(line)
            except json.JSONDecodeError as exc:
                raise EvidenceError(
                    f"{conversion_path}:{line_number}: invalid canonical NDJSON: "
                    f"{exc.msg}"
                ) from exc
            if not isinstance(canonical, dict):
                raise EvidenceError(
                    f"{conversion_path}:{line_number}: canonical row must be an object"
                )
            site = canonical.get("site")
            member = next(
                (
                    repo for prefix, repo in cohort_by_prefix.items()
                    if isinstance(site, str) and site.startswith(prefix)
                ),
                None,
            )
            if member is None:
                continue

            source_entry["attempts"] += 1
            question_id = canonical.get("question_id") or canonical.get("name")
            if not isinstance(question_id, str) or not question_id.strip():
                raise EvidenceError(
                    f"{conversion_path}:{line_number}: exact-cohort row has no question ID"
                )
            question_id = question_id.strip()
            attempt_base: dict[str, Any] = {
                "repo_id": member["repo_id"],
                "url": member["url"],
                "pin": member["pin"],
                "site": site,
                "question_id": question_id,
                "kind": canonical.get("kind"),
                "synthesized": canonical.get("synthesized"),
                "contract": canonical.get("contract"),
                "domain": canonical.get("domain"),
            }
            if not isinstance(attempt_base["contract"], dict):
                raise EvidenceError(
                    f"{conversion_path}:{line_number}: exact-cohort row has no contract"
                )
            if canonical.get("product_reportable") is False:
                source_entry["excluded_questions"].append(
                    {
                        "site": site,
                        "question_id": question_id,
                        "status": canonical.get("result"),
                        "reason": "canonical_row_not_product_reportable",
                    }
                )
                continue
            if canonical.get("kind") not in {"property", "counterexample_finder", "bug_demo"}:
                source_entry["excluded_questions"].append(
                    {
                        "site": site,
                        "question_id": question_id,
                        "status": canonical.get("result"),
                        "reason": "canonical_kind_not_product_question",
                    }
                )
                continue
            if canonical.get("synthesized") is not False:
                source_entry["excluded_questions"].append(
                    {
                        "site": site,
                        "question_id": question_id,
                        "status": canonical.get("result"),
                        "reason": "synthesized_rows_are_not_product_questions",
                    }
                )
                continue
            if canonical.get("contract", {}).get("site") != site:
                raise EvidenceError(
                    f"{conversion_path}:{line_number}: canonical contract site differs"
                )

            disposition = _canonical_disposition(
                canonical,
                "sat" if canonical.get("result") == "gap" else canonical.get("result"),
                canonical.get("ground_truth_status")
                or ("not_applicable" if canonical.get("result") == "unsat" else "not_run"),
            )
            try:
                proof_row = canonical_row_to_checkpoint(
                    canonical,
                    repo_id=member["repo_id"],
                    url=member["url"],
                    pin=member["pin"],
                    disposition=disposition,
                )
            except ConversionCheckpointError as exc:
                raise EvidenceError(
                    f"{conversion_path}:{line_number}: incompatible exact-cohort "
                    f"canonical row: {exc}"
                ) from exc

            result = proof_row["result"]
            ground_truth = proof_row["ground_truth_status"]
            replayed = result == "sat" and ground_truth in {"reproduced", "PASS"}
            status = (
                "unsat" if result == "unsat"
                else "sat" if replayed
                else "sat_pending_ground_truth"
            )
            attempt = {
                **attempt_base,
                "status": status,
                "detail": None if status in {"sat", "unsat"} else (
                    "Imported canonical SAT row has no successful persisted product replay."
                ),
                "gate": {
                    "source_pin_verified": False,
                    "product_engine_replayed": replayed,
                    "mutation_guard_passed": False,
                    "differential_cases": 0,
                    "gate_id": None,
                    "local_gate_command": None,
                    "local_gate_passed": False,
                    "consumer_adopted": False,
                },
            }
            source_row, exclusion = _match_attempt(attempt, inventory)
            if exclusion is not None:
                source_entry["excluded_questions"].append(
                    {
                        "site": site,
                        "question_id": question_id,
                        "status": status,
                        "reason": exclusion,
                    }
                )
                continue

            identity = _identity(attempt)
            if identity in seen_in_file:
                raise EvidenceError(
                    f"{conversion_path}: duplicate exact-cohort product row {identity!r}"
                )
            seen_in_file.add(identity)
            if identity in selected_identities:
                existing_attempt = selected_attempts_by_identity[identity]
                existing_row = selected_rows_by_identity.get(identity)
                if (
                    existing_row is None
                    or _canonical_core(existing_row) != _canonical_core(proof_row)
                    or existing_attempt["status"] not in {status, "sat_pending_ground_truth"}
                ):
                    raise EvidenceError(
                        "canonical conversion row conflicts with an existing product "
                        f"question checkpoint: {identity!r}"
                    )
                if replayed:
                    existing_attempt["gate"]["product_engine_replayed"] = True
                source_entry["corroborated_questions"].append(
                    {
                        "site": site,
                        "question_id": question_id,
                        "status": status,
                    }
                )
                continue

            selected_identities.add(identity)
            selected_attempts.append(attempt)
            selected_attempts_by_identity[identity] = attempt
            selected_rows.append(proof_row)
            selected_rows_by_identity[identity] = proof_row
            source_entry["matched_questions"].append(
                {
                    "site": site,
                    "question_id": question_id,
                    "status": status,
                    "source_inventory_match": {
                        "regex_id": source_row["regex_id"],
                        "source_site_id": source_row["source_site_id"],
                        "dialect_family": source_row["dialect_family"],
                        "source_file": source_row["source_file"],
                        "source_file_sha256": source_row["source_file_sha256"],
                        "git_blob_oid": source_row["git_blob_oid"],
                        "pattern": source_row["pattern"],
                    },
                }
            )
        if source_entry["attempts"] or source_entry["excluded_questions"]:
            checkpoint_sources.append(source_entry)

    if not selected_attempts:
        raise EvidenceError("no exact-pin attempts matched the declared-dialect inventory")
    selected_attempts.sort(key=_identity)
    selected_rows.sort(key=_identity)
    checkpoint_sources.sort(key=lambda row: row["path"])
    return selected_attempts, selected_rows, checkpoint_sources


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cohort", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--sites", type=Path, required=True)
    parser.add_argument("--checkpoint-root", type=Path, required=True)
    parser.add_argument(
        "--conversion-root",
        type=Path,
        help="also import compatible canonical *_conversion.ndjson rows",
    )
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        cohort_bytes = args.cohort.read_bytes()
        cohort_doc = json.loads(cohort_bytes)
        cohort = validate_manifest(cohort_doc)
        inventory_doc = json.loads(args.inventory.read_text(encoding="utf-8"))
        if (
            inventory_doc.get("cohort_id") != cohort["cohort_id"]
            or inventory_doc.get("manifest_digest") != cohort["manifest_digest"]
            or inventory_doc.get("cohort_manifest_sha256") != _sha256(cohort_bytes)
        ):
            raise EvidenceError("P2 source inventory is not bound to the supplied cohort bytes")

        sites, sites_sha = _read_sites(args.sites)
        if (
            inventory_doc.get("summary", {}).get("source_sites") != len(sites)
            or inventory_doc.get("summary", {}).get("source_sites_ndjson_sha256") != sites_sha
        ):
            raise EvidenceError("P2 source rows do not match the inventory summary digest/count")
        source_index = _inventory_index(sites, cohort)
        attempts, rows, checkpoint_sources = _load_inputs(
            args.checkpoint_root,
            args.conversion_root,
            args.out_dir,
            cohort,
            source_index,
            args.repo_root,
        )

        roster_inputs = [
            {
                "repo_id": item["repo_id"],
                "url": item["url"],
                "pin": item["pin"],
                "site": item["site"],
                "question_id": item["question_id"],
                "kind": item["kind"],
                "synthesized": item["synthesized"],
                "domain": item["domain"],
                "contract": item["contract"],
            }
            for item in attempts
        ]
        roster = build_product_roster(roster_inputs, cohort)
        checkpoint = checkpoint_from_attempts(
            attempts,
            rows,
            cohort=cohort,
            product_coverage_manifest=roster,
        )
        report = build_report(checkpoint)

        excluded = [
            {"source_checkpoint": item["path"], **question}
            for item in checkpoint_sources
            for question in item["excluded_questions"]
        ]
        source_manifest = {
            "schema_version": "1",
            "artifact_kind": "p2-retrospective-evidence-source-manifest",
            "scope": _AGGREGATE_SCOPE,
            "cohort_id": cohort["cohort_id"],
            "cohort_manifest_digest": cohort["manifest_digest"],
            "cohort_file_sha256": _sha256(cohort_bytes),
            "source_inventory_file_sha256": _sha256(args.inventory.read_bytes()),
            "source_sites_file_sha256": sites_sha,
            "source_site_count": len(sites),
            "checkpoint_root": args.checkpoint_root.resolve().relative_to(args.repo_root.resolve()).as_posix(),
            "checkpoints": checkpoint_sources,
            "matched_question_count": len(attempts),
            "excluded_attempt_count": len(excluded),
            "excluded_attempts": excluded,
        }
        if args.conversion_root is not None:
            source_manifest["conversion_root"] = (
                args.conversion_root.resolve()
                .relative_to(args.repo_root.resolve())
                .as_posix()
            )
        source_manifest["input_set_sha256"] = _sha256(_canonical_json(source_manifest))

        out_dir = args.out_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        _write_json(out_dir / "roster.json", roster)
        _write_json(out_dir / "attempts.json", attempts)
        _write_json(out_dir / "source-checkpoints.json", source_manifest)
        _write_json(out_dir / "checkpoint.json", checkpoint)
        _write_json(out_dir / "report.json", report)
        atomic_write_text(
            out_dir / "conversion.ndjson",
            "".join(
                json.dumps(row["canonical"], ensure_ascii=True, sort_keys=True) + "\n"
                for row in rows
            ),
        )
        (out_dir / "conversion.ndjson").chmod(0o644)
    except (
        OSError,
        json.JSONDecodeError,
        ValueError,
        CohortManifestError,
        ConversionCheckpointError,
        EvidenceError,
    ) as exc:
        print(f"build-p2-evidence-checkpoint: error: {exc}", file=sys.stderr)
        return 2

    statuses = Counter(item["status"] for item in attempts)
    print(
        f"retrospective P2 checkpoint: {len(attempts)} unique source-matched "
        f"questions; statuses={dict(sorted(statuses.items()))}; "
        f"excluded={len(excluded)}; report={out_dir / 'report.json'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
