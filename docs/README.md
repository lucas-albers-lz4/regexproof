# docs/ index

Grouped by task, not by depth. Root entry points live one level up; every
other page is in this directory. Each entry is one link plus one clause.

## Entry points

- [`../README.md`](../README.md) — landing page: quickstart, layout, provenance.
- [`../AGENTS.md`](../AGENTS.md) — agent decision tree: when/how to verify.
- [`PLAYBOOK.md`](PLAYBOOK.md) — the core method: strategy, workflow, verification workflow.

## Method & traps

- [`TRAPS.md`](TRAPS.md) — every solver trap we hit (Complement, z3str3, NUL, length bounds) with evidence.
- [`BACKENDS.md`](BACKENDS.md) — seq vs z3str3 vs Z3-Noodler vs cvc5 — what to use when.
- [`SEMANTICS.md`](SEMANTICS.md) — `call_kind`, fold closures, `\d`/`\s`/`\w`, terminators per dialect.
- [`NEGATION.md`](NEGATION.md) — ModSecurity negation policy (`!@rx`, `negated=True`).
- [`DECOMPOSITION.md`](DECOMPOSITION.md) — decompose hard properties + how to read a proof correctly.
- [`DYNAMIC.md`](DYNAMIC.md) — dynamic compiles: classify, bound, prove or file.
- [`LOOKBEHIND_REWRITE.md`](LOOKBEHIND_REWRITE.md) — variable-width lookbehind → string-ops rewrite.

## Contracts & reporting

- [`CONTRACTS.md`](CONTRACTS.md) — property-contract object, provenance, what batch may scale.
- [`REPORTING.md`](REPORTING.md) — scanner NDJSON / triage / batch MD field contracts.
- [`conversion-upstream.jsonl`](conversion-upstream.jsonl) — curated last-mile conversion events (filed / fixed / false positive / private_first).
- [`verified-findings.jsonl`](verified-findings.jsonl) — machine-readable verified implementation findings.
- [`CLUSTER-CONVERSION.md`](CLUSTER-CONVERSION.md) — conversion-wave SOP: rank / write ≤5 human contracts per idiom slice.
- [`why.md`](why.md) — three claims with different evidence: mirror soundness, encodable fraction, conversion.

## Operations

- [`SECURITY-AUDIT.md`](SECURITY-AUDIT.md) — auditing regexproof itself: trust boundaries, controls, settled decisions, sweeps.
- [`CODERABBIT.md`](CODERABBIT.md) — working with CodeRabbit on PRs.
- [`REDOS.md`](REDOS.md) — ReDoS (complexity) tooling — complements, not replaces, the SMT approach.
- [`PIPELINE.md`](PIPELINE.md) — operator funnel: mine → rank → probe → gate → wave.
- [`MINE-SETUP.md`](MINE-SETUP.md) — daily mine setup (scheduled GitHub Code Search job).
- [`NEWGATE.md`](NEWGATE.md) — consumer adoption: point regexproof at one regex and get a gate.
- [`PILOT.md`](PILOT.md) — dogfooding report: usrmanage, fwlive, happycow trial runs + lessons.
- [`RESEARCH.md`](RESEARCH.md) — deep research: Z3/SMT for regex security, with sources.

## Reference & history

- [`terminology.md`](terminology.md) — corpus pipeline terminology.
- [`examples/`](examples/) — shape-5 `rule_diff` example (kind/family/mutation guards).
- [`final-report.md`](final-report.md) — corpus wave final report (#51–#57).
- [`metrics-operator-minutes.md`](metrics-operator-minutes.md) — operator-minutes metric (#575 Wave 6).
