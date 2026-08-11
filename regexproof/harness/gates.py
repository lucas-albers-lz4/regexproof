r"""Registration gates (design #213 D7/S1 + \p gate, Phase 2 — PR A).

Two gates run at registration for every property that declares a source
pattern:

1. **\p gate** (#226): reject any real `\p{`/`\P{` token (odd backslash chain)
   — measured: from_ecma2020 silently literalizes \p; the mirror has no Unicode
   property encoding. Even-chain escaped literals (`\\p{L}`) pass.
2. **D7 structural gate** (S1 + S1-parser): the pattern is parsed by the SAME
   Node-based parser the D14 oracle uses (helpers/ecma/parse.mjs, regexpp —
   never hand-rolled regex-on-regex). The gate applies the mechanical rules to
   the AST-derived structure report:
   - anchored-definition: single top-level alternative (no top-level
     alternation), leading `^` AND trailing `$`. Known conservative
     false-positive: `^a$|^b$` fails even though every branch is anchored —
     rewrite as `^(?:a|b)$` (documented).
   - wrap-validity: every top-level alternative starts with `.*` AND ends with
     `.*` (a `.*a|b` unparenthesized wrap fails — alternative 2 is unwrapped).
   - balanced grouping: a parse success implies balanced groups (regexpp would
     reject otherwise); the fixture table covers escaped parens, non-capturing
     groups, and anchor-looking chars in classes.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

NODE = "node"
PARSE_MJS = Path(__file__).resolve().parent.parent.parent / "helpers" / "ecma" / "parse.mjs"

# The \p tokenizer (p_gate.py, PR #226): odd backslash chain = real property
# escape; even chain = escaped literal. Both cases \p and \P.
P_TOKEN = re.compile(r"(?<!\\)(?:\\\\)*\\(?:p|P)\{")


class RegistrationError(Exception):
    """A property failed a registration gate. Raised at registration/validation
    time with the failing check and the rewrite suggestion."""


def check_p_gate(pattern: str) -> None:
    r"""Reject real \p{}/\P{ tokens. Escaped literals (even backslash chain)
    pass. Measured basis: from_ecma2020 silently literalizes \p (identity
    escape, never an error) — the U4 no-silent-folding rule forces rejection."""
    m = P_TOKEN.search(pattern)
    if m:
        raise RegistrationError(
            f"pattern contains a real \\p{{}}/\\P{{}} property escape at "
            f"position {m.start()}: {pattern!r}. The harness has no Unicode "
            "property encoding (from_ecma2020 silently literalizes \\p — "
            "measured). Rewrite: expand to explicit character classes, or use "
            "the escaped-literal form \\\\p if literal text is intended."
        )


def _structure(pattern: str, flags: str = "") -> dict:
    """Parse the pattern via the Node/regexpp parser and return the structure
    report. Raises RegistrationError on parse failure or parser absence."""
    try:
        p = subprocess.run(
            [NODE, str(PARSE_MJS), pattern, flags],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except FileNotFoundError:
        raise RegistrationError(
            "node is required for the D7 registration gate "
            "(helpers/ecma/parse.mjs) but is not on PATH."
        )
    except subprocess.TimeoutExpired:
        raise RegistrationError(f"registration parser timed out on {pattern!r}")
    try:
        d = json.loads(p.stdout)
    except json.JSONDecodeError:
        raise RegistrationError(
            f"registration parser produced no JSON for {pattern!r}: "
            f"{p.stderr.strip()[:120]}"
        )
    if not d.get("ok"):
        raise RegistrationError(
            f"pattern {pattern!r} is not encodable: "
            f"{d.get('unencodable_reason') or d.get('error')}"
        )
    return d["structure"]


def check_anchored(pattern: str, flags: str = "") -> None:
    """Anchored-definition rule (D7): single top-level alternative, leading ^
    AND trailing $. `^a$|^b$` is the documented conservative false-positive."""
    s = _structure(pattern, flags)
    if s["top_level_alternation"]:
        raise RegistrationError(
            f"anchored pattern {pattern!r} has top-level alternation — every "
            "branch must be fully anchored AND the alternation grouped "
            "(`^(?:a|b)$`, not `^a$|^b$` — the known conservative "
            "false-positive, documented in the design)."
        )
    alt = s["alternatives"][0]
    if not (alt["leading_anchor"] and alt["trailing_anchor"]):
        raise RegistrationError(
            f"anchored pattern {pattern!r} must have top-level ^ AND $ — "
            f"measured: leading={alt['leading_anchor']} "
            f"trailing={alt['trailing_anchor']}. Partial anchors (`^abc`, "
            "`abc$`) change the search language and fail registration."
        )


def check_wrap(pattern: str, flags: str = "") -> None:
    """Wrap-validity rule (D7): EVERY top-level alternative must start with
    `.*` and end with `.*`. Catches unparenthesized wraps (`.*a|b`) and
    unwrapped alternatives."""
    s = _structure(pattern, flags)
    bad = []
    for i, alt in enumerate(s["alternatives"]):
        if not (alt["leading_dotstar"] and alt["trailing_dotstar"]):
            bad.append(i)
    if bad:
        raise RegistrationError(
            f"search_wrapped pattern {pattern!r} has unwrapped alternative(s) "
            f"{bad} — every top-level alternative needs `.*` prefix AND `.*` "
            "suffix (a `.*a|b` unparenthesized wrap silently changes the "
            "language). Wrap as `.*(?:a|b).*`."
        )


def validate_pattern(
    pattern: str,
    flags: str = "",
    *,
    anchored: bool = False,
    search_wrapped: bool = False,
) -> None:
    """Full registration validation for a declared source pattern."""
    check_p_gate(pattern)
    if search_wrapped:
        check_wrap(pattern, flags)
    if anchored:
        check_anchored(pattern, flags)
