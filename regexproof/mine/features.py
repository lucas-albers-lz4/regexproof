"""Shared score-v1/v2 feature helpers (Fowler Move Function, #454).

Do not unify ``_repo_slug`` with ``mine.tree._repo_slug`` — different contracts.
"""

from __future__ import annotations

import math
import re
from datetime import date, datetime, timezone
from urllib.parse import urlparse

from regexproof.mine.feeds import FEED_QUERIES
from regexproof.mine.search import SEARCH_QUERIES

# Map exact SEARCH_QUERIES strings → family (order matches search.py comments).
_QUERY_FAMILY: dict[str, str] = {
    SEARCH_QUERIES[0]: "security",
    SEARCH_QUERIES[1]: "security",
    SEARCH_QUERIES[2]: "security",
    SEARCH_QUERIES[3]: "validators",
    SEARCH_QUERIES[4]: "validators",
    SEARCH_QUERIES[5]: "rules",
    SEARCH_QUERIES[6]: "rules",
    SEARCH_QUERIES[7]: "rules",
    SEARCH_QUERIES[8]: "testdata",
    SEARCH_QUERIES[9]: "testdata",
    SEARCH_QUERIES[10]: "security",  # .gitleaks.toml
    SEARCH_QUERIES[11]: "security",  # .trufflehog.yml/.toml
    SEARCH_QUERIES[12]: "security",  # secretlintrc
    SEARCH_QUERIES[13]: "rules",  # semgrep.yml/yaml (semgrep = rules family)
    SEARCH_QUERIES[14]: "security",  # secrets.yml/yaml
    SEARCH_QUERIES[15]: "rules",  # index.yar
    SEARCH_QUERIES[16]: "rules",  # path:signatures extension:yar
    SEARCH_QUERIES[17]: "rules",  # rules.yar path:rules
    SEARCH_QUERIES[18]: "validators",  # validator.py/validators.py path:src
    SEARCH_QUERIES[19]: "testdata",  # regex_test.go / regexp_test.go
}
_QUERY_FAMILY.update({q: fam for fam, q in FEED_QUERIES})


def _repo_slug(url: str) -> str:
    """Return ``owner/repo`` (or last path segment) from a GitHub-ish URL."""
    u = (url or "").strip()
    if u.startswith("git@"):
        try:
            path = u.split(":", 1)[1]
        except IndexError:
            return u
        parts = [p for p in path.split("/") if p]
        if len(parts) >= 2:
            return f"{parts[0]}/{parts[1].removesuffix('.git')}"
        return path.removesuffix(".git")
    parsed = urlparse(u)
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1].removesuffix('.git')}"
    if parts:
        return parts[0].removesuffix(".git")
    return u


def query_family(source_query: str) -> str:
    """Classify a search/source query into a density family.

    Exact ``SEARCH_QUERIES`` / ``FEED_QUERIES`` map first; fuzzy fallback
    for drifted historical ``source_query`` text. Keep ``_query_family`` as
    a compatibility alias.
    """
    q = (source_query or "").strip()
    if q in _QUERY_FAMILY:
        return _QUERY_FAMILY[q]
    # Fuzzy fallback if query text drifted slightly
    ql = q.lower()
    if "gitleaks" in ql or "detect-secrets" in ql or "trufflehog" in ql or "secretlint" in ql or "secrets." in ql:
        return "security"
    if "semgrep" in ql or "yara" in ql or "secrule" in ql or "extension:yar" in ql or ".yar" in ql or "yar " in ql:
        return "rules"
    if "crs-setup" in ql or "coraza" in ql or "suricata" in ql or "sigma.yml" in ql or "sigma.yaml" in ql or "qlpack" in ql or "snort" in ql:
        return "rules"
    if "validator" in ql or "isemail" in ql or "isfqdn" in ql or "govalidator" in ql:
        return "validators"
    if "testdata" in ql or "re_tests" in ql or "test_re" in ql or "regex_test" in ql or "regexp_test" in ql:
        return "testdata"
    if "procd" in ql or "netifd" in ql or "apkbuild" in ql or "fstools" in ql:
        return "other"
    return "other"


# Compatibility alias (scripts / older call sites).
_query_family = query_family


def _parse_pushed(pushed: str) -> date | None:
    s = (pushed or "").strip()
    if not s:
        return None
    # Accept YYYY-MM-DD or full ISO timestamps.
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", s)
    if not m:
        return None
    try:
        return date.fromisoformat(m.group(1))
    except ValueError:
        return None


def _recency_points(pushed: str, *, today: date | None = None) -> float:
    d = _parse_pushed(pushed)
    if d is None:
        return 0.0
    today = today or datetime.now(timezone.utc).date()
    age = (today - d).days
    if age < 0:
        age = 0
    if age <= 365:
        return 15.0
    if age <= 365 * 3:
        return 5.0
    return 0.0


def _stars_points(stars: int) -> float:
    return float(min(25, math.floor(8 * math.log10(max(0, stars) + 1))))
