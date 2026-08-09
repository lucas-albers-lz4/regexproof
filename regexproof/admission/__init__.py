"""Corpus admission probe + authoring (mine-and-approve P1/P3)."""

from __future__ import annotations

from regexproof.admission.author import author_auto, author_human, emit_decision_text
from regexproof.admission.auto_nogo import auto_nogo_eligible
from regexproof.admission.boundary import classify_boundary
from regexproof.admission.constructs import accumulate_constructs, count_constructs
from regexproof.admission.dialect_aliases import normalize_dialect_counts
from regexproof.admission.draft import FIELDS_REMAINING, build_draft, emit_draft_text
from regexproof.admission.serialize import dumps_pinned
from regexproof.admission.vocabulary import load_vocabulary, predict_buckets
from regexproof.admission.walk import walk_repo

__all__ = [
    "FIELDS_REMAINING",
    "accumulate_constructs",
    "author_auto",
    "author_human",
    "auto_nogo_eligible",
    "build_draft",
    "classify_boundary",
    "count_constructs",
    "dumps_pinned",
    "emit_decision_text",
    "emit_draft_text",
    "load_vocabulary",
    "normalize_dialect_counts",
    "predict_buckets",
    "walk_repo",
]
