"""Deterministic saturation measurements for a frozen cohort manifest.

The public input schema is a JSON object with ``schema_version`` (currently
``"1"``) and ``repos``.  ``repos`` is an ordered list; order is significant
because the trailing two observations for each dialect family are the last
two observations for that family in manifest order::

    {
      "schema_version": "1",
      "repos": [
        {
          "repo_id": "owner/repo",
          "dialect_family": "py_re",
          "sites": 100,
          "novel_sites": 2,
          "new_reject_buckets": [],
          "properties_asked": 10,
          "properties_sat": 2,
          "properties_ground_truthed": 2,
          "properties_filed": 1,
          "properties_accepted": 0
        }
      ]
    }

All count fields are JSON integers, not booleans or floating-point values.
They must be non-negative; ``novel_sites`` cannot exceed ``sites``.  A repo
must have at least one site so its novelty rate has a defined denominator.
The product and target denominators are the cohort totals for
``properties_asked``; their thresholds are 50 and 100 respectively.

The compiler stop rule is deliberately exact: a family stops only when it has
at least two repos, each of its trailing two per-repo novelty rates is
strictly less than 0.03, and both trailing repos report no new reject buckets.
All threshold and novelty comparisons use integer arithmetic.  Rates in the
returned report are canonical decimal strings (12 fractional places maximum)
so JSON output is stable across runs and Python versions.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Mapping

SCHEMA_VERSION = "1"
PRODUCT_DENOMINATOR_THRESHOLD = 50
TARGET_DENOMINATOR_THRESHOLD = 100
TRAILING_REPO_COUNT = 2
NOVELTY_RATE_NUMERATOR = 3
NOVELTY_RATE_DENOMINATOR = 100

REPO_FIELDS = (
    "repo_id",
    "dialect_family",
    "sites",
    "novel_sites",
    "new_reject_buckets",
    "properties_asked",
    "properties_sat",
    "properties_ground_truthed",
    "properties_filed",
    "properties_accepted",
)
COUNT_FIELDS = (
    "sites",
    "novel_sites",
    "properties_asked",
    "properties_sat",
    "properties_ground_truthed",
    "properties_filed",
    "properties_accepted",
)


class ManifestError(ValueError):
    """Raised when a saturation manifest is malformed or unsafe to measure."""


def _fail(message: str) -> ManifestError:
    return ManifestError(f"invalid saturation manifest: {message}")


def _mapping(value: Any, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise _fail(f"{context} must be an object")
    return value


def _required(value: Mapping[str, Any], name: str, context: str) -> Any:
    if name not in value:
        raise _fail(f"{context} is missing required field {name!r}")
    return value[name]


def _nonnegative_int(value: Any, name: str, context: str) -> int:
    # bool is an int subclass, but accepting true/false for a count makes a
    # typo silently change the denominator.
    if isinstance(value, bool) or not isinstance(value, int):
        if isinstance(value, float):
            raise _fail(f"{context}.{name} must be a finite JSON integer")
        raise _fail(f"{context}.{name} must be a non-negative JSON integer")
    if value < 0:
        raise _fail(f"{context}.{name} must be non-negative")
    return value


def _text(value: Any, name: str, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise _fail(f"{context}.{name} must be a non-empty string")
    return value


def _validate_repo(raw: Any, index: int) -> dict[str, Any]:
    context = f"repos[{index}]"
    repo = _mapping(raw, context)
    missing = [field for field in REPO_FIELDS if field not in repo]
    if missing:
        raise _fail(f"{context} is missing required field(s): {', '.join(missing)}")

    repo_id = _text(repo["repo_id"], "repo_id", context)
    family = _text(repo["dialect_family"], "dialect_family", context)
    counts = {
        field: _nonnegative_int(repo[field], field, context) for field in COUNT_FIELDS
    }
    if counts["sites"] == 0:
        raise _fail(f"{context}.sites must be greater than zero to compute novelty rate")
    if counts["novel_sites"] > counts["sites"]:
        raise _fail(f"{context}.novel_sites cannot exceed sites")
    if counts["properties_sat"] > counts["properties_asked"]:
        raise _fail(f"{context}.properties_sat cannot exceed properties_asked")
    if counts["properties_ground_truthed"] > counts["properties_sat"]:
        raise _fail(
            f"{context}.properties_ground_truthed cannot exceed properties_sat"
        )
    if counts["properties_filed"] > counts["properties_ground_truthed"]:
        raise _fail(
            f"{context}.properties_filed cannot exceed properties_ground_truthed"
        )
    if counts["properties_accepted"] > counts["properties_filed"]:
        raise _fail(
            f"{context}.properties_accepted cannot exceed properties_filed"
        )

    buckets = repo["new_reject_buckets"]
    if not isinstance(buckets, list):
        raise _fail(f"{context}.new_reject_buckets must be a list of strings")
    clean_buckets: list[str] = []
    for bucket_index, bucket in enumerate(buckets):
        if not isinstance(bucket, str) or not bucket.strip():
            raise _fail(
                f"{context}.new_reject_buckets[{bucket_index}] must be a non-empty string"
            )
        clean_buckets.append(bucket)

    return {
        "repo_id": repo_id,
        "dialect_family": family,
        **counts,
        "new_reject_buckets": clean_buckets,
    }


def validate_manifest(manifest: Any) -> list[dict[str, Any]]:
    """Validate *manifest* and return normalized repo observations.

    The returned list preserves manifest order.  A bare list is accepted for
    library callers as a convenience, but the documented on-disk schema is an
    object containing ``schema_version`` and ``repos``.
    """
    if isinstance(manifest, list):
        raw_repos = manifest
    else:
        document = _mapping(manifest, "manifest")
        version = document.get("schema_version", SCHEMA_VERSION)
        if version not in (SCHEMA_VERSION, 1):
            raise _fail(f"unsupported schema_version {version!r}; expected {SCHEMA_VERSION!r}")
        raw_repos = _required(document, "repos", "manifest")

    if not isinstance(raw_repos, list):
        raise _fail("repos must be a list")

    normalized = [_validate_repo(repo, index) for index, repo in enumerate(raw_repos)]
    seen: set[str] = set()
    for repo in normalized:
        repo_id = repo["repo_id"]
        if repo_id in seen:
            raise _fail(f"repo_id {repo_id!r} occurs more than once")
        seen.add(repo_id)
    return normalized


def load_manifest(path: str | Path) -> list[dict[str, Any]]:
    """Read and validate a manifest without modifying it or its directory."""
    manifest_path = Path(path)
    try:
        text = manifest_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ManifestError(f"cannot read manifest {manifest_path}: {exc}") from exc
    try:
        document = json.loads(text, parse_constant=lambda value: (_ for _ in ()).throw(
            _fail(f"non-finite JSON number {value!r} is not allowed")
        ))
    except ManifestError:
        raise
    except json.JSONDecodeError as exc:
        raise ManifestError(f"invalid JSON in {manifest_path}: {exc.msg}") from exc
    return validate_manifest(document)


def _decimal_ratio(numerator: int, denominator: int, places: int = 12) -> str:
    """Return a deterministic, rounded decimal for a non-negative ratio."""
    if denominator <= 0:
        raise ValueError("ratio denominator must be positive")
    whole, remainder = divmod(numerator, denominator)
    digits: list[str] = []
    for _ in range(places):
        remainder *= 10
        digit, remainder = divmod(remainder, denominator)
        digits.append(str(digit))
    # Round half up using integers, avoiding platform-dependent binary floats.
    remainder *= 2
    if remainder >= denominator:
        carry = 1
        for index in range(len(digits) - 1, -1, -1):
            value = int(digits[index]) + carry
            digits[index] = str(value % 10)
            carry = value // 10
        whole += carry
    fractional = "".join(digits).rstrip("0")
    return f"{whole}.{fractional}" if fractional else str(whole)


def _rate(novel_sites: int, sites: int) -> str:
    return _decimal_ratio(novel_sites, sites)


def _repo_summary(repo: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "repo_id": repo["repo_id"],
        "sites": repo["sites"],
        "novel_sites": repo["novel_sites"],
        "novelty_rate": _rate(repo["novel_sites"], repo["sites"]),
        "new_reject_buckets": sorted(set(repo["new_reject_buckets"])),
    }


def _compiler_stop(trailing: list[Mapping[str, Any]]) -> bool:
    if len(trailing) != TRAILING_REPO_COUNT:
        return False
    return all(
        repo["novel_sites"] * NOVELTY_RATE_DENOMINATOR
        < NOVELTY_RATE_NUMERATOR * repo["sites"]
        and not repo["new_reject_buckets"]
        for repo in trailing
    )


def build_report(manifest: Any) -> dict[str, Any]:
    """Build a deterministic saturation report from a validated cohort."""
    repos = validate_manifest(manifest)
    by_family: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for repo in repos:
        by_family[repo["dialect_family"]].append(repo)

    families: dict[str, dict[str, Any]] = {}
    for family in sorted(by_family):
        family_repos = by_family[family]
        trailing = family_repos[-TRAILING_REPO_COUNT:]
        trailing_sites = sum(repo["sites"] for repo in trailing)
        trailing_novel = sum(repo["novel_sites"] for repo in trailing)
        families[family] = {
            "repo_count": len(family_repos),
            "repo_ids": [repo["repo_id"] for repo in family_repos],
            "trailing_two": [_repo_summary(repo) for repo in trailing],
            "trailing_two_novelty_rate": _rate(trailing_novel, trailing_sites),
            "compiler_stop": _compiler_stop(trailing),
        }

    totals = {field: sum(repo[field] for repo in repos) for field in COUNT_FIELDS}
    reject_buckets = sorted(
        {bucket for repo in repos for bucket in repo["new_reject_buckets"]}
    )
    product_denominator = totals["properties_asked"]
    target_denominator = totals["properties_asked"]
    return {
        "schema_version": SCHEMA_VERSION,
        "thresholds": {
            "compiler_novelty_rate_strictly_below": "0.03",
            "trailing_repos": TRAILING_REPO_COUNT,
            "product_denominator": PRODUCT_DENOMINATOR_THRESHOLD,
            "target_denominator": TARGET_DENOMINATOR_THRESHOLD,
        },
        "families": families,
        "compiler_stop": bool(families) and all(
            family["compiler_stop"] for family in families.values()
        ),
        "cohort_totals": {
            "repo_count": len(repos),
            "dialect_family_count": len(families),
            **totals,
            "new_reject_buckets": reject_buckets,
        },
        "product_denominator": product_denominator,
        "product_denominator_met": product_denominator >= PRODUCT_DENOMINATOR_THRESHOLD,
        "target_denominator": target_denominator,
        "target_denominator_met": target_denominator >= TARGET_DENOMINATOR_THRESHOLD,
    }


def report_from_path(path: str | Path) -> dict[str, Any]:
    """Load a manifest by path and return its deterministic report."""
    return build_report(load_manifest(path))


def dumps_report(report: Mapping[str, Any]) -> str:
    """Serialize a report in the canonical CLI form."""
    return json.dumps(report, indent=2, sort_keys=True) + "\n"
