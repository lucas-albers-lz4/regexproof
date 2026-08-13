"""Shared reject-marker tables (fix-wave #73; Wave-3 perl #113).

Used by dialect compilers and helpers so the helper gate cannot drift from
the compiler.
"""

from __future__ import annotations

import re

# Odd backslash chain = real Unicode property escape; even chain = escaped
# literal. Same tokenizer as regexproof.harness.gates.P_TOKEN (#226 / #362).
_UNICODE_PROP_BRACED = re.compile(r"(?<!\\)(?:\\\\)*\\(?:p|P)\{")
_UNICODE_PROP_BRACELESS = re.compile(r"(?<!\\)(?:\\\\)*\\(?:p|P)(?!\{)[A-Za-z]")


def unicode_prop_unencodable(pattern: str) -> str | None:
    """Return ``unicode-prop`` when *pattern* contains a real ``\\p``/``\\P`` token."""
    if _UNICODE_PROP_BRACED.search(pattern) or _UNICODE_PROP_BRACELESS.search(pattern):
        return "unicode-prop"
    return None


# (substring, unencodable_reason)
PCRE_REJECT_MARKERS: tuple[tuple[str, str], ...] = (
    ("(?=", "lookaround"),
    ("(?!", "lookaround"),
    ("(?<=", "lookaround"),
    ("(?<!", "lookaround"),
    ("\\k<", "backref"),
    ("\\g<", "backref"),
    ("(?(", "conditional"),
    ("\\K", "reset"),
    ("\\G", "g-anchor"),
    ("\\R", "r-escape"),
    ("\\X", "x-escape"),
    ("\\C", "c-escape"),
)

# Perl: \\K is stripped (membership-transparent), not rejected.
# \\z/\\Z/\\A are absolute anchors — shared parse_pattern treats \\z as literal
# ``z``, so reject fail-closed rather than silently wrong mirrors.
PERL_REJECT_MARKERS: tuple[tuple[str, str], ...] = (
    ("(?=", "lookaround"),
    ("(?!", "lookaround"),
    ("(?<=", "lookaround"),
    ("(?<!", "lookaround"),
    ("(?(", "conditional"),
    ("(?{", "code-embed"),
    ("\\g{", "backref"),
    ("\\g<", "backref"),
    ("\\N{", "named-char"),
    ("\\h", "h-escape"),
    ("\\v", "v-escape"),
    ("\\Q", "quote-meta"),
    ("\\z", "z-anchor"),
    ("\\Z", "Z-anchor"),
    ("\\A", "A-anchor"),
    ("(?R)", "recursion"),
    ("(?&", "recursion"),
)
