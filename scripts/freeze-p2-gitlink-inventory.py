#!/usr/bin/env python3
"""Freeze raw P2 regex sites from independently verified Gitlink checkouts.

This produces an additive submodule inventory. It does not change the frozen
root-repository inventory or classify sites as security boundaries.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_lines, atomic_write_text  # noqa: E402
from regexproof.mine import p2_source_inventory as p2_inventory  # noqa: E402


class GitlinkInventoryError(ValueError):
    """Raised when a child source or its parent binding cannot be verified."""


def _strict_json(path: Path) -> Any:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise GitlinkInventoryError(f"{path}: duplicate JSON key {key!r}")
            result[key] = value
        return result

    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
    except OSError as exc:
        raise GitlinkInventoryError(f"cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise GitlinkInventoryError(f"invalid JSON in {path}: {exc.msg}") from exc


def _git(path: Path, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(path), *args],
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise GitlinkInventoryError(f"git {' '.join(args)} failed: {exc}") from exc
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip() or "command failed"
        raise GitlinkInventoryError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout.strip()


def _gitlinks(path: Path) -> list[dict[str, str]]:
    raw = subprocess.run(
        ["git", "-C", str(path), "ls-tree", "-rz", "HEAD"],
        check=False,
        capture_output=True,
        timeout=30,
    )
    if raw.returncode:
        detail = raw.stderr.decode("utf-8", "replace").strip() or "ls-tree failed"
        raise GitlinkInventoryError(f"cannot enumerate child gitlinks: {detail}")
    result = []
    for item in raw.stdout.split(b"\0"):
        if not item:
            continue
        header, separator, path_bytes = item.partition(b"\t")
        fields = header.decode("ascii").split()
        if separator and len(fields) == 3 and fields[:2] == ["160000", "commit"]:
            result.append({"path": path_bytes.decode("utf-8"), "commit_oid": fields[2]})
    return result


def _blob(path: Path, relative: str) -> tuple[str, str]:
    raw = subprocess.run(
        ["git", "--literal-pathspecs", "-C", str(path), "ls-tree", "-z", "HEAD", "--", relative],
        check=False,
        capture_output=True,
        timeout=30,
    )
    if raw.returncode:
        detail = raw.stderr.decode("utf-8", "replace").strip() or "ls-tree failed"
        raise GitlinkInventoryError(f"cannot bind {relative!r} to child tree: {detail}")
    rows = []
    for item in raw.stdout.split(b"\0"):
        if not item:
            continue
        header, separator, filename = item.partition(b"\t")
        fields = header.decode("ascii").split()
        if separator and filename.decode("utf-8", "surrogateescape") == relative:
            if len(fields) == 3 and fields[1] == "blob":
                rows.append((fields[0], fields[2]))
    if len(rows) != 1:
        raise GitlinkInventoryError(f"expected one child-tree blob for {relative!r}; found {len(rows)}")
    return rows[0]


def _dogfood_module() -> Any:
    path = ROOT / "scripts" / "dogfood-singleton-analysis.py"
    spec = importlib.util.spec_from_file_location("regexproof_p2_gitlink_dogfood", path)
    if spec is None or spec.loader is None:
        raise GitlinkInventoryError(f"cannot load registered extractor {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _checkout_map(values: list[str]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for value in values:
        gitlink_path, separator, checkout = value.partition("=")
        if not separator or not gitlink_path or not checkout or gitlink_path in result:
            raise GitlinkInventoryError("--checkout must use a unique GITLINK_PATH=CHECKOUT_PATH")
        result[gitlink_path] = Path(checkout)
    return result


def _site_line(row: dict[str, Any]) -> str:
    return json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _extract_gitlink(
    row: dict[str, Any], checkout: Path, parent: dict[str, Any], dogfood: Any,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    gitlink_path = row["path"]
    checkout = checkout.resolve(strict=True)
    if not checkout.is_dir():
        raise GitlinkInventoryError(f"{gitlink_path}: checkout is not a directory")
    commit = _git(checkout, "rev-parse", "HEAD")
    if commit != row["commit"]:
        raise GitlinkInventoryError(f"{gitlink_path}: HEAD {commit} differs from Gitlink {row['commit']}")
    tree = _git(checkout, "rev-parse", "HEAD^{tree}")
    if tree != row["object_tree_oid"]:
        raise GitlinkInventoryError(f"{gitlink_path}: tree {tree} differs from recorded {row['object_tree_oid']}")
    if p2_inventory._normalized_url(_git(checkout, "remote", "get-url", "origin")) != p2_inventory._normalized_url(row["repository_url"]):
        raise GitlinkInventoryError(f"{gitlink_path}: checkout origin does not match verified source URL")
    if _git(checkout, "status", "--porcelain", "--untracked-files=all"):
        raise GitlinkInventoryError(f"{gitlink_path}: checkout is dirty")

    include_hidden = True
    p2_inventory._check_symlink_reads(checkout, dogfood, include_hidden=include_hidden)
    nested = _gitlinks(checkout)
    extensions = p2_inventory._FAMILY_EXTENSIONS[parent["dialect_family"]]
    dialects = p2_inventory._FAMILY_DIALECTS[parent["dialect_family"]]
    kwargs: dict[str, Any] = {"dir_mode": True, "include_hidden": include_hidden}
    if extensions is not None:
        kwargs["exts"] = set(extensions)
    scan = dogfood.extract_repo(parent["repo_id"], str(checkout), **kwargs)
    nested_paths = tuple(item["path"].rstrip("/") for item in nested)
    selected = [
        site for site in scan.records
        if site.get("dialect") in dialects
        and not any(
            site.get("file") == nested_path
            or str(site.get("file") or "").startswith(nested_path + "/")
            for nested_path in nested_paths
        )
    ]
    file_cache: dict[str, tuple[str, str, str]] = {}
    sites: list[dict[str, Any]] = []
    for site in selected:
        source_file = site.get("file")
        if not isinstance(source_file, str) or not source_file:
            raise GitlinkInventoryError(f"{gitlink_path}: extractor emitted a missing file path")
        posix = PurePosixPath(source_file)
        if posix.is_absolute() or ".." in posix.parts:
            raise GitlinkInventoryError(f"{gitlink_path}: extractor emitted unsafe path {source_file!r}")
        source_path_unresolved = checkout.joinpath(*posix.parts)
        source_path = source_path_unresolved.resolve(strict=True)
        if not source_path.is_relative_to(checkout) or not source_path.is_file():
            raise GitlinkInventoryError(f"{gitlink_path}: extracted path escapes child checkout")
        if source_file not in file_cache:
            git_mode, blob_oid = _blob(checkout, source_file)
            source_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
            file_cache[source_file] = (source_sha256, git_mode, blob_oid)
        source_sha256, git_mode, blob_oid = file_cache[source_file]
        line = int(site["line"])
        column = int(site["column"])
        identity = [
            parent["repo_id"], parent["pin"], gitlink_path, row["repository_url"],
            row["commit"], source_file, line, column, site.get("regex_id"), source_sha256,
        ]
        site_id = hashlib.sha256(
            json.dumps(identity, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        result = {
            "source_site_id": site_id,
            "cohort_id": parent["cohort_id"],
            "manifest_digest": parent["manifest_digest"],
            "repo_id": parent["repo_id"],
            "url": parent["url"],
            "pin": parent["pin"],
            "commit_tree_oid": parent["commit_tree_oid"],
            "gitlink_path": gitlink_path,
            "gitlink_url": row["repository_url"],
            "gitlink_commit": row["commit"],
            "gitlink_tree_oid": tree,
            "source_file": f"{gitlink_path}/{posix.as_posix()}",
            "child_source_file": posix.as_posix(),
            "source_file_sha256": source_sha256,
            "source_symlink_target": (
                os.readlink(source_path_unresolved) if source_path_unresolved.is_symlink() else None
            ),
            "git_mode": git_mode,
            "git_blob_oid": blob_oid,
            "regex_id": site.get("regex_id"),
            "site": site.get("site"),
            "line": line,
            "column": column,
            "pattern": site.get("pattern", ""),
            "flags": site.get("flags", ""),
            "dialect": site.get("dialect"),
            "call_kind": site.get("call_kind"),
            "domain": site.get("domain"),
            "context_snippet": site.get("context_snippet", ""),
            "extractor": site.get("extractor"),
            "review_status": "unreviewed",
            "contract_status": "none",
            "question_ids": [],
            "solver_outcome": None,
        }
        if isinstance(site.get("shell_flags"), dict):
            result["shell_flags"] = dict(site["shell_flags"])
        sites.append(result)
    sites.sort(key=lambda item: (item["source_file"], item["line"], item["column"], item.get("regex_id", "")))
    summary = {
        "path": gitlink_path,
        "repository_url": row["repository_url"],
        "commit": commit,
        "tree_oid": tree,
        "nested_gitlinks_excluded": nested,
        "scanned_files": scan.scanned_files,
        "oversized_files": scan.oversized_files,
        "site_count": len(sites),
        "status": "complete" if not nested and not scan.oversized_files else "incomplete",
    }
    return summary, sites


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent-inventory", type=Path, required=True)
    parser.add_argument("--gitlink-audit", type=Path, required=True)
    parser.add_argument("--checkout", action="append", default=[], metavar="GITLINK_PATH=CHECKOUT_PATH")
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        calibration_root = (ROOT / "properties" / "calibration").resolve()
        out_dir = args.out_dir.resolve()
        if not out_dir.is_relative_to(calibration_root) or out_dir == calibration_root:
            raise GitlinkInventoryError("--out-dir must be a child of properties/calibration")
        parent_inventory = _strict_json(args.parent_inventory)
        audit = _strict_json(args.gitlink_audit)
        parent_rows = [
            item for item in parent_inventory.get("repositories", [])
            if item.get("repo_id") == audit.get("repository")
        ]
        if len(parent_rows) != 1:
            raise GitlinkInventoryError("parent inventory does not have one matching root repository")
        parent = parent_rows[0]
        if parent.get("pin") != audit.get("root_commit"):
            raise GitlinkInventoryError("audit root commit differs from frozen parent inventory")
        if audit.get("root_tree_oid") and parent.get("commit_tree_oid") != audit["root_tree_oid"]:
            raise GitlinkInventoryError("audit root tree differs from frozen parent inventory")
        if audit.get("gitmodules", {}).get("present_in_tree") is not False:
            raise GitlinkInventoryError("expected an explicit no-.gitmodules audit")
        parent = {
            **parent,
            "cohort_id": parent_inventory["cohort_id"],
            "manifest_digest": parent_inventory["manifest_digest"],
        }
        expected = {
            row["path"]: row["commit"] for row in audit.get("gitlinks", [])
        }
        frozen = {
            item["path"]: item["commit_oid"]
            for item in parent.get("submodules_excluded", [])
        }
        if expected != frozen:
            raise GitlinkInventoryError("audit gitlink paths and commits differ from parent inventory")
        checkouts = _checkout_map(args.checkout)
        verified = {
            row["path"]: row for row in audit["gitlinks"]
            if row.get("mapping_status") == "exact_gitlink_commit_verified_via_github_api"
        }
        if set(checkouts) != set(verified):
            raise GitlinkInventoryError("checkouts must cover every verified source and no unresolved Gitlink")
        dogfood = _dogfood_module()
        summaries: list[dict[str, Any]] = []
        sites: list[dict[str, Any]] = []
        for path in sorted(verified):
            summary, rows = _extract_gitlink(verified[path], checkouts[path], parent, dogfood)
            summaries.append(summary)
            sites.extend(rows)
        ids = [row["source_site_id"] for row in sites]
        if len(ids) != len(set(ids)):
            raise GitlinkInventoryError("duplicate source site IDs")
        site_lines = [
            _site_line(row) for row in sorted(
                sites, key=lambda item: (item["source_file"], item["line"], item["column"])
            )
        ]
        sites_payload = "".join(line + "\n" for line in site_lines)
        artifact = {
            "schema_version": "1",
            "artifact_kind": "p2-gitlink-source-sites",
            "parent_inventory_sha256": hashlib.sha256(args.parent_inventory.read_bytes()).hexdigest(),
            "gitlink_audit_sha256": hashlib.sha256(args.gitlink_audit.read_bytes()).hexdigest(),
            "cohort_id": parent["cohort_id"],
            "manifest_digest": parent["manifest_digest"],
            "root_repository": parent["repo_id"],
            "root_url": parent["url"],
            "root_pin": parent["pin"],
            "root_tree_oid": parent["commit_tree_oid"],
            "dialect_family": parent["dialect_family"],
            "extractor": "scripts/dogfood-singleton-analysis.py:extract_repo(include_hidden=True)",
            "generator": "scripts/freeze-p2-gitlink-inventory.py",
            "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "extractor_sources": p2_inventory._extractor_fingerprint(),
            "interpretation": "Unreviewed raw source sites from exact verified Gitlink trees only; not boundaries, contracts, product questions, or proof outcomes.",
            "gitlinks": summaries,
            "unresolved_gitlinks": [row["path"] for row in audit["gitlinks"] if row["path"] not in verified],
            "summary": {
                "verified_gitlinks_scanned": len(summaries),
                "unresolved_gitlinks": len(audit["gitlinks"]) - len(summaries),
                "source_sites": len(sites),
                "reviewed_sites": 0,
                "contracts": 0,
                "questions": 0,
                "source_sites_ndjson_sha256": hashlib.sha256(sites_payload.encode("utf-8")).hexdigest(),
            },
        }
        out_dir.mkdir(parents=True, exist_ok=True)
        atomic_write_lines(out_dir / "sites.ndjson", site_lines)
        atomic_write_text(out_dir / "inventory.json", json.dumps(artifact, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    except (KeyError, OSError, TypeError, UnicodeError, ValueError) as exc:
        print(f"freeze-p2-gitlink-inventory: error: {exc}", file=sys.stderr)
        return 2

    for row in artifact["gitlinks"]:
        print(f"{row['path']}: {row['status']} sites={row['site_count']}")
    print(f"sites={artifact['summary']['source_sites']} unresolved_gitlinks={artifact['summary']['unresolved_gitlinks']}")
    return 0 if artifact["summary"]["unresolved_gitlinks"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
