"""OpenWrt packages conversion-wave properties (family ``OW-packages``).

Wave 1–2: ten human contracts plus one mutation guard. Wave 3: query-string
``[^&]*``, DNSPod digit RecordId, Mosquitto UCI quote capture, pbr nftset
escape image. Product engine is BusyBox; GNU is logged and must not decide
the ground-truth bit. Importing this module registers into ``REGISTRY``.
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
HEX_LC = Union(Range("0", "9"), Range("a", "f"))
HEX3_LC = Concat(HEX_LC, HEX_LC, HEX_LC)
IPV4_CHAR = Union(Range("0", "9"), Re("."))
HUAWEI_ID_CHAR = Union(Range("a", "z"), Range("0", "9"))
DIGIT_CHAR = Range("0", "9")
# TransIP token values: declared domain is NUL-free ASCII (POSIX/BusyBox).
ASCII_NUL_FREE = Range("\x01", "\x7f")
# pbr extras class at :213 — mapped to ``_``; image is ASCII minus extras.
PBR_EXTRAS_CHARS = set(". ~`!@#$%^&*()+=,<>?;:/\\-")
# pbr nftset grep-E escape class at :1143 — mapped to ``\&``.
PBR_NFTSET_EXTRAS_CHARS = set("/.^$*[\\")
# Mosquitto UCI dump values: no single-quote in the declared domain.
UCI_NO_QUOTE = Union(Range("\x01", "&"), Range("(", "\x7f"))

TRANSIP_SED = r's/^.*"token" *: *"\([^"]*\)".*$/\1/'
WAN_MARK_SED = r"s/option wan_mark '0x\(.*\)'/option wan_mark '\1'/"
EXPAND_IPV6_SED = r"s|:\([0-9a-f]\{3\}\):|:0\1:|g"
CLOUDFLARE_GREP1 = r'"content":\s*"[^"]*'
CLOUDFLARE_GREP2 = r'[^"]*$'
ALIYUN_GREP = r"RecordId=[^&]*"
MOSQ_SED = r"s/^.*_\(auth_opt_.*\)='\(.*\)'/\1 \2/"

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
    if proc.returncode != 0 and not proc.stdout:
        raise RuntimeError(f"sed replay failed rc={proc.returncode}")
    return proc.stdout.rstrip("\n")


def _sed_engines(pattern: str, stream: str) -> dict[str, str | None]:
    """Run *pattern* on GNU sed and BusyBox sed. BusyBox absence raises."""
    _require_busybox()
    out: dict[str, str | None] = {}
    out["gnu"] = _run_sed(["sed", pattern], stream)
    out["busybox"] = _run_sed(["busybox", "sed", pattern], stream)
    return out


def _ascii_minus(forbidden: set[str]):
    """ASCII 0x01–0x7f minus *forbidden* (those chars are mapped away)."""
    parts = []
    start = None
    prev = None
    for i in range(1, 128):
        ch = chr(i)
        if ch in forbidden:
            if start is not None:
                parts.append(Re(start) if start == prev else Range(start, prev))
                start = None
            continue
        if start is None:
            start = ch
        prev = ch
    if start is not None:
        parts.append(Re(start) if start == prev else Range(start, prev))
    acc = parts[0]
    for p in parts[1:]:
        acc = Union(acc, p)
    return acc


SANITIZER_IMAGE = _ascii_minus(PBR_EXTRAS_CHARS)
NFTSET_PASSTHROUGH = _ascii_minus(PBR_NFTSET_EXTRAS_CHARS)


def _run_grep_o(argv: list[str], stream: str) -> str:
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
        raise RuntimeError("grep replay timed out") from exc
    # grep: 0 = match, 1 = no match. Other rc is a hard error.
    if proc.returncode not in (0, 1):
        raise RuntimeError(f"grep replay failed rc={proc.returncode}")
    return proc.stdout


def is_prefix_truncation(capture: str | None, v: str) -> bool:
    """True when *capture* is a non-empty strict prefix of *v*.

    Empty capture is not truncation — ``str.startswith("")`` is always
    true, so a failed grep/sed replay must not count as reproduced.
    """
    if not capture:
        return False
    return capture != v and v.startswith(capture) and len(capture) < len(v)


def _cloudflare_capture(grep_prefix: list[str], stream: str) -> str:
    p1 = _run_grep_o([*grep_prefix, "-o", CLOUDFLARE_GREP1], stream)
    p2 = _run_grep_o([*grep_prefix, "-o", CLOUDFLARE_GREP2], p1)
    lines = p2.splitlines()
    return lines[0] if lines else ""


def _cloudflare_engines(stream: str) -> dict[str, str | None]:
    """Run the Cloudflare content extract on GNU grep and BusyBox grep."""
    _require_busybox()
    return {
        "gnu": _cloudflare_capture(["grep"], stream),
        "busybox": _cloudflare_capture(["busybox", "grep"], stream),
    }


def _prefix_truncation_gt(
    log_key: str,
    stream_fn,
    engines_fn,
):
    """Parameterize Method: BusyBox prefix-truncation GT shared by OW sites."""

    def gt(witness: dict) -> bool:
        v = witness["v"]
        stream = stream_fn(v)
        try:
            caps = engines_fn(stream)
        except RuntimeError as exc:
            OW_VERDICT_LOG[log_key] = {
                "busybox_absent": "busybox" in str(exc),
                "gnu": False,
                "busybox": False,
            }
            return False

        gnu_ok = is_prefix_truncation(caps["gnu"], v)
        bb_ok = is_prefix_truncation(caps["busybox"], v)
        OW_VERDICT_LOG[log_key] = {
            "gnu": gnu_ok,
            "busybox": bb_ok,
            "busybox_absent": False,
            "gnu_capture": caps["gnu"],
            "busybox_capture": caps["busybox"],
        }
        return bb_ok

    return gt


def _aliyun_id(grep_prefix: list[str], stream: str) -> str:
    raw = _run_grep_o([*grep_prefix, "-o", ALIYUN_GREP], stream)
    lines = raw.splitlines()
    if not lines:
        return ""
    line = lines[0]
    if not line.startswith("RecordId="):
        return ""
    return line.split("=", 1)[1]


def _aliyun_engines(stream: str) -> dict[str, str | None]:
    _require_busybox()
    return {
        "gnu": _aliyun_id(["grep"], stream),
        "busybox": _aliyun_id(["busybox", "grep"], stream),
    }


# Parameterize Method: one shared BusyBox prefix-truncation body per site.
transip_ground_truth = _prefix_truncation_gt(
    "OW-packages-transip-token-truncation",
    lambda v: '{"token" : "' + v + '"}',
    lambda stream: _sed_engines(TRANSIP_SED, stream),
)
transip_ground_truth.__doc__ = (
    "Replay the TransIP token capture on BusyBox sed. GNU is logged only.\n\n"
    "Returns False on busybox-absent / sed failure so ``run_one`` records\n"
    "``ground_truth=failed`` instead of aborting the suite."
)

cloudflare_ground_truth = _prefix_truncation_gt(
    "OW-packages-cloudflare-content-truncation",
    lambda v: '{"content":"' + v + '"}',
    _cloudflare_engines,
)
cloudflare_ground_truth.__doc__ = (
    'Replay Cloudflare ``content`` ``[^"]*`` extract on BusyBox grep.\n\n'
    "Returns False on busybox-absent / grep failure so ``run_one`` records\n"
    "``ground_truth=failed`` instead of aborting the suite."
)

aliyun_ground_truth = _prefix_truncation_gt(
    "OW-packages-aliyun-recordid-truncation",
    lambda v: f"RecordId={v}&other=1",
    _aliyun_engines,
)
aliyun_ground_truth.__doc__ = (
    "Replay Aliyun ``RecordId=[^&]*`` extract on BusyBox grep.\n\n"
    "Returns False on busybox-absent / grep failure so ``run_one`` records\n"
    "``ground_truth=failed`` instead of aborting the suite."
)


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
    return [
        InRe(v, Star(ASCII_NUL_FREE)),
        first_quote > 0,
        capture != v,
    ], Contains(v, StringVal('"'))


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
    "OW-packages-sanitizer-image-no-semicolon",
    "pbr str_extras_to_underscore image alphabet (ASCII minus extras; "
    "extras including ';' map to '_') contains no semicolon "
    "(length-independent single-char)",
    expect_unsat=True,
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    contract={
        "schema_version": "1",
        "site": "net/pbr/files/etc/init.d/pbr:213:str_extras_to_underscore",
        "guarantee": (
            "sanitizer output alphabet contains no semicolon "
            "(extras class maps ';' to '_')"
        ),
        "input_source": "UCI policy dest / domain token (nft/dnsmasq names)",
        "trust": "config",
        "declared_domain": (
            "sanitizer image alphabet (ASCII 0x01-0x7f minus extras), "
            "single char, ASCII"
        ),
        "provenance": "human",
    },
)
def ow_sanitizer_image():
    c = String("c")
    return [InRe(c, SANITIZER_IMAGE), Length(c) == 1], c == StringVal(";")


@prop(
    "OW-packages-ipv4-regex-no-semicolon",
    "ddns IPV4_REGEX constant alphabet [0-9.] contains no semicolon "
    "(length-independent single-char; prove the definition, not $IPV4_REGEX)",
    expect_unsat=True,
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract={
        "schema_version": "1",
        "site": "net/ddns-scripts/files/usr/lib/ddns/dynamic_dns_functions.sh:69:IPV4_REGEX",
        "guarantee": "IPV4_REGEX extract alphabet chars contain no semicolon",
        "input_source": "WAN / local IP string before send_update",
        "trust": "untrusted-input",
        "declared_domain": "IPv4 extract alphabet [0-9.], single char, ASCII",
        "provenance": "human",
    },
)
def ow_ipv4_regex():
    c = String("c")
    return [InRe(c, IPV4_CHAR), Length(c) == 1], c == StringVal(";")


@prop(
    "OW-packages-expand-ipv6-nibble-capture",
    "expand_ipv6 3-hex nibble between colons is captured in full by "
    r"s|:([0-9a-f]{3}):|:0\1:| — proven for exactly 3 lowercase hex",
    expect_unsat=True,
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    contract={
        "schema_version": "1",
        "site": (
            "net/ddns-scripts/files/usr/lib/ddns/"
            "dynamic_dns_functions.sh:1181:expand_ipv6"
        ),
        "guarantee": "3-hex IPv6 nibbles are captured in full (no colon in domain)",
        "input_source": "WAN IPv6 compared after DDNS GET",
        "trust": "untrusted-input",
        "declared_domain": "lowercase hex [0-9a-f]{3}, ASCII, colon-free",
        "provenance": "human",
    },
)
def ow_expand_ipv6():
    w = String("w")
    colon = IndexOf(w, StringVal(":"), 0)
    cap = If(colon < 0, w, SubString(w, 0, colon))
    return [InRe(w, HEX3_LC), Length(w) == 3], cap != w


@prop(
    "OW-packages-cloudflare-content-truncation",
    "exists v: v contains a quote AND BusyBox grep [^\\\"]* content "
    "extract is a strict prefix of v — Cloudflare JSON content extract",
    expect_unsat=False,
    ground_truth=cloudflare_ground_truth,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract={
        "schema_version": "1",
        "site": (
            "net/ddns-scripts/files/usr/lib/ddns/"
            "update_cloudflare_com_v4.sh:245:content"
        ),
        "guarantee": "JSON content capture truncates at the first unescaped quote",
        "input_source": "Cloudflare HTTPS JSON body (WAN)",
        "trust": "untrusted-input",
        "declared_domain": "ASCII JSON string values, NUL-free, BusyBox grep",
        "provenance": "human",
    },
)
def ow_cloudflare():
    v = String("v")
    first_quote = IndexOf(v, StringVal('"'), 0)
    capture = SubString(v, 0, first_quote)
    return [
        InRe(v, Star(ASCII_NUL_FREE)),
        first_quote > 0,
        capture != v,
    ], Contains(v, StringVal('"'))


@prop(
    "OW-packages-huawei-id-no-semicolon",
    "Huawei DNS JSON id alphabet [a-z0-9] contains no semicolon "
    "(length-independent single-char; id is interpolated into API paths)",
    expect_unsat=True,
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract={
        "schema_version": "1",
        "site": "net/ddns-scripts/files/usr/lib/ddns/update_huaweicloud_com.sh:94:id",
        "guarantee": "extracted zone/record id alphabet chars contain no semicolon",
        "input_source": "Huawei DNS HTTPS JSON body (WAN)",
        "trust": "untrusted-input",
        "declared_domain": "id alphabet [a-z0-9], single char, ASCII",
        "provenance": "human",
    },
)
def ow_huawei_id():
    c = String("c")
    return [InRe(c, HUAWEI_ID_CHAR), Length(c) == 1], c == StringVal(";")


@prop(
    "OW-packages-aliyun-recordid-truncation",
    "exists v: v contains '&' AND BusyBox grep RecordId=[^&]* extract "
    "is a strict prefix of v — Aliyun query-string RecordId",
    expect_unsat=False,
    ground_truth=aliyun_ground_truth,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract={
        "schema_version": "1",
        "site": "net/ddns-scripts/files/usr/lib/ddns/update_aliyun_com.sh:115:RecordId",
        "guarantee": "query-string RecordId capture truncates at the first '&'",
        "input_source": "UCI param_enc query fragment (config)",
        "trust": "config",
        "declared_domain": "ASCII query values, NUL-free, BusyBox grep",
        "provenance": "human",
    },
)
def ow_aliyun():
    v = String("v")
    amp = IndexOf(v, StringVal("&"), 0)
    capture = SubString(v, 0, amp)
    return [
        InRe(v, Star(ASCII_NUL_FREE)),
        amp > 0,
        capture != v,
    ], Contains(v, StringVal("&"))


@prop(
    "OW-packages-dnspod-recordid-no-semicolon",
    "DNSPod JSON RecordId digit alphabet [0-9] contains no semicolon "
    "(length-independent single-char; id is interpolated into ModifyRecord)",
    expect_unsat=True,
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract={
        "schema_version": "1",
        "site": "net/ddns-scripts/files/usr/lib/ddns/update_dnspod_cn_v3.sh:312:RecordId",
        "guarantee": "extracted RecordId digit alphabet chars contain no semicolon",
        "input_source": "Tencent DNSPod HTTPS JSON body (WAN)",
        "trust": "untrusted-input",
        "declared_domain": "RecordId alphabet [0-9], single char, ASCII",
        "provenance": "human",
    },
)
def ow_dnspod_recordid():
    c = String("c")
    return [InRe(c, DIGIT_CHAR), Length(c) == 1], c == StringVal(";")


@prop(
    "OW-packages-mosquitto-uci-quote-capture",
    "UCI auth_opt values (no single-quote) are captured in full by "
    r"s/^.*_(auth_opt_.*)='(.*)'/ — proven for len 1..16 quote-free ASCII",
    expect_unsat=True,
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    contract={
        "schema_version": "1",
        "site": "net/mosquitto/files/etc/init.d/mosquitto:101:auth_opt",
        "guarantee": "quote-free UCI auth_opt values are captured in full into mosquitto.conf",
        "input_source": "UCI mosquitto auth_opt_* options",
        "trust": "config",
        "declared_domain": "ASCII minus U+0027, len 1..16, BusyBox sed",
        "provenance": "human",
    },
)
def ow_mosquitto():
    w = String("w")
    q = IndexOf(w, StringVal("'"), 0)
    cap = If(q < 0, w, SubString(w, 0, q))
    return [
        InRe(w, Concat(UCI_NO_QUOTE, Star(UCI_NO_QUOTE))),
        Length(w) >= 1,
        Length(w) <= 16,
    ], cap != w


@prop(
    "OW-packages-nftset-passthrough-no-dot",
    "pbr nftset grep-E escape passthrough alphabet (ASCII minus "
    r"[/.^$*\[\\]; those map to \&) contains no '.' "
    "(length-independent single-char)",
    expect_unsat=True,
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    contract={
        "schema_version": "1",
        "site": "net/pbr/files/etc/init.d/pbr:1143:nftset-escape",
        "guarantee": (
            "nftset names that skip the grep-E extras class contain no '.' "
            "(extras including '.' are escaped)"
        ),
        "input_source": "dnsmasq nftset name from pbr policy",
        "trust": "config",
        "declared_domain": (
            "nftset passthrough alphabet (ASCII 0x01-0x7f minus "
            r"[/.^$*\[\\]), single char, ASCII"
        ),
        "provenance": "human",
    },
)
def ow_nftset_passthrough():
    c = String("c")
    return [InRe(c, NFTSET_PASSTHROUGH), Length(c) == 1], c == StringVal(".")


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
