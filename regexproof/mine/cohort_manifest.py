"""Build a deterministic frozen cohort manifest from offline candidates."""

from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path
from typing import Any, Mapping

SCHEMA_VERSION = "1"
PIN_RE = re.compile(r"^[0-9a-fA-F]{40}$")
CANDIDATE_FIELDS = {
    "repo_id",
    "url",
    "pin",
    "dialect_family",
    "boundary_family",
    "score",
    "sites",
    "fork",
    "duplicate_of",
    "partial",
}
OUTPUT_FIELDS = (
    "repo_id",
    "url",
    "pin",
    "dialect_family",
    "boundary_family",
    "score",
    "sites",
)


class CohortManifestError(ValueError):
    """Raised when candidates or cohort options are invalid."""


def _error(message: str) -> CohortManifestError:
    return CohortManifestError(f"invalid cohort candidates: {message}")


def _object(value: Any, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise _error(f"{context} must be an object")
    return value


def _text(value: Any, field: str, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise _error(f"{context}.{field} must be a non-empty string")
    return value


def _required(row: Mapping[str, Any], field: str, context: str) -> Any:
    if field not in row:
        raise _error(f"{context} is missing required field {field!r}")
    return row[field]


def _validate_candidate(value: Any, index: int) -> dict[str, Any]:
    context = f"candidates[{index}]"
    row = _object(value, context)
    missing = sorted(CANDIDATE_FIELDS - row.keys())
    if missing:
        raise _error(f"{context} is missing required field(s): {', '.join(missing)}")
    extra = sorted(set(row) - CANDIDATE_FIELDS)
    if extra:
        raise _error(f"{context} has unknown field(s): {', '.join(extra)}")

    repo_id = _text(row["repo_id"], "repo_id", context)
    url = _text(row["url"], "url", context)
    pin = _text(row["pin"], "pin", context)
    if PIN_RE.fullmatch(pin) is None:
        raise _error(f"{context}.pin must be exactly 40 hexadecimal characters")
    dialect = _text(row["dialect_family"], "dialect_family", context)
    boundary = _text(row["boundary_family"], "boundary_family", context)

    score = row["score"]
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise _error(f"{context}.score must be a finite number")
    if not math.isfinite(score):
        raise _error(f"{context}.score must be a finite number")

    sites = row["sites"]
    if isinstance(sites, bool) or not isinstance(sites, int) or sites <= 0:
        raise _error(f"{context}.sites must be a positive integer")

    fork = row["fork"]
    if not isinstance(fork, bool):
        raise _error(f"{context}.fork must be a boolean")
    duplicate_of = row["duplicate_of"]
    if duplicate_of is not None and (
        not isinstance(duplicate_of, str) or not duplicate_of.strip()
    ):
        raise _error(f"{context}.duplicate_of must be null or a non-empty string")
    partial = row["partial"]
    if not isinstance(partial, bool):
        raise _error(f"{context}.partial must be a boolean")

    return {
        "repo_id": repo_id,
        "url": url,
        "pin": pin,
        "dialect_family": dialect,
        "boundary_family": boundary,
        "score": score,
        "sites": sites,
        "fork": fork,
        "duplicate_of": duplicate_of,
        "partial": partial,
    }


def validate_candidates(document: Any) -> list[dict[str, Any]]:
    """Validate an input document and return normalized candidates."""
    root = _object(document, "input")
    if set(root) != {"candidates"}:
        extra = sorted(set(root) - {"candidates"})
        missing = "candidates" not in root
        if missing:
            raise _error("input is missing required field 'candidates'")
        raise _error(f"input has unknown field(s): {', '.join(extra)}")
    raw = root["candidates"]
    if not isinstance(raw, list):
        raise _error("input.candidates must be a list")
    candidates = [_validate_candidate(row, index) for index, row in enumerate(raw)]
    seen_repo_ids: set[str] = set()
    seen_attempts: set[tuple[str, str]] = set()
    for candidate in candidates:
        repo_id = candidate["repo_id"]
        if repo_id in seen_repo_ids:
            raise _error(f"duplicate repo_id {repo_id!r}")
        seen_repo_ids.add(repo_id)
        attempt = (candidate["url"], candidate["pin"])
        if attempt in seen_attempts:
            raise _error(
                f"duplicate repository attempt {candidate['url']!r}@{candidate['pin']}"
            )
        seen_attempts.add(attempt)
    return candidates


def load_candidates(path: str | Path) -> list[dict[str, Any]]:
    """Read candidates from *path* without modifying it."""
    source = Path(path)
    try:
        text = source.read_text(encoding="utf-8")
    except OSError as exc:
        raise CohortManifestError(f"cannot read candidates {source}: {exc}") from exc
    try:
        document = json.loads(
            text,
            parse_constant=lambda value: (_ for _ in ()).throw(
                _error(f"non-finite JSON number {value!r} is not allowed")
            ),
        )
    except CohortManifestError:
        raise
    except json.JSONDecodeError as exc:
        raise CohortManifestError(f"invalid JSON in {source}: {exc.msg}") from exc
    return validate_candidates(document)


def _canonical_content(cohort_id: str, repos: list[dict[str, Any]]) -> str:
    content = {"schema_version": SCHEMA_VERSION, "cohort_id": cohort_id, "repos": repos}
    return json.dumps(content, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def build_manifest(
    candidates: Any, cohort_id: str, limit: int
) -> dict[str, Any]:
    """Select eligible candidates and return a frozen, digest-bearing manifest."""
    if not isinstance(cohort_id, str) or not cohort_id.strip():
        raise CohortManifestError("cohort_id must be a non-empty string")
    if isinstance(limit, bool) or not isinstance(limit, int) or limit <= 0:
        raise CohortManifestError("limit must be a positive integer")
    if isinstance(candidates, Mapping):
        rows = validate_candidates(candidates)
    elif isinstance(candidates, list):
        rows = validate_candidates({"candidates": candidates})
    else:
        raise _error("candidates must be a list or input object")
    eligible = [
        row
        for row in rows
        if not row["fork"] and row["duplicate_of"] is None and not row["partial"]
    ]
    eligible.sort(
        key=lambda row: (
            -row["score"],
            row["dialect_family"],
            row["boundary_family"],
            row["repo_id"],
            row["url"],
        )
    )
    selected = eligible[:limit]
    if not selected:
        raise CohortManifestError("no eligible candidates remain after exclusions")
    repos = [{field: row[field] for field in OUTPUT_FIELDS} for row in selected]
    canonical = _canonical_content(cohort_id, repos)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return {
        "schema_version": SCHEMA_VERSION,
        "cohort_id": cohort_id,
        "manifest_digest": digest,
        "repos": repos,
    }


def build_manifest_from_path(path: str | Path, cohort_id: str, limit: int) -> dict[str, Any]:
    return build_manifest(load_candidates(path), cohort_id, limit)


def dumps_manifest(manifest: Mapping[str, Any]) -> str:
    """Serialize a generated manifest in stable, newline-terminated JSON."""
    return json.dumps(manifest, ensure_ascii=True, sort_keys=True, indent=2) + "\n"
