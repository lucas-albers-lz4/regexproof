"""Extractor name → callable registry (#195).

Partial migration: glob-style extractors dispatch through this map; complex
tree walkers remain inline in ``extract_corpus`` so regex_ids stay frozen.
``re2_testdata`` is registered for reuse but ``extract_corpus`` keeps
file-or-dir dispatch (not the glob-only whitelist).
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from regexproof.extractors.busybox_tests import extract_busybox_tests
from regexproof.extractors.dompurify import extract_dompurify
from regexproof.extractors.email_addresses import extract_email_addresses
from regexproof.extractors.go_regexp import extract_go_regexp
from regexproof.extractors.ids_rules import extract_ids_rules
from regexproof.extractors.isemail import extract_isemail
from regexproof.extractors.noseyparker import extract_noseyparker
from regexproof.extractors.pcre2_testdata import extract_pcre2_testdata
from regexproof.extractors.python_ast import extract_python
from regexproof.extractors.re2_testdata import extract_re2_testdata
from regexproof.extractors.semgrep_yaml import extract_semgrep_yaml
from regexproof.extractors.shell_posix import extract_shell_posix
from regexproof.extractors.shhgit import extract_shhgit
from regexproof.extractors.spamassassin import extract_spamassassin
from regexproof.extractors.yara import extract_yara

# (src, rel, meta) -> list[record]
ExtractorFn = Callable[[str, str, dict[str, Any]], list[dict[str, Any]]]

# Glob defaults for registry extractors (comma-separated patterns OK).
EXTRACTOR_GLOBS: dict[str, str] = {
    "python_dir": "**/*.py",
    "go_regexp": "**/*.go",
    "ids_rules": "*.rules",
    "re2_testdata": "*.txt",
    "pcre2_testdata": "testinput*",
    "busybox_tests": "*.tests",
    "yara": "**/*.yar,**/*.yara",
    "spamassassin": "**/*.cf",
    "noseyparker": "**/*.yml",
    "shhgit": "config.yaml",
    "shell_posix": "**/*.sh,**/*.bash,**/*.init,**/init.d/**",
    "dompurify": "src/*.ts",
    "isemail": "*.js",
    "email_addresses": "*.js",
    "semgrep_yaml": "**/*.yml,**/*.yaml",
}


def _with_dialect(fn, *, dialect_kw: bool = True) -> ExtractorFn:
    def _call(src: str, rel: str, meta: dict[str, Any]) -> list[dict[str, Any]]:
        kwargs: dict[str, Any] = {"repo": meta["repo"], "file": rel}
        if dialect_kw:
            kwargs["dialect"] = meta["dialect"]
        return fn(src, **kwargs)

    return _call


EXTRACTORS: dict[str, ExtractorFn] = {
    "python_dir": _with_dialect(extract_python, dialect_kw=False),
    "go_regexp": _with_dialect(extract_go_regexp),
    "ids_rules": _with_dialect(extract_ids_rules),
    "re2_testdata": _with_dialect(extract_re2_testdata),
    "pcre2_testdata": _with_dialect(extract_pcre2_testdata),
    "busybox_tests": _with_dialect(extract_busybox_tests),
    "yara": _with_dialect(extract_yara, dialect_kw=False),
    "spamassassin": _with_dialect(extract_spamassassin, dialect_kw=False),
    "noseyparker": _with_dialect(extract_noseyparker),
    "shhgit": _with_dialect(extract_shhgit),
    "shell_posix": _with_dialect(extract_shell_posix),
    "dompurify": _with_dialect(extract_dompurify, dialect_kw=False),
    "isemail": _with_dialect(extract_isemail, dialect_kw=False),
    "email_addresses": _with_dialect(extract_email_addresses, dialect_kw=False),
    "semgrep_yaml": _with_dialect(extract_semgrep_yaml),
}


def registry_glob(name: str, meta: dict[str, Any]) -> str:
    return meta.get("glob") or EXTRACTOR_GLOBS[name]
