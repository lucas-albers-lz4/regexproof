"""mycelium conversion-wave properties (family ``MY-mycelium``).

Wave 1 (control-plane fail-closed guards): sshd authorized-key type prefix,
AmneziaWG dialect-key alphabet, REALITY donor ALPN h2 line alphabet, and
AllowedIPs last-octet capture before client address allocation.
Product engine is BusyBox (``grep -E`` at search sites; ``sed -E`` at the
last-octet substitution — not sed-for-bash-``=~``). BusyBox alone decides
ground-truth; GNU is not consulted.
Importing this module registers into ``REGISTRY``.
"""

from __future__ import annotations

from z3 import (
    Concat,
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

FAMILY = "MY-mycelium"

DIGIT = Range("0", "9")
DIGIT_PLUS = Concat(DIGIT, Star(DIGIT))


def _union_chars(text: str):
    seen: list[str] = []
    parts = []
    for ch in text:
        if ch in seen:
            continue
        seen.append(ch)
        parts.append(Re(ch))
    return Union(*parts)


# harden_sshd authorized-key prefixes: ssh-(ed25519|rsa) | ecdsa- | sk-
SSH_KEY_CHAR = _union_chars("ssh-ed25519ssh-rsaecdsa-sk-")
# _awg_dialect_lines keys: Jc|Jmin|Jmax|S1|S2|H1|H2|H3|H4
AWG_DIALECT_CHAR = _union_chars("JcJminJmaxS1S2H1H2H3H4")
# donor_offers_h2 exact ALPN line (POSIX space + literals).
ALPN_H2_CHAR = _union_chars(" \tALPN protocol:h2")

SSH_KEY_GREP = r"^(ssh-(ed25519|rsa)|ecdsa-|sk-)"
AWG_DIALECT_GREP = r"^(Jc|Jmin|Jmax|S1|S2|H1|H2|H3|H4) = "
ALPN_H2_GREP = r"^[[:space:]]*ALPN protocol:[[:space:]]*h2[[:space:]]*$"
AWG_LAST_OCTET_SED = r"s#^[0-9]+\.[0-9]+\.[0-9]+\.([0-9]+)/.*#\1#"


def _alphabet_no(ch: str, name: str, alphabet, site: str, guarantee: str,
                 input_source: str, trust: str, declared_domain: str):
    @prop(
        name,
        f"{guarantee} (length-independent single-char)",
        expect_unsat=True,
        kind="property",
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
    "MY-mycelium-ssh-key-prefix-no-semicolon",
    SSH_KEY_CHAR,
    "control/lib/nb_harden.sh:74:ssh-key",
    (
        "authorized-key type prefix alphabet contains no semicolon "
        "(matched prefix fail-closes sshd key-only harden / anti-lockout)"
    ),
    "local authorized_keys files enumerated from sshd -T AuthorizedKeysFile",
    "config",
    "ssh key-type prefix alphabet [ssh-ed25519|ssh-rsa|ecdsa-|sk- chars], single char, ASCII",
)

_alphabet_no(
    ";",
    "MY-mycelium-awg-dialect-key-no-semicolon",
    AWG_DIALECT_CHAR,
    "control/lib/nb_render_awg.sh:434:dialect",
    (
        "AmneziaWG dialect-key alphabet contains no semicolon "
        "(exactly-9 dialect lines fail-close awg-regen of live awg0.conf)"
    ),
    "live /etc/amnezia/amneziawg/awg0.conf [Interface] obfuscation lines",
    "config",
    "AWG dialect-key alphabet [Jc|Jmin|Jmax|S1|S2|H1-H4 chars], single char, ASCII",
)

_alphabet_no(
    ";",
    "MY-mycelium-alpn-h2-line-no-semicolon",
    ALPN_H2_CHAR,
    "control/lib/nb_donor.sh:158:alpn-h2",
    (
        "ALPN h2 detect-line alphabet contains no semicolon "
        "(matched line prefers the donor in pick_donor REALITY cover selection)"
    ),
    "openssl s_client ALPN line from a candidate REALITY donor host:443",
    "untrusted-input",
    "ALPN h2 line alphabet [POSIX space + 'ALPN protocol:h2'], single char, ASCII",
)


@prop(
    "MY-mycelium-awg-last-octet-capture",
    "AllowedIPs last IPv4 octet (digits before '/') is captured in full by "
    r"sed -E 's#^[0-9]+\.[0-9]+\.[0-9]+\.([0-9]+)/.*#\1#' — "
    "proven for octet len 1..3 plus '/' plus mask digits",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    contract={
        "schema_version": "1",
        "site": "control/lib/nb_render_awg.sh:639:last-octet",
        "guarantee": (
            "digit last-octets before '/' are captured in full into the "
            "AmneziaWG client address slot (awg-issue enrolment)"
        ),
        "input_source": "live awg0.conf AllowedIPs for an existing peer public key",
        "trust": "config",
        "declared_domain": (
            "last-octet field DIGIT{1,3} '/' DIGIT{1,2} ASCII, slash is the "
            "real delimiter, BusyBox sed -E"
        ),
        "provenance": "human",
    },
)
def my_awg_last_octet_capture():
    # Mirror group 1 under ``([0-9]+)/.*``: Concat so '/' is IN the domain
    # (Luna: no vacuous IndexOf on an alphabet-disjoint char).
    octet = String("octet")
    mask = String("mask")
    w = Concat(octet, StringVal("/"), mask)
    q = IndexOf(w, StringVal("/"), 0)
    cap = If(q < 0, w, SubString(w, 0, q))
    return [
        InRe(octet, DIGIT_PLUS),
        InRe(mask, DIGIT_PLUS),
        Length(octet) >= 1,
        Length(octet) <= 3,
        Length(mask) >= 1,
        Length(mask) <= 2,
        q >= 0,
    ], cap != octet


@prop(
    "MY-mycelium-mutated-ssh-key-semicolon",
    "MUTATION GUARD: if the ssh key-type prefix alphabet admits ';', "
    "ssh-key-prefix-no-semicolon MUST flip UNSAT->SAT",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def my_ssh_key_mutated():
    c = String("c")
    weak = Union(SSH_KEY_CHAR, Re(";"))
    return [InRe(c, weak), Length(c) == 1], c == StringVal(";")
