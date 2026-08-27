"""claude-code-plugins conversion-wave properties (family ``AI-claude-plugins``).

Wave 1 (posix-shell plugin/hooks/guards): CLI long-flag alphabet, slash-command
``/plugin:skill`` reference alphabet, and git-clean ``-e`` short-option bundle
alphabet. Product engine is BusyBox ``grep -E`` at bash ``=~`` search sites and
BusyBox ``sed -E`` at the skill-ref substitution. BusyBox alone decides
ground-truth; GNU is not consulted.
Importing this module registers into ``REGISTRY``.
"""

from __future__ import annotations

from z3 import (
    InRe,
    Length,
    Re,
    String,
    StringVal,
    Union,
)

from regexproof.harness.core import prop

FAMILY = "AI-claude-plugins"


def _union_chars(text: str):
    seen: list[str] = []
    parts = []
    for ch in text:
        if ch in seen:
            continue
        seen.append(ch)
        parts.append(Re(ch))
    return Union(*parts)


# cli-flag-verify.sh — long-flag token ``^(--[a-zA-Z][a-zA-Z0-9-]*)``.
CLI_FLAG_CHAR = _union_chars("-ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
# skill-reference-verify.sh — ``/<plugin>:<skill>`` command token.
SKILL_REF_CHAR = _union_chars("/abcdefghijklmnopqrstuvwxyz0123456789:-")
# block-dangerous-git.sh — git clean short bundle containing ``e``.
GIT_E_CHAR = _union_chars("-ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

CLI_FLAG_GREP = r"^(--[a-zA-Z][a-zA-Z0-9-]*)"
SKILL_REF_SED = r"^(/[a-z][a-z0-9-]*:[a-z][a-z0-9-]*)([[:space:]].*)?$"
GIT_E_GREP = r"^-[A-Za-z]*e[A-Za-z]*$"


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
    "AI-claude-plugins-cli-flag-no-semicolon",
    CLI_FLAG_CHAR,
    "plugins/guardrails/hooks/cli-flag-verify.sh:247:flag",
    (
        "CLI long-flag alphabet contains no semicolon "
        "(extracted --flag token reaches <bin> --help verification)"
    ),
    "agent Write/Edit of *.sh/*.bash/*.ps1/*.md command text (PostToolUse payload)",
    "untrusted-input",
    "CLI long-flag alphabet [--A-Za-z0-9-], single char, ASCII",
)

_alphabet_no(
    ";",
    "AI-claude-plugins-skill-ref-no-semicolon",
    SKILL_REF_CHAR,
    "plugins/guardrails/hooks/skill-reference-verify.sh:290:skill-ref",
    (
        "slash-command /plugin:skill alphabet contains no semicolon "
        "(extracted ref reaches marketplace skill-dir resolve)"
    ),
    "agent Write/Edit of *.md inline-code spans (PostToolUse payload)",
    "untrusted-input",
    "skill-ref alphabet [/[a-z0-9:-]], single char, ASCII",
)

_alphabet_no(
    ";",
    "AI-claude-plugins-git-clean-e-bundle-no-semicolon",
    GIT_E_CHAR,
    "plugins/guardrails/hooks/block-dangerous-git.sh:1055:clean-e",
    (
        "git-clean -e short-option bundle alphabet contains no semicolon "
        "(matched bundle fail-closes irreversible git clean -f)"
    ),
    "agent Bash/PowerShell tool-call argv (PreToolUse command)",
    "untrusted-input",
    "git-clean -e bundle alphabet [-A-Za-z], single char, ASCII",
)


@prop(
    "AI-claude-plugins-mutated-cli-flag-semicolon",
    "MUTATION GUARD: if the CLI long-flag alphabet admits ';', "
    "cli-flag-no-semicolon MUST flip UNSAT->SAT",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def ai_cli_flag_mutated():
    c = String("c")
    weak = Union(CLI_FLAG_CHAR, Re(";"))
    return [InRe(c, weak), Length(c) == 1], c == StringVal(";")
