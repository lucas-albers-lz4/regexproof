"""Stable regex_id: length-prefixed SHA-256 prefix (Phase 1→2 invariant).

Formula (issue #14 / #17 / #97):
  sha256(lp(repo) || lp(pattern) || lp(flags) || lp(dialect) || lp(call_kind) || lp(site) [|| lp(domain)])[:32]

where lp(s) = uint32_be(len(utf8(s))) || utf8(s). All fields are
length-prefixed so delimiter collisions cannot conflate components.
Unencodability reasons are never folded into the hash.

Schema v2 adds domain as the 7th component. When domain is the default
("ascii"), it is omitted from the hash to preserve backward-compat with
v1 IDs. Non-default domains (e.g. "wide") produce distinct IDs.
"""

from __future__ import annotations

import hashlib

from regexproof.kinds import validate_call_kind, validate_dialect, validate_domain

DEFAULT_DOMAIN = "ascii"

# Wave-2 P2 (#97/#105) formula marker. Wave-3 hard-fails in
# check_corpus_coverage when this does not match the expected post-migration
# id_formula string used in fraction artifacts.
REGEX_ID_FORMULA_VERSION = "v2-domain-optional-ascii-default"


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
    domain: str = DEFAULT_DOMAIN,
) -> str:
    """Return 32 hex chars identifying (repo, pattern, flags, dialect, call_kind, site[, domain]).

    `site` must be `file:line:column`.
    When ``domain`` equals the default ("ascii"), it is not folded into the
    hash — this preserves backward-compat with schema-v1 IDs.
    """
    validate_dialect(dialect)
    validate_call_kind(call_kind)
    validate_domain(domain)
    payload = (
        _lp(repo)
        + _lp(pattern)
        + _lp(flags)
        + _lp(dialect)
        + _lp(call_kind)
        + _lp(site)
    )
    if domain != DEFAULT_DOMAIN:
        payload += _lp(domain)
    return hashlib.sha256(payload).hexdigest()[:32]
