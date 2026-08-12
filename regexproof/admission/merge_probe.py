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
    """Return a copy of *draft* with SHELL evidence merged from *records*.

    Only ``posix-shell`` records are aggregated (the merge is the shell-
    evidence bridge; the scaffold's walk already counted the non-shell
    surface — mixing py/js records from a full export would double-count
    and corrupt the dialect totals, luna #275 finding).
    """
    shell = [r for r in records if r.get("dialect") == "posix-shell"]
    # Shell-aware-scaffold guard (luna #276 -r3 finding #2): post-P2 the
    # walk HAS shell dispatch, so a scaffold that already counted posix-shell
    # would be DOUBLE-counted by this merge (the tool is the PRE-P2
    # shell-evidence bridge per the plan). Fail closed on the ambiguity.
    scaffold_shell = (draft.get("probe") or {}).get("dialect") or {}
    if scaffold_shell.get("posix-shell"):
        raise ValueError(
            "merge_draft: the scaffold's walk already counted posix-shell "
            f"({scaffold_shell['posix-shell']} sites) — this merge is the "
            "PRE-P2 shell-evidence bridge; re-run probe-corpus-admission.py "
            "pre-P2 or fold the evidence directly"
        )
    patterns = [r.get("pattern") or "" for r in shell]
    flags: Counter[str] = Counter()
    for r in shell:
        for ch in r.get("flags") or "":
            flags[ch] += 1
    merged = Counter(accumulate_constructs(patterns))
    for ch, n in flags.items():
        key = _FLAG_LETTER_TO_CONSTRUCT.get(ch)
        if key:
            merged[key] += n
    out = json.loads(json.dumps(draft))  # deep copy
    # ADD to the scaffold walk's evidence (the walk is shell-blind pre-P2;
    # replacing drops the non-shell surface — cumulative review finding #5,
    # luna #276 finding #4): sites, per-file counts, dialect, and buckets
    # are all additive; the shell records extend the walk's evidence.
    out["probe"]["regex_sites"] = (out["probe"].get("regex_sites") or 0) + len(shell)
    per_file = Counter(out["probe"].get("regex_sites_per_file") or {})
    for r in shell:
        per_file[r.get("file") or ""] += 1
    out["probe"]["regex_sites_per_file"] = dict(sorted(per_file.items()))
    # dialect: the scaffold's walk saw no shell pre-P2 — aggregate the
    # SHELL record dialects on top of whatever the scaffold counted.
    dialect = Counter(out["probe"].get("dialect") or {})
    for r in shell:
        dialect[r.get("dialect") or "unknown"] += 1
    out["probe"]["dialect"] = dict(dialect)
    # flags + construct_counts: canonical probe fields must carry the shell
    # evidence (cumulative Reviewer B finding #6 — the decision's narrative
    # said `-i 39` but probe.flags was empty because the merge never
    # populated it; _probe_subset preserves what the draft carries).
    walk_flags = Counter(out["probe"].get("flags") or {})
    for r in shell:
        for ch in r.get("flags") or "":
            walk_flags[ch] += 1
    out["probe"]["flags"] = dict(walk_flags)
    walk_constructs = Counter(out["probe"].get("construct_counts") or {})
    out["probe"]["construct_counts"] = dict(walk_constructs + merged)
    walk_buckets = Counter(out["probe"].get("predicted_buckets") or {})
    out["probe"]["predicted_buckets"] = dict(walk_buckets + Counter(predict_buckets(dict(merged))))
    out["probe"]["_shell_evidence"] = {
        "records": len(shell),
        "construct_counts": dict(merged),
    }
    return out
