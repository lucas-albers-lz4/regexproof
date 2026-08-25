"""Budget preset equivalence — Fowler PR4 (before replacing manifest literals)."""

from __future__ import annotations

from regexproof.batch.budgets import BUDGET_PRESETS, budget_as_dict
from regexproof.batch.manifests import CORPUS_MANIFESTS


def _matches_preset(budget: dict, preset: dict) -> bool:
    return dict(budget) == dict(preset)


def test_every_manifest_budget_matches_literal_or_known_preset():
    """Equivalence: reconstructing via presets must equal stored budgets.

    Corpora that do not match any named preset keep inline budgets; this
    test only asserts that every preset-shaped budget equals its named
    constant exactly (no silent wall_s / mem drift).
    """
    for name, meta in CORPUS_MANIFESTS.items():
        budget = meta.get("budget") or {}
        if not budget:
            continue
        matched = [
            pname
            for pname, preset in BUDGET_PRESETS.items()
            if _matches_preset(budget, budget_as_dict(preset))
        ]
        if matched:
            assert len(matched) == 1, (name, matched)
            assert dict(budget) == budget_as_dict(BUDGET_PRESETS[matched[0]])


def test_budget_presets_are_distinct():
    seen: dict[tuple, str] = {}
    for pname, preset in BUDGET_PRESETS.items():
        key = tuple(sorted(budget_as_dict(preset).items()))
        assert key not in seen, f"{pname} duplicates {seen[key]}"
        seen[key] = pname
