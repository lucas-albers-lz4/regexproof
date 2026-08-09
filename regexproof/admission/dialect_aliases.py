"""Dialect key alias policy for probe output (umbrella C6)."""

from __future__ import annotations

# Known aliases → compiler DIALECTS keys. Unknown/first-seen keys are preserved.
DIALECT_ALIASES: dict[str, str] = {
    "py": "py_re",
}


def normalize_dialect_counts(counts: dict[str, int]) -> dict[str, int]:
    """Normalize known dialect aliases; preserve unknown keys; merge collisions."""
    out: dict[str, int] = {}
    for key, n in counts.items():
        canon = DIALECT_ALIASES.get(key, key)
        out[canon] = out.get(canon, 0) + int(n)
    return out
