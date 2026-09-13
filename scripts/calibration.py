#!/usr/bin/env python3
"""Execute the pinned PR5 calibration and emit its evidence bundle."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.calibration import (  # noqa: E402
    CalibrationError,
    build_closeout,
    build_observation_artifact,
    dumps,
    load_manifest,
    render_closeout,
    saturation_envelope,
)
from regexproof.mine.saturation import build_report  # noqa: E402


def _repo_mapping(values: list[str]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for value in values:
        repo_id, separator, path = value.partition("=")
        if not separator or not repo_id or not path:
            raise CalibrationError("--repo must use REPO_ID=CHECKOUT_PATH")
        if repo_id in result:
            raise CalibrationError(f"duplicate --repo mapping for {repo_id!r}")
        result[repo_id] = Path(path)
    return result


def _load_optional(path: Path | None) -> dict:
    if path is None:
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CalibrationError(f"cannot read {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CalibrationError(f"{path} must contain a JSON object")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "The command never clones or updates repositories. Every --repo checkout "
            "must already be at the exact 40-character pin in the frozen manifest."
        ),
    )
    parser.add_argument("manifest", type=Path, help="PR2 frozen cohort manifest")
    parser.add_argument("--repo", action="append", default=[], metavar="ID=PATH", help="pinned local checkout (repeatable)")
    parser.add_argument("--reject-buckets", type=Path, help="optional JSON map of repo_id to exact new reject-bucket strings")
    parser.add_argument("--conversion-report", type=Path, help="optional PR4 checkpoint report for close-out context")
    parser.add_argument(
        "--expected-repos",
        type=int,
        help="optional fail-closed assertion for the frozen cohort size",
    )
    parser.add_argument("--output-dir", type=Path, required=True, help="directory for the evidence bundle")
    args = parser.parse_args(argv)
    try:
        manifest = load_manifest(args.manifest)
        if args.expected_repos is not None and args.expected_repos <= 0:
            raise CalibrationError(
                "--expected-repos must be a positive integer"
            )
        if (
            args.expected_repos is not None
            and len(manifest["repos"]) != args.expected_repos
        ):
            raise CalibrationError(
                f"expected {args.expected_repos} manifest repositories; "
                f"got {len(manifest['repos'])}"
            )
        artifact = build_observation_artifact(
            manifest,
            _repo_mapping(args.repo),
            reject_buckets=_load_optional(args.reject_buckets),
        )
        closeout = build_closeout(
            artifact,
            conversion_report=_load_optional(args.conversion_report) or None,
        )
        args.output_dir.mkdir(parents=True, exist_ok=True)
        (args.output_dir / "canonical-observations.json").write_text(dumps(artifact), encoding="utf-8")
        (args.output_dir / "skip-failure-log.json").write_text(
            dumps({"cohort_id": artifact["cohort_id"], "failures": artifact["failures"]}),
            encoding="utf-8",
        )
        (args.output_dir / "closeout.json").write_text(dumps(closeout), encoding="utf-8")
        (args.output_dir / "closeout.md").write_text(render_closeout(closeout), encoding="utf-8")
        if not artifact["failures"]:
            (args.output_dir / "saturation-report.json").write_text(
                dumps(build_report(saturation_envelope(artifact))), encoding="utf-8"
            )
    except CalibrationError as exc:
        print(f"calibration: error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
