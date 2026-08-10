#!/usr/bin/env python3
"""Perl ground-truth helper — parse + replay via system perl (never Python re).

Usage:
  match.py version
  match.py parse <pattern>
  match.py match <pattern> <flags>   # stdin → exit 0 on match

Exit 0 = ok/match; 1 = parse fail / no-match; 2 = perl unavailable / version
mismatch; 3 = pattern compile failure at match time.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Checkout bootstrap so helper shares reject markers with compile_perl (#113).
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from regexproof.compiler.reject_markers import PERL_REJECT_MARKERS  # noqa: E402

# Pin: major.minor must match installed perl (Wave-3 hard pre-gate).
# Local/CI currently ship 5.38.x; prefix gate accepts 5.38+.
PERL_VERSION = "5.38.2"
PERL_VERSION_PREFIX = "5."
HELPER_TIMEOUT_S = 30


def _reject_unencodable(pattern: str) -> str | None:
    for marker, reason in PERL_REJECT_MARKERS:
        if marker in pattern:
            return reason
    if re.search(r"(?<!\\)\\[1-9]", pattern):
        return "backref"
    return None

# Shared Perl fragment: load pattern from a file (NUL-safe) and compile with
# double-interpolation guards so `$`/`@` in the pattern are not re-scanned as
# Perl variables (Bugbot finding on qr/$p/).
_PERL_LOAD_AND_COMPILE = r"""
use strict;
use warnings;
sub load_pat {
  my ($path) = @_;
  open my $fh, '<:raw', $path or die "open: $!";
  local $/; my $p = <$fh>;
  close $fh;
  return $p // '';
}
sub protect {
  # Escape $/@ that would interpolate as variables; leave end-anchor $ alone.
  my ($s) = @_;
  $s =~ s/(?<!\\)\$(?=[\w\{])/\\\$/g;
  $s =~ s/(?<!\\)\@/\\@/g;
  return $s;
}
sub compile_re {
  my ($pat, $flag_prefix) = @_;
  my $safe = protect($flag_prefix . $pat);
  my $re = eval { qr/(?^:$safe)/ };
  return ($re, $@);
}
"""


def _perl_bin() -> str | None:
    return shutil.which("perl")


def _perl_version_string(bin_: str) -> str | None:
    proc = subprocess.run(
        [bin_, "-e", "print $^V"],
        capture_output=True,
        text=True,
        check=False,
        timeout=HELPER_TIMEOUT_S,
    )
    if proc.returncode != 0:
        return None
    raw = (proc.stdout or "").strip().lstrip("v")
    return raw or None


def _version_ok(ver: str) -> bool:
    if not ver.startswith(PERL_VERSION_PREFIX):
        return False
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
    wanted = "".join(c for c in "imsx" if c in (flags or ""))
    return f"(?{wanted})" if wanted else ""


def _write_pat_file(pattern: str) -> Path:
    fd, name = tempfile.mkstemp(prefix="rp-perl-pat-", suffix=".pat")
    os.close(fd)
    path = Path(name)
    path.write_bytes(pattern.encode("utf-8"))
    return path


def parse(pattern: str) -> int:
    reason = _reject_unencodable(pattern)
    if reason:
        print(
            json.dumps(
                {"ok": False, "unencodable_reason": reason, "helper": "perl"}
            )
        )
        return 1
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
    pat_path = _write_pat_file(pattern)
    try:
        script = (
            _PERL_LOAD_AND_COMPILE
            + r"""
my $pat = load_pat($ARGV[0]);
my ($re, $err) = compile_re($pat, '');
if ($err || !defined $re) {
  print STDERR $err // 'compile failed';
  exit 1;
}
exit 0;
"""
        )
        proc = subprocess.run(
            [bin_, "-e", script, "--", str(pat_path)],
            capture_output=True,
            text=True,
            check=False,
            timeout=HELPER_TIMEOUT_S,
        )
    finally:
        pat_path.unlink(missing_ok=True)
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
    pat_path = _write_pat_file(pattern)
    try:
        prefix = _flag_prefix(flags)
        script = (
            _PERL_LOAD_AND_COMPILE
            + r"""
my $pat = load_pat($ARGV[0]);
my $flag_prefix = $ARGV[1] // '';
my ($re, $err) = compile_re($pat, $flag_prefix);
if ($err || !defined $re) {
  print STDERR $err // 'compile failed';
  exit 3;
}
local $/; my $s = <STDIN>;
$s = '' unless defined $s;
exit($s =~ /$re/ ? 0 : 1);
"""
        )
        proc = subprocess.run(
            [bin_, "-e", script, "--", str(pat_path), prefix],
            input=data,
            capture_output=True,
            text=True,
            check=False,
            timeout=HELPER_TIMEOUT_S,
        )
    finally:
        pat_path.unlink(missing_ok=True)
    if proc.returncode in (0, 1, 3):
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
