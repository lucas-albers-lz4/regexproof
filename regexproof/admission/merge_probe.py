"""Merge a P1 ``--dir --ndjson`` shell record export into a probe draft (P3-A).

The ``probe-corpus-admission.py`` draft's ``walk_repo`` path sees NO shell
files pre-P2 (no shell dispatch in ``_extractors_for``).  This module
populates the draft's ``probe.regex_sites`` (aggregated from the FULL
records) and ``probe.predicted_buckets`` (constructs derived from the record
pattern text), so the authored artifact's shell novelty evidence is real.

The construct-counting step is DEFINED to match walk.py EXACTLY
(walk.py:186-199): ``accumulate_constructs(patterns)`` on the record pattern
texts, then FOLD the record ``flags`` through ``_FLAG_LETTER_TO_CONSTRUCT``
(``i``→``(?i)`` …) into a merged Counter, and only THEN feed it through
``predict_buckets`` — so shell ``grep -i`` records land in the
``(?i)``/inline-flag bucket, not silently dropped.

**Preflight enforcement:** callers must refuse to emit a draft with EMPTY
``probe.predicted_buckets`` — the AC4 "under-report forces
triage-trial/no-go" rule (the CLI exits 2).
"""

from __future__ import annotations

import json
from collections import Counter
from typing import Any

from regexproof.admission.constructs import accumulate_constructs
from regexproof.admission.vocabulary import predict_buckets
from regexproof.admission.walk import _FLAG_LETTER_TO_CONSTRUCT


def merge_draft(draft: dict[str, Any], records: list[dict[str, Any]]) -> dict[str, Any]:
    """Return a copy of *draft* with shell evidence merged from *records*."""
    patterns = [r.get("pattern") or "" for r in records]
    flags: Counter[str] = Counter()
    for r in records:
        for ch in r.get("flags") or "":
            flags[ch] += 1
    merged = Counter(accumulate_constructs(patterns))
    for ch, n in flags.items():
        key = _FLAG_LETTER_TO_CONSTRUCT.get(ch)
        if key:
            merged[key] += n
    out = json.loads(json.dumps(draft))  # deep copy
    out["probe"]["regex_sites"] = len(records)
    out["probe"]["regex_sites_per_file"] = dict(sorted(
        Counter(r.get("file") or "" for r in records).items()))
    out["probe"]["predicted_buckets"] = predict_buckets(dict(merged))
    out["probe"]["_shell_evidence"] = {
        "records": len(records),
        "construct_counts": dict(merged),
    }
    return out
