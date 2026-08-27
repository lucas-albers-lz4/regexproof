#!/usr/bin/env python3
"""BusyBox is the aidevops posix-shell product engine (conversion wave 1).

Unlike ``ci-check-busybox-sed.py`` (GNU∩BusyBox agreement), this checker:

- hard-fails when busybox is absent
- expected-UNSAT shape-3 (brief t-ID capture, gh issue digit capture)
  is differential fuzz, not witness replay
- bash ``=~`` sites are replayed as BusyBox ``grep -E`` (not sed)
- BusyBox alone decides pass/fail (GNU is not consulted)

Run from the golden job after busybox is installed.
"""

from __future__ import annotations

import random
import shutil
import string
import subprocess
import sys

from regexproof.harness.aidevops import (
    BRIEF_FILTER,
    BRIEF_TID_GREP,
    FAMILY,
    ISSUE_GREP,
)
from regexproof.harness.core import REGISTRY

CRED_IDENT = r"\$\{?(remote_url|origin_url)\}?"
SCOPE_HEADING = r"^##[#]?[[:space:]]+Files[[:space:]]+Scope"


def _require_busybox() -> None:
    if not shutil.which("busybox"):
        print(
            "error: busybox absent — aidevops product engine is required",
            file=sys.stderr,
        )
        raise SystemExit(2)


def _busybox_grep_o(pattern: str, stream: str) -> str:
    proc = subprocess.run(
        ["busybox", "grep", "-oE", pattern],
        input=stream,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    if proc.returncode not in (0, 1):
        raise RuntimeError(f"grep -oE failed rc={proc.returncode}")
    lines = proc.stdout.splitlines()
    return lines[0] if lines else ""


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


def _fuzz_brief_tid(n: int = 32, seed: int = 42) -> int:
    """Replay bash ``=~ ^todo/tasks/(t[0-9]+)-brief\\.md$`` via BusyBox grep -E."""
    rng = random.Random(seed)
    for i in range(n):
        digits = "".join(rng.choice(string.digits) for _ in range(rng.randint(1, 15)))
        tid = "t" + digits
        stream = f"todo/tasks/{tid}-brief.md"
        if not _busybox_grep_q(BRIEF_FILTER, stream):
            print(
                f"error: brief filter reject good path i={i} stream={stream!r}",
                file=sys.stderr,
            )
            return 2
        got = _busybox_grep_o(BRIEF_TID_GREP, stream)
        if got != tid:
            print(
                f"error: brief tid fuzz mismatch i={i} tid={tid!r} got={got!r}",
                file=sys.stderr,
            )
            return 2
    print(f"brief-tid differential fuzz: {n} t[0-9]+ ids identity-ok on BusyBox grep -E")
    return 0


def _fuzz_gh_issue(n: int = 32, seed: int = 42) -> int:
    rng = random.Random(seed)
    for i in range(n):
        w = "".join(rng.choice(string.digits) for _ in range(rng.randint(1, 8)))
        stream = f"Resolves #{w}"
        raw = _busybox_grep_o(ISSUE_GREP, stream)
        got = raw[1:] if raw.startswith("#") else raw
        if got != w:
            print(
                f"error: gh-issue fuzz mismatch i={i} w={w!r} got={got!r} raw={raw!r}",
                file=sys.stderr,
            )
            return 2
    print(f"gh-issue differential fuzz: {n} digit issues identity-ok on BusyBox")
    return 0


def _spot_alphabets() -> int:
    if not _busybox_grep_q(BRIEF_FILTER, "todo/tasks/t12-brief.md"):
        print("error: brief filter reject good filename", file=sys.stderr)
        return 1
    if _busybox_grep_q(BRIEF_FILTER, "todo/tasks/t12;x-brief.md"):
        print("error: brief filter accept semicolon", file=sys.stderr)
        return 1
    if not _busybox_grep_q(CRED_IDENT, "echo $remote_url"):
        print("error: cred ident reject $remote_url", file=sys.stderr)
        return 1
    if _busybox_grep_q(CRED_IDENT, "echo $remote;url"):
        print("error: cred ident accept semicolon ident", file=sys.stderr)
        return 1
    if not _busybox_grep_q(SCOPE_HEADING, "## Files Scope"):
        print("error: scope heading reject ## Files Scope", file=sys.stderr)
        return 1
    if _busybox_grep_q(SCOPE_HEADING, "## Files; Scope"):
        print("error: scope heading accept semicolon", file=sys.stderr)
        return 1
    print("AI-aidevops alphabet spot-checks: ok on BusyBox grep -E")
    return 0


def main() -> int:
    _require_busybox()
    names = [n for n, e in REGISTRY.items() if e.get("family") == FAMILY]
    if not names:
        print("error: family AI-aidevops missing from REGISTRY", file=sys.stderr)
        return 1
    print("AI-aidevops registry:", ", ".join(sorted(names)))
    rc = _spot_alphabets()
    if rc:
        return rc
    brief = _fuzz_brief_tid()
    if brief:
        return brief
    return _fuzz_gh_issue()


if __name__ == "__main__":
    raise SystemExit(main())
