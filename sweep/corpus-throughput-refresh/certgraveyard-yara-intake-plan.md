# CertGraveyard YARA intake close-out — 2026-10-09

**Repository:** [`tjnel/certgraveyard_yara`](https://github.com/tjnel/certgraveyard_yara)

**Disposition:** admit a narrowly named Python generator source slice as
`triage-trial`; do not count this as YARA-rule regex corpus intake.

**Active time:** not recorded contemporaneously; no retrospective estimate
was made.

**Exact pin:** `d965ff32860bef8010f7eb1e7df7b9ea1762d2d4`

**Parent plan:** [`plan.md`](plan.md). The repository owner authorized agents
to adopt evidence-backed contracts under the standing rule in
[`docs/CONTRACTS.md`](../../docs/CONTRACTS.md). Autonomous admission decisions
for this backlog execution are covered by the user-directed scope recorded in
[`plan.md`](plan.md), not by the narrower standing contract authority.

## Intake decision

The refreshed repository metadata looked attractive in the stale score-v1
snapshot: its recorded YARA size was 15,374 and its old mined pin was
`cac568463861fdf80386a50958951cc06b3e9bbb`. At the new default-branch head,
however, the repository contains **2,889 YARA files and zero YARA regex
literals**. The complete Git tree has 2,923 blobs and 11 tree nodes (2,934
recursive entries); the rule files occupy 8,484,653 bytes. The license file is
MIT. These facts are recorded in
[`certgraveyard-yara-generator_source_inventory.json`](../../properties/generated/certgraveyard-yara-generator_source_inventory.json).

The exact-pin probe found three Python `re` sites:

| Site | Pattern | Boundary assessment |
|---|---|---|
| `src/cert_graveyard_yara/generator.py:79` | `[^a-zA-Z0-9]` | Replaces characters in CSV-derived name fields before YARA identifier/filename use. |
| `src/cert_graveyard_yara/generator.py:81` | `_{2,}` | Collapses underscores in the same sanitizer. |
| `src/cert_graveyard_yara/changelog.py:155` | `(## \[)` | Searches existing local changelog content; internal, no property adopted. |

The canonical probe command was:

```bash
uv run --python 3.12 python -m regexproof.probe --single \
  https://github.com/tjnel/certgraveyard_yara \
  --pin d965ff32860bef8010f7eb1e7df7b9ea1762d2d4 \
  --max-disk-mb 500 \
  --output /tmp/certgraveyard-yara-probe.json
```

It completed with three `py_re` sites, zero extractor errors, and
`security_boundary=deterministic-true`. Its per-file counts and the exact
probe pin are preserved in
[`certgraveyard-yara-generator_gate_decision.json`](../../properties/generated/certgraveyard-yara-generator_gate_decision.json).
The repository candidate ledger was not rewritten: its pin remains a mining
snapshot, and the gate-label artifact hashes the ledger bytes. A temporary
refreshed shortlist was used for screening, but its ranking artifact was not
retained and is not evidence for this committed intake.

## Admission conditions and scope

1. **New surface: no.** Python `re` and YARA are already supported. The YARA
   rules at this pin contain no regex literals.
2. **Security boundary: yes, narrowly.** The CSV parser maps external
   `Malware`, `Issuer Short`, and `Serial` fields into `CertificateRecord`.
   `sanitize_name` applies the two regex transformations before those values
   enter generated YARA identifiers and filenames. The CLI defaults to the
   CertGraveyard CSV endpoint and also permits an operator-supplied URL.
3. **Large and under-saturated: no.** There are three Python regex sites, far
   below 1,000; YARA-rule saturation does not apply to this Python source
   slice.

Condition 2 supports `triage-trial` for the dedicated slug
`certgraveyard-yara-generator`. The manifest scans only `src/**/*.py` with
`python_dir` / `py_re`, is marked as a security tool, and is not in
`WAVE_CORPORA`. It cannot inflate the YARA-rule corpus fraction or compiler
site count. The gate decision is schema-valid and records this narrow scope.

## Contract and source replay

The adopted contract is
[`certgraveyard-yara-generator_contract_candidate.json`](../../properties/generated/certgraveyard-yara-generator_contract_candidate.json).
Its guarantee is limited to a nonempty ASCII alphanumeric/underscore output
component for the three CSV-derived values at production call sites. The
fixed generated rule-name prefix and filename suffix then keep those values
from adding YARA syntax delimiters or path separators. It makes no length
claim and does not cover separate metadata escaping. Provenance remains
`agent_derived`; adoption records the user's standing delegation.

The replay script loads the pinned function definitions from their AST and
checks the real Python implementation. It tested 10,359 cases covering 10,276
distinct strings (including traversal forms, separators, controls, Unicode,
and deterministic random strings), 93,231 sanitized components, and 62,154
generated names. All passed. A mutation that lets `/` through the first
character class produced `/` for the witness `/`, so the output-alphabet guard
detected the weakened behavior. Evidence is saved in
[`certgraveyard-yara-generator_sanitizer_replay.json`](../../properties/generated/certgraveyard-yara-generator_sanitizer_replay.json)
and can be regenerated with:

```bash
uv run python scripts/replay-certgraveyard-yara-sanitizer.py \
  --repo /tmp/regexproof-certgraveyard-yara-src
```

The exact-pinned source audit also checks both YARA regex literal forms:
string assignments (`= /.../`) and condition expressions (`matches /.../`).
It found no hits in either form across all 2,889 rule files; the counts and
hit-site lists are recorded in
[`certgraveyard-yara-generator_source_inventory.json`](../../properties/generated/certgraveyard-yara-generator_source_inventory.json).
Reproduce it with:

```bash
uv run python scripts/audit-certgraveyard-yara-tree.py --repo /tmp/regexproof-certgraveyard-yara-src
```

The upstream `tests/test_generator.py` also passed all 32 tests when run with
the project coverage threshold disabled for this focused file. The replay and
upstream tests support the contract; neither is an SMT proof or a product
property result.

## Compiler and batch result

The full registered Python-source fraction run is deterministic and complete:
**3/3 encodable (1.0000)**, zero parse errors, no budget breaches, Python
3.12.15 / Z3 5.0.0. The exact output is in
[`certgraveyard-yara-generator_encodable_fraction.json`](../../properties/generated/certgraveyard-yara-generator_encodable_fraction.json);
the three extracted sites are listed in
[`certgraveyard-yara-generator-inventory.ndjson`](../../properties/generated/certgraveyard-yara-generator-inventory.ndjson).
Reproduce the determinism check with:

```bash
uv run python scripts/measure-corpus-fraction.py \
  --corpus certgraveyard-yara-generator --assert-determinism
```

The Smith batch completed with `extracted=3`, `encodable=3`, and
`triage=0`. Its [`batch summary`](../../properties/generated/certgraveyard-yara-generator_batch_summary.json)
and [NDJSON](../../properties/generated/certgraveyard-yara-generator.ndjson)
show four generic inventory questions in `planned` status; the
[corpus triage file](../../properties/triage/certgraveyard-yara-generator.ndjson)
is empty. The [PR dry-run](../../properties/generated/certgraveyard-yara-generator-pr-dry-run.json)
records four `private_first` planned rows and `publish=false`; the
[batch report](../../properties/generated/certgraveyard-yara-generator_batch.md)
has the human-readable summary. Reproduce it with:

```bash
uv run python scripts/batch-scan.py \
  --corpus certgraveyard-yara-generator \
  --out properties/generated \
  --cache-dir /tmp/regexproof-yara-batch-cache
```

These are workflow and compiler-smoke results only: **zero solver-run product
properties, zero SAT witnesses, zero conversion rows, and zero accepted
findings**. Do not turn the four planned questions into `properties_asked`.
Adding the new triage file and gate decision regenerated the live
[`compiler-feature-yield` summary](../../properties/generated/compiler-feature-yield.md):
its provenance now records 89 triage files and 871 gate decisions, while the
feature rows, 53,182 unencodable sites, and 156,477 weighted sites are
unchanged. This live summary is separate from the frozen human-provenance-only
PR4 calibration denominator.
The generated conversion ledger also now reflects the added batch summary:
three extracted and encodable Python sites plus four planned triage stubs.
Product questions, ground-truthed witnesses, and accepted upstream fixes did
not increase; these intake counters do not represent product conversion yield.

## Claims checked and disproved

- The large rule-file count and byte size do not imply a regex-bearing YARA
  corpus. The exact-pinned tree contains zero assignment-form (`= /`) or
  condition-form (`matches /`) regex literals in all 2,889 YARA files.
- The old candidate-ledger pin is stale; the live head is the exact pin above.
  The historical ledger row was preserved rather than rewritten.
- The changelog search is over existing local content, not the untrusted CSV
  boundary, so it was not given a contract.
- `3/3` encodable is a compiler fraction on three Python patterns, not a
  YARA-rule fraction, a solver result, or product success.
- The sanitizer replay checks the stated output properties. It does not
  establish full transformation equivalence for every string or cover
  metadata fields.

## Close-out

Keep the small Python source manifest, gate decision, source inventory,
contract candidate, and replay artifacts as a private-first triage record.
Do not add a YARA-rule manifest, conversion wave, or conversion-ledger row
from this intake. No public disclosure or upstream filing was performed.
Any later full product claim needs a dedicated harness property with a
sound transformation model and regression gate; the adopted contract alone
does not supply that proof.
