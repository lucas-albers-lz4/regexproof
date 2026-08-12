"""Multi-extractor probe walk over a local repo tree (P1 A4)."""

from __future__ import annotations

import os
import re
from collections import Counter
from pathlib import Path
from typing import Any, Callable

from regexproof.admission.constructs import accumulate_constructs
from regexproof.admission.dialect_aliases import normalize_dialect_counts
from regexproof.admission.vocabulary import predict_buckets
from regexproof.extractors.go_regexp import extract_go_regexp
from regexproof.extractors.ids_rules import extract_ids_rules
from regexproof.extractors.js_babel import extract_js_precise
from regexproof.extractors.modsec import extract_modsec
from regexproof.extractors.python_ast import extract_python
from regexproof.extractors.rule_file import extract_rule_file
from regexproof.extractors.shell_posix import extract_shell_posix
from regexproof.extractors.spamassassin import extract_spamassassin
from regexproof.extractors.test262 import extract_test262
from regexproof.extractors.yara import extract_yara

_SKIP_DIR_NAMES = frozenset(
    {".git", "node_modules", "vendor", ".venv", "venv", "dist", "build", "__pycache__"}
)
_MAX_FILE_BYTES = 2_000_000

_JAVA_PATTERN_COMPILE = re.compile(
    r"Pattern\s*\.\s*compile\s*\(\s*\"((?:\\.|[^\"\\])*)\"",
    re.MULTILINE,
)

# Extractor flag letters → construct keys for predict_buckets.
_FLAG_LETTER_TO_CONSTRUCT = {
    "i": "(?i)",
    "x": "(?x)",
    "s": "(?s)",
    "m": "(?m)",
    "u": "u-flag",
    "v": "v-flag",
    "g": "stateful",
}

ExtractFn = Callable[[str, str], list[dict[str, Any]]]


def _iter_files(root: Path) -> list[Path]:
    """List candidate files under *root*, pruning skip-dir names in-place.

    Same membership as the prior ``rglob`` + post-filter path: skip
    ``_SKIP_DIR_NAMES`` subtrees, symlinks (``is_file()`` follows links), and
    files larger than ``_MAX_FILE_BYTES``. Result is sorted for stable walk order.
    """
    files: list[Path] = []
    root_s = str(root)
    for dirpath, dirnames, filenames in os.walk(root_s, topdown=True, followlinks=False):
        dirnames[:] = sorted(d for d in dirnames if d not in _SKIP_DIR_NAMES)
        for name in filenames:
            p = Path(dirpath) / name
            # Skip symlinks before is_file() — is_file() follows links.
            if p.is_symlink():
                continue
            if not p.is_file():
                continue
            try:
                if p.stat().st_size > _MAX_FILE_BYTES:
                    continue
            except OSError:
                continue
            files.append(p)
    return sorted(files)


def _rel(root: Path, path: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def _extractors_for(path: Path) -> list[ExtractFn]:
    """Return extractors to try for *path* (first non-empty wins for conf)."""
    name = path.name.lower()
    suffix = path.suffix.lower()
    path_s = str(path).lower()

    if suffix == ".java":
        return []  # handled by count-only path
    if suffix in _SHELL_SUFFIXES:
        return [_shell_extractor]
    if suffix in {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"}:
        if "test262" in path_s:
            return [lambda src, rel: extract_test262(src, repo="probe", file=rel)]
        return [lambda src, rel: extract_js_precise(src, repo="probe", file=rel)]
    if suffix == ".py":
        return [lambda src, rel: extract_python(src, repo="probe", file=rel)]
    if suffix == ".go":
        return [
            lambda src, rel: extract_go_regexp(
                src, repo="probe", file=rel, dialect="re2"
            )
        ]
    if suffix in {".yml", ".yaml", ".toml"}:
        return [
            lambda src, rel: extract_rule_file(
                src, repo="probe", file=rel, dialect="rust-regex"
            )
        ]
    if suffix in {".yar", ".yara"}:
        return [lambda src, rel: extract_yara(src, repo="probe", file=rel)]
    if suffix in {".rules", ".rule"}:
        return [
            lambda src, rel: extract_ids_rules(
                src, repo="probe", file=rel, dialect="pcre"
            )
        ]
    if suffix in {".conf", ".cf"} or name.endswith(".conf"):
        return [
            lambda src, rel: extract_modsec(src, repo="probe", file=rel),
            lambda src, rel: extract_spamassassin(src, repo="probe", file=rel),
        ]
    # init.d/ + shebang files come LAST — suffix extractors (py/js/conf…)
    # take precedence, matching the P1 `--dir` counter's selection order.
    if _is_shell_context(path):
        return [_shell_extractor]
    return []


def _should_read(path: Path) -> bool:
    """True when *path* has a java count path or at least one extractor."""
    if path.suffix.lower() == ".java":
        return True
    return bool(_extractors_for(path))


_SHELL_SUFFIXES = frozenset({".sh", ".bash", ".init"})
_SHELL_SHEBANGS = frozenset({
    "#!/bin/sh", "#!/bin/bash",
    "#!/usr/bin/env sh", "#!/usr/bin/env bash",
})


def _is_shell_context(path: Path) -> bool:
    """init.d/ path segment or extensionless file with a shell shebang
    (matches the P1 `--dir` counter's selection; suffix files are handled
    by their suffix extractor first)."""
    if any(p == "init.d" for p in path.parts):
        return True
    if path.suffix == "":
        try:
            with path.open("r", encoding="utf-8", errors="replace") as fh:
                first = fh.readline(80).strip()
        except OSError:
            return False
        return first in _SHELL_SHEBANGS
    return False


def _shell_extractor(src: str, rel: str) -> list[dict]:
    """Probe-path shell extractor (repo='probe', dialect posix-shell)."""
    return extract_shell_posix(src, repo="probe", file=rel, dialect="posix-shell")


def count_java_pattern_compile(source: str) -> list[str]:
    """Return Java Pattern.compile string literals (count-only path)."""
    return [m.group(1) for m in _JAVA_PATTERN_COMPILE.finditer(source)]


def walk_repo(root: Path | str, *, repo_name: str = "probe") -> dict[str, Any]:
    """Walk *root* and aggregate probe facts (sites, dialects, flags, constructs)."""
    root_p = Path(root).resolve()
    dialect_counts: Counter[str] = Counter()
    flag_counts: Counter[str] = Counter()
    patterns: list[str] = []
    per_file: dict[str, int] = {}
    extractor_errors = 0

    for fp in _iter_files(root_p):
        if not _should_read(fp):
            continue
        rel = _rel(root_p, fp)
        try:
            text = fp.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        file_sites = 0

        if fp.suffix.lower() == ".java":
            java_pats = count_java_pattern_compile(text)
            if java_pats:
                dialect_counts["java"] += len(java_pats)
                file_sites += len(java_pats)
                patterns.extend(java_pats)
        else:
            for extract_fn in _extractors_for(fp):
                try:
                    recs = extract_fn(text, rel)
                except Exception:
                    extractor_errors += 1
                    continue
                if not recs:
                    continue
                for rec in recs:
                    dial = str(rec.get("dialect") or "unknown")
                    dialect_counts[dial] += 1
                    file_sites += 1
                    flags = rec.get("flags") or ""
                    for ch in flags:
                        flag_counts[ch] += 1
                    pat = rec.get("pattern") or ""
                    if pat:
                        patterns.append(pat)
                break  # first successful extractor for this file

        if file_sites:
            per_file[rel] = file_sites

    constructs = accumulate_constructs(patterns)
    # Fold extractor flag letters into construct keys so /pat/i → (?i) bucket.
    merged = Counter(constructs)
    for ch, n in flag_counts.items():
        key = _FLAG_LETTER_TO_CONSTRUCT.get(ch)
        if key:
            merged[key] += n
    return {
        "regex_sites": int(sum(dialect_counts.values())),
        "regex_sites_per_file": dict(sorted(per_file.items())),
        "dialect": normalize_dialect_counts(dict(dialect_counts)),
        "flags": dict(sorted(flag_counts.items())),
        "construct_counts": constructs,
        "predicted_buckets": predict_buckets(dict(merged)),
        "repo_name": repo_name,
        "extractor_errors": extractor_errors,
    }
