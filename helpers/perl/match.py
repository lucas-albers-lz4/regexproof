#!/usr/bin/env python3
"""Perl ground-truth helper — parse + replay via system perl (never Python re).

Usage:
  match.py version
  match.py parse <pattern>
  match.py match <pattern> <flags>   # stdin → exit 0 on match

Exit 0 = ok/match; 1 = parse fail / no-match; 2 = perl unavailable / version mismatch.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys

# Pin: major.minor must match installed perl (Wave-3 hard pre-gate).
# Local/CI currently ship 5.38.x; prefix gate accepts 5.38+ / 5.40+.
PERL_VERSION = "5.38.2"
PERL_VERSION_PREFIX = "5."


def _perl_bin() -> str | None:
    return shutil.which("perl")


def _perl_version_string(bin_: str) -> str | None:
    proc = subprocess.run(
        [bin_, "-e", "print $^V"],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return None
    # $^V prints v5.38.2
    raw = (proc.stdout or "").strip().lstrip("v")
    return raw or None


def _version_ok(ver: str) -> bool:
    if not ver.startswith(PERL_VERSION_PREFIX):
        return False
    # Require 5.38+ (plan assumed 5.40.1; box/CI may be 5.38.x).
    m = re.match(r"^(\d+)\.(\d+)", ver)
    if not m:
        return False
    major, minor = int(m.group(1)), int(m.group(2))
    return (major, minor) >= (5, 38)


def version() -> int:
    bin_ = _perl_bin()
    if not bin_:
        print(json.dumps({"ok": False, "error": "perl-helper-unavailable", "helper": "none"}))
        return 2
    ver = _perl_version_string(bin_)
    if ver is None or not _version_ok(ver):
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": "perl-version-mismatch",
                    "helper": bin_,
                    "version": ver,
                    "want_prefix": PERL_VERSION_PREFIX,
                    "pin": PERL_VERSION,
                }
            )
        )
        return 2
    print(
        json.dumps(
            {
                "ok": True,
                "helper": bin_,
                "version": ver,
                "pin": PERL_VERSION,
            }
        )
    )
    return 0


def _flag_prefix(flags: str) -> str:
    """Map helper flags string to a leading (?…) group perl understands."""
    wanted = "".join(c for c in "imsx" if c in (flags or ""))
    return f"(?{wanted})" if wanted else ""


def parse(pattern: str) -> int:
    bin_ = _perl_bin()
    if not bin_:
        print(
            json.dumps(
                {
                    "ok": False,
                    "unencodable_reason": "perl-helper-unavailable",
                    "helper": "none",
                }
            )
        )
        return 2
    ver = _perl_version_string(bin_)
    if ver is None or not _version_ok(ver):
        print(
            json.dumps(
                {
                    "ok": False,
                    "unencodable_reason": "perl-version-mismatch",
                    "helper": bin_,
                    "version": ver,
                }
            )
        )
        return 2
    # Compile via qr//; escape nothing — pattern is operator-supplied.
    script = (
        "use strict; use warnings;\n"
        "my $p = $ARGV[0];\n"
        "eval { qr/$p/; 1 } or do { print STDERR $@; exit 1 };\n"
        "exit 0;\n"
    )
    proc = subprocess.run(
        [bin_, "-e", script, "--", pattern],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode == 0:
        print(json.dumps({"ok": True, "helper": "perl", "version": ver}))
        return 0
    print(
        json.dumps(
            {
                "ok": False,
                "unencodable_reason": "parse-error",
                "error": (proc.stderr or "").strip() or "perl reject",
                "helper": "perl",
            }
        )
    )
    return 1


def match(pattern: str, flags: str, data: str) -> int:
    bin_ = _perl_bin()
    if not bin_:
        print("FATAL: perl missing — refusing Python re fallback", file=sys.stderr)
        return 2
    ver = _perl_version_string(bin_)
    if ver is None or not _version_ok(ver):
        print(
            f"FATAL: perl version {ver!r} fails pin {PERL_VERSION} "
            f"(prefix {PERL_VERSION_PREFIX}) — refusing Python re fallback",
            file=sys.stderr,
        )
        return 2
    prefixed = _flag_prefix(flags) + pattern
    script = (
        "use strict; use warnings;\n"
        "my $p = $ARGV[0];\n"
        "local $/; my $s = <STDIN>;\n"
        "my $re = eval { qr/$p/ };\n"
        "exit 2 if $@ || !defined $re;\n"
        "exit($s =~ /$re/ ? 0 : 1);\n"
    )
    proc = subprocess.run(
        [bin_, "-e", script, "--", prefixed],
        input=data,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode in (0, 1):
        return proc.returncode
    return 2


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: match.py version|parse|match ...", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "version":
        return version()
    if cmd == "parse":
        if len(sys.argv) < 3:
            print("usage: match.py parse <pattern>", file=sys.stderr)
            return 2
        return parse(sys.argv[2])
    if cmd == "match":
        if len(sys.argv) < 3:
            print("usage: match.py match <pattern> [flags]", file=sys.stderr)
            return 2
        pattern = sys.argv[2]
        flags = sys.argv[3] if len(sys.argv) > 3 else ""
        return match(pattern, flags, sys.stdin.read())
    print("unknown command", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
