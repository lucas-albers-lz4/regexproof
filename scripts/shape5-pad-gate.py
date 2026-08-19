#!/usr/bin/env python3
"""Bounded pad-gate replay for shape-5 batch (issue #524, luna r5).

The pad-gate runs Python ``re.search`` over untrusted ``py_re`` patterns. A
catastrophic-backtracking pattern (e.g. ``(a+)+$``) can make ``re.search`` take
seconds to minutes — or effectively hang — on a non-match. The repo's security
model runs every untrusted pattern in a *timed subprocess* (pcre.py, ecma.py,
redos/tools.py), so the shape-5 pad gate does the same: the solver calls this
script with ``subprocess.run(timeout=...)`` and treats a timeout/error as a
fail-closed unknown (the witness does NOT confirm a search gap).

Payload is read from **stdin as one JSON object** — never argv — so a Z3 witness
containing characters that cannot cross the OS argv boundary (e.g. a NUL byte
``\\x00``) is handled safely (luna r6, issue #524).

Input JSON: {"r1_pattern", "r1_flags", "r2_pattern", "r2_flags", "witness"}
Prints a single JSON object {"confirmed": bool, "error": null|str}.
"""
from __future__ import annotations

import json
import re
import sys

PADS = ("", "a", " ", "\n", "0", "x")

_FLAG_MAP = {
    "i": re.IGNORECASE,
    "m": re.MULTILINE,
    "s": re.DOTALL,
    "x": re.VERBOSE,
}


def _flags_int(flags: str) -> int:
    out = 0
    for ch in flags or "":
        bit = _FLAG_MAP.get(ch)
        if bit:
            out |= bit
    return out


def _real_search(pattern: str, flags: str, text: str) -> bool:
    # Untrusted patterns can raise more than re.error (coderabbit #529):
    # RecursionError / OverflowError / MemoryError from catastrophic constructs.
    # Any of these means the search could not be evaluated -> treat as no-match
    # (False) so the replay still emits the defined JSON protocol instead of an
    # unhandled traceback (which would leave stdout empty and fail the parent).
    try:
        return re.search(pattern, text, _flags_int(flags)) is not None
    except (re.error, RecursionError, OverflowError, MemoryError):
        return False


def _main() -> int:
    raw = sys.stdin.read()
    if not raw.strip():
        json.dump({"confirmed": False, "error": "empty-stdin"}, sys.stdout)
        return 2
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        json.dump({"confirmed": False, "error": "bad-json"}, sys.stdout)
        return 2
    r1_pat = str(payload.get("r1_pattern") or "")
    r1_flags = str(payload.get("r1_flags") or "")
    r2_pat = str(payload.get("r2_pattern") or "")
    r2_flags = str(payload.get("r2_flags") or "")
    witness = payload.get("witness")
    if not isinstance(witness, str) or not witness:
        json.dump({"confirmed": False, "error": "empty-witness"}, sys.stdout)
        return 0
    confirmed = False
    for pre in PADS:
        for suf in PADS:
            s = pre + witness + suf
            if _real_search(r2_pat, r2_flags, s) and not _real_search(
                r1_pat, r1_flags, s
            ):
                confirmed = True
                break
        if confirmed:
            break
    json.dump({"confirmed": confirmed, "error": None}, sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
