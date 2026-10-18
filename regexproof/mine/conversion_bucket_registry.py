"""Reviewed, source-pinned registrations for new conversion idiom buckets."""

from __future__ import annotations

import hashlib
import fcntl
import json
import pathlib
import re
import subprocess
from datetime import date
from typing import Any

from regexproof.contract_adoption import contract_digest
from regexproof.harness.contract import valid_product_contract
from regexproof.io_atomic import atomic_write_text

ROOT = pathlib.Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "properties" / "conversion_bucket_registry.json"
STOPPED_CLUSTERS = frozenset({"openwrt_packages", "openwrt_luci"})
PIN_RE = re.compile(r"^[0-9a-f]{40}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
TRUST_CLASSES = frozenset({"untrusted-input", "config", "internal"})
MAX_REGISTERED_SOURCE_SITES = 10_000
MAX_REVIEW_CANDIDATES = 15
ROOT_FIELDS = {"schema_version", "entries"}
ENTRY_FIELDS = {
    "cluster", "bucket", "repository_url", "source_pin", "product_engine",
    "trust_map", "source_sites", "question_family", "max_candidates",
    "registered_on", "rationale", "source_files", "contract_site",
    "contract_sha256", "review",
}
OPTIONAL_ENTRY_FIELDS = {"dialect_family"}


class BucketRegistryError(ValueError):
    """Invalid or unsafe idiom bucket registration."""


def _text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise BucketRegistryError(f"{field} must be a non-empty trimmed string")
    return value


def _relative_source_site_path(site: str, repository_url: str, pin: str) -> str:
    """Extract a checkout-relative path from a plain or repository-pinned site."""
    owner_repo = repository_url.removeprefix("https://github.com/")
    qualified_prefix = f"{owner_repo}@{pin}:"
    if site.startswith(qualified_prefix):
        site = site[len(qualified_prefix):]
    elif re.match(r"^[^/]+/[^/:]+@[0-9a-f]{40}:", site):
        raise BucketRegistryError(
            f"source site repository or pin does not match registration: {site!r}"
        )
    parts = site.rsplit(":", 2)
    if len(parts) != 3:
        raise BucketRegistryError(f"invalid source site {site!r}; expected path:line:token")
    rel = pathlib.PurePosixPath(parts[0])
    if rel.is_absolute() or ".." in rel.parts or not rel.parts:
        raise BucketRegistryError(f"source site path is unsafe: {site!r}")
    return rel.as_posix()


def _validate_entry(raw: Any, index: int) -> dict[str, Any]:
    ctx = f"entries[{index}]"
    if (
        not isinstance(raw, dict)
        or frozenset(raw) not in {
            frozenset(ENTRY_FIELDS),
            frozenset(ENTRY_FIELDS | OPTIONAL_ENTRY_FIELDS),
        }
    ):
        raise BucketRegistryError(f"{ctx} must have exactly the registered-entry fields")
    for field in ("cluster", "bucket", "question_family"):
        value = _text(raw[field], f"{ctx}.{field}")
        if not ID_RE.fullmatch(value):
            raise BucketRegistryError(f"{ctx}.{field} must be a plain identifier")
    if raw["cluster"] in STOPPED_CLUSTERS:
        raise BucketRegistryError(f"{ctx}.cluster is stopped and cannot be reopened here")
    url = _text(raw["repository_url"], f"{ctx}.repository_url")
    if not re.fullmatch(r"https://github\.com/[^/\s]+/[^/\s]+", url):
        raise BucketRegistryError(f"{ctx}.repository_url must be a GitHub repository URL")
    if not isinstance(raw["source_pin"], str) or not PIN_RE.fullmatch(raw["source_pin"]):
        raise BucketRegistryError(f"{ctx}.source_pin must be 40 lowercase hexadecimal characters")
    _text(raw["product_engine"], f"{ctx}.product_engine")
    if "dialect_family" in raw:
        family = _text(raw["dialect_family"], f"{ctx}.dialect_family")
        if not ID_RE.fullmatch(family):
            raise BucketRegistryError(f"{ctx}.dialect_family must be a plain identifier")
    trust = raw["trust_map"]
    if not isinstance(trust, dict) or not trust or set(trust) - TRUST_CLASSES:
        raise BucketRegistryError(f"{ctx}.trust_map must map known trust classes to notes")
    for key, value in trust.items():
        _text(value, f"{ctx}.trust_map.{key}")
    sites = raw["source_sites"]
    if (
        not isinstance(sites, list)
        or not sites
        or len(sites) > MAX_REGISTERED_SOURCE_SITES
    ):
        raise BucketRegistryError(
            f"{ctx}.source_sites must contain 1..{MAX_REGISTERED_SOURCE_SITES} sites"
        )
    if any(not isinstance(site, str) or not site.strip() for site in sites):
        raise BucketRegistryError(f"{ctx}.source_sites must contain non-empty strings")
    if len(set(sites)) != len(sites):
        raise BucketRegistryError(f"{ctx}.source_sites contains duplicates")
    if (
        type(raw["max_candidates"]) is not int
        or not 1 <= raw["max_candidates"] <= MAX_REVIEW_CANDIDATES
    ):
        raise BucketRegistryError(
            f"{ctx}.max_candidates must be in 1..{MAX_REVIEW_CANDIDATES}"
        )
    try:
        if date.fromisoformat(_text(raw["registered_on"], f"{ctx}.registered_on")).isoformat() != raw["registered_on"]:
            raise ValueError
    except ValueError as exc:
        raise BucketRegistryError(f"{ctx}.registered_on must be an ISO date") from exc
    _text(raw["rationale"], f"{ctx}.rationale")
    _text(raw["contract_site"], f"{ctx}.contract_site")
    if not isinstance(raw["contract_sha256"], str) or not SHA_RE.fullmatch(raw["contract_sha256"]):
        raise BucketRegistryError(f"{ctx}.contract_sha256 must be a SHA-256 digest")
    files = raw["source_files"]
    if not isinstance(files, list) or not files:
        raise BucketRegistryError(f"{ctx}.source_files must be non-empty")
    seen_paths = set()
    for item in files:
        if not isinstance(item, dict) or set(item) != {"path", "sha256", "evidence_ref"}:
            raise BucketRegistryError(f"{ctx}.source_files entries have invalid fields")
        path = _text(item["path"], f"{ctx}.source_files.path")
        if path.startswith("/") or ".." in pathlib.PurePosixPath(path).parts:
            raise BucketRegistryError(f"{ctx}.source_files.path must be checkout-relative")
        if path in seen_paths:
            raise BucketRegistryError(f"{ctx}.source_files has duplicate paths")
        seen_paths.add(path)
        if not isinstance(item["sha256"], str) or not SHA_RE.fullmatch(item["sha256"]):
            raise BucketRegistryError(f"{ctx}.source_files.sha256 must be a SHA-256 digest")
        ref = f"{url}/blob/{raw['source_pin']}/{path}"
        if item["evidence_ref"] != ref:
            raise BucketRegistryError(f"{ctx}.source_files.evidence_ref is not pin-bound")
    review = raw["review"]
    if not isinstance(review, dict) or set(review) != {"author", "reviewer", "same_model"}:
        raise BucketRegistryError(f"{ctx}.review has invalid fields")
    _text(review["author"], f"{ctx}.review.author")
    _text(review["reviewer"], f"{ctx}.review.reviewer")
    if not isinstance(review["same_model"], bool):
        raise BucketRegistryError(f"{ctx}.review.same_model must be boolean")
    return dict(raw)


def validate_registry(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != ROOT_FIELDS:
        raise BucketRegistryError("registry must have exactly schema_version and entries")
    if value["schema_version"] != "1" or not isinstance(value["entries"], list):
        raise BucketRegistryError("registry schema_version must be '1' and entries a list")
    entries = [_validate_entry(item, index) for index, item in enumerate(value["entries"])]
    seen_buckets: set[tuple[str, str]] = set()
    seen_families: set[tuple[str, str]] = set()
    for entry in entries:
        key = (entry["cluster"], entry["bucket"])
        family = (entry["cluster"], entry["question_family"])
        if key in seen_buckets:
            raise BucketRegistryError(f"duplicate registered bucket {key!r}")
        if family in seen_families:
            raise BucketRegistryError(f"duplicate question family {family!r}")
        seen_buckets.add(key)
        seen_families.add(family)
    return {"schema_version": "1", "entries": entries}


def load_registry(path: pathlib.Path | None = None) -> dict[str, Any]:
    source = pathlib.Path(path) if path else REGISTRY_PATH
    if not source.exists():
        return {"schema_version": "1", "entries": []}
    try:
        value = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BucketRegistryError(f"cannot read registry {source}: {exc}") from exc
    return validate_registry(value)


def build_registration(
    *,
    cluster: str,
    bucket: str,
    repository_url: str,
    pin: str,
    checkout: pathlib.Path,
    product_engine: str,
    trust_map: dict[str, str],
    source_sites: list[str],
    question_family: str,
    max_candidates: int,
    registered_on: str,
    rationale: str,
    contract: dict[str, Any],
    author: str,
    reviewer: str,
    same_model: bool,
    dialect_family: str | None = None,
) -> dict[str, Any]:
    root = checkout.resolve()
    try:
        actual_pin = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True, timeout=10,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError) as exc:
        raise BucketRegistryError(f"cannot verify source checkout: {exc}") from exc
    if actual_pin != pin:
        raise BucketRegistryError(f"checkout pin {actual_pin!r} does not match requested {pin!r}")
    if not valid_product_contract(contract):
        raise BucketRegistryError("representative contract must be fully adopted")
    if not source_sites:
        raise BucketRegistryError("source_sites must contain at least one site")
    if contract.get("site") != source_sites[0]:
        raise BucketRegistryError("representative contract.site must match the first source site")
    adoption = contract.get("adoption", {})
    if (
        adoption.get("source_url", "").rstrip("/") != repository_url.rstrip("/")
        or adoption.get("source_pin") != pin
    ):
        raise BucketRegistryError("representative contract adoption must match this source pin")
    source_paths = []
    for site in source_sites:
        source_paths.append(_relative_source_site_path(site, repository_url, pin))
    source_paths.append(adoption["source_file"])
    sources = []
    for path in sorted(set(source_paths)):
        candidate = root.joinpath(*pathlib.PurePosixPath(path).parts)
        cursor = root
        for part in pathlib.PurePosixPath(path).parts:
            cursor = cursor / part
            if cursor.is_symlink():
                raise BucketRegistryError(f"source path traverses symlink: {path}")
        try:
            resolved = candidate.resolve()
            resolved.relative_to(root)
        except ValueError as exc:
            raise BucketRegistryError(f"source path escapes checkout: {path}") from exc
        if not resolved.is_file():
            raise BucketRegistryError(f"source file is missing: {path}")
        try:
            committed = subprocess.run(
                ["git", "-C", str(root), "show", f"{pin}:{path}"],
                check=True, capture_output=True, timeout=10,
            ).stdout
        except (OSError, subprocess.SubprocessError) as exc:
            raise BucketRegistryError(f"cannot read pinned source {path}: {exc}") from exc
        if resolved.read_bytes() != committed:
            raise BucketRegistryError(f"working source differs from pinned commit: {path}")
        digest = hashlib.sha256(committed).hexdigest()
        if path == adoption["source_file"] and digest != adoption.get("source_sha256"):
            raise BucketRegistryError("representative contract source digest is stale")
        sources.append({
            "path": path,
            "sha256": digest,
            "evidence_ref": f"{repository_url.rstrip('/')}/blob/{pin}/{path}",
        })
    record = {
        "cluster": cluster,
        "bucket": bucket,
        "repository_url": repository_url.rstrip("/"),
        "source_pin": pin,
        "product_engine": product_engine,
        "trust_map": trust_map,
        "source_sites": source_sites,
        "question_family": question_family,
        "max_candidates": max_candidates,
        "registered_on": registered_on,
        "rationale": rationale,
        "source_files": sources,
        "contract_site": contract["site"],
        "contract_sha256": contract_digest(contract),
        "review": {"author": author, "reviewer": reviewer, "same_model": same_model},
    }
    if dialect_family is not None:
        record["dialect_family"] = dialect_family
    _validate_entry(record, 0)
    return record


def append_registration(entry: dict[str, Any], path: pathlib.Path | None = None) -> dict[str, Any]:
    destination = pathlib.Path(path) if path else REGISTRY_PATH
    destination.parent.mkdir(parents=True, exist_ok=True)
    lock_path = destination.with_suffix(destination.suffix + ".lock")
    with lock_path.open("a+") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        registry = load_registry(destination)
        candidate = validate_registry(
            {"schema_version": "1", "entries": [*registry["entries"], entry]}
        )
        payload = json.dumps(candidate, indent=2, sort_keys=True) + "\n"
        atomic_write_text(destination, payload)
    return entry
