"""Source-bound contracts for LLM honeypot sync and Tor-control scripts."""

from __future__ import annotations

import json
import ipaddress
from pathlib import Path

from z3 import Concat, InRe, Length, Not, Or, Range, Re, String, StringVal, Union

from regexproof.compiler import compile_pattern
from regexproof.groundtruth.llm_honeypot_replay import (
    PRIVATE_IP_PATTERN,
    TOR_PATTERN,
    grep_matches,
    sed_transform,
)
from regexproof.harness.core import prop

PIN = "65624396e263074bb8cb2e049f9a9ec6215ea5c1"
FAMILY_PRIVATE_IP = "LH-llm-honeypot-private-ip-redaction"
FAMILY_TOR = "LH-llm-honeypot-tor-newnym-response"
PRIVATE_IP_SITE = (
    f"Leviticus-Triage/llm-honeypot-intelligence@{PIN}:"
    "scripts/sync-to-github.sh:76:PRIVATE_IP_PATTERN"
)
TOR_SITE = (
    f"Leviticus-Triage/llm-honeypot-intelligence@{PIN}:"
    "spiderfoot-toolbox/tor-gateway/rotate-tor.sh:34:250 OK"
)
PRIVATE_IP_QUESTION = "LH-llm-honeypot-private-ip-rfc1918-redaction"
PRIVATE_IP_SUBPROPERTY = "LH-llm-honeypot-private-ip-192-168-coverage"
PRIVATE_IP_MUTATION = "LH-llm-honeypot-private-ip-embedded-search-mutation"
TOR_QUESTION = "LH-llm-honeypot-tor-newnym-response-sequencing"
TOR_SUBPROPERTY = "LH-llm-honeypot-tor-failure-only-response-rejected"
TOR_MUTATION = "LH-llm-honeypot-tor-mutated-response-acceptance"

_HERE = Path(__file__).resolve().parents[2]
_CALIBRATION = _HERE / "properties" / "calibration" / "2026-10-15-p2-llm-honeypot-source-review"
PRIVATE_IP_CONTRACT = json.loads((_CALIBRATION / "private-ip-contract.json").read_text())
TOR_CONTRACT = json.loads((_CALIBRATION / "tor-response-contract.json").read_text())


def _compiled(pattern: str, call_kind: str):
    result = compile_pattern(
        pattern,
        dialect="posix-shell",
        call_kind=call_kind,
        max_length=256,
        domain="ascii",
        shell_flags={"syntax": "ere"},
    )
    if result.mirror is None:
        raise RuntimeError(f"LLM honeypot POSIX ERE is not encodable: {result.unencodable_reason}")
    return result.mirror


_PRIVATE_SEARCH = _compiled(PRIVATE_IP_PATTERN, "substitution")
_PRIVATE_ANCHORED_MUTATION = _compiled(
    r"^192\.168\.[0-9]+\.[0-9]+$", "substitution"
)
_TOR_SEARCH = _compiled(TOR_PATTERN, "search")
_TOR_WIDENED = _compiled(".*", "search")

_DIGIT = Range("0", "9")
_NONZERO = Range("1", "9")
_OCTET = Union(
    Re("0"),
    _NONZERO,
    Concat(_NONZERO, _DIGIT),
    Concat(Re("1"), _DIGIT, _DIGIT),
    Concat(Re("2"), Range("0", "4"), _DIGIT),
    Concat(Re("25"), Range("0", "5")),
)
_DOT = Re(".")
_RFC1918 = Union(
    Concat(Re("10"), _DOT, _OCTET, _DOT, _OCTET, _DOT, _OCTET),
    Concat(
        Re("172"), _DOT,
        Union(
            Concat(Re("1"), Range("6", "9")),
            Concat(Re("2"), _DIGIT),
            Re("30"), Re("31"),
        ),
        _DOT, _OCTET, _DOT, _OCTET,
    ),
    Concat(Re("192"), _DOT, Re("168"), _DOT, _OCTET, _DOT, _OCTET),
)
_PRIVATE_192_168 = Concat(
    Re("192"), _DOT, Re("168"), _DOT, _OCTET, _DOT, _OCTET
)
_FAILURE_STATUS = Union(Re("550"), Re("551"), Re("552"), Re("553"), Re("555"))


def _address_is_rfc1918(value: str) -> bool:
    try:
        address = ipaddress.IPv4Address(value)
    except ipaddress.AddressValueError:
        return False
    networks = (
        ipaddress.IPv4Network("10.0.0.0/8"),
        ipaddress.IPv4Network("172.16.0.0/12"),
        ipaddress.IPv4Network("192.168.0.0/16"),
    )
    return any(address in network for network in networks)


def _private_gap_reproduces(witness: dict) -> bool:
    address = witness.get("private_address", "")
    if not _address_is_rfc1918(address):
        return False
    output = sed_transform(address)
    return output == address and address in output


@prop(
    PRIVATE_IP_SUBPROPERTY,
    "Every canonical 192.168/16 IPv4 token is covered by the pinned sed ERE",
    expect_unsat=True,
    kind="property",
    family=FAMILY_PRIVATE_IP,
    input_domain="ascii",
    call_kind="substitution",
    pattern=PRIVATE_IP_PATTERN,
    contract=PRIVATE_IP_CONTRACT,
)
def llm_honeypot_private_192_168_tokens_are_matched():
    address = String("private_address")
    return [InRe(address, _PRIVATE_192_168)], Not(InRe(address, _PRIVATE_SEARCH))


@prop(
    PRIVATE_IP_QUESTION,
    "COUNTEREXAMPLE FINDER: an RFC 1918 IPv4 token can pass through the exact "
    "pinned sed pattern without replacement",
    expect_unsat=False,
    kind="counterexample_finder",
    family=FAMILY_PRIVATE_IP,
    input_domain="ascii",
    call_kind="substitution",
    pattern=PRIVATE_IP_PATTERN,
    ground_truth=_private_gap_reproduces,
    contract=PRIVATE_IP_CONTRACT,
)
def llm_honeypot_rfc1918_redaction_gap():
    address = String("private_address")
    return [InRe(address, _RFC1918)], Not(InRe(address, _PRIVATE_SEARCH))


def _private_mutation_replays(witness: dict) -> bool:
    address = witness.get("private_address", "")
    content = witness.get("file_content", "")
    if not address.startswith("192.168.") or address not in content:
        return False
    output = sed_transform(content, r"^192\.168\.[0-9]+\.[0-9]+$")
    return address in output and "[REDACTED]" not in output


@prop(
    PRIVATE_IP_MUTATION,
    "MUTATION GUARD: anchoring the search regex to the whole file leaves an "
    "embedded 192.168 address unredacted",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY_PRIVATE_IP,
    input_domain="ascii",
    ground_truth=_private_mutation_replays,
)
def llm_honeypot_private_redaction_embedded_search_mutation():
    address = String("private_address")
    file_content = String("file_content")
    constraints = [
        InRe(address, _PRIVATE_192_168),
        file_content == Concat(StringVal("source="), address, StringVal(";")),
    ]
    return constraints, Not(InRe(file_content, _PRIVATE_ANCHORED_MUTATION))


def _tor_false_success_reproduces(witness: dict) -> bool:
    response = witness.get("control_reply", "")
    lines = response.splitlines()
    if (
        len(lines) < 2
        or lines[0] != "250 OK"
        or not lines[1].startswith(("550 ", "551 ", "552 ", "553 ", "555 "))
        or not grep_matches(response)
    ):
        return False
    # send_newnym's return status is the grep status; the source-bound gate
    # below separately replays the exact shell function with a local fake nc.
    return True


@prop(
    TOR_SUBPROPERTY,
    "A failure-only Tor ControlPort response has no matching success line",
    expect_unsat=True,
    kind="property",
    family=FAMILY_TOR,
    input_domain="ascii",
    call_kind="search",
    pattern=TOR_PATTERN,
    contract=TOR_CONTRACT,
)
def llm_honeypot_tor_failure_only_response_is_rejected():
    status = String("signal_status")
    response = String("control_reply")
    return [
        InRe(status, _FAILURE_STATUS),
        response == Concat(status, StringVal(" Internal error\r\n")),
    ], InRe(response, _TOR_SEARCH)


@prop(
    TOR_QUESTION,
    "COUNTEREXAMPLE FINDER: an AUTHENTICATE 250 OK followed by a failed "
    "SIGNAL NEWNYM reply still makes the pinned grep success predicate true",
    expect_unsat=False,
    kind="counterexample_finder",
    family=FAMILY_TOR,
    input_domain="ascii",
    call_kind="search",
    pattern=TOR_PATTERN,
    ground_truth=_tor_false_success_reproduces,
    contract=TOR_CONTRACT,
)
def llm_honeypot_tor_newnym_error_after_auth_success():
    status = String("signal_status")
    response = String("control_reply")
    constraints = [
        InRe(status, Union(Re("550"), Re("551"), Re("552"), Re("553"), Re("555"))),
        response
        == Concat(
            StringVal("250 OK\r\n"),
            status,
            StringVal(" Internal error\r\n250 closing connection\r\n"),
        ),
        Length(response) <= 128,
    ]
    return constraints, InRe(response, _TOR_SEARCH)


def _tor_mutation_replays(witness: dict) -> bool:
    response = witness.get("control_reply", "")
    return bool(response) and grep_matches(response, ".*")


@prop(
    TOR_MUTATION,
    "MUTATION GUARD: replacing the 250 OK matcher with .* accepts a failure-only reply",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY_TOR,
    input_domain="ascii",
    ground_truth=_tor_mutation_replays,
)
def llm_honeypot_tor_widened_matcher_accepts_failure():
    status = String("signal_status")
    response = String("control_reply")
    constraints = [
        InRe(status, _FAILURE_STATUS),
        response == Concat(status, StringVal(" Internal error\r\n")),
    ]
    return constraints, InRe(response, _TOR_WIDENED)


__all__ = [
    "FAMILY_PRIVATE_IP",
    "FAMILY_TOR",
    "PIN",
    "PRIVATE_IP_QUESTION",
    "PRIVATE_IP_SITE",
    "PRIVATE_IP_SUBPROPERTY",
    "TOR_QUESTION",
    "TOR_SITE",
    "TOR_SUBPROPERTY",
]
