"""Active-time measurements for human conversion-wave site reviews.

This log is separate from ``operator_minutes.jsonl`` (admission review) and
from conversion checkpoint evidence. One row represents one completed
ranked-site review, including a recorded skip.
"""

from __future__ import annotations

import json
import math
import pathlib
import re
import statistics
import uuid
from collections import Counter
from datetime import datetime, timezone
from typing import Any

LOG_PATH = (
    pathlib.Path(__file__).resolve().parents[2]
    / "properties"
    / "generated"
    / "conversion_review_minutes.jsonl"
)
PIN_RE = re.compile(r"^[0-9a-f]{40}$")
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
OUTCOMES = frozenset(
    {
        "contracted",
        "skipped_unreachable",
        "skipped_out_of_scope",
        "skipped_no_response",
        "skipped_duplicate",
    }
)


class ConversionReviewError(ValueError):
    """Invalid or duplicate conversion-review measurement."""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _required_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ConversionReviewError(f"{field} is required")
    text = value.strip()
    if text != value:
        raise ConversionReviewError(f"{field} may not have surrounding whitespace")
    if "\x00" in text:
        raise ConversionReviewError(f"{field} may not contain NUL")
    if field.endswith(".site") and ("\n" in text or "\r" in text):
        raise ConversionReviewError(f"{field} may not contain line breaks")
    return text


def _validate_row(row: Any, index: int) -> dict[str, Any]:
    context = f"row {index}"
    if not isinstance(row, dict):
        raise ConversionReviewError(f"{context} must be an object")
    required = {
        "schema_version",
        "measurement_id",
        "corpus",
        "pin",
        "wave_id",
        "idiom_bucket",
        "site",
        "rank",
        "question_id",
        "outcome",
        "source",
        "active_minutes",
        "recorded_at",
    }
    missing = sorted(required - set(row))
    extra = sorted(set(row) - required)
    if missing or extra:
        details = []
        if missing:
            details.append(f"missing {', '.join(missing)}")
        if extra:
            details.append(f"unknown {', '.join(extra)}")
        raise ConversionReviewError(f"{context}: {'; '.join(details)}")
    if row["schema_version"] != "1":
        raise ConversionReviewError(f"{context}.schema_version must be '1'")
    _required_text(row["measurement_id"], f"{context}.measurement_id")
    for field in ("corpus", "wave_id", "idiom_bucket"):
        value = _required_text(row[field], f"{context}.{field}")
        if ID_RE.fullmatch(value) is None:
            raise ConversionReviewError(
                f"{context}.{field} must be a plain identifier"
            )
    pin = _required_text(row["pin"], f"{context}.pin")
    if PIN_RE.fullmatch(pin) is None:
        raise ConversionReviewError(
            f"{context}.pin must be 40 lowercase hexadecimal characters"
        )
    site = _required_text(row["site"], f"{context}.site")
    if not isinstance(row["rank"], int) or isinstance(row["rank"], bool):
        raise ConversionReviewError(f"{context}.rank must be an integer")
    if not 1 <= row["rank"] <= 15:
        raise ConversionReviewError(f"{context}.rank must be in the top 15")
    question_id = row["question_id"]
    if question_id is not None:
        question_id = _required_text(question_id, f"{context}.question_id")
        if ID_RE.fullmatch(question_id) is None:
            raise ConversionReviewError(
                f"{context}.question_id must be a plain identifier"
            )
    outcome = _required_text(row["outcome"], f"{context}.outcome")
    if outcome not in OUTCOMES:
        raise ConversionReviewError(
            f"{context}.outcome must be one of {sorted(OUTCOMES)}"
        )
    if outcome == "contracted" and question_id is None:
        raise ConversionReviewError(
            f"{context}.question_id is required for a contracted site"
        )
    if outcome != "contracted" and question_id is not None:
        raise ConversionReviewError(
            f"{context}.question_id must be omitted for a skipped site"
        )
    if row["source"] != "stopwatch":
        raise ConversionReviewError(f"{context}.source must be 'stopwatch'")
    active = row["active_minutes"]
    if isinstance(active, bool) or not isinstance(active, (int, float)):
        raise ConversionReviewError(f"{context}.active_minutes must be numeric")
    if not math.isfinite(active) or active <= 0:
        raise ConversionReviewError(
            f"{context}.active_minutes must be finite and > 0"
        )
    recorded = _required_text(row["recorded_at"], f"{context}.recorded_at")
    try:
        datetime.fromisoformat(recorded.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ConversionReviewError(
            f"{context}.recorded_at must be an ISO timestamp"
        ) from exc
    return dict(row)


def load_rows(path: pathlib.Path | None = None) -> list[dict[str, Any]]:
    """Load and validate the append-only measurement log."""
    source = pathlib.Path(path) if path is not None else LOG_PATH
    if not source.is_file():
        return []
    rows: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_reviews: set[tuple[str, str, str]] = set()
    wave_dimensions: dict[tuple[str, str], tuple[str, str]] = {}
    wave_ranks: dict[tuple[str, str], set[int]] = {}
    for index, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            raw = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ConversionReviewError(
                f"{source}:{index}: invalid JSON: {exc.msg}"
            ) from exc
        row = _validate_row(raw, index)
        measurement_id = row["measurement_id"]
        review_key = (row["corpus"], row["wave_id"], row["site"])
        if measurement_id in seen_ids:
            raise ConversionReviewError(
                f"{source}:{index}: duplicate measurement_id {measurement_id}"
            )
        if review_key in seen_reviews:
            raise ConversionReviewError(
                f"{source}:{index}: duplicate completed review for "
                f"{review_key[0]}/{review_key[1]} {review_key[2]}"
            )
        wave_key = (row["corpus"], row["wave_id"])
        dimensions = (row["pin"], row["idiom_bucket"])
        prior_dimensions = wave_dimensions.setdefault(wave_key, dimensions)
        if prior_dimensions != dimensions:
            raise ConversionReviewError(
                f"{source}:{index}: wave {wave_key[0]}/{wave_key[1]} must use "
                "one source pin and one idiom bucket"
            )
        ranks = wave_ranks.setdefault(wave_key, set())
        if row["rank"] in ranks:
            raise ConversionReviewError(
                f"{source}:{index}: wave {wave_key[0]}/{wave_key[1]} has "
                f"duplicate rank {row['rank']}"
            )
        ranks.add(row["rank"])
        seen_ids.add(measurement_id)
        seen_reviews.add(review_key)
        rows.append(row)
    return rows


def append_row(
    *,
    corpus: str,
    pin: str,
    wave_id: str,
    idiom_bucket: str,
    site: str,
    rank: int,
    outcome: str,
    active_minutes: float,
    question_id: str | None = None,
    path: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Append one completed human review, refusing duplicate site/wave rows."""
    row = {
        "schema_version": "1",
        "measurement_id": str(uuid.uuid4()),
        "corpus": corpus,
        "pin": pin,
        "wave_id": wave_id,
        "idiom_bucket": idiom_bucket,
        "site": site,
        "rank": rank,
        "question_id": question_id,
        "outcome": outcome,
        "source": "stopwatch",
        "active_minutes": active_minutes,
        "recorded_at": _utc_now(),
    }
    row = _validate_row(row, 1)
    dest = pathlib.Path(path) if path is not None else LOG_PATH
    dest.parent.mkdir(parents=True, exist_ok=True)

    # Serialize duplicate-check + append on the same file descriptor so two
    # operators cannot record the same completed site concurrently.
    import fcntl

    with dest.open("a+", encoding="utf-8") as fh:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
        fh.seek(0)
        existing_text = fh.read()
        existing_ids: set[str] = set()
        existing_reviews: set[tuple[str, str, str]] = set()
        existing_wave_dimensions: dict[tuple[str, str], tuple[str, str]] = {}
        existing_wave_ranks: dict[tuple[str, str], set[int]] = {}
        for index, line in enumerate(existing_text.splitlines(), 1):
            if not line.strip():
                continue
            try:
                old = _validate_row(json.loads(line), index)
            except (json.JSONDecodeError, ConversionReviewError) as exc:
                raise ConversionReviewError(
                    f"cannot append to invalid {dest}:{index}: {exc}"
                ) from exc
            if old["measurement_id"] in existing_ids:
                raise ConversionReviewError(
                    f"{dest}:{index}: duplicate measurement_id "
                    f"{old['measurement_id']}"
                )
            existing_ids.add(old["measurement_id"])
            old_review_key = (old["corpus"], old["wave_id"], old["site"])
            if old_review_key in existing_reviews:
                raise ConversionReviewError(
                    f"{dest}:{index}: duplicate completed review for "
                    f"{old_review_key[0]}/{old_review_key[1]} {old_review_key[2]}"
                )
            existing_reviews.add(old_review_key)
            wave_key = (old["corpus"], old["wave_id"])
            dimensions = (old["pin"], old["idiom_bucket"])
            prior_dimensions = existing_wave_dimensions.setdefault(
                wave_key, dimensions
            )
            if prior_dimensions != dimensions:
                raise ConversionReviewError(
                    f"{dest}:{index}: wave {wave_key[0]}/{wave_key[1]} must use "
                    "one source pin and one idiom bucket"
                )
            ranks = existing_wave_ranks.setdefault(wave_key, set())
            if old["rank"] in ranks:
                raise ConversionReviewError(
                    f"{dest}:{index}: wave {wave_key[0]}/{wave_key[1]} has "
                    f"duplicate rank {old['rank']}"
                )
            ranks.add(old["rank"])
        review_key = (row["corpus"], row["wave_id"], row["site"])
        if review_key in existing_reviews:
            raise ConversionReviewError(
                f"review already recorded for {row['corpus']}/{row['wave_id']} "
                f"{row['site']}"
            )
        wave_key = (row["corpus"], row["wave_id"])
        dimensions = (row["pin"], row["idiom_bucket"])
        existing_dimensions = existing_wave_dimensions.get(wave_key)
        if existing_dimensions is not None and existing_dimensions != dimensions:
            raise ConversionReviewError(
                f"wave {row['corpus']}/{row['wave_id']} is already recorded with "
                "a different source pin or idiom bucket"
            )
        if row["rank"] in existing_wave_ranks.get(wave_key, set()):
            raise ConversionReviewError(
                f"rank {row['rank']} is already recorded for "
                f"{row['corpus']}/{row['wave_id']}"
            )
        if row["measurement_id"] in existing_ids:
            raise ConversionReviewError("measurement_id collision")
        fh.seek(0, 2)
        fh.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n")
        fh.flush()
        import os

        os.fsync(fh.fileno())
        fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
    return row


def _median_mean(values: list[float]) -> dict[str, float | None | int]:
    if not values:
        return {"median": None, "mean": None, "total": 0.0, "n": 0}
    return {
        "median": statistics.median(values),
        "mean": statistics.mean(values),
        "total": sum(values),
        "n": len(values),
    }


def summarize(path: pathlib.Path | None = None) -> dict[str, Any]:
    """Summarize review effort by corpus, wave, and idiom bucket."""
    grouped: dict[tuple[str, str, str, str], list[dict[str, Any]]] = {}
    for row in load_rows(path):
        key = (row["corpus"], row["pin"], row["wave_id"], row["idiom_bucket"])
        grouped.setdefault(key, []).append(row)
    waves = []
    for (corpus, pin, wave_id, bucket), rows in sorted(grouped.items()):
        times = [float(row["active_minutes"]) for row in rows]
        contracted = sum(row["outcome"] == "contracted" for row in rows)
        skipped = len(rows) - contracted
        outcome_counts = dict(sorted(Counter(row["outcome"] for row in rows).items()))
        stats = _median_mean(times)
        total_minutes = float(stats["total"] or 0.0)
        waves.append(
            {
                "corpus": corpus,
                "pin": pin,
                "wave_id": wave_id,
                "idiom_bucket": bucket,
                "reviewed_sites": len(rows),
                "contracted_sites": contracted,
                "skipped_sites": skipped,
                "outcome_counts": outcome_counts,
                "active_minutes": stats,
                "contracts_adopted_per_active_hour": (
                    contracted * 60.0 / total_minutes if total_minutes > 0 else None
                ),
            }
        )
    return {"schema_version": "1", "waves": waves}
