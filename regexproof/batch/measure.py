"""Shared measure/remeasure fingerprint helpers (#197)."""

from __future__ import annotations

import hashlib
import platform
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]


def compiler_fingerprint(*, root: Path | None = None) -> str:
    """Stable short hash of ``regexproof/compiler/*.py`` contents."""
    base = (root or ROOT) / "regexproof" / "compiler"
    h = hashlib.sha256()
    for p in sorted(base.rglob("*.py")):
        h.update(p.read_bytes())
    return h.hexdigest()[:16]


def engine_versions(*, z3_mod: Any | None = None) -> dict[str, str]:
    """Python + z3 versions for measure artifacts."""
    if z3_mod is None:
        import z3 as z3_mod
    return {
        "python": platform.python_version(),
        "z3": getattr(z3_mod, "get_version_string", lambda: "?")(),
    }


def fraction_report(
    *,
    corpus: str,
    sample_size: int,
    encodable: int,
    reasons: dict[str, int],
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Common encodable-fraction report skeleton."""
    n = sample_size or 1
    report: dict[str, Any] = {
        "corpus": corpus,
        "sample_size": sample_size,
        "encodable": encodable,
        "fraction": round(encodable / n, 4),
        "reasons": reasons,
        "compiler_fingerprint": compiler_fingerprint(),
        **engine_versions(),
    }
    if extra:
        report.update(extra)
    return report
