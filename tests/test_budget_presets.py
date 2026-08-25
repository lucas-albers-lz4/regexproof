"""Budget preset equivalence — Fowler PR4 (before replacing manifest literals)."""

from __future__ import annotations

import json
from pathlib import Path

from regexproof.batch.budgets import BUDGET_PRESETS, budget_as_dict
from regexproof.batch.manifests import CORPUS_MANIFESTS

_BASELINE_PATH = Path(__file__).resolve().parent / "fixtures" / "corpus_budget_baseline.json"
_MAIN_BASELINE: dict[str, dict] = json.loads(_BASELINE_PATH.read_text(encoding="utf-8"))


def test_every_manifest_budget_matches_main_baseline():
    """Equivalence: post-preset budgets must equal pre-refactor main literals."""
    assert set(CORPUS_MANIFESTS) == set(_MAIN_BASELINE)
    for name, meta in CORPUS_MANIFESTS.items():
        current = dict(meta.get("budget") or {})
        expected = dict(_MAIN_BASELINE[name])
        assert current == expected, name


def test_preset_shaped_budgets_use_named_constants():
    """Preset-shaped budgets must resolve to exactly one named preset."""
    for name, meta in CORPUS_MANIFESTS.items():
        budget = meta.get("budget") or {}
        if not budget:
            continue
        matched = [
            pname
            for pname, preset in BUDGET_PRESETS.items()
            if dict(budget) == budget_as_dict(preset)
        ]
        if matched:
            assert len(matched) == 1, (name, matched)


def test_budget_presets_are_distinct():
    seen: dict[tuple, str] = {}
    for pname, preset in BUDGET_PRESETS.items():
        key = tuple(sorted(budget_as_dict(preset).items()))
        assert key not in seen, f"{pname} duplicates {seen[key]}"
        seen[key] = pname
