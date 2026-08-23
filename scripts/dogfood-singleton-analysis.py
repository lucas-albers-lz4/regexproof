#!/usr/bin/env python3
"""Dogfooding singleton analysis — P(compiles) distribution novelty curve.

Extracts regex sites from the four dogfooding repos (usrmanage, fwlive,
happycow, hermes-agent-fork) using the project's own extractors (python_ast,
js_babel) plus the REGISTERED posix-shell extractor
(regexproof/extractors/shell_posix.py — the P1-frozen heuristic semantics,
P2c migration), then computes:

  - distinct patterns per repo (exact pattern+flags+dialect identity)
  - singleton fraction  -> Good-Turing P(next repo yields something unseen)
  - accumulation curve  -> novelty rate per repo added
  - Zipf concentration  -> top-N pattern share

Shell scanner semantics (labeled heuristic):
  - grep/egrep quoted args are BRE/ERE patterns; fgrep / grep -F args are
    LITERALS and are skipped; grep -i maps to record flags="i".
  - sed contributes the search part of s/// (any delimiter) and /re/ address
    forms only; numeric addresses/ranges (e.g. 1,20p) are rejected.
  - awk program text is skipped; awk '/re/' address forms and awk -F'ERE'
    field separators are extracted.
  - [[ $x =~ PAT ]] extracts the UNQUOTED RHS only (bash 3.2+: a quoted RHS
    is a literal string match, not a regex).

Known false negatives (documented, not code paths):
  - glued flags+pattern, e.g. `grep -qE'pat'` (no space between the flag run
    and the quoted pattern), is not matched by the flag-run regex.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter, namedtuple
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.batch.manifests import MAX_FILE_BYTES  # noqa: E402
from regexproof.extractors.js_babel import extract_js_precise  # noqa: E402
from regexproof.extractors.python_ast import extract_python  # noqa: E402
from regexproof.extractors.shell_posix import extract_shell_posix  # noqa: E402

DOGFOOD = {
    "usrmanage": "/root/workspace/usrmanage",
    "fwlive": "/root/workspace/fwlive",
    "happycow": "/root/workspace/happycow",
    "hermes-agent": "/root/workspace/hermes-agent-fork",
}

# Canonicalization: same pattern modulo variable names / literals.
#   $_u, $MNT, ${index_url} -> $V ; \d+ runs -> # ; quoted literals left as-is
_CANON_VAR = re.compile(r"\$\{[^}]+\}|\$[A-Za-z_][A-Za-z0-9_]*")
_CANON_NUM = re.compile(r"\d+")


def canon(pattern: str) -> str:
    p = _CANON_VAR.sub("$V", pattern)
    p = _CANON_NUM.sub("#", p)
    return p


SKIP_DIRS = {".git", "node_modules", "dist", "build", ".venv", "venv",
             "__pycache__", ".tox", "coverage", "htmlcov", ".next"}

# --- shell extraction via the REGISTERED extractor (P2c migration) ---
# The P1 heuristic scanner internals were removed in P2c: the registered
# `regexproof.extractors.shell_posix` is the single source of the
# P1-frozen semantics (unquoted =~ RHS, fgrep/-F literal skip, -i -> flags,
# sed s/// + /re/ forms, awk /re/ + -F ERE, comment/string guards, token
# boundary).  Thin wrappers keep the probe-facing helpers stable.


def extract_bash_ere(src: str) -> list[str]:
    """Unquoted RHS patterns of bash/ksh [[ $x =~ ere ]] tests (via the
    registered extractor)."""
    return [r["pattern"] for r in _shell(src) if
            (r.get("shell_flags") or {}).get("syntax") == "bash_ksh"]


def extract_shell_patterns(src: str) -> list[str]:
    """Pattern strings only — thin wrapper for tests/probes."""
    return [r["pattern"] for r in _shell(src)]


def _shell(src: str) -> list[dict]:
    return extract_shell_posix(src, repo="", file="", dialect="posix-shell")

# --- repo walk / extraction -------------------------------------------------

_JS_EXTS = {".js", ".mjs", ".ts", ".tsx"}
# Shell surface OpenWrt actually uses, selected in --dir mode.
_SHELL_EXTS_DIR_MODE = {".sh", ".bash", ".init"}
_SHELL_SHEBANGS = {"#!/bin/sh", "#!/bin/bash",
                   "#!/usr/bin/env sh", "#!/usr/bin/env bash"}

RepoScan = namedtuple("RepoScan", "records per_file scanned_files oversized_files")


def _filtered(rel: str) -> bool:
    parts = Path(rel).parts
    if any(seg in SKIP_DIRS for seg in parts):
        return True
    return any(part.startswith(".") and part != ".gitignore" for part in parts)


def _classify(rel: str, first_line: str, *, dir_mode: bool) -> str | None:
    """Return 'py' | 'js' | 'sh' | None for a repo-relative path."""
    ext = Path(rel).suffix.lower()
    if ext == ".py":
        return "py"
    if ext in _JS_EXTS:
        return "js"
    if not dir_mode:
        return "sh" if ext == ".sh" else None
    if ext in _SHELL_EXTS_DIR_MODE:
        return "sh"
    if "init.d" in Path(rel).parts:
        return "sh"
    if first_line.strip() in _SHELL_SHEBANGS:
        return "sh"
    return None


def extract_repo(name: str, path: str, *, dir_mode: bool = False,
                 exts: set[str] | None = None) -> RepoScan:
    """Extract all regex-site records from one repo.

    dir_mode selects the full OpenWrt shell surface (*.sh, *.bash, *.init,
    init.d/*, shebang sniff); default mode scans .sh only, as before.
    exts (normalized, dot-prefixed) restricts the walk to those suffixes and
    disables init.d/shebang sniffing.  Files larger than MAX_FILE_BYTES are
    skipped (counted in oversized_files), never read.
    """
    records: list[dict] = []
    per_file: list[tuple[str, int]] = []
    scanned = oversized = 0
    walk_root = Path(path)
    if walk_root.name == "staged_probes":
        # Never walk staged probes (CI guard #559) — return a consistent
        # RepoScan (the namedtuple, not a bare tuple).
        return RepoScan(records, per_file, scanned, oversized)
    for p in sorted(walk_root.rglob("*")):
        if not p.is_file():
            continue
        rel = str(p.relative_to(path))
        if _filtered(rel):
            continue
        if exts is not None and p.suffix.lower() not in exts:
            continue
        try:
            size = p.stat().st_size
        except OSError:
            continue
        if size > MAX_FILE_BYTES:
            oversized += 1  # documented skip — never read, cannot OOM
            continue
        try:
            src = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        kind = _classify(rel, src.split("\n", 1)[0], dir_mode=dir_mode)
        if kind is None:
            continue
        scanned += 1
        if kind == "py":
            recs = extract_python(src, repo=name, file=rel)
        elif kind == "js":
            recs = extract_js_precise(src, repo=name, file=rel)
        else:
            recs = extract_shell_posix(src, repo=name, file=rel,
                                       dialect="posix-shell")
        kept = 0
        for r in recs:
            if not r.get("pattern"):
                continue  # empty placeholder (composite-pattern etc.) — not a user regex
            r["extractor"] = r.get("extractor", "shell_posix" if kind == "sh" else kind)
            records.append(r)
            kept += 1
        per_file.append((rel, kept))
    return RepoScan(records, per_file, scanned, oversized)


# --- CLI --------------------------------------------------------------------

NDJSON_NAME = "probe_records.ndjson"

_NDJSON_EPILOG = """\
--ndjson export schema (probe_records.ndjson):
  one NDJSON object per line, one record per regex site, EXACTLY these fields:
    pattern      str     regex text (sed: search part of s/// or /re/ address)
    flags        str     flag letters, "" when none (grep -i -> "i")
    dialect      str     "posix-shell" for shell-heuristic sites; .py/.js/.ts
                         sites keep their project-extractor dialect
    shell_flags  object  {"syntax": "bre"|"ere"|"bash_ksh",
                          "grep_mode": "basic"|"extended"|"fixed"|null}
                         (null for non-shell records)
    file         str     repo-relative path
    line         int     1-based line number
  Per-file counts are derived by AGGREGATING these records — the pattern text
  is required downstream (P3 merge) to derive construct counts.

Files larger than MAX_FILE_BYTES (2000000 bytes) are skipped and reported,
never read.  --ext restricts the walk to the given suffixes and disables
init.d/shebang sniffing.  --dry-run prints per-file record counts only (no
summary, no export).
"""


def _norm_exts(values: list[str] | None) -> set[str] | None:
    if not values:
        return None
    exts: set[str] = set()
    for v in values:
        for e in v.split(","):
            e = e.strip().lower()
            if e:
                exts.add(e if e.startswith(".") else "." + e)
    return exts or None


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        prog="dogfood-singleton-analysis.py",
        description="Dogfooding singleton analysis — P(compiles) novelty curve "
                    "over the four DOGFOOD repos (default) or one --dir repo.",
        epilog=_NDJSON_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--dir", metavar="PATH",
                    help="extract this repo instead of the four DOGFOOD repos; "
                         "shell file selection covers the OpenWrt surface "
                         "(*.sh, *.bash, *.init, init.d/*, shell shebangs)")
    ap.add_argument("--name", metavar="LABEL", default=None,
                    help="repo label for --dir (default: directory basename)")
    ap.add_argument("--ext", action="append", metavar="EXT",
                    help="restrict extraction to these file extensions "
                         "(repeatable, comma-separated ok; e.g. --ext sh --ext .py)")
    ap.add_argument("--dry-run", action="store_true",
                    help="print per-file record counts only; no summary, no export")
    ap.add_argument("--ndjson", action="store_true",
                    help=f"write full extraction records to {NDJSON_NAME} "
                         "(schema below)")
    ap.add_argument("--snapshot", action="store_true",
                    help="freeze/verify the novelty snapshot at "
                         "properties/generated/dogfooding_novelty_2026-08-12.json "
                         "(pinned per-repo SHAs, file lists, per-file site "
                         "counts, shell_flags-aware identity); refuses on "
                         "repo HEAD != recorded SHA; rerun is byte-identical")
    ap.add_argument("--snapshot-out", metavar="PATH", default=None,
                    help="write the snapshot to a different path (P2.5 "
                         "re-freeze: dogfooding_novelty_2026-08-12_POST_P2.json); "
                         "the pin-verification still reads the canonical "
                         "SNAPSHOT_PATH")
    args = ap.parse_args(argv)
    if args.name and not args.dir:
        ap.error("--name requires --dir")
    if args.dir and not Path(args.dir).is_dir():
        ap.error(f"--dir path is not a directory: {args.dir}")
    return args


def _ndjson_record(r: dict) -> dict:
    return {
        "pattern": r["pattern"],
        "flags": r.get("flags") or "",
        "dialect": r["dialect"],
        "shell_flags": r.get("shell_flags"),
        "file": r["file"],
        "line": int(r["line"]),
    }


def write_ndjson(by_repo: dict[str, list[dict]], out_path: Path) -> int:
    n = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for name, recs in by_repo.items():
            for r in recs:
                fh.write(json.dumps(_ndjson_record(r), ensure_ascii=False) + "\n")
                n += 1
    return n


SNAPSHOT_PATH = ROOT / "properties" / "generated" / "dogfooding_novelty_2026-08-12.json"
SNAPSHOT_DATE = "2026-08-12"
_SNAPSHOT_OUT: str | None = None


def _ident_of(r: dict, *, canon_pat: bool = False) -> tuple:
    """Identity for distinct/singleton counting.

    Shell records include the shell_flags syntax selector so a BRE literal
    `a+b` and an ERE one-or-more `a+b` do NOT collapse into one distinct
    pattern (P1 Step 4 requirement).
    """
    pat = canon(r["pattern"]) if canon_pat else r["pattern"]
    if r.get("dialect") == "posix-shell":
        sf = r.get("shell_flags") or {}
        return (pat, r.get("flags", ""), r["dialect"], sf.get("syntax"))
    return (pat, r.get("flags", ""), r["dialect"])


def _repo_head(path: str) -> str:
    out = subprocess.run(["git", "-C", path, "rev-parse", "HEAD"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit(f"snapshot: cannot resolve HEAD of {path}: "
                         f"{out.stderr.strip()}")
    return out.stdout.strip()


def _snapshot() -> None:
    """Freeze (or verify) the novelty snapshot over the DOGFOOD repos.

    Pins are load-bearing: the recorded SHA per repo is verified against the
    live HEAD on every run and a mismatch REFUSES to snapshot (no
    operator-dependent pinning). Rerun against the same pins is
    byte-identical (deterministic JSON: sorted keys/lists, no timestamps).
    """
    pins: dict[str, str] = {}
    if SNAPSHOT_PATH.exists():
        prev = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
        pins = {name: repo["sha"] for name, repo in prev["repos"].items()}
    heads = {name: _repo_head(path) for name, path in DOGFOOD.items()}
    for name, sha in heads.items():
        if name in pins and pins[name] != sha:
            raise SystemExit(
                f"snapshot: {name} HEAD {sha[:12]} != recorded pin "
                f"{pins[name][:12]} — refusing to snapshot (repos are "
                f"moving targets; reset to the pin or refresh the snapshot)")

    by_repo: dict[str, list[dict]] = {}
    for name, path in DOGFOOD.items():
        scan = extract_repo(name, path)
        by_repo[name] = scan.records

    def owner_map(ident_of) -> dict[tuple, set[str]]:
        o: dict[tuple, set[str]] = {}
        for name, recs in by_repo.items():
            for r in recs:
                o.setdefault(ident_of(r), set()).add(name)
        return o

    exact = owner_map(lambda r: _ident_of(r))
    canon_ids = owner_map(lambda r: _ident_of(r, canon_pat=True))

    sites_total = sum(len(recs) for recs in by_repo.values())
    n1_sites = sum(
        1 for name, recs in by_repo.items()
        for r in recs if len(exact[_ident_of(r)]) == 1)
    per_obs = n1_sites / sites_total if sites_total else 0.0

    per_repo: dict[str, dict] = {}
    file_lists: dict[str, list[str]] = {}
    site_counts: dict[str, dict[str, int]] = {}
    for name, recs in by_repo.items():
        d_exact = len({_ident_of(r) for r in recs})
        d_canon = len({_ident_of(r, canon_pat=True) for r in recs})
        own = sum(1 for i, owners in canon_ids.items()
                  if owners == {name} and i in {_ident_of(r, canon_pat=True)
                                                for r in recs})
        joint = own / d_canon if d_canon else 0.0
        per_repo[name] = {"sites": len(recs), "distinct_exact": d_exact,
                          "distinct_canon": d_canon, "joint_novelty": joint}
        shell_files = sorted({r["file"] for r in recs
                              if r.get("dialect") == "posix-shell"})
        file_lists[name] = shell_files
        counts: dict[str, int] = {}
        for r in recs:
            if r.get("dialect") == "posix-shell":
                counts[r["file"]] = counts.get(r["file"], 0) + 1
        site_counts[name] = dict(sorted(counts.items()))

    data = {
        "schema_version": "1",
        "snapshot_date": SNAPSHOT_DATE,
        "repos": {name: {"sha": heads[name]} for name in DOGFOOD},
        "stats": {
            "global": {
                "sites": sites_total,
                "distinct_exact": len(exact),
                "distinct_canon": len(canon_ids),
                "singleton_frac_exact": (
                    sum(1 for o in exact.values() if len(o) == 1) / len(exact)
                    if exact else 0.0),
                "singleton_frac_canon": (
                    sum(1 for o in canon_ids.values() if len(o) == 1)
                    / len(canon_ids) if canon_ids else 0.0),
                "per_observation_singleton_sites": per_obs,
            },
            "per_repo": per_repo,
        },
        "file_lists": file_lists,
        "site_counts_per_file": site_counts,
        "dialect_surface": dict(Counter(
            r["dialect"] for recs in by_repo.values() for r in recs)),
    }
    SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    target = SNAPSHOT_PATH
    if _SNAPSHOT_OUT:
        target = Path(_SNAPSHOT_OUT)
        target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    g = data["stats"]["global"]
    print(f"snapshot -> {target}")
    print(f"sites={g['sites']} distinct(exact)={g['distinct_exact']} "
          f"distinct(canon)={g['distinct_canon']} "
          f"singleton_frac(exact)={g['singleton_frac_exact']:.3f} "
          f"singleton_frac(canon)={g['singleton_frac_canon']:.3f} "
          f"per-obs-singleton={g['per_observation_singleton_sites']:.3f}")
    for name, st in per_repo.items():
        print(f"  {name:<14} sha={heads[name][:12]} sites={st['sites']} "
              f"distinct={st['distinct_canon']} joint={st['joint_novelty']:.3f}")


def main(argv: list[str] | None = None) -> None:
    args = _parse_args(argv)
    if args.snapshot:
        if args.dir or args.ext or args.dry_run or args.ndjson:
            raise SystemExit("--snapshot is exclusive: no --dir/--ext/"
                             "--dry-run/--ndjson")
        global _SNAPSHOT_OUT
        _SNAPSHOT_OUT = args.snapshot_out
        _snapshot()
        return
    if args.dir:
        dir_mode = True
        repos = {args.name or Path(args.dir).resolve().name: args.dir}
    else:
        dir_mode = False
        repos = dict(DOGFOOD)
    exts = _norm_exts(args.ext)

    by_repo: dict[str, list[dict]] = {}
    for name, path in repos.items():
        scan = extract_repo(name, path, dir_mode=dir_mode, exts=exts)
        recs = scan.records
        by_repo[name] = recs
        if args.dry_run:
            for rel, n in scan.per_file:
                if n:
                    print(f"{name}:{rel}: {n}")
            print(f"{name}: TOTAL records={len(recs)} "
                  f"files_scanned={scan.scanned_files} "
                  f"oversized_skipped={scan.oversized_files} "
                  f"(max_file_bytes={MAX_FILE_BYTES})")
            continue
        sites = len(recs)
        distinct = len({(r["pattern"], r.get("flags", ""), r["dialect"]) for r in recs})
        print(f"{name:<14} sites={sites:>5}  distinct={distinct:>4}")
        if scan.oversized_files:
            print(f"  skipped {scan.oversized_files} file(s) > {MAX_FILE_BYTES} bytes")

    if args.dry_run:
        return

    if args.ndjson:
        n = write_ndjson(by_repo, Path(NDJSON_NAME))
        print(f"wrote {n} records -> {Path(NDJSON_NAME).resolve()}")

    if not any(by_repo.values()):
        print("no regex sites found")
        return

    # identity = (pattern, flags, dialect) — shell records additionally carry
    # the syntax selector so a BRE literal `a+b` and an ERE one-or-more `a+b`
    # do NOT collapse into one distinct pattern (same rule as --snapshot).
    def ident_of(r: dict) -> tuple:
        return _ident_of(r)

    def cident_of(r: dict) -> tuple:
        return _ident_of(r, canon_pat=True)

    def summarize(label: str, ident_of) -> dict[tuple, set[str]]:
        owner: dict[tuple, set[str]] = {}
        for name, recs in by_repo.items():
            for r in recs:
                owner.setdefault(ident_of(r), set()).add(name)
        all_idents = list(owner)
        singletons = [i for i, owners in owner.items() if len(owners) == 1]
        shared = [i for i, owners in owner.items() if len(owners) > 1]
        frac = len(singletons) / len(all_idents)
        print(f"=== {label} ===")
        print(f"total distinct: {len(all_idents)}  "
              f"singleton: {len(singletons)}  shared(>=2 repos): {len(shared)}")
        print(f"distinct-pattern singleton fraction (convenience-sample "
              f"estimate, NOT a formal Good-Turing estimator) = {frac:.3f}  "
              f"({frac*100:.1f}%)")
        print()
        return owner

    owner = summarize("identity = exact (pattern, flags, dialect, shell syntax)",
                      ident_of)
    cowner = summarize("identity = canonicalized (vars->$V, digits->#)",
                       cident_of)

    # per-observation singleton fraction: n1/N over SITES (the honest
    # Good-Turing-adjacent figure; the distinct fraction above is a
    # convenience-sample estimate, not a formal estimator).
    n1 = sum(1 for recs in by_repo.values() for r in recs
             if len(owner[_ident_of(r)]) == 1)
    n_sites = sum(len(recs) for recs in by_repo.values())
    print(f"per-observation singleton fraction (n1/N over sites) = "
          f"{n1/n_sites:.3f}  ({n1}/{n_sites})")
    print()

    print("=== per-repo novelty (canonicalized) ===")
    for name, recs in by_repo.items():
        own = sum(1 for i, owners in cowner.items() if owners == {name})
        tot = len({cident_of(r) for r in recs})
        print(f"  {name:<14} unique-to-repo={own:>4}/{tot}  "
              f"{(own/tot*100) if tot else 0:.0f}%")

    print("\n=== accumulation curve (canonicalized, order: size asc) ===")
    order = sorted(by_repo, key=lambda n: len({cident_of(r) for r in by_repo[n]}))
    seen: set[tuple] = set()
    for n in order:
        new = sum(1 for i in {cident_of(r) for r in by_repo[n]} if i not in seen)
        seen |= {cident_of(r) for r in by_repo[n]}
        print(f"  after {n:<14}: distinct={len(seen):>4}  (+{new} new)")

    print("\n=== Zipf concentration (exact identity) ===")
    cnt = Counter(i for name, recs in by_repo.items() for i in {ident_of(r) for r in recs})
    top = cnt.most_common(8)
    tot = sum(cnt.values())
    cum = 0
    for i, c in top:
        cum += c
        print(f"  {i[0][:60]!r:62} x{c}  cum={cum/tot*100:.1f}%")

    print("\n=== pattern-only view (no flags/dialect/syntax split) ===")
    powner: dict[str, set[str]] = {}
    for name, recs in by_repo.items():
        for r in recs:
            powner.setdefault(r["pattern"], set()).add(name)
    psing = [p for p, o in powner.items() if len(o) == 1]
    print(f"distinct patterns: {len(powner)}  singleton: {len(psing)}  "
          f"pattern-singleton fraction = {len(psing)/len(powner):.3f}")

    # shared patterns of interest (the 'seen-before' mass)
    print("\n=== most-shared patterns ===")
    top_shared = sorted(powner.items(), key=lambda kv: -len(kv[1]))[:10]
    for p, owners in top_shared:
        if len(owners) > 1:
            print(f"  x{len(owners)} {p[:70]!r}  in {sorted(owners)}")

    # dialect surface
    print("\n=== dialect surface ===")
    d = Counter(r["dialect"] for name, recs in by_repo.items() for r in recs)
    for k, v in d.most_common():
        print(f"  {k:<14} {v}")


if __name__ == "__main__":
    main()
