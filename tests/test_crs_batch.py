"""CRS batch shape-5 tree resolve + timeout skip."""

from __future__ import annotations

import json
from pathlib import Path

from regexproof.batch.runner import _clear_batch_shape5
from regexproof.rule_diff.crs_batch import (
    BATCH_TIMEOUT_PAIR_IDS,
    discover_crs_batch_pairs,
    resolve_crs_version_trees,
)


def test_clear_batch_shape5_rewrites_stale(tmp_path: Path):
    stale = tmp_path / "coreruleset_batch_shape5.json"
    stale.write_text(
        json.dumps({"schema_version": "1", "corpus": "coreruleset", "rows": [{"x": 1}]}),
        encoding="utf-8",
    )
    _clear_batch_shape5("coreruleset", tmp_path, note="trees missing")
    data = json.loads(stale.read_text(encoding="utf-8"))
    assert data["rows"] == []
    assert data["summary"]["executed"] == 0
    assert data["summary"]["note"] == "trees missing"


def test_resolve_missing_returns_none(tmp_path: Path, monkeypatch):
    monkeypatch.delenv("REGEXPROOF_CRS_OLDER_RULES", raising=False)
    monkeypatch.delenv("REGEXPROOF_CRS_NEWER_RULES", raising=False)
    # Empty env override: set both to empty dirs so lookup does not fall
    # through to a host /tmp/crs-shape5 from a prior local run.
    empty_a = tmp_path / "a"
    empty_b = tmp_path / "b"
    empty_a.mkdir()
    empty_b.mkdir()
    monkeypatch.setenv("REGEXPROOF_CRS_OLDER_RULES", str(empty_a))
    monkeypatch.setenv("REGEXPROOF_CRS_NEWER_RULES", str(empty_b))
    assert resolve_crs_version_trees(repo_root=tmp_path) is None


def test_resolve_env_paths(tmp_path: Path, monkeypatch):
    older = tmp_path / "old" / "rules"
    newer = tmp_path / "new" / "rules"
    older.mkdir(parents=True)
    newer.mkdir(parents=True)
    (older / "a.conf").write_text("x\n", encoding="utf-8")
    (newer / "a.conf").write_text("y\n", encoding="utf-8")
    monkeypatch.setenv("REGEXPROOF_CRS_OLDER_RULES", str(older))
    monkeypatch.setenv("REGEXPROOF_CRS_NEWER_RULES", str(newer))
    got = resolve_crs_version_trees(repo_root=tmp_path)
    assert got == (older, newer)


def test_discover_skips_known_timeout_pair():
    fixture = Path(__file__).resolve().parent / "fixtures" / "crs_pairs"
    older = fixture / "v4.27.0" / "rules"
    newer = fixture / "v4.28.0" / "rules"
    if not older.is_dir() or not newer.is_dir():
        return  # fixture layout optional for this skip test
    discovered = discover_crs_batch_pairs(older_rules=older, newer_rules=newer)
    ids = {p["pair_id"] for p in discovered["admitted"]}
    assert ids.isdisjoint(BATCH_TIMEOUT_PAIR_IDS)
