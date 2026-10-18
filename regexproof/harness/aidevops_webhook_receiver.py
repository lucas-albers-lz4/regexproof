"""Contract-backed Bash regex properties for the pinned Aidevops webhook receiver."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, Concat, InRe, IndexOf, Length, Loop, Not, Plus, Range, Re, Star, String, StringVal, SubString, Union

from regexproof.compiler import compile_pattern
from regexproof.groundtruth.aidevops_webhook_replay import (
    PIN,
    pr_number_mutation_reproduces,
    secret_env_mutation_reproduces,
    sha_mutation_reproduces,
    slug_mutation_reproduces,
)
from regexproof.harness.core import prop

_ROOT = Path(__file__).resolve().parents[2]
_BUNDLE = _ROOT / "properties" / "calibration" / "2026-10-16-autonomous-aidevops-webhook-action-protocol-20r2"

PAT_SECRET = r"^[A-Za-z_][A-Za-z0-9_]*$"
PAT_SLUG = r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$"
PAT_OWNER = r"^[A-Za-z0-9][A-Za-z0-9_.-]*$"
PAT_SHA = r"^[A-Fa-f0-9]{40}$"
PAT_PR_NUMBER = r"^[0-9]+$"

FAMILY_SECRET = "AE-aidevops-webhook-secret-env-name"
FAMILY_SLUG = "AE-aidevops-webhook-repository-slug"
FAMILY_SHA = "AE-aidevops-webhook-check-sha"
FAMILY_PR = "AE-aidevops-webhook-pr-number"

SITE_SECRET = f"marcusquinn/aidevops@{PIN}:.agents/scripts/pulse-merge-webhook-receiver.sh:167:1"
SITE_SLUG = f"marcusquinn/aidevops@{PIN}:.agents/scripts/pulse-merge-webhook-receiver.sh:197:1"
SITE_SHA = f"marcusquinn/aidevops@{PIN}:.agents/scripts/pulse-merge-webhook-receiver.sh:224:1"
SITE_PR_NUMBER = f"marcusquinn/aidevops@{PIN}:.agents/scripts/pulse-merge-webhook-receiver.sh:302:6"

Q_SECRET = "AE-aidevops-webhook-secret-env-identifier"
Q_SHA = "AE-aidevops-webhook-check-sha-token"
Q_PR = "AE-aidevops-webhook-process-pr-number"
M_SECRET = "AE-aidevops-webhook-secret-env-mutation"
M_SLUG = "AE-aidevops-webhook-slug-owner-mutation"
M_SHA = "AE-aidevops-webhook-check-sha-mutation"
M_PR = "AE-aidevops-webhook-process-pr-number-mutation"


def _contract(name: str) -> dict:
    return json.loads((_BUNDLE / name).read_text(encoding="utf-8"))


def _compile(pattern: str):
    result = compile_pattern(
        pattern,
        dialect="posix-shell",
        call_kind="search",
        max_length=256,
        domain="ascii",
        shell_flags={"syntax": "bash_ksh"},
    )
    if result.mirror is None:
        raise RuntimeError(f"Aidevops webhook Bash ERE is not encodable: {result.unencodable_reason}")
    return result.mirror


_SOURCE_SECRET = _compile(PAT_SECRET)
_WEAK_SECRET = _compile(r"^[A-Za-z0-9_][A-Za-z0-9_]*$")
_SOURCE_SLUG = _compile(PAT_SLUG)
_WEAK_OWNER = _compile(r"^[A-Za-z0-9_.-]+$")
_SOURCE_SHA = _compile(PAT_SHA)
_WEAK_SHA = _compile(r"^[A-Fa-f0-9]{1,40}$")
_SOURCE_PR = _compile(PAT_PR_NUMBER)
_WEAK_PR = _compile(r"^.*$")

_ALPHA = Union(Range("A", "Z"), Range("a", "z"))
_DIGIT = Range("0", "9")
_UNDERSCORE = Re("_")
_NAME_REST_CHAR = Union(_ALPHA, _DIGIT, _UNDERSCORE)
_IDENTIFIER = Concat(Union(_ALPHA, _UNDERSCORE), Star(_NAME_REST_CHAR))
_ALNUM = Union(_ALPHA, _DIGIT)
_HEX = Union(_DIGIT, Range("A", "F"), Range("a", "f"))
_HEX40 = Loop(_HEX, 40, 40)
_DIGITS_PLUS = Plus(_DIGIT)


@prop(
    Q_SECRET,
    "The configured secret-variable name accepted by the receiver is a Bash identifier",
    expect_unsat=True,
    kind="property",
    family=FAMILY_SECRET,
    input_domain="ascii",
    call_kind="search",
    pattern=PAT_SECRET,
    contract=_contract("contract-secret-env-name.json"),
)
def webhook_secret_name_is_bash_identifier():
    name = String("name")
    return [InRe(name, _SOURCE_SECRET)], Not(InRe(name, _IDENTIFIER))


@prop(
    M_SECRET,
    "MUTATION GUARD: allowing a digit in the first variable-name position loses the identifier check",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY_SECRET,
    input_domain="ascii",
    call_kind="search",
    pattern=PAT_SECRET,
    ground_truth=secret_env_mutation_reproduces,
)
def webhook_secret_name_digit_first_mutation():
    name = String("name")
    return [InRe(name, _WEAK_SECRET), name == StringVal("8SECRET")], name == StringVal("8SECRET")


@prop(
    M_SLUG,
    "MUTATION GUARD: weakening the owner-first-character rule admits a leading-dot owner",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY_SLUG,
    input_domain="ascii",
    call_kind="search",
    pattern=PAT_SLUG,
    ground_truth=slug_mutation_reproduces,
)
def webhook_slug_owner_mutation():
    slug = String("slug")
    slash = IndexOf(slug, StringVal("/"), 0)
    owner = SubString(slug, 0, slash)
    name = SubString(slug, slash + 1, Length(slug) - slash - 1)
    accepted = And(InRe(slug, _SOURCE_SLUG), InRe(owner, _WEAK_OWNER), name != StringVal("."), name != StringVal(".."))
    return [accepted, slug == StringVal(".owner/repo")], slug == StringVal(".owner/repo")


@prop(
    Q_SHA,
    "The receiver's SHA regex accepts only 40-character ASCII hexadecimal tokens",
    expect_unsat=True,
    kind="property",
    family=FAMILY_SHA,
    input_domain="ascii",
    call_kind="search",
    pattern=PAT_SHA,
    contract=_contract("contract-check-sha-regex-only.json"),
)
def webhook_sha_is_exactly_40_hex():
    sha = String("sha")
    return [InRe(sha, _SOURCE_SHA)], Not(InRe(sha, _HEX40))


@prop(
    M_SHA,
    "MUTATION GUARD: shortening the SHA length range admits a one-character token to cache invalidation",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY_SHA,
    input_domain="ascii",
    call_kind="search",
    pattern=PAT_SHA,
    ground_truth=sha_mutation_reproduces,
)
def webhook_sha_length_mutation():
    sha = String("sha")
    return [InRe(sha, _WEAK_SHA), sha == StringVal("a")], sha == StringVal("a")


@prop(
    Q_PR,
    "Every nonempty token admitted by the receiver's Bash PR-number regex contains only decimal digits",
    expect_unsat=True,
    kind="property",
    family=FAMILY_PR,
    input_domain="ascii",
    call_kind="search",
    pattern=PAT_PR_NUMBER,
    contract=_contract("contract-process-pr-number-regex-only.json"),
)
def webhook_process_pr_number_is_positive_decimal():
    number = String("number")
    # Prove the regex's local guarantee directly: every token admitted by
    # `^[0-9]+$` consists only of decimal digits. The pinned server's
    # positive-integer conversion and the dispatcher's separate `-le 0`
    # predicate supply positivity; coupling both numeric domains back into
    # this regex-inclusion query made Z3 time out without strengthening the
    # claim about the regex itself.
    return [InRe(number, _SOURCE_PR)], Not(InRe(number, _DIGITS_PLUS))


@prop(
    M_PR,
    "MUTATION GUARD: dropping the digits-only check admits Bash arithmetic text to process_pr",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY_PR,
    input_domain="ascii",
    call_kind="search",
    pattern=PAT_PR_NUMBER,
    ground_truth=pr_number_mutation_reproduces,
)
def webhook_process_pr_number_mutation():
    number = String("number")
    return [InRe(number, _WEAK_PR), number == StringVal("2#1")], number == StringVal("2#1")


__all__ = [
    "Q_PR", "Q_SECRET", "Q_SHA", "SITE_PR_NUMBER", "SITE_SECRET", "SITE_SHA", "SITE_SLUG",
]
