"""OpenWrt LuCI conversion-wave properties (family ``OW-luci``).

Wave 1: adblock tcpdump-filter alphabet, validation ``netdevname``, firewall
mark alphabet, dockerman publish-host capture (colon-free). Product engine is
Node ``RegExp`` via ``helpers/ecma/match.mjs`` (absence is a hard fail for
replay/fuzz). Importing this module registers into ``REGISTRY``.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from z3 import (
    Concat,
    If,
    InRe,
    IndexOf,
    Length,
    Range,
    Re,
    Star,
    String,
    StringVal,
    SubString,
    Union,
)

from regexproof.harness.core import prop

FAMILY = "OW-luci"
ROOT = Path(__file__).resolve().parents[2]
MATCH_MJS = ROOT / "helpers" / "ecma" / "match.mjs"

# adblock overview.js:870 — tcpdump report filter expression charset.
_ADBLOCK_FILTER_CHARS = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    " \t.:/()[]!&|<>=+*%\\-"
)
ADBLOCK_FILTER_CHAR = Union(*[Re(ch) for ch in _ADBLOCK_FILTER_CHARS])

# firewall.js:335 — mark value/mask digits (hex or decimal atom).
MARK_DIGIT = Union(Range("0", "9"), Range("a", "f"), Range("A", "F"))

# validation.js:1006 — netdevname ``[^:/%\s]`` over ASCII 0x01–0x7f.
# Semicolon is *in* this alphabet (JS allows it); wave-1 asks that as a
# counterexample_finder, not an UNSAT disjointness claim.
_NETDEV_FORBIDDEN = set(":/% \t\n\r\v\f")
NETDEV_CHAR = Union(
    *[
        Re(chr(i))
        for i in range(1, 128)
        if chr(i) not in _NETDEV_FORBIDDEN
    ]
)

# dockerman publish host field ``([^:]+)`` — colon-free ASCII (two ranges).
HOST_NO_COLON = Union(Range("\x01", "9"), Range(";", "\x7f"))

DOCKERMAN_PUBLISH = r"^([^:]+):(\d+):(\d+)\/(tcp|udp)$"
NETDEVNAME_PAT = r"^[^:/%\s]{1,15}$"


def _require_node() -> None:
    if not shutil.which("node"):
        raise RuntimeError("node_absent")
    if not MATCH_MJS.is_file():
        raise RuntimeError("match.mjs_absent")


def node_fullmatch(pattern: str, witness: str, flags: str = "") -> bool:
    """Replay *pattern* on *witness* via ``helpers/ecma/match.mjs`` (``.test``)."""
    _require_node()
    try:
        proc = subprocess.run(
            ["node", str(MATCH_MJS), pattern, flags],
            input=witness,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError("node replay timed out") from exc
    if proc.returncode == 0:
        return True
    if proc.returncode == 1:
        return False
    raise RuntimeError(f"node match.mjs rc={proc.returncode}: {proc.stderr.strip()}")


def netdevname_semicolon_ground_truth(witness: dict) -> bool:
    """Node must accept a single ``;`` as a netdevname (alphabet admits it)."""
    c = witness.get("c")
    if c != ";":
        return False
    try:
        return node_fullmatch(NETDEVNAME_PAT, c)
    except RuntimeError:
        return False


def _alphabet_no(ch: str, name: str, alphabet, site: str, guarantee: str,
                 input_source: str, trust: str, declared_domain: str):
    @prop(
        name,
        f"{guarantee} (length-independent single-char)",
        expect_unsat=True,
        family=FAMILY,
        input_domain="ascii",
        call_kind="search",
        contract={
            "schema_version": "1",
            "site": site,
            "guarantee": guarantee,
            "input_source": input_source,
            "trust": trust,
            "declared_domain": declared_domain,
            "provenance": "human",
        },
    )
    def _fn(ch=ch, alphabet=alphabet):
        c = String("c")
        return [InRe(c, alphabet), Length(c) == 1], c == StringVal(ch)

    return _fn


_alphabet_no(
    ";",
    "OW-luci-adblock-tcpdump-filter-no-semicolon",
    ADBLOCK_FILTER_CHAR,
    "applications/luci-app-adblock/htdocs/luci-static/resources/view/"
    "adblock/overview.js:870:adb_repfilter",
    "accepted tcpdump report-filter chars contain no semicolon",
    "LuCI adblock Report Filter form value (config → tcpdump -f)",
    "config",
    "adblock tcpdump-filter alphabet "
    r"[a-zA-Z0-9 \t.:/()[\]!&|<>=+*%\\-], single char, ASCII",
)

_alphabet_no(
    ";",
    "OW-luci-firewall-mark-no-semicolon",
    MARK_DIGIT,
    "applications/luci-app-firewall/htdocs/luci-static/resources/tools/"
    "firewall.js:335:mark",
    "accepted firewall mark digit/hex chars contain no semicolon",
    "LuCI firewall mark / set_mark / set_xmark form value (config → fw4)",
    "config",
    "firewall mark atom alphabet [0-9a-fA-F], single char, ASCII",
)


@prop(
    "OW-luci-netdevname-semicolon-admitted",
    "exists a single char in the netdevname alphabet [^:/%\\s] that is ';' "
    "— LuCI validation.js admits semicolon in network device names",
    expect_unsat=False,
    ground_truth=netdevname_semicolon_ground_truth,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract={
        "schema_version": "1",
        "site": "modules/luci-base/htdocs/luci-static/resources/validation.js:1006:netdevname",
        "guarantee": (
            "netdevname alphabet admits ';' (shell metachar reaches UCI / netifd "
            "if an operator pastes it)"
        ),
        "input_source": "LuCI form netdevname validator (config → UCI / netifd)",
        "trust": "config",
        "declared_domain": "netdevname alphabet [^:/%\\s] over ASCII 0x01-0x7f, single char",
        "provenance": "human",
    },
)
def ow_netdevname_semicolon():
    c = String("c")
    return [InRe(c, NETDEV_CHAR), Length(c) == 1], c == StringVal(";")


@prop(
    "OW-luci-dockerman-publish-host-capture",
    "dockerman publish host field (no colon) is captured in full by "
    r"^([^:]+):(\d+):(\d+)/(tcp|udp)$ — proven for len 1..16 colon-free ASCII",
    expect_unsat=True,
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract={
        "schema_version": "1",
        "site": (
            "applications/luci-app-dockerman/htdocs/luci-static/resources/view/"
            "dockerman/container_new.js:836:PortBindings"
        ),
        "guarantee": (
            "colon-free publish host tokens are captured in full into Docker "
            "PortBindings HostIp"
        ),
        "input_source": "LuCI dockerman container publish form (config → Docker API)",
        "trust": "config",
        "declared_domain": "ASCII 0x01-0x7f minus U+003A, len 1..16, Node RegExp",
        "provenance": "human",
    },
)
def ow_dockerman_publish_host():
    # Mirror of group 1 under ``([^:]+)``: first colon truncates; the declared
    # domain is colon-free so IndexOf == -1 and the extract equals ``w``.
    w = String("w")
    q = IndexOf(w, StringVal(":"), 0)
    cap = If(q < 0, w, SubString(w, 0, q))
    return [
        InRe(w, Concat(HOST_NO_COLON, Star(HOST_NO_COLON))),
        Length(w) >= 1,
        Length(w) <= 16,
    ], cap != w


@prop(
    "OW-luci-mutated-adblock-filter-semicolon",
    "MUTATION GUARD: if the adblock tcpdump-filter alphabet admits ';', "
    "adblock-tcpdump-filter-no-semicolon MUST flip UNSAT->SAT",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def ow_adblock_filter_mutated():
    c = String("c")
    weak = Union(ADBLOCK_FILTER_CHAR, Re(";"))
    return [InRe(c, weak), Length(c) == 1], c == StringVal(";")
