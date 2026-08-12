"""Public corpus extraction API (#193)."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from regexproof.batch.extractor_registry import (
    EXTRACTORS,
    registry_glob,
)
from regexproof.batch.manifests import MAX_FILE_BYTES, ROOT, WAVE_CORPORA
from regexproof.extractors.busybox_tests import extract_busybox_tests
from regexproof.extractors.cpython_re_tests import (
    extract_cpython_combined,
    extract_cpython_re_tests,
)
from regexproof.extractors.re2_testdata import extract_re2_testdata
from regexproof.extractors.go_regexp import extract_go_regexp
from regexproof.extractors.go_regexp_tests import (
    extract_go_regexp_tests,
    extract_go_regexp_tests_tree,
)
from regexproof.extractors.ids_rules import extract_ids_rules
from regexproof.extractors.js_babel import extract_js, extract_js_precise
from regexproof.extractors.modsec import extract_modsec
from regexproof.extractors.pcre2_testdata import extract_pcre2_testdata
from regexproof.extractors.perl_re_tests import (
    extract_perl_re_file,
    extract_perl_re_tree,
)
from regexproof.extractors.python_ast import extract_python
from regexproof.extractors.rule_file import extract_rule_file
from regexproof.extractors.dompurify import extract_dompurify
from regexproof.extractors.email_addresses import extract_email_addresses
from regexproof.extractors.isemail import extract_isemail
from regexproof.extractors.noseyparker import extract_noseyparker
from regexproof.extractors.shhgit import extract_shhgit
from regexproof.extractors.spamassassin import extract_spamassassin
from regexproof.extractors.v8_mjsunit import (
    extract_v8_mjsunit,
    extract_v8_mjsunit_tree,
)
from regexproof.extractors.yara import extract_yara

def validate_expected_roots(corpus: str, meta: dict[str, Any]) -> None:
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


def extract_corpus(corpus: str, meta: dict[str, Any]) -> list[dict[str, Any]]:
    path: Path = meta["path"]
    extractor = meta["extractor"]
    # Registry path for pure glob extractors (#195) — preserves regex_ids.
    if extractor in EXTRACTORS and extractor in {
        "python_dir",
        "go_regexp",
        "ids_rules",
        "pcre2_testdata",
        "busybox_tests",
        "yara",
        "spamassassin",
        "noseyparker",
        "shhgit",
        "shell_posix",
        "dompurify",
        "isemail",
        "email_addresses",
    }:
        fn = EXTRACTORS[extractor]
        return extract_glob(
            path,
            meta,
            glob=registry_glob(extractor, meta),
            extract_fn=lambda src, rel: fn(src, rel, meta),
        )
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
    if meta["extractor"] == "js_precise_dir":
        # Wave ecma path: Babel/comment-aware extract_js_precise (not legacy extract_js).
        out: list[dict[str, Any]] = []
        for name in meta.get("files") or sorted(p.name for p in path.glob("*.js")):
            fp = path / name
            if not fp.is_file():
                raise SystemExit(f"HARD ERROR: missing js_precise_dir file: {fp}")
            rel = str(fp.relative_to(ROOT))
            out.extend(
                extract_js_precise(
                    fp.read_text(encoding="utf-8", errors="replace"),
                    repo=meta["repo"],
                    file=rel,
                )
            )
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
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.py",
            extract_fn=lambda src, rel: extract_python(
                src, repo=meta["repo"], file=rel
            ),
        )
    if meta["extractor"] == "go_regexp":
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.go",
            extract_fn=lambda src, rel: extract_go_regexp(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "ids_rules":
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "*.rules",
            extract_fn=lambda src, rel: extract_ids_rules(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "semgrep_yaml":
        from regexproof.extractors.semgrep_yaml import extract_semgrep_yaml

        return extract_glob(
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
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "*.txt",
            extract_fn=lambda src, rel: extract_re2_testdata(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "pcre2_testdata":
        return extract_glob(
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
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "*.tests",
            extract_fn=lambda src, rel: extract_busybox_tests(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "yara":
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.yar,**/*.yara",
            extract_fn=lambda src, rel: extract_yara(
                src, repo=meta["repo"], file=rel
            ),
        )
    if meta["extractor"] == "spamassassin":
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.cf",
            extract_fn=lambda src, rel: extract_spamassassin(
                src, repo=meta["repo"], file=rel
            ),
        )
    if meta["extractor"] == "noseyparker":
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.yml",
            extract_fn=lambda src, rel: extract_noseyparker(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "shhgit":
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "config.yaml",
            extract_fn=lambda src, rel: extract_shhgit(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "dompurify":
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "src/*.ts",
            extract_fn=lambda src, rel: extract_dompurify(
                src, repo=meta["repo"], file=rel
            ),
        )
    if meta["extractor"] == "isemail":
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "*.js",
            extract_fn=lambda src, rel: extract_isemail(
                src, repo=meta["repo"], file=rel
            ),
        )
    if meta["extractor"] == "email_addresses":
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "*.js",
            extract_fn=lambda src, rel: extract_email_addresses(
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
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*.js",
            extract_fn=lambda src, rel: extract_test262(
                src, repo=meta["repo"], file=rel
            ),
        )
    if meta["extractor"] == "perl_re_tests":
        if not path.exists():
            raise FileNotFoundError(f"perl_tre root missing: {path}")
        if path.is_dir() and meta.get("measure_scope") != "sample":
            expected = meta.get("expected_files")
            recs, stats = extract_perl_re_tree(
                path,
                repo=meta["repo"],
                expected_files=expected,
                dialect=meta["dialect"],
            )
            meta["_extract_stats"] = stats
            if expected is not None and not stats["files_ok"]:
                raise SystemExit(
                    f"HARD ERROR: perl_tre expected {expected} files, "
                    f"saw {stats['files_seen']}"
                )
            return recs
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "*.t,re_tests",
            extract_fn=lambda src, rel: extract_perl_re_file(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "go_regexp_tests":
        if not path.exists():
            raise FileNotFoundError(f"go_regexp_tests root missing: {path}")
        if path.is_dir() and meta.get("measure_scope") != "sample":
            expected = meta.get("expected_files")
            recs, stats = extract_go_regexp_tests_tree(
                path,
                repo=meta["repo"],
                expected_files=expected,
                dialect=meta["dialect"],
            )
            meta["_extract_stats"] = stats
            if expected is not None and not stats["files_ok"]:
                raise SystemExit(
                    f"HARD ERROR: go_regexp_tests expected {expected} files, "
                    f"saw {stats['files_seen']}"
                )
            return recs
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/*_test.go",
            extract_fn=lambda src, rel: extract_go_regexp_tests(
                src, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            ),
        )
    if meta["extractor"] == "v8_mjsunit":
        if not path.exists():
            raise FileNotFoundError(f"v8_mjsunit root missing: {path}")
        if path.is_dir() and meta.get("measure_scope") != "sample":
            expected = meta.get("expected_files")
            recs, stats = extract_v8_mjsunit_tree(
                path,
                repo=meta["repo"],
                expected_files=expected,
            )
            meta["_extract_stats"] = stats
            if expected is not None and not stats["files_ok"]:
                raise SystemExit(
                    f"HARD ERROR: v8_mjsunit expected {expected} files, "
                    f"saw {stats['files_seen']}"
                )
            return recs
        return extract_glob(
            path,
            meta,
            glob=meta.get("glob") or "**/regexp*.js",
            extract_fn=lambda src, rel: extract_v8_mjsunit(
                src, repo=meta["repo"], file=rel
            ),
        )
    raise ValueError(meta["extractor"])


def extract_glob(
    path: Path,
    meta: dict[str, Any],
    *,
    glob: str,
    extract_fn,
) -> list[dict[str, Any]]:
    """Deterministic directory walk: sorted paths, fixed order.

    ``glob`` may be a single pattern or a comma-separated list (brace-free),
    e.g. ``**/*.yml,**/*.yaml``.

    Files larger than ``MAX_FILE_BYTES`` are skipped (counted on
    ``meta["skipped_oversized"]``). Symlinks are followed — detect-secrets
    and similar corpora materialize plugins via symlink (#175).
    """
    out: list[dict[str, Any]] = []
    root_resolved = ROOT.resolve()
    skipped_oversized = 0
    if not path.is_dir():
        meta["skipped_oversized"] = 0
        return out
    files: list[Path] = []
    named = meta.get("files")
    if named:
        # Explicit file list (single-file corpora e.g. shhgit config.yaml).
        # Fail closed: a partial rules/ tree must not silently under-count.
        missing = [name for name in named if not (path / name).is_file()]
        if missing:
            raise FileNotFoundError(
                f"{meta.get('repo', path)}: manifest files missing under {path}: "
                + ", ".join(missing)
            )
        for name in named:
            files.append(path / name)
    else:
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
            if fp.stat().st_size > MAX_FILE_BYTES:
                skipped_oversized += 1
                continue
        except OSError:
            continue
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
    meta["skipped_oversized"] = skipped_oversized
    if skipped_oversized:
        print(
            f"warning: skipped {skipped_oversized} oversized file(s) "
            f"(>{MAX_FILE_BYTES} bytes) under {path}",
            file=sys.stderr,
        )
    return out


