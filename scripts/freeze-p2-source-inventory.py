#!/usr/bin/env python3
"""Freeze exact-pin source regex-site identities for a PR2 cohort.

The output is a raw source inventory. It does not mark security boundaries,
adopt contracts, or count proof questions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_lines, atomic_write_text  # noqa: E402
from regexproof.mine.cohort_manifest import validate_manifest  # noqa: E402
from regexproof.mine.p2_source_inventory import (  # noqa: E402
    P2SourceInventoryError,
    build_source_inventory,
)


def _repo_mapping(values: list[str]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for value in values:
        repo_id, separator, path = value.partition("=")
        if not separator or not repo_id or not path:
            raise P2SourceInventoryError("--repo must use REPO_ID=CHECKOUT_PATH")
        if repo_id in result:
            raise P2SourceInventoryError(f"duplicate --repo mapping for {repo_id!r}")
        result[repo_id] = Path(path)
    return result


def _strict_json(text: str, *, source: Path) -> Any:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise P2SourceInventoryError(
                    f"duplicate JSON key {key!r} in {source}"
                )
            result[key] = value
        return result

    try:
        return json.loads(text, object_pairs_hook=reject_duplicates)
    except P2SourceInventoryError:
        raise
    except json.JSONDecodeError as exc:
        raise P2SourceInventoryError(
            f"invalid JSON in {source}:{exc.lineno}:{exc.colno}: {exc.msg}"
        ) from exc


def _output_dir(value: Path) -> Path:
    calibration_root = (ROOT / "properties" / "calibration").resolve()
    resolved = value.resolve()
    if not resolved.is_relative_to(calibration_root) or resolved == calibration_root:
        raise P2SourceInventoryError(
            "--out-dir must be a child of properties/calibration"
        )
    return resolved


def _site_lines(sites: list[dict[str, Any]]) -> list[str]:
    return [
        json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        for row in sites
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    checkout_group = parser.add_mutually_exclusive_group(required=True)
    checkout_group.add_argument(
        "--checkout-root", type=Path,
        help="derive each path as ROOT/<repo basename>-<frozen pin>",
    )
    checkout_group.add_argument(
        "--repo", action="append", default=None, metavar="REPO_ID=CHECKOUT_PATH",
        help="exact-pin local checkout; repeat for each available cohort member",
    )
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        raw_manifest = args.manifest.read_bytes()
        manifest = validate_manifest(
            _strict_json(raw_manifest.decode("utf-8"), source=args.manifest)
        )
        if args.checkout_root is not None:
            checkout_root = args.checkout_root
            repo_paths = {
                row["repo_id"]: checkout_root
                / f"{row['repo_id'].split('/')[-1]}-{row['pin']}"
                for row in manifest.get("repos", [])
            }
        else:
            repo_paths = _repo_mapping(args.repo or [])
        artifact, sites = build_source_inventory(
            manifest,
            repo_paths,
            cohort_manifest_sha256=hashlib.sha256(raw_manifest).hexdigest(),
        )
        out_dir = _output_dir(args.out_dir)
        site_lines = _site_lines(sites)
        atomic_write_lines(out_dir / "sites.ndjson", site_lines)
        atomic_write_text(
            out_dir / "inventory.json",
            json.dumps(artifact, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        )
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"freeze-p2-source-inventory: error: {exc}", file=sys.stderr)
        return 2

    for row in artifact["repositories"]:
        print(
            f"{row['repo_id']}: {row['status']} sites={row['site_count']}"
        )
    summary = artifact["summary"]
    print(
        f"cohort={artifact['cohort_id']} repos={summary['cohort_repositories']} "
        f"complete={summary['complete_repositories']} "
        f"incomplete={summary['incomplete_or_failed_repositories']} "
        f"source_sites={summary['source_sites']} "
        f"sha256={summary['source_sites_ndjson_sha256']}"
    )
    return 0 if summary["incomplete_or_failed_repositories"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
