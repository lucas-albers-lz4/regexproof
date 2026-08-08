"""Batch orchestrator: extract → triage → intent → (optional redos join) → report."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

from regexproof.batch.disclose import (  # noqa: E402
    assert_no_auto_publication,
    tag_disclosure,
    write_pr_dry_run,
)
from regexproof.batch.evidence import enforce_evidence_gates  # noqa: E402
from regexproof.batch.intent import (  # noqa: E402
    detect_intent_mismatches,
    detect_usage_mismatches,
)
from regexproof.batch.inventory import check_corpus_coverage, load_inventory  # noqa: E402
from regexproof.batch.report import write_markdown, write_ndjson  # noqa: E402
from regexproof.batch.triage import triage_records_from_compiled, write_triage_ndjson  # noqa: E402
from regexproof.compiler import compile_pattern  # noqa: E402
from regexproof.compiler.normalize import normalize_inline_flags  # noqa: E402
from regexproof.extractors.busybox_tests import extract_busybox_tests  # noqa: E402
from regexproof.extractors.cpython_re_tests import extract_cpython_re_tests  # noqa: E402
from regexproof.extractors.go_regexp import extract_go_regexp  # noqa: E402
from regexproof.extractors.ids_rules import extract_ids_rules  # noqa: E402
from regexproof.extractors.js_babel import extract_js  # noqa: E402
from regexproof.extractors.modsec import count_operators, extract_modsec  # noqa: E402
from regexproof.extractors.pcre2_testdata import extract_pcre2_testdata  # noqa: E402
from regexproof.extractors.python_ast import extract_python  # noqa: E402
from regexproof.extractors.rule_file import extract_rule_file  # noqa: E402
from regexproof.redos.join import join_findings  # noqa: E402

CORPUS_MANIFESTS: dict[str, dict[str, Any]] = {
    "gitleaks": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "pilots" / "gitleaks" / "config" / "gitleaks.toml",
        "dialect": "re2",
        "extractor": "rule_file",
        "repo": "gitleaks/gitleaks",
        "security_tool": True,
        "lift_inline": True,
    },
    "validatorjs": {
        "corpus_type": "validator",
        "path": ROOT / "pilots" / "validatorjs" / "src",
        # Verified domain (Phase 4): the 7-file pilot subset. Full upstream
        # src/lib inventory (~103 files) is measured separately; this manifest
        # is the declared verified domain for property execution.
        "files": [
            "isAscii.js",
            "isAlpha.js",
            "isAlphanumeric.js",
            "isEmail.js",
            "isFQDN.js",
            "isURL.js",
            "alpha.js",
        ],
        "verified_domain": "pilots/validatorjs/src/{isAscii,isAlpha,isAlphanumeric,isEmail,isFQDN,isURL,alpha}.js",
        "dialect": "ecma",
        "extractor": "js_dir",
        "repo": "validatorjs/validator.js",
        "security_tool": False,
        "lift_inline": False,
    },
    "detect-secrets": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "pilots" / "detect-secrets" / "sample_plugins.py",
        "dialect": "py_re",
        "extractor": "python",
        "repo": "Yelp/detect-secrets",
        "security_tool": True,
        "lift_inline": False,
    },
    "coreruleset": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "batch" / "corpora" / "coreruleset" / "rules",
        "dialect": "pcre",
        "extractor": "modsec",
        "repo": "coreruleset/coreruleset",
        "security_tool": True,
        "lift_inline": True,
    },
    "trufflehog": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "batch" / "corpora" / "trufflehog" / "detectors",
        "glob": "**/*.go",
        "dialect": "re2",
        "extractor": "go_regexp",
        "repo": "trufflesecurity/trufflehog",
        "security_tool": True,
        "lift_inline": True,
        "corpus_pin": "v3.88.29",
        "commit": "90190deac64289cb10bb694894be8db9ead8790b",
        "budget": {"max_patterns": 5000, "max_wall_s": 600},
    },
    "ids_rules": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "batch" / "corpora" / "ids_rules" / "rules",
        "glob": "*.rules",
        "dialect": "pcre",
        "extractor": "ids_rules",
        "repo": "emergingthreats/open",
        "security_tool": True,
        "lift_inline": True,
        "corpus_pin": "suricata-7.0.3-et-open",
        "commit": "emergingthreats-open-suricata-7.0.3",
        "budget": {"max_patterns": 20000, "max_wall_s": 900},
    },
    "semgrep_rules": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "batch" / "corpora" / "semgrep_rules" / "rules",
        "glob": "**/*.yml,**/*.yaml",
        "dialect": "py_re",
        "extractor": "semgrep_yaml",
        "repo": "semgrep/semgrep-rules",
        "security_tool": True,
        "lift_inline": True,
        "corpus_pin": "40b8c63f75dc7c22c8a77482d73bfb864b146f7e",
        "commit": "40b8c63f75dc7c22c8a77482d73bfb864b146f7e",
        "budget": {"max_patterns": 5000, "max_wall_s": 600},
    },
    "re2_testdata": {
        "corpus_type": "testdata",
        "path": ROOT / "batch" / "corpora" / "re2_testdata" / "sample" / "patterns.toml",
        "dialect": "re2",
        "extractor": "rule_file",
        "repo": "google/re2",
        "security_tool": False,
        "lift_inline": False,
        "corpus_pin": "2024-07-02",
        "measure_scope": "sample",
        "budget": {"max_patterns": 5000, "max_wall_s": 300},
    },
    "pcre2_testdata": {
        "corpus_type": "testdata",
        # Full testdata can OOM the process; prefer sample for CI / default path.
        "path": ROOT / "batch" / "corpora" / "pcre2_testdata" / "sample",
        "glob": "testinput*",
        "dialect": "pcre",
        "extractor": "pcre2_testdata",
        "repo": "PCRE2Project/pcre2",
        "security_tool": False,
        "lift_inline": False,
        "corpus_pin": "pcre2-10.44",
        "measure_scope": "sample",
        "budget": {"max_patterns": 20000, "max_wall_s": 900},
    },
    "cpython_re": {
        "corpus_type": "testdata",
        "path": ROOT / "batch" / "corpora" / "cpython_re" / "re_tests.py",
        "dialect": "py_re",
        "extractor": "cpython_re_tests",
        "repo": "python/cpython",
        "security_tool": False,
        "lift_inline": False,
        "corpus_pin": "v3.12.8",
        "measure_scope": "sample",
        "budget": {"max_patterns": 5000, "max_wall_s": 300},
    },
    "busybox": {
        "corpus_type": "testdata",
        # Default to sample; materialize full testsuite via README symlink.
        "path": ROOT / "batch" / "corpora" / "busybox" / "sample",
        "glob": "*.tests",
        "dialect": "pcre",
        "extractor": "busybox_tests",
        "repo": "mirror/busybox",
        "security_tool": False,
        "lift_inline": False,
        "corpus_pin": "1_36_1",
        "measure_scope": "sample",
        "budget": {"max_patterns": 5000, "max_wall_s": 300},
    },
    "rust_regex": {
        "corpus_type": "inventory_only",
        "path": ROOT / "batch" / "corpora" / "rust_regex" / "sample",
        "dialect": "rust_regex",
        "extractor": "rust_inventory",
        "repo": "rust-lang/regex",
        "security_tool": False,
        "lift_inline": False,
        "corpus_pin": "1.11.1",
        "measure_scope": "sample",
        "budget": {"max_patterns": 0, "max_wall_s": 60},
    },
}


def _extract(corpus: str, meta: dict[str, Any]) -> list[dict[str, Any]]:
    path: Path = meta["path"]
    if meta["extractor"] == "rule_file":
        source = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        return extract_rule_file(
            source, repo=meta["repo"], file=rel, dialect=meta["dialect"]
        )
    if meta["extractor"] == "modsec":
        out: list[dict[str, Any]] = []
        root_resolved = ROOT.resolve()
        for fp in sorted(path.glob("*.conf")):
            try:
                rel = str(fp.resolve().relative_to(root_resolved))
            except ValueError:
                rel = str(fp)
            out.extend(
                extract_modsec(
                    fp.read_text(encoding="utf-8", errors="replace"),
                    repo=meta["repo"],
                    file=rel,
                )
            )
        return out
    if meta["extractor"] == "js_dir":
        out: list[dict[str, Any]] = []
        for name in meta.get("files") or sorted(p.name for p in path.glob("*.js")):
            fp = path / name
            rel = str(fp.relative_to(ROOT))
            out.extend(extract_js(fp.read_text(encoding="utf-8"), repo=meta["repo"], file=rel))
        return out
    if meta["extractor"] == "js":
        source = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        return extract_js(source, repo=meta["repo"], file=rel)
    if meta["extractor"] == "python":
        source = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        return extract_python(source, repo=meta["repo"], file=rel)
    if meta["extractor"] == "go_regexp":
        return _extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.go",
            extract_fn=lambda src, rel: extract_go_regexp(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "ids_rules":
        return _extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "*.rules",
            extract_fn=lambda src, rel: extract_ids_rules(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "semgrep_yaml":
        return _extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.yml,**/*.yaml",
            extract_fn=lambda src, rel: extract_rule_file(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "pcre2_testdata":
        return _extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "testinput*",
            extract_fn=lambda src, rel: extract_pcre2_testdata(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "cpython_re_tests":
        source = path.read_text(encoding="utf-8", errors="replace")
        try:
            rel = str(path.resolve().relative_to(ROOT.resolve()))
        except ValueError:
            rel = str(path)
        return extract_cpython_re_tests(
            source, repo=meta["repo"], file=rel, dialect=meta["dialect"]
        )
    if meta["extractor"] == "busybox_tests":
        return _extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "*.tests",
            extract_fn=lambda src, rel: extract_busybox_tests(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    raise ValueError(meta["extractor"])


def _extract_glob(
    path: Path,
    meta: dict[str, Any],
    *,
    glob: str,
    extract_fn,
) -> list[dict[str, Any]]:
    """Deterministic directory walk: sorted paths, fixed order.

    ``glob`` may be a single pattern or a comma-separated list (brace-free),
    e.g. ``**/*.yml,**/*.yaml``.
    """
    out: list[dict[str, Any]] = []
    root_resolved = ROOT.resolve()
    if not path.is_dir():
        return out
    files: list[Path] = []
    for pattern in glob.split(","):
        pattern = pattern.strip()
        if not pattern:
            continue
        files.extend(path.glob(pattern))
    seen: set[Path] = set()
    for fp in sorted(files, key=lambda p: str(p)):
        if fp in seen or not fp.is_file():
            continue
        seen.add(fp)
        try:
            rel = str(fp.resolve().relative_to(root_resolved))
        except ValueError:
            rel = str(fp)
        out.extend(
            extract_fn(fp.read_text(encoding="utf-8", errors="replace"), rel)
        )
    return out


def _compile_all(
    records: list[dict[str, Any]], *, lift_inline: bool, corpus_slug: str
) -> list[dict[str, Any]]:
    out = []
    for rec in records:
        pattern = rec["pattern"]
        flags = rec.get("flags") or ""
        if lift_inline:
            pattern, flags = normalize_inline_flags(pattern, flags)
        if rec.get("unencodable_reason"):
            out.append(
                {
                    **rec,
                    "encodable": False,
                    "compile_reason": rec["unencodable_reason"],
                    "corpus": corpus_slug,
                    "corpus_slug": corpus_slug,
                }
            )
            continue
        cr = compile_pattern(pattern, flags, rec["dialect"], rec["call_kind"])
        out.append(
            {
                **rec,
                "pattern": pattern,
                "flags": flags,
                "encodable": cr.encodable,
                "compile_reason": cr.unencodable_reason,
                "corpus": corpus_slug,
                "corpus_slug": corpus_slug,
            }
        )
    return out


def run_corpus(
    corpus: str,
    *,
    out_dir: Path,
    with_redos: bool = False,
    approval_path: Path | None = None,
    require_ground_truth: bool = False,
    fail_planned: bool = False,
    redos_cap: int | None = None,
    emit_planned: bool = True,
) -> dict[str, Any]:
    meta = CORPUS_MANIFESTS[corpus]
    if meta.get("corpus_type") == "inventory_only":
        from regexproof.extractors.rust_inventory import write_rust_inventory

        path: Path = meta["path"]
        report = write_rust_inventory(path, out_dir / f"{corpus}_inventory_only.json")
        return {
            "corpus": corpus,
            "findings": 0,
            "encodable": report.get("extracted"),
            "decision": "inventory_only",
            "detail": report,
        }
    inventory = load_inventory(meta["corpus_type"])
    records = _extract(corpus, meta)
    compiled = _compile_all(
        records, lift_inline=bool(meta.get("lift_inline")), corpus_slug=corpus
    )

    triage = triage_records_from_compiled(compiled)
    write_triage_ndjson(out_dir.parent / "triage" / f"{corpus}.ndjson", triage)

    findings: list[dict[str, Any]] = []
    # Inventory-driven shape markers (auto property stubs — encode deferred to Z3 job)
    if emit_planned:
        for q in inventory["questions"]:
            findings.append(
                {
                    "schema_version": "1",
                    "regex_id": f"inventory:{q['id']}",
                    "kind": "property",
                    "corpus": corpus,
                    "result": "planned",
                    "site": f"inventory:{q['id']}",
                    "pattern": "",
                    "shape": q["shape"],
                    "disclosure": None,
                    "detail": {"question_id": q["id"], "threat": q["threat"]},
                }
            )

    findings.extend(detect_usage_mismatches(compiled))
    findings.extend(detect_intent_mismatches(compiled))

    redos_findings: list[dict[str, Any]] = []
    redos_incomplete = False
    if with_redos:
        from regexproof.redos.runner import analyze_record

        for rec in compiled:
            if not rec.get("encodable"):
                continue
            if redos_cap is not None and len(redos_findings) >= redos_cap:
                redos_incomplete = True
                break
            for f in analyze_record(rec, triage=False):
                redos_findings.append(f)
                findings.append(
                    {
                        "schema_version": "1",
                        "regex_id": f["regex_id"],
                        "kind": "redos",
                        "corpus": corpus,
                        "result": f["result"],
                        "site": f.get("site") or "",
                        "pattern": f.get("pattern") or "",
                        "shape": None,
                        "disclosure": "private_first" if meta.get("security_tool") else None,
                        "engine_versions": (
                            {str(f.get("tool")): str(f.get("tool_version"))}
                            if f.get("tool")
                            else None
                        ),
                        "detail": {"tool": f.get("tool"), "severity": f.get("severity")},
                    }
                )

    if redos_incomplete:
        findings.append(
            {
                "schema_version": "1",
                "regex_id": f"redos-incomplete:{corpus}",
                "kind": "redos",
                "corpus": corpus,
                "result": "incomplete",
                "site": f"redos-cap:{redos_cap}",
                "pattern": "",
                "shape": None,
                "disclosure": "private_first" if meta.get("security_tool") else None,
                "detail": {
                    "error": f"ReDoS fan-out truncated at cap={redos_cap}",
                    "findings_emitted": len(redos_findings),
                },
            }
        )

    # Join Z3-side placeholders with redos (separate sections)
    z3_side = [{"regex_id": f["regex_id"], "result": f["result"]} for f in findings if f["kind"] != "redos"]
    joined = join_findings(z3_side, redos_findings)

    findings = tag_disclosure(findings, corpus=corpus)
    enforce_evidence_gates(
        findings,
        require_ground_truth=require_ground_truth,
        fail_planned=fail_planned,
    )
    if redos_incomplete:
        raise SystemExit(
            f"evidence gate failed: ReDoS report incomplete (cap={redos_cap}); "
            "omit --redos-cap for an uncapped run"
        )
    write_ndjson(out_dir / f"{corpus}.ndjson", findings)
    # Keep Phase 3 shape-5 report at {corpus}.md; batch uses a distinct path.
    write_markdown(out_dir / f"{corpus}_batch.md", corpus=corpus, findings=findings)

    dry = write_pr_dry_run(
        out_dir / f"{corpus}-pr-dry-run.json",
        findings=findings,
        approval_path=approval_path,
    )
    assert_no_auto_publication(dry)

    summary = {
        "schema_version": "1",
        "corpus": corpus,
        "corpus_type": meta["corpus_type"],
        "extracted": len(records),
        "encodable": sum(1 for c in compiled if c.get("encodable")),
        "triage": len(triage),
        "findings": len(findings),
        "inventory_questions": len(inventory["questions"]),
        "join_regex_ids": len(joined.get("regex_ids") or []),
        "engine": {"python": platform.python_version()},
        "redos_findings": len(redos_findings),
        "redos_incomplete": redos_incomplete,
    }
    (out_dir / f"{corpus}_batch_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return summary


def measure_coreruleset_sample(out_dir: Path) -> dict[str, Any]:
    """PCRE encodable-fraction gate on pinned CRS sample; go iff >= 0.30."""
    sample = ROOT / "batch" / "corpora" / "coreruleset" / "sample.rules"
    lines = [
        ln.strip()
        for ln in sample.read_text(encoding="utf-8").splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]
    encodable = 0
    for i, pat in enumerate(lines):
        cr = compile_pattern(pat, "", "pcre", "search")
        if cr.encodable:
            encodable += 1
    n = len(lines) or 1
    fraction = encodable / n
    decision = "go" if fraction >= 0.30 else "no-go"
    report = {
        "schema_version": "1",
        "pilot": "coreruleset",
        "dialect": "pcre",
        "sample_size": len(lines),
        "encodable": encodable,
        "fraction": fraction,
        "go_no_go_threshold": 0.3,
        "decision": decision,
        "sample_path": str(sample.relative_to(ROOT)),
        "scope": "sample",
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    (out_dir / "coreruleset_sample_encodable_fraction.json").write_text(
        payload, encoding="utf-8"
    )
    # When full corpus is absent, the sample report is the primary artifact.
    (out_dir / "coreruleset_encodable_fraction.json").write_text(
        payload, encoding="utf-8"
    )
    return report


def measure_coreruleset_full(out_dir: Path) -> dict[str, Any] | None:
    """Full-corpus CRS fraction (modsec extractor + normalize → compile_pcre).

    Returns None when ``batch/corpora/coreruleset/rules`` is not materialized.
    Writes ``coreruleset_encodable_fraction.json`` (primary artifact) and
    ``crs-inventory.ndjson`` for P2/P3 handoff. @rx-only numerator matches the
    Phase-1 GO comment (selectors reported separately).
    """
    from collections import Counter

    import platform as _platform

    import z3

    rules_dir = ROOT / "batch" / "corpora" / "coreruleset" / "rules"
    if not rules_dir.is_dir():
        return None

    records: list[dict[str, Any]] = []
    op_counts: Counter[str] = Counter()
    for fp in sorted(rules_dir.glob("*.conf")):
        src = fp.read_text(encoding="utf-8", errors="replace")
        op_counts.update(count_operators(src))
        rel = str(fp.relative_to(ROOT))
        records.extend(extract_modsec(src, repo="coreruleset/coreruleset", file=rel))

    compiled = _compile_all(records, lift_inline=True, corpus_slug="coreruleset")
    rx_only = [c for c in compiled if not c.get("selector")]
    selectors = [c for c in compiled if c.get("selector")]
    rx_enc = [c for c in rx_only if c.get("encodable")]
    n = len(rx_only) or 1
    fraction = len(rx_enc) / n
    decision = "go" if fraction >= 0.30 else "no-go"
    reasons = Counter((c.get("compile_reason") or "ok") for c in rx_only)

    out_dir.mkdir(parents=True, exist_ok=True)
    inv_path = out_dir / "crs-inventory.ndjson"
    with inv_path.open("w", encoding="utf-8") as fh:
        for c in compiled:
            fh.write(
                json.dumps(
                    {
                        "regex_id": c.get("regex_id"),
                        "rule_id": c.get("rule_id"),
                        "site": c.get("site"),
                        "pattern": c.get("pattern"),
                        "flags": c.get("flags") or "",
                        "dialect": c.get("dialect"),
                        "call_kind": c.get("call_kind"),
                        "encodable": bool(c.get("encodable")),
                        "compile_reason": c.get("compile_reason"),
                        "negated": c.get("negated"),
                        "selector": bool(c.get("selector")),
                        "corpus": "coreruleset",
                    },
                    sort_keys=True,
                )
                + "\n"
            )

    report = {
        "schema_version": "1",
        "pilot": "coreruleset",
        "dialect": "pcre",
        "scope": "full_corpus",
        "corpus_pin": "v4.28.0",
        "sample_size": len(rx_only),
        "encodable": len(rx_enc),
        "fraction": round(fraction, 4),
        "go_no_go_threshold": 0.3,
        "decision": decision,
        "decision_rule": (
            "go iff @rx-only encodable/sample_size >= 0.3 "
            "(normalize_inline_flags → compile_pcre; selectors excluded from fraction)"
        ),
        "reasons": dict(reasons),
        "selectors": {
            "count": len(selectors),
            "encodable": sum(1 for c in selectors if c.get("encodable")),
        },
        "operators": dict(op_counts),
        "extracted_total": len(compiled),
        "inventory_path": str(inv_path),
        "engine_versions": {
            "python": _platform.python_version(),
            "z3": z3.get_version_string(),
        },
        "records": [
            {
                "regex_id": c.get("regex_id"),
                "rule_id": c.get("rule_id"),
                "site": c.get("site"),
                "call_kind": c.get("call_kind"),
                "dialect": c.get("dialect"),
                "encodable": bool(c.get("encodable")),
                "reason": c.get("compile_reason"),
                "pattern": (c.get("pattern") or "")[:120],
                "flags": c.get("flags") or "",
                "selector": bool(c.get("selector")),
            }
            for c in compiled
        ],
    }
    (out_dir / "coreruleset_encodable_fraction.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return report


def measure_coreruleset(out_dir: Path) -> dict[str, Any]:
    """Prefer full-corpus fraction when rules/ is present and out_dir is in-repo."""
    try:
        out_dir.resolve().relative_to((ROOT / "properties").resolve())
        in_repo_properties = True
    except ValueError:
        in_repo_properties = False
    if in_repo_properties:
        full = measure_coreruleset_full(out_dir)
        if full is not None:
            # Still emit sample artifact for CI smoke without depending on it for GO.
            measure_coreruleset_sample(out_dir)
            return full
    return measure_coreruleset_sample(out_dir)


def run_batch(
    corpora: list[str],
    *,
    out_dir: Path | None = None,
    with_redos: bool = False,
    require_ground_truth: bool = False,
    fail_planned: bool = False,
    redos_cap: int | None = None,
    emit_planned: bool = True,
) -> dict[str, Any]:
    cov = check_corpus_coverage()
    if cov:
        raise SystemExit("inventory coverage failed: " + "; ".join(cov))

    out_dir = out_dir or (ROOT / "properties" / "generated")
    out_dir.mkdir(parents=True, exist_ok=True)
    (ROOT / "properties" / "triage").mkdir(parents=True, exist_ok=True)

    summaries = {}
    pair_counts = {}
    for name in corpora:
        summaries[name] = run_corpus(
            name,
            out_dir=out_dir,
            with_redos=with_redos,
            require_ground_truth=require_ground_truth,
            fail_planned=fail_planned,
            redos_cap=redos_cap,
            emit_planned=emit_planned,
        )
        # Pair-at-scale: reuse Phase-3 discovery when catalog exists
        if name == "gitleaks":
            from regexproof.rule_diff.pairs import discover_pairs

            specs = ROOT / "pilots" / "gitleaks" / "canonical_specs" / "catalog.json"
            toml = ROOT / "pilots" / "gitleaks" / "config" / "gitleaks.toml"
            d = discover_pairs(toml_path=toml, specs_path=specs)
            pair_counts[name] = {
                "admitted": d["admitted_count"],
                "dropped": d["dropped_count"],
            }
        else:
            pair_counts[name] = {"admitted": 0, "dropped": 0, "note": "no independent-spec catalog"}

    crs = measure_coreruleset(out_dir)
    if crs["decision"] == "go":
        pair_counts["coreruleset"] = {
            "admitted": 0,
            "dropped": 0,
            "note": "fraction gate go; CRS rule-derived adapter is Phase-2 rule_diff",
            "scope": crs.get("scope"),
            "fraction": crs.get("fraction"),
        }
    else:
        pair_counts["coreruleset"] = {
            "admitted": 0,
            "note": f"excluded decision={crs['decision']} fraction={crs['fraction']}",
            "scope": crs.get("scope"),
        }

    batch = {
        "schema_version": "1",
        "corpora": summaries,
        "pair_counts": pair_counts,
        "coreruleset": {
            k: crs[k]
            for k in crs
            if k != "records"  # keep batch_summary compact; full report on disk
        },
    }
    (out_dir / "batch_pair_counts.json").write_text(
        json.dumps(pair_counts, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (out_dir / "batch_summary.json").write_text(
        json.dumps(batch, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    # Byte-identical fingerprint of triage+ndjson names for reproducibility smoke
    blob = ""
    for name in sorted(corpora):
        for suffix in (f"{name}.ndjson",):
            p = out_dir / suffix
            blob += hashlib.sha256(p.read_bytes()).hexdigest() + "\n"
    (out_dir / "batch_repro.sha256").write_text(blob, encoding="utf-8")
    return batch


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="regexproof batch scanner (Phase 5 NDJSON contract)",
    )
    ap.add_argument(
        "--corpus",
        default="all",
        help="gitleaks|validatorjs|detect-secrets|coreruleset|all",
    )
    ap.add_argument("--out", type=Path, default=ROOT / "properties" / "generated")
    ap.add_argument("--with-redos", action="store_true")
    ap.add_argument(
        "--redos-cap",
        type=int,
        default=None,
        help="optional ReDoS fan-out cap; truncation emits incomplete and fails the gate",
    )
    ap.add_argument(
        "--require-ground-truth",
        action="store_true",
        help="hard-fail SAT Z3 findings without reproduced ground_truth_status; "
        "TIMEOUT/unknown always hard-fails",
    )
    ap.add_argument(
        "--fail-planned",
        action="store_true",
        help="hard-fail inventory planned stubs (lists unexecuted question IDs)",
    )
    ap.add_argument(
        "--no-planned",
        action="store_true",
        help="omit inventory planned stubs from findings",
    )
    ap.add_argument(
        "--json-legacy",
        action="store_true",
        help="mutually exclusive legacy flag (rejected)",
    )
    args = ap.parse_args(argv)
    if args.json_legacy:
        print("error: --json-legacy is mutually exclusive with batch NDJSON", file=sys.stderr)
        return 2
    if args.corpus == "all":
        # coreruleset is opt-in: its corpus is an external pinned clone, not
        # committed (see batch/corpora/coreruleset/README.md).
        corpora = ["gitleaks", "validatorjs", "detect-secrets"]
    else:
        corpora = [args.corpus]
    run_batch(
        corpora,
        out_dir=args.out,
        with_redos=args.with_redos,
        require_ground_truth=args.require_ground_truth,
        fail_planned=args.fail_planned,
        redos_cap=args.redos_cap,
        emit_planned=not args.no_planned,
    )
    print("batch ok:", ", ".join(corpora))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
