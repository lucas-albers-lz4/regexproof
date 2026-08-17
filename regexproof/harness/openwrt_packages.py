"""OpenWrt packages conversion-wave properties (family ``OW-packages``).

Five human contracts from the frozen rank shortlist plus one mutation
guard. Product engine is BusyBox; GNU is logged and must not decide the
ground-truth bit. Importing this module registers into ``REGISTRY``.
"""

from __future__ import annotations

import shutil
import subprocess

from z3 import (
    Concat,
    Contains,
    If,
    IndexOf,
    InRe,
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

FAMILY = "OW-packages"

HOSTNAME_LABEL = Union(
    Range("a", "z"),
    Range("A", "Z"),
    Range("0", "9"),
    Re("_"),
    Re("-"),
)
BANIP_EXPIRY = Union(
    Range("0", "9"),
    Re("m"),
    Re("s"),
    Re("h"),
    Re("d"),
    Re("w"),
)
HEX_CLS = Union(Range("0", "9"), Range("a", "f"), Range("A", "F"))
HEX_RE = Concat(HEX_CLS, Star(HEX_CLS))

TRANSIP_SED = r's/^.*"token" *: *"\([^"]*\)".*$/\1/'
WAN_MARK_SED = r"s/option wan_mark '0x\(.*\)'/option wan_mark '\1'/"

OW_VERDICT_LOG: dict[str, dict[str, bool]] = {}


def _require_busybox() -> None:
    if not shutil.which("busybox"):
        raise RuntimeError("busybox_absent")


def _run_sed(argv: list[str], stream: str) -> str:
    try:
        proc = subprocess.run(
            argv,
            input=stream,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError("sed replay timed out") from exc
    return proc.stdout.rstrip("\n")


def _sed_engines(pattern: str, stream: str) -> dict[str, str | None]:
    """Run *pattern* on GNU sed and BusyBox sed. BusyBox absence raises."""
    _require_busybox()
    out: dict[str, str | None] = {}
    out["gnu"] = _run_sed(["sed", pattern], stream)
    out["busybox"] = _run_sed(["busybox", "sed", pattern], stream)
    return out


def transip_ground_truth(witness: dict) -> bool:
    """Replay the TransIP token capture on BusyBox sed. GNU is logged only."""
    v = witness["v"]
    stream = '{"token" : "' + v + '"}'
    try:
        caps = _sed_engines(TRANSIP_SED, stream)
    except RuntimeError as exc:
        OW_VERDICT_LOG["OW-packages-transip-token-truncation"] = {
            "busybox_absent": "busybox" in str(exc),
            "gnu": False,
            "busybox": False,
        }
        raise
    gnu_ok = caps["gnu"] != v and v.startswith(caps["gnu"] or "")
    bb_ok = caps["busybox"] != v and v.startswith(caps["busybox"] or "")
    OW_VERDICT_LOG["OW-packages-transip-token-truncation"] = {
        "gnu": gnu_ok,
        "busybox": bb_ok,
        "busybox_absent": False,
        "gnu_capture": caps["gnu"],
        "busybox_capture": caps["busybox"],
    }
    return bb_ok


def _hostname_no(ch: str, name: str, guarantee: str):
    @prop(
        name,
        f"pbr is_hostname label alphabet [A-Za-z0-9_-] contains no {ch!r} "
        "(length-independent single-char)",
        expect_unsat=True,
        family=FAMILY,
        input_domain="ascii",
        call_kind="search",
        contract={
            "schema_version": "1",
            "site": "net/pbr/files/etc/init.d/pbr:354:is_hostname",
            "guarantee": guarantee,
            "input_source": "UCI policy dest / domain token",
            "trust": "config",
            "declared_domain": "hostname label alphabet [A-Za-z0-9_-], single char, ASCII",
            "provenance": "human",
        },
    )
    def _fn(ch=ch):
        c = String("c")
        return [InRe(c, HOSTNAME_LABEL), Length(c) == 1], c == StringVal(ch)

    return _fn


_hostname_no(";", "OW-packages-hostname-no-semicolon",
             "accepted hostname-label chars contain no semicolon")
_hostname_no(" ", "OW-packages-hostname-no-space",
             "accepted hostname-label chars contain no space")


@prop(
    "OW-packages-banip-expiry-no-semicolon",
    "banIP nft expiry alphabet [0-9mshdw] contains no semicolon "
    "(length-independent single-char)",
    expect_unsat=True,
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract={
        "schema_version": "1",
        "site": "net/banip/files/banip-functions.sh:2643:ban_nftexpiry",
        "guarantee": "accepted nft expiry alphabet chars contain no semicolon",
        "input_source": "UCI ban_nftexpiry",
        "trust": "config",
        "declared_domain": "expiry alphabet [0-9mshdw], single char, ASCII",
        "provenance": "human",
    },
)
def ow_banip_expiry():
    c = String("c")
    return [InRe(c, BANIP_EXPIRY), Length(c) == 1], c == StringVal(";")


@prop(
    "OW-packages-transip-token-truncation",
    "exists v: v contains a quote AND BusyBox sed [^\\\"]* token capture "
    "is a strict prefix of v — TransIP JSON token extract",
    expect_unsat=False,
    ground_truth=transip_ground_truth,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    contract={
        "schema_version": "1",
        "site": "net/ddns-scripts/files/usr/lib/ddns/update_transip_nl.sh:96:token",
        "guarantee": "JSON token capture truncates at the first unescaped quote",
        "input_source": "TransIP HTTPS JSON body (WAN)",
        "trust": "untrusted-input",
        "declared_domain": "ASCII JSON string values, NUL-free, BusyBox sed",
        "provenance": "human",
    },
)
def ow_transip():
    v = String("v")
    first_quote = IndexOf(v, StringVal('"'), 0)
    capture = SubString(v, 0, first_quote)
    return [first_quote > 0, capture != v], Contains(v, StringVal('"'))


@prop(
    "OW-packages-wan-mark-hex-capture",
    "UCI wan_mark hex payload (no quote) is captured in full by "
    "s/option wan_mark '0x(.*)'/ — proven for len 1..8 hex",
    expect_unsat=True,
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    contract={
        "schema_version": "1",
        "site": "net/pbr/files/etc/uci-defaults/90-pbr:20:wan_mark",
        "guarantee": "hex-only wan_mark values are captured in full (no quote in domain)",
        "input_source": "UCI option wan_mark",
        "trust": "config",
        "declared_domain": "hex [0-9A-Fa-f]{1,8}, ASCII, quote-free",
        "provenance": "human",
    },
)
def ow_wan_mark():
    w = String("w")
    fq = IndexOf(w, StringVal("'"), 0)
    cap = If(fq < 0, w, SubString(w, 0, fq))
    constraints = [InRe(w, HEX_RE), Length(w) >= 1, Length(w) <= 8]
    return constraints, cap != w


@prop(
    "OW-packages-mutated-hostname-semicolon",
    "MUTATION GUARD: if the hostname label alphabet admits ';', "
    "hostname-no-semicolon MUST flip UNSAT->SAT",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def ow_hostname_mutated():
    c = String("c")
    weak = Union(HOSTNAME_LABEL, Re(";"))
    return [InRe(c, weak), Length(c) == 1], c == StringVal(";")
