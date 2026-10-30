#!/usr/bin/env python3
"""Parse and replay patterns with the real JDK java.util.regex.Pattern engine.

Requires a JDK with source-file mode (Java 11+). There is deliberately no
fallback to Python's regex engine: missing Java is reported as unavailable.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

RUNNER = Path(__file__).with_name("PatternRunner.java")
TIMEOUT_S = 30


def run(mode: str, pattern: str, flags: str = "", call_kind: str = "search") -> int:
    java = shutil.which("java")
    if java is None:
        print(
            json.dumps(
                {"ok": False, "helper": "java-pattern-missing", "error": "java unavailable"}
            )
        )
        return 3
    args = [java, str(RUNNER), mode, pattern, flags, call_kind]
    try:
        proc = subprocess.run(
            args,
            input=sys.stdin.read() if mode == "match" else None,
            text=True,
            capture_output=True,
            shell=False,
            check=False,
            timeout=TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        print(json.dumps({"ok": False, "unencodable_reason": "timeout", "helper": "java-pattern"}))
        return 3
    if mode == "parse":
        print(proc.stdout.strip() or json.dumps({
            "ok": False,
            "unencodable_reason": "parse-error",
            "error": proc.stderr.strip(),
            "helper": "java-pattern",
        }))
    return proc.returncode


def main() -> int:
    if len(sys.argv) < 3:
        print(
            "usage: match.py parse PATTERN [FLAGS] | match PATTERN FLAGS CALL_KIND",
            file=sys.stderr,
        )
        return 2
    mode = sys.argv[1]
    pattern = sys.argv[2]
    flags = sys.argv[3] if len(sys.argv) >= 4 else ""
    call_kind = sys.argv[4] if len(sys.argv) >= 5 else "search"
    if mode not in {"parse", "match"}:
        print(f"unknown mode: {mode}", file=sys.stderr)
        return 2
    return run(mode, pattern, flags, call_kind)


if __name__ == "__main__":
    sys.exit(main())
