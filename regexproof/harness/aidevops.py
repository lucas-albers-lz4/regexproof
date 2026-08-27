"""aidevops conversion-wave properties (family ``AI-aidevops``).

Wave 1 (posix-shell hooks/guards): brief-filename task-id alphabet + capture,
credential-emission ``remote_url``/``origin_url`` identifier alphabet, scope-guard
Files Scope heading alphabet, GitHub issue-number capture before ``gh issue view``.
Product engine is BusyBox ``grep``/``sed`` as at the call site (bash ``=~`` sites
replayed as ERE). GNU is logged and must not decide the ground-truth bit.
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

FAMILY = "AI-aidevops"

DIGIT = Range("0", "9")
DIGIT_PLUS = Concat(DIGIT, Star(DIGIT))
# brief-filename-guard.sh — t-ID body ``t[0-9]+``.
BRIEF_TID_CHAR = Union(Re("t"), DIGIT)
BRIEF_TID = Concat(Re("t"), DIGIT_PLUS)
# credential-emission-pre-push.sh — ``remote_url`` / ``origin_url`` ident.
CRED_IDENT_CHAR = Union(Range("a", "z"), Re("_"))
# scope-guard Files Scope heading: ``#``, POSIX space, letters.
SCOPE_HEADING_CHAR = Union(
    Re("#"),
    Re(" "),
    Re("\t"),
    Range("A", "Z"),
    Range("a", "z"),
)

BRIEF_SED = r"s|^todo/tasks/(t[0-9]+)-brief\.md$|\1|"
ISSUE_GREP = r"#[0-9]+"


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
    "AI-aidevops-brief-tid-no-semicolon",
    BRIEF_TID_CHAR,
    ".agents/hooks/brief-filename-guard.sh:84:brief-filename",
    (
        "captured brief task-id alphabet contains no semicolon "
        "(token reaches git log --grep claim lookup)"
    ),
    "agent-staged todo/tasks/tNNN-brief.md filename (pre-commit index)",
    "untrusted-input",
    "brief task-id alphabet [t0-9], single char, ASCII",
)

_alphabet_no(
    ";",
    "AI-aidevops-cred-ident-no-semicolon",
    CRED_IDENT_CHAR,
    ".agents/hooks/credential-emission-pre-push.sh:103:remote_url",
    (
        "credential-emission detector identifier alphabet contains no semicolon "
        "(matched $remote_url/$origin_url tokens flag unsanitized emits)"
    ),
    "added lines in .agents/scripts|hooks/*.sh diffs (pre-push)",
    "untrusted-input",
    "identifier alphabet [a-z_], single char, ASCII",
)

_alphabet_no(
    ";",
    "AI-aidevops-scope-heading-no-semicolon",
    SCOPE_HEADING_CHAR,
    ".agents/hooks/scope-guard-pre-push.sh:137:files-scope",
    (
        "Files Scope heading alphabet contains no semicolon "
        "(heading detect fail-closes the scope guard)"
    ),
    "operator-authored todo/tasks/tNNN-brief.md Files Scope heading",
    "config",
    "Files Scope heading alphabet [# \\tA-Za-z], single char, ASCII",
)


@prop(
    "AI-aidevops-brief-tid-capture",
    "brief filename t-ID (no hyphen) is captured in full by "
    r"^todo/tasks/(t[0-9]+)-brief\.md$ — proven for len 2..16 [t0-9]+",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract={
        "schema_version": "1",
        "site": ".agents/hooks/brief-filename-guard.sh:105:tid",
        "guarantee": (
            "hyphen-free brief task-id tokens are captured in full into "
            "git log --grep claim lookup"
        ),
        "input_source": "agent-staged todo/tasks/tNNN-brief.md filename (pre-commit index)",
        "trust": "untrusted-input",
        "declared_domain": "t[0-9]+ ASCII, len 2..16, hyphen-free, BusyBox sed",
        "provenance": "human",
    },
)
def ai_brief_tid_capture():
    w = String("w")
    q = IndexOf(w, StringVal("-"), 0)
    cap = If(q < 0, w, SubString(w, 0, q))
    return [
        InRe(w, BRIEF_TID),
        Length(w) >= 2,
        Length(w) <= 16,
    ], cap != w


@prop(
    "AI-aidevops-gh-issue-digit-capture",
    "GitHub issue numbers (digits only) are captured in full by "
    r"grep -oE '#[0-9]+' before gh issue view — proven for len 1..8 digits",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract={
        "schema_version": "1",
        "site": ".agents/hooks/task-id-collision-guard.sh:378:issue",
        "guarantee": (
            "digit-only issue numbers are captured in full into gh issue view"
        ),
        "input_source": "commit-message Resolves/Closes/Fixes/Ref/For #NNN footers",
        "trust": "untrusted-input",
        "declared_domain": "digits [0-9]{1,8}, ASCII, BusyBox grep -oE",
        "provenance": "human",
    },
)
def ai_gh_issue_capture():
    w = String("w")
    q = IndexOf(w, StringVal(";"), 0)
    cap = If(q < 0, w, SubString(w, 0, q))
    return [
        InRe(w, DIGIT_PLUS),
        Length(w) >= 1,
        Length(w) <= 8,
    ], cap != w


@prop(
    "AI-aidevops-mutated-brief-tid-semicolon",
    "MUTATION GUARD: if the brief task-id alphabet admits ';', "
    "brief-tid-no-semicolon MUST flip UNSAT->SAT",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def ai_brief_tid_mutated():
    c = String("c")
    weak = Union(BRIEF_TID_CHAR, Re(";"))
    return [InRe(c, weak), Length(c) == 1], c == StringVal(";")
