#!/usr/bin/env python3
"""Python `re` ground-truth helper — timed subprocess runner owned by the
ground-truth adapter (``regexproof/groundtruth/adapters.py``).

The adapter routes py_re replay through this helper so ``timeout_s`` is ALWAYS
honored: a catastrophic pattern would block the gate indefinitely in-process
(P1 finding 3), here the subprocess timeout bounds it. ``re.fullmatch`` /
``re.match`` / ``re.search`` semantics are honored directly — no pattern
wrapping (for the subprocess dialects whose helpers are bare search runners the
adapter wraps the pattern instead; py_re's whole-string/prefix/search intent is
the engine's native call).

Usage:
  match.py match <call_kind> <pattern> <flags>   # stdin → verdict on stdout
  match.py batch <call_kind> <pattern> <flags>   # NUL-framed witnesses

Exit codes (helper contract shared with the other match helpers):
  0 = accepted, 1 = rejected, 2 = engine/compile error, 3 = runner unavailable.

Batch framing: witnesses are NUL-delimited on stdin; each witness is escaped
byte-wise (0x00 → ``\\0``, ``\\`` → ``\\\\``) before joining so witnesses
containing NUL round-trip exactly (raw NUL never appears inside an escaped
segment, so NUL is an unambiguous delimiter). The helper emits one
``<index>:<verdict>`` line per witness on stdout (0 rejected / 1 accepted).
"""

from __future__ import annotations

import re
import sys

_FLAG_BITS = {
    "i": re.IGNORECASE,
    "m": re.MULTILINE,
    "s": re.DOTALL,
    "x": re.VERBOSE,
    "a": re.ASCII,
    "u": re.UNICODE,
}


def _compile(pattern: str, flags: str):
    bits = 0
    for ch in flags or "":
        if ch not in _FLAG_BITS:
            raise ValueError(f"unknown py_re flag {ch!r}")
        bits |= _FLAG_BITS[ch]
    return re.compile(pattern, bits)


def _match(rx, call_kind: str, data: str) -> bool:
    if call_kind == "fullmatch":
        return rx.fullmatch(data) is not None
    if call_kind == "match":
        return rx.match(data) is not None
    return rx.search(data) is not None  # search / exec


def _decode_frame(raw: bytes) -> str:
    out = bytearray()
    i = 0
    n = len(raw)
    while i < n:
        b = raw[i]
        if b == 0x5C:  # backslash escape
            nxt = raw[i + 1] if i + 1 < n else None
            if nxt == 0x5C:
                out.append(0x5C)
                i += 2
                continue
            if nxt == 0x30:  # '0'
                out.append(0x00)
                i += 2
                continue
            out.append(b)
            i += 1
            continue
        out.append(b)
        i += 1
    return bytes(out).decode("utf-8")


def _read_frames() -> list[str]:
    raw = sys.stdin.buffer.read()
    frames = raw.split(b"\x00")
    if frames and frames[-1] == b"":
        frames.pop()
    return [_decode_frame(f) for f in frames]


def cmd_match(call_kind: str, pattern: str, flags: str) -> int:
    try:
        data = sys.stdin.buffer.read().decode("utf-8")
    except UnicodeDecodeError as exc:
        print(f"engine-error: {exc}", file=sys.stderr)
        return 2
    try:
        rx = _compile(pattern, flags)
        accepted = _match(rx, call_kind, data)
    except (re.error, ValueError) as exc:
        print(f"engine-error: {exc}", file=sys.stderr)
        return 2
    print("accepted" if accepted else "rejected")
    return 0 if accepted else 1


def cmd_batch(call_kind: str, pattern: str, flags: str) -> int:
    witnesses = _read_frames()
    try:
        rx = _compile(pattern, flags)
    except (re.error, ValueError) as exc:
        print(f"engine-error: {exc}", file=sys.stderr)
        return 2
    for i, w in enumerate(witnesses):
        try:
            accepted = _match(rx, call_kind, w)
        except re.error as exc:  # engine error mid-batch aborts the session
            print(f"engine-error: {exc}", file=sys.stderr)
            return 2
        print(f"{i}:{1 if accepted else 0}")
    return 0


def main(argv) -> int:
    if len(argv) < 3 or argv[0] not in ("match", "--batch"):
        print(
            "usage: match.py match|batch <call_kind> <pattern> [flags]",
            file=sys.stderr,
        )
        return 2
    cmd, call_kind, pattern = argv[0], argv[1], argv[2]
    flags = argv[3] if len(argv) > 3 else ""
    if cmd == "match":
        return cmd_match(call_kind, pattern, flags)
    return cmd_batch(call_kind, pattern, flags)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
