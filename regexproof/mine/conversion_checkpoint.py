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
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping

from .cohort_manifest import CohortManifestError, validate_manifest as validate_cohort

SCHEMA_VERSION = "1"
PIN_RE = re.compile(r"^[0-9a-f]{40}$")
DIGEST_RE = re.compile(r"^[0-9a-f]{64}$")
PRODUCT_KINDS = frozenset({"property", "counterexample_finder", "bug_demo"})
TRUST_CLASSES = frozenset({"untrusted-input", "config", "internal"})
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
        "filed_plan",
        "filed",
        "private_first",
        "fixed_upstream",
        "wont_file",
        "false_positive",
        "approval_missing",
        "out_of_scope_redos",
    }
)
ROOT_FIELDS = {
    "schema_version",
    "cohort_id",
    "manifest_digest",
    "cohort",
    "expected_rows",
    "rows",
}
EXPECTED_ROW_FIELDS = {"repo_id", "url", "pin", "site", "question_id"}
ROW_FIELDS = {
    "repo_id",
    "url",
    "pin",
    "schema_version",
    "site",
    "question_id",
    "kind",
    "synthesized",
    "result",
    "domain",
    "contract",
    "ground_truth_status",
    "disposition",
    "canonical",
}
CONTRACT_FIELDS = {
    "schema_version",
    "site",
    "guarantee",
    "input_source",
    "trust",
    "declared_domain",
    "provenance",
}
CONTRACT_OPTIONAL_FIELDS = {"family_contract"}
DISPOSITION_FIELDS = {
    "status",
    "filed_at",
    "resolved_at",
    "approval_escape",
    "approval_ref",
    "reason_code",
    "backfilled",
    "disposition_date",
}
CANONICAL_REQUIRED_FIELDS = {
    "schema_version",
    "site",
    "contract",
    "domain",
    "kind",
    "synthesized",
    "result",
    "ground_truth_status",
}
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
    missing = sorted(CONTRACT_FIELDS - set(contract))
    extra = sorted(set(contract) - CONTRACT_FIELDS - CONTRACT_OPTIONAL_FIELDS)
    if missing:
        raise _fail(
            f"{context}.contract is missing required field(s): {', '.join(missing)}"
        )
    if extra:
        raise _fail(
            f"{context}.contract has unknown field(s): {', '.join(extra)}"
        )
    normalized = {
        field: _text(contract[field], field, f"{context}.contract")
        for field in CONTRACT_FIELDS
    }
    if normalized["schema_version"] != SCHEMA_VERSION:
        raise _fail(f"{context}.contract.schema_version must be {SCHEMA_VERSION!r}")
    if normalized["trust"] not in TRUST_CLASSES:
        raise _fail(
            f"{context}.contract.trust must be one of {sorted(TRUST_CLASSES)}"
        )
    if normalized["provenance"] != "human":
        raise _fail(f"{context}.contract.provenance must be 'human'")
    if contract["site"] != normalized["site"]:
        raise _fail(f"{context}.contract.site must be stable and non-empty")
    if "family_contract" in contract:
        if not isinstance(contract["family_contract"], Mapping):
            raise _fail(f"{context}.contract.family_contract must be an object")
        normalized["family_contract"] = contract["family_contract"]
    return normalized


def _iso_date_or_timestamp(value: Any, field: str, context: str) -> str | None:
    if value is None:
        return None
    text = _text(value, field, context)
    try:
        date.fromisoformat(text)
    except ValueError:
        try:
            datetime.fromisoformat(text.replace("Z", "+00:00"))
        except ValueError as exc:
            raise _fail(f"{context}.{field} must be an ISO date or timestamp") from exc
    return text


def _validate_disposition(value: Any, context: str) -> dict[str, str | None]:
    disposition = _object(value, f"{context}.disposition")
    _exact_fields(disposition, DISPOSITION_FIELDS, f"{context}.disposition")
    status = _text(disposition["status"], "status", f"{context}.disposition")
    if status not in DISPOSITION_STATUSES:
        raise _fail(f"{context}.disposition.status {status!r} is unknown")
    filed_at = _iso_date_or_timestamp(disposition["filed_at"], "filed_at", context)
    resolved_at = _iso_date_or_timestamp(
        disposition["resolved_at"], "resolved_at", context
    )
    approval_escape = disposition["approval_escape"]
    if approval_escape is not None:
        approval_escape = _text(approval_escape, "approval_escape", context)
    approval_ref = disposition["approval_ref"]
    if approval_ref is not None:
        approval_ref = _text(approval_ref, "approval_ref", context)
    reason_code = disposition["reason_code"]
    if reason_code is not None:
        reason_code = _text(reason_code, "reason_code", context)
    if not isinstance(disposition["backfilled"], bool):
        raise _fail(f"{context}.disposition.backfilled must be boolean")
    disposition_date = disposition["disposition_date"]
    if disposition["backfilled"]:
        if disposition_date != "unknown_date":
            disposition_date = _iso_date_or_timestamp(
                disposition_date, "disposition_date", context
            )
            if disposition_date is None:
                raise _fail(
                    f"{context}.disposition.disposition_date is required when backfilled"
                )
    elif disposition_date is not None:
        raise _fail(
            f"{context}.disposition.disposition_date is only valid for backfilled rows"
        )
    if status in {"filed", "filed_plan", "private_first", "fixed_upstream"}:
        if filed_at is None and resolved_at is None and not disposition["backfilled"]:
            raise _fail(
                f"{context}.disposition filing status requires filed_at or resolved_at"
            )
    if status == "approval_missing":
        if approval_escape == "approval_present":
            if approval_ref is None:
                raise _fail(
                    f"{context}.disposition approval_missing requires approval_ref"
                )
        elif approval_escape == "wont_file":
            if reason_code is None:
                raise _fail(
                    f"{context}.disposition approval_missing with wont_file escape "
                    "requires reason_code"
                )
        else:
            raise _fail(
                f"{context}.disposition approval_missing requires approval_escape"
            )
    return {
        "status": status,
        "filed_at": filed_at,
        "resolved_at": resolved_at,
        "approval_escape": approval_escape,
        "approval_ref": approval_ref,
        "reason_code": reason_code,
        "backfilled": disposition["backfilled"],
        "disposition_date": disposition_date,
    }


def _validate_row(value: Any, index: int) -> dict[str, Any]:
    context = f"rows[{index}]"
    row = _object(value, context)
    _exact_fields(row, ROW_FIELDS, context)
    normalized = {
        "repo_id": _text(row["repo_id"], "repo_id", context),
        "url": _text(row["url"], "url", context),
        "pin": _pin(row["pin"], context),
        "schema_version": _text(row["schema_version"], "schema_version", context),
        "site": _text(row["site"], "site", context),
        "question_id": _text(row["question_id"], "question_id", context),
        "kind": _text(row["kind"], "kind", context),
        "synthesized": row["synthesized"],
        "result": row["result"],
        "domain": _text(row["domain"], "domain", context),
        "ground_truth_status": row["ground_truth_status"],
    }
    if normalized["schema_version"] != SCHEMA_VERSION:
        raise _fail(f"{context}.schema_version must be {SCHEMA_VERSION!r}")
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
    if normalized["contract"]["site"] != normalized["site"]:
        raise _fail(f"{context}.contract.site must equal row.site")
    canonical = _object(row["canonical"], f"{context}.canonical")
    missing_canonical = sorted(CANONICAL_REQUIRED_FIELDS - set(canonical))
    if missing_canonical:
        raise _fail(
            f"{context}.canonical is missing required field(s): "
            f"{', '.join(missing_canonical)}"
        )
    if canonical["schema_version"] != normalized["schema_version"]:
        raise _fail(f"{context}.canonical.schema_version does not match row")
    if canonical["site"] != normalized["site"]:
        raise _fail(f"{context}.canonical.site does not match row")
    if canonical["domain"] != normalized["domain"]:
        raise _fail(f"{context}.canonical.domain does not match row")
    if canonical["kind"] != normalized["kind"]:
        raise _fail(f"{context}.canonical.kind does not match row")
    if canonical["synthesized"] is not normalized["synthesized"]:
        raise _fail(f"{context}.canonical.synthesized does not match row")
    canonical_result = "sat" if canonical["result"] == "gap" else canonical["result"]
    if canonical_result != normalized["result"]:
        raise _fail(f"{context}.canonical.result does not match row")
    canonical_gt = canonical["ground_truth_status"]
    if canonical_gt is None:
        canonical_gt = "not_applicable" if canonical_result == "unsat" else "not_run"
    if canonical_gt != normalized["ground_truth_status"]:
        raise _fail(f"{context}.canonical.ground_truth_status does not match row")
    canonical_contract = _validate_contract(canonical["contract"], f"{context}.canonical")
    if canonical_contract != normalized["contract"]:
        raise _fail(f"{context}.canonical.contract does not match row.contract")
    canonical_qid = canonical.get("question_id") or canonical.get("name")
    if not isinstance(canonical_qid, str) or not canonical_qid.strip():
        raise _fail(f"{context}.canonical requires question_id or name")
    if canonical_qid.strip() != normalized["question_id"]:
        raise _fail(f"{context}.canonical question identity does not match row")
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
    if status in {"wont_file", "false_positive", "approval_missing", "out_of_scope_redos"} and normalized[
        "result"
    ] == "sat" and not gt:
        raise _fail(f"{context}.disposition {status!r} requires ground truth")
    normalized["canonical"] = canonical
    return normalized


def canonical_row_to_checkpoint(
    canonical: Mapping[str, Any],
    *,
    repo_id: str,
    url: str,
    pin: str,
    disposition: Mapping[str, Any],
) -> dict[str, Any]:
    """Normalize one ``*_conversion.ndjson`` row for a checkpoint.

    The full canonical row is retained under ``canonical``.  The only
    intentional normalization is ``gap`` -> ``sat`` and a null UNSAT ground
    truth marker -> ``not_applicable`` (a null SAT marker becomes ``not_run``).
    A disposition is mandatory because canonical conversion artifacts do not
    own filing state.
    """
    raw = dict(canonical)
    missing = sorted(CANONICAL_REQUIRED_FIELDS - set(raw))
    if missing:
        raise _fail(f"canonical row is missing required field(s): {', '.join(missing)}")
    context = "canonical row"
    raw_schema = _text(raw["schema_version"], "schema_version", context)
    if raw_schema != SCHEMA_VERSION:
        raise _fail(f"canonical.schema_version must be {SCHEMA_VERSION!r}")
    site = _text(raw["site"], "site", context)
    qid_value = raw.get("question_id") or raw.get("name")
    question_id = _text(qid_value, "question_id", context).strip()
    kind = _text(raw["kind"], "kind", context)
    synthesized = raw["synthesized"]
    if synthesized is not False:
        raise _fail("canonical.synthesized must be false")
    if kind not in PRODUCT_KINDS:
        raise _fail(f"canonical.kind must be one of {sorted(PRODUCT_KINDS)}")
    result = raw["result"]
    if result == "gap":
        normalized_result = "sat"
    elif result in {"sat", "unsat"}:
        normalized_result = result
    else:
        raise _fail("canonical.result must be sat, gap, or unsat")
    ground_truth = raw["ground_truth_status"]
    if ground_truth is None:
        ground_truth = "not_applicable" if normalized_result == "unsat" else "not_run"
    if not isinstance(ground_truth, str) or ground_truth not in GT_STATUSES:
        raise _fail("canonical.ground_truth_status is unknown")
    contract = _validate_contract(raw["contract"], context)
    domain = _text(raw["domain"], "domain", context)
    if contract["site"] != site:
        raise _fail("canonical.contract.site must equal canonical.site")
    return {
        "repo_id": _text(repo_id, "repo_id", "checkpoint row"),
        "url": _text(url, "url", "checkpoint row"),
        "pin": _pin(pin, "checkpoint row"),
        "schema_version": raw_schema,
        "site": site,
        "question_id": question_id,
        "kind": kind,
        "synthesized": synthesized,
        "result": normalized_result,
        "domain": domain,
        "contract": contract,
        "ground_truth_status": ground_truth,
        "disposition": dict(disposition),
        "canonical": raw,
    }


def checkpoint_from_canonical_rows(
    canonical_rows: list[Mapping[str, Any]],
    *,
    cohort: Mapping[str, Any],
    expected_rows: list[Mapping[str, Any]],
    repo_id: str,
    url: str,
    pin: str,
    dispositions: Mapping[tuple[str, str], Mapping[str, Any]],
) -> dict[str, Any]:
    """Build a complete checkpoint envelope from canonical rows.

    ``expected_rows`` is deliberately independent input.  The function fails
    if canonical rows or dispositions omit an expected stable identity.
    """
    normalized = []
    for raw in canonical_rows:
        raw_site = _text(raw.get("site"), "site", "canonical row")
        raw_qid = _text(raw.get("question_id") or raw.get("name"), "question_id", "canonical row")
        key = (raw_site, raw_qid.strip())
        if key not in dispositions:
            raise _fail(f"missing disposition for canonical identity {key!r}")
        normalized.append(
            canonical_row_to_checkpoint(
                raw,
                repo_id=repo_id,
                url=url,
                pin=pin,
                disposition=dispositions[key],
            )
        )
    result = dict(cohort)
    checkpoint = {
        "schema_version": SCHEMA_VERSION,
        "cohort_id": _text(result.get("cohort_id"), "cohort_id", "cohort"),
        "manifest_digest": _digest(result.get("manifest_digest"), "manifest_digest", "cohort"),
        "cohort": result,
        "expected_rows": [dict(item) for item in expected_rows],
        "rows": normalized,
    }
    _validated_root(checkpoint)
    return checkpoint


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
    expected_rows = root["expected_rows"]
    if not isinstance(expected_rows, list) or not expected_rows:
        raise _fail("expected_rows must be a non-empty list")

    allowed = {
        (repo["repo_id"], repo["url"], repo["pin"]): repo for repo in cohort["repos"]
    }
    expected: set[tuple[str, str, str, str, str]] = set()
    for index, raw in enumerate(expected_rows):
        context = f"expected_rows[{index}]"
        item = _object(raw, context)
        _exact_fields(item, EXPECTED_ROW_FIELDS, context)
        identity = (
            _text(item["repo_id"], "repo_id", context),
            _text(item["url"], "url", context),
            _pin(item["pin"], context),
            _text(item["site"], "site", context),
            _text(item["question_id"], "question_id", context),
        )
        if identity[:3] not in allowed:
            raise _fail(f"{context} repository is outside the frozen cohort")
        if identity in expected:
            raise _fail(f"{context} duplicates expected stable product identity")
        expected.add(identity)

    normalized: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str, str, str]] = set()
    for index, raw in enumerate(rows):
        row = _validate_row(raw, index)
        repo_identity = (row["repo_id"], row["url"], row["pin"])
        if repo_identity not in allowed:
            raise _fail(f"rows[{index}] repository is outside the frozen cohort")
        identity = (
            row["repo_id"],
            row["url"],
            row["pin"],
            row["site"],
            row["question_id"],
        )
        if identity in seen:
            raise _fail(f"rows[{index}] duplicates stable product identity")
        if identity not in expected:
            raise _fail(f"rows[{index}] is not listed in expected_rows")
        seen.add(identity)
        normalized.append(row)
    missing = sorted(expected - seen)
    if missing:
        raise _fail(f"rows omit expected stable product identity {missing[0]!r}")
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
        if row["disposition"]["status"] != "filed_plan"
        and (
            row["disposition"]["status"] in FILED_STATUSES
            or row["disposition"]["filed_at"] is not None
        )
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
        "sample_sizes": {
            "unit": "human product properties",
            "asked": asked,
            "sat": len(sat_rows),
            "ground_truthed": len(gt_rows),
        },
        "target_status": {
            str(target): {
                "target": target,
                "observed": asked,
                "reached": asked >= target,
                "status": "reached" if asked >= target else "sub_target",
                "shortfall": max(0, target - asked),
            }
            for target in TARGETS
        },
        "filing_interpretation": {
            "filed_statuses": sorted(FILED_STATUSES),
            "filed_at_also_counts_as_filed": True,
            "filed_plan_is_not_filed": True,
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
    "canonical_row_to_checkpoint",
    "checkpoint_from_canonical_rows",
    "dumps_report",
    "load_checkpoint",
    "report_from_path",
    "validate_checkpoint",
    "wilson_interval",
]
