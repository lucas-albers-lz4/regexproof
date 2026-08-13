"""Pattern → Z3 compilers (per dialect)."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

from regexproof.compiler.base import CompileResult, Unencodable
from regexproof.compiler.caret_in_x import try_compile_caret_in_x
from regexproof.compiler.py_re import compile_py_re
from regexproof.compiler.trailing_alt_dollar import try_compile_trailing_alt_dollar

def compiler_source_fingerprint() -> str:
    """Hash compiler sources, including comments, for cache invalidation."""
    base = Path(__file__).resolve().parent
    digest = hashlib.sha256()
    for source in sorted(base.glob("*.py")):
        contents = source.read_text(encoding="utf-8")
        if source.resolve() == Path(__file__).resolve():
            # The generated assignment cannot be part of its own digest.
            contents = re.sub(
                r"(?m)^COMPILER_VERSION\s*=.*$",
                "COMPILER_VERSION = <generated>",
                contents,
            )
        digest.update(str(source.name).encode("utf-8"))
        digest.update(b"\0")
        digest.update(contents.encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


# This is deliberately derived from source contents rather than a hand-edited
# label: a code or comment change in any compiler file changes the cache key.
COMPILER_VERSION = compiler_source_fingerprint()

__all__ = [
    "COMPILER_VERSION",
    "CompileResult",
    "Unencodable",
    "compile_pattern",
    "compile_py_re",
    "compiler_source_fingerprint",
]


def _compile_dialect(
    pattern: str,
    flags: str,
    dialect: str,
    call_kind: str,
    *,
    max_length: int,
    domain: str = "ascii",
) -> CompileResult:
    if dialect == "py_re":
        return compile_py_re(
            pattern, flags=flags, call_kind=call_kind, max_length=max_length
        )
    if dialect == "ecma":
        from regexproof.compiler.ecma import compile_ecma

        return compile_ecma(
            pattern, flags=flags, call_kind=call_kind, max_length=max_length
        )
    if dialect == "re2":
        from regexproof.compiler.re2 import compile_re2

        return compile_re2(
            pattern, flags=flags, call_kind=call_kind, max_length=max_length
        )
    if dialect == "pcre":
        from regexproof.compiler.pcre import compile_pcre

        return compile_pcre(
            pattern, flags=flags, call_kind=call_kind, max_length=max_length
        )
    if dialect == "posix-shell":
        # Entry-only normalize: compile_pattern normalized BEFORE the hooks;
        # this branch compiles the already-normalized text directly and
        # never re-normalizes (a re-normalize would round-trip BRE
        # `\+`→`+`→`\+` and cancel the fix).
        from regexproof.compiler.posix_shell import compile_posix_shell

        return compile_posix_shell(
            pattern,
            flags=flags,
            call_kind=call_kind,
            max_length=max_length,
            domain=domain,
        )
    if dialect == "yara":
        from regexproof.compiler.yara import compile_yara

        return compile_yara(
            pattern,
            flags=flags,
            call_kind=call_kind,
            max_length=max_length,
            domain=domain,
        )
    if dialect == "perl":
        from regexproof.compiler.perl import compile_perl

        return compile_perl(
            pattern, flags=flags, call_kind=call_kind, max_length=max_length
        )
    raise ValueError(f"unknown dialect {dialect!r}")


def compile_pattern(
    pattern: str,
    flags: str = "",
    dialect: str = "py_re",
    call_kind: str = "search",
    *,
    max_length: int = 256,
    domain: str = "ascii",
    shell_flags: dict | None = None,
    cache: Any | None = None,
    cache_dir: str | None = None,
    cache_stats: dict[str, int] | None = None,
):
    """Dispatch to a dialect compiler. Never use z3.Re(pattern_string).

    ``shell_flags`` (posix-shell only): the record's syntax selector
    (``{"syntax": "bre"|"ere"|"bash_ksh", ...}``); missing/unknown selectors
    default to BRE.  The BRE→ERE normalize runs HERE — at entry, inside the
    try/except (so a rejection returns a rejected ``CompileResult`` instead
    of propagating and aborting batch), before the caret_in_x /
    trailing_alt_dollar hooks, which then see normalized ERE text — and is
    never re-run inside the dialect branch.
    """
    import z3

    cache_key = None
    if cache is None and cache_dir is not None:
        from regexproof.compiler.cache import MirrorCache

        cache = MirrorCache(cache_dir)

    def compile_bare(pat: str, fl: str, dia: str, ck: str) -> CompileResult:
        return _compile_dialect(
            pat, fl, dia, ck, max_length=max_length, domain=domain
        )

    try:
        if dialect == "posix-shell":
            from regexproof.compiler.posix_shell import normalize_shell

            sf = shell_flags or {}
            pattern = normalize_shell(pattern, sf.get("syntax", "bre"))

        if cache is not None:
            from regexproof.compiler.cache import mirror_cache_key

            cache_key = mirror_cache_key(
                pattern,
                flags,
                dialect,
                call_kind,
                domain,
                shell_flags,
                COMPILER_VERSION,
                z3.get_version_string(),
                max_length,
            )
            artifact = cache.get(cache_key)
            if artifact is not None:
                if cache_stats is not None:
                    cache_stats["hits"] = cache_stats.get("hits", 0) + 1
                return CompileResult(
                    mirror=artifact.mirror,
                    unencodable_reason=None,
                    dialect=dialect,
                    call_kind=call_kind,
                    flags=str(artifact.metadata.get("_normalized_flags", flags)),
                    pattern=pattern,
                    declared_domain=str(
                        artifact.metadata.get("_declared_domain", domain)
                    ),
                    meta=artifact.metadata,
                )
            if cache_stats is not None:
                cache_stats["misses"] = cache_stats.get("misses", 0) + 1

        def finish(result: CompileResult) -> CompileResult:
            if cache is not None and cache_key is not None and result.encodable:
                try:
                    # Re-gate 4: store the NORMALIZED flags + derived domain so
                    # a cache hit returns the same CompileResult metadata as a
                    # fresh compile (the hit path reads them back below).
                    meta = dict(result.meta or {})
                    meta["_normalized_flags"] = result.flags
                    meta["_declared_domain"] = result.declared_domain
                    cache.put(cache_key, result.mirror, meta)
                except (OSError, TypeError, ValueError):
                    # Caching is an optimization; a full or unavailable cache
                    # must not change the compiler's fail-closed result.
                    pass
            return result

        # Caret-in-X is more specific than A1B; try it first (#103).
        caret = try_compile_caret_in_x(
            pattern,
            flags,
            dialect,
            call_kind,
            max_length=max_length,
            compile_bare=compile_bare,
        )
        if caret is not None:
            return finish(caret)
        special = try_compile_trailing_alt_dollar(
            pattern,
            flags,
            dialect,
            call_kind,
            max_length=max_length,
            compile_bare=compile_bare,
        )
        if special is not None:
            return finish(special)
        return finish(
            _compile_dialect(
                pattern,
                flags,
                dialect,
                call_kind,
                max_length=max_length,
                domain=domain,
            )
        )
    except Unencodable as exc:
        return CompileResult(
            mirror=None,
            unencodable_reason=exc.reason,
            dialect=dialect,
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain=domain,
        )
    except z3.Z3Exception:
        # REJECT-never-crash: Z3 Loop/bounds bugs must triage, not abort batch.
        return CompileResult(
            mirror=None,
            unencodable_reason="z3-exception",
            dialect=dialect,
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain=domain,
        )
    except (OverflowError, MemoryError, RecursionError):
        # Huge quantifiers / nested reps in testdata must not abort measure.
        return CompileResult(
            mirror=None,
            unencodable_reason="pattern-too-large",
            dialect=dialect,
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain=domain,
        )
    except ValueError as exc:
        # subprocess argv cannot embed NUL (perl helper / similar).
        msg = str(exc).lower()
        reason = "embedded-nul" if "null" in msg else "value-error"
        return CompileResult(
            mirror=None,
            unencodable_reason=reason,
            dialect=dialect,
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain=domain,
        )
