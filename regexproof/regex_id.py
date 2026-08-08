"""Stable regex_id: length-prefixed SHA-256 prefix (Phase 1 invariant).

Formula (issue #14 / #17):
  sha256(lp(repo) || lp(pattern) || lp(flags) || lp(dialect) || lp(call_kind) || lp(site))[:32]

where lp(s) = uint32_be(len(utf8(s))) || utf8(s). All six fields are
length-prefixed so delimiter collisions cannot conflate components.
Unencodability reasons are never folded into the hash.
"""

from __future__ import annotations

import hashlib

from regexproof.kinds import validate_call_kind, validate_dialect


def _lp(s: str) -> bytes:
    encoded = s.encode("utf-8")
    return len(encoded).to_bytes(4, "big") + encoded


def make_regex_id(
    repo: str,
    pattern: str,
    flags: str,
    dialect: str,
    call_kind: str,
    site: str,
) -> str:
    """Return 32 hex chars identifying (repo, pattern, flags, dialect, call_kind, site).

    `site` must be `file:line:column`.
    """
    validate_dialect(dialect)
    validate_call_kind(call_kind)
    payload = (
        _lp(repo)
        + _lp(pattern)
        + _lp(flags)
        + _lp(dialect)
        + _lp(call_kind)
        + _lp(site)
    )
    return hashlib.sha256(payload).hexdigest()[:32]
