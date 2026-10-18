"""Exact-pin Doberman secret-store path coverage properties."""

from __future__ import annotations

import json
import re
from pathlib import Path

from z3 import AllChar, Concat, InRe, Not, Range, Re, Star, String, Union

from regexproof.harness.core import prop


_ROOT = Path(__file__).resolve().parents[2]
_CONTRACT = json.loads(
    (
        _ROOT
        / "properties/calibration/2026-10-15-autonomous-doberman-win-secret-path-20r2/contract.json"
    ).read_text(encoding="utf-8")
)

SECRET_PATH_PATTERN = r"""(?ix)
    (?:^|/)\.env(?:\.[\w.-]+)?$       # .env, .env.local, .env.production
    | (?:^|[./])env$                  # app.env / prod.env / .env (any .env file)
    | \.pem$                          # certificates / keys
    | \.key$                          # private keys
    | (?:^|/)id_rsa[\w.-]*$           # ssh private keys
    | (?:^|/)id_ed25519[\w.-]*$
    | (?:^|/)\.npmrc$                 # often carries auth tokens
    | (?:^|/)credentials$             # aws/gcloud credentials files
    """
_SECRET_PATH_SOURCE = re.compile(SECRET_PATH_PATTERN)
_WINDOWS_INPUT = re.compile(
    r"[A-Za-z]:\\(?:[A-Za-z0-9_. -]+\\)+(?:\.npmrc|credentials)"
)

_COMPONENT_CHAR = Union(
    Range("A", "Z"),
    Range("a", "z"),
    Range("0", "9"),
    Re("_"),
    Re("-"),
    Re("."),
    Re(" "),
)
_PATH_COMPONENT = Concat(_COMPONENT_CHAR, Star(_COMPONENT_CHAR))
_DRIVE_ABSOLUTE_PREFIX = Concat(
    Union(Range("A", "Z"), Range("a", "z")),
    Re(":"),
    Re("\\"),
    _PATH_COMPONENT,
    Star(Concat(Re("\\"), _PATH_COMPONENT)),
    Re("\\"),
)
_WINDOWS_SECRET_PATHS = Concat(
    _DRIVE_ABSOLUTE_PREFIX,
    Union(Re(".npmrc"), Re("credentials")),
)

# Restricted to the two basenames under review, the only relevant source
# alternatives are `(?:^|/)\.npmrc$` and `(?:^|/)credentials$`. Other
# alternatives in SECRET_PATH_PATTERN end in distinct suffixes and cannot
# match this domain. Inputs exclude LF, so Python `$` and end-of-string agree.
_ANY = AllChar(Re("").sort())
_SOURCE_RELEVANT_MATCHES = Union(
    Re(".npmrc"),
    Concat(Star(_ANY), Re("/.npmrc")),
    Re("credentials"),
    Concat(Star(_ANY), Re("/credentials")),
)
_POSIX_SECRET_PATH_CONTROLS = Union(
    Re("C:/repo/.npmrc"),
    Re("C:/repo/credentials"),
)


def _windows_miss_reproduced(witness: dict) -> bool:
    target = witness.get("s", "")
    return bool(
        _WINDOWS_INPUT.fullmatch(target)
        and _SECRET_PATH_SOURCE.search(target) is None
    )


@prop(
    "PY-doberman-secret-store-windows-miss",
    "BUG DEMO: a Windows drive path to .npmrc or credentials is not "
    "recognized by the pinned secret-store search regex",
    expect_unsat=False,
    ground_truth=_windows_miss_reproduced,
    kind="bug_demo",
    family="PY-doberman-secret-store-path",
    input_domain="ascii",
    call_kind="search",
    pattern=SECRET_PATH_PATTERN,
    contract=_CONTRACT,
)
def py_doberman_secret_store_windows_miss():
    s = String("s")
    return [InRe(s, _WINDOWS_SECRET_PATHS)], Not(
        InRe(s, _SOURCE_RELEVANT_MATCHES)
    )


@prop(
    "PY-doberman-secret-store-mutated-missing-credentials",
    "MUTATION GUARD: removing the credentials alternative must expose a "
    "POSIX secret-store path the remaining matcher misses",
    expect_unsat=False,
    kind="mutation_guard",
    family="PY-doberman-secret-store-path",
    input_domain="ascii",
)
def py_doberman_secret_store_mutated_missing_credentials():
    s = String("s")
    weakened = Union(
        Re(".npmrc"),
        Concat(Star(_ANY), Re("/.npmrc")),
    )
    return [InRe(s, _POSIX_SECRET_PATH_CONTROLS)], Not(InRe(s, weakened))
