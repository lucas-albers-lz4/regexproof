"""Wave 9 (#578): depth-1 root-dir signature — soft deprioritize, never reject."""

from __future__ import annotations

from typing import Iterable

DEPRIORITIZE_ROOTS = frozenset(
    {
        "test",
        "tests",
        "vendor",
        "contrib",
        "examples",
        "docs",
        "ci",
        "node_modules",
    }
)
SRC_LIKE_ROOTS = frozenset(
    {"src", "lib", "pkg", "app", "cmd", "internal", "packages", "core"}
)


def root_names_from_paths(paths: Iterable[str]) -> list[str]:
    names: set[str] = set()
    for raw in paths:
        p = str(raw or "").strip().lstrip("./")
        if not p:
            continue
        names.add(p.split("/", 1)[0].lower())
    return sorted(names)


def root_dir_deprioritized(root_names: Iterable[str]) -> bool:
    """True when depth-1 names look like a test/vendor tree, not product src.

    Soft ranking signal only — callers must never drop the candidate.
    """
    roots = {str(n).lower() for n in root_names if str(n).strip()}
    if not roots:
        return False
    testish = roots & DEPRIORITIZE_ROOTS
    frac = len(testish) / len(roots)
    has_src = bool(roots & SRC_LIKE_ROOTS)
    return frac >= 0.5 or (not has_src and frac >= 0.3)
