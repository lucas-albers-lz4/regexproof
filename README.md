# regexproof

**Prove security properties of your regexes with Z3 — a playbook + toolkit for
humans and coding agents.**

Regexes sit on security boundaries everywhere: input validators, whitelists,
sanitizers, parsers, log classifiers. `regexproof` turns "I think this regex is
safe" into "no string in the declared domain can violate this property —
machine-checked", and turns suspected parser bugs into reproducible witness
inputs.

- **SMT core:** `z3-solver` (Microsoft Z3), empirically validated on
  `z3-solver==5.0.0` (2026-08) against real OpenWrt/POSIX-sh security
  boundaries (see `docs/PLAYBOOK.md`).
- **Agent-first:** `AGENTS.md` is written to be consumed directly by coding
  agents (Hermes, Claude Code, Codex, opencode). An agent that loads this repo
  can go from "there's a regex on a security boundary" to a verified property
  suite with counterexamples.
- **ReDoS complement:** SMT proves *language properties* (containment,
  exclusion, capture correctness). Catastrophic-backtracking *complexity*
  analysis is a different problem — `docs/REDOS.md` maps the right tool
  (recheck, safe-regex2, …) per case.
- **Everything is testable:** the harness treats solver `unknown` (timeout) as
  a hard failure, requires mutation guards (a proof harness that can't fail
  proves nothing), and demands ground-truthing every counterexample against
  the real implementation.

## Quickstart

```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"             # package + z3-solver==5.0.0 (pinned)

# Run the 4 canonical property shapes (alphabet, whitelist, counterexample, per-token image):
.venv/bin/python scripts/z3-property-template.py

# Run the harness skeleton (property registry + mutation guards + timeout=hard-fail):
.venv/bin/python scripts/z3-verify.py --all --require-ground-truth

# Phase-1 foundations (compiler golden suite, schemas, argv-only fuzz adapters):
.venv/bin/pytest -q
```

Expected: all shapes PASS (UNSAT where property holds, SAT with a witness for
the counterexample finder — the sed-truncation bug repro).

## Layout

| Path | Role |
|---|---|
| `AGENTS.md` | Agent-facing instructions: when/how to verify, property checklist, what to ground-truth |
| `docs/PLAYBOOK.md` | The core method: strategy, workflow, performance rules, verification workflow |
| `docs/TRAPS.md` | Every solver trap we hit (Complement, z3str3, NUL, length bounds, …) with evidence |
| `docs/DECOMPOSITION.md` | How to decompose hard properties + how to read a proof correctly |
| `docs/BACKENDS.md` | seq vs z3str3 vs Z3-Noodler vs cvc5/Z3str3RE/dZ3 — what to use when |
| `docs/SEMANTICS.md` | Python `re` / JS ECMA-262 semantics mapping: expressible subset, lookaheads, backrefs, Unicode |
| `docs/REDOS.md` | ReDoS (complexity) tooling — complements, not replaces, the SMT approach |
| `docs/RESEARCH.md` | Deep-research findings: papers, tools, ecosystem, with sources |
| `regexproof/` | Installable package: `regex_id`, dialect compilers, argv-only fuzz adapters, extractor scaffolds, JSON schemas |
| `helpers/` | Mandated Go RE2 + ECMA (regexpp) + PCRE2 CLI helpers (parse and replay) |
| `tests/` | Golden suite, schema/extractor fixtures, false-UNSAT + Noodler probes |
| `scripts/z3-property-template.py` | The 4 canonical property shapes, copy-and-adapt |
| `scripts/z3-verify.py` | Harness: property registry, mutation guards, `rule_diff`/`call_kind`, `--require-ground-truth`, `--json`, timeout = hard failure |
| `scripts/differential-fuzz.py` | Fuzz a Z3 mirror against a real engine via `--real-argv` (no `shell=True`) |
| `properties/usrmanage-p1-p6.md` | Worked property suite (P1–P6) from the usrmanage case study |
| `properties/fwlive-classifier.md` | Worked regex inventory of the fwlive LuCI log classifier + lookahead blocker |
| `ci/python-matrix.toml` | Supported Python minors for golden-suite re-run (non-empty enforced in CI) |

## Provenance

Aggregated from real verification work on `lucas-albers-lz4/usrmanage`
(issue #6) and `lucas-albers-lz4/fwlive` (issue #120): every trap, timing,
and pattern in this repo was measured against `z3-solver==5.0.0` and
ground-truthed against real `sed`/`busybox sed` behavior. See
`docs/RESEARCH.md` for external sources.

## License

MIT
