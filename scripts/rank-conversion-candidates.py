#!/usr/bin/env python3
"""Rank conversion-wave candidates (Gate 1–2). Deterministic; no Z3.

Reads inventory or scanner NDJSON, applies drop rules, scores survivors,
emits a frozen shortlist JSON. Cluster vocabulary is the only per-cluster
input.

Usage:
  python scripts/rank-conversion-candidates.py \\
    --ndjson properties/generated/openwrt_packages-inventory.ndjson \\
    --vocab init.d,uci,nft,iptables,firewall,passwd,ddns,mwan,banip,adblock,pbr,hotplug \\
    --limit 15 -o properties/generated/openwrt_packages_rank.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

# OpenWrt packages conversion-wave default (docs/CLUSTER-CONVERSION.md).
DEFAULT_VOCAB = (
    "init.d",
    "uci",
    "nft",
    "iptables",
    "firewall",
    "passwd",
    "ddns",
    "mwan",
    "banip",
    "adblock",
    "pbr",
    "hotplug",
)

DROP_TEST_NAMES = frozenset({"test-version.sh", "run_tests.sh"})
_TEST_NAME_SUFFIX = ".test.sh"
_DROP_PATH_SEGS = frozenset({"tests", "testdata", "fixtures"})

# Regex metacharacters that make a pattern non-literal.
_METACHAR = frozenset(".^$*+?{}[]()|\\")
_IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_INTERP = re.compile(r"\$\{?[A-Za-z_][A-Za-z0-9_]*\}?")
_CAPTURE_BRE = re.compile(r"\\\(|\\\)")
_CAPTURE_ERE = re.compile(r"(?<!\\)\((?!\?)")
_CHARSET = re.compile(r"(?<!\\)\[")
_UNTRUSTED = (
    "argv",
    "http",
    "https",
    "luci",
    "wan",
    "wget",
    "curl",
    "hostname",
    "unauth",
)
_CONFIG = ("uci", "config", "luci")
_INTERNAL = (
    "ip route",
    "pointopoint",
    "feature",
    "/proc/",
    "ip addr",
    "ip link",
)

# Seed sites the OpenWrt plan asks the rank JSON to explain if dropped.
OPENWRT_SEEDS = (
    {
        "id": "pbr-sanitizer",
        "needle_path": "net/pbr/files/etc/init.d/pbr",
        "needle_pat": "!@#$%^&*()",
    },
    {
        "id": "ddns-private-ip",
        "needle_path": "dynamic_dns_functions.sh",
        "needle_pat": "(^0|^10\\.",
    },
    {
        "id": "mwan3-dev-capture",
        "needle_path": "mwan3.sh",
        "needle_pat": "dev (",
    },
)


def _path_of(rec: dict[str, Any]) -> str:
    site = str(rec.get("site") or rec.get("file") or "")
    # site is file:line:column — strip the last two numeric fields when present.
    parts = site.replace("\\", "/").split(":")
    if len(parts) >= 3 and parts[-1].isdigit() and parts[-2].isdigit():
        return ":".join(parts[:-2])
    return str(rec.get("file") or site)


def _path_segments(path: str) -> list[str]:
    return [p for p in path.replace("\\", "/").split("/") if p]


def drop_reason(rec: dict[str, Any]) -> str | None:
    """Return a drop reason or None to keep for scoring.

    Drop rules run *before* scoring so test-dir density cannot outrank a
    real init script.
    """
    path = _path_of(rec)
    segs = _path_segments(path)
    name = segs[-1] if segs else ""
    if any(s in _DROP_PATH_SEGS for s in segs):
        return "path-segment:tests|testdata|fixtures"
    if name in DROP_TEST_NAMES or name.endswith(_TEST_NAME_SUFFIX):
        return f"test-filename:{name}"
    pat = str(rec.get("pattern") or "")
    if not pat.strip():
        return "malformed:empty-pattern"
    if not (rec.get("site") or rec.get("file")):
        return "malformed:missing-site"
    if _IDENT.fullmatch(pat.lstrip("$")) and pat.startswith("$"):
        return "interpolated:$ident"
    if _INTERP.search(pat):
        return "interpolated"
    if pat and not any(c in _METACHAR for c in pat):
        return "literal-no-metachar"
    call_kind = str(rec.get("call_kind") or "")
    has_capture = bool(_CAPTURE_BRE.search(pat) or _CAPTURE_ERE.search(pat))
    has_charset = bool(_CHARSET.search(pat))
    if call_kind == "substitution" and not has_capture and not has_charset:
        return "substitution-no-capture-or-charset"
    if rec.get("encodable") is False or rec.get("compile_reason"):
        return f"unencodable:{rec.get('compile_reason') or 'false'}"
    return None


def _haystack(rec: dict[str, Any]) -> str:
    return " ".join(
        str(rec.get(k) or "")
        for k in ("site", "file", "pattern", "context_snippet")
    ).lower()


def score(rec: dict[str, Any], vocab: tuple[str, ...]) -> int:
    path = _path_of(rec).lower()
    hay = _haystack(rec)
    pat = str(rec.get("pattern") or "")
    pts = 0
    if any(tok.lower() in path or tok.lower() in hay for tok in vocab):
        pts += 2
    if any(tok in hay for tok in _UNTRUSTED):
        pts += 2
    if any(tok in hay for tok in _CONFIG):
        pts += 1
    if _CAPTURE_BRE.search(pat) or _CAPTURE_ERE.search(pat):
        pts += 2
    if _CHARSET.search(pat):
        pts += 2
    if rec.get("encodable") is True:
        pts += 1
    if any(tok in hay for tok in _INTERNAL):
        pts -= 2
    if _INTERP.search(pat):
        pts -= 3
    return pts


def rank_rows(
    records: list[dict[str, Any]],
    *,
    vocab: tuple[str, ...] = DEFAULT_VOCAB,
    limit: int = 15,
) -> dict[str, Any]:
    dropped: list[dict[str, Any]] = []
    survivors: list[dict[str, Any]] = []
    for rec in records:
        reason = drop_reason(rec)
        if reason:
            dropped.append(
                {
                    "site": rec.get("site") or rec.get("file"),
                    "pattern": rec.get("pattern"),
                    "reason": reason,
                }
            )
            continue
        survivors.append(rec)
    scored = []
    for rec in survivors:
        pts = score(rec, vocab)
        scored.append(
            {
                "score": pts,
                "site": rec.get("site"),
                "file": _path_of(rec),
                "pattern": rec.get("pattern"),
                "call_kind": rec.get("call_kind"),
                "encodable": rec.get("encodable"),
                "regex_id": rec.get("regex_id"),
            }
        )
    scored.sort(key=lambda r: (-int(r["score"]), str(r["site"] or "")))
    keep = scored[:limit]
    return {
        "schema_version": "1",
        "vocab": list(vocab),
        "limit": limit,
        "input_rows": len(records),
        "dropped_count": len(dropped),
        "survivor_count": len(survivors),
        "keep": keep,
        "dropped": dropped,
    }


def annotate_seeds(result: dict[str, Any], seeds: tuple[dict[str, str], ...] = OPENWRT_SEEDS) -> dict[str, Any]:
    dropped_idx = {
        (d.get("site") or "", d.get("pattern") or ""): d.get("reason")
        for d in result.get("dropped") or []
    }
    notes: dict[str, Any] = {}
    keep_pats = [(k.get("site") or "", k.get("pattern") or "") for k in result.get("keep") or []]
    all_keep = result.get("keep") or []
    for seed in seeds:
        sid = seed["id"]
        needle_path = seed["needle_path"]
        needle_pat = seed["needle_pat"]
        kept = [
            k
            for k in all_keep
            if needle_path in str(k.get("file") or k.get("site") or "")
            and needle_pat in str(k.get("pattern") or "")
        ]
        if kept:
            notes[sid] = {"status": "kept", "site": kept[0].get("site")}
            continue
        # Among dropped, find a matching path+pattern.
        hit = None
        for (site, pat), reason in dropped_idx.items():
            if needle_path in str(site) and needle_pat in str(pat):
                hit = {"status": "dropped", "reason": reason, "site": site}
                break
        if hit is None:
            # Survivors that didn't make top-N.
            notes[sid] = {"status": "not-in-top", "needle_path": needle_path}
        else:
            notes[sid] = hit
    result["seeds"] = notes
    return result


def load_ndjson(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if isinstance(rec, dict):
            rows.append(rec)
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ndjson", type=Path, required=True)
    ap.add_argument(
        "--vocab",
        default=",".join(DEFAULT_VOCAB),
        help="comma-separated path/vocab tokens",
    )
    ap.add_argument("--limit", type=int, default=15)
    ap.add_argument("-o", "--output", type=Path)
    ap.add_argument("--corpus", default="")
    args = ap.parse_args(argv)
    vocab = tuple(t.strip() for t in args.vocab.split(",") if t.strip())
    records = load_ndjson(args.ndjson)
    result = rank_rows(records, vocab=vocab, limit=args.limit)
    result["corpus"] = args.corpus or args.ndjson.stem.replace("-inventory", "")
    annotate_seeds(result)
    text = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(f"rank -> {args.output}: keep={len(result['keep'])} dropped={result['dropped_count']}")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
