"""Freeze source-bound regex-site identities for an autonomous P2 cohort.

This artifact is an extractor inventory only. It does not classify a regex as
a security boundary, adopt a property contract, or count proof questions.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import platform
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Mapping
from urllib.parse import urlparse

from .cohort_manifest import CohortManifestError, validate_manifest

SCHEMA_VERSION = "1"
_EXTRACTOR_FILES = (
    "scripts/dogfood-singleton-analysis.py",
    "scripts/freeze-p2-source-inventory.py",
    "regexproof/extractors/go_regexp.py",
    "regexproof/extractors/js_babel.py",
    "regexproof/extractors/python_ast.py",
    "regexproof/extractors/record.py",
    "regexproof/extractors/shell_posix.py",
    "regexproof/regex_id.py",
    "regexproof/mine/p2_source_inventory.py",
    "regexproof/schemas/__init__.py",
    "regexproof/batch/manifests.py",
)
_FAMILY_DIALECTS = {
    "py_re": frozenset({"py_re"}),
    "ecma": frozenset({"ecma"}),
    "go_re": frozenset({"re2"}),
    "posix-shell": frozenset({"posix-shell"}),
}
_FAMILY_EXTENSIONS = {
    "py_re": frozenset({".py"}),
    "ecma": frozenset({".js", ".mjs", ".ts", ".tsx"}),
    "go_re": frozenset({".go"}),
    # Shell uses the registered dir-mode discovery: shell suffixes, init.d,
    # and recognized shebangs, including extensionless scripts.
    "posix-shell": None,
}


class P2SourceInventoryError(ValueError):
    """Raised when a frozen source inventory cannot be trusted."""


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
        raise P2SourceInventoryError(f"git {' '.join(args)} failed: {exc}") from exc
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "command failed"
        raise P2SourceInventoryError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout.strip()


def _normalized_url(value: str) -> str:
    raw = value.strip()
    if raw.startswith("git@github.com:"):
        raw = "https://github.com/" + raw.split(":", 1)[1]
    parsed = urlparse(raw)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return raw.rstrip("/").removesuffix(".git").lower()
    path = parsed.path.rstrip("/").removesuffix(".git")
    return f"{parsed.netloc.lower()}{path}".lower()


def _dogfood_module() -> Any:
    source = Path(__file__).resolve().parents[2] / "scripts" / "dogfood-singleton-analysis.py"
    spec = importlib.util.spec_from_file_location("regexproof_p2_dogfood", source)
    if spec is None or spec.loader is None:
        raise P2SourceInventoryError(f"cannot load registered extractor {source}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _extractor_fingerprint() -> dict[str, str]:
    root = Path(__file__).resolve().parents[2]
    result: dict[str, str] = {}
    for relative in _EXTRACTOR_FILES:
        path = root / relative
        try:
            payload = path.read_bytes()
        except OSError as exc:
            raise P2SourceInventoryError(
                f"cannot hash extractor source {relative}: {exc}"
            ) from exc
        result[relative] = hashlib.sha256(payload).hexdigest()
    return result


def _check_symlink_reads(root: Path, dogfood: Any, *, include_hidden: bool) -> None:
    """Refuse source trees that could make the extractor read outside root."""
    root_resolved = root.resolve(strict=True)
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if dogfood._filtered(relative, include_hidden=include_hidden) or not path.is_symlink():
            continue
        try:
            resolved = path.resolve(strict=True)
        except OSError as exc:
            raise P2SourceInventoryError(
                f"dangling or unreadable source symlink {relative!r}: {exc}"
            ) from exc
        if not resolved.is_relative_to(root_resolved):
            raise P2SourceInventoryError(
                f"source symlink {relative!r} resolves outside the pinned checkout"
            )


def _tree_entry(path: Path, pin: str, relative_file: str) -> tuple[str, str]:
    """Return Git mode and blob ID for one exact pinned source path."""
    raw = subprocess.run(
        [
            "git", "--literal-pathspecs", "-C", str(path), "ls-tree", "-z",
            pin, "--", relative_file,
        ],
        check=False,
        capture_output=True,
        timeout=30,
    )
    if raw.returncode != 0:
        detail = raw.stderr.decode("utf-8", "replace").strip() or "ls-tree failed"
        raise P2SourceInventoryError(f"cannot bind {relative_file!r} to Git tree: {detail}")
    entries = [item for item in raw.stdout.split(b"\0") if item]
    matching: list[tuple[str, str]] = []
    for entry in entries:
        header, separator, tree_path = entry.partition(b"\t")
        if not separator or tree_path.decode("utf-8", "surrogateescape") != relative_file:
            continue
        fields = header.decode("ascii").split()
        if len(fields) != 3 or fields[1] != "blob":
            continue
        matching.append((fields[0], fields[2]))
    if len(matching) != 1:
        raise P2SourceInventoryError(
            f"pinned Git tree must contain exactly one blob for {relative_file!r}; "
            f"found {len(matching)}"
        )
    return matching[0]


def _gitlinks(path: Path, pin: str) -> list[dict[str, str]]:
    """List pinned submodule entries without trusting .gitmodules metadata."""
    raw = subprocess.run(
        ["git", "-C", str(path), "ls-tree", "-rz", pin],
        check=False,
        capture_output=True,
        timeout=30,
    )
    if raw.returncode != 0:
        detail = raw.stderr.decode("utf-8", "replace").strip() or "ls-tree failed"
        raise P2SourceInventoryError(f"cannot enumerate pinned gitlinks: {detail}")
    result: list[dict[str, str]] = []
    for entry in raw.stdout.split(b"\0"):
        if not entry:
            continue
        header, separator, tree_path = entry.partition(b"\t")
        if not separator:
            raise P2SourceInventoryError("Git emitted a malformed tree entry")
        fields = header.decode("ascii").split()
        if len(fields) != 3 or fields[0] != "160000" or fields[1] != "commit":
            continue
        try:
            decoded_path = tree_path.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise P2SourceInventoryError("Gitlink path is not valid UTF-8") from exc
        result.append({"path": decoded_path, "commit_oid": fields[2]})
    return result


def _source_path(root: Path, relative_file: Any) -> tuple[Path, str]:
    if not isinstance(relative_file, str) or not relative_file:
        raise P2SourceInventoryError("extractor emitted a missing source file")
    posix = PurePosixPath(relative_file)
    if posix.is_absolute() or ".." in posix.parts:
        raise P2SourceInventoryError(
            f"extractor emitted unsafe source path {relative_file!r}"
        )
    path = root.joinpath(*posix.parts)
    resolved_root = root.resolve(strict=True)
    resolved = path.resolve(strict=True)
    if not resolved.is_relative_to(resolved_root) or not resolved.is_file():
        raise P2SourceInventoryError(
            f"extractor source path {relative_file!r} escapes checkout or is not a file"
        )
    return path, posix.as_posix()


def _repo_record(
    repo: Mapping[str, Any],
    checkout: Path | None,
    dogfood: Any,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    base = {
        "repo_id": repo["repo_id"],
        "url": repo["url"],
        "pin": repo["pin"],
        "dialect_family": repo["dialect_family"],
    }
    if checkout is None:
        return ({**base, "status": "missing_checkout", "site_count": 0}, [])

    try:
        root = checkout.resolve(strict=True)
        if not root.is_dir():
            raise P2SourceInventoryError("checkout path is not a directory")
        head = _git(root, "rev-parse", "HEAD")
        if head != repo["pin"]:
            raise P2SourceInventoryError(
                f"checkout HEAD {head!r} does not match frozen pin {repo['pin']!r}"
            )
        origin = _git(root, "remote", "get-url", "origin")
        if _normalized_url(origin) != _normalized_url(repo["url"]):
            raise P2SourceInventoryError(
                f"origin {origin!r} does not match frozen URL {repo['url']!r}"
            )
        dirty = _git(root, "status", "--porcelain", "--untracked-files=all")
        if dirty:
            raise P2SourceInventoryError("pinned source checkout is dirty")
        tree_oid = _git(root, "rev-parse", f"{repo['pin']}^{{tree}}")
        submodules = _gitlinks(root, repo["pin"])
        include_hidden = True
        _check_symlink_reads(root, dogfood, include_hidden=include_hidden)

        extensions = _FAMILY_EXTENSIONS.get(repo["dialect_family"], "unsupported")
        dialects = _FAMILY_DIALECTS.get(repo["dialect_family"])
        if extensions == "unsupported" or dialects is None:
            raise P2SourceInventoryError(
                f"no registered source extractor for {repo['dialect_family']!r}"
            )
        kwargs: dict[str, Any] = {
            "dir_mode": True,
            "include_hidden": include_hidden,
        }
        if extensions is not None:
            kwargs["exts"] = set(extensions)
        scan = dogfood.extract_repo(repo["repo_id"], str(root), **kwargs)
        submodule_paths = tuple(item["path"].rstrip("/") for item in submodules)
        selected = [
            row
            for row in scan.records
            if row.get("dialect") in dialects
            and not any(
                row.get("file") == submodule
                or str(row.get("file") or "").startswith(submodule + "/")
                for submodule in submodule_paths
            )
        ]

        file_cache: dict[str, tuple[str, str, str]] = {}
        sites: list[dict[str, Any]] = []
        for record in selected:
            source_path, source_file = _source_path(root, record.get("file"))
            if source_file not in file_cache:
                mode, blob_oid = _tree_entry(root, repo["pin"], source_file)
                source_bytes = source_path.read_bytes()
                file_cache[source_file] = (
                    hashlib.sha256(source_bytes).hexdigest(), mode, blob_oid
                )
            source_sha256, git_mode, git_blob_oid = file_cache[source_file]
            file_sha = source_path.read_bytes()
            if hashlib.sha256(file_sha).hexdigest() != source_sha256:
                raise P2SourceInventoryError(
                    f"source file changed during scan: {source_file!r}"
                )
            try:
                line = int(record["line"])
                column = int(record["column"])
            except (KeyError, TypeError, ValueError) as exc:
                raise P2SourceInventoryError(
                    f"extractor emitted invalid line/column for {source_file!r}"
                ) from exc
            identity = [
                repo["repo_id"], repo["pin"], source_file, line, column,
                record.get("regex_id"), source_sha256,
            ]
            site_id = hashlib.sha256(
                json.dumps(identity, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
            ).hexdigest()
            site_row = {
                    "source_site_id": site_id,
                    "cohort_id": None,  # filled by the caller after manifest validation
                    "manifest_digest": None,
                    **base,
                    "commit_tree_oid": tree_oid,
                    "regex_id": record.get("regex_id"),
                    "site": record.get("site"),
                    "source_file": source_file,
                    "source_file_sha256": source_sha256,
                    "source_symlink_target": (
                        os.readlink(source_path) if source_path.is_symlink() else None
                    ),
                    "git_mode": git_mode,
                    "git_blob_oid": git_blob_oid,
                    "line": line,
                    "column": column,
                    "pattern": record.get("pattern", ""),
                    "flags": record.get("flags", ""),
                    "dialect": record.get("dialect"),
                    "call_kind": record.get("call_kind"),
                    "domain": record.get("domain"),
                    "context_snippet": record.get("context_snippet", ""),
                    "extractor": record.get("extractor"),
                    "review_status": "unreviewed",
                    "contract_status": "none",
                    "question_ids": [],
                    "solver_outcome": None,
                }
            # BRE and ERE are separate product languages. Preserve the
            # extractor's command mode so later compiler joins cannot silently
            # default an original `grep -E` site to BRE.
            if isinstance(record.get("shell_flags"), dict):
                site_row["shell_flags"] = dict(record["shell_flags"])
            sites.append(site_row)
        sites.sort(
            key=lambda row: (
                row["source_file"], row["line"], row["column"], row["regex_id"] or ""
            )
        )
        status = "complete"
        limitations: list[str] = []
        if scan.oversized_files:
            status = "incomplete_oversized_files"
            limitations.append("one or more files exceeded the extractor 2 MB cap")
        if submodules:
            status = "incomplete_submodules"
            limitations.append("submodule content is outside the frozen root inventory")
        if not selected:
            status = "empty_inventory"
            limitations.append("registered extractor found no sites in the frozen dialect family")
        repo_row = {
            **base,
            "status": status,
            "commit_tree_oid": tree_oid,
            "scanned_files": scan.scanned_files,
            "oversized_files": scan.oversized_files,
            "submodules_excluded": submodules,
            "limitations": limitations,
            "site_count": len(sites),
        }
        return repo_row, sites
    except Exception as exc:
        return (
            {
                **base,
                "status": "failed",
                "site_count": 0,
                "error": f"{type(exc).__name__}: {exc}",
            },
            [],
        )


def build_source_inventory(
    manifest_value: Any,
    repo_paths: Mapping[str, str | Path],
    *,
    cohort_manifest_sha256: str,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Extract every registered family site from all frozen cohort members."""
    try:
        manifest = validate_manifest(manifest_value)
    except CohortManifestError as exc:
        raise P2SourceInventoryError(str(exc)) from exc
    if len(cohort_manifest_sha256) != 64 or any(
        char not in "0123456789abcdef" for char in cohort_manifest_sha256
    ):
        raise P2SourceInventoryError("cohort_manifest_sha256 must be lowercase SHA-256")
    extra = sorted(set(repo_paths) - {row["repo_id"] for row in manifest["repos"]})
    if extra:
        raise P2SourceInventoryError(
            "checkout map contains repos outside the frozen cohort: " + ", ".join(extra)
        )

    dogfood = _dogfood_module()
    extractor_sources = _extractor_fingerprint()
    extractor_fingerprint = hashlib.sha256(
        json.dumps(extractor_sources, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    repo_rows: list[dict[str, Any]] = []
    all_sites: list[dict[str, Any]] = []
    for repo in manifest["repos"]:
        raw_path = repo_paths.get(repo["repo_id"])
        checkout = Path(raw_path) if raw_path is not None else None
        repo_row, sites = _repo_record(repo, checkout, dogfood)
        repo_rows.append(repo_row)
        all_sites.extend(sites)
    site_ids = [row["source_site_id"] for row in all_sites]
    if len(site_ids) != len(set(site_ids)):
        raise P2SourceInventoryError("extractor emitted duplicate source-site identities")
    for row in all_sites:
        row["cohort_id"] = manifest["cohort_id"]
        row["manifest_digest"] = manifest["manifest_digest"]

    lines = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
        for row in all_sites
    )
    artifact = {
        "schema_version": SCHEMA_VERSION,
        "artifact_kind": "p2-extracted-source-sites",
        "cohort_id": manifest["cohort_id"],
        "manifest_digest": manifest["manifest_digest"],
        "cohort_manifest_sha256": cohort_manifest_sha256,
        "extractor": (
            "scripts/dogfood-singleton-analysis.py:extract_repo(include_hidden=True)"
        ),
        "extractor_fingerprint_sha256": extractor_fingerprint,
        "extractor_sources": extractor_sources,
        "runtime": {
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
            "platform": sys.platform,
        },
        "extraction_scope": (
            "registered Python AST, Babel ECMA, Go regexp, and POSIX shell extractors; "
            "dir-mode file selection with hidden source paths included; fixed "
            "Git, generated, virtualenv, coverage, and cache directories excluded; files over 2 MB and "
            "submodule contents reported as incomplete"
        ),
        "interpretation": (
            "Raw extracted regex sites only. Every site is unreviewed, has no adopted "
            "contract, has no attempted question, and has no solver outcome. This is "
            "not a security-boundary candidate count or conversion yield."
        ),
        "repositories": repo_rows,
        "summary": {
            "cohort_repositories": len(manifest["repos"]),
            "complete_repositories": sum(row["status"] == "complete" for row in repo_rows),
            "incomplete_or_failed_repositories": sum(row["status"] != "complete" for row in repo_rows),
            "source_sites": len(all_sites),
            "reviewed_sites": 0,
            "contracted_sites": 0,
            "attempted_questions": 0,
            "solver_outcomes": 0,
            "source_sites_ndjson_sha256": hashlib.sha256(lines.encode("utf-8")).hexdigest(),
        },
    }
    return artifact, all_sites
