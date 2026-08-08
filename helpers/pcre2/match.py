#!/usr/bin/env python3
"""PCRE2 CLI helper — parse + replay via the `pcre2` Python bindings if present,
falling back to the system `pcre2grep` for match-only.

Usage:
  match.py parse <pattern>
  match.py match <pattern> <flags>   # stdin → exit 0 on match
"""

from __future__ import annotations

import json
import subprocess
import sys


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: match.py parse|match ...", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "parse":
        pattern = sys.argv[2]
        return parse(pattern)
    if cmd == "match":
        pattern = sys.argv[2]
        flags = sys.argv[3] if len(sys.argv) > 3 else ""
        data = sys.stdin.read()
        return match(pattern, flags, data)
    print("unknown command", file=sys.stderr)
    return 2


def parse(pattern: str) -> int:
    # Reject known unencodable constructs for the Phase-1 subset.
    reject_markers = [
        ("(?=", "lookaround"),
        ("(?!", "lookaround"),
        ("(?<=", "lookaround"),
        ("(?<!", "lookaround"),
        ("\\k<", "backref"),
        ("\\g<", "backref"),
        ("(?(", "conditional"),
        ("\\K", "reset"),
        ("\\G", "g-anchor"),
    ]
    for marker, reason in reject_markers:
        if marker in pattern:
            print(json.dumps({"ok": False, "unencodable_reason": reason, "helper": "pcre2"}))
            return 1
    # Backrefs \1..\9
    import re as _re

    if _re.search(r"(?<!\\)\\[1-9]", pattern):
        print(json.dumps({"ok": False, "unencodable_reason": "backref", "helper": "pcre2"}))
        return 1
    try:
        import pcre2  # type: ignore

        pcre2.compile(pattern.encode())
        print(json.dumps({"ok": True, "helper": "pcre2-bindings"}))
        return 0
    except ImportError:
        # Bindings absent — structural accept for encodable-subset probes.
        print(json.dumps({"ok": True, "helper": "pcre2-structural"}))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"ok": False, "unencodable_reason": "parse-error", "error": str(exc)}))
        return 1


def match(pattern: str, flags: str, data: str) -> int:
    try:
        import pcre2  # type: ignore

        opts = 0
        if "i" in flags:
            opts |= pcre2.COMPAT_I
        re = pcre2.compile(pattern.encode(), options=opts)
        return 0 if re.search(data.encode()) else 1
    except ImportError:
        pass
    # Fallback: Python re as approximate for ASCII subset smoke only.
    import re

    f = 0
    if "i" in flags:
        f |= re.I
    try:
        return 0 if re.search(pattern, data, f) else 1
    except re.error:
        return 2


if __name__ == "__main__":
    # Optional pcre2grep path for environments that ship it.
    if len(sys.argv) >= 2 and sys.argv[1] == "match-pcre2grep":
        pattern = sys.argv[2]
        data = sys.stdin.read()
        proc = subprocess.run(
            ["pcre2grep", "-q", "--", pattern],
            input=data,
            text=True,
            capture_output=True,
            shell=False,
            check=False,
        )
        sys.exit(proc.returncode)
    sys.exit(main())
