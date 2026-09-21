"""Forge CLI secret-redaction conversion properties.

Wave 1 covers five human-adopted contracts from
``sweep/forge-cli-conversion/plan.md`` at pin ``PIN``. PRODUCT and MATCH
are independently specified; aliasing them is Concat-identity and is not a
countable property.

Three slots are length-independent shape-1 alphabets taken from the pinned
Python classes (new alphabets, not hostname / JSON / IPv4). Two slots are
coverage inclusions: an escaped-quote JAAS product grammar against
``_JAAS_CONFIG_RE``, and the documented sensitive-key forms against
``SENSITIVE_ENV_KEY_RE``. The unencodable LLM query ``[^&]+`` at
``providers.py:280`` is skipped; the adopted LLM site is the encodable
userinfo substitution at ``:287``.
"""

from __future__ import annotations

from z3 import (
    Concat,
    InRe,
    Length,
    Loop,
    Not,
    Re,
    String,
    StringVal,
    Union,
)

from regexproof.harness.core import ci, prop

FAMILY = "FC-forge-cli"
PIN = "efcf8e4c0087def553a737dc1c4eebda5d8a90cd"

# Inventory patterns at the pin (CPython ``re`` is the product engine).
URL_PASSWORD_PATTERN = r"[^/?#@\s]"
JAAS_PATTERN = (
    r'(?i)([\w.]{,64}sasl\.jaas\.config"?\s{,8}[:=]\s{,8}")'
    r'((?:[^"\\]|\\.){,2048})(")'
)
ENV_PATTERN = (
    r"(?i)(password|passphrase|secret|token|api[_-]?key|"
    r"private[_-]?key|credential|auth)"
)
DMM_VALUE_PATTERN = r"[^\"'\s,;}]+"
LLM_USERINFO_PATTERN = r"[^@/]"

SITE_URL = (
    f"Agenticstiger/forge-cli@{PIN}:"
    "fluid_build/observability/secret_redactor.py:151:_URL_USERINFO_RE"
)
SITE_JAAS = (
    f"Agenticstiger/forge-cli@{PIN}:"
    "fluid_build/observability/secret_redactor.py:218:_JAAS_CONFIG_RE"
)
SITE_ENV = (
    f"Agenticstiger/forge-cli@{PIN}:"
    "fluid_build/build_runners/base.py:54:SENSITIVE_ENV_KEY_RE"
)
SITE_DMM = (
    f"Agenticstiger/forge-cli@{PIN}:"
    "fluid_build/providers/datamesh_manager/datamesh_manager.py:88:_SECRET_ERROR_PATTERNS"
)
SITE_LLM = (
    f"Agenticstiger/forge-cli@{PIN}:"
    "fluid_build/llm/providers.py:287:LlmConfig.redacted_endpoint"
)

_WHITESPACE = frozenset(" \t\n\r\f\v")
_PRINTABLE = range(0x20, 0x7F)


def _chars(text: str):
    return Union(*(Re(ch) for ch in text))


def _ascii_minus(forbidden: set[str]):
    """Printable ASCII (0x20-0x7E) minus *forbidden*."""

    return _chars("".join(chr(i) for i in _PRINTABLE if chr(i) not in forbidden))


# Source ``[^/?#@\s]`` restricted to the declared printable-ASCII domain.
URL_PASSWORD_CHAR = _ascii_minus({"/", "?", "#", "@"} | _WHITESPACE)
# Source ``[^"'\s,;}]+``
DMM_VALUE_CHAR = _ascii_minus({'"', "'", ",", ";", "}"} | _WHITESPACE)
# Source ``([^@/]+)`` at providers.py:287, not the unencodable ``[^&]+`` at :280.
LLM_USERINFO_CHAR = _ascii_minus({"@", "/"})

# Independent JAAS product: letters plus one required escaped-quote token.
# MATCH is the inventory escape grammar on the same tiny alphabet — not an
# alias of PRODUCT. The declared domain is this restricted letter subset,
# not the full 2048-token source bound (that inclusion TIMEOUTs).
JAAS_OPEN = Re('sasl.jaas.config="')
JAAS_CLOSE = Re('"')
JAAS_BODY_CHAR = _chars("abcdefghijklmnopqrstuvwxyz")
JAAS_PRODUCT = Concat(
    JAAS_OPEN,
    Loop(JAAS_BODY_CHAR, 0, 4),
    Re('\\"'),
    Loop(JAAS_BODY_CHAR, 0, 4),
    JAAS_CLOSE,
)
JAAS_ESCAPE_PAYLOAD = Union(JAAS_BODY_CHAR, Re('"'), Re("\\"))
JAAS_MATCH = Concat(
    JAAS_OPEN,
    Loop(Union(JAAS_BODY_CHAR, Concat(Re("\\"), JAAS_ESCAPE_PAYLOAD)), 0, 16),
    JAAS_CLOSE,
)

# Independent ENV product: the documented key forms, including the empty
# ``[_-]?`` case (``apikey``, ``privatekey``). MATCH is the source regex.
ENV_POLICY_KEYS = (
    "password",
    "passphrase",
    "secret",
    "token",
    "credential",
    "auth",
    "apikey",
    "api_key",
    "api-key",
    "privatekey",
    "private_key",
    "private-key",
)
ENV_PRODUCT = Union(*(ci(word) for word in ENV_POLICY_KEYS))
ENV_MATCH = Union(
    ci("password"),
    ci("passphrase"),
    ci("secret"),
    ci("token"),
    ci("credential"),
    ci("auth"),
    Concat(ci("api"), Loop(_chars("_-"), 0, 1), ci("key")),
    Concat(ci("private"), Loop(_chars("_-"), 0, 1), ci("key")),
)


def _contract(site: str, guarantee: str, input_source: str, trust: str, domain: str) -> dict:
    return {
        "schema_version": "1",
        "site": site,
        "guarantee": guarantee,
        "input_source": input_source,
        "trust": trust,
        "declared_domain": domain,
        "provenance": "human",
    }


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
        contract=_contract(site, guarantee, input_source, trust, declared_domain),
    )
    def _fn(ch=ch, alphabet=alphabet):
        c = String("c")
        return [InRe(c, alphabet), Length(c) == 1], c == StringVal(ch)

    return _fn


_alphabet_no(
    " ",
    "FC-forge-cli-url-password-no-space",
    URL_PASSWORD_CHAR,
    SITE_URL,
    (
        "URL userinfo password alphabet contains no space "
        "(matched password reaches redact_secret_text)"
    ),
    "provider and operator endpoint text reaching shared logs and state",
    "config",
    "printable ASCII intersect [^/?#@\\s], single char",
)

_alphabet_no(
    ";",
    "FC-forge-cli-dmm-value-no-semicolon",
    DMM_VALUE_CHAR,
    SITE_DMM,
    (
        "Datamesh assignment-value alphabet contains no semicolon "
        "(matched value reaches _redact_error_body)"
    ),
    "untrusted remote provider error body",
    "untrusted-input",
    "printable ASCII intersect [^\"'\\s,;}], single char",
)

_alphabet_no(
    "@",
    "FC-forge-cli-llm-userinfo-no-at",
    LLM_USERINFO_CHAR,
    SITE_LLM,
    (
        "LLM endpoint userinfo alphabet contains no @ "
        "(matched userinfo reaches LlmConfig.redacted_endpoint)"
    ),
    "configured LLM endpoint used by the AI setup/test report",
    "config",
    "printable ASCII intersect [^@/], single char",
)


@prop(
    "FC-forge-cli-jaas-escaped-quote-covered",
    "escaped-quote JAAS values in the independent product grammar are "
    "accepted by _JAAS_CONFIG_RE (ASCII, total len 1..64)",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract=_contract(
        SITE_JAAS,
        "an escaped-quote sasl.jaas.config value in the product grammar is "
        "accepted by _JAAS_CONFIG_RE before redact_secret_text",
        "serialized connector/provider configuration and engine error text",
        "untrusted-input",
        "ASCII sasl.jaas.config=\"...\" record; value is [a-z]{0,4}\\\"[a-z]{0,4}, "
        "total len 1..64",
    ),
)
def forge_cli_jaas_escaped_quote_covered():
    s = String("s")
    return [InRe(s, JAAS_PRODUCT), Length(s) <= 64], Not(InRe(s, JAAS_MATCH))


@prop(
    "FC-forge-cli-sensitive-env-key-covered",
    "documented ASCII sensitive-key forms are accepted by "
    "SENSITIVE_ENV_KEY_RE (key len 1..32)",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract=_contract(
        SITE_ENV,
        "documented sensitive-key forms are accepted by SENSITIVE_ENV_KEY_RE "
        "before _render_command_for_log",
        "operator/provider configuration rendered by _render_command_for_log",
        "config",
        "exact ASCII policy-key literals (case-insensitive), len 1..32",
    ),
)
def forge_cli_sensitive_env_key_covered():
    s = String("s")
    return [InRe(s, ENV_PRODUCT), Length(s) <= 32], Not(InRe(s, ENV_MATCH))


@prop(
    "FC-forge-cli-mutated-url-password-space",
    "MUTATION GUARD: if the URL password alphabet admits space, "
    "url-password-no-space MUST flip UNSAT->SAT",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def forge_cli_mutated_url_password_space():
    c = String("c")
    weak = Union(URL_PASSWORD_CHAR, Re(" "))
    return [InRe(c, weak), Length(c) == 1], c == StringVal(" ")
