# regexproof

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

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
  a hard failure (**not proven**), requires mutation guards (a proof harness
  that can't fail proves nothing), and demands ground-truthing every
  counterexample against the real implementation.

## Quickstart

```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"             # package + z3-solver==5.0.0 (pinned)

# Run the 5 canonical property shapes (alphabet, whitelist, counterexample,
# per-token image, rule_diff):
.venv/bin/python scripts/z3-property-template.py

# Run the harness skeleton (property registry + mutation guards + timeout=hard-fail):
.venv/bin/python scripts/z3-verify.py --all --require-ground-truth

# Run the shape-5 rule_diff pilot (gitleaks encodable subset, Phase 3):
.venv/bin/python scripts/rule-diff-pilot.py --family RD-github-oauth-token --require-ground-truth

# Run the batch scanner (inventory → triage → NDJSON/MD reports, Phase 5):
.venv/bin/python -m regexproof.batch --help

# Phase foundations (compiler golden suite, schemas, argv-only fuzz adapters):
.venv/bin/pytest -q
```

Expected: all shapes PASS (UNSAT where property holds, SAT with a witness for
the counterexample finder — the sed-truncation bug repro). If you run the ReDoS
stage, read `docs/REDOS.md` first.

Pinned helpers (Perl 5.38.x, `recheck`, YARA CLI) are **hard failures in CI**.
Locally, tests that need them skip and name the missing install:

```bash
# Perl pin (helpers/perl/match.py version → ok, 5.38.x)
# macOS: brew install perl@5.38 && export PATH="$(brew --prefix perl@5.38)/bin:$PATH"

# ReDoS recheck (helpers/redos/recheck.cjs)
cd helpers/redos && npm install && cd ../..

# YARA CLI (not the yara-python package) used by helpers/yara/match.py
brew install yara
```

`CI=true` or `GITHUB_ACTIONS=true` keeps the skip path closed so CI still fails
on toolchain drift.

## Layout

| Path | Role |
|---|---|
| `README.md` | Landing page: quickstart, layout index, provenance | 
| `CHANGELOG.md` | Phase-by-phase history of the initial development cycle |
| `AGENTS.md` | Agent-facing instructions: when/how to verify, property checklist, NDJSON contract |
| `SECURITY.md` | Private-disclosure-first policy for security-tool findings |
| `docs/SECURITY-AUDIT.md` | Auditing regexproof itself: trust boundaries, existing controls, settled decisions, sweeps |
| `docs/PLAYBOOK.md` | The core method: strategy, workflow, performance rules, verification workflow |
| `docs/TRAPS.md` | Every solver trap we hit (Complement, z3str3, NUL, length bounds, …) with evidence |
| `docs/DECOMPOSITION.md` | How to decompose hard properties + how to read a proof correctly |
| `docs/BACKENDS.md` | seq vs z3str3 vs Z3-Noodler vs cvc5/Z3str3RE/dZ3 — what to use when |
| `docs/SEMANTICS.md` | `call_kind`, fold closures, `\d`/`\s`/`\w`, terminators per dialect |
| `docs/DYNAMIC.md` | Dynamic compiles (`re.compile` from variables): classify, bound, prove or file | 
| `docs/LOOKBEHIND_REWRITE.md` | Variable-width lookbehind → string-ops rewrite (the `(?<=^)` + MULTILINE case) |
| `docs/REPORTING.md` | Scanner NDJSON / triage / batch MD field contracts |
| `docs/why.md` | Why this project exists: two machines + conversion, Heap's law vs product yield |
| `docs/conversion-upstream.jsonl` | Curated last-mile conversion events (filed / fixed / false positive / private_first) |
| `docs/examples/shape5-rule_diff.md` | Shape-5 `rule_diff` kind/family/mutation guards |
| `docs/verified-findings.jsonl` | Machine-readable verified implementation findings (toolkit traps, not vuln counts) |
| `docs/REDOS.md` | ReDoS (complexity) tooling — complements, not replaces, the SMT approach |
| `docs/RESEARCH.md` | Deep-research findings: papers, tools, ecosystem, with sources |
| `docs/PILOT.md` | Dogfooding report: usrmanage, fwlive, happycow trial runs + lessons |
| `regexproof/` | Installable package: compilers, batch, ReDoS, schemas |
| `helpers/` | Mandated Go RE2 + ECMA (regexpp) + PCRE2 CLI helpers + npm ReDoS helpers (parse and replay) |
| `pilots/` | Pilot corpora + dialect probes (gitleaks, validator.js, detect-secrets) |
| `batch/` | Batch corpora, fixtures, inventories (scanner-pipeline inputs) |
| `tests/` | Golden suite, schema/extractor fixtures, CI contract + docs checks |
| `scripts/z3-property-template.py` | The 5 canonical property shapes, copy-and-adapt |
| `scripts/z3-verify.py` | Harness: registry, mutation guards, `--json` / `--json-legacy`, GT |
| `scripts/differential-fuzz.py` | Fuzz a Z3 mirror against a real engine via `--real-argv` (no `shell=True`) |
| `scripts/rule-diff-pilot.py` | Phase-3 shape-5 `rule_diff` pilot on the gitleaks encodable subset |
| `scripts/batch-scan.py` | Phase-5 batch scan driver: inventory → triage → NDJSON/MD reports |
| `scripts/conversion-ledger.py` | Product funnel: sites → properties asked → SAT → GT → accepted upstream |
| `scripts/ci-assert-toolchain.py` | CI gate: assert pinned toolchain versions before runs |
| `scripts/ci-run-property-subset.py` | CI gate: run the measured-stable property subset |
| `scripts/ground-truth-b.py` | Batch ground-truth replay helper (real engines on witnesses) |
| `properties/usrmanage-p1-p6.md` | Worked property suite (P1–P6) from the usrmanage case study |
| `properties/fwlive-classifier.md` | Worked regex inventory of the fwlive LuCI log classifier + lookahead blocker |
| `properties/generated/` | Batch outputs: scanner NDJSON, `*_batch.md` reports, PR dry-runs, conversion ledger (regenerated) |
| `properties/triage/` | Triage NDJSON for unencodable / TIMEOUT / ambiguous compile items |
| `ci/python-matrix.toml` | Supported Python minors for golden-suite re-run (non-empty enforced in CI) |
| `ci/toolchain.toml` | Pinned toolchain versions for reproducible batch runs |

## Provenance

Aggregated from real verification work on `lucas-albers-lz4/usrmanage`
(issue #6) and `lucas-albers-lz4/fwlive` (issue #120): every trap, timing,
and pattern in this repo was measured against `z3-solver==5.0.0` and
ground-truthed against real `sed`/`busybox sed` behavior. See
`docs/RESEARCH.md` for external sources.

## License

MIT
