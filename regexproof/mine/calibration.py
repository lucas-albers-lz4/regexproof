"""Run a pinned, fail-closed calibration over a frozen cohort.

PR5 is intentionally an operator artifact, not a second selector.  The PR2
manifest owns membership and order; this module verifies each local checkout
at the manifest pin, invokes the registered dogfood extractor, and records
the exact canonical identities used for site-instance novelty.  A skipped or
partial repository is never converted into a saturation observation.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Any, Mapping

from .cohort_manifest import CohortManifestError, validate_manifest
from .saturation import CANONICALIZATION_VERSION, build_report

SCHEMA_VERSION = "1"
FAILURE_FIELDS = ("repo_id", "url", "pin", "status", "reason")
ARTIFACT_FIELDS = {
    "schema_version",
    "canonicalization_version",
    "cohort_id",
    "manifest_digest",
    "cohort",
    "observations",
    "failures",
}


class CalibrationError(ValueError):
    """Raised when calibration input or an execution artifact is unsafe."""


class UnsupportedDialectError(CalibrationError):
    """Raised when the registered extractor cannot support a manifest family."""


_EXTRACTOR_DIALECTS_BY_FAMILY = {
    "py_re": frozenset({"py_re"}),
    "ecma": frozenset({"ecma"}),
    "posix-shell": frozenset({"posix-shell"}),
    # The calibration dogfood extractor does not currently emit re2 records.
    # Keep this family explicit so a shell/Python record cannot be mislabeled
    # as Go evidence while Go extraction is being brought into this runner.
    "go_re": frozenset({"re2"}),
}
_EXTRACTOR_EXTS_BY_FAMILY = {
    "py_re": frozenset({".py"}),
    "ecma": frozenset({".js", ".mjs", ".ts", ".tsx"}),
    "go_re": frozenset({".go"}),
    # Shell shebangs and init.d paths are part of the registered dir-mode
    # surface, so this family deliberately uses the walker's default filter.
    "posix-shell": None,
}


def _error(message: str) -> CalibrationError:
    return CalibrationError(f"invalid calibration artifact: {message}")


def _strict_load(path: str | Path) -> Any:
    source = Path(path)

    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise _error(f"duplicate JSON key {key!r} in {source}")
            result[key] = value
        return result

    try:
        return json.loads(
            source.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicates,
            parse_constant=lambda value: (_ for _ in ()).throw(
                _error(f"non-finite JSON constant {value!r} in {source}")
            ),
        )
    except CalibrationError:
        raise
    except OSError as exc:
        raise CalibrationError(f"cannot read {source}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise CalibrationError(f"invalid JSON in {source}: {exc.msg}") from exc


def load_manifest(path: str | Path) -> dict[str, Any]:
    """Load and validate a PR2 frozen manifest without changing it."""
    try:
        return validate_manifest(_strict_load(path))
    except CohortManifestError as exc:
        raise CalibrationError(str(exc)) from exc


def _dogfood_module() -> Any:
    """Load the canonical extractor and identity implementation by path."""
    source = Path(__file__).resolve().parents[2] / "scripts" / "dogfood-singleton-analysis.py"
    spec = importlib.util.spec_from_file_location("regexproof_dogfood_singleton", source)
    if spec is None or spec.loader is None:
        raise CalibrationError(f"cannot load canonical extractor {source}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _git_head(path: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "HEAD"],
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise CalibrationError(f"cannot resolve git pin for {path}: {exc}") from exc
    if result.returncode != 0:
        detail = result.stderr.strip() or "git rev-parse failed"
        raise CalibrationError(f"cannot resolve git pin for {path}: {detail}")
    return result.stdout.strip()


def _identity_json(identity: tuple[Any, ...]) -> list[Any]:
    return list(identity)


def _reject_buckets(value: Any, repo_id: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item.strip() for item in value
    ):
        raise CalibrationError(
            f"reject buckets for {repo_id!r} must be a list of non-empty strings"
        )
    return sorted(set(value))


def _failure(repo: Mapping[str, Any], status: str, reason: str) -> dict[str, str]:
    return {
        "repo_id": repo["repo_id"],
        "url": repo["url"],
        "pin": repo["pin"],
        "status": status,
        "reason": reason,
    }


def _empty_product_properties() -> list[dict[str, Any]]:
    # Conversion evidence belongs to PR4.  An empty list is explicit so the
    # saturation report cannot mistake missing conversion data for zero rows.
    return []


def _observation(
    repo: Mapping[str, Any],
    records: list[Mapping[str, Any]],
    prior_ids: set[tuple[Any, ...]],
    reject_buckets: Any,
    dogfood: Any,
) -> tuple[dict[str, Any], set[tuple[Any, ...]]]:
    identities = [dogfood._ident_of(record, canon_pat=True) for record in records]
    canonical_ids = [_identity_json(identity) for identity in identities]
    novel_sites = sum(identity not in prior_ids for identity in identities)
    current_ids = set(identities)
    row = {
        "repo_id": repo["repo_id"],
        "url": repo["url"],
        "pin": repo["pin"],
        "dialect_family": repo["dialect_family"],
        "sites": len(records),
        "novel_sites": novel_sites,
        "canonical_ids": canonical_ids,
        "new_reject_buckets": _reject_buckets(reject_buckets, repo["repo_id"]),
        "product_properties": _empty_product_properties(),
    }
    return row, prior_ids | current_ids


def _records_for_family(
    repo: Mapping[str, Any], records: list[Mapping[str, Any]]
) -> list[Mapping[str, Any]]:
    family = repo["dialect_family"]
    expected = _EXTRACTOR_DIALECTS_BY_FAMILY.get(family)
    if expected is None:
        raise UnsupportedDialectError(
            f"no calibration extractor registered for dialect family {family!r}"
        )
    selected = [record for record in records if record.get("dialect") in expected]
    if not selected:
        observed = sorted(
            {record.get("dialect") for record in records},
            key=lambda value: str(value),
        )
        raise UnsupportedDialectError(
            f"dialect family {family!r} requires extractor dialect(s) "
            f"{sorted(expected)!r}, but inventory returned {observed!r}"
        )
    return selected


def _extractor_exts_for_family(family: str) -> frozenset[str] | None:
    try:
        return _EXTRACTOR_EXTS_BY_FAMILY[family]
    except KeyError as exc:
        raise UnsupportedDialectError(
            f"no calibration file surface registered for dialect family {family!r}"
        ) from exc


def build_observation_artifact(
    manifest: Mapping[str, Any],
    repo_paths: Mapping[str, str | Path],
    *,
    reject_buckets: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Extract a complete or explicitly incomplete canonical-ID artifact.

    ``repo_paths`` is deliberately explicit.  The function never clones,
    fetches, or follows a mutable branch.  Missing paths, pin mismatches,
    extractor failures, empty inventories, and oversized-file skips become
    failure-log rows; they do not advance the preceding-family prefix.
    """
    try:
        frozen = validate_manifest(manifest)
    except CohortManifestError as exc:
        raise CalibrationError(str(exc)) from exc
    if not isinstance(repo_paths, Mapping):
        raise CalibrationError("repo_paths must be an object keyed by repo_id")
    reject_buckets = reject_buckets or {}
    if not isinstance(reject_buckets, Mapping):
        raise CalibrationError("reject_buckets must be an object keyed by repo_id")

    dogfood = _dogfood_module()
    observations: list[dict[str, Any]] = []
    failures: list[dict[str, str]] = []
    family_seen: dict[str, set[tuple[Any, ...]]] = defaultdict(set)
    for repo in frozen["repos"]:
        repo_id = repo["repo_id"]
        raw_path = repo_paths.get(repo_id)
        if raw_path is None:
            failures.append(_failure(repo, "missing_checkout", "no local checkout supplied"))
            continue
        path = Path(raw_path)
        try:
            if not path.is_dir():
                raise CalibrationError(f"checkout path is not a directory: {path}")
            actual_pin = _git_head(path)
            if actual_pin != repo["pin"]:
                raise CalibrationError(
                    f"HEAD {actual_pin!r} does not match manifest pin {repo['pin']!r}"
                )
            extractor_exts = _extractor_exts_for_family(repo["dialect_family"])
            extractor_kwargs: dict[str, Any] = {"dir_mode": True}
            if extractor_exts is not None:
                extractor_kwargs["exts"] = extractor_exts
            scan = dogfood.extract_repo(repo_id, str(path), **extractor_kwargs)
            if scan.oversized_files:
                raise CalibrationError(
                    f"inventory skipped {scan.oversized_files} oversized file(s)"
                )
            if not scan.records:
                raise CalibrationError("pinned inventory contains zero regex sites")
            records = _records_for_family(repo, scan.records)
            row, family_seen[repo["dialect_family"]] = _observation(
                repo,
                records,
                family_seen[repo["dialect_family"]],
                reject_buckets.get(repo_id),
                dogfood,
            )
            observations.append(row)
        # A pinned repository may contain syntax from an older language
        # version or a malformed source file.  Calibration must keep the
        # failure visible and continue collecting independent repositories;
        # it must never abort the whole cohort or turn the site count into 0.
        except UnsupportedDialectError as exc:
            failures.append(_failure(repo, "unsupported_dialect", str(exc)))
        except Exception as exc:
            failures.append(_failure(repo, "failed", str(exc)))

    return {
        "schema_version": SCHEMA_VERSION,
        "canonicalization_version": CANONICALIZATION_VERSION,
        "cohort_id": frozen["cohort_id"],
        "manifest_digest": frozen["manifest_digest"],
        "cohort": frozen,
        "observations": observations,
        "failures": failures,
    }


def validate_artifact(artifact: Any) -> dict[str, Any]:
    """Validate artifact shape and bind every observation to manifest order."""
    if not isinstance(artifact, Mapping):
        raise _error("root must be an object")
    if set(artifact) != ARTIFACT_FIELDS:
        missing = sorted(ARTIFACT_FIELDS - set(artifact))
        extra = sorted(set(artifact) - ARTIFACT_FIELDS)
        if missing:
            raise _error(f"missing field(s): {', '.join(missing)}")
        raise _error(f"unknown field(s): {', '.join(extra)}")
    if artifact["schema_version"] != SCHEMA_VERSION:
        raise _error(f"schema_version must be {SCHEMA_VERSION!r}")
    if artifact["canonicalization_version"] != CANONICALIZATION_VERSION:
        raise _error(f"canonicalization_version must be {CANONICALIZATION_VERSION!r}")
    try:
        cohort = validate_manifest(artifact["cohort"])
    except CohortManifestError as exc:
        raise _error(str(exc)) from exc
    if artifact["cohort_id"] != cohort["cohort_id"]:
        raise _error("cohort_id does not match cohort")
    if artifact["manifest_digest"] != cohort["manifest_digest"]:
        raise _error("manifest_digest does not match cohort")
    observations = artifact["observations"]
    failures = artifact["failures"]
    if not isinstance(observations, list) or not isinstance(failures, list):
        raise _error("observations and failures must be lists")
    expected = {repo["repo_id"]: repo for repo in cohort["repos"]}
    seen: set[str] = set()
    observed_order: list[str] = []
    for index, row in enumerate(observations):
        if not isinstance(row, Mapping):
            raise _error(f"observations[{index}] must be an object")
        for field in (
            "repo_id",
            "url",
            "pin",
            "dialect_family",
            "sites",
            "novel_sites",
            "canonical_ids",
            "new_reject_buckets",
            "product_properties",
        ):
            if field not in row:
                raise _error(f"observations[{index}] is missing {field!r}")
        repo_id = row["repo_id"]
        if repo_id in seen or repo_id not in expected:
            raise _error(f"observation repo_id {repo_id!r} is duplicate or not in cohort")
        expected_repo = expected[repo_id]
        for field in ("url", "pin", "dialect_family"):
            if row[field] != expected_repo[field]:
                raise _error(f"observations[{index}].{field} does not match cohort")
        if not isinstance(row["sites"], int) or isinstance(row["sites"], bool) or row["sites"] <= 0:
            raise _error(f"observations[{index}].sites must be a positive integer")
        if not isinstance(row["novel_sites"], int) or isinstance(row["novel_sites"], bool):
            raise _error(f"observations[{index}].novel_sites must be an integer")
        if not 0 <= row["novel_sites"] <= row["sites"]:
            raise _error(f"observations[{index}].novel_sites is outside its site bounds")
        if not isinstance(row["canonical_ids"], list) or len(row["canonical_ids"]) != row["sites"]:
            raise _error(f"observations[{index}].canonical_ids must cover every site")
        seen.add(repo_id)
        observed_order.append(repo_id)
    for index, failure in enumerate(failures):
        if not isinstance(failure, Mapping) or set(failure) != set(FAILURE_FIELDS):
            raise _error(f"failures[{index}] must contain exactly {FAILURE_FIELDS}")
        if failure["repo_id"] not in expected:
            raise _error(f"failures[{index}] references a repository outside the cohort")
    if seen & {failure["repo_id"] for failure in failures}:
        raise _error("a repository cannot appear in both observations and failures")
    expected_observed_order = [repo["repo_id"] for repo in cohort["repos"] if repo["repo_id"] in seen]
    if observed_order != expected_observed_order:
        raise _error("observations must preserve frozen cohort order")
    return dict(artifact)


def saturation_envelope(artifact: Mapping[str, Any]) -> dict[str, Any]:
    """Project a complete raw artifact into PR1's strict report input."""
    checked = validate_artifact(artifact)
    if checked["failures"] or len(checked["observations"]) != len(checked["cohort"]["repos"]):
        raise CalibrationError("cannot build saturation envelope from incomplete calibration")
    observations = []
    for row in checked["observations"]:
        observations.append(
            {
                key: row[key]
                for key in (
                    "repo_id",
                    "url",
                    "pin",
                    "dialect_family",
                    "sites",
                    "novel_sites",
                    "new_reject_buckets",
                    "product_properties",
                )
            }
        )
    return {
        "schema_version": SCHEMA_VERSION,
        "canonicalization_version": CANONICALIZATION_VERSION,
        "cohort_id": checked["cohort_id"],
        "manifest_digest": checked["manifest_digest"],
        "cohort": checked["cohort"],
        "observations": observations,
    }


def build_closeout(artifact: Mapping[str, Any], *, conversion_report: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Build the 10-repository decision without treating missing data as saturation."""
    checked = validate_artifact(artifact)
    expected_count = len(checked["cohort"]["repos"])
    if checked["failures"] or len(checked["observations"]) != expected_count:
        observed_by_family: dict[str, int] = defaultdict(int)
        expected_by_family: dict[str, list[str]] = defaultdict(list)
        observed_ids = {row["repo_id"] for row in checked["observations"]}
        for repo in checked["cohort"]["repos"]:
            expected_by_family[repo["dialect_family"]].append(repo["repo_id"])
            if repo["repo_id"] in observed_ids:
                observed_by_family[repo["dialect_family"]] += 1
        incomplete_families = {
            family: {
                "status": (
                    "insufficient_data"
                    if observed_by_family[family] < 2
                    else (
                        "incomplete"
                        if set(repo_ids) - observed_ids
                        else "observed_but_closeout_blocked"
                    )
                ),
                "repo_count": observed_by_family[family],
                "expected_repo_count": len(repo_ids),
                "missing_repo_ids": sorted(
                    set(repo_ids) - observed_ids
                ),
            }
            for family, repo_ids in sorted(expected_by_family.items())
        }
        return {
            "schema_version": SCHEMA_VERSION,
            "cohort_id": checked["cohort_id"],
            "manifest_digest": checked["manifest_digest"],
            "decision": "inconclusive",
            "reason": "incomplete calibration; rerun skipped repositories at their pins",
            "continue_to_20": True,
            "continue_to_30": "pending_20_repo_run",
            "failures": checked["failures"],
            "families": incomplete_families,
        }
    report = build_report(saturation_envelope(checked))
    families: dict[str, Any] = {}
    reasons: list[str] = []
    for family, data in report["families"].items():
        if data["repo_count"] < 2:
            status = "insufficient_data"
            reasons.append(f"{family} has fewer than two eligible repositories")
        elif data["compiler_stop"]:
            status = "saturated"
        else:
            status = "productive"
            reasons.append(f"{family} has not met the strict trailing novelty rule")
        families[family] = {"status": status, "repo_count": data["repo_count"]}
    if report["product_denominator"] < 50:
        reasons.append("human product-property denominator is below 50")
    if conversion_report is None:
        reasons.append("PR4 conversion checkpoint was not supplied")
    result = {
        "schema_version": SCHEMA_VERSION,
        "cohort_id": checked["cohort_id"],
        "manifest_digest": checked["manifest_digest"],
        "decision": "continue" if reasons else "stop",
        "reason": "; ".join(reasons) if reasons else "all calibration criteria met",
        "continue_to_20": bool(reasons),
        "continue_to_30": "pending_20_repo_run",
        "failures": [],
        "families": families,
        "compiler_stop": report["compiler_stop"],
        "product_denominator": report["product_denominator"],
        "conversion_checkpoint_supplied": conversion_report is not None,
    }
    return result


def dumps(value: Mapping[str, Any]) -> str:
    """Serialize a calibration artifact deterministically."""
    return json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n"


def dumps_digest(value: Mapping[str, Any]) -> str:
    """Return a digest for an emitted artifact, excluding no fields."""
    return hashlib.sha256(dumps(value).encode("utf-8")).hexdigest()


def render_closeout(closeout: Mapping[str, Any]) -> str:
    """Render a concise, committed close-out memo."""
    lines = [
        "# Calibration close-out",
        "",
        f"- Decision: **{closeout['decision']}**",
        f"- Cohort: `{closeout['cohort_id']}`",
        f"- Manifest digest: `{closeout['manifest_digest']}`",
        f"- Continue to 20: **{str(closeout['continue_to_20']).lower()}**",
        f"- Continue to 30: **{closeout['continue_to_30']}**",
        "",
        f"Reason: {closeout['reason']}",
        "",
        "Per-family outcomes:",
        "",
    ]
    for family, data in sorted(closeout.get("families", {}).items()):
        lines.append(f"- `{family}`: {data['status']} ({data['repo_count']} repos)")
    if closeout.get("failures"):
        lines.extend(["", "Skipped/failed repositories:", ""])
        for failure in closeout["failures"]:
            lines.append(f"- `{failure['repo_id']}`: {failure['status']} — {failure['reason']}")
    return "\n".join(lines) + "\n"
