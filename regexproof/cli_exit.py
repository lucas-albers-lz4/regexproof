"""Shared SystemExit → process exit-code mapping for CLIs."""

from __future__ import annotations

import sys


def exit_code_from_system_exit(exc: BaseException) -> int:
    """Map ``SystemExit`` to an int exit code.

    Preserves: ``None`` → 0, ``int`` passthrough, other → print stderr + 1.
    """
    code = getattr(exc, "code", 1)
    if code is None:
        return 0
    if isinstance(code, int):
        return code
    print(code, file=sys.stderr)
    return 1
