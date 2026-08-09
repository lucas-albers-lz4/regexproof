"""Corpus admission probe foundations (mine-and-approve P1)."""

from __future__ import annotations

from regexproof.admission.boundary import classify_boundary
from regexproof.admission.dialect_aliases import normalize_dialect_counts
from regexproof.admission.serialize import dumps_pinned
from regexproof.admission.vocabulary import load_vocabulary, predict_buckets

__all__ = [
    "classify_boundary",
    "dumps_pinned",
    "load_vocabulary",
    "normalize_dialect_counts",
    "predict_buckets",
]
