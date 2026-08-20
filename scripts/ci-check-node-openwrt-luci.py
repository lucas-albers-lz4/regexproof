#!/usr/bin/env python3
"""Node RegExp product-engine checks for family ``OW-luci``.

- Absence of ``node`` or ``helpers/ecma/match.mjs`` is a hard fail.
- Expected-UNSAT shape-3 (dockerman publish host) is differential fuzz:
  colon-free hosts formatted as ``host:port:cport/proto`` must match and
  capture group 1 == host.
- Shape-1 alphabets are spot-checked via ``match.mjs`` accept/reject.
"""

from __future__ import annotations

import random
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.harness.openwrt_luci import (  # noqa: E402
    DOCKERMAN_PUBLISH,
    _ADBLOCK_FILTER_CHARS,
    node_fullmatch,
)

ADBLOCK_FILTER = (
    r"^[a-zA-Z0-9 \t.:/()[\]!&|<>=+*%\\-]+$"
)
NETDEVNAME = r"^[^:/%\s]{1,15}$"
FIREWALL_MARK = (
    r"^(0x[0-9a-f]{1,8}|[0-9]{1,10})(?:/(0x[0-9a-f]{1,8}|[0-9]{1,10}))?$"
)


def _require_node() -> None:
    if not shutil.which("node"):
        print("error: node absent (OW-luci product engine)", file=sys.stderr)
        raise SystemExit(2)
    match = ROOT / "helpers" / "ecma" / "match.mjs"
    if not match.is_file():
        print(f"error: missing {match}", file=sys.stderr)
        raise SystemExit(2)


def _node_exec_capture(host: str) -> str | None:
    """Return group-1 host from dockerman publish pattern, or None."""
    witness = f"{host}:8080:80/tcp"
    script = (
        "const fs = require('fs');"
        "const s = fs.readFileSync(0, 'utf8');"
        "const re = /^([^:]+):(\\d+):(\\d+)\\/(tcp|udp)$/;"
        "const m = re.exec(s);"
        "process.stdout.write(m ? m[1] : '');"
        "process.exit(m ? 0 : 1);"
    )
    proc = subprocess.run(
        ["node", "-e", script],
        input=witness,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    if proc.returncode != 0:
        return None
    return proc.stdout


def _fuzz_dockerman(n: int = 48, seed: int = 42) -> int:
    rng = random.Random(seed)
    # Printable ASCII minus colon — argv/stdout round-trip safe for Node.
    alphabet = [chr(i) for i in range(0x20, 0x7F) if chr(i) != ":"]
    for i in range(n):
        length = rng.randint(1, 16)
        host = "".join(rng.choice(alphabet) for _ in range(length))
        if ":" in host:
            print(f"error: fuzz generated colon host={host!r}", file=sys.stderr)
            return 1
        got = _node_exec_capture(host)
        if got != host:
            print(
                f"error: dockerman fuzz mismatch i={i} host={host!r} got={got!r}",
                file=sys.stderr,
            )
            return 1
        if not node_fullmatch(DOCKERMAN_PUBLISH, f"{host}:8080:80/tcp"):
            print(
                f"error: dockerman match.mjs reject i={i} host={host!r}",
                file=sys.stderr,
            )
            return 1
    print(f"dockerman differential fuzz: {n} colon-free hosts identity-ok on Node")
    return 0


def _spot_alphabets() -> int:
    if not node_fullmatch(ADBLOCK_FILTER, "not net 10.0.0.0/24"):
        print("error: adblock filter reject good witness", file=sys.stderr)
        return 1
    if node_fullmatch(ADBLOCK_FILTER, "bad;injection"):
        print("error: adblock filter accept semicolon", file=sys.stderr)
        return 1
    sample = _ADBLOCK_FILTER_CHARS[0]
    if not node_fullmatch(ADBLOCK_FILTER, sample):
        print(f"error: adblock filter reject alphabet char {sample!r}", file=sys.stderr)
        return 1
    if not node_fullmatch(NETDEVNAME, "eth0"):
        print("error: netdevname reject eth0", file=sys.stderr)
        return 1
    # Semicolon is *admitted* by netdevname (SAT finder GT).
    if not node_fullmatch(NETDEVNAME, ";"):
        print("error: netdevname reject semicolon (expected admit)", file=sys.stderr)
        return 1
    if node_fullmatch(NETDEVNAME, "eth:0"):
        print("error: netdevname accept colon", file=sys.stderr)
        return 1
    if not node_fullmatch(FIREWALL_MARK, "0xff", "i"):
        print("error: firewall mark reject 0xff", file=sys.stderr)
        return 1
    if node_fullmatch(FIREWALL_MARK, "0xff;", "i"):
        print("error: firewall mark accept semicolon", file=sys.stderr)
        return 1
    print("OW-luci alphabet spot-checks: ok on Node match.mjs")
    return 0


def main() -> int:
    _require_node()
    from regexproof.harness.core import REGISTRY  # noqa: WPS433

    names = [n for n, e in REGISTRY.items() if e.get("family") == "OW-luci"]
    if not names:
        print("error: family OW-luci missing from REGISTRY", file=sys.stderr)
        return 1
    print("OW-luci registry:", ", ".join(sorted(names)))
    rc = _spot_alphabets()
    if rc:
        return rc
    return _fuzz_dockerman()


if __name__ == "__main__":
    raise SystemExit(main())
