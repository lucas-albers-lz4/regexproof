"""Strict, read-only conversion checkpoint for a frozen cohort.

This artifact is intentionally separate from ``conversion-ledger.py``.  The
ledger is the historical aggregate; this module validates one immutable,
digest-bound cohort and its complete product evidence before calculating the
funnel.  Only human, non-synthesized product rows are admissible.

The interval reported by :func:`build_report` is a two-sided 95% Wilson score
interval.  The widths for the 50 and 100 targets are the *maximum* interval
width over every possible success count at that sample size.  They therefore
describe the worst-case precision available from a target-sized checkpoint,
not uncertainty around this particular cohort's observed rate.
"""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any, Mapping

from .cohort_manifest import CohortManifestError, validate_manifest as validate_cohort

SCHEMA_VERSION = "1"
PIN_RE = re.compile(r"^[0-9a-f]{40}$")
DIGEST_RE = re.compile(r"^[0-9a-f]{64}$")
PRODUCT_KINDS = frozenset({"property", "counterexample_finder", "bug_demo"})
GT_PASS = frozenset({"reproduced", "PASS"})
GT_STATUSES = frozenset(
    {"not_applicable", "not_run", "unknown", "failed", "reproduced", "PASS"}
)
# Kept in lockstep with scripts/conversion-ledger.py.  Do not broaden this
# list without updating that source-of-truth vocabulary and this contract.
FILED_STATUSES = frozenset({"filed", "private_first", "fixed_upstream"})
ACCEPTED_STATUSES = frozenset({"fixed_upstream"})
DISPOSITION_STATUSES = frozenset(
    {
        "pending",
        "filed_plan",
        "filed",
        "private_first",
        "fixed_upstream",
        "wont_file",
        "false_positive",
        "out_of_scope_redos",
        "not_applicable",
    }
)
ROOT_FIELDS = {"schema_version", "cohort_id", "manifest_digest", "cohort", "rows"}
ROW_FIELDS = {
    "repo_id",
    "url",
    "pin",
    "site",
    "question_id",
    "kind",
    "synthesized",
    "result",
    "contract",
    "ground_truth_status",
    "disposition",
}
CONTRACT_FIELDS = {"guarantee", "input_source", "trust_class", "domain", "provenance"}
DISPOSITION_FIELDS = {"status", "filed_at"}
TARGETS = (50, 100)


class ConversionCheckpointError(ValueError):
    """Raised when a conversion checkpoint is malformed or untrustworthy."""


def _fail(message: str) -> ConversionCheckpointError:
    return ConversionCheckpointError(f"invalid conversion checkpoint: {message}")


def _object(value: Any, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise _fail(f"{context} must be an object")
    return value


def _text(value: Any, field: str, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise _fail(f"{context}.{field} must be a non-empty string")
    return value


def _exact_fields(value: Mapping[str, Any], expected: set[str], context: str) -> None:
    actual = set(value)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing:
        raise _fail(f"{context} is missing required field(s): {', '.join(missing)}")
    if extra:
        raise _fail(f"{context} has unknown field(s): {', '.join(extra)}")


def _digest(value: Any, field: str, context: str) -> str:
    text = _text(value, field, context)
    if DIGEST_RE.fullmatch(text) is None:
        raise _fail(f"{context}.{field} must be 64 lowercase hexadecimal characters")
    return text


def _pin(value: Any, context: str) -> str:
    text = _text(value, "pin", context)
    if PIN_RE.fullmatch(text) is None:
        raise _fail(f"{context}.pin must be exactly 40 lowercase hexadecimal characters")
    return text


def _is_gt_pass(status: str) -> bool:
    return status in GT_PASS


def _validate_contract(value: Any, context: str) -> dict[str, str]:
    contract = _object(value, f"{context}.contract")
    _exact_fields(contract, CONTRACT_FIELDS, f"{context}.contract")
    normalized = {
        field: _text(contract[field], field, f"{context}.contract")
        for field in ("guarantee", "input_source", "trust_class", "domain", "provenance")
    }
    if normalized["provenance"] != "human":
        raise _fail(f"{context}.contract.provenance must be 'human'")
    return normalized


def _validate_disposition(value: Any, context: str) -> dict[str, str | None]:
    disposition = _object(value, f"{context}.disposition")
    _exact_fields(disposition, DISPOSITION_FIELDS, f"{context}.disposition")
    status = _text(disposition["status"], "status", f"{context}.disposition")
    if status not in DISPOSITION_STATUSES:
        raise _fail(f"{context}.disposition.status {status!r} is unknown")
    filed_at = disposition["filed_at"]
    if filed_at is not None:
        filed_at = _text(filed_at, "filed_at", f"{context}.disposition")
    return {"status": status, "filed_at": filed_at}


def _validate_row(value: Any, index: int) -> dict[str, Any]:
    context = f"rows[{index}]"
    row = _object(value, context)
    _exact_fields(row, ROW_FIELDS, context)
    normalized = {
        "repo_id": _text(row["repo_id"], "repo_id", context),
        "url": _text(row["url"], "url", context),
        "pin": _pin(row["pin"], context),
        "site": _text(row["site"], "site", context),
        "question_id": _text(row["question_id"], "question_id", context),
        "kind": _text(row["kind"], "kind", context),
        "synthesized": row["synthesized"],
        "result": row["result"],
        "ground_truth_status": row["ground_truth_status"],
    }
    if normalized["kind"] not in PRODUCT_KINDS:
        raise _fail(
            f"{context}.kind must be one of {sorted(PRODUCT_KINDS)}; rule_diff and other kinds are excluded"
        )
    if normalized["synthesized"] is not False:
        raise _fail(f"{context}.synthesized must be false")
    if normalized["result"] not in {"sat", "unsat"}:
        raise _fail(f"{context}.result must be 'sat' or 'unsat'")
    gt_status = normalized["ground_truth_status"]
    if not isinstance(gt_status, str) or gt_status not in GT_STATUSES:
        raise _fail(f"{context}.ground_truth_status is unknown")
    if normalized["result"] == "unsat" and gt_status != "not_applicable":
        raise _fail(f"{context}.ground_truth_status must be 'not_applicable' for UNSAT")
    if normalized["result"] == "sat" and gt_status == "not_applicable":
        raise _fail(f"{context}.ground_truth_status cannot be 'not_applicable' for SAT")
    normalized["contract"] = _validate_contract(row["contract"], context)
    normalized["disposition"] = _validate_disposition(row["disposition"], context)
    status = normalized["disposition"]["status"]
    filed_at = normalized["disposition"]["filed_at"]
    gt = _is_gt_pass(gt_status)
    filed_by_status = status in FILED_STATUSES
    accepted = status in ACCEPTED_STATUSES
    if (filed_by_status or filed_at is not None) and not (
        normalized["result"] == "sat" and gt
    ):
        raise _fail(f"{context}.disposition filing requires a ground-truthed SAT")
    if accepted and not (normalized["result"] == "sat" and gt):
        raise _fail(f"{context}.disposition accepted requires a ground-truthed SAT")
    if status in {"wont_file", "false_positive", "out_of_scope_redos"} and normalized[
        "result"
    ] == "sat" and not gt:
        raise _fail(f"{context}.disposition {status!r} requires ground truth")
    return normalized


def _validated_root(document: Any) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    root = _object(document, "checkpoint")
    _exact_fields(root, ROOT_FIELDS, "checkpoint")
    if root["schema_version"] != SCHEMA_VERSION:
        raise _fail(f"schema_version must be {SCHEMA_VERSION!r}")
    cohort_id = _text(root["cohort_id"], "cohort_id", "checkpoint")
    digest = _digest(root["manifest_digest"], "manifest_digest", "checkpoint")
    try:
        cohort = validate_cohort(root["cohort"])
    except CohortManifestError as exc:
        raise _fail(f"invalid frozen cohort: {exc}") from exc
    if cohort_id != cohort["cohort_id"]:
        raise _fail("cohort_id does not match the embedded frozen cohort")
    if digest != cohort["manifest_digest"]:
        raise _fail("manifest_digest does not match the embedded frozen cohort")
    rows = root["rows"]
    if not isinstance(rows, list):
        raise _fail("rows must be a list")

    allowed = {
        (repo["repo_id"], repo["url"], repo["pin"]): repo for repo in cohort["repos"]
    }
    normalized: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str, str, str]] = set()
    for index, raw in enumerate(rows):
        row = _validate_row(raw, index)
        repo_identity = (row["repo_id"], row["url"], row["pin"])
        if repo_identity not in allowed:
            raise _fail(f"rows[{index}] repository is outside the frozen cohort")
        identity = (cohort_id, row["url"], row["pin"], row["site"], row["question_id"])
        if identity in seen:
            raise _fail(f"rows[{index}] duplicates stable product identity")
        seen.add(identity)
        normalized.append(row)
    return cohort, normalized


def validate_checkpoint(document: Any) -> list[dict[str, Any]]:
    """Validate a checkpoint and return normalized product rows."""
    _cohort, rows = _validated_root(document)
    return rows


def _reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _fail(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise _fail(f"non-finite JSON number {value!r} is not allowed")


def load_checkpoint(path: str | Path) -> dict[str, Any]:
    """Load and validate a checkpoint without modifying the source file."""
    source = Path(path)
    try:
        text = source.read_text(encoding="utf-8")
    except OSError as exc:
        raise ConversionCheckpointError(f"cannot read checkpoint {source}: {exc}") from exc
    try:
        document = json.loads(
            text, object_pairs_hook=_reject_duplicates, parse_constant=_reject_constant
        )
    except ConversionCheckpointError:
        raise
    except json.JSONDecodeError as exc:
        raise ConversionCheckpointError(f"invalid JSON in {source}: {exc.msg}") from exc
    _validated_root(document)
    return document


def _inverse_normal(p: float) -> float:
    """Acklam inverse-normal approximation used for deterministic Wilson scores."""
    if not 0.0 < p < 1.0:
        raise ValueError("normal quantile probability must be between zero and one")
    a = (
        -39.6968302866538,
        220.946098424521,
        -275.928510446969,
        138.357751867269,
        -30.6647980661472,
        2.50662827745924,
    )
    b = (
        -54.4760987982241,
        161.585836858041,
        -155.698979859887,
        66.8013118877197,
        -13.2806815528857,
    )
    c = (
        -0.00778489400243029,
        -0.322396458041136,
        -2.40075827716184,
        -2.54973253934373,
        4.37466414146497,
        2.93816398269878,
    )
    d = (0.00778469570904146, 0.32246712907004, 2.445134137143, 3.75440866190742)
    plow = 0.02425
    if p < plow:
        q = math.sqrt(-2.0 * math.log(p))
        numerator = (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5])
        denominator = (((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1.0
        return numerator / denominator
    if p <= 1.0 - plow:
        q = p - 0.5
        r = q * q
        numerator = (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q
        denominator = ((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1.0
        return numerator / denominator
    q = math.sqrt(-2.0 * math.log(1.0 - p))
    numerator = (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5])
    denominator = (((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1.0
    return -numerator / denominator


def wilson_interval(
    successes: int, trials: int, confidence: float = 0.95
) -> tuple[float, float]:
    """Return a two-sided Wilson score interval using only the stdlib."""
    if isinstance(successes, bool) or isinstance(trials, bool) or trials <= 0:
        raise ValueError("trials must be a positive integer")
    if (
        not isinstance(successes, int)
        or not isinstance(trials, int)
        or not 0 <= successes <= trials
    ):
        raise ValueError("successes must be an integer in [0, trials]")
    if not 0.0 < confidence < 1.0 or not math.isfinite(confidence):
        raise ValueError("confidence must be finite and between zero and one")
    z = abs(_inverse_normal((1.0 - confidence) / 2.0))
    p = successes / trials
    denominator = 1.0 + z * z / trials
    centre = (p + z * z / (2.0 * trials)) / denominator
    half = z * math.sqrt(
        p * (1.0 - p) / trials + z * z / (4.0 * trials * trials)
    ) / denominator
    return max(0.0, centre - half), min(1.0, centre + half)


def _decimal(value: float) -> str:
    return f"{value:.12f}".rstrip("0").rstrip(".") or "0"


def _ratio(numerator: int, denominator: int) -> str | None:
    if denominator == 0:
        return None
    return _decimal(numerator / denominator)


def _target_intervals() -> dict[str, Any]:
    targets: dict[str, Any] = {}
    for trials in TARGETS:
        widths = []
        for successes in range(trials + 1):
            lower, upper = wilson_interval(successes, trials)
            widths.append((upper - lower, successes))
        width, at_successes = max(widths, key=lambda item: (item[0], -item[1]))
        targets[str(trials)] = {
            "max_width": _decimal(width),
            "successes_at_max_width": at_successes,
        }
    return targets


def build_report(document: Any) -> dict[str, Any]:
    """Return deterministic funnel counts and interpretations for a checkpoint."""
    cohort, rows = _validated_root(document)
    asked = len(rows)
    sat_rows = [row for row in rows if row["result"] == "sat"]
    gt_rows = [row for row in sat_rows if _is_gt_pass(row["ground_truth_status"])]
    filed_rows = [
        row
        for row in gt_rows
        if row["disposition"]["status"] in FILED_STATUSES
        or row["disposition"]["filed_at"] is not None
    ]
    private_rows = [
        row for row in gt_rows if row["disposition"]["status"] == "private_first"
    ]
    accepted_rows = [
        row for row in gt_rows if row["disposition"]["status"] in ACCEPTED_STATUSES
    ]
    counts = {
        "asked": asked,
        "sat": len(sat_rows),
        "ground_truthed": len(gt_rows),
        "filed": len(filed_rows),
        "private_first": len(private_rows),
        "accepted": len(accepted_rows),
    }
    rates = {
        "sat_per_asked": _ratio(counts["sat"], counts["asked"]),
        "ground_truthed_per_sat": _ratio(counts["ground_truthed"], counts["sat"]),
        "filed_per_ground_truthed": _ratio(counts["filed"], counts["ground_truthed"]),
        "private_first_per_ground_truthed": _ratio(
            counts["private_first"], counts["ground_truthed"]
        ),
        "accepted_per_ground_truthed": _ratio(
            counts["accepted"], counts["ground_truthed"]
        ),
    }
    dispositions = Counter(row["disposition"]["status"] for row in rows)
    return {
        "schema_version": SCHEMA_VERSION,
        "cohort_id": cohort["cohort_id"],
        "manifest_digest": cohort["manifest_digest"],
        "counts": counts,
        "rates": rates,
        "disposition_breakdown": {
            status: dispositions[status] for status in sorted(dispositions)
        },
        "filing_interpretation": {
            "filed_statuses": sorted(FILED_STATUSES),
            "filed_at_also_counts_as_filed": True,
            "private_first_is_filed": True,
            "accepted_statuses": sorted(ACCEPTED_STATUSES),
            "accepted_is_not_third_party_remediation": True,
            "third_party_remediation_requires_separate_classification": True,
        },
        "idiom_interpretation": {
            "compiler_saturation_measured_elsewhere": True,
            "product_conversion_checkpoint_is_not_compiler_saturation": True,
            "zero_gt_to_filed_does_not_prove_idiom_exhaustion": True,
        },
        "intervals": {
            "method": "wilson_score_95_two_sided",
            "target_width_meaning": (
                "maximum interval width over all success counts at the target sample size; "
                "it describes worst-case precision, not this cohort's observed rate"
            ),
            "targets": _target_intervals(),
        },
    }


def report_from_path(path: str | Path) -> dict[str, Any]:
    return build_report(load_checkpoint(path))


def dumps_report(report: Mapping[str, Any]) -> str:
    return json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True) + "\n"


__all__ = [
    "ConversionCheckpointError",
    "build_report",
    "dumps_report",
    "load_checkpoint",
    "report_from_path",
    "validate_checkpoint",
    "wilson_interval",
]
