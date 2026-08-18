#!/usr/bin/env python3
"""Generate ``<corpus>_conversion.ndjson`` from harness ``run_one`` records.

Maps harness ``ground_truth`` (string) → scanner ``ground_truth_status``.
Requires top-level ``domain``. Product rows only (mutation guards omitted).

Usage:
  python scripts/emit-conversion-ndjson.py --family OW-packages --corpus openwrt_packages
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.harness.contract import product_reportable  # noqa: E402
from regexproof.harness.core import REGISTRY, run_one  # noqa: E402

GEN = ROOT / "properties" / "generated"
SHAPE = {
    "OW-packages-hostname-no-semicolon": 1,
    "OW-packages-hostname-no-space": 1,
    "OW-packages-banip-expiry-no-semicolon": 1,
    "OW-packages-transip-token-truncation": 3,
    "OW-packages-wan-mark-hex-capture": 3,
    "OW-packages-sanitizer-image-no-semicolon": 4,
    "OW-packages-ipv4-regex-no-semicolon": 1,
    "OW-packages-expand-ipv6-nibble-capture": 3,
    "OW-packages-cloudflare-content-truncation": 3,
    "OW-packages-huawei-id-no-semicolon": 1,
    "OW-packages-aliyun-recordid-truncation": 3,
    "OW-packages-dnspod-recordid-no-semicolon": 1,
    "OW-packages-mosquitto-uci-quote-capture": 3,
    "OW-packages-nftset-passthrough-no-dot": 4,
}


def _regex_id(name: str) -> str:
    return hashlib.sha256(name.encode("utf-8")).hexdigest()[:32]


def row_from_run(name: str, entry: dict, result: dict, corpus: str) -> dict:
    domain = entry.get("domain") or result.get("domain")
    if not isinstance(domain, str) or not domain.strip():
        raise SystemExit(f"error: {name} missing top-level domain")
    gt = result.get("ground_truth")
    rec = {
        "schema_version": "1",
        "regex_id": _regex_id(name),
        "kind": entry["kind"],
        "corpus": corpus,
        "result": result.get("result"),
        "site": (entry.get("contract") or {}).get("site") or name,
        "shape": SHAPE.get(name),
        "ground_truth_status": gt if isinstance(gt, str) else None,
        "ground_truth": None,
        "disclosure": None,
        "witness": None,
        "domain": domain,
        "name": name,
        "family": entry.get("family"),
        "product_reportable": product_reportable(entry),
        "contract": entry.get("contract"),
        "synthesized": False,
    }
    return rec


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--family", required=True)
    ap.add_argument("--corpus", required=True)
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        help="default: properties/generated/<corpus>_conversion.ndjson",
    )
    args = ap.parse_args(argv)
    out = args.output or (GEN / f"{args.corpus}_conversion.ndjson")
    rows = []
    for name, entry in sorted(REGISTRY.items()):
        if entry.get("family") != args.family:
            continue
        if entry.get("kind") == "mutation_guard":
            continue
        res = run_one(name, entry, require_ground_truth=True)
        if not res.get("ok"):
            raise SystemExit(
                f"error: {name} harness run failed "
                f"(result={res.get('result')!r} ground_truth={res.get('ground_truth')!r})"
            )
        rec = row_from_run(name, entry, res, args.corpus)
        if not rec["product_reportable"]:
            raise SystemExit(f"error: {name} is not product_reportable")
        if not rec.get("domain"):
            raise SystemExit(f"error: {name} missing domain")
        rows.append(rec)
    out.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n" for r in rows)
    out.write_text(text, encoding="utf-8")
    print(f"conversion ndjson -> {out}: {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
