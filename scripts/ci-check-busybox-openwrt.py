"""BusyBox is the OpenWrt product engine (conversion wave P4).

Unlike ``ci-check-busybox-sed.py`` (GNU∩BusyBox agreement, sed-only,
busybox-absent still PASSes if GNU reproduced), this checker:

- hard-fails when busybox is absent
- replays SAT OW-packages witnesses on BusyBox; GNU is logged
- does not require GNU/BusyBox agreement
- expected-UNSAT shape-3 (wan_mark hex, expand_ipv6 nibble,
  mosquitto UCI quote-free) is differential fuzz, not witness replay

Run from the golden job after busybox is installed. The proof job must
also install busybox because OW-packages stays on ``z3-verify.py --all``.
"""

from __future__ import annotations

import shutil
import string
import subprocess
import sys

from regexproof.harness.openwrt_packages import (
    FAMILY,
    OW_VERDICT_LOG,
    EXPAND_IPV6_SED,
    MOSQ_SED,
    WAN_MARK_SED,
    aliyun_ground_truth,
    cloudflare_ground_truth,
    transip_ground_truth,
)
from regexproof.harness.core import REGISTRY


def _require_busybox() -> None:
    if not shutil.which("busybox"):
        print(
            "error: busybox absent — OpenWrt product engine is required",
            file=sys.stderr,
        )
        raise SystemExit(2)


def _fuzz_wan_mark(n: int = 32, seed: int = 42) -> int:
    """Hex payloads must round-trip through BusyBox sed (identity capture)."""
    import random

    rng = random.Random(seed)
    alphabet = string.hexdigits
    for i in range(n):
        w = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 8)))
        stream = f"option wan_mark '0x{w}'"
        proc = subprocess.run(
            ["busybox", "sed", WAN_MARK_SED],
            input=stream,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        got = proc.stdout.rstrip("\n")
        want = f"option wan_mark '{w}'"
        if got != want:
            print(
                f"error: wan_mark fuzz mismatch i={i} w={w!r} got={got!r} want={want!r}",
                file=sys.stderr,
            )
            return 2
    print(f"wan_mark differential fuzz: {n} hex payloads identity-ok on BusyBox")
    return 0


def _fuzz_expand_ipv6(n: int = 32, seed: int = 42) -> int:
    """3-hex nibbles must round-trip through BusyBox sed (pad with 0)."""
    import random

    rng = random.Random(seed)
    alphabet = "0123456789abcdef"
    for i in range(n):
        w = "".join(rng.choice(alphabet) for _ in range(3))
        stream = f":{w}:"
        proc = subprocess.run(
            ["busybox", "sed", "-e", EXPAND_IPV6_SED],
            input=stream,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        got = proc.stdout.rstrip("\n")
        want = f":0{w}:"
        if got != want:
            print(
                f"error: expand_ipv6 fuzz mismatch i={i} w={w!r} got={got!r} want={want!r}",
                file=sys.stderr,
            )
            return 2
    print(f"expand_ipv6 differential fuzz: {n} 3-hex nibbles identity-ok on BusyBox")
    return 0


def _fuzz_mosquitto(n: int = 32, seed: int = 42) -> int:
    """Quote-free UCI auth_opt values must round-trip through BusyBox sed."""
    import random
    import string as _string

    rng = random.Random(seed)
    alphabet = _string.ascii_letters + _string.digits + "_-"
    for i in range(n):
        w = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 16)))
        stream = f"CONFIG_owrt_auth_opt_foo='{w}'"
        proc = subprocess.run(
            ["busybox", "sed", MOSQ_SED],
            input=stream,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        got = proc.stdout.rstrip("\n")
        want = f"auth_opt_foo {w}"
        if got != want:
            print(
                f"error: mosquitto fuzz mismatch i={i} w={w!r} got={got!r} want={want!r}",
                file=sys.stderr,
            )
            return 2
    print(f"mosquitto differential fuzz: {n} quote-free values identity-ok on BusyBox")
    return 0


def main() -> int:
    _require_busybox()
    names = [n for n, e in REGISTRY.items() if e.get("family") == FAMILY]
    if not names:
        print("error: family OW-packages missing from REGISTRY", file=sys.stderr)
        return 2
    print("OW-packages registry:", ", ".join(sorted(names)))
    ok = transip_ground_truth({"v": 'x"'})
    log = OW_VERDICT_LOG.get("OW-packages-transip-token-truncation") or {}
    print("transip busybox SAT replay:", {k: log.get(k) for k in ("gnu", "busybox", "busybox_absent")})
    if log.get("busybox_absent") is True:
        print("error: busybox_absent during SAT replay", file=sys.stderr)
        return 2
    if not ok or log.get("busybox") is not True:
        print("error: BusyBox did not reproduce TransIP truncation", log, file=sys.stderr)
        return 2
    if log.get("gnu") is not True:
        print("note: GNU sed disagreed (logged, not a fail):", log)
    ok_cf = cloudflare_ground_truth({"v": 'x"'})
    log_cf = OW_VERDICT_LOG.get("OW-packages-cloudflare-content-truncation") or {}
    print(
        "cloudflare busybox SAT replay:",
        {k: log_cf.get(k) for k in ("gnu", "busybox", "busybox_absent")},
    )
    if log_cf.get("busybox_absent") is True:
        print("error: busybox_absent during Cloudflare SAT replay", file=sys.stderr)
        return 2
    if not ok_cf or log_cf.get("busybox") is not True:
        print("error: BusyBox did not reproduce Cloudflare truncation", log_cf, file=sys.stderr)
        return 2
    if log_cf.get("gnu") is not True:
        print("note: GNU grep disagreed (logged, not a fail):", log_cf)
    ok_ali = aliyun_ground_truth({"v": "ab&c"})
    log_ali = OW_VERDICT_LOG.get("OW-packages-aliyun-recordid-truncation") or {}
    print(
        "aliyun busybox SAT replay:",
        {k: log_ali.get(k) for k in ("gnu", "busybox", "busybox_absent")},
    )
    if log_ali.get("busybox_absent") is True:
        print("error: busybox_absent during Aliyun SAT replay", file=sys.stderr)
        return 2
    if not ok_ali or log_ali.get("busybox") is not True:
        print("error: BusyBox did not reproduce Aliyun RecordId truncation", log_ali, file=sys.stderr)
        return 2
    if log_ali.get("gnu") is not True:
        print("note: GNU grep disagreed (logged, not a fail):", log_ali)
    wan = _fuzz_wan_mark()
    if wan != 0:
        return wan
    exp = _fuzz_expand_ipv6()
    if exp != 0:
        return exp
    return _fuzz_mosquitto()


if __name__ == "__main__":
    raise SystemExit(main())
