#!/usr/bin/env python3
"""BusyBox is the claude-code-plugins posix-shell product engine (wave 1).

Unlike ``ci-check-busybox-sed.py`` (GNU∩BusyBox agreement), this checker:

- hard-fails when busybox is absent
- bash ``=~`` search sites replay as BusyBox ``grep -E`` alphabet spot-checks
- skill-ref substitution replays as BusyBox ``sed -nE`` as at the call site
- BusyBox alone decides pass/fail (GNU is not consulted)

Run from the golden / proof job after busybox is installed.
"""

from __future__ import annotations

import shutil
import subprocess
import sys

from regexproof.harness.claude_code_plugins import (
    CLI_FLAG_GREP,
    FAMILY,
    GIT_E_GREP,
    SKILL_REF_SED,
)
from regexproof.harness.core import REGISTRY


def _require_busybox() -> None:
    if not shutil.which("busybox"):
        print(
            "error: busybox absent — claude-code-plugins product engine is required",
            file=sys.stderr,
        )
        raise SystemExit(2)


def _busybox_grep_q(pattern: str, stream: str) -> bool:
    proc = subprocess.run(
        ["busybox", "grep", "-qE", pattern],
        input=stream,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    if proc.returncode not in (0, 1):
        raise RuntimeError(f"grep -qE failed rc={proc.returncode}")
    return proc.returncode == 0


def _busybox_sed_n(pattern: str, stream: str) -> str:
    expr = f"s|{pattern}|\\1|p"
    proc = subprocess.run(
        ["busybox", "sed", "-nE", expr],
        input=stream,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    if proc.returncode not in (0, 1):
        raise RuntimeError(f"sed -nE failed rc={proc.returncode} err={proc.stderr!r}")
    lines = proc.stdout.splitlines()
    return lines[0] if lines else ""


def _spot_alphabets() -> int:
    if not _busybox_grep_q(CLI_FLAG_GREP, "--force-evaluate"):
        print("error: CLI flag reject --force-evaluate", file=sys.stderr)
        return 1
    if _busybox_grep_q(CLI_FLAG_GREP, "--;force"):
        print("error: CLI flag accept semicolon as flag body", file=sys.stderr)
        return 1
    if not _busybox_grep_q(GIT_E_GREP, "-fe"):
        print("error: git-clean -e bundle reject -fe", file=sys.stderr)
        return 1
    if _busybox_grep_q(GIT_E_GREP, "-f;e"):
        print("error: git-clean -e bundle accept semicolon", file=sys.stderr)
        return 1
    got = _busybox_sed_n(SKILL_REF_SED, "/guardrails:audit --apply")
    if got != "/guardrails:audit":
        print(
            f"error: skill-ref sed identity fail got={got!r}",
            file=sys.stderr,
        )
        return 1
    if _busybox_sed_n(SKILL_REF_SED, "/guardrails:audit;rm"):
        print("error: skill-ref sed accept semicolon in ref", file=sys.stderr)
        return 1
    print("AI-claude-plugins alphabet spot-checks: ok on BusyBox grep -E / sed -E")
    return 0


def main() -> int:
    _require_busybox()
    names = [n for n, e in REGISTRY.items() if e.get("family") == FAMILY]
    if not names:
        print("error: family AI-claude-plugins missing from REGISTRY", file=sys.stderr)
        return 1
    print("AI-claude-plugins registry:", ", ".join(sorted(names)))
    return _spot_alphabets()


if __name__ == "__main__":
    raise SystemExit(main())
