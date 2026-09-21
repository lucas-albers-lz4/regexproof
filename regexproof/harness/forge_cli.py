"""Forge CLI secret-redaction conversion properties.

Wave 1 covers the five human-adopted redaction contracts from
``sweep/forge-cli-conversion/plan.md``.  The source is pinned to
``Agenticstiger/forge-cli`` at ``PIN``; the mirrors below deliberately model
the encodable ASCII subset of the Python ``re`` sites rather than claiming to
cover the repository's other regexes.

The properties are coverage obligations for the real redaction sinks:
credentialed URL userinfo, serialized JAAS values, dbt environment arguments,
Datamesh error bodies, and LLM endpoint query credentials.  Each family has a
mutation guard so a weakened mirror cannot pass silently.
"""

from __future__ import annotations

from z3 import (
    Concat,
    Contains,
    InRe,
    Length,
    Loop,
    Not,
    Re,
    Star,
    String,
    StringVal,
    Union,
)

from regexproof.harness.core import prop

FAMILY = "FC-forge-cli"
PIN = "efcf8e4c0087def553a737dc1c4eebda5d8a90cd"


def _chars(text: str):
    return Union(*(Re(ch) for ch in text))


ASCII = _chars("".join(chr(i) for i in range(0x20, 0x7F)))
ASCII_NO_QUOTE_BACKSLASH = _chars(
    "".join(chr(i) for i in range(0x20, 0x7F) if chr(i) not in {'"', "\\"})
)
ASCII_NO_AMPERSAND = _chars(
    "".join(chr(i) for i in range(0x20, 0x7F) if chr(i) != "&")
)
WORD = _chars("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_")
WORD_DOT = _chars("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.")
LETTER = _chars("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
URL_SCHEME_CHAR = _chars("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+.-")
URL_USER_CHAR = _chars(
    "".join(
        chr(i)
        for i in range(0x20, 0x7F)
        if chr(i) not in "/?#@:\t\n\r\f\v "
    )
)
URL_PASSWORD_CHAR = _chars(
    "".join(chr(i) for i in range(0x20, 0x7F) if chr(i) not in "/?#@\t\n\r\f\v ")
)
URL_HOST_CHAR = _chars(
    "".join(chr(i) for i in range(0x21, 0x7F) if chr(i) not in "?#@\t\n\r\f\v ")
)


def _ci(text: str):
    """Mirror Python ``re.IGNORECASE`` over the declared ASCII domain."""

    return Concat(
        *[
            Union(Re(char.lower()), Re(char.upper()))
            if char.isalpha()
            else Re(char)
            for char in text
        ]
    )


def _ci_literal_variants(*words: str):
    return Union(*(_ci(word) for word in words))


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
    "fluid_build/providers/datamesh_manager/datamesh_manager.py:87:_SECRET_ERROR_PATTERNS"
)
SITE_LLM = (
    f"Agenticstiger/forge-cli@{PIN}:"
    "fluid_build/llm/providers.py:277:LlmConfig.redacted_endpoint"
)


# ---------------------------------------------------------------------------
# Source-language mirrors
# ---------------------------------------------------------------------------

URL_SCHEME = Concat(LETTER, Loop(URL_SCHEME_CHAR, 0, 40), Re("://"))
URL_USER = Star(URL_USER_CHAR)
URL_PASSWORD = Concat(URL_PASSWORD_CHAR, Star(URL_PASSWORD_CHAR))
URL_HOST = Concat(URL_HOST_CHAR, Star(URL_HOST_CHAR))
URL_USERINFO_MATCH = Concat(
    URL_SCHEME,
    URL_USER,
    Re(":"),
    URL_PASSWORD,
    Re("@"),
)
URL_SEARCH = Concat(URL_USERINFO_MATCH, URL_HOST)
URL_PRODUCT = Concat(URL_SCHEME, URL_USER, Re(":"), URL_PASSWORD, Re("@"), URL_HOST)

JAAS_PREFIX = Concat(
    Loop(WORD_DOT, 0, 64),
    _ci("sasl"),
    Re("."),
    _ci("jaas"),
    Re("."),
    _ci("config"),
    Loop(Re('"'), 0, 1),
    Loop(_chars(" \t\r\f\v\n"), 0, 8),
    _chars(":="),
    Loop(_chars(" \t\r\f\v\n"), 0, 8),
    Re('"'),
)
JAAS_VALUE_TOKEN = Union(
    ASCII_NO_QUOTE_BACKSLASH,
    Concat(Re("\\"), ASCII),
)
JAAS_VALUE = Loop(JAAS_VALUE_TOKEN, 0, 2048)
JAAS_MATCH = Concat(JAAS_PREFIX, JAAS_VALUE, Re('"'))
JAAS_PRODUCT = JAAS_MATCH

SENSITIVE_KEY_TOKEN = Union(
    _ci_literal_variants(
        "password",
        "passphrase",
        "secret",
        "token",
        "private_key",
        "private-key",
        "credential",
        "auth",
    ),
    Concat(_ci("api"), Loop(_chars("_-"), 0, 1), _ci("key")),
)
SENSITIVE_KEY_MATCH = Concat(Star(WORD), SENSITIVE_KEY_TOKEN, Star(WORD))
SENSITIVE_KEY_PRODUCT = SENSITIVE_KEY_MATCH

DMM_KEY = Union(
    _ci_literal_variants("x-api-key", "password", "token", "secret"),
    Concat(_ci("api"), Loop(_chars("_-"), 0, 1), _ci("key")),
)
DMM_SEPARATOR = Loop(_chars("\"' \t\r\f\v:=\n"), 1, 16)
DMM_VALUE = Concat(
    _chars(
        "".join(
            chr(i)
            for i in range(0x20, 0x7F)
            if chr(i) not in "\"'\t\n\r\f\v,;}"
        )
    ),
    Star(
        _chars(
            "".join(
                chr(i)
                for i in range(0x20, 0x7F)
                if chr(i) not in "\"'\t\n\r\f\v,;}"
            )
        )
    ),
)
DMM_ASSIGNMENT = Concat(DMM_KEY, DMM_SEPARATOR, DMM_VALUE)
DMM_TOKEN = Concat(
    Re("ed_live_"),
    Concat(
        _chars("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"),
        Star(_chars("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_")),
    ),
)
DMM_MATCH = Union(DMM_ASSIGNMENT, DMM_TOKEN)
DMM_PRODUCT = DMM_MATCH

LLM_KEY = _ci_literal_variants("key", "token", "auth", "secret", "credential", "password")
LLM_KEY = Union(LLM_KEY, Concat(_ci("api"), Re("_"), _ci("key")))
LLM_QUERY_MATCH = Concat(
    _chars("?&"),
    LLM_KEY,
    Re("="),
    ASCII_NO_AMPERSAND,
    Star(ASCII_NO_AMPERSAND),
)
LLM_QUERY_PRODUCT = LLM_QUERY_MATCH


def _contract(site: str, guarantee: str, input_source: str, domain: str) -> dict:
    return {
        "schema_version": "1",
        "site": site,
        "guarantee": guarantee,
        "input_source": input_source,
        "trust": "untrusted-input" if "error" in input_source.lower() else "config",
        "declared_domain": domain,
        "provenance": "human",
    }


@prop(
    "FC-forge-cli-url-userinfo-coverage",
    "every ASCII credentialed URL accepted by the product grammar is covered "
    "by _URL_USERINFO_RE (scheme/user/password/host; password len 1..4096)",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract=_contract(
        SITE_URL,
        "credentialed URL userinfo is recognized by the shared redaction sink "
        "while the scheme, user, and host remain available for diagnostics",
        "provider and operator endpoint text reaching shared logs and state",
        "ASCII credentialed URL with total len 1..64; scheme body len 1..41, "
        "user len 0..256, password len 1..4096, nonempty ASCII host",
    ),
)
def forge_cli_url_userinfo_coverage():
    s = String("s")
    return [InRe(s, URL_PRODUCT), Length(s) <= 64], Not(InRe(s, URL_SEARCH))


@prop(
    "FC-forge-cli-jaas-escaped-quote-coverage",
    "serialized sasl.jaas.config values with escaped quotes are covered by "
    "the whole-value _JAAS_CONFIG_RE branch",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    contract=_contract(
        SITE_JAAS,
        "an escaped-quote-safe sasl.jaas.config value is replaced as one "
        "quoted value before it reaches logs or persisted state",
        "serialized connector/provider configuration and engine error text",
        "ASCII serialized sasl.jaas.config record; value uses escaped-quote "
        "tokens, has len <= 2048 regex tokens, and contains no raw NUL/LF",
    ),
)
def forge_cli_jaas_escaped_quote_coverage():
    s = String("s")
    return [InRe(s, JAAS_PRODUCT), Contains(s, StringVal('\\"'))], Not(
        InRe(s, JAAS_MATCH)
    )


@prop(
    "FC-forge-cli-sensitive-env-key-coverage",
    "every ASCII sensitive dbt -e key is recognized by SENSITIVE_ENV_KEY_RE",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract=_contract(
        SITE_ENV,
        "a sensitive KEY=VALUE argument is rendered with its value redacted "
        "before the dbt command reaches the CLI log",
        "operator/provider configuration rendered by _render_command_for_log",
        "ASCII key containing a case-insensitive sensitive token, key len 1..64",
    ),
)
def forge_cli_sensitive_env_key_coverage():
    s = String("s")
    return [InRe(s, SENSITIVE_KEY_PRODUCT), Length(s) <= 64], Not(
        InRe(s, SENSITIVE_KEY_MATCH)
    )


@prop(
    "FC-forge-cli-dmm-error-secret-coverage",
    "recognized Datamesh assignment and ed_live_ tokens are covered by the "
    "error-body redaction patterns",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    contract=_contract(
        SITE_DMM,
        "recognized credential assignments and ed_live_ tokens do not reach "
        "ProviderError text in clear form",
        "untrusted remote provider error body",
        "ASCII Datamesh error fragment; assignment value is nonempty and "
        "terminates at the product delimiter set, or an ed_live_ token",
    ),
)
def forge_cli_dmm_error_secret_coverage():
    s = String("s")
    return [InRe(s, DMM_PRODUCT), Length(s) <= 256], Not(InRe(s, DMM_MATCH))


@prop(
    "FC-forge-cli-llm-query-secret-coverage",
    "credential query parameters in an ASCII endpoint are covered by the "
    "redacted_endpoint substitution",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    contract=_contract(
        SITE_LLM,
        "recognized endpoint query credentials are replaced before the AI test "
        "report exposes the endpoint",
        "configured LLM endpoint used by the AI setup/test report",
        "ASCII endpoint query fragment beginning with ? or &, recognized key, "
        "equals, and nonempty value with no ampersand",
    ),
)
def forge_cli_llm_query_secret_coverage():
    s = String("s")
    return [InRe(s, LLM_QUERY_PRODUCT), Length(s) <= 256], Not(
        InRe(s, LLM_QUERY_MATCH)
    )


@prop(
    "FC-forge-cli-mutated-url-userinfo-at",
    "MUTATION GUARD: allowing @ inside the URL password must expose a value "
    "the shipped userinfo matcher does not cover",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def forge_cli_mutated_url_userinfo_at():
    s = String("s")
    weakened_password = Concat(
        URL_PASSWORD_CHAR,
        Star(Union(URL_PASSWORD_CHAR, Re("@"))),
    )
    weakened = Concat(
        URL_SCHEME,
        URL_USER,
        Re(":"),
        weakened_password,
        Re("@"),
        URL_HOST,
    )
    witness = StringVal("https://user:pa@ss@example.com")
    return [InRe(s, weakened), s == witness], Not(InRe(s, URL_PRODUCT))
