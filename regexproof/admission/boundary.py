"""Deterministic security-boundary classifier (umbrella C2 + Sonnet B)."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Literal

BoundaryVerdict = Literal["deterministic-true", "deterministic-false", "unknown"]

_SIGNALS_PATH = Path(__file__).resolve().parent / "boundary_signals.json"


@dataclass(frozen=True)
class BoundarySignals:
    """Inputs available to the probe boundary classifier (metadata-level)."""

    repo_name: str = ""
    topics: tuple[str, ...] = ()
    paths: tuple[str, ...] = ()
    description: str = ""
    extra_positive: bool = False
    extra_negative_category: str | None = None


@lru_cache(maxsize=2)
def load_signal_lists(path: str | None = None) -> dict[str, Any]:
    p = Path(path) if path else _SIGNALS_PATH
    return json.loads(p.read_text(encoding="utf-8"))


def _token_match(hay: str, needle: str) -> bool:
    """Match *needle* as a token, or as an intentional prefix if it ends with ``-``/``/``.

    Whole-token matching avoids ``waf``⊂``waffle``. Prefix needles like
    ``awesome-`` / ``secrets/`` only require a leading boundary so directory
    and name-prefix signals still fire (Bugbot follow-up).
    """
    n = needle.lower().strip()
    if not n:
        return False
    h = hay.lower()
    if n[-1] in "-_/":
        return re.search(rf"(?<![a-z0-9]){re.escape(n)}", h) is not None
    return re.search(rf"(?<![a-z0-9]){re.escape(n)}(?![a-z0-9])", h) is not None


def _has_positive(signals: BoundarySignals, lists: dict[str, Any]) -> bool:
    if signals.extra_positive:
        return True
    pos = lists.get("positive", {})
    name_hay = f"{signals.repo_name} {signals.description}"
    for sub in pos.get("name_substrings", []):
        if _token_match(name_hay, sub):
            return True
    topic_hay = " ".join(signals.topics)
    desc = signals.description
    for kw in pos.get("topic_keywords", []):
        if _token_match(topic_hay, kw) or _token_match(desc, kw):
            return True
    path_hay = " ".join(signals.paths)
    for sub in pos.get("path_substrings", []):
        if _token_match(path_hay, sub):
            return True
    return False


def _negative_category(signals: BoundarySignals, lists: dict[str, Any]) -> str | None:
    if signals.extra_negative_category:
        return signals.extra_negative_category
    cats: dict[str, Any] = lists.get("negative_categories", {})
    name_hay = f"{signals.repo_name} {signals.description}"
    for cat, spec in cats.items():
        for sub in spec.get("name_substrings", []):
            if _token_match(name_hay, sub):
                return cat
    return None


def classify_boundary(
    signals: BoundarySignals,
    *,
    signal_lists: dict[str, Any] | None = None,
) -> BoundaryVerdict:
    """Ordered rule: positive → true; else negative → false; else unknown."""
    lists = signal_lists if signal_lists is not None else load_signal_lists()
    if _has_positive(signals, lists):
        return "deterministic-true"
    if _negative_category(signals, lists) is not None:
        return "deterministic-false"
    return "unknown"
