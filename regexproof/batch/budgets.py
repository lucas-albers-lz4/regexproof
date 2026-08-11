"""Corpus budget helpers and BudgetBreached (#193)."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_ADDRESS_SPACE_CAP_WARNED = False
LAST_ADDRESS_SPACE_CAP_APPLIED: bool | None = None


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
    except Exception:  # noqa: BLE001
        pass
    try:
        import resource

        usage = resource.getrusage(resource.RUSAGE_SELF)
        # Linux: ru_maxrss is kB; macOS: bytes. Detect via /proc existence.
        raw = int(usage.ru_maxrss)
        if Path("/proc/self/status").exists():
            return raw // 1024
        return raw // (1024 * 1024)
    except Exception:  # noqa: BLE001
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
    except Exception as exc:  # noqa: BLE001
        if not _ADDRESS_SPACE_CAP_WARNED:
            print(
                f"WARNING: address-space memory cap unavailable "
                f"(max_mem_mb={max_mb} is advisory only): {exc}",
                file=sys.stderr,
            )
            _ADDRESS_SPACE_CAP_WARNED = True
        LAST_ADDRESS_SPACE_CAP_APPLIED = False
        return False
