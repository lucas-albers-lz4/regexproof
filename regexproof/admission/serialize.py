"""Pinned JSON serialization for admission probe drafts (umbrella determinism)."""

from __future__ import annotations

import json
from typing import Any


def dumps_pinned(obj: Any) -> str:
    """Serialize with the contract pinned in #129 / ci-batch-repro convention.

    ``json.dumps(indent=2, sort_keys=True, ensure_ascii=False)`` plus a trailing
    newline so on-disk artifacts match committed gate-decision style.
    """
    return json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
