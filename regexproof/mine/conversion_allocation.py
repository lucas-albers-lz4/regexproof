"""Deterministic, pre-outcome allocation of conversion review sites."""

from __future__ import annotations

import hashlib
import json
import re
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker, ValidationError

from regexproof.schemas import conversion_candidate_population_schema

SCHEMA_VERSION = "1"
SAMPLE_SIZE = 15
MAX_SAMPLE_SIZE = 15
STRATA = ("productive", "novel_idiom", "unbiased")
WEIGHTS = {"productive": 70, "novel_idiom": 20, "unbiased": 10}
TIE_ORDER = {"productive": 0, "novel_idiom": 1, "unbiased": 2}
CLASSES = frozenset({"productive", "novel_idiom", "unclassified"})
TRUST_CLASSES = frozenset({"untrusted-input", "config"})
CALL_KINDS = frozenset({"fullmatch", "match", "search", "exec", "substitution"})
_PIN = re.compile(r"^[0-9a-f]{40}$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_REGEX_ID = re.compile(r"^[0-9a-f]{32}$")


class AllocationError(ValueError):
    """Invalid or incomplete candidate population/allocation input."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise AllocationError(f"duplicate JSON key {key!r}")
        value[key] = item
    return value


def validate_population(population: Any) -> dict[str, Any]:
    """Validate the frozen pre-outcome population and its candidate identities."""
    try:
        Draft202012Validator(
            conversion_candidate_population_schema(), format_checker=FormatChecker()
        ).validate(population)
    except ValidationError as exc:
        raise AllocationError(f"invalid candidate population schema: {exc.message}") from exc
    if not isinstance(population, dict):
        raise AllocationError("candidate population must be a JSON object")
    required = {
        "schema_version", "population_id", "cluster", "repository_url",
        "source_pin", "idiom_bucket", "product_engine", "frozen_at",
        "inventory_sha256", "classification_sha256", "outcome_ledger_sha256",
        "selection_seed_sha256", "question_history_sha256", "candidates",
    }
    if not required.issubset(population):
        raise AllocationError(
            "candidate population is missing fields: "
            + ", ".join(sorted(required - set(population)))
        )
    if set(population) != required:
        raise AllocationError(
            "candidate population has unknown fields: "
            + ", ".join(sorted(set(population) - required))
        )
    if population.get("schema_version") != SCHEMA_VERSION:
        raise AllocationError("unsupported candidate population schema_version")
    for field in (
        "population_id", "cluster", "repository_url", "idiom_bucket",
        "product_engine", "frozen_at",
    ):
        value = population.get(field)
        if not isinstance(value, str) or not value.strip():
            raise AllocationError(f"population.{field} must be non-empty text")
    if not _PIN.fullmatch(str(population.get("source_pin") or "")):
        raise AllocationError("population.source_pin must be a 40-character pin")
    for field in (
        "inventory_sha256", "classification_sha256", "outcome_ledger_sha256",
        "selection_seed_sha256", "question_history_sha256",
    ):
        if not _SHA256.fullmatch(str(population.get(field) or "")):
            raise AllocationError(f"population.{field} must be a SHA-256 digest")
    candidates = population.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise AllocationError("candidate population must contain at least one eligible site")
    seen_sites: set[str] = set()
    seen_inventory_sites: set[str] = set()
    seen_ids: set[str] = set()
    required_candidate = {
        "regex_id", "site", "inventory_site", "source_file", "source_sha256", "idiom_bucket",
        "pattern", "flags", "dialect", "call_kind", "trust_class", "encodable",
        "idiom_key", "idiom_class", "classification_evidence", "prior_question_ids",
    }
    optional_candidate = {"shell_flags"}
    for i, candidate in enumerate(candidates):
        label = f"candidate[{i}]"
        if (
            not isinstance(candidate, dict)
            or not required_candidate.issubset(candidate)
            or set(candidate) - required_candidate - optional_candidate
        ):
            raise AllocationError(f"{label} is missing required candidate fields")
        if "shell_flags" in candidate:
            shell_flags = candidate["shell_flags"]
            if not isinstance(shell_flags, dict) or not isinstance(shell_flags.get("syntax"), str):
                raise AllocationError(f"{label}.shell_flags must preserve the product syntax selector")
        site = candidate.get("site")
        inventory_site = candidate.get("inventory_site")
        source_file = candidate.get("source_file")
        if not isinstance(site, str) or not site.strip():
            raise AllocationError(f"{label}.site must be non-empty text")
        if not isinstance(inventory_site, str) or not inventory_site.strip():
            raise AllocationError(f"{label}.inventory_site must be non-empty text")
        if not isinstance(source_file, str) or not source_file.strip():
            raise AllocationError(f"{label}.source_file must be non-empty text")
        if (
            source_file.startswith("/")
            or "\\" in source_file
            or ".." in source_file.split("/")
        ):
            raise AllocationError(f"{label}.source_file must be checkout-relative")
        if not site.startswith(source_file + ":"):
            raise AllocationError(f"{label}.site must be bound to source_file")
        regex_id = candidate.get("regex_id")
        if not isinstance(regex_id, str) or not _REGEX_ID.fullmatch(regex_id):
            raise AllocationError(f"{label}.regex_id must be a 32-character lowercase digest")
        if site in seen_sites or regex_id in seen_ids:
            raise AllocationError(f"duplicate candidate identity in population: {site}")
        if inventory_site in seen_inventory_sites:
            raise AllocationError(f"duplicate inventory site in population: {inventory_site}")
        seen_sites.add(site)
        seen_inventory_sites.add(inventory_site)
        seen_ids.add(regex_id)
        if candidate.get("idiom_bucket") != population["idiom_bucket"]:
            raise AllocationError(f"{label}.idiom_bucket differs from population bucket")
        if not _SHA256.fullmatch(str(candidate.get("source_sha256") or "")):
            raise AllocationError(f"{label}.source_sha256 must be a SHA-256 digest")
        if candidate.get("trust_class") not in TRUST_CLASSES:
            raise AllocationError(f"{label} is not at a declared config/untrusted boundary")
        if candidate.get("encodable") is not True:
            raise AllocationError(f"{label} is not marked encodable")
        if candidate.get("call_kind") not in CALL_KINDS:
            raise AllocationError(f"{label}.call_kind is unsupported")
        for field in ("pattern", "dialect", "idiom_key", "classification_evidence"):
            if not isinstance(candidate.get(field), str) or not candidate[field].strip():
                raise AllocationError(f"{label}.{field} must be non-empty text")
        if candidate.get("idiom_class") not in CLASSES:
            raise AllocationError(f"{label}.idiom_class is unsupported")
        prior = candidate.get("prior_question_ids")
        if not isinstance(prior, list) or prior:
            raise AllocationError(f"{label} was already asked or has invalid prior_question_ids")
    return population


def verify_inventory_binding(population: dict[str, Any], inventory_text: str) -> int:
    """Require each candidate to match one exact row in its frozen inventory."""
    inventory: dict[str, dict[str, Any]] = {}
    for line_number, line in enumerate(inventory_text.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line, object_pairs_hook=_unique_object)
        except json.JSONDecodeError as exc:
            raise AllocationError(f"inventory line {line_number} is invalid JSON") from exc
        if not isinstance(row, dict):
            raise AllocationError(f"inventory line {line_number} must be an object")
        regex_id = row.get("regex_id")
        if not isinstance(regex_id, str) or not regex_id:
            raise AllocationError(f"inventory line {line_number} has no regex_id")
        if regex_id in inventory:
            raise AllocationError(f"inventory has duplicate regex_id {regex_id}")
        inventory[regex_id] = row

    fields = ["site", "pattern", "flags", "dialect", "call_kind", "encodable"]
    for candidate in population["candidates"]:
        row = inventory.get(candidate["regex_id"])
        if row is None:
            raise AllocationError(
                f"candidate {candidate['regex_id']} is absent from the frozen inventory"
            )
        if row.get("corpus") != population["cluster"]:
            raise AllocationError(
                f"candidate {candidate['regex_id']} inventory corpus differs from population"
            )
        compared_fields = fields + (["shell_flags"] if "shell_flags" in candidate else [])
        if any(
            row.get(field)
            != (candidate["inventory_site"] if field == "site" else candidate[field])
            for field in compared_fields
        ):
            raise AllocationError(
                f"candidate {candidate['regex_id']} differs from its frozen inventory row"
            )
    return len(population["candidates"])


def verify_classification_binding(
    population: dict[str, Any], classification: Any
) -> int:
    """Require a one-to-one, digest-bound pre-outcome label for each candidate."""
    required = {
        "schema_version", "population_id", "source_pin", "outcome_ledger_sha256",
        "classifications",
    }
    if not isinstance(classification, dict) or set(classification) != required:
        raise AllocationError("classification evidence has invalid root fields")
    if (
        classification["schema_version"] != "1"
        or classification["population_id"] != population["population_id"]
        or classification["source_pin"] != population["source_pin"]
        or classification["outcome_ledger_sha256"] != population["outcome_ledger_sha256"]
    ):
        raise AllocationError("classification evidence does not bind this population and ledger")
    rows = classification["classifications"]
    if not isinstance(rows, list):
        raise AllocationError("classification evidence classifications must be a list")
    expected: dict[str, dict[str, Any]] = {
        row["regex_id"]: row for row in population["candidates"]
    }
    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or set(row) != {
            "regex_id", "idiom_key", "idiom_class", "evidence"
        }:
            raise AllocationError(f"classification row {index} has invalid fields")
        regex_id = row.get("regex_id")
        if not isinstance(regex_id, str) or regex_id not in expected or regex_id in seen:
            raise AllocationError(f"classification row {index} has unknown or duplicate regex_id")
        candidate = expected[regex_id]
        if (
            row.get("idiom_key") != candidate["idiom_key"]
            or row.get("idiom_class") != candidate["idiom_class"]
            or row.get("evidence") != candidate["classification_evidence"]
        ):
            raise AllocationError(f"classification differs from frozen candidate {regex_id}")
        seen.add(regex_id)
    if seen != set(expected):
        missing = sorted(set(expected) - seen)
        raise AllocationError(f"classification evidence omits candidates: {', '.join(missing)}")
    return len(seen)


def _weighted_quotas(sample_size: int, counts: dict[str, int]) -> dict[str, int]:
    """Hamilton quotas with one slot per available arm when capacity allows."""
    active = [
        name
        for name in STRATA
        if (counts.get(name, 0) > 0 if name != "unbiased" else sum(counts.values()) > 0)
    ]
    quotas = {name: 0 for name in STRATA}
    if sample_size <= 0 or not active:
        return quotas
    if sample_size >= len(active):
        for name in active:
            quotas[name] = 1
    remaining = sample_size - sum(quotas.values())
    while remaining > 0:
        available = [
            name for name in active
            if name == "unbiased" or quotas[name] < counts.get(name, 0)
        ]
        if not available:
            break
        total_weight = sum(WEIGHTS[name] for name in available)
        exact = {
            name: remaining * WEIGHTS[name] / total_weight
            for name in available
        }
        assigned = 0
        for name in available:
            room = remaining if name == "unbiased" else max(0, counts[name] - quotas[name])
            extra = min(room, int(exact[name]))
            if extra:
                quotas[name] += extra
                assigned += extra
        remaining -= assigned
        if remaining == 0:
            break
        available = [
            name for name in available
            if name == "unbiased" or quotas[name] < counts.get(name, 0)
        ]
        if not available:
            break
        total_weight = sum(WEIGHTS[name] for name in available)
        winner = min(
            available,
            key=lambda name: (
                -(remaining * WEIGHTS[name] / total_weight
                  - int(remaining * WEIGHTS[name] / total_weight)),
                TIE_ORDER[name],
            ),
        )
        quotas[winner] += 1
        remaining -= 1
    return quotas


def _ranked(candidates: list[dict[str, Any]], seed: str, arm: str) -> list[dict[str, Any]]:
    return sorted(
        candidates,
        key=lambda row: (
            hashlib.sha256(f"{seed}\0{arm}\0{row['regex_id']}".encode()).hexdigest(),
            row["regex_id"],
        ),
    )


def allocate_candidates(
    population: Any,
    *,
    seed: str,
    sample_size: int = SAMPLE_SIZE,
) -> dict[str, Any]:
    """Select review candidates deterministically from a frozen eligible pool.

    The unbiased arm is a uniform keyed-hash draw from the complete eligible
    population. Productive and novel-idiom arms use their pre-outcome labels;
    they exclude sites already selected by the unbiased arm. Shortfalls are
    filled by a second uniform draw and reported as ``unbiased_reallocation``.
    """
    data = validate_population(population)
    if not _SHA256.fullmatch(seed):
        raise AllocationError("selection seed must be a 64-character lowercase SHA-256 value")
    if hashlib.sha256(seed.encode()).hexdigest() != data["selection_seed_sha256"]:
        raise AllocationError("selection seed does not match the frozen population commitment")
    if type(sample_size) is not int or not 1 <= sample_size <= MAX_SAMPLE_SIZE:
        raise AllocationError(f"sample_size must be an integer in 1..{MAX_SAMPLE_SIZE}")
    rows = list(data["candidates"])
    size = min(sample_size, len(rows))
    counts = {
        "productive": sum(row["idiom_class"] == "productive" for row in rows),
        "novel_idiom": sum(row["idiom_class"] == "novel_idiom" for row in rows),
        "unbiased": len(rows),
    }
    quotas = _weighted_quotas(size, counts)
    chosen: list[dict[str, Any]] = []
    selected: set[str] = set()

    def add(pool: list[dict[str, Any]], amount: int, mode: str, arm: str) -> int:
        if amount <= 0:
            return 0
        added = 0
        for row in _ranked(pool, seed, arm):
            if row["regex_id"] in selected:
                continue
            item = dict(row)
            item["selection_mode"] = mode
            chosen.append(item)
            selected.add(row["regex_id"])
            added += 1
            if added == amount:
                break
        return added

    unbiased_pool = rows
    unbiased_selected = add(unbiased_pool, quotas["unbiased"], "unbiased", "unbiased")
    productive_pool = [row for row in rows if row["idiom_class"] == "productive"]
    novel_pool = [row for row in rows if row["idiom_class"] == "novel_idiom"]
    productive_selected = add(
        productive_pool, quotas["productive"], "productive", "productive"
    )
    novel_selected = add(novel_pool, quotas["novel_idiom"], "novel_idiom", "novel_idiom")
    shortfall = size - len(chosen)
    reallocated = add(
        [row for row in rows if row["regex_id"] not in selected],
        shortfall,
        "unbiased_reallocation",
        "unbiased_reallocation",
    )
    if len(chosen) != size:
        raise AllocationError("allocator could not fill the requested sample from its population")
    actual = {name: 0 for name in (*STRATA, "unbiased_reallocation")}
    for row in chosen:
        actual[row["selection_mode"]] += 1
    return {
        "schema_version": SCHEMA_VERSION,
        "population_id": data["population_id"],
        "cluster": data["cluster"],
        "repository_url": data["repository_url"],
        "source_pin": data["source_pin"],
        "idiom_bucket": data["idiom_bucket"],
        "sample_size_requested": sample_size,
        "sample_size_selected": size,
        "selection_seed": seed,
        "selection_seed_sha256": hashlib.sha256(seed.encode()).hexdigest(),
        "allocation_shares": {name: WEIGHTS[name] / 100 for name in STRATA},
        "population_stratum_counts": counts,
        "nominal_quotas": quotas,
        "actual_selection_counts": actual,
        "unbiased_unique_count": unbiased_selected,
        "productive_unique_count": productive_selected,
        "novel_idiom_unique_count": novel_selected,
        "unbiased_reallocation_count": reallocated,
        "selected_candidates": chosen,
    }
