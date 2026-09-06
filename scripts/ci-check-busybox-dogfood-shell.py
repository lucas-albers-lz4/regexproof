#!/usr/bin/env python3
"""BusyBox is the dogfood_shell normalize product engine (funnel #615 wave 1).

Unlike ``ci-check-busybox-sed.py`` (GNU∩BusyBox agreement), this checker:

- hard-fails when busybox is absent
- replays the EXACT shipped script ``s/[[:space:]:]*$//`` (not a paraphrase)
  through BusyBox ``sed``: idempotency spot-checks + fixpoint spot-checks
- replays the weakened ``[[:space:]]*`` script to prove the mutation-guard
  witnesses are real bug witnesses for the 2026-08 regression class
- differential-fuzzes the Z3 mirror (``normalize_mirror``) against BusyBox
  ``sed`` so mirror ≡ product engine is proved by execution
- BusyBox alone decides pass/fail (GNU is not consulted)

Run from the golden job after busybox is installed.
"""

from __future__ import annotations

import random
import shutil
import string
import subprocess
import sys
from pathlib import Path

# Checkout bootstrap (match scripts/z3-verify.py) — import the working
# tree, never a stale editable install pointing at another worktree.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from regexproof.harness.dogfood_shell import (
    FAMILY,
    SED_SCRIPT,
    normalize_mirror,
)

WEAK_SCRIPT = "s/[[:space:]]*$//"
SEED = 615
N_RANDOM = 300


def _require_busybox() -> None:
    if not shutil.which("busybox"):
        print(
            "error: busybox absent — dogfood_shell product engine is required",
            file=sys.stderr,
        )
        raise SystemExit(2)


def _busybox_sed(script: str, stream: str) -> str:
    proc = subprocess.run(
        ["busybox", "sed", script],
        input=stream.encode("utf-8"),
        capture_output=True,
        timeout=30,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"busybox sed failed rc={proc.returncode}")
    out = proc.stdout.decode("utf-8")
    if out.endswith("\n"):
        out = out[:-1]
    return out


def _spot_fixpoint() -> int:
    cases = {
        "zz::": "zz",
        "zz:": "zz",
        "fwlive-ssh ": "fwlive-ssh",
        "a\t: \t:": "a",
        "plain": "plain",
        "": "",
        ":": "",
        "a:b": "a:b",
    }
    for given, want in cases.items():
        got = _busybox_sed(SED_SCRIPT, given)
        if got != want:
            print(
                f"error: fixpoint replay {given!r} -> {got!r}, want {want!r}",
                file=sys.stderr,
            )
            return 1
        if _busybox_sed(SED_SCRIPT, got) != got:
            print(
                f"error: not a fixpoint: {got!r} strips further",
                file=sys.stderr,
            )
            return 1
    return 0


def _spot_regression_class() -> int:
    # The exact 2026-08 regression: colon dropped from the strip class.
    # The weakened script MUST leave the colon (guard witness is real).
    if _busybox_sed(WEAK_SCRIPT, "zz:") != "zz:":
        print(
            "error: weakened script stripped the colon — "
            "regression witness does not replay",
            file=sys.stderr,
        )
        return 1
    if _busybox_sed(WEAK_SCRIPT, "zz::") != "zz::":
        print(
            "error: weakened script touched colons "
            "(zz:: should stay zz:: — colon is outside [[:space:]])",
            file=sys.stderr,
        )
        return 1
    return 0


def _fuzz_mirror(n: int = N_RANDOM, seed: int = SEED) -> int:
    rng = random.Random(seed)
    alphabet = (
        string.ascii_letters + string.digits + " \t:.-_/" + "\r\x0c\x0b"
    )
    for _ in range(n):
        length = rng.randint(0, 12)
        stream = "".join(rng.choice(alphabet) for _ in range(length))
        want = normalize_mirror(stream)
        got = _busybox_sed(SED_SCRIPT, stream)
        if got != want:
            print(
                f"error: mirror divergence on {stream!r}: "
                f"sed={got!r} mirror={want!r}",
                file=sys.stderr,
            )
            return 1
    # Exhaustive short strings over the load-bearing alphabet.
    tiny = ["a", ":", " ", "\t"]
    stack = [""]
    checked = 0
    while stack:
        prefix = stack.pop()
        if _busybox_sed(SED_SCRIPT, prefix) != normalize_mirror(prefix):
            print(
                f"error: mirror divergence on {prefix!r}",
                file=sys.stderr,
            )
            return 1
        checked += 1
        if len(prefix) < 3:
            stack.extend(prefix + c for c in tiny)
    print(f"mirror ≡ busybox sed on {n} random + {checked} exhaustive inputs")
    return 0


def main() -> int:
    _require_busybox()
    for check in (_spot_fixpoint, _spot_regression_class, _fuzz_mirror):
        if rc := check():
            return rc
    print(f"{FAMILY} BusyBox sed replay: idempotent fixpoint holds")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
