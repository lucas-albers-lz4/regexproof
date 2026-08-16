# Property contracts (#496 / #474)

A counted UNSAT or SAT is not a product result without a **contract**.

## Object

Schema: `regexproof/schemas/property_contract.schema.json`.

Required fields: `site`, `guarantee`, `input_source`, `trust`
(`untrusted-input` | `config` | `internal`), `declared_domain`, `provenance`.

## Provenance (#496)

| Value | Scale? | Meaning |
|---|---|---|
| `human` | no | A person named the guarantee. Required for the general case. |
| `version_diff` | yes | Same rule id, adjacent tags. Machine-derivable. |
| `cross_engine` | yes | Same rule text, two engines, with `family_contract`. |
| `agent_derived` | no | An agent invented the question. Treat as smoke unless a human adopts it. |

Batch-scale generators may run only for `version_diff` and `cross_engine`.
Sibling-family pairing is not a provenance (#469).

## Harness (#476)

UNSAT without contract + declared domain is not reportable product. Mutation
guards remain hygiene.

## Synthesis (#479)

Untargeted validator.js shape-1/2 rows are `properties_asked_synthesized`,
not `properties_asked`.

## Taint (#475)

Site-level taint/boundary is **not this architecture**. Extractors do not
carry sink provenance. Minimum future annotation: optional `input_source`
on the extractor record. Do not invent a dataflow engine here.

## Shape 3 generator (#478)

Deferred. No non-tautological search-shaped question exists without a human
contract. Do not ship “does this miss a space?”.

## Shape 5 in batch (#477)

Admit only `version_diff` / `cross_engine` pairs that already have
`family_contract`. SAT must pass the search/pad matrix
(`regexproof.rule_diff.search_replay` when present). Keep fullmatch solve.
Do not flip `solver_call_kind` to search (VF-007).

## Measurement notes (#481–#495)

- **#481** Forks: gate decisions already carry `candidate_url`. Treat
  CPython-family clones as duplicates at admission when `fork: true` and
  the parent is already GO. Do not count 13× CPython as 13 corpora of novel
  surface.
- **#492** YARA `fullword-boundary` is ~68% of unencodable. Quote encodable
  fraction with and without YARA corpora.
- **#482 / #483** Bias-audit and rejected-tail risk are study design: freeze
  a labeled holdout, then measure. Not a regex change.
- **#491** Extractor recall needs an independently labeled sample (not the
  implementer).
- **#485** Independent annotator for gate labels. Live allocator stays
  score-v1. Do not turn on score-v2.
- **#495** Z3 vs DFA: add a `docs/why.md` paragraph per shape after a
  no-timeout DFA-product benchmark on the regular fragment. Not a Z3 rip-out.
