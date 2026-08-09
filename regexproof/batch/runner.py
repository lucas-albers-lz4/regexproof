"""Batch orchestrator: extract → triage → intent → (optional redos join) → report."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import time
from pathlib import Path
from typing import Any

import jsonschema

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
from regexproof.batch.negation_policy import (  # noqa: E402
    NEGATED_UNSUPPORTED_REASON,
    should_reject_negated,
)
from regexproof.batch.report import write_markdown, write_ndjson  # noqa: E402
from regexproof.batch.triage import triage_records_from_compiled, write_triage_ndjson  # noqa: E402
from regexproof.compiler import compile_pattern  # noqa: E402
from regexproof.compiler.normalize import normalize_inline_flags  # noqa: E402
from regexproof.extractors.busybox_tests import extract_busybox_tests  # noqa: E402
from regexproof.extractors.cpython_re_tests import (  # noqa: E402
    extract_cpython_combined,
    extract_cpython_re_tests,
)
from regexproof.extractors.re2_testdata import extract_re2_testdata  # noqa: E402
from regexproof.extractors.go_regexp import extract_go_regexp  # noqa: E402
from regexproof.extractors.ids_rules import extract_ids_rules  # noqa: E402
from regexproof.extractors.js_babel import extract_js  # noqa: E402
from regexproof.extractors.modsec import count_operators, extract_modsec  # noqa: E402
from regexproof.extractors.pcre2_testdata import extract_pcre2_testdata  # noqa: E402
from regexproof.extractors.python_ast import extract_python  # noqa: E402
from regexproof.extractors.rule_file import extract_rule_file  # noqa: E402
from regexproof.extractors.spamassassin import extract_spamassassin  # noqa: E402
from regexproof.extractors.yara import extract_yara  # noqa: E402
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
        "budget": {"redos_wall_s": 120},
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
        "budget": {"redos_wall_s": 120},
    },
    "detect-secrets": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "batch" / "corpora" / "detect-secrets" / "plugins",
        "glob": "**/*.py",
        "dialect": "py_re",
        "extractor": "python_dir",
        "repo": "Yelp/detect-secrets",
        "security_tool": True,
        "lift_inline": False,
        "corpus_pin": "v1.5.0",
        "commit": "01886c8a910c64595c47f186ca1ffc0b77fa5458",
        "budget": {"redos_wall_s": 60},
    },
    "coreruleset": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "batch" / "corpora" / "coreruleset" / "rules",
        "dialect": "pcre",
        "extractor": "modsec",
        "repo": "coreruleset/coreruleset",
        "security_tool": True,
        "lift_inline": True,
        "budget": {"redos_wall_s": 180},
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
        "budget": {"max_patterns": 5000, "max_wall_s": 600, "redos_wall_s": 120, "max_mem_mb": 1024, "max_disk_mb": 100},
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
        "budget": {"max_patterns": 20000, "max_wall_s": 900, "redos_wall_s": 180, "max_mem_mb": 2048, "max_disk_mb": 200},
    },
    "semgrep_rules": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "batch" / "corpora" / "semgrep_rules" / "rules",
        "glob": "**/*.yml,**/*.yaml",
        # Semgrep evaluates pattern-regex via rust `regex` crate; stock path
        # is an ASCII approximation (declared + fidelity-fuzzed).
        "dialect": "py_re",
        "declared_semantics": "ascii_approx_rust_regex",
        "extractor": "semgrep_yaml",
        "repo": "semgrep/semgrep-rules",
        "security_tool": True,
        "lift_inline": True,
        "corpus_pin": "40b8c63f75dc7c22c8a77482d73bfb864b146f7e",
        "commit": "40b8c63f75dc7c22c8a77482d73bfb864b146f7e",
        "budget": {"max_patterns": 5000, "max_wall_s": 600, "redos_wall_s": 120, "max_mem_mb": 1024, "max_disk_mb": 100},
    },
    "re2_testdata": {
        "corpus_type": "testdata",
        "path": ROOT / "batch" / "corpora" / "re2_testdata" / "testdata",
        "full_path": ROOT / "batch" / "corpora" / "re2_testdata" / "testdata",
        "sample_path": ROOT / "batch" / "corpora" / "re2_testdata" / "sample",
        "glob": "*.txt",
        "dialect": "re2",
        "extractor": "re2_testdata",
        "repo": "google/re2",
        "security_tool": False,
        "lift_inline": False,
        "corpus_pin": "2024-07-02",
        "measure_scope": "sample",
        "budget": {"max_patterns": 5000, "max_wall_s": 300, "max_mem_mb": 512, "max_disk_mb": 50},
    },
    "pcre2_testdata": {
        "corpus_type": "testdata",
        "path": ROOT / "batch" / "corpora" / "pcre2_testdata" / "testdata",
        "full_path": ROOT / "batch" / "corpora" / "pcre2_testdata" / "testdata",
        "sample_path": ROOT / "batch" / "corpora" / "pcre2_testdata" / "sample",
        "glob": "testinput*",
        "dialect": "pcre",
        "extractor": "pcre2_testdata",
        "repo": "PCRE2Project/pcre2",
        "security_tool": False,
        "lift_inline": False,
        "corpus_pin": "pcre2-10.44",
        "measure_scope": "sample",
        "budget": {"max_patterns": 20000, "max_wall_s": 900, "max_mem_mb": 1024, "max_disk_mb": 100},
    },
    "cpython_re": {
        "corpus_type": "testdata",
        "path": ROOT / "batch" / "corpora" / "cpython_re",
        "full_path": ROOT / "batch" / "corpora" / "cpython_re",
        "sample_path": ROOT / "batch" / "corpora" / "cpython_re" / "re_tests.py",
        "glob": "*.py",
        "dialect": "py_re",
        "extractor": "cpython_re_tests",
        "repo": "python/cpython",
        "security_tool": False,
        "lift_inline": False,
        "corpus_pin": "v3.12.8",
        "measure_scope": "sample",
        "budget": {"max_patterns": 5000, "max_wall_s": 300, "max_mem_mb": 512, "max_disk_mb": 50},
    },
    "busybox": {
        "corpus_type": "testdata",
        "path": ROOT / "batch" / "corpora" / "busybox" / "testsuite",
        "full_path": ROOT / "batch" / "corpora" / "busybox" / "testsuite",
        "sample_path": ROOT / "batch" / "corpora" / "busybox" / "sample",
        "glob": "*.tests,**/*.tests",
        "dialect": "pcre",
        "extractor": "busybox_tests",
        "repo": "mirror/busybox",
        "security_tool": False,
        "lift_inline": False,
        "corpus_pin": "1_36_1",
        "measure_scope": "sample",
        "budget": {"max_patterns": 5000, "max_wall_s": 300, "max_mem_mb": 512, "max_disk_mb": 50},
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
    "yara_rules": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "batch" / "corpora" / "yara_rules" / "rules",
        "glob": "**/*.yar,**/*.yara",
        "dialect": "yara",
        "extractor": "yara",
        "repo": "YARA-Rules/rules",
        "security_tool": True,
        "lift_inline": False,
        "corpus_pin": "0f93570194a80d2f2032869055808b0ddcdfb360",
        "commit": "0f93570194a80d2f2032869055808b0ddcdfb360",
        # Full clone ~17.5k string sites; 5k was pre-enforcement decorative.
        "budget": {"max_patterns": 25000, "max_wall_s": 600, "redos_wall_s": 120, "max_mem_mb": 1024, "max_disk_mb": 100},
    },
    "test262": {
        "corpus_type": "testdata",
        "path": ROOT / "batch" / "corpora" / "test262" / "RegExp",
        "full_path": ROOT / "batch" / "corpora" / "test262" / "RegExp",
        "sample_path": ROOT / "batch" / "corpora" / "test262" / "sample",
        "glob": "**/*.js",
        "dialect": "ecma",
        "extractor": "test262",
        "repo": "tc39/test262",
        "security_tool": False,
        "lift_inline": False,
        "corpus_pin": "be13516fb6441b950ba8a3df97eb34062c186972",
        "expected_files": 1879,
        "measure_scope": "sample",
        "budget": {"max_patterns": 20000, "max_wall_s": 900, "max_mem_mb": 1024, "max_disk_mb": 200},
    },
    "spamassassin": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "batch" / "corpora" / "spamassassin" / "rules",
        "glob": "**/*.cf",
        "dialect": "perl",
        "extractor": "spamassassin",
        "repo": "apache/spamassassin",
        "security_tool": True,
        "lift_inline": True,
        "corpus_pin": "17e7842caa629d032589458f86d2f5ce8e7306a4",
        "commit": "17e7842caa629d032589458f86d2f5ce8e7306a4",
        "budget": {
            "max_patterns": 5000,
            "max_wall_s": 600,
            "redos_wall_s": 120,
            "max_mem_mb": 1024,
            "max_disk_mb": 100,
        },
    },
}

WAVE_CORPORA = frozenset({
    "trufflehog", "ids_rules", "semgrep_rules",
    "pcre2_testdata", "re2_testdata", "cpython_re", "busybox",
    "yara_rules", "test262", "spamassassin",
})


class BudgetBreached(Exception):
    """Raised when a corpus budget limit is exceeded."""

    def __init__(self, corpus: str, field: str, limit: Any, actual: Any) -> None:
        self.corpus = corpus
        self.field = field
        self.limit = limit
        self.actual = actual
        super().__init__(
            f"budget breach: {corpus}.{field} limit={limit} actual={actual}"
        )


def _check_budget_patterns(
    records: list[dict[str, Any]],
    budget: dict[str, Any],
    corpus_slug: str,
) -> None:
    max_pat = budget.get("max_patterns")
    if max_pat is not None and max_pat > 0 and len(records) > max_pat:
        raise BudgetBreached(corpus_slug, "max_patterns", max_pat, len(records))


def _check_budget_mem() -> int:
    """Return current process RSS in MB (best-effort)."""
    try:
        import resource
        usage = resource.getrusage(resource.RUSAGE_SELF)
        return int(usage.ru_maxrss / 1024)
    except Exception:  # noqa: BLE001
        return 0


def _validate_expected_roots(corpus: str, meta: dict[str, Any]) -> None:
    """Fail closed when expected corpus path/glob would produce zero files."""
    path: Path = meta["path"]
    if not path.exists():
        if corpus in WAVE_CORPORA:
            raise SystemExit(
                f"HARD ERROR: expected root missing for {corpus}: {path}"
            )
        return
    if path.is_dir():
        glob_pat = meta.get("glob") or ""
        if glob_pat:
            files = []
            for pat in glob_pat.split(","):
                pat = pat.strip()
                if pat:
                    files.extend(path.glob(pat))
            if not files and corpus in WAVE_CORPORA:
                raise SystemExit(
                    f"HARD ERROR: {corpus} glob '{glob_pat}' at {path} "
                    f"matched 0 files — fail closed on empty root"
                )


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
    if meta["extractor"] == "python_dir":
        return _extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.py",
            extract_fn=lambda src, rel: extract_python(
                src, repo=meta["repo"], file=rel
            ),
        )
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
        from regexproof.extractors.semgrep_yaml import extract_semgrep_yaml

        return _extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.yml,**/*.yaml",
            extract_fn=lambda src, rel: extract_semgrep_yaml(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "re2_testdata":
        if path.is_file():
            source = path.read_text(encoding="utf-8", errors="replace")
            try:
                rel = str(path.resolve().relative_to(ROOT.resolve()))
            except ValueError:
                rel = str(path)
            return extract_re2_testdata(
                source, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            )
        return _extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "*.txt",
            extract_fn=lambda src, rel: extract_re2_testdata(
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
        if path.is_dir():
            sources: dict[str, str] = {}
            for fp in sorted(path.glob(meta.get("glob") or "*.py")):
                if fp.is_file():
                    try:
                        rel = str(fp.resolve().relative_to(ROOT.resolve()))
                    except ValueError:
                        rel = str(fp)
                    sources[fp.name] = fp.read_text(encoding="utf-8", errors="replace")
            if sources:
                try:
                    base = str(path.resolve().relative_to(ROOT.resolve()))
                except ValueError:
                    base = str(path)
                return extract_cpython_combined(
                    sources, repo=meta["repo"], base_path=base,
                )
        if path.is_file():
            source = path.read_text(encoding="utf-8", errors="replace")
            try:
                rel = str(path.resolve().relative_to(ROOT.resolve()))
            except ValueError:
                rel = str(path)
            return extract_cpython_re_tests(
                source, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            )
        return []
    if meta["extractor"] == "busybox_tests":
        return _extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "*.tests",
            extract_fn=lambda src, rel: extract_busybox_tests(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "yara":
        return _extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.yar,**/*.yara",
            extract_fn=lambda src, rel: extract_yara(
                src, repo=meta["repo"], file=rel
            ),
        )
    if meta["extractor"] == "spamassassin":
        return _extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.cf",
            extract_fn=lambda src, rel: extract_spamassassin(
                src, repo=meta["repo"], file=rel
            ),
        )
    if meta["extractor"] == "test262":
        from regexproof.extractors.test262 import extract_test262, extract_test262_tree

        if path.is_dir() and meta.get("measure_scope") != "sample":
            # Full tree: use dedicated walker + expected-file gate.
            expected = meta.get("expected_files")
            recs, stats = extract_test262_tree(
                path,
                repo=meta["repo"],
                expected_files=expected,
            )
            if expected is not None and not stats["files_ok"]:
                raise SystemExit(
                    f"HARD ERROR: test262 expected {expected} files, "
                    f"saw {stats['files_seen']}"
                )
            return recs
        return _extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.js",
            extract_fn=lambda src, rel: extract_test262(
                src, repo=meta["repo"], file=rel
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
        # Prefer the unresolved path under ROOT so symlink materializations
        # (plugins/ → /tmp/…) keep stable repo-relative sites / regex_ids.
        try:
            rel = str(fp.relative_to(ROOT))
        except ValueError:
            try:
                rel = str(fp.resolve().relative_to(root_resolved))
            except ValueError:
                rel = str(fp)
        out.extend(
            extract_fn(fp.read_text(encoding="utf-8", errors="replace"), rel)
        )
    return out


def _compile_all(
    records: list[dict[str, Any]],
    *,
    lift_inline: bool,
    corpus_slug: str,
    budget: dict[str, Any] | None = None,
    wall_t0: float | None = None,
) -> list[dict[str, Any]]:
    budget = budget or {}
    _check_budget_patterns(records, budget, corpus_slug)
    max_wall = budget.get("max_wall_s")
    max_mem = budget.get("max_mem_mb")
    # wall_t0 may be set before extraction so max_wall_s covers extract+compile.
    t0 = wall_t0 if wall_t0 is not None else time.monotonic()
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
        # ModSecurity !@rx / selectors: never silent-positive (fix-wave #72).
        if rec.get("negated") and should_reject_negated(rec.get("dialect") or ""):
            out.append(
                {
                    **rec,
                    "encodable": False,
                    "compile_reason": NEGATED_UNSUPPORTED_REASON,
                    "unencodable_reason": NEGATED_UNSUPPORTED_REASON,
                    "corpus": corpus_slug,
                    "corpus_slug": corpus_slug,
                }
            )
            continue
        cr = compile_pattern(
            pattern,
            flags,
            rec["dialect"],
            rec["call_kind"],
            domain=rec.get("domain") or "ascii",
        )
        row = {
            **rec,
            "pattern": pattern,
            "flags": flags,
            "encodable": cr.encodable,
            "compile_reason": cr.unencodable_reason,
            "corpus": corpus_slug,
            "corpus_slug": corpus_slug,
        }
        # Surface compile timeouts for triage kind=timeout (fix-wave #71).
        if cr.unencodable_reason == "timeout":
            row["result"] = "timeout"
        out.append(row)

        if max_wall and (time.monotonic() - t0) > max_wall:
            raise BudgetBreached(corpus_slug, "max_wall_s", max_wall, time.monotonic() - t0)
        if max_mem:
            rss = _check_budget_mem()
            if rss > max_mem:
                raise BudgetBreached(corpus_slug, "max_mem_mb", max_mem, rss)

    return out


def run_corpus(
    corpus: str,
    *,
    out_dir: Path,
    with_redos: bool = False,
    approval_path: Path | None = None,
    require_ground_truth: bool = False,
    fail_planned: bool = False,
    redos_timeout_s: float | None = None,
    emit_planned: bool = True,
) -> dict[str, Any]:
    meta = CORPUS_MANIFESTS[corpus]
    if meta.get("corpus_type") == "inventory_only":
        from regexproof.extractors.rust_inventory import write_rust_inventory

        path: Path = meta["path"]
        out_dir.mkdir(parents=True, exist_ok=True)
        report = write_rust_inventory(path, out_dir / f"{corpus}_inventory_only.json")
        # Empty findings NDJSON so run_batch repro hashing still finds the file.
        write_ndjson(out_dir / f"{corpus}.ndjson", [])
        write_markdown(
            out_dir / f"{corpus}_batch.md",
            corpus=corpus,
            findings=[],
        )
        summary = {
            "corpus": corpus,
            "findings": 0,
            "encodable": report.get("extracted"),
            "decision": "inventory_only",
            "detail": report,
        }
        (out_dir / f"{corpus}_batch_summary.json").write_text(
            __import__("json").dumps(summary, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return summary
    meta = dict(meta)
    path: Path = meta["path"]
    sample_path = meta.get("sample_path") or ROOT / "batch" / "corpora" / corpus / "sample"
    if isinstance(sample_path, str):
        sample_path = Path(sample_path)
    path_usable = path.exists() and (path.is_file() or any(path.iterdir()))
    if not path_usable:
        if corpus in WAVE_CORPORA:
            # Match measure-corpus-fraction.py: sample fallback only when
            # measure_scope is explicitly "sample"; otherwise fail closed.
            if meta.get("measure_scope") == "sample" and isinstance(
                sample_path, Path
            ) and sample_path.exists():
                meta["path"] = sample_path
                print(
                    f"NOTE: {corpus} full corpus path missing ({path}); "
                    f"using sample at {sample_path}",
                    file=sys.stderr,
                )
            else:
                raise SystemExit(
                    f"HARD ERROR: {corpus} corpus path missing/empty ({path}) "
                    f"and measure_scope={meta.get('measure_scope')!r} "
                    f"(sample fallback only when measure_scope='sample')"
                )
        else:
            sample = ROOT / "batch" / "corpora" / corpus / "sample"
            if sample.is_dir():
                print(
                    f"NOTE: {corpus} corpus path missing/empty ({path}); "
                    f"falling back to sample at {sample}",
                    file=sys.stderr,
                )
                meta["path"] = sample
                meta["measure_scope"] = "sample"
    # Honor declared sample scope even when the full tree is present so batch
    # extraction stays aligned with measure-corpus-fraction.py.
    if meta.get("measure_scope") == "sample":
        sp = meta.get("sample_path")
        if isinstance(sp, str):
            sp = Path(sp)
        if not isinstance(sp, Path):
            sp = sample_path if isinstance(sample_path, Path) else None
        if isinstance(sp, Path) and sp.exists():
            cur = meta["path"]
            if "sample" not in Path(cur).parts:
                meta["path"] = sp
                print(
                    f"NOTE: {corpus} measure_scope=sample; using {sp}",
                    file=sys.stderr,
                )
        elif not isinstance(sp, Path) or not sp.exists():
            raise SystemExit(
                f"HARD ERROR: {corpus} measure_scope=sample but sample path "
                f"missing ({sp})"
            )
    _validate_expected_roots(corpus, meta)
    inventory = load_inventory(meta["corpus_type"])
    budget = meta.get("budget") or {}
    wall_t0 = time.monotonic()
    records = _extract(corpus, meta)
    if not records and corpus in WAVE_CORPORA:
        raise SystemExit(
            f"HARD ERROR: {corpus} extraction produced 0 records — "
            f"empty glob must not fake zero-pattern success"
        )
    try:
        compiled = _compile_all(
            records,
            lift_inline=bool(meta.get("lift_inline")),
            corpus_slug=corpus,
            budget=budget,
            wall_t0=wall_t0,
        )
    except BudgetBreached as exc:
        raise SystemExit(
            f"BUDGET BREACH ({corpus}): {exc.field} "
            f"limit={exc.limit} actual={exc.actual}"
        ) from exc

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

        budget_s = redos_timeout_s
        if budget_s is None:
            budget_s = (meta.get("budget") or {}).get("redos_wall_s", 120)
        t0 = time.monotonic()
        for rec in compiled:
            if not rec.get("encodable"):
                continue
            if budget_s is not None and (time.monotonic() - t0) >= float(budget_s):
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
            # Re-check after each record so a slow analyze_record still trips the gate.
            if budget_s is not None and (time.monotonic() - t0) >= float(budget_s):
                redos_incomplete = True
                break

    if redos_incomplete:
        findings.append(
            {
                "schema_version": "1",
                "regex_id": f"redos-incomplete:{corpus}",
                "kind": "redos",
                "corpus": corpus,
                "result": "incomplete",
                "site": f"redos-timeout:{redos_timeout_s or (meta.get('budget') or {}).get('redos_wall_s', 120)}",
                "pattern": "",
                "shape": None,
                "disclosure": "private_first" if meta.get("security_tool") else None,
                "detail": {
                    "error": "ReDoS fan-out truncated by wall-clock timeout gate",
                    "redos_timeout_s": redos_timeout_s
                    or (meta.get("budget") or {}).get("redos_wall_s", 120),
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
    write_ndjson(out_dir / f"{corpus}.ndjson", findings)
    # Keep Phase 3 shape-5 report at {corpus}.md; batch uses a distinct path.
    write_markdown(out_dir / f"{corpus}_batch.md", corpus=corpus, findings=findings)
    if redos_incomplete:
        raise SystemExit(
            f"evidence gate failed: ReDoS report incomplete "
            f"(timeout_s={redos_timeout_s or (meta.get('budget') or {}).get('redos_wall_s', 120)}); "
            "raise --redos-timeout-s / corpus budget.redos_wall_s for a complete run "
            f"(partial findings written to {out_dir / f'{corpus}.ndjson'})"
        )

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


def measure_coreruleset_sample(
    out_dir: Path, *, as_primary: bool = False
) -> dict[str, Any]:
    """PCRE encodable-fraction gate on pinned CRS sample; go iff >= 0.30.

    Always writes ``coreruleset_sample_encodable_fraction.json``. Only when
    ``as_primary`` (full ``rules/`` absent) may it also write the primary
    ``coreruleset_encodable_fraction.json`` — never overwrite a full-corpus
    primary with the sample report.
    """
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
    if as_primary:
        primary = out_dir / "coreruleset_encodable_fraction.json"
        # Never clobber a committed/full-corpus primary when rules/ is absent
        # (CI smoke without materializing CRS).
        keep_full = False
        if primary.is_file():
            try:
                prev = json.loads(primary.read_text(encoding="utf-8"))
                keep_full = prev.get("scope") == "full_corpus"
            except json.JSONDecodeError:
                keep_full = False
        if not keep_full:
            primary.write_text(payload, encoding="utf-8")
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

    compiled = _compile_all(
        records, lift_inline=True, corpus_slug="coreruleset",
        budget=CORPUS_MANIFESTS.get("coreruleset", {}).get("budget"),
    )
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
            measure_coreruleset_sample(out_dir, as_primary=False)
            return full
        # rules/ missing: keep returning a committed full-corpus primary if present.
        primary = out_dir / "coreruleset_encodable_fraction.json"
        if primary.is_file():
            try:
                prev = json.loads(primary.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                prev = {}
            if prev.get("scope") == "full_corpus":
                measure_coreruleset_sample(out_dir, as_primary=False)
                return prev
    return measure_coreruleset_sample(out_dir, as_primary=True)


def check_admission_gates(
    corpora: list[str],
    *,
    out_dir: Path,
) -> list[str]:
    """Return violation messages for missing/invalid corpus admission decisions.

    The corpus admission gate (sweep/corpus-admission-gate.md): every
    rule_corpus / validator corpus in CORPUS_MANIFESTS must have a
    ``<corpus>_gate_decision.json`` at ``out_dir`` (default
    ``properties/generated``), valid against ``gate_decision.schema.json``,
    with decision in ``go`` / ``triage-trial``. Testdata and inventory-only
    corpora are pipeline inputs, not scanned repos, so they are exempt.

    Missing or invalid artifacts hard-fail (never silent): a corpus with no
    admission record is not a corpus we are allowed to run.
    """
    from regexproof.schemas import load_schema

    schema = load_schema("gate_decision.schema.json")
    violations: list[str] = []
    for name in corpora:
        meta = CORPUS_MANIFESTS.get(name)
        if meta is None:
            violations.append(f"{name}: not in CORPUS_MANIFESTS")
            continue
        if meta.get("corpus_type") in ("testdata", "inventory_only"):
            continue
        path = out_dir / f"{name}_gate_decision.json"
        if not path.exists():
            violations.append(
                f"{name}: admission decision missing ({path.name}); "
                "run the admission probe and commit the decision artifact "
                "(sweep/corpus-admission-gate.md)"
            )
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            violations.append(f"{name}: admission decision unreadable: {exc}")
            continue
        try:
            jsonschema.validate(instance=data, schema=schema)
        except jsonschema.ValidationError as exc:
            violations.append(f"{name}: admission decision fails schema: {exc.message}")
            continue
        decision = data.get("decision")
        if decision not in ("go", "triage-trial"):
            violations.append(
                f"{name}: admission decision={decision!r}; "
                "go or triage-trial required (no-go corpora are not run)"
            )
    return violations


def run_batch(
    corpora: list[str],
    *,
    out_dir: Path | None = None,
    with_redos: bool = False,
    require_ground_truth: bool = False,
    fail_planned: bool = False,
    redos_timeout_s: float | None = None,
    emit_planned: bool = True,
) -> dict[str, Any]:
    cov = check_corpus_coverage()
    if cov:
        raise SystemExit("inventory coverage failed: " + "; ".join(cov))

    out_dir = out_dir or (ROOT / "properties" / "generated")
    admission = check_admission_gates(corpora, out_dir=out_dir)
    if admission:
        raise SystemExit("admission gate failed: " + "; ".join(admission))

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
            redos_timeout_s=redos_timeout_s,
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
        "--redos-timeout-s",
        type=float,
        default=None,
        help="wall-clock ReDoS fan-out budget in seconds (per corpus); "
        "truncation emits incomplete and fails the gate. "
        "Falls back to corpus budget.redos_wall_s when unset.",
    )
    ap.add_argument(
        "--redos-cap",
        type=int,
        default=None,
        help=argparse.SUPPRESS,  # removed: use --redos-timeout-s
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
    if args.redos_cap is not None:
        print(
            "error: --redos-cap was removed; use --redos-timeout-s (wall-clock gate)",
            file=sys.stderr,
        )
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
        redos_timeout_s=args.redos_timeout_s,
        emit_planned=not args.no_planned,
    )
    print("batch ok:", ", ".join(corpora))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
