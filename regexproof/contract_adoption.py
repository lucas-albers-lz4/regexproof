"""Shared validation for source-bound autonomous contract adoption."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import date
from pathlib import Path
from typing import Any

POLICY_VERSION = "autonomous-contracts-v1"
_PIN = re.compile(r"^[0-9a-f]{40}$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_ADOPTION_FIELDS = {
    "policy_version",
    "status",
    "authority",
    "approved_on",
    "rationale",
    "evidence",
    "source_url",
    "source_pin",
    "source_file",
    "source_sha256",
    "contract_sha256",
    "review",
}
_REVIEW_FIELDS = {"author", "reviewer", "same_model"}


def contract_digest(contract: Any) -> str | None:
    """Hash every contract field except adoption, which stores this digest."""
    if not isinstance(contract, dict):
        return None
    subject = {key: value for key, value in contract.items() if key != "adoption"}
    try:
        payload = json.dumps(
            subject,
            ensure_ascii=True,
            allow_nan=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    except (TypeError, ValueError):
        return None
    return hashlib.sha256(payload).hexdigest()


def valid_adoption_record(adoption: Any, contract: Any = None) -> bool:
    """Validate adoption evidence, pinned source identity, and contract binding."""
    if not isinstance(adoption, dict) or set(adoption) != _ADOPTION_FIELDS:
        return False
    if adoption.get("policy_version") != POLICY_VERSION:
        return False
    if adoption.get("status") != "approved":
        return False
    if adoption.get("authority") not in {
        "direct_user_approval",
        "standing_user_delegation",
    }:
        return False
    approved_on = adoption.get("approved_on")
    if not isinstance(approved_on, str):
        return False
    try:
        if date.fromisoformat(approved_on).isoformat() != approved_on:
            return False
    except ValueError:
        return False
    rationale = adoption.get("rationale")
    evidence = adoption.get("evidence")
    if not isinstance(rationale, str) or not rationale.strip():
        return False
    if not isinstance(evidence, list) or not evidence or any(
        not isinstance(item, str) or not item.strip() for item in evidence
    ):
        return False
    url = adoption.get("source_url")
    path = adoption.get("source_file")
    if not isinstance(url, str) or not re.fullmatch(
        r"https://github\.com/[^/\s]+/[^/\s]+", url
    ):
        return False
    if not isinstance(path, str) or not path or path.startswith("/") or ".." in path.split("/"):
        return False
    if not _PIN.fullmatch(str(adoption.get("source_pin") or "")):
        return False
    if not _SHA256.fullmatch(str(adoption.get("source_sha256") or "")):
        return False
    if not _SHA256.fullmatch(str(adoption.get("contract_sha256") or "")):
        return False
    pinned_source_ref = f"{url}/blob/{adoption['source_pin']}/{path}"
    if pinned_source_ref not in evidence:
        return False
    review = adoption.get("review")
    if not isinstance(review, dict) or set(review) != _REVIEW_FIELDS:
        return False
    for field in ("author", "reviewer"):
        if not isinstance(review.get(field), str) or not review[field].strip():
            return False
    if not isinstance(review.get("same_model"), bool):
        return False
    if contract is not None:
        if not isinstance(contract, dict) or contract.get("provenance") != "agent_derived":
            return False
        if contract_digest(contract) != adoption.get("contract_sha256"):
            return False
    return True


def build_adoption_record(
    contract: dict[str, Any],
    *,
    repository_url: str,
    pin: str,
    checkout: str | Path,
    source_file: str,
    evidence: list[str],
    rationale: str,
    author: str,
    reviewer: str,
    same_model: bool,
    approved_on: str,
    authority: str = "standing_user_delegation",
) -> dict[str, Any]:
    """Build an adoption only from a checkout at the named pin and its source bytes."""
    root = Path(checkout).expanduser().resolve()
    if not _PIN.fullmatch(str(pin)):
        raise ValueError("pin must be exactly 40 lowercase hexadecimal characters")
    if not isinstance(repository_url, str) or not re.fullmatch(
        r"https://github\.com/[^/\s]+/[^/\s]+", repository_url.rstrip("/")
    ):
        raise ValueError("repository_url must be a canonical GitHub repository URL")
    try:
        actual_pin = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError) as exc:
        raise ValueError(f"cannot verify source checkout: {exc}") from exc
    if actual_pin != pin:
        raise ValueError(f"checkout pin {actual_pin!r} does not match requested {pin!r}")
    if not source_file or Path(source_file).is_absolute() or ".." in Path(source_file).parts:
        raise ValueError("source_file must be a safe checkout-relative path")
    candidate = root / source_file
    if candidate.is_symlink():
        raise ValueError("source_file must not be a symlink")
    source = candidate.resolve()
    try:
        source.relative_to(root)
    except ValueError as exc:
        raise ValueError("source_file resolves outside the checkout") from exc
    if not source.is_file():
        raise ValueError(f"source file not found: {source_file}")
    try:
        committed = subprocess.run(
            ["git", "-C", str(root), "show", f"{pin}:{source_file}"],
            check=True,
            capture_output=True,
            timeout=10,
        ).stdout
    except (OSError, subprocess.SubprocessError) as exc:
        raise ValueError(f"cannot read source file at pinned commit: {exc}") from exc
    source_bytes = source.read_bytes()
    if source_bytes != committed:
        raise ValueError("source_file working-tree bytes differ from the pinned commit")
    contract = {**contract, "provenance": "agent_derived"}
    contract.pop("adoption", None)
    record = {
        "policy_version": POLICY_VERSION,
        "status": "approved",
        "authority": authority,
        "approved_on": approved_on,
        "rationale": rationale,
        "evidence": evidence,
        "source_url": repository_url.rstrip("/"),
        "source_pin": pin,
        "source_file": source_file,
        "source_sha256": hashlib.sha256(committed).hexdigest(),
        "contract_sha256": contract_digest(contract),
        "review": {"author": author, "reviewer": reviewer, "same_model": same_model},
    }
    if not valid_adoption_record(record, contract):
        raise ValueError("adoption inputs failed the autonomous-contracts-v1 policy")
    return record


def contract_is_adopted(contract: Any) -> bool:
    """Human/machine-paired contracts keep existing authority; agents need a record."""
    if not isinstance(contract, dict):
        return False
    provenance = contract.get("provenance")
    if provenance in {"human", "version_diff", "cross_engine"}:
        return True
    return provenance == "agent_derived" and valid_adoption_record(
        contract.get("adoption"), contract
    )


def verify_adoption_source(contract: Any, checkout: str | Path) -> bool:
    """Recheck an adopted contract's source bytes against its pinned checkout."""
    if not isinstance(contract, dict) or not contract_is_adopted(contract):
        raise ValueError("contract has no valid source-bound autonomous adoption")
    adoption = contract["adoption"]
    root = Path(checkout).expanduser().resolve()
    pin = adoption["source_pin"]
    source_file = adoption["source_file"]
    try:
        actual_pin = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError) as exc:
        raise ValueError(f"cannot verify source checkout: {exc}") from exc
    if actual_pin != pin:
        raise ValueError(f"checkout pin {actual_pin!r} does not match contract pin {pin!r}")
    rel = Path(source_file)
    if rel.is_absolute() or ".." in rel.parts or not rel.parts:
        raise ValueError("adoption source_file is not a safe checkout-relative path")
    candidate = root / rel
    cursor = root
    for part in rel.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError(f"adoption source path traverses symlink: {source_file}")
    try:
        source = candidate.resolve()
        source.relative_to(root)
    except ValueError as exc:
        raise ValueError("adoption source path resolves outside the checkout") from exc
    if not source.is_file():
        raise ValueError(f"adoption source file is missing: {source_file}")
    try:
        committed = subprocess.run(
            ["git", "-C", str(root), "show", f"{pin}:{source_file}"],
            check=True,
            capture_output=True,
            timeout=10,
        ).stdout
    except (OSError, subprocess.SubprocessError) as exc:
        raise ValueError(f"cannot read pinned source {source_file}: {exc}") from exc
    if source.read_bytes() != committed:
        raise ValueError("adoption source working-tree bytes differ from the pinned commit")
    if hashlib.sha256(committed).hexdigest() != adoption["source_sha256"]:
        raise ValueError("adoption source digest does not match the pinned file")
    return True
