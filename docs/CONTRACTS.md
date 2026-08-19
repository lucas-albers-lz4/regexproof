# Property contracts (#496 / #474)

A counted UNSAT or SAT is not a product result without a **contract**.

How to pick *which* sites get a `human` contract, per distinct corpus
cluster (cap 5 per idiom slice, rank 15, no taint engine):
[`CLUSTER-CONVERSION.md`](CLUSTER-CONVERSION.md). First wave:
[`sweep/openwrt-conversion/plan.md`](../sweep/openwrt-conversion/plan.md).

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

UNSAT without contract + declared domain is not reportable product
(`product: false` on the harness NDJSON record). `--require-contract` makes
that a hard failure. Mutation guards remain hygiene. Registry P1–P6 carry
human contracts so their UNSAT stays countable.

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
`family_contract` (`regexproof.rule_diff.batch_shape5`). The batch runner
**executes** those pairs (fullmatch Z3), then applies the search/pad SAT
gate (`gate_sat_witness`). A fullmatch SAT that fails the pad matrix is
`sat_fullmatch_only`, not a search finding. Do not flip `solver_call_kind`
to search (VF-007). Sibling-family and independent-spec pairs are not
admitted. Gitleaks catalog pairs currently have no `family_contract`, so
`gitleaks_batch_shape5` executed stays 0. CRS `version_diff` stamps
`family_contract` at discovery; Golden CI materializes older+newer rule
trees under `/tmp/crs-shape5/` and batch writes
`coreruleset_batch_shape5.json`. Pair `crs-942522` is excluded from batch
(hard timeout at DEFAULT_MAX_LEN). The conversion ledger counts decided
batch shape-5 rows as `properties_asked`. The pad matrix uses Python
`re.search` as a necessary filter, not PCRE2/RE2 fidelity; filing still
replays the real engines.

## Measurement notes (#481–#495)

- **#481** Forks: `regexproof.admission.forks` NO-GOs a clone when `fork: true`
  and the parent is already GO, or when the repo is a CPython/interpreter
  duplicate class. Mine search drops those candidates at enrich time (the
  enrich object has `fork` / `parent`). Human GO/triage-trial without enrich
  metadata still catches CPython-named URLs; other forks are the mine-search
  gate, not a second GitHub API call in `author_human`.
- **#492** Quote encodable fraction from `*_encodable_fraction.json` **with
  and without YARA**. Live `yara_split` on the conversion ledger.
- **#482 / #483** Bias-audit and rejected-tail risk (study design): freeze a
  labeled holdout of N≥100 gate decisions drawn before seeing score-v2
  weights. Labels: `should_admit` / `should_reject` / `uncertain`. Then
  measure (a) score-v1 vs human on that freeze, (b) among NO-GO rows,
  P(security-boundary regex | rejected) vs P(same | admitted). Do not retune
  weights on the freeze.
- **#491** Extractor recall: independently labeled sample of 50 files per
  dialect (not the implementer). Gold: span of each regex literal. Composer
  computes precision/recall; Grok or Luna labels if Grok fitted the extractor.
- **#485** Independent annotator for gate labels. Composer builds a
  blind-label harness (hide score, show probe only) and Cohen’s κ. Live
  allocator stays **score-v1**. Do not turn on score-v2.
- **#495** Z3 vs DFA: on the regular fragment, shape-1/2/5 are DFA-product
  decidable with no length bound and no `not_proven`. Until that benchmark
  ships, keep Z3. Outcome is a paragraph per shape in `docs/why.md`.
