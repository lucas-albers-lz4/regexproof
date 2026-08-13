#!/usr/bin/env python3
"""YARA ground-truth helper — temp-file replay (never stdin; NUL-safe).

Usage:
  python helpers/yara/match.py compile <rule.yar>
  python helpers/yara/match.py match <rule.yar> <sample>
  python helpers/yara/match.py version

Exit 0 = ok/match; 1 = no-match; 2 = compile/scan error (invalid rule);
3 = yara unavailable (helper contract — a compile failure is never
misreported as a rejection, finding 5).
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HELPER_TIMEOUT_S = 30


def _yara_bin() -> str | None:
    return shutil.which("yara")


def version() -> int:
    bin_ = _yara_bin()
    if not bin_:
        print(json.dumps({"ok": False, "error": "yara-helper-unavailable"}))
        return 2
    proc = subprocess.run(
        [bin_, "-v"],
        capture_output=True,
        text=True,
        check=False,
        timeout=HELPER_TIMEOUT_S,
    )
    ver = (proc.stdout or proc.stderr or "").strip().splitlines()[0] if proc.returncode == 0 else ""
    print(json.dumps({"ok": proc.returncode == 0, "helper": bin_, "version": ver}))
    return 0 if proc.returncode == 0 else 2


def compile_rule(rule_path: Path) -> int:
    """Compile via ``yarac`` (``yara -c`` is --count, not compile)."""
    yarac = shutil.which("yarac")
    if not yarac:
        print(json.dumps({"ok": False, "error": "yarac-helper-unavailable"}))
        return 2
    with tempfile.TemporaryDirectory(prefix="yarac-") as tmp:
        out = Path(tmp) / "rules.yac"
        proc = subprocess.run(
            [yarac, str(rule_path), str(out)],
            capture_output=True,
            text=True,
            check=False,
            timeout=HELPER_TIMEOUT_S,
        )
    print(
        json.dumps(
            {
                "ok": proc.returncode == 0,
                "helper": yarac,
                "stderr": (proc.stderr or "").strip(),
            }
        )
    )
    return 0 if proc.returncode == 0 else 1


def match_rule(rule_path: Path, sample_path: Path) -> int:
    bin_ = _yara_bin()
    if not bin_:
        return 3  # helper unavailable — distinct from compile error
    proc = subprocess.run(
        [bin_, str(rule_path), str(sample_path)],
        capture_output=True,
        check=False,
        timeout=HELPER_TIMEOUT_S,
    )
    if proc.returncode != 0:
        # yara exits 1 on scan errors (e.g. the rule failed to compile) —
        # a compile failure is an engine-error, not a no-match.
        return 2
    # yara prints rule names on match; exit 0 always if scan succeeds.
    matched = bool((proc.stdout or b"").strip())
    return 0 if matched else 1


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print("usage: match.py {version|compile|match} ...", file=sys.stderr)
        return 2
    cmd = argv[0]
    if cmd == "version":
        return version()
    if cmd == "compile":
        if len(argv) < 2:
            print("usage: match.py compile <rule.yar>", file=sys.stderr)
            return 2
        return compile_rule(Path(argv[1]))
    if cmd == "match":
        if len(argv) < 3:
            print("usage: match.py match <rule.yar> <sample>", file=sys.stderr)
            return 2
        return match_rule(Path(argv[1]), Path(argv[2]))
    print(f"unknown command: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
