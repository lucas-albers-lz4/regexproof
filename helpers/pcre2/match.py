#!/usr/bin/env python3
"""PCRE2 CLI helper — parse + replay via pcre2 bindings or pcre2grep.

Never falls back to Python `re` (wrong engine = broken ground-truth gate).

Usage:
  match.py parse <pattern>
  match.py match <pattern> <flags>   # stdin → exit 0 on match
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

# Checkout bootstrap so helper shares reject markers with compile_pcre (#73).
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from regexproof.compiler.reject_markers import (  # noqa: E402
    PCRE_REJECT_MARKERS,
    unicode_prop_unencodable,
)

HELPER_TIMEOUT_S = 30


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: match.py parse|match ...", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "parse":
        return parse(sys.argv[2])
    if cmd == "match":
        pattern = sys.argv[2]
        flags = sys.argv[3] if len(sys.argv) > 3 else ""
        data = sys.stdin.read()
        return match(pattern, flags, data)
    print("unknown command", file=sys.stderr)
    return 2


def _reject_unencodable(pattern: str) -> str | None:
    prop = unicode_prop_unencodable(pattern)
    if prop:
        return prop
    for marker, reason in PCRE_REJECT_MARKERS:
        if marker in pattern:
            return reason
    import re as _re

    if _re.search(r"(?<!\\)\\[1-9]", pattern):
        return "backref"
    return None


def _has_pcre2_bindings() -> bool:
    try:
        import pcre2  # noqa: F401

        return True
    except ImportError:
        return False


def _has_pcre2grep() -> bool:
    return shutil.which("pcre2grep") is not None


def parse(pattern: str) -> int:
    reason = _reject_unencodable(pattern)
    if reason:
        print(json.dumps({"ok": False, "unencodable_reason": reason, "helper": "pcre2"}))
        return 1
    if _has_pcre2_bindings():
        try:
            import pcre2  # type: ignore

            pcre2.compile(pattern.encode())
            print(json.dumps({"ok": True, "helper": "pcre2-bindings"}))
            return 0
        except Exception as exc:  # noqa: BLE001
            print(
                json.dumps(
                    {
                        "ok": False,
                        "unencodable_reason": "parse-error",
                        "error": str(exc),
                        "helper": "pcre2-bindings",
                    }
                )
            )
            return 1
    if _has_pcre2grep():
        # pcre2grep validates by attempting a match against empty — compile errors → 2
        proc = subprocess.run(
            ["pcre2grep", "-q", "--", pattern],
            input="",
            text=True,
            capture_output=True,
            shell=False,
            check=False,
            timeout=HELPER_TIMEOUT_S,
        )
        if proc.returncode in (0, 1):
            print(json.dumps({"ok": True, "helper": "pcre2grep"}))
            return 0
        print(
            json.dumps(
                {
                    "ok": False,
                    "unencodable_reason": "parse-error",
                    "error": proc.stderr.strip() or "pcre2grep reject",
                    "helper": "pcre2grep",
                }
            )
        )
        return 1
    print(
        json.dumps(
            {
                "ok": False,
                "unencodable_reason": "pcre2-helper-unavailable",
                "helper": "none",
            }
        )
    )
    return 1


def match(pattern: str, flags: str, data: str) -> int:
    if _has_pcre2_bindings():
        try:
            import pcre2  # type: ignore

            opts = 0
            if "i" in flags and hasattr(pcre2, "COMPAT_I"):
                opts |= pcre2.COMPAT_I
            compiled = pcre2.compile(pattern.encode(), options=opts)
            return 0 if compiled.search(data.encode()) else 1
        except Exception:  # noqa: BLE001
            return 2
    if _has_pcre2grep():
        argv = ["pcre2grep", "-q"]
        if "i" in flags:
            argv.append("-i")
        argv.extend(["--", pattern])
        proc = subprocess.run(
            argv,
            input=data,
            text=True,
            capture_output=True,
            shell=False,
            check=False,
            timeout=HELPER_TIMEOUT_S,
        )
        return 0 if proc.returncode == 0 else 1
    print("FATAL: no pcre2 bindings and no pcre2grep — refusing Python re fallback", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
