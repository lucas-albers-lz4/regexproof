"""Public corpus extraction API (#193)."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from regexproof.admission.walk import _SHELL_SHEBANGS, _SKIP_DIR_NAMES
from regexproof.batch.extractor_registry import (
    EXTRACTORS,
    registry_glob,
)
from regexproof.batch.manifests import MAX_FILE_BYTES, ROOT, WAVE_CORPORA
from regexproof.extractors.cpython_re_tests import (
    extract_cpython_combined,
    extract_cpython_re_tests,
)
from regexproof.extractors.go_regexp_tests import (
    extract_go_regexp_tests,
    extract_go_regexp_tests_tree,
)
from regexproof.extractors.js_babel import extract_js, extract_js_precise
from regexproof.extractors.modsec import extract_modsec
from regexproof.extractors.perl_re_tests import (
    extract_perl_re_file,
    extract_perl_re_tree,
)
from regexproof.extractors.python_ast import extract_python
from regexproof.extractors.re2_testdata import extract_re2_testdata
from regexproof.extractors.rule_file import extract_rule_file
from regexproof.extractors.v8_mjsunit import (
    extract_v8_mjsunit,
    extract_v8_mjsunit_tree,
)


def _read_capped(path: Path, meta: dict[str, Any] | None = None) -> str | None:
    """Read *path* if it is within ``MAX_FILE_BYTES``; else skip (#365 / #175).

    Oversized → ``None`` (and optional ``meta["skipped_oversized"]`` bump).
    Missing/unreadable paths raise ``OSError`` — do not conflate with skip.
    """
    size = path.stat().st_size
    if size > MAX_FILE_BYTES:
        if meta is not None:
            meta["skipped_oversized"] = int(meta.get("skipped_oversized") or 0) + 1
        print(
            f"warning: skipped oversized file {path} (>{MAX_FILE_BYTES} bytes)",
            file=sys.stderr,
        )
        return None
    return path.read_text(encoding="utf-8", errors="replace")


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
    # re2_testdata is in EXTRACTORS but stays file-or-dir below; do not
    # dispatch `if extractor in EXTRACTORS` blindly.
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
        "semgrep_yaml",
    }:
        fn = EXTRACTORS[extractor]
        if extractor == "shell_posix":
            # the admission walker counts extensionless files with a
            # recognized shell shebang — batch must match (luna #276 -r7
            # finding #3): enumerate everything, admit by filter
            return extract_glob(
                path,
                meta,
                glob="**/*",
                file_filter=_is_shell_script,
                extract_fn=lambda src, rel: fn(src, rel, meta),
            )
        return extract_glob(
            path,
            meta,
            glob=registry_glob(extractor, meta),
            extract_fn=lambda src, rel: fn(src, rel, meta),
        )
    if meta["extractor"] == "rule_file":
        source = _read_capped(path, meta)
        if source is None:
            return []
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
            text = _read_capped(fp, meta)
            if text is None:
                continue
            out.extend(
                extract_modsec(
                    text,
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
            text = _read_capped(fp, meta)
            if text is None:
                continue
            out.extend(extract_js(text, repo=meta["repo"], file=rel))
        return out
    if meta["extractor"] == "js_precise_dir":
        # Wave ecma path: Babel/comment-aware extract_js_precise (not legacy extract_js).
        out: list[dict[str, Any]] = []
        for name in meta.get("files") or sorted(p.name for p in path.glob("*.js")):
            fp = path / name
            if not fp.is_file():
                raise SystemExit(f"HARD ERROR: missing js_precise_dir file: {fp}")
            rel = str(fp.relative_to(ROOT))
            text = _read_capped(fp, meta)
            if text is None:
                continue
            out.extend(
                extract_js_precise(
                    text,
                    repo=meta["repo"],
                    file=rel,
                )
            )
        return out
    if meta["extractor"] == "js":
        source = _read_capped(path, meta)
        if source is None:
            return []
        rel = str(path.relative_to(ROOT))
        return extract_js(source, repo=meta["repo"], file=rel)
    if meta["extractor"] == "python":
        source = _read_capped(path, meta)
        if source is None:
            return []
        rel = str(path.relative_to(ROOT))
        return extract_python(source, repo=meta["repo"], file=rel)
    if meta["extractor"] == "re2_testdata":
        if path.is_file():
            source = _read_capped(path, meta)
            if source is None:
                return []
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
    if meta["extractor"] == "cpython_re_tests":
        if path.is_dir():
            sources: dict[str, str] = {}
            for fp in sorted(path.glob(meta.get("glob") or "*.py")):
                if fp.is_file():
                    try:
                        rel = str(fp.resolve().relative_to(ROOT.resolve()))
                    except ValueError:
                        rel = str(fp)
                    text = _read_capped(fp, meta)
                    if text is None:
                        continue
                    sources[fp.name] = text
            if sources:
                try:
                    base = str(path.resolve().relative_to(ROOT.resolve()))
                except ValueError:
                    base = str(path)
                return extract_cpython_combined(
                    sources, repo=meta["repo"], base_path=base,
                )
        if path.is_file():
            source = _read_capped(path, meta)
            if source is None:
                return []
            try:
                rel = str(path.resolve().relative_to(ROOT.resolve()))
            except ValueError:
                rel = str(path)
            return extract_cpython_re_tests(
                source, repo=meta["repo"], file=rel, dialect=meta["dialect"]
            )
        return []
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
            if stats.get("skipped_oversized"):
                meta["skipped_oversized"] = int(meta.get("skipped_oversized") or 0) + int(
                    stats["skipped_oversized"]
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
            if stats.get("skipped_oversized"):
                meta["skipped_oversized"] = int(meta.get("skipped_oversized") or 0) + int(
                    stats["skipped_oversized"]
                )
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
            if stats.get("skipped_oversized"):
                meta["skipped_oversized"] = int(meta.get("skipped_oversized") or 0) + int(
                    stats["skipped_oversized"]
                )
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
            if stats.get("skipped_oversized"):
                meta["skipped_oversized"] = int(meta.get("skipped_oversized") or 0) + int(
                    stats["skipped_oversized"]
                )
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


def _is_shell_script(fp: Path) -> bool:
    """shell_posix batch file filter — aligned with dogfood ``--dir``
    ``_classify`` (scripts/dogfood-singleton-analysis.py): known suffix,
    ``init.d/`` path segment, or first line in the walker's exact shebang
    allowlist **regardless of suffix**.

    Luna #276: the allowlist is exact ``_SHELL_SHEBANGS`` (never a ``sh``
    substring), so ``#!/usr/bin/zsh`` stays rejected. Suffix-early-return
    previously dropped OpenWrt ``.defaults`` / ``.uci`` / ``.dnsprefetch``
    shebang files that ``--dir`` admits.

    Path segments in the admission walker's ``_SKIP_DIR_NAMES`` (``.git``,
    ``node_modules``, …) are refused so ``**/*`` does not admit clone-hook
    sample scripts under ``.git/hooks/``.
    """
    if any(p in _SKIP_DIR_NAMES for p in fp.parts):
        return False
    if fp.suffix in (".sh", ".bash", ".init"):
        return True
    if any(p == "init.d" for p in fp.parts):
        return True
    try:
        with fp.open("r", encoding="utf-8", errors="replace") as fh:
            first = fh.readline(80).strip()
    except OSError:
        return False
    return first in _SHELL_SHEBANGS


def extract_glob(
    path: Path,
    meta: dict[str, Any],
    *,
    glob: str,
    extract_fn,
    file_filter=None,
) -> list[dict[str, Any]]:
    """Deterministic directory walk: sorted paths, fixed order.

    ``glob`` may be a single pattern or a comma-separated list (brace-free),
    e.g. ``**/*.yml,**/*.yaml``.  ``file_filter`` (optional callable
    Path→bool) further prunes matched files — used by shell_posix to admit
    extensionless files with a recognized shell shebang (the admission
    walker includes them; batch must match — luna #276 -r7 finding #3).

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
        if file_filter is not None and not file_filter(fp):
            continue
        seen.add(fp)
        try:
            if fp.stat().st_size > MAX_FILE_BYTES:
                skipped_oversized += 1
                continue
        except OSError:
            # Glob discovery: match admission walker (#175) — skip
            # transient/unreadable matches. Named-file paths already
            # fail-closed above via the missing-file gate; single-file
            # extractors use `_read_capped`, which re-raises OSError.
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


