"""Wave 10 (#579): target-feed catalog and query-share (not a day-cap raise).

Density evidence is measured from committed gate decisions. A 30–40%
*query* share toward high-density feeds is applied only when that
evidence clears the skip-class median floor. ``DAILY_MINE_CAP`` stays 10.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Sequence

from regexproof.mine.queue import DEFAULT_DAILY_CAP

FEED_DENSITY_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "generated"
    / "feed_density.json"
)

# Skip-class cutoff from Wave 9 (#578). A feed must beat this median on
# walked regex_sites before it takes query-budget share.
SITE_MEDIAN_FLOOR = 50
TARGET_QUERY_SHARE = 0.35
SKIP_CLASS_CAP = 50

# GitHub code-search queries (no repo: qualifiers — same contract as SEARCH_QUERIES).
FEED_QUERIES: tuple[tuple[str, str], ...] = (
    # rules / WAF / IDS
    ("rules", "filename:crs-setup.conf OR filename:REQUEST-942-APPLICATION-ATTACK-SQLI.conf"),
    ("rules", "filename:coraza.conf OR filename:coraza.yaml"),
    ("rules", "filename:suricata.yaml path:rules"),
    ("rules", "path:rules filename:snort.conf OR filename:local.rules"),
    ("rules", "filename:sigma.yml OR filename:sigma.yaml path:rules"),
    ("rules", "filename:qlpack.yml OR extension:ql path:ql"),
    # registry-shaped validators (package paths, not generic filename:validator.js)
    ("validators", "filename:isEmail.js path:src OR filename:isFQDN.js path:src"),
    ("validators", "filename:email_validator.py OR filename:govalidator.go"),
    # BusyBox / OpenWrt-adjacent (same density class as packages/luci)
    ("other", "filename:procd.c OR filename:netifd.c"),
    ("other", "filename:APKBUILD path:main OR filename:fstools"),
)

OSV_WITNESS_NOTE = (
    "osv.dev / GitHub Advisory DB is a witness feed (pinned repo+commit), "
    "not a live drain source. Do not spend primary probe budget here."
)


def feed_query_strings() -> list[str]:
    return [q for _fam, q in FEED_QUERIES]


def family_for_feed_query(query: str) -> str | None:
    for fam, q in FEED_QUERIES:
        if q == query:
            return fam
    return None


def median(values: Sequence[int]) -> float | None:
    xs = sorted(int(v) for v in values)
    if not xs:
        return None
    n = len(xs)
    mid = n // 2
    if n % 2:
        return float(xs[mid])
    return (xs[mid - 1] + xs[mid]) / 2.0


def query_share_n(budget: int, *, share: float = TARGET_QUERY_SHARE) -> int:
    n = round(max(0, budget) * float(share))
    return max(0, min(n, budget))


def load_family_medians(path: Path | None = None) -> dict[str, float]:
    p = path if path is not None else FEED_DENSITY_PATH
    if not p.is_file():
        return {}
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, TypeError):
        return {}
    families = doc.get("families") if isinstance(doc, dict) else None
    if not isinstance(families, dict):
        return {}
    out: dict[str, float] = {}
    for name, body in families.items():
        if not isinstance(body, dict):
            continue
        med = body.get("median_regex_sites")
        if isinstance(med, (int, float)):
            out[str(name)] = float(med)
    return out


def evidence_allows_share(family_medians: dict[str, float]) -> bool:
    """Shift query share when the *rules* feed (highest proven density) clears the floor.

    Generic ``validators`` GitHub filename queries do **not** qualify (Wave 10
    measurement: median 11). Named-package validator queries still ride along
    once rules evidence opens the share.
    """
    rules = family_medians.get("rules")
    return rules is not None and rules >= SITE_MEDIAN_FLOOR


def select_queries(
    legacy: Sequence[str],
    *,
    budget: int,
    family_medians: dict[str, float] | None = None,
    feed_queries: Sequence[str] | None = None,
) -> list[str]:
    """Return the query list for one mine run. Never raises DAILY_MINE_CAP."""
    feeds = list(feed_queries if feed_queries is not None else feed_query_strings())
    seen: set[str] = set()
    out: list[str] = []
    allow = evidence_allows_share(family_medians or {})
    share_n = query_share_n(budget) if allow else 0
    for q in feeds[:share_n]:
        if q and q not in seen:
            seen.add(q)
            out.append(q)
    for q in legacy:
        if q and q not in seen:
            seen.add(q)
            out.append(q)
    return out


def daily_cap_unchanged() -> dict[str, Any]:
    return {
        "DAILY_MINE_CAP_default": DEFAULT_DAILY_CAP,
        "raised": False,
        "note": "Wave 10 moves query share only; the calendar day admit cap stays 10.",
    }
