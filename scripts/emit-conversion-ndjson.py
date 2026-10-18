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
    "OW-luci-adblock-tcpdump-filter-no-semicolon": 1,
    "OW-luci-netdevname-semicolon-admitted": 1,
    "OW-luci-firewall-mark-no-semicolon": 1,
    "OW-luci-dockerman-publish-host-capture": 3,
    "AI-aidevops-brief-tid-no-semicolon": 1,
    "AI-aidevops-cred-ident-no-semicolon": 1,
    "AI-aidevops-scope-heading-no-semicolon": 1,
    "AI-aidevops-brief-tid-capture": 3,
    "AI-aidevops-gh-issue-digit-capture": 3,
    "AE-aidevops-secret-read-basename-coverage": 2,
    "MY-mycelium-ssh-key-prefix-no-semicolon": 1,
    "MY-mycelium-awg-dialect-key-no-semicolon": 1,
    "MY-mycelium-alpn-h2-line-no-semicolon": 1,
    "AI-claude-plugins-cli-flag-no-semicolon": 1,
    "AI-claude-plugins-skill-ref-no-semicolon": 1,
    "AI-claude-plugins-git-clean-e-bundle-no-semicolon": 1,
    "FC-forge-cli-url-password-no-space": 1,
    "FC-forge-cli-dmm-value-no-semicolon": 1,
    "FC-forge-cli-llm-userinfo-no-at": 1,
    "FC-forge-cli-jaas-escaped-quote-covered": 2,
    "FC-forge-cli-sensitive-env-key-covered": 2,
    "FC-forge-cli-sensitive-env-helper-redacts": 4,
    "TC-tracecat-origin-slug-safe-image": 4,
    "TC-mcp-env-key-accepts-terminal-lf": 5,
    "TC-mcp-server-name-separators-excluded": 1,
    "TC-artifact-path-segment-safe-image": 4,
    "TC-workspace-sync-path-segment-component-image": 4,
    "TC-rbac-scope-nonstar-glob-metacharacters-excluded": 1,
    "TC-table-identifier-double-quote-excluded": 1,
    "TC-sandbox-env-key-excludes-equals": 1,
    "MY-mycelium-release-preflight-requires-64-hex": 2,
    "MY-mycelium-20r2-release-preflight-requires-64-hex": 2,
    "MC-malcontent-cve48384-embedded-cr-excludes-lf": 1,
    "MC-malcontent-author-metadata-extra-markdown-link": 3,
    "MC-malcontent-description-metadata-extra-markdown-link": 3,
    "AN-anax-orgname-denylist-validation": 1,
    "AA-autoar-html-text-escape-codepoint-image": 4,
    "JE-json-editor-enum-string-html-text-codepoint-image": 4,
    "AA-autoar-jsendpoint-assignment-capture-delimiter": 1,
    "AA-autoar-jsendpoint-loopback-script-src-fetch": 3,
    "AA-autoar-phase-log-module-component-safe": 1,
    "DF-dogfood-shell-normalize-fixpoint": 3,
    "DF-dogfood-shell-normalize-idempotent": 3,
    "PY-doberman-windows-root-token": 2,
    "PY-doberman-disk-wipe-token": 2,
    "LH-llm-honeypot-private-ip-192-168-coverage": 2,
    "LH-llm-honeypot-private-ip-rfc1918-redaction": 3,
    "LH-llm-honeypot-tor-failure-only-response-rejected": 3,
    "LH-llm-honeypot-tor-newnym-response-sequencing": 3,
    "PA-panther-staged-secrets-file-excluded-from-review-prompt": 3,
    "IH-inhale-file-url-output-root-confinement": 3,
    "IH-inhale-directory-url-output-root-confinement": 3,
    "ME-oauth2-pkce-s256-base64url": 4,
    "ME-rn-bare-pkce-s256-base64url": 4,
    "ME-rn-expo-pkce-s256-base64url": 4,
    "ME-oauth2-webauthn-base64url": 4,
    "ME-passkey-base64url": 4,
    "ME-wallet-kit-base64url": 4,
    "ME-webauthn-base64url": 4,
    "ME-provider-webauthn-base64url": 4,
    "ME-rn-bare-dpop-base64url": 4,
    "ME-provider-dpop-base64url": 4,
    "DB-codex-apply-patch-file-target-path": 3,
    "DB-codex-apply-patch-move-target-path": 3,
    "RR-route-segment-allowed-alphabet": 1,
    "RR-navigation-param-control-characters-rejected": 1,
    "AE-aidevops-predispatch-cited-file-traversal-read": 3,
    "AE-aidevops-predispatch-threshold-leading-zero-fail-open": 3,
    # Full regular-language inclusion against independently composed contract
    # languages; unlike bounded shape-5 rule diffs, these are source invariants.
    "AE-aidevops-webhook-secret-env-identifier": 6,
    "AE-aidevops-webhook-check-sha-token": 6,
    "AE-aidevops-webhook-process-pr-number": 6,
}
WAVE_ID_BY_PROPERTY = {
    # This follow-up is a separate renderer-image gate from the five-property
    # helper inventory wave; keep its provenance and close-out attribution.
    "FC-forge-cli-sensitive-env-helper-redacts": "forge-cli_helper_image",
    "MC-malcontent-author-metadata-extra-markdown-link": "malcontent_author_markdown_20r2",
    "MC-malcontent-description-metadata-extra-markdown-link": "malcontent_description_markdown_20r2",
}


def _regex_id(name: str) -> str:
    return hashlib.sha256(name.encode("utf-8")).hexdigest()[:32]


def row_from_run(
    name: str,
    entry: dict,
    result: dict,
    corpus: str,
    wave_id: str | None = None,
    idiom_bucket: str | None = None,
) -> dict:
    domain = entry.get("domain") or result.get("domain")
    if not isinstance(domain, str) or not domain.strip():
        raise SystemExit(f"error: {name} missing top-level domain")
    if name not in SHAPE:
        raise SystemExit(f"error: {name} missing SHAPE entry (fail closed)")
    gt = result.get("ground_truth")
    engines = result.get("engine_versions")
    if (
        not isinstance(engines, dict)
        or any(
            not isinstance(version, str)
            or not version.strip()
            or version == "?"
            for version in (engines.get("python"), engines.get("z3"))
        )
    ):
        raise SystemExit(
            f"error: {name} missing engine_versions "
            "(python+z3 required by docs/CLUSTER-CONVERSION.md)"
        )
    rec = {
        "schema_version": "1",
        "regex_id": _regex_id(name),
        "kind": entry["kind"],
        "corpus": corpus,
        "result": result.get("result"),
        "site": (entry.get("contract") or {}).get("site") or name,
        "shape": SHAPE[name],
        "ground_truth_status": gt if isinstance(gt, str) else None,
        "ground_truth": None,
        "disclosure": None,
        "witness": None,
        "domain": domain,
        "name": name,
        "family": entry.get("family"),
        # Wave join keys live at scanner-row TOP level (#554). Never inside
        # `contract` — property_contract.schema.json is additionalProperties:false.
        "wave_id": wave_id,
        "idiom_bucket": idiom_bucket,
        "product_reportable": product_reportable(entry),
        "contract": entry.get("contract"),
        "synthesized": False,
        "engine_versions": {
            "python": engines["python"],
            "z3": engines["z3"],
        },
    }
    return rec


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--family", required=True)
    ap.add_argument("--corpus", required=True)
    ap.add_argument("--wave-id", required=True, help="e.g. openwrt_packages_w2")
    ap.add_argument(
        "--idiom-bucket",
        required=True,
        help="Idiom slice label, e.g. image-and-ddns-json",
    )
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
        rec = row_from_run(
            name,
            entry,
            res,
            args.corpus,
            wave_id=WAVE_ID_BY_PROPERTY.get(name, args.wave_id),
            idiom_bucket=args.idiom_bucket,
        )
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
