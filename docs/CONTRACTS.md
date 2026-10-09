# Property contracts (#496 / #474)

A counted UNSAT or SAT is not a product result without a **contract**.

How to pick *which* sites get an approved contract, per distinct corpus
cluster (cap 5 per idiom slice, rank 15, no taint engine):
[`CLUSTER-CONVERSION.md`](CLUSTER-CONVERSION.md). First wave:
[`sweep/openwrt-conversion/plan.md`](../sweep/openwrt-conversion/plan.md).

## Object

Schema: `regexproof/schemas/property_contract.schema.json`.

Required fields: `schema_version` (`"1"`), `site`, `guarantee`, `input_source`,
`trust` (`untrusted-input` | `config` | `internal`), `declared_domain`, and
`provenance`. Agent-authored contracts can also carry an optional `adoption`
record; see the standing-authority section below.

## Provenance (#496)

| Value | Batch-scale? | Meaning |
|---|---|---|
| `human` | no | A person authored the guarantee; historical human-authored contracts are adopted implicitly. |
| `version_diff` | yes | Same rule id, adjacent tags. Machine-derivable. |
| `cross_engine` | yes | Same rule text, two engines, with `family_contract`. |
| `agent_derived` | no | An agent authored the guarantee. By itself it is a proposal and remains smoke; it becomes adopted only with a valid `adoption` record. |

Batch-scale generators may run only for `version_diff` and `cross_engine`.
Sibling-family pairing is not a provenance (#469). Provenance records how the
guarantee was authored or derived; adoption records the authority that approved
an agent-authored guarantee. Keep those facts separate.

## Standing user delegation (2026-10-09)

The repository owner has authorized agents working in this repository to
create and approve contracts without another approval prompt. A recommendation
that satisfies the evidence criteria below is the approval; do not stop for a
routine confirmation. This is a standing repository instruction, not a claim
that the agent is a human author.

For an approved agent-authored contract, retain `provenance: "agent_derived"`
and add an `adoption` object:

```json
{
  "status": "approved",
  "authority": "standing_user_delegation",
  "approved_on": "YYYY-MM-DD",
  "rationale": "Why this exact guarantee is useful and supported.",
  "evidence": ["source file and exact repository pin", "replay or test evidence"]
}
```

`authority` may instead be `direct_user_approval` when the user approved that
specific guarantee in the conversation. The schema requires an approval date,
non-empty rationale, and at least one evidence reference. An agent may approve
a contract only after reading the surrounding source and checking that the
guarantee, input source, trust class, and declared domain are specific and
supported. Narrow the domain to what the evidence supports. If the source does
not support a useful claim, leave the draft unadopted or record a no-go instead
of manufacturing a contract.

The harness and conversion ledger count an `agent_derived` contract only when
this adoption record is valid. Adoption does not prove that the mirror matches
the product engine: SAT witnesses still require ground truth, and UNSAT/TIMEOUT
semantics, engine versions, domain limits, and mutation guards remain separate
requirements. The frozen saturation calibration and PR4 checkpoint continue
to count only their original human-provenance cohort; delegated adoption does
not change that historical denominator.

This authority does not approve public disclosure, upstream filing, or messages
to third parties. Security-tool findings remain `private_first`; follow
[`SECURITY.md`](../SECURITY.md) for any external filing.

## Harness (#476)

UNSAT without an adopted contract + declared domain is not reportable product
(`product: false` on the harness NDJSON record). `--require-contract` makes
that a hard failure. An agent-authored contract must carry the approved
adoption record above. Mutation guards remain hygiene. Registry P1–P6 carry
human contracts so their UNSAT stays countable.

## Synthesis (#479)

Untargeted validator.js shape-1/2 rows are `properties_asked_synthesized`,
not `properties_asked`.

## Taint (#475)

Site-level taint/boundary is **not this architecture**. Extractors do not
carry sink provenance. Minimum future annotation: optional `input_source`
on the extractor record. Do not invent a dataflow engine here.

## Shape 3 generator (#478)

Deferred. No non-tautological search-shaped question exists without an adopted
product contract. Do not ship “does this miss a space?”.

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
