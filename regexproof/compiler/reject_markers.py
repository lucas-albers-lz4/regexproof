"""Shared PCRE reject-marker table (fix-wave #73 consolidation).

Used by ``compile_pcre`` and ``helpers/pcre2/match.py`` so the helper gate
cannot drift from the compiler (previously missing ``\\R``/``\\X``/``\\C``).
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
