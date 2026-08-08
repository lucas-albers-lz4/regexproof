"""Per-dialect case-fold closures (not pair lists).

Distinguishing probes:
  - Python: İ (U+0130) and ı (U+0131) fold into [i] under default Unicode.
  - RE2: those do NOT fold into [i] (verified divergence).
  - JS non-u: ß does NOT fold to SS.
"""

from __future__ import annotations

import unicodedata


def _simple_fold_char(ch: str) -> set[str]:
    """Unicode simple case fold closure for one character (Python-style)."""
    chars = {ch, ch.lower(), ch.upper(), ch.casefold()}
    # Expand one more hop for stability of the closure.
    out = set(chars)
    for c in list(chars):
        out.add(c.lower())
        out.add(c.upper())
        out.add(c.casefold())
    return {c for c in out if len(c) == 1}


def python_fold_closure(ch: str, *, ascii_only: bool = False) -> set[str]:
    if ascii_only:
        if ch.isascii() and ch.isalpha():
            return {ch.lower(), ch.upper()}
        return {ch}
    return _simple_fold_char(ch)


def re2_fold_closure(ch: str) -> set[str]:
    """RE2 simple fold — ASCII letters + Unicode folds that RE2 applies.

    RE2 does NOT fold U+0130/U+0131 into i (unlike Python). We approximate the
    RE2 table by excluding those distinguishing cases from the i-class.
    """
    base = _simple_fold_char(ch)
    if ch.lower() == "i" or ch in "İı\u0130\u0131":
        # Keep only ASCII i/I for the i class under RE2.
        if ch in "iI":
            return {"i", "I"}
        return {ch}
    # Drop İ/ı from other closures that Python would merge.
    return {c for c in base if c not in "İı\u0130\u0131"}


def js_nonsu_fold_closure(ch: str) -> set[str]:
    """JS without /u: ASCII case fold; non-ASCII maps to its uppercase form only.

    ß does not expand to SS (multi-char folds are out).
    """
    if ch.isascii() and ch.isalpha():
        return {ch.lower(), ch.upper()}
    # Single-char uppercase mapping only — no multi-char.
    up = ch.upper()
    if len(up) == 1 and up != ch:
        return {ch, up}
    lo = ch.lower()
    if len(lo) == 1 and lo != ch:
        return {ch, lo}
    return {ch}


def category_name(ch: str) -> str:
    return unicodedata.category(ch)
