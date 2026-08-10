"""Shared z3-solver version pin (exit 3 on non-5.0.x)."""

from __future__ import annotations

import sys


def assert_z3_pinned() -> str:
    """Refuse to run on an unpinned solver. Returns the version string on success.

    Exit code 3 matches ``scripts/z3-verify.py`` / AGENTS.md contract.
    """
    import z3

    version = z3.get_version_string()
    if not version.startswith("5.0"):
        print(
            f"FATAL: z3-solver {version} — this harness is validated against "
            "5.0.x only. Install the pinned version: pip install -r requirements.txt",
            file=sys.stderr,
        )
        sys.exit(3)
    return version
