from __future__ import annotations

from regexproof.mine.score_v2_gate import check_score_v2_artifact_cadence


def _rows(count: int) -> list[dict[str, object]]:
    return [
        {"url": f"https://github.com/acme/repo-{index}", "label": "no-go"}
        for index in range(count)
    ]


def _check(
    *,
    source_rows: list[dict[str, object]],
    current_rows: list[dict[str, object]],
    current_weights: dict[str, object],
    expected_source: dict[str, object] | None = None,
) -> tuple[bool, str]:
    return check_score_v2_artifact_cadence(
        source_rows=source_rows,
        current_rows=current_rows,
        current_weights=current_weights,
        expected_source_weights=expected_source or {"fit": "source"},
    )


def test_small_append_keeps_exact_fit_snapshot_pinned() -> None:
    source = _rows(10)
    current = [*source, {"url": "https://github.com/acme/new", "label": "triage-trial"}]
    passed, detail = _check(
        source_rows=source,
        current_rows=current,
        current_weights={"fit": "source"},
    )
    assert passed
    assert "below 20%" in detail


def test_changed_existing_row_requires_current_refit() -> None:
    source = _rows(10)
    current = [*source]
    current[0] = {**current[0], "label": "go"}
    passed, detail = _check(
        source_rows=source,
        current_rows=current,
        current_weights={"fit": "source"},
    )
    assert not passed
    assert "changed or disappeared" in detail


def test_twenty_percent_append_requires_current_refit() -> None:
    source = _rows(10)
    current = [
        *source,
        {"url": "https://github.com/acme/new-1", "label": "no-go"},
        {"url": "https://github.com/acme/new-2", "label": "no-go"},
    ]
    passed, detail = _check(
        source_rows=source,
        current_rows=current,
        current_weights={"fit": "source"},
    )
    assert not passed
    assert "20% refit threshold" in detail


def test_refit_source_snapshot_allows_existing_row_change() -> None:
    source = _rows(10)
    current = [*source]
    current[0] = {**current[0], "label": "go"}
    passed, detail = _check(
        source_rows=current,
        current_rows=current,
        current_weights={"fit": "source"},
    )
    assert passed
    assert "0/10 appended rows" in detail


def test_weights_must_reproduce_from_recorded_source_labels() -> None:
    source = _rows(10)
    passed, detail = _check(
        source_rows=source,
        current_rows=source,
        current_weights={"fit": "stale"},
        expected_source={"fit": "source"},
    )
    assert not passed
    assert "do not reproduce from their recorded fit source" in detail


def test_duplicate_current_rows_fail_even_with_exact_current_fit() -> None:
    source = _rows(10)
    current = [*source, source[0]]
    passed, detail = _check(
        source_rows=source,
        current_rows=current,
        current_weights={"fit": "source"},
    )
    assert not passed
    assert "duplicate score-v2 label row" in detail
