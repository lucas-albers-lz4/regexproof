"""CI validation for score-v2's documented refit cadence."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from regexproof.mine.exclusions import normalize_repo_url


def _rows_by_url(rows: Sequence[Mapping[str, Any]]) -> dict[str, Mapping[str, Any]]:
    by_url: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        url = normalize_repo_url(str(row.get("url") or ""))
        if not url:
            raise ValueError("score-v2 label row has no repository URL")
        if url in by_url:
            raise ValueError(f"duplicate score-v2 label row for {url}")
        by_url[url] = row
    return by_url


def check_score_v2_artifact_cadence(
    *,
    source_rows: Sequence[Mapping[str, Any]],
    current_rows: Sequence[Mapping[str, Any]],
    current_weights: Mapping[str, Any],
    expected_source_weights: Mapping[str, Any],
) -> tuple[bool, str]:
    """Check the committed fit against its recorded label snapshot.

    A fit stays pinned only when all source rows are unchanged, current data
    is append-only, and new linked decisions remain below the 20% refit cadence.
    """
    if not source_rows:
        return False, "recorded fit-source gate-label snapshot is empty"
    try:
        source_by_url = _rows_by_url(source_rows)
        current_by_url = _rows_by_url(current_rows)
    except ValueError as exc:
        return False, str(exc)
    if len(source_by_url) != len(source_rows):
        return False, "fit-source gate-label rows are not unique by repository URL"
    if len(current_by_url) != len(current_rows):
        return False, "current gate-label rows are not unique by repository URL"
    if dict(current_weights) != dict(expected_source_weights):
        return False, "score-v2 weights do not reproduce from their recorded fit source"

    for url, source_row in source_by_url.items():
        if current_by_url.get(url) != source_row:
            return False, f"fit-source label row changed or disappeared: {url}"
    additions = len(current_by_url) - len(source_by_url)
    if additions < 0:
        return False, "current gate-label snapshot removed fit-source rows"
    if additions * 5 >= len(source_by_url):
        return (
            False,
            f"{additions}/{len(source_by_url)} appended rows reached the 20% refit threshold",
        )
    return (
        True,
        f"retained exact fit snapshot; {additions}/{len(source_by_url)} appended rows is below 20%",
    )
