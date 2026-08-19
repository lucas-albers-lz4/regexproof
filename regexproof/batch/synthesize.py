"""Synthesize validator properties from compiled, replayable regex sites.

Public import surface for the synthesizer (#453). Phase internals live in
``synth_certify``, ``synth_queries``, and ``synth_emit``. This module
re-exports the stable API and remains the monkeypatch facade.

The compiler remains the source of truth for wrapper shape and mirror
exactness.  This module only inspects the already-lowered metadata and uses
the parser AST to certify the small shape-1 subset.
"""

from __future__ import annotations

from typing import Any

from regexproof.batch.synth_certify import (
    SKIP_BUCKETS,
    AlphabetCertification,
    _certified_contains,
    _certify_alphabet_union,
    _compile_view,
    _eligibility,
    _parse_for_certification,
    _question_payload,
    _selected_questions,
    selector_matches,
)
from regexproof.batch.synth_emit import SynthesisResult, _guard_row, _property_row
from regexproof.batch.synth_queries import (
    SynthesisError,
    _diff_fuzz_site,
    _require_nonvacuous,
    _shape2_query,
    _widened_guard,
)
from regexproof.groundtruth.adapters import (
    Replayability,
    ReplayVerdict,
    classify_replayability,
    replay,
    require_replayable,
    status_for_claim,
)

DEFAULT_SYNTH_MAX_SITES = 200
DEFAULT_SYNTH_LEN_BOUND = 16
DEFAULT_SYNTH_DIFF_FUZZ_SAMPLE = 5

__all__ = [
    "SKIP_BUCKETS",
    "AlphabetCertification",
    "SynthesisError",
    "SynthesisResult",
    "selector_matches",
    "synthesize_compiled",
]


def synthesize_compiled(
    corpus: str,
    compiled: list[tuple[dict[str, Any], Any, dict[str, Any] | None]],
    inventory: dict[str, Any],
    manifest: dict[str, Any] | None = None,
    *,
    diff_fuzz_sample: int | None = None,
) -> SynthesisResult:
    """Synthesize properties/guards from the compiled stream."""
    manifest = manifest or {}
    all_rows = sorted(
        (item[0] for item in compiled),
        key=lambda row: str(row.get("regex_id") or ""),
    )
    max_sites = int(manifest.get("synth_max_sites", DEFAULT_SYNTH_MAX_SITES))
    rows = all_rows[:max_sites]
    questions = list(inventory.get("questions") or [])
    selected, selector_outcomes = _selected_questions(rows, questions)
    bound = int(manifest.get("synth_len_bound", DEFAULT_SYNTH_LEN_BOUND))
    fuzz_sample = (
        int(diff_fuzz_sample)
        if diff_fuzz_sample is not None
        else int(manifest.get("synth_diff_fuzz_sample", DEFAULT_SYNTH_DIFF_FUZZ_SAMPLE))
    )
    stats: dict[str, Any] = {
        "synth_max_sites": max_sites,
        "synth_len_bound": bound,
        "synth_diff_fuzz_sample": fuzz_sample,
        "selector_outcomes": selector_outcomes,
        "skip_buckets": {bucket: 0 for bucket in SKIP_BUCKETS},
        "skip_reasons": {},
        "selected_sites": len(
            {str(r.get("regex_id")) for values in selected.values() for r in values}
        ),
        "selected_sites_after_cap": len(
            {str(r.get("regex_id")) for values in selected.values() for r in values}
        ),
        "encodable_sites": sum(1 for row, _mirror, _meta in compiled if row.get("encodable")),
    }
    stats["shape1_certification_count"] = 0
    for row, mirror, meta in compiled:
        if not row.get("encodable") or mirror is None:
            continue
        if _compile_view(row, mirror, meta).mirror_exact is not True:
            continue
        ast = _parse_for_certification(str(row.get("pattern") or ""))
        if ast is None:
            continue
        if _certify_alphabet_union(ast, mirror) is not None:
            stats["shape1_certification_count"] += 1

    item_by_id = {str(row.get("regex_id")): (row, mirror, meta) for row, mirror, meta in compiled}
    property_rows: list[dict[str, Any]] = []
    guard_inputs: dict[
        tuple[str, str],
        tuple[dict[str, Any], Any, int, AlphabetCertification | None, str],
    ] = {}
    executed_questions: set[str] = set()
    counted_skips: set[tuple[str, str]] = set()
    premeasure_sites: set[str] = set()
    premeasure_certified: set[str] = set()

    for question in questions:
        if not _question_payload(question):
            continue
        qid = str(question["id"])
        for row in selected.get(qid, []):
            regex_id = str(row.get("regex_id") or "")
            mirror_meta = item_by_id.get(regex_id)
            if mirror_meta is None:
                continue
            _row, mirror, meta = mirror_meta
            replayability = classify_replayability(
                str(row.get("dialect") or ""), str(row.get("call_kind") or "")
            )
            if replayability is Replayability.SKIPPED_NO_GT_ADAPTER:
                bucket = "synth_skipped_no_gt_adapter"
                if (regex_id, bucket) not in counted_skips:
                    stats["skip_buckets"][bucket] += 1
                    counted_skips.add((regex_id, bucket))
                continue
            if replayability is Replayability.SKIPPED_SUBSTITUTION:
                bucket = "synth_skipped_substitution_call_kind"
                if (regex_id, bucket) not in counted_skips:
                    stats["skip_buckets"][bucket] += 1
                    counted_skips.add((regex_id, bucket))
                continue
            if not row.get("encodable") or mirror is None or meta is None:
                continue
            cr = _compile_view(row, mirror, meta)
            skip = _eligibility(cr)
            if skip is not None:
                if skip == "synth_skipped_unanchored_search":
                    if (regex_id, skip) not in counted_skips:
                        stats["skip_reasons"][skip] = int(stats["skip_reasons"].get(skip, 0)) + 1
                        stats["skip_buckets"][skip] += 1
                        counted_skips.add((regex_id, skip))
                else:
                    stats["skip_reasons"][skip] = int(stats["skip_reasons"].get(skip, 0)) + 1
                continue
            premeasure_sites.add(regex_id)
            if cr.mirror_exact is not True:
                bucket = "synth_skipped_approximate_mirror"
                if (regex_id, bucket) not in counted_skips:
                    stats["skip_buckets"][bucket] += 1
                    counted_skips.add((regex_id, bucket))
                continue
            ast = _parse_for_certification(str(row.get("pattern") or ""))
            certification = _certify_alphabet_union(ast, mirror) if ast is not None else None
            if certification is not None:
                premeasure_certified.add(regex_id)
                effective_shape = 1
            else:
                effective_shape = 2
            if question.get("shape") == 2:
                effective_shape = 2
            for bad_char in question.get("bad_chars") or []:
                if not isinstance(bad_char, str) or len(bad_char) != 1:
                    raise SynthesisError(f"{qid}: bad_chars must contain one-character strings")
                domain_note = "all-lengths" if effective_shape == 1 else f"len<={bound}"
                if effective_shape == 1:
                    assert certification is not None
                    result = (
                        "sat"
                        if _certified_contains(certification, bad_char)
                        else "unsat"
                    )
                    witness = bad_char if result == "sat" else None
                else:
                    result, witness = _shape2_query(mirror, bad_char, bound, want_model=True)
                gt_status = None
                if result == "sat":
                    assert witness is not None
                    gt_result = replay(
                        str(row.get("pattern") or ""),
                        str(row.get("flags") or ""),
                        str(row.get("dialect") or ""),
                        str(row.get("call_kind") or ""),
                        witness,
                    )
                    require_replayable(gt_result)
                    gt_status = status_for_claim(gt_result, True)
                    if gt_status != "reproduced":
                        if gt_result.verdict is ReplayVerdict.REJECTED:
                            # SEMANTIC disagreement: the real engine rejects
                            # the witness the mirror claims to accept — the
                            # certification/query is wrong. Never skip this
                            # class; it is a soundness violation.
                            raise SynthesisError(
                                f"SAT witness failed replay for {regex_id}/{qid}/{bad_char!r}: "
                                f"{gt_result.verdict.value}"
                            )
                        # INFRA limitation (engine-error/timeout/no-adapter):
                        # the witness cannot be transported or evaluated (e.g.
                        # a NUL byte breaks the P1 NUL-framed batch protocol).
                        # The SAT claim is unverifiable — drop the row
                        # fail-closed and count it; do not crash the run.
                        bucket = "synth_skipped_witness_replay"
                        if (regex_id, bucket) not in counted_skips:
                            stats["skip_buckets"][bucket] += 1
                            counted_skips.add((regex_id, bucket))
                        continue
                property_rows.append(
                    _property_row(
                        corpus=corpus,
                        row=row,
                        question=question,
                        bad_char=bad_char,
                        shape=effective_shape,
                        result=result,
                        witness=witness,
                        domain_note=domain_note,
                        ground_truth_status=gt_status,
                    )
                )
                key = (f"synth:{corpus}:{regex_id}", bad_char)
                guard_inputs.setdefault(
                    key, (row, mirror, effective_shape, certification, qid)
                )
            executed_questions.add(qid)

    guard_rows: list[dict[str, Any]] = []
    for (_family, bad_char), (row, mirror, shape, certification, qid) in sorted(
        guard_inputs.items(), key=lambda item: (item[0][0], item[0][1])
    ):
        _require_nonvacuous(
            mirror,
            shape=shape,
            certification=certification,
            bound=bound,
        )
        result, witness = _widened_guard(
            mirror,
            bad_char,
            shape=shape,
            certification=certification,
            bound=bound,
        )
        if result != "sat":
            raise SynthesisError(f"mutation guard is {result}, expected sat")
        guard_rows.append(
            _guard_row(
                corpus=corpus,
                row=row,
                question_id=qid,
                bad_char=bad_char,
                shape=shape,
                witness=witness,
            )
        )

    synth_findings = sorted(
        property_rows + guard_rows,
        key=lambda finding: (
            str(finding.get("regex_id") or ""),
            str(finding.get("question_id") or ""),
            str(finding.get("bad_char") or ""),
            str(finding.get("kind") or ""),
        ),
    )
    stats["synthesized_property_rows"] = len(property_rows)
    stats["mutation_guard_rows"] = len(guard_rows)
    stats["pre_measure"] = {
        "selected_sites": stats["selected_sites"],
        "selected_fullmatch_shaped_encodable_replay_supported": len(premeasure_sites),
        "shape1_certification_count_over_all_encodable_sites": stats["shape1_certification_count"],
        "shape1_certification_count_selected": len(premeasure_certified),
        "encodable_sites": stats["encodable_sites"],
    }

    fuzz_sites: list[
        tuple[dict[str, Any], Any, list[str], int, AlphabetCertification | None]
    ] = []
    seen_sites: set[str] = set()
    for finding in property_rows:
        if finding.get("shape") not in (1, 2):
            continue
        regex_id = str(finding["regex_id"])
        if regex_id in seen_sites:
            continue
        source = item_by_id.get(regex_id)
        if source is None:
            continue
        source_row, source_mirror, _source_meta = source
        dangerous = [
            str(other.get("bad_char"))
            for other in property_rows
            if other.get("regex_id") == regex_id
        ]
        guard_info = next(
            (
                value
                for (family, bad), value in guard_inputs.items()
                if family == f"synth:{corpus}:{regex_id}"
            ),
            None,
        )
        if guard_info is None:
            continue
        _guard_row_source, _guard_mirror, guard_shape, guard_cert, _guard_qid = guard_info
        fuzz_sites.append((source_row, source_mirror, dangerous, guard_shape, guard_cert))
        seen_sites.add(regex_id)
    shape1_sites = [item for item in fuzz_sites if item[3] == 1]
    shape2_sites = [item for item in fuzz_sites if item[3] != 1]
    # Shape-1 sites are all checked. Shape-2 sites are deterministic samples.
    selected_fuzz_sites = shape1_sites + sorted(
        shape2_sites, key=lambda item: str(item[0].get("regex_id"))
    )[:fuzz_sample]
    fuzz_witnesses = 0
    for source_row, source_mirror, dangerous, shape, certification in selected_fuzz_sites:
        fuzz_witnesses += _diff_fuzz_site(
            source_row,
            source_mirror,
            dangerous,
            fuzz_sample,
            shape=shape,
            certification=certification,
        )
    stats["diff_fuzz_sites"] = len(selected_fuzz_sites)
    stats["diff_fuzz_witnesses"] = fuzz_witnesses
    stats["diff_fuzz_disagreements"] = 0
    return SynthesisResult(synth_findings, stats, executed_questions)
