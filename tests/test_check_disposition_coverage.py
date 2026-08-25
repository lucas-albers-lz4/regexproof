"""#554 Phase A: fail-closed disposition-coverage join (GT SAT ↔ curated)."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


chk = _load("_rp_check_disposition_coverage", "scripts/check-disposition-coverage.py")
cl = _load("_rp_cl_for_coverage", "scripts/conversion-ledger.py")


def _gt_row(**overrides):
    row = {
        "schema_version": "1",
        "kind": "property",
        "result": "sat",
        "regex_id": "a" * 32,
        "corpus": "demo",
        "site": "net/demo/files/etc/init.d/demo:42:is_host",
        "question_id": "no-semicolon-in-hostname",
        "ground_truth_status": "reproduced",
        "synthesized": False,
        "wave_id": "demo_w1",
        "idiom_bucket": "validator-charsets",
    }
    row.update(overrides)
    return row


def _curated(**overrides):
    row = {
        "id": "CU-901",
        "corpus": "demo",
        "status": "filed_plan",
        "kind": "property",
        "language_membership": True,
        "site": "net/demo/files/etc/init.d/demo:42:is_host",
        "question_id": "no-semicolon-in-hostname",
        "wave_id": "demo_w1",
        "idiom_bucket": "validator-charsets",
        "filed_at": "2026-08-20",
    }
    row.update(overrides)
    return row


def _write_upstream(path: Path, *rows, crs_row: bool = True) -> Path:
    """Write a curated JSONL; by default carries the single CRS 942220 row
    ``run()`` requires (guard: exactly one curated disposition per rule)."""
    if crs_row:
        rows = (
            *rows,
            {
                "id": "CU-005",
                "corpus": "coreruleset",
                "status": "false_positive",
                "kind": "version_diff",
                "language_membership": True,
                "rule": "942220",
            },
        )
    path.write_text(
        "".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8"
    )
    return path


def _gen_dir(tmp_path: Path, *rows) -> Path:
    gen = tmp_path / "generated"
    gen.mkdir(exist_ok=True)
    (gen / "demo_conversion.ndjson").write_text(
        "".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8"
    )
    return gen


def test_gt_sat_without_curated_row_fails(tmp_path: Path, capsys):
    """Red state: a GT SAT with no curated row must exit 1 and name the key."""
    gen = _gen_dir(tmp_path, _gt_row())
    up = _write_upstream(tmp_path / "conversion-upstream.jsonl")
    rc = chk.run(gen_dir=gen, upstream_path=up)
    assert rc == 1
    err = capsys.readouterr().err
    assert "missing curated disposition rows" in err
    assert "no-semicolon-in-hostname" in err


def test_full_coverage_passes(tmp_path: Path):
    gen = _gen_dir(tmp_path, _gt_row())
    up = _write_upstream(tmp_path / "conversion-upstream.jsonl", _curated())
    assert chk.run(gen_dir=gen, upstream_path=up) == 0


def test_ready_to_file_lists_non_wont_file(tmp_path: Path, capsys):
    gen = _gen_dir(
        tmp_path,
        _gt_row(),
        _gt_row(
            site="net/demo/other:1:x",
            question_id="other-q",
        ),
    )
    up = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        _curated(),
        _curated(
            id="CU-902",
            site="net/demo/other:1:x",
            question_id="other-q",
            status="wont_file",
        ),
    )
    assert chk.run(gen_dir=gen, upstream_path=up, ready_to_file=True) == 0
    out = capsys.readouterr().out
    assert "ready-to-file: 1" in out
    assert "CU-901" in out
    assert "CU-902" not in out


def test_url_case_joins_but_repo_paths_stay_case_sensitive(
    tmp_path: Path, capsys
):
    """Canonicalization contract: URL scheme+host case-insensitive; repo
    paths compare verbatim."""
    assert cl.canonical_site(" HTTPS://GitHub.COM/x/y.js:1:0 ") == (
        "https://github.com/x/y.js:1:0"
    )
    assert cl.canonical_site("Net/pbr:1:x") == "Net/pbr:1:x"

    gen = _gen_dir(
        tmp_path, _gt_row(site="https://GitHub.COM/x/y.js:1:0")
    )
    up = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        _curated(site="https://github.com/x/y.js:1:0"),
    )
    assert chk.run(gen_dir=gen, upstream_path=up) == 0
    capsys.readouterr()

    gen2 = _gen_dir(tmp_path, _gt_row(site="Net/pbr:1:x"))
    up2 = _write_upstream(
        tmp_path / "conversion-upstream2.jsonl",
        _curated(site="net/pbr:1:x"),
    )
    assert chk.run(gen_dir=gen2, upstream_path=up2) == 1
    assert "Net/pbr:1:x" in capsys.readouterr().err


def test_question_id_falls_back_to_name(tmp_path: Path):
    rec = _gt_row()
    del rec["question_id"]
    rec["name"] = "named-question"
    gen = _gen_dir(tmp_path, rec)
    up = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        _curated(question_id="named-question"),
    )
    assert chk.run(gen_dir=gen, upstream_path=up) == 0


def test_mutation_guard_and_synthesized_are_not_gt_sats(tmp_path: Path):
    rows = [
        _gt_row(kind="mutation_guard", ground_truth_status="mutation-guard-sat-expected"),
        _gt_row(synthesized=True),
        _gt_row(result="timeout", ground_truth_status=None),
    ]
    gen = _gen_dir(tmp_path, *rows)
    up = _write_upstream(tmp_path / "conversion-upstream.jsonl")
    assert chk.run(gen_dir=gen, upstream_path=up) == 0


def test_unknown_disposition_rejected(tmp_path: Path):
    gen = _gen_dir(tmp_path, _gt_row())
    up = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        _curated(status="closed-wontfix"),
    )
    with pytest.raises(SystemExit, match="unknown disposition"):
        chk.run(gen_dir=gen, upstream_path=up)


def test_filed_plan_is_a_valid_disposition(tmp_path: Path):
    gen = _gen_dir(tmp_path, _gt_row())
    up = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        _curated(status="filed_plan"),
    )
    assert chk.run(gen_dir=gen, upstream_path=up) == 0


def test_backfilled_row_requires_reason_code_and_date(tmp_path: Path):
    gen = tmp_path / "generated"
    gen.mkdir(exist_ok=True)
    up = tmp_path / "conversion-upstream.jsonl"
    bad = _curated(backfilled=True)
    _write_upstream(up, bad)
    with pytest.raises(SystemExit, match="reason_code"):
        chk.load_curated_index(up, cl)

    bad2 = _curated(backfilled=True, reason_code="historical_close_out")
    _write_upstream(up, bad2)
    with pytest.raises(SystemExit, match="disposition_date"):
        chk.load_curated_index(up, cl)

    ok = _curated(
        backfilled=True,
        reason_code="historical_close_out",
        disposition_date=chk.DATE_UNKNOWN,
    )
    _write_upstream(up, ok)
    idx = chk.load_curated_index(up, cl)
    assert len(idx) == 1


def test_crs942220_guard_flags_conflicting_prose(tmp_path: Path):
    up = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        {
            "id": "CU-005",
            "corpus": "coreruleset",
            "status": "false_positive",
            "rule": "942220",
            "language_membership": True,
        },
        crs_row=False,
    )
    good = tmp_path / "good.md"
    good.write_text(
        "CRS 942220 is `false_positive` per conversion-upstream.jsonl\n",
        encoding="utf-8",
    )
    assert chk.crs942220_guard(up, (good,)) == []

    conflict = tmp_path / "conflict.md"
    conflict.write_text(
        "Rule 942220 disposition: `wont_file`.\n",
        encoding="utf-8",
    )
    problems = chk.crs942220_guard(up, (conflict,))
    assert any("`wont_file`" in p for p in problems)


def test_crs942220_guard_requires_exactly_one_curated_row(tmp_path: Path):
    up = _write_upstream(
        tmp_path / "conversion-upstream.jsonl", crs_row=False
    )
    problems = chk.crs942220_guard(up, ())
    assert len(problems) == 1
    assert "found 0" in problems[0]


def test_crs942220_guard_rejects_wrong_curated_status(tmp_path: Path):
    # A single 942220 row that is NOT CU-005 false_positive must fail — the
    # guard exists to pin this rule's disposition, not merely to count rows.
    up = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        {
            "id": "CU-005",
            "corpus": "coreruleset",
            "status": "wont_file",
            "rule": "942220",
            "language_membership": True,
        },
        crs_row=False,
    )
    problems = chk.crs942220_guard(up, ())
    assert any("not 'false_positive'" in p for p in problems)


def test_crs942220_guard_accepts_sibling_tokens_with_correct_status(
    tmp_path: Path,
):
    # A line that states the correct status alongside other dispositions
    # (different rows in the same table cell) is consistent.
    up = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        {
            "id": "CU-005",
            "corpus": "coreruleset",
            "status": "false_positive",
            "rule": "942220",
            "language_membership": True,
        },
        crs_row=False,
    )
    good = tmp_path / "good.md"
    good.write_text(
        "existence proofs: 1 (usrmanage P3 own-code `fixed_upstream`; "
        "CRS 942220 is `false_positive` per conversion-upstream.jsonl)\n",
        encoding="utf-8",
    )
    assert chk.crs942220_guard(up, (good,)) == []


def test_crs942220_guard_requires_status_or_cite_on_every_line(
    tmp_path: Path,
):
    # Per-line contract: a 942220 mention with neither the curated status nor
    # an on-line citation fails even when another line in the doc cites.
    up = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        {
            "id": "CU-005",
            "corpus": "coreruleset",
            "status": "false_positive",
            "rule": "942220",
            "language_membership": True,
        },
        crs_row=False,
    )
    doc = tmp_path / "mixed.md"
    doc.write_text(
        "CRS 942220 is `false_positive` per conversion-upstream.jsonl\n"
        "A bare CRS 942220 mention with no status and no citation\n",
        encoding="utf-8",
    )
    problems = chk.crs942220_guard(up, (doc,))
    assert any("without stating" in p for p in problems)


def test_crs942220_guard_rejects_cited_conflicting_status(tmp_path: Path):
    # A line that cites the curated file AND claims a conflicting status is a
    # contradiction — the citation must not exempt it from conflict detection.
    up = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        {
            "id": "CU-005",
            "corpus": "coreruleset",
            "status": "false_positive",
            "rule": "942220",
            "language_membership": True,
        },
        crs_row=False,
    )
    doc = tmp_path / "contradicts.md"
    doc.write_text(
        "CRS 942220 is `wont_file` per conversion-upstream.jsonl\n",
        encoding="utf-8",
    )
    problems = chk.crs942220_guard(up, (doc,))
    assert any("claims `wont_file`" in p for p in problems)


def test_backfilled_row_rejects_non_iso_disposition_date(tmp_path: Path):
    gen = _gen_dir(
        tmp_path,
        _gt_row(ground_truth_status="ground_truth_reproduced"),
    )
    curated = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        {
            "id": "CU-200",
            "corpus": "demo",
            "status": "wont_file",
            "site": "demo/site.py:10",
            "question_id": "demo-1",
            "backfilled": True,
            "reason_code": "pattern_class_regression_gate",
            "disposition_date": "yesterday",
        },
    )
    with pytest.raises(SystemExit, match="not an ISO date"):
        chk.run(gen_dir=gen, upstream_path=curated)


def test_backfilled_row_accepts_iso_and_unknown_date(tmp_path: Path):
    for disp_date in ("2026-08-20", "unknown_date"):
        gen = _gen_dir(
            tmp_path,
            _gt_row(ground_truth_status="ground_truth_reproduced"),
        )
        curated = _write_upstream(
            tmp_path / "conversion-upstream.jsonl",
            {
                "id": "CU-201",
                "corpus": "demo",
                "status": "wont_file",
                "site": "demo/site.py:10",
                "question_id": "demo-1",
                "backfilled": True,
                "reason_code": "pattern_class_regression_gate",
                "disposition_date": disp_date,
            },
        )
        assert chk.run(gen, curated) == 0


def test_non_backfilled_filing_row_requires_date(tmp_path: Path):
    gen = _gen_dir(
        tmp_path,
        _gt_row(ground_truth_status="ground_truth_reproduced"),
    )
    # Non-backfilled filing-status row without filed_at/resolved_at fails.
    curated = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        {
            "id": "CU-300",
            "corpus": "demo",
            "status": "filed",
            "site": "demo/site.py:10",
            "question_id": "demo-1",
        },
    )
    with pytest.raises(SystemExit, match="missing filed_at and resolved_at"):
        chk.run(gen, curated)
    # Invalid date also fails.
    curated2 = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        {
            "id": "CU-301",
            "corpus": "demo",
            "status": "filed",
            "site": "demo/site.py:10",
            "question_id": "demo-1",
            "filed_at": "not-a-date",
        },
    )
    with pytest.raises(SystemExit, match="not an ISO date"):
        chk.run(gen, curated2)
    # Valid date passes.
    curated3 = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        {
            "id": "CU-302",
            "corpus": "demo",
            "status": "filed",
            "site": "demo/site.py:10",
            "question_id": "demo-1",
            "filed_at": "2026-08-20",
        },
    )
    assert chk.run(gen, curated3) == 0


def test_crs942220_guard_requires_reconciliation_present(tmp_path: Path):
    # Fail-closed: if no guarded doc mentions 942220 at all, the guard must
    # fail (reconciliation prose removed entirely).
    up = _write_upstream(
        tmp_path / "conversion-upstream.jsonl",
        {
            "id": "CU-005",
            "corpus": "coreruleset",
            "status": "false_positive",
            "rule": "942220",
            "language_membership": True,
        },
        crs_row=False,
    )
    doc = tmp_path / "nodoc.md"
    doc.write_text("No mention of the rule anywhere.\n", encoding="utf-8")
    problems = chk.crs942220_guard(up, (doc,))
    assert any("no guarded doc mentions 942220" in p for p in problems)
