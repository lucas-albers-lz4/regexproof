"""Shared reject-marker tables (fix-wave #73; Wave-3 perl #113).

Used by dialect compilers and helpers so the helper gate cannot drift from
the compiler.
"""

from __future__ import annotations

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
    ("\\p{", "unicode-prop"),
    ("\\P{", "unicode-prop"),
    ("\\h", "h-escape"),
    ("\\v", "v-escape"),
    ("\\Q", "quote-meta"),
    ("\\z", "z-anchor"),
    ("\\Z", "Z-anchor"),
    ("\\A", "A-anchor"),
    ("(?R)", "recursion"),
    ("(?&", "recursion"),
)
