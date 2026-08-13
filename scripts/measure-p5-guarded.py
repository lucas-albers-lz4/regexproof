#!/usr/bin/env python3
"""Guarded corpus measure — OOM-hardened wrapper for long Wave suites.

Guardrails:
- single-flight flock (stacked measure processes were OOM-killing the host)
- quiet stdout (milestones every 1000 only)
- progress status in ``/tmp/p5-measure-status.json`` (overwritten, tiny)
- relies on ``_compile_all`` RLIMIT_AS + VmRSS budget checks in runner.py

Usage:
  python scripts/measure-p5-guarded.py v8_mjsunit
  python scripts/measure-p5-guarded.py perl_tre go_regexp_tests
  python scripts/measure-p5-guarded.py v8_mjsunit --limit 300
"""

from __future__ import annotations

import fcntl
import importlib.util
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

STATUS = Path("/tmp/p5-measure-status.json")
LOCK = Path("/tmp/p5-measure.lock")


def _rss_mb() -> int:
    try:
        with open("/proc/self/status", encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("VmRSS:"):
                    return int(line.split()[1]) // 1024
    except Exception:
        return 0
    return 0


def _acquire_lock() -> object:
    fh = open(LOCK, "w", encoding="utf-8")
    try:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        raise SystemExit(
            f"ABORT: another measure holds {LOCK}. "
            f"Kill leftover python measure processes before retrying."
        ) from exc
    fh.write(f"pid={os.getpid()}\n")
    fh.flush()
    return fh


def _status(update: dict) -> None:
    cur: dict = {}
    if STATUS.exists():
        try:
            cur = json.loads(STATUS.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            cur = {}
    cur.update(update)
    cur["rss_mb"] = _rss_mb()
    cur["updated_ms"] = int(time.time() * 1000)
    STATUS.write_text(json.dumps(cur, indent=2, sort_keys=True) + "\n", encoding="utf-8")


spec = importlib.util.spec_from_file_location(
    "mcf", ROOT / "scripts" / "measure-corpus-fraction.py"
)
mcf = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mcf)

from regexproof.batch import runner as runner_mod  # noqa: E402
from regexproof.batch import compile_records as compile_mod  # noqa: E402

_orig = compile_mod.compile_records


def _compile_all_guarded(records, *, lift_inline, corpus_slug, budget=None, wall_t0=None):
    budget = budget or {}
    # Fail-fast on full extract size before chunking (Bugbot: chunked path
    # otherwise never sees len(records) > max_patterns).
    runner_mod._check_budget_patterns(records, budget, corpus_slug)
    n = len(records)
    out: list = []
    chunk = 100
    t0 = time.time()
    for i in range(0, n, chunk):
        part = records[i : i + chunk]
        # Per-chunk: skip max_patterns re-check (already enforced above).
        chunk_budget = dict(budget)
        chunk_budget.pop("max_patterns", None)
        out.extend(
            _orig(
                part,
                lift_inline=lift_inline,
                corpus_slug=corpus_slug,
                budget=chunk_budget,
                wall_t0=wall_t0,
            )
        )
        done = min(i + chunk, n)
        wall = time.time() - t0
        _status(
            {
                "phase": "compile",
                "corpus": corpus_slug,
                "done": done,
                "total": n,
                "wall_s": round(wall, 1),
            }
        )
        if done == n or done % 1000 == 0:
            print(
                f"  milestone {corpus_slug} {done}/{n} "
                f"wall={wall:.1f}s rss_mb={_rss_mb()}",
                flush=True,
            )
    return out


runner_mod._compile_all = _compile_all_guarded
runner_mod.compile_records = _compile_all_guarded
compile_mod.compile_records = _compile_all_guarded
mcf.compile_records = _compile_all_guarded


def main(argv: list[str]) -> int:
    lock_fh = _acquire_lock()
    limit = None
    args: list[str] = []
    i = 0
    while i < len(argv):
        if argv[i] == "--limit" and i + 1 < len(argv):
            limit = int(argv[i + 1])
            i += 2
            continue
        args.append(argv[i])
        i += 1
    corpora = args or ["v8_mjsunit"]

    try:
        for name in corpora:
            print(f"START {name}", flush=True)
            _status({"phase": "start", "corpus": name, "done": 0, "total": 0, "wall_s": 0})
            t0 = time.time()
            if limit is not None:
                from regexproof.batch.extract import extract_corpus
                from regexproof.batch.manifests import CORPUS_MANIFESTS

                meta = CORPUS_MANIFESTS[name]
                recs = extract_corpus(name, meta)[:limit]
                compiled = _compile_all_guarded(
                    recs,
                    lift_inline=bool(meta.get("lift_inline")),
                    corpus_slug=name,
                    budget=meta.get("budget") or {},
                )
                # compile_records now returns (row, mirror, meta) triples.
                enc = sum(1 for c, _m, _meta in compiled if c.get("encodable"))
                print(
                    f"DONE {name} limited {enc}/{len(compiled)} "
                    f"wall={time.time() - t0:.1f}s rss_mb={_rss_mb()}",
                    flush=True,
                )
                _status(
                    {
                        "phase": "done_limited",
                        "corpus": name,
                        "encodable": enc,
                        "sample_size": len(compiled),
                        "wall_s": round(time.time() - t0, 1),
                    }
                )
                # C1 fold (luna re-gate 4): release the Z3 ASTs — the measure
                # loop holds every corpus's mirrors otherwise.
                compiled.clear()
                continue

            report = mcf.measure(name, assert_determinism=False)
            print(
                f"DONE {name}: {report.get('encodable')}/{report.get('sample_size')} "
                f"= {report.get('fraction')} decision={report.get('decision')} "
                f"parse-error={report.get('unclassified_parse_errors')} "
                f"complete_run={report.get('complete_run')} "
                f"wall={time.time() - t0:.1f}s rss_mb={_rss_mb()}",
                flush=True,
            )
            _status(
                {
                    "phase": "done",
                    "corpus": name,
                    "encodable": report.get("encodable"),
                    "sample_size": report.get("sample_size"),
                    "fraction": report.get("fraction"),
                    "decision": report.get("decision"),
                    "unclassified_parse_errors": report.get(
                        "unclassified_parse_errors"
                    ),
                    "complete_run": report.get("complete_run"),
                    "wall_s": round(time.time() - t0, 1),
                }
            )
        return 0
    finally:
        try:
            lock_fh.close()
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
