#!/usr/bin/env python3
"""Dogfooding singleton analysis — P(compiles) distribution novelty curve.

Extracts regex sites from the four dogfooding repos (usrmanage, fwlive,
happycow, hermes-agent-fork) using the project's own extractors where they
exist (python_ast, js_babel) plus a labeled heuristic shell scanner (no shell
extractor exists yet — the OpenWrt dialect gap), then computes:

  - distinct patterns per repo (exact pattern+flags+dialect identity)
  - singleton fraction  -> Good-Turing P(next repo yields something unseen)
  - accumulation curve  -> novelty rate per repo added
  - Zipf concentration  -> top-N pattern share
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.extractors.python_ast import extract_python  # noqa: E402
from regexproof.extractors.js_babel import extract_js_precise  # noqa: E402

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

# --- heuristic shell scanner (labeled; no shell extractor in the project) ---
# grep/egrep/fgrep/sed 'PAT' | "PAT"; sed 's/SEARCH/REPL/' (search part);
# sed '/ADDR/d' address forms (first /re/ token); awk '/re/' programs;
# [[ $var =~ PAT ]].  NOTE: no VERBOSE mode — literal spaces are load-bearing.
_SHELL_CMD = re.compile(
    r"(?P<cmd>grep|egrep|fgrep|sed|awk)"
    r"(?:[ \t]+-[A-Za-z][A-Za-z0-9]*)*"      # flag runs incl. separate flags
    r"[ \t]+(?P<e>-e[ \t]+|--regexp=[ \t]*)?"
    r"(?P<q>['\"])(?P<pat>.*?)(?P=q)"
)
_SHELL_BASH = re.compile(r"\[\[[ \t]+\S+[ \t]+=~[ \t]+(?P<q>['\"])(?P<pat>.*?)(?P=q)")

_SED_S = re.compile(r"^s(?P<d>[^A-Za-z0-9])(?P<search>.*?)(?P=d)")
_SED_ADDR = re.compile(r"^/(?P<re>[^/]+)/")


def _sed_search(pat: str) -> str | None:
    m = _SED_S.match(pat)
    if m:
        return m.group("search")
    m = _SED_ADDR.match(pat)
    if m:
        return m.group("re")
    return None  # numeric address / range / other — not a regex


def scan_shell(src: str, *, repo: str, file: str) -> list[dict]:
    out = []
    for m in _SHELL_CMD.finditer(src):
        cmd, pat = m.group("cmd"), m.group("pat")
        if not pat:
            continue
        if cmd == "sed":
            search = _sed_search(pat)
            if search is None:
                continue
            pat = search
        elif cmd == "awk" and not pat.startswith("/"):
            continue  # awk program text is not a regex literal
        elif cmd == "awk":
            am = _SED_ADDR.match(pat)
            if not am:
                continue
            pat = am.group("re")
        # grep/egrep/fgrep: quoted arg IS the regex (flags consumed above)
        if len(pat) < 2:
            continue
        line_no = src.count("\n", 0, m.start()) + 1
        out.append({
            "pattern": pat,
            "flags": "",
            "dialect": "posix-shell",
            "file": file,
            "line": line_no,
            "extractor": "shell-heuristic",
        })
    for m in _SHELL_BASH.finditer(src):
        pat = m.group("pat")
        if len(pat) < 2:
            continue
        line_no = src.count("\n", 0, m.start()) + 1
        out.append({
            "pattern": pat,
            "flags": "",
            "dialect": "posix-shell",
            "file": file,
            "line": line_no,
            "extractor": "shell-heuristic",
        })
    return out


def extract_repo(name: str, path: str) -> list[dict]:
    records = []
    for p in sorted(Path(path).rglob("*")):
        if not p.is_file():
            continue
        rel = str(p.relative_to(path))
        if any(seg in SKIP_DIRS for seg in p.parts):
            continue
        if any(part.startswith(".") and part not in (".gitignore",) for part in p.parts):
            continue
        try:
            src = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        ext = p.suffix.lower()
        if ext == ".py":
            recs = extract_python(src, repo=name, file=rel)
        elif ext in (".js", ".mjs", ".ts", ".tsx"):
            recs = extract_js_precise(src, repo=name, file=rel)
        elif ext == ".sh":
            recs = scan_shell(src, repo=name, file=rel)
        else:
            continue
        for r in recs:
            if not r.get("pattern"):
                continue  # empty placeholder (composite-pattern etc.) — not a user regex
            r["extractor"] = r.get("extractor", ext.lstrip("."))
            records.append(r)
    return records


def main() -> None:
    by_repo: dict[str, list[dict]] = {}
    for name, path in DOGFOOD.items():
        recs = extract_repo(name, path)
        by_repo[name] = recs
        sites = len(recs)
        distinct = len({(r["pattern"], r.get("flags", ""), r["dialect"]) for r in recs})
        print(f"{name:<14} sites={sites:>5}  distinct={distinct:>4}")

    # identity = (pattern, flags, dialect)
    ident_of = lambda r: (r["pattern"], r.get("flags", ""), r["dialect"])
    pattern_of = lambda r: r["pattern"]
    cident_of = lambda r: (canon(r["pattern"]), r.get("flags", ""), r["dialect"])

    def summarize(label: str, ident_of) -> dict[tuple, set[str]]:
        owner: dict[tuple, set[str]] = {}
        for name, recs in by_repo.items():
            for r in recs:
                owner.setdefault(ident_of(r), set()).add(name)
        all_idents = list(owner)
        singletons = [i for i, owners in owner.items() if len(owners) == 1]
        shared = [i for i, owners in owner.items() if len(owners) > 1]
        gt = len(singletons) / len(all_idents)
        print(f"=== {label} ===")
        print(f"total distinct: {len(all_idents)}  singleton: {len(singletons)}  shared(>=2 repos): {len(shared)}")
        print(f"Good-Turing estimate P(next repo yields unseen pattern) = {gt:.3f}  ({gt*100:.1f}%)")
        print()
        return owner

    owner = summarize("identity = exact (pattern, flags, dialect)", ident_of)
    cowner = summarize("identity = canonicalized (vars->$V, digits->#)", cident_of)

    print("=== per-repo novelty (canonicalized) ===")
    for name in by_repo:
        own = sum(1 for i, owners in cowner.items() if owners == {name})
        tot = len({cident_of(r) for r in by_repo[name]})
        print(f"  {name:<14} unique-to-repo={own:>4}/{tot}  ({own/tot*100:.0f}%)")

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

    print("\n=== pattern-only view (no flags/dialect split) ===")
    powner: dict[str, set[str]] = {}
    for name, recs in by_repo.items():
        for r in recs:
            powner.setdefault(pattern_of(r), set()).add(name)
    psing = [p for p, o in powner.items() if len(o) == 1]
    print(f"distinct patterns: {len(powner)}  singleton: {len(psing)}  "
          f"GT = {len(psing)/len(powner):.3f}")

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
