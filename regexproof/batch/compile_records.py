"""Public compile_records API — pattern → encodable rows (#193)."""

from __future__ import annotations

import time
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing
import os
from pathlib import Path
from typing import Any

from regexproof.batch.budgets import (
    BudgetBreached,
    apply_address_space_cap,
    check_budget_mem,
    check_budget_patterns,
)
from regexproof.batch.negation_policy import (
    NEGATED_UNSUPPORTED_REASON,
    should_reject_negated,
)
from regexproof.compiler import compile_pattern
from regexproof.compiler.cache import (
    DEFAULT_CACHE_DIR,
    MirrorCache,
    deserialize_mirror,
    serialize_mirror,
)
from regexproof.compiler.normalize import normalize_inline_flags

DEFAULT_WORKER_COUNT = min(os.cpu_count() or 1, 8)


def _resolved_jobs(jobs: int | None) -> int:
    if jobs is None:
        return DEFAULT_WORKER_COUNT
    if jobs < 1:
        raise ValueError("jobs must be at least 1")
    return min(int(jobs), 8)


def _compile_one_record(
    rec: dict[str, Any],
    *,
    lift_inline: bool,
    corpus_slug: str,
    budget: dict[str, Any],
    cache: MirrorCache,
) -> tuple[dict[str, Any], str | None, dict[str, Any] | None, bool]:
    """Compile one record and return only spawn-safe values."""
    pattern = rec["pattern"]
    flags = rec.get("flags") or ""
    if lift_inline:
        pattern, flags = normalize_inline_flags(pattern, flags)
    if rec.get("unencodable_reason"):
        return (
            {
                **rec,
                "encodable": False,
                "compile_reason": rec["unencodable_reason"],
                "corpus": corpus_slug,
                "corpus_slug": corpus_slug,
            },
            None,
            None,
            False,
        )
    # ModSecurity !@rx / selectors: never silent-positive (fix-wave #72).
    if rec.get("negated") and should_reject_negated(rec.get("dialect") or ""):
        return (
            {
                **rec,
                "encodable": False,
                "compile_reason": NEGATED_UNSUPPORTED_REASON,
                "unencodable_reason": NEGATED_UNSUPPORTED_REASON,
                "corpus": corpus_slug,
                "corpus_slug": corpus_slug,
            },
            None,
            None,
            False,
        )
    try:
        local_cache_stats: dict[str, int] = {}
        cr = compile_pattern(
            pattern,
            flags,
            rec["dialect"],
            rec["call_kind"],
            domain=rec.get("domain") or "ascii",
            shell_flags=rec.get("shell_flags"),
            cache=cache,
            cache_stats=local_cache_stats,
        )
    except MemoryError as exc:
        raise BudgetBreached(
            corpus_slug,
            "max_mem_mb",
            budget.get("max_mem_mb") or 0,
            check_budget_mem(),
        ) from exc
    row = {
        **rec,
        "pattern": cr.pattern,
        "flags": flags,
        "encodable": cr.encodable,
        "compile_reason": cr.unencodable_reason,
        "corpus": corpus_slug,
        "corpus_slug": corpus_slug,
    }
    if cr.unencodable_reason == "timeout":
        row["result"] = "timeout"
    script = serialize_mirror(cr.mirror) if cr.encodable else None
    return (
        row,
        script,
        cr.meta,
        bool(local_cache_stats.get("hits")),
    )


_WORKER_CACHE: MirrorCache | None = None


def _init_compile_worker(
    budget: dict[str, Any], cache_dir: str,
) -> None:
    """Install per-worker limits and initialize a worker-local cache handle."""
    global _WORKER_CACHE
    apply_address_space_cap(budget)
    _WORKER_CACHE = MirrorCache(cache_dir)


def _compile_record_worker(payload: tuple[Any, ...]):
    rec, lift_inline, corpus_slug, budget = payload
    if _WORKER_CACHE is None:  # pragma: no cover - initializer contract
        raise RuntimeError("compile worker cache was not initialized")
    return _compile_one_record(
        rec,
        lift_inline=lift_inline,
        corpus_slug=corpus_slug,
        budget=budget,
        cache=_WORKER_CACHE,
    )


def compile_records(
    records: list[dict[str, Any]],
    *,
    lift_inline: bool,
    corpus_slug: str,
    budget: dict[str, Any] | None = None,
    wall_t0: float | None = None,
    jobs: int | None = 1,
    cache_dir: Path | str | None = DEFAULT_CACHE_DIR,
    cache_stats: dict[str, Any] | None = None,
) -> list[tuple[dict[str, Any], Any, dict[str, Any] | None]]:
    """Public compile_records API — pattern → ``(row, mirror, meta)`` (#193, C1).

    NDJSON rows stay lean (no Z3 AST in the row dicts); the mirror and its
    lowering metadata travel in-process as a ``(row, mirror, meta)`` triple so
    the P3 synthesis stage can consume them. A row whose compile failed or was
    rejected carries ``(row, None, None)`` — mirror is None and metadata is
    absent, so synthesis skips it fail-closed (never assumed eligible).
    """
    budget = budget or {}
    # Keep the value-observation seam visible to callers inspecting this API:
    # shell_flags=rec.get("shell_flags") is passed by _compile_one_record.
    check_budget_patterns(records, budget, corpus_slug)
    max_wall = budget.get("max_wall_s")
    max_mem = budget.get("max_mem_mb")
    # wall_t0 may be set before extraction so max_wall_s covers extract+compile.
    t0 = wall_t0 if wall_t0 is not None else time.monotonic()
    if max_mem:
        apply_address_space_cap(budget)
    else:
        from regexproof.batch import budgets as _budgets

        _budgets.LAST_ADDRESS_SPACE_CAP_APPLIED = None
    resolved_jobs = _resolved_jobs(jobs)
    cache = MirrorCache(cache_dir or DEFAULT_CACHE_DIR)
    payloads = [(rec, lift_inline, corpus_slug, budget) for rec in records]
    serialized: list[
        tuple[dict[str, Any], str | None, dict[str, Any] | None, bool]
    ] = []

    if resolved_jobs == 1 or len(payloads) < 2:
        for payload in payloads:
            rec, lift, slug, limits = payload
            serialized.append(
                _compile_one_record(
                    rec,
                    lift_inline=lift,
                    corpus_slug=slug,
                    budget=limits,
                    cache=cache,
                )
            )
            if max_wall and (time.monotonic() - t0) > max_wall:
                raise BudgetBreached(
                    corpus_slug, "max_wall_s", max_wall, time.monotonic() - t0
                )
            if max_mem:
                rss = check_budget_mem()
                if rss > max_mem:
                    raise BudgetBreached(corpus_slug, "max_mem_mb", max_mem, rss)
    else:
        executor = ProcessPoolExecutor(
            max_workers=resolved_jobs,
            mp_context=multiprocessing.get_context("spawn"),
            initializer=_init_compile_worker,
            initargs=(budget, str(cache.directory)),
        )
        futures = [executor.submit(_compile_record_worker, payload) for payload in payloads]
        breached = False
        try:
            for future in as_completed(futures):
                serialized.append(future.result())
                # The parent owns the wall-clock gate.  Check between worker
                # result batches rather than trusting child-local clocks.
                if max_wall and (time.monotonic() - t0) > max_wall:
                    breached = True
                    raise BudgetBreached(
                        corpus_slug, "max_wall_s", max_wall, time.monotonic() - t0
                    )
                if max_mem and check_budget_mem() > max_mem:
                    breached = True
                    raise BudgetBreached(
                        corpus_slug, "max_mem_mb", max_mem, check_budget_mem()
                    )
        finally:
            executor.shutdown(wait=not breached, cancel_futures=breached)

    if cache_stats is not None:
        hits = sum(bool(item[3]) for item in serialized)
        misses = sum(
            1
            for item in serialized
            if item[1] is not None and not item[3]
        )
        cache_stats["hits"] = hits
        cache_stats["misses"] = misses
        cache_stats["entries"] = hits + misses
        cache_stats["hit_rate"] = hits / (hits + misses) if hits + misses else 0.0

    # Workers return only strings/dicts.  Rebuild the live ASTs in the parent
    # after gathering all results, then sort before any downstream consumer.
    out = [
        (row, deserialize_mirror(script) if script is not None else None, meta)
        for row, script, meta, _cache_hit in serialized
    ]
    out.sort(key=lambda item: str(item[0].get("regex_id") or ""))
    return out
