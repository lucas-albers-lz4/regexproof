"""Frozen index of previously asked or reserved conversion sites."""

from __future__ import annotations

import hashlib
import json
import pathlib
import re
from collections import defaultdict
from typing import Any

SCHEMA_VERSION = "1"
SOURCE_PATTERNS = (
    ("conversion_ndjson", "properties/generated/*_conversion.ndjson"),
    ("autonomous_measurements", "properties/generated/autonomous_work.jsonl"),
    ("conversion_ndjson", "properties/calibration/**/conversion.ndjson"),
    ("runner_state", "properties/calibration/**/state.json"),
    ("attempt_checkpoint", "properties/calibration/**/checkpoint.json"),
    ("attempts", "properties/calibration/**/attempts.json"),
    ("frozen_roster", "properties/calibration/**/roster*.json"),
    ("p2_source_review", "properties/calibration/*-p2-*-source-review/evidence*.json"),
    ("queue", "properties/conversion_queue/*.json"),
    ("review_evidence", "properties/calibration/**/review-evidence*.json"),
    ("review_decisions", "properties/calibration/**/review*.ndjson"),
    ("contract_artifact", "properties/calibration/**/contract*.json"),
    ("shortlist", "properties/calibration/**/shortlist.json"),
    ("queue_transition_replay", "properties/calibration/**/queue-transition-replay.json"),
    ("upstream_dispositions", "docs/conversion-upstream.jsonl"),
)
PIN_RE = re.compile(r"^[0-9a-f]{40}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
QUALIFIED_SITE_RE = re.compile(r"^([^/]+)/([^/:]+)@([0-9a-f]{40}):(.+)$")


class QuestionHistoryError(ValueError):
    """History artifacts are incomplete, malformed, or stale."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise QuestionHistoryError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def _json_bytes(raw: bytes, label: str) -> Any:
    try:
        return json.loads(raw, object_pairs_hook=_unique_object)
    except (UnicodeDecodeError, json.JSONDecodeError, QuestionHistoryError) as exc:
        raise QuestionHistoryError(f"{label}: invalid JSON: {exc}") from exc


def _url_repo_id(url: str | None) -> str | None:
    if not url:
        return None
    prefix = "https://github.com/"
    if not url.startswith(prefix):
        return None
    return url.removeprefix(prefix).rstrip("/")


def _normalize_identity(
    *,
    site: Any,
    cluster: Any = None,
    repository_url: Any = None,
    source_pin: Any = None,
    repo_id: Any = None,
) -> dict[str, Any] | None:
    if not isinstance(site, str) or not site.strip():
        return None
    url = repository_url if isinstance(repository_url, str) and repository_url else None
    pin = source_pin if isinstance(source_pin, str) and source_pin else None
    repo = repo_id if isinstance(repo_id, str) and repo_id else _url_repo_id(url)
    match = QUALIFIED_SITE_RE.fullmatch(site)
    if match:
        qualified_repo = f"{match.group(1)}/{match.group(2)}"
        qualified_pin = match.group(3)
        if repo and repo.lower() != qualified_repo.lower():
            raise QuestionHistoryError(
                f"qualified site repo {qualified_repo!r} conflicts with {repo!r}"
            )
        if pin and pin != qualified_pin:
            raise QuestionHistoryError(
                f"qualified site pin {qualified_pin!r} conflicts with {pin!r}"
            )
        if url and _url_repo_id(url) and _url_repo_id(url).lower() != qualified_repo.lower():
            raise QuestionHistoryError(
                f"qualified site URL {url!r} conflicts with {qualified_repo!r}"
            )
        repo = qualified_repo
        pin = qualified_pin
        url = url or f"https://github.com/{qualified_repo}"
        site = match.group(4)
    if pin is not None and not PIN_RE.fullmatch(pin):
        raise QuestionHistoryError(f"invalid source pin in history record: {pin!r}")
    # Corpus labels vary across source artifacts (for example, a runner may
    # use `owner/repo` while its conversion row uses `repo`). For a
    # repository-backed identity, aggregate by the canonical GitHub repo name;
    # exact repository URL, pin, and site remain the identity fields. Keep the
    # supplied cluster only when no GitHub repository can be derived.
    canonical_repo = _url_repo_id(url)
    if canonical_repo:
        cluster = canonical_repo.lower()
    elif not isinstance(cluster, str) or not cluster:
        cluster = repo
    return {
        "cluster": cluster,
        "repository_url": url.rstrip("/") if url else None,
        "repo_id": repo,
        "source_pin": pin,
        "site": site,
    }


def _record_identity(
    row: dict[str, Any], *, cluster: str | None = None, site: Any = None
) -> dict[str, Any] | None:
    contract = row.get("contract")
    adoption: dict[str, Any] = {}
    if isinstance(contract, dict) and isinstance(contract.get("adoption"), dict):
        adoption = contract["adoption"]
    source_url = row.get("url") or row.get("repository_url") or adoption.get("source_url")
    source_pin = row.get("pin") or row.get("source_pin") or adoption.get("source_pin")
    return _normalize_identity(
        site=site or row.get("site") or (
            contract.get("site") if isinstance(contract, dict) else None
        ),
        cluster=cluster or row.get("corpus") or row.get("cluster"),
        repository_url=source_url,
        source_pin=source_pin,
        repo_id=row.get("repo_id") or row.get("repo"),
    )


def _source_line_key(site: Any) -> tuple[str, str] | None:
    """Normalize path:line:column/token aliases to their source line."""
    if not isinstance(site, str) or not site:
        return None
    match = QUALIFIED_SITE_RE.fullmatch(site)
    if match:
        site = match.group(4)
    path, separator, suffix = site.rpartition(":")
    if not separator:
        return None
    source, separator, line = path.rpartition(":")
    if not separator or not line.isdigit():
        return None
    return source, line


def _discover_sources(root: pathlib.Path) -> list[dict[str, Any]]:
    found: dict[str, tuple[str, pathlib.Path]] = {}
    for kind, pattern in SOURCE_PATTERNS:
        for path in root.glob(pattern):
            relative = path.relative_to(root).as_posix()
            prior = found.get(relative)
            if prior and prior[0] != kind:
                raise QuestionHistoryError(f"history source matched multiple families: {relative}")
            found[relative] = (kind, path)
    sources: list[dict[str, Any]] = []
    for relative, (kind, path) in sorted(found.items()):
        # P6 runners retain `roster-input.json` as the pre-freeze array passed
        # to the roster builder. The canonical frozen artifact is `roster.json`;
        # the input is neither a roster checkpoint nor independently useful
        # duplicate-prevention history.
        if kind == "frozen_roster" and path.name == "roster-input.json":
            continue
        if path.is_symlink() or not path.is_file():
            raise QuestionHistoryError(f"history source is missing or a symlink: {relative}")
        try:
            raw = path.read_bytes()
        except OSError as exc:
            raise QuestionHistoryError(f"cannot read history source {relative}: {exc}") from exc
        sources.append({
            "path": relative,
            "kind": kind,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "records": 0,
        })
    return sources


def _iter_json_records(path: pathlib.Path, kind: str) -> list[dict[str, Any]]:
    raw = path.read_bytes()
    if kind.endswith("ndjson") or kind in {
        "review_decisions", "upstream_dispositions", "autonomous_measurements"
    }:
        records = []
        for line_number, line in enumerate(raw.splitlines(), start=1):
            if not line.strip():
                continue
            value = _json_bytes(line, f"{path}:{line_number}")
            if not isinstance(value, dict):
                raise QuestionHistoryError(f"{path}:{line_number}: record must be an object")
            records.append(value)
        if kind == "autonomous_measurements":
            expanded: list[dict[str, Any]] = []
            for record_number, row in enumerate(records):
                if row.get("schema_version") != "3":
                    expanded.append(row)
                    continue
                items = row.get("work_items")
                if not isinstance(items, list):
                    raise QuestionHistoryError(
                        f"{path}: schema 3 measurement {record_number} has no work_items array"
                    )
                reviewed_count = 0
                question_count = 0
                seen_questions: set[tuple[str, str]] = set()
                for item_number, item in enumerate(items):
                    if (
                        not isinstance(item, dict)
                        or set(item) != {"site", "reviewed", "question_ids"}
                        or not isinstance(item["site"], str)
                        or not item["site"]
                        or type(item["reviewed"]) is not bool
                        or not isinstance(item["question_ids"], list)
                    ):
                        raise QuestionHistoryError(
                            f"{path}: measurement work item {record_number}:{item_number} is invalid"
                        )
                    reviewed_count += int(item["reviewed"])
                    question_ids = item["question_ids"]
                    if any(not isinstance(qid, str) or not qid for qid in question_ids):
                        raise QuestionHistoryError(
                            f"{path}: measurement question identity is invalid"
                        )
                    for question_id in question_ids:
                        identity = (item["site"], question_id)
                        if identity in seen_questions:
                            raise QuestionHistoryError(
                                f"{path}: duplicate site/question identity in measurement"
                            )
                        seen_questions.add(identity)
                    question_count += len(question_ids)
                    if item["reviewed"]:
                        expanded.append(dict(
                            row,
                            site=item["site"],
                            status="reviewed",
                            question_id=None,
                        ))
                    for question_id in question_ids:
                        expanded.append(dict(
                            row,
                            site=item["site"],
                            status="attempted",
                            question_id=question_id,
                        ))
                if reviewed_count != row.get("reviewed_sites"):
                    raise QuestionHistoryError(
                        f"{path}: schema 3 reviewed site identities do not match count"
                    )
                if question_count != row.get("proof_questions_attempted"):
                    raise QuestionHistoryError(
                        f"{path}: schema 3 question identities do not match attempt count"
                    )
            return expanded
        return records
    value = _json_bytes(raw, str(path))
    if kind == "attempts":
        if not isinstance(value, list) or any(not isinstance(row, dict) for row in value):
            raise QuestionHistoryError(f"{path}: attempts artifact must be an object array")
        return value
    if kind == "contract_artifact":
        if isinstance(value, list):
            rows = value
        elif isinstance(value, dict):
            rows = value.get("contracts", [value])
        else:
            raise QuestionHistoryError(f"{path}: contract artifact must be an object or array")
        if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
            raise QuestionHistoryError(f"{path}: contract artifact must contain object records")
        return rows
    if not isinstance(value, dict) and not (
        kind == "frozen_roster" and isinstance(value, list)
    ):
        raise QuestionHistoryError(f"{path}: history artifact must be an object")
    if kind in {"runner_state", "attempt_checkpoint"}:
        rows = value.get("attempts")
        if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
            raise QuestionHistoryError(f"{path}: attempts must be an object array")
        return rows
    if kind == "frozen_roster":
        # Some calibration bundles preserve the pre-freeze contract rows as a
        # JSON array named roster-contracts.json. Treat those rows as the
        # roster identities they are; the canonical roster.json remains an
        # object containing an `identities` array.
        if isinstance(value, list):
            if any(not isinstance(row, dict) for row in value):
                raise QuestionHistoryError(
                    f"{path}: roster contract rows must be objects"
                )
            return value
        rows = value.get("identities")
        if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
            raise QuestionHistoryError(f"{path}: identities must be an object array")
        return rows
    if kind == "queue":
        rows = value.get("candidate_sites")
        if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
            raise QuestionHistoryError(f"{path}: candidate_sites must be an object array")
        return [dict(row, cluster=value.get("cluster")) for row in rows]
    if kind == "review_evidence":
        rows = value.get("candidates")
        if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
            raise QuestionHistoryError(f"{path}: candidates must be an object array")
        return [dict(row, cluster=value.get("cluster"),
                     repository_url=value.get("repository_url"),
                     source_pin=value.get("source_pin")) for row in rows]
    if kind == "p2_source_review":
        repository = value.get("repository")
        rows = value.get("sites")
        if (
            value.get("artifact_kind") != "p2-exact-pin-source-review"
            or value.get("schema_version") != "1"
            or not isinstance(repository, dict)
            or not isinstance(repository.get("repo_id"), str)
            or not isinstance(repository.get("url"), str)
            or not isinstance(repository.get("pin"), str)
            or not isinstance(rows, list)
            or any(not isinstance(row, dict) for row in rows)
        ):
            raise QuestionHistoryError(f"{path}: invalid P2 source-review evidence")
        enriched = []
        for row in rows:
            if (
                not isinstance(row.get("site"), str)
                or not isinstance(row.get("regex_id"), str)
                or row.get("decision") not in {"adopted", "skip", "unresolved"}
            ):
                raise QuestionHistoryError(f"{path}: invalid P2 reviewed site")
            enriched.append(dict(
                row,
                cluster=repository["repo_id"],
                repo_id=repository["repo_id"],
                repository_url=repository["url"],
                source_pin=repository["pin"],
                status=row["decision"],
            ))
        return enriched
    if kind == "shortlist":
        rows = value.get("keep") or value.get("sites")
        if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
            raise QuestionHistoryError(f"{path}: shortlist must contain keep or sites object rows")
        enriched = []
        for row in rows:
            candidate = dict(row)
            if not candidate.get("site"):
                source_file = value.get("source_file")
                line = candidate.get("line")
                name = candidate.get("name")
                if isinstance(source_file, str) and isinstance(line, int) and isinstance(name, str):
                    candidate["site"] = f"{source_file}:{line}:{name}"
            candidate["cluster"] = value.get("cluster") or value.get("corpus")
            candidate["repository_url"] = value.get("repository_url")
            candidate["source_pin"] = value.get("source_pin")
            candidate["status"] = candidate.get("disposition") or "shortlisted"
            enriched.append(candidate)
        return enriched
    if kind == "queue_transition_replay":
        rows = value.get("transitions")
        if rows is not None:
            if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
                raise QuestionHistoryError(f"{path}: transitions must be an object array")
            enriched = []
            for row in rows:
                stdout = row.get("stdout")
                if not isinstance(stdout, str):
                    continue
                try:
                    candidate = json.loads(stdout, object_pairs_hook=_unique_object)
                except (json.JSONDecodeError, QuestionHistoryError) as exc:
                    raise QuestionHistoryError(f"{path}: malformed transition stdout: {exc}") from exc
                if isinstance(candidate, dict):
                    enriched.append(dict(candidate,
                                         cluster=value.get("cluster") or value.get("corpus"),
                                         repository_url=value.get("repository_url"),
                                         source_pin=value.get("source_pin")))
            return enriched

        # Early P4 close-outs stored a compact lifecycle summary rather than
        # raw transition command records. Preserve their explicit site
        # reservations, but do not infer that any product question was asked
        # from the phase-name strings.
        phase_summary = value.get("second_wave_transitions")
        contracted_sites = value.get("contracted_sites")
        if (
            isinstance(phase_summary, list)
            and phase_summary
            and all(isinstance(phase, str) and phase for phase in phase_summary)
            and isinstance(contracted_sites, list)
            and all(
                isinstance(row, dict)
                and isinstance(row.get("site"), str)
                and row.get("status") == "contracted"
                for row in contracted_sites
            )
        ):
            return [
                dict(
                    row,
                    cluster=value.get("cluster") or value.get("corpus"),
                    repository_url=value.get("repository_url"),
                    source_pin=value.get("source_pin"),
                )
                for row in contracted_sites
            ]
        raise QuestionHistoryError(
            f"{path}: expected transitions object array or a contracted-site lifecycle summary"
        )
    raise QuestionHistoryError(f"unsupported history source kind: {kind}")


def build_question_history_index(root: pathlib.Path) -> dict[str, Any]:
    """Scan known in-repository proof, review, roster, and queue artifacts."""
    root = pathlib.Path(root).resolve()
    sources = _discover_sources(root)
    rows_by_key: dict[tuple[Any, ...], dict[str, Any]] = {}
    unbound: list[dict[str, Any]] = []
    counts: dict[str, int] = defaultdict(int)

    for source in sources:
        source_path = root / source["path"]
        rows = _iter_json_records(source_path, source["kind"])
        source["records"] = len(rows)
        for index, row in enumerate(rows):
            counts[source["kind"]] += 1
            contract = row.get("contract")
            contract_site = (
                contract.get("site") if isinstance(contract, dict) else None
            )
            site_values = [
                row.get("site"), contract_site, row.get("previous_site"),
                row.get("revised_site"), row.get("inventory_site"),
            ]
            site_values = list(dict.fromkeys(
                site for site in site_values if isinstance(site, str) and site
            ))
            identities = [
                identity for identity in (
                    _record_identity(row, site=site) for site in site_values if site
                ) if identity is not None
            ]
            if not identities:
                states = {
                    str(row.get(field) or "").strip().lower()
                    for field in ("status", "result", "decision")
                }
                measurement_attempts = row.get("proof_questions_attempted", 0)
                measurement_reviews = row.get("reviewed_sites", 0)
                is_unbound_measurement = (
                    source["kind"] == "autonomous_measurements"
                    and (
                        (isinstance(measurement_attempts, int) and measurement_attempts > 0)
                        or (isinstance(measurement_reviews, int) and measurement_reviews > 0)
                    )
                )
                if (
                    row.get("question_id") or row.get("name")
                    or is_unbound_measurement
                    or states & {
                        "claimed", "contracted", "emitted", "unsat", "sat", "timeout",
                        "unknown", "error", "encoding_failed", "unreachable",
                        "behavioral_only", "adopted", "unresolved", "deferred",
                    }
                ):
                    unbound.append({
                        "cluster": row.get("cluster") or row.get("corpus"),
                        "repository_url": row.get("url") or row.get("repository_url"),
                        "source_pin": row.get("pin") or row.get("source_pin"),
                        "question_id": row.get("question_id") or row.get("name") or (
                            f"aggregate:{row.get('run_id')}"
                            if is_unbound_measurement and row.get("run_id") else None
                        ),
                        "source": source["path"],
                        "record": index,
                        "status": row.get("status") or row.get("result"),
                        "reason": "history record has no usable site identity",
                    })
                continue

            kind = source["kind"]
            status = str(row.get("status") or row.get("result") or "")
            question_id = row.get("question_id") or row.get("name")
            asked = kind in {
                "conversion_ndjson", "runner_state", "attempt_checkpoint",
                "attempts", "upstream_dispositions",
            } and status not in {"", "planned", "not_attempted"}
            reserved = kind in {
                "frozen_roster", "queue", "review_evidence", "review_decisions",
                "queue_transition_replay", "contract_artifact", "shortlist",
                "p2_source_review",
            }
            if kind == "autonomous_measurements":
                asked = status == "attempted"
                reserved = status == "reviewed"
            if kind in {"runner_state", "attempt_checkpoint", "attempts"}:
                reserved = status != "not_attempted"
                asked = status not in {"", "not_attempted"}
            regex_id = row.get("regex_id")
            if not asked and not reserved:
                continue
            for identity in identities:
                key = (
                    identity["cluster"], identity["repository_url"], identity["source_pin"],
                    identity["site"],
                )
                entry = rows_by_key.setdefault(key, {
                    **identity,
                    "regex_ids": [],
                    "patterns": [],
                    "question_ids": [],
                    "asked": False,
                    "reserved": False,
                    "statuses": [],
                    "evidence": [],
                })
                if isinstance(regex_id, str) and regex_id and regex_id not in entry["regex_ids"]:
                    entry["regex_ids"].append(regex_id)
                pattern = row.get("pattern")
                if isinstance(pattern, str):
                    signature = {
                        "pattern": pattern,
                        "flags": str(row.get("flags") or ""),
                        "call_kind": str(row.get("call_kind") or ""),
                    }
                    if signature not in entry["patterns"]:
                        entry["patterns"].append(signature)
                if isinstance(question_id, str) and question_id and question_id not in entry["question_ids"]:
                    entry["question_ids"].append(question_id)
                entry["asked"] = entry["asked"] or asked
                entry["reserved"] = entry["reserved"] or reserved
                if status and status not in entry["statuses"]:
                    entry["statuses"].append(status)
                entry["evidence"].append({
                    "source": source["path"],
                    "record": index,
                    "kind": kind,
                    "status": status or None,
                    "question_id": question_id if isinstance(question_id, str) else None,
                })

    entries = sorted(
        rows_by_key.values(),
        key=lambda row: (
            str(row["cluster"] or ""), str(row["repository_url"] or ""),
            str(row["source_pin"] or ""), row["site"],
        ),
    )
    for row in entries:
        row["regex_ids"].sort()
        row["patterns"].sort(
            key=lambda signature: (
                signature["pattern"], signature["flags"], signature["call_kind"]
            )
        )
        row["question_ids"].sort()
        row["statuses"].sort()
        row["evidence"].sort(key=lambda item: (item["source"], item["record"], item["kind"]))
    unbound.sort(key=lambda row: (str(row.get("cluster") or ""), row["source"], row["record"]))
    return {
        "schema_version": SCHEMA_VERSION,
        "source_patterns": [
            {"kind": kind, "glob": pattern} for kind, pattern in SOURCE_PATTERNS
        ],
        "sources": sources,
        "entries": entries,
        "unbound_records": unbound,
        "audit": {
            "source_count": len(sources),
            "record_counts_by_kind": dict(sorted(counts.items())),
            "entry_count": len(entries),
            "asked_site_count": sum(bool(row["asked"]) for row in entries),
            "reserved_site_count": sum(bool(row["reserved"]) for row in entries),
            "unbound_record_count": len(unbound),
            "scope": "recognized in-repository conversion, run measurement, contract, shortlist, runner, exact-pin P2 source review, review, roster, queue, and disposition artifacts",
        },
    }


def validate_question_history_index(value: Any) -> dict[str, Any]:
    required = {
        "schema_version", "source_patterns", "sources", "entries", "unbound_records", "audit"
    }
    if not isinstance(value, dict) or set(value) != required:
        raise QuestionHistoryError("history index has invalid root fields")
    if value["schema_version"] != SCHEMA_VERSION:
        raise QuestionHistoryError("unsupported question-history index version")
    if not isinstance(value["sources"], list) or not isinstance(value["entries"], list):
        raise QuestionHistoryError("history index sources and entries must be arrays")
    for source in value["sources"]:
        if (
            not isinstance(source, dict)
            or set(source) != {"path", "kind", "sha256", "records"}
            or not isinstance(source["path"], str)
            or not isinstance(source["kind"], str)
            or not isinstance(source["records"], int)
            or not SHA_RE.fullmatch(str(source["sha256"]))
        ):
            raise QuestionHistoryError("history index contains an invalid source record")
    for entry in value["entries"]:
        if (
            not isinstance(entry, dict)
            or not isinstance(entry.get("site"), str)
            or not isinstance(entry.get("asked"), bool)
            or not isinstance(entry.get("reserved"), bool)
            or not isinstance(entry.get("question_ids"), list)
        ):
            raise QuestionHistoryError("history index contains an invalid site entry")
        patterns = entry.get("patterns")
        if patterns is not None and (
            not isinstance(patterns, list)
            or any(
                not isinstance(row, dict)
                or set(row) != {"pattern", "flags", "call_kind"}
                or not all(isinstance(row.get(key), str) for key in ("pattern", "flags", "call_kind"))
                for row in patterns
            )
        ):
            raise QuestionHistoryError("history index contains invalid pattern signatures")
    if not isinstance(value["unbound_records"], list) or not isinstance(value["audit"], dict):
        raise QuestionHistoryError("history index audit or unbound records are invalid")
    return value


def verify_index_current(root: pathlib.Path, index: Any) -> dict[str, Any]:
    """Rebuild the index and reject stale source set, digests, or extracted rows."""
    frozen = validate_question_history_index(index)
    current = build_question_history_index(root)
    if frozen != current:
        raise QuestionHistoryError("question-history index is stale for current repo artifacts")
    return current


def check_candidates_new(population: dict[str, Any], index: dict[str, Any]) -> int:
    """Reject candidates present in asked, reserved, or unresolved local history."""
    cluster = population["cluster"]
    population_url = population["repository_url"].rstrip("/")
    pin = population["source_pin"]
    history = validate_question_history_index(index)
    for candidate in population["candidates"]:
        candidate_sites = {candidate["site"]}
        if isinstance(candidate.get("inventory_site"), str):
            candidate_sites.add(candidate["inventory_site"])
        candidate_regex_id = candidate.get("regex_id")
        candidate_line = next((
            _source_line_key(site) for site in candidate_sites
            if _source_line_key(site) is not None
        ), None)
        candidate_signature = {
            "pattern": candidate.get("pattern"),
            "flags": candidate.get("flags", ""),
            "call_kind": candidate.get("call_kind", ""),
        }
        repo_url = population_url
        for entry in history["entries"]:
            entry_site = entry["site"]
            same_site = entry_site in candidate_sites
            same_regex = (
                isinstance(candidate_regex_id, str)
                and candidate_regex_id in entry.get("regex_ids", [])
            )
            same_line = (
                candidate_line is not None
                and candidate_line == _source_line_key(entry_site)
            )
            prior_patterns = entry.get("patterns")
            same_line_pattern = same_line and (
                not isinstance(prior_patterns, list)
                or not prior_patterns
                or candidate_signature in prior_patterns
            )
            same_repo = (
                entry.get("repository_url") in {None, repo_url}
                and entry.get("cluster") in {None, cluster}
            )
            same_pin = entry.get("source_pin") in {None, pin}
            same_identity = (
                entry.get("repository_url") == repo_url
                and entry.get("source_pin") == pin
            )
            if (same_site or same_regex or same_line_pattern) and (
                (same_repo and same_pin) or same_identity
            ):
                state = "asked" if entry["asked"] else "reserved"
                refs = ", ".join(item["source"] for item in entry["evidence"][:3])
                raise QuestionHistoryError(
                    f"candidate site {candidate['site']!r} is already {state} in history ({refs})"
                )
        for row in history["unbound_records"]:
            row_cluster = row.get("cluster")
            row_url = row.get("repository_url")
            row_pin = row.get("source_pin")
            if row_cluster == cluster or row_url == repo_url:
                if row_pin in {None, pin}:
                    raise QuestionHistoryError(
                        f"candidate site {candidate['site']!r} has unresolved prior history in {row['source']}"
                    )
    return len(population["candidates"])
