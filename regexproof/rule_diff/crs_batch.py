"""CRS version-diff trees + batch shape-5 admission (#477 follow-on).

Batch executes only ``version_diff`` pairs with ``family_contract``. Pair
``crs-942522`` times out at DEFAULT_MAX_LEN=96 under the 30s batch budget
(measured); it stays out of batch until a bounded encoding lands.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from regexproof.rule_diff.crs_pairs import discover_crs_version_pairs

ROOT = Path(__file__).resolve().parents[2]

# Hard timeout under batch 30s / even 120s at max_len=96 — exclude from batch.
BATCH_TIMEOUT_PAIR_IDS = frozenset(
    {
        "crs-942522-v4.27.0-v4.28.0",
    }
)

DEFAULT_OLDER_TAG = "v4.27.0"
DEFAULT_NEWER_TAG = "v4.28.0"


def resolve_crs_version_trees(
    *,
    older_tag: str = DEFAULT_OLDER_TAG,
    newer_tag: str = DEFAULT_NEWER_TAG,
    repo_root: Path | None = None,
) -> tuple[Path, Path] | None:
    """Return ``(older_rules, newer_rules)`` when both trees exist.

    Lookup order:
    1. ``REGEXPROOF_CRS_OLDER_RULES`` / ``REGEXPROOF_CRS_NEWER_RULES``
    2. ``/tmp/crs-shape5/coreruleset-{tag}/rules`` (CI / local materialize)
    3. ``batch/corpora/coreruleset-{tag}/rules`` under *repo_root*
    """
    root = (repo_root or ROOT).resolve()
    env_old = (os.environ.get("REGEXPROOF_CRS_OLDER_RULES") or "").strip()
    env_new = (os.environ.get("REGEXPROOF_CRS_NEWER_RULES") or "").strip()
    if env_old or env_new:
        if not (env_old and env_new):
            return None
        older, newer = Path(env_old), Path(env_new)
        if (
            older.is_dir()
            and newer.is_dir()
            and any(older.iterdir())
            and any(newer.iterdir())
        ):
            return older, newer
        return None
    candidates: list[tuple[Path, Path]] = [
        (
            Path(f"/tmp/crs-shape5/coreruleset-{older_tag}/rules"),
            Path(f"/tmp/crs-shape5/coreruleset-{newer_tag}/rules"),
        ),
        (
            root / "batch" / "corpora" / f"coreruleset-{older_tag}" / "rules",
            root / "batch" / "corpora" / f"coreruleset-{newer_tag}" / "rules",
        ),
    ]
    for older, newer in candidates:
        if older.is_dir() and newer.is_dir() and any(older.iterdir()) and any(
            newer.iterdir()
        ):
            return older, newer
    return None


def discover_crs_batch_pairs(
    *,
    older_rules: Path,
    newer_rules: Path,
    older_tag: str = DEFAULT_OLDER_TAG,
    newer_tag: str = DEFAULT_NEWER_TAG,
) -> dict[str, Any]:
    """Discover version-diff pairs and drop known batch timeouts."""
    discovered = discover_crs_version_pairs(
        older_rules=older_rules,
        newer_rules=newer_rules,
        older_tag=older_tag,
        newer_tag=newer_tag,
    )
    admitted = [
        p
        for p in discovered["admitted"]
        if str(p.get("pair_id") or "") not in BATCH_TIMEOUT_PAIR_IDS
    ]
    skipped = [
        p
        for p in discovered["admitted"]
        if str(p.get("pair_id") or "") in BATCH_TIMEOUT_PAIR_IDS
    ]
    return {
        **{k: v for k, v in discovered.items() if k != "admitted"},
        "admitted": admitted,
        "batch_timeout_skipped": skipped,
    }
