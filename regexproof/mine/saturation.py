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
          "url": "https://github.com/owner/repo",
          "pin": "0123456789abcdef0123456789abcdef01234567",
          "dialect_family": "py_re",
          "sites": 100,
          "novel_sites": 2,
          "new_reject_buckets": [],
          "product_properties": [
            {
              "site": "src/validator.py:10:4",
              "question_id": "no-space",
              "kind": "property",
              "provenance": "human",
              "synthesized": false,
              "result": "unsat",
              "ground_truthed": false,
              "filed": false,
              "accepted": false
            }
          ]
        }
      ]
    }

``sites`` and ``novel_sites`` are JSON integers, not booleans or
floating-point values.  They must be non-negative; ``novel_sites`` cannot
exceed ``sites``.  A repo must have at least one site so its novelty rate has
a defined denominator. Product counts are derived only from unique
``(site, question_id)`` records with human provenance, a non-synthesized
product kind, and an explicit result. The product and target denominators are
the cohort totals for these records; their thresholds are 50 and 100.

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
import re
from typing import Any, Mapping

SCHEMA_VERSION = "1"
PRODUCT_DENOMINATOR_THRESHOLD = 50
TARGET_DENOMINATOR_THRESHOLD = 100
TRAILING_REPO_COUNT = 2
NOVELTY_RATE_NUMERATOR = 3
NOVELTY_RATE_DENOMINATOR = 100
PIN_RE = re.compile(r"^[0-9a-fA-F]{40}$")
PRODUCT_KINDS = frozenset({"property", "counterexample_finder", "bug_demo"})

REPO_FIELDS = (
    "repo_id",
    "url",
    "pin",
    "dialect_family",
    "sites",
    "novel_sites",
    "new_reject_buckets",
    "product_properties",
)
COUNT_FIELDS = ("sites", "novel_sites")
PROPERTY_FIELDS = frozenset(
    {
        "site",
        "question_id",
        "kind",
        "provenance",
        "synthesized",
        "result",
        "ground_truthed",
        "filed",
        "accepted",
    }
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


def _validate_properties(raw: Any, context: str) -> dict[str, int]:
    if not isinstance(raw, list):
        raise _fail(f"{context}.product_properties must be a list")
    seen: set[tuple[str, str]] = set()
    counts = {
        "properties_asked": 0,
        "properties_sat": 0,
        "properties_ground_truthed": 0,
        "properties_filed": 0,
        "properties_accepted": 0,
    }
    for index, item in enumerate(raw):
        item_context = f"{context}.product_properties[{index}]"
        prop = _mapping(item, item_context)
        if set(prop) != PROPERTY_FIELDS:
            missing = sorted(PROPERTY_FIELDS - set(prop))
            extra = sorted(set(prop) - PROPERTY_FIELDS)
            if missing:
                raise _fail(
                    f"{item_context} is missing required field(s): {', '.join(missing)}"
                )
            raise _fail(f"{item_context} has unknown field(s): {', '.join(extra)}")
        site = _text(prop["site"], "site", item_context)
        question_id = _text(prop["question_id"], "question_id", item_context)
        identity = (site, question_id)
        if identity in seen:
            raise _fail(
                f"{item_context} duplicates product identity ({site!r}, {question_id!r})"
            )
        seen.add(identity)
        kind = _text(prop["kind"], "kind", item_context)
        if kind not in PRODUCT_KINDS:
            raise _fail(f"{item_context}.kind {kind!r} is not a product kind")
        if prop["provenance"] != "human":
            raise _fail(f"{item_context}.provenance must be 'human'")
        if prop["synthesized"] is not False:
            raise _fail(f"{item_context}.synthesized must be false")
        result = prop["result"]
        if result not in {"sat", "unsat"}:
            raise _fail(f"{item_context}.result must be 'sat' or 'unsat'")
        for field in ("ground_truthed", "filed", "accepted"):
            if not isinstance(prop[field], bool):
                raise _fail(f"{item_context}.{field} must be a boolean")
        if prop["ground_truthed"] and result != "sat":
            raise _fail(f"{item_context}.ground_truthed requires result 'sat'")
        if prop["filed"] and not prop["ground_truthed"]:
            raise _fail(f"{item_context}.filed requires ground_truthed")
        if prop["accepted"] and not prop["filed"]:
            raise _fail(f"{item_context}.accepted requires filed")
        counts["properties_asked"] += 1
        counts["properties_sat"] += result == "sat"
        counts["properties_ground_truthed"] += prop["ground_truthed"]
        counts["properties_filed"] += prop["filed"]
        counts["properties_accepted"] += prop["accepted"]
    return counts


def _validate_repo(raw: Any, index: int) -> dict[str, Any]:
    context = f"repos[{index}]"
    repo = _mapping(raw, context)
    missing = [field for field in REPO_FIELDS if field not in repo]
    if missing:
        raise _fail(f"{context} is missing required field(s): {', '.join(missing)}")

    repo_id = _text(repo["repo_id"], "repo_id", context)
    _text(repo["url"], "url", context)
    pin = _text(repo["pin"], "pin", context)
    if PIN_RE.fullmatch(pin) is None:
        raise _fail(f"{context}.pin must be exactly 40 hexadecimal characters")
    family = _text(repo["dialect_family"], "dialect_family", context)
    counts = {
        field: _nonnegative_int(repo[field], field, context) for field in COUNT_FIELDS
    }
    counts.update(_validate_properties(repo["product_properties"], context))
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
        "url": repo["url"],
        "pin": pin,
        "dialect_family": family,
        **counts,
        "new_reject_buckets": clean_buckets,
    }


def validate_manifest(manifest: Any) -> list[dict[str, Any]]:
    """Validate *manifest* and return normalized repo observations.

    The returned list preserves manifest order. The on-disk schema is an
    object containing exactly ``schema_version`` and ``repos``.
    """
    document = _mapping(manifest, "manifest")
    if set(document) != {"schema_version", "repos"}:
        missing = sorted({"schema_version", "repos"} - set(document))
        extra = sorted(set(document) - {"schema_version", "repos"})
        if missing:
            raise _fail(f"manifest is missing required field(s): {', '.join(missing)}")
        raise _fail(f"manifest has unknown field(s): {', '.join(extra)}")
    version = document["schema_version"]
    if version != SCHEMA_VERSION:
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
        def reject_duplicates(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    raise _fail(f"duplicate JSON key {key!r}")
                result[key] = value
            return result

        document = json.loads(
            text,
            object_pairs_hook=reject_duplicates,
            parse_constant=lambda value: (_ for _ in ()).throw(
                _fail(f"non-finite JSON number {value!r} is not allowed")
            ),
        )
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

    product_fields = (
        "properties_asked",
        "properties_sat",
        "properties_ground_truthed",
        "properties_filed",
        "properties_accepted",
    )
    totals = {
        field: sum(repo[field] for repo in repos)
        for field in (*COUNT_FIELDS, *product_fields)
    }
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
