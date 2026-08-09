"""Prediction vocabulary loader (umbrella C5 / P1 task 0)."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_VOCAB_PATH = REPO_ROOT / "properties" / "generated" / "prediction_vocabulary.json"


@lru_cache(maxsize=4)
def load_vocabulary(path: str | None = None) -> dict[str, Any]:
    """Load the committed prediction-vocabulary artifact."""
    p = Path(path) if path else DEFAULT_VOCAB_PATH
    data = json.loads(p.read_text(encoding="utf-8"))
    if "construct_to_bucket" not in data:
        raise ValueError(f"prediction vocabulary missing construct_to_bucket: {p}")
    return data


def predict_buckets(
    construct_counts: dict[str, int],
    *,
    vocabulary: dict[str, Any] | None = None,
) -> dict[str, int]:
    """Map construct counts → predicted reject-bucket counts via the vocabulary.

    Unknown constructs are skipped (no silent invent of bucket names).
    """
    vocab = vocabulary if vocabulary is not None else load_vocabulary()
    mapping: dict[str, str] = vocab["construct_to_bucket"]
    out: dict[str, int] = {}
    for construct, n in construct_counts.items():
        bucket = mapping.get(construct)
        if bucket is None:
            continue
        out[bucket] = out.get(bucket, 0) + int(n)
    return out
