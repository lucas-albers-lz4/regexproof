"""Corpus budget helpers and BudgetBreached (#193)."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, NotRequired, TypedDict

_ADDRESS_SPACE_CAP_WARNED = False
LAST_ADDRESS_SPACE_CAP_APPLIED: bool | None = None


class Budget(TypedDict, total=False):
    max_patterns: int
    max_wall_s: int
    redos_wall_s: int
    max_mem_mb: int
    max_disk_mb: int


# Exact presets — only use where the 5-tuple (or subset) matches byte-for-byte.
BUDGET_RULE_DEFAULT: Budget = {
    "max_patterns": 5000,
    "max_wall_s": 900,
    "redos_wall_s": 180,
    "max_mem_mb": 2048,
    "max_disk_mb": 500,
}
BUDGET_VALIDATOR: Budget = {
    "max_patterns": 5000,
    "max_wall_s": 600,
    "redos_wall_s": 120,
    "max_mem_mb": 1024,
    "max_disk_mb": 100,
}
BUDGET_VALIDATOR_DISK200: Budget = {
    "max_patterns": 5000,
    "max_wall_s": 600,
    "redos_wall_s": 120,
    "max_mem_mb": 1024,
    "max_disk_mb": 200,
}
BUDGET_PATROL: Budget = {
    "max_patterns": 5000,
    "max_wall_s": 600,
    "redos_wall_s": 120,
    "max_mem_mb": 2048,
    "max_disk_mb": 500,
}
BUDGET_PATROL_DISK1000: Budget = {
    "max_patterns": 5000,
    "max_wall_s": 600,
    "redos_wall_s": 120,
    "max_mem_mb": 2048,
    "max_disk_mb": 1000,
}
BUDGET_LUCI_DISK: Budget = {
    "max_patterns": 5000,
    "max_wall_s": 900,
    "redos_wall_s": 180,
    "max_mem_mb": 2048,
    "max_disk_mb": 2000,
}
BUDGET_LIGHT: Budget = {
    "max_patterns": 5000,
    "max_wall_s": 300,
    "redos_wall_s": 60,
    "max_mem_mb": 512,
    "max_disk_mb": 50,
}
BUDGET_HEAVY_30K: Budget = {
    "max_patterns": 30000,
    "max_wall_s": 1200,
    "redos_wall_s": 240,
    "max_mem_mb": 4096,
    "max_disk_mb": 1000,
}
BUDGET_HEAVY_50K: Budget = {
    "max_patterns": 50000,
    "max_wall_s": 1200,
    "redos_wall_s": 240,
    "max_mem_mb": 4096,
    "max_disk_mb": 1000,
}
BUDGET_TESTDATA_LIGHT: Budget = {
    "max_patterns": 5000,
    "max_wall_s": 300,
    "max_mem_mb": 512,
    "max_disk_mb": 50,
}

# Named preset registry for equivalence tests / loaders.
BUDGET_PRESETS: dict[str, Budget] = {
    "rule_default": BUDGET_RULE_DEFAULT,
    "validator": BUDGET_VALIDATOR,
    "validator_disk200": BUDGET_VALIDATOR_DISK200,
    "patrol": BUDGET_PATROL,
    "patrol_disk1000": BUDGET_PATROL_DISK1000,
    "luci_disk": BUDGET_LUCI_DISK,
    "light": BUDGET_LIGHT,
    "heavy_30k": BUDGET_HEAVY_30K,
    "heavy_50k": BUDGET_HEAVY_50K,
    "testdata_light": BUDGET_TESTDATA_LIGHT,
}


class CorpusManifest(TypedDict, total=False):
    """Loose TypedDict — glob / files / measure_scope are NotRequired (Grok G5)."""

    corpus_type: str
    path: Path
    dialect: str
    extractor: str
    repo: str
    security_tool: bool
    lift_inline: bool
    corpus_pin: str
    budget: Budget
    glob: NotRequired[str]
    files: NotRequired[list[str]]
    measure_scope: NotRequired[str]
    sample_path: NotRequired[Path]
    full_path: NotRequired[Path]
    declared_semantics: NotRequired[str]
    commit: NotRequired[str]


def budget_as_dict(budget: Budget) -> dict[str, Any]:
    """Return a plain dict copy (manifests store dicts for JSON round-trips)."""
    return dict(budget)


class BudgetBreached(Exception):
    """Raised when a corpus budget limit is exceeded."""

    def __init__(self, corpus: str, field: str, limit: Any, actual: Any) -> None:
        self.corpus = corpus
        self.field = field
        self.limit = limit
        self.actual = actual
        super().__init__(
            f"budget breach: {corpus}.{field} limit={limit} actual={actual}"
        )


def check_budget_patterns(
    records: list[dict[str, Any]],
    budget: dict[str, Any],
    corpus_slug: str,
) -> None:
    max_pat = budget.get("max_patterns")
    if max_pat is not None and max_pat > 0 and len(records) > max_pat:
        raise BudgetBreached(corpus_slug, "max_patterns", max_pat, len(records))


def check_budget_mem() -> int:
    """Return *current* process RSS in MB (best-effort).

    Prefer ``/proc/self/status`` VmRSS on Linux so growth is visible during a
    long compile. ``ru_maxrss`` is peak-only and still used as fallback.
    """
    try:
        with open("/proc/self/status", encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("VmRSS:"):
                    # VmRSS is kB.
                    return int(line.split()[1]) // 1024
    except Exception:
        pass
    try:
        import resource

        usage = resource.getrusage(resource.RUSAGE_SELF)
        # Linux: ru_maxrss is kB; macOS: bytes. Detect via /proc existence.
        raw = int(usage.ru_maxrss)
        if Path("/proc/self/status").exists():
            return raw // 1024
        return raw // (1024 * 1024)
    except Exception:
        return 0


def apply_address_space_cap(budget: dict[str, Any]) -> bool:
    """Hard OS cap so a runaway Z3 compile cannot OOM-kill the desktop.

    Uses ``RLIMIT_AS`` at 2× ``max_mem_mb`` (bytes). Soft MemoryError /
    allocation failure then surfaces before the kernel OOM killer.

    Returns True when the cap was installed; False when unavailable
    (platform/permission). Warns once on failure so macOS/dev runs are not
    silent about advisory-only memory budgets.
    """
    global _ADDRESS_SPACE_CAP_WARNED, LAST_ADDRESS_SPACE_CAP_APPLIED
    max_mb = budget.get("max_mem_mb")
    if not max_mb:
        LAST_ADDRESS_SPACE_CAP_APPLIED = None
        return False
    try:
        import resource

        # 2× budget: leave headroom for allocator arenas; still far below
        # the ~30GiB OOM kills observed on v8_mjsunit measure runs.
        cap = int(max_mb) * 2 * 1024 * 1024
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        # Only tighten; never raise an existing stricter cap.
        new_soft = cap if soft == resource.RLIM_INFINITY else min(soft, cap)
        new_hard = cap if hard == resource.RLIM_INFINITY else min(hard, cap)
        resource.setrlimit(resource.RLIMIT_AS, (new_soft, new_hard))
        LAST_ADDRESS_SPACE_CAP_APPLIED = True
        return True
    except Exception as exc:
        if not _ADDRESS_SPACE_CAP_WARNED:
            print(
                f"WARNING: address-space memory cap unavailable "
                f"(max_mem_mb={max_mb} is advisory only): {exc}",
                file=sys.stderr,
            )
            _ADDRESS_SPACE_CAP_WARNED = True
        LAST_ADDRESS_SPACE_CAP_APPLIED = False
        return False
