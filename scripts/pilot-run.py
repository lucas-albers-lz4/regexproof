#!/usr/bin/env python3
"""Phase 2 pilot runner: extract → compile → encodable-fraction → report.

Argv-only subprocesses; TIMEOUT treated as not-proven in property harness.
"""

from __future__ import annotations

import json
import platform
import subprocess
import sys
from collections import Counter
from pathlib import Path

import z3

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.compiler import compile_pattern  # noqa: E402
from regexproof.compiler.normalize import normalize_inline_flags  # noqa: E402
from regexproof.extractors.js_babel import extract_js  # noqa: E402
from regexproof.extractors.rule_file import extract_rule_file  # noqa: E402
from regexproof.fuzz.adapters import reject_shell_subprocess_usage  # noqa: E402
from regexproof.schemas import EXTRACTOR_SCHEMA_VERSION  # noqa: E402

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None


def engine_versions() -> dict[str, str]:
    versions = {
        "python": platform.python_version(),
        "z3": z3.get_version_string(),
    }
    try:
        node = subprocess.run(
            ["node", "--version"], capture_output=True, text=True, shell=False, check=False
        )
        if node.returncode == 0:
            versions["node"] = node.stdout.strip()
    except FileNotFoundError:
        versions["node"] = "unavailable"
    try:
        go = subprocess.run(
            ["go", "version"], capture_output=True, text=True, shell=False, check=False
        )
        if go.returncode == 0:
            versions["go"] = go.stdout.strip()
    except FileNotFoundError:
        versions["go"] = "unavailable"
    return versions


def compile_record(rec: dict, *, lift_inline: bool = False) -> dict:
    pattern = rec["pattern"]
    flags = rec.get("flags") or ""
    if lift_inline:
        pattern, flags = normalize_inline_flags(pattern, flags)
    if rec.get("unencodable_reason"):
        return {
            **rec,
            "encodable": False,
            "compile_reason": rec["unencodable_reason"],
            "normalized_pattern": pattern,
            "normalized_flags": flags,
        }
    result = compile_pattern(
        pattern,
        flags=flags,
        dialect=rec["dialect"],
        call_kind=rec["call_kind"],
    )
    return {
        **rec,
        "encodable": result.encodable,
        "compile_reason": result.unencodable_reason,
        "normalized_pattern": pattern,
        "normalized_flags": flags,
        "declared_domain": result.declared_domain,
    }


def fraction_report(
    name: str,
    dialect: str,
    records: list[dict],
    *,
    lift_inline: bool,
    go_no_go_threshold: float,
) -> dict:
    compiled = [compile_record(r, lift_inline=lift_inline) for r in records]
    encodable = [c for c in compiled if c["encodable"]]
    reasons = Counter(c["compile_reason"] or "ok" for c in compiled)
    fraction = len(encodable) / len(compiled) if compiled else 0.0
    decision = "go" if fraction >= go_no_go_threshold else "no-go"
    return {
        "schema_version": "1",
        "pilot": name,
        "dialect": dialect,
        "extractor_schema_version": EXTRACTOR_SCHEMA_VERSION,
        "sample_size": len(compiled),
        "encodable": len(encodable),
        "fraction": round(fraction, 4),
        "go_no_go_threshold": go_no_go_threshold,
        "decision": decision,
        "decision_rule": (
            f"go iff encodable/sample_size >= {go_no_go_threshold} "
            "(Phase 3 admits only encodable pairs; no-go blocks scaling that corpus)"
        ),
        "reasons": dict(reasons),
        "call_kinds": dict(Counter(c["call_kind"] for c in compiled)),
        "engine_versions": engine_versions(),
        "shell_true_violations": reject_shell_subprocess_usage(),
        "records": [
            {
                "regex_id": c["regex_id"],
                "site": c["site"],
                "call_kind": c["call_kind"],
                "dialect": c["dialect"],
                "encodable": c["encodable"],
                "reason": c["compile_reason"],
                "pattern": (c.get("normalized_pattern") or c["pattern"])[:120],
                "flags": c.get("normalized_flags") or c.get("flags") or "",
            }
            for c in compiled
        ],
    }


def run_validatorjs(manifest: dict) -> dict:
    src = ROOT / manifest["corpus_path"]
    recs: list[dict] = []
    for path in sorted(src.rglob("*.js")):
        recs.extend(
            extract_js(
                path.read_text(encoding="utf-8"),
                repo=manifest["repo"],
                file=str(path.relative_to(ROOT)),
            )
        )
    if jsonschema is not None:
        from regexproof.schemas import extractor_schema

        schema = extractor_schema()
        for r in recs:
            jsonschema.validate(r, schema)
    report = fraction_report(
        "validatorjs",
        "ecma",
        recs,
        lift_inline=False,
        go_no_go_threshold=manifest["go_no_go_threshold"],
    )
    report["manifest"] = manifest
    return report


def run_gitleaks(manifest: dict) -> dict:
    path = ROOT / manifest["corpus_path"]
    recs = extract_rule_file(
        path.read_text(encoding="utf-8"),
        repo=manifest["repo"],
        file=str(path.relative_to(ROOT)),
        dialect="re2",
    )
    if jsonschema is not None:
        from regexproof.schemas import extractor_schema

        schema = extractor_schema()
        for r in recs:
            jsonschema.validate(r, schema)
    report = fraction_report(
        "gitleaks",
        "re2",
        recs,
        lift_inline=True,
        go_no_go_threshold=manifest["go_no_go_threshold"],
    )
    report["manifest"] = manifest
    report["selection_rationale"] = manifest["selection_rationale"]
    return report


def main() -> int:
    vjs_manifest = json.loads((ROOT / "pilots/validatorjs/manifest.json").read_text())
    gl_manifest = json.loads((ROOT / "pilots/gitleaks/manifest.json").read_text())
    out_dir = ROOT / "properties" / "generated"
    out_dir.mkdir(parents=True, exist_ok=True)

    vjs = run_validatorjs(vjs_manifest)
    gl = run_gitleaks(gl_manifest)

    (out_dir / "validatorjs_encodable_fraction.json").write_text(
        json.dumps(vjs, indent=2) + "\n", encoding="utf-8"
    )
    (out_dir / "gitleaks_encodable_fraction.json").write_text(
        json.dumps(gl, indent=2) + "\n", encoding="utf-8"
    )

    summary = {
        "schema_version": "1",
        "pilots": {
            "validatorjs": {
                "fraction": vjs["fraction"],
                "decision": vjs["decision"],
                "sample_size": vjs["sample_size"],
                "encodable": vjs["encodable"],
            },
            "gitleaks": {
                "fraction": gl["fraction"],
                "decision": gl["decision"],
                "sample_size": gl["sample_size"],
                "encodable": gl["encodable"],
            },
        },
        "shell_true_violations": reject_shell_subprocess_usage(),
        "engine_versions": engine_versions(),
        "timeout_policy": "TIMEOUT/unknown = not proven (never a pass)",
    }
    (out_dir / "phase2_pilot_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))
    if summary["shell_true_violations"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
