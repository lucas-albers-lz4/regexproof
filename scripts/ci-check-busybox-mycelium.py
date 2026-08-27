#!/usr/bin/env python3
"""BusyBox is the mycelium posix-shell product engine (conversion wave 1).

Unlike ``ci-check-busybox-sed.py`` (GNU∩BusyBox agreement), this checker:

- hard-fails when busybox is absent
- expected-UNSAT shape-3 (AllowedIPs last-octet capture) is differential
  fuzz, not witness replay
- search sites replay as BusyBox ``grep -E``; the last-octet substitution
  replays as BusyBox ``sed -E`` (as at the call site — not sed-for-bash-``=~``)
- BusyBox alone decides pass/fail (GNU is not consulted)

Run from the golden job after busybox is installed.
"""

from __future__ import annotations

import random
import shutil
import subprocess
import sys

from regexproof.harness.core import REGISTRY
from regexproof.harness.mycelium import (
    ALPN_H2_GREP,
    AWG_DIALECT_GREP,
    AWG_LAST_OCTET_SED,
    FAMILY,
    SSH_KEY_GREP,
)


def _require_busybox() -> None:
    if not shutil.which("busybox"):
        print(
            "error: busybox absent — mycelium product engine is required",
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


def _busybox_sed(script: str, stream: str) -> str:
    proc = subprocess.run(
        ["busybox", "sed", "-E", script],
        input=stream,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"sed -E failed rc={proc.returncode} err={proc.stderr!r}")
    return proc.stdout.rstrip("\n")


def _fuzz_last_octet(n: int = 32, seed: int = 42) -> int:
    """Replay ``sed -E`` last-octet capture on BusyBox (awg-issue enrolment)."""
    rng = random.Random(seed)
    for i in range(n):
        a = rng.randint(0, 255)
        b = rng.randint(0, 255)
        c = rng.randint(0, 255)
        octet = rng.randint(1, 239)
        mask = rng.choice((8, 16, 24, 32))
        stream = f"{a}.{b}.{c}.{octet}/{mask}"
        got = _busybox_sed(AWG_LAST_OCTET_SED, stream)
        if got != str(octet):
            print(
                f"error: last-octet fuzz mismatch i={i} stream={stream!r} "
                f"want={octet!r} got={got!r}",
                file=sys.stderr,
            )
            return 2
    print(
        f"last-octet differential fuzz: {n} IPv4 CIDRs identity-ok on BusyBox sed -E"
    )
    return 0


def _spot_alphabets() -> int:
    if not _busybox_grep_q(SSH_KEY_GREP, "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5"):
        print("error: ssh key prefix reject ssh-ed25519", file=sys.stderr)
        return 1
    if _busybox_grep_q(SSH_KEY_GREP, ";ssh-ed25519 AAAAC3"):
        print("error: ssh key prefix accept leading semicolon", file=sys.stderr)
        return 1
    if not _busybox_grep_q(AWG_DIALECT_GREP, "Jc = 4"):
        print("error: dialect key reject Jc = 4", file=sys.stderr)
        return 1
    if _busybox_grep_q(AWG_DIALECT_GREP, "Jc; = 4"):
        print("error: dialect key accept semicolon in key", file=sys.stderr)
        return 1
    if not _busybox_grep_q(ALPN_H2_GREP, "ALPN protocol: h2"):
        print("error: ALPN h2 reject good line", file=sys.stderr)
        return 1
    if _busybox_grep_q(ALPN_H2_GREP, "ALPN protocol: h2;x"):
        print("error: ALPN h2 accept semicolon trailer", file=sys.stderr)
        return 1
    print("MY-mycelium alphabet spot-checks: ok on BusyBox grep -E")
    return 0


def main() -> int:
    _require_busybox()
    names = [n for n, e in REGISTRY.items() if e.get("family") == FAMILY]
    if not names:
        print("error: family MY-mycelium missing from REGISTRY", file=sys.stderr)
        return 1
    print("MY-mycelium registry:", ", ".join(sorted(names)))
    rc = _spot_alphabets()
    if rc:
        return rc
    return _fuzz_last_octet()


if __name__ == "__main__":
    raise SystemExit(main())
