# Three-hour intake plan: certgraveyard YARA

**Candidate:** `tjnel/certgraveyard_yara`

**Mined pin:** `cac568463861fdf80386a50958951cc06b3e9bbb`

**Scope:** one bounded admission and (only if admitted) Smith triage cycle.
This is a plan to measure useful new corpus surface, not a conversion wave,
product proof, or security finding.

**Parents:** the [12-hour intake plan](plan.md),
[corpus admission gate](../corpus-admission-gate.md), and
[operator pipeline](../../docs/PIPELINE.md).

## Start condition

The ModSecurity rule 22200029 contract candidate is still `agent_derived`.
Close that cluster's human decision by adopting or rejecting its exact
guarantee before starting this intake. Until the decision is recorded, do
metadata-only preparation; do not clone, probe, register, or batch this
candidate. The pending CodeRabbit manual-review requirement on PR #650 is a
separate code-merge gate and does not decide the ModSecurity contract.

Once the prior contract gate is closed, re-read the current candidate ledger,
rank output, and gate files. The values below are the Oct 9, 2026 snapshot,
not permission to reuse a stale pin:

- Rank 5, score 89; YARA, recorded repository size 15,374; non-fork; pushed
  2026-08-14.
- URL: `https://github.com/tjnel/certgraveyard_yara`.
- Mined pin: `cac568463861fdf80386a50958951cc06b3e9bbb`.
- YARA is already supported. The admitted `yara_rules` corpus has 17,574
  sites and a recorded encodable fraction of 0.6563, so condition 1 is not
  met and condition 3 is possible only if this candidate has at least 1,000
  regex sites. Repository byte size is not a regex-site count.
- There is no committed gate or corpus manifest for this candidate at this
  snapshot.

## Work blocks (up to three active hours)

### 0:00–0:15 — close the prerequisite and refresh the candidate

- Confirm the ModSecurity human contract decision is recorded. If it is
  pending, stop candidate work here.
- Re-run the score-v1 shortlist and inspect the exact candidate-ledger row,
  gate labels, and any new gate decision. Record the rank, current pin, fork
  status, pushed date, and source query.
- Do not use `--allow-stale-pin`. If the default branch has moved since the
  mined pin, stop and re-rank; use a new exact pin only after its source and
  admission evidence are refreshed.

### 0:15–0:45 — run the bounded admission probe

Run the canonical single-candidate probe with the current exact pin and a
500 MB disk cap. Save the draft outside the repository:

```bash
uv run python -m regexproof.probe --single \
  https://github.com/tjnel/certgraveyard_yara \
  --pin cac568463861fdf80386a50958951cc06b3e9bbb \
  --max-disk-mb 500 \
  --output /tmp/certgraveyard-yara-probe.json
```

Record the observed YARA site count and per-file distribution, construct and
modifier counts, predicted buckets, extractor errors, and boundary label.
Treat the probe as a registered-extractor snapshot: it does not establish
complete tree coverage or count skipped oversized files as scanned.

### 0:45–1:25 — test admission value and overlap

- Verify the candidate has real `.yar`/`.yara` rule content at the exact pin;
  the mined repository size alone is not evidence of corpus scale.
- Check whether at least 1,000 regex sites are present. Re-read the current
  `yara_rules` fraction before applying condition 3's under-saturation test.
- Assess condition 2 independently. A security-tool label or YARA syntax is
  not enough: identify one concrete contract shape and the guarantee it
  could ask. For shape 5, require an independent specification or a valid
  version/cross-engine pair with a family contract.
- Compare exact rule-file and extracted-site fingerprints against the
  admitted YARA sources and prior YARA triage packs. Report the overlap and
  novel counts; do not treat copied rules as new compiler or conversion
  yield.
- Re-read the repository license and rule provenance before planning any
  later public disclosure. Any security-tool batch result remains
  `private_first`.

### 1:25–1:50 — prepare the admission decision packet

Evaluate all three documented admission conditions explicitly:

1. New dialect/flag/encoding surface: expected **no**; confirm from probe.
2. Security boundary with a concrete candidate property: only **yes** if
   source context names a testable guarantee and its property shape.
3. Large and under-saturated: **yes** only if the probe finds at least 1,000
   sites and the current nearest YARA fraction is below 0.85.

Prepare the schema-valid decision draft and a concise GO, triage-trial, or
NO-GO recommendation with exact evidence. Leave the decision pending until a
human records it; do not label a draft as an admitted gate.

### 1:50–2:45 — run Smith triage only after admission is recorded

If a human records `go` or `triage-trial` during the work block:

- Materialize the exact pin under `/tmp/regexproof-certgraveyard-yara` and
  verify `git rev-parse HEAD` equals the recorded pin. Keep the manifest slug
  `certgraveyard-yara` distinct from existing YARA corpus slugs.
- Use the pin revalidated in the first block:

  ```bash
  PIN=cac568463861fdf80386a50958951cc06b3e9bbb
  git clone --filter=blob:none \
    https://github.com/tjnel/certgraveyard_yara.git \
    /tmp/regexproof-certgraveyard-yara
  git -C /tmp/regexproof-certgraveyard-yara fetch --depth 1 origin "$PIN"
  git -C /tmp/regexproof-certgraveyard-yara checkout "$PIN"
  test "$(git -C /tmp/regexproof-certgraveyard-yara rev-parse HEAD)" = "$PIN"
  mkdir -p batch/corpora/certgraveyard-yara
  ln -sfn /tmp/regexproof-certgraveyard-yara/rules \
    batch/corpora/certgraveyard-yara/rules
  ```

- Add a narrow `rule_corpus` manifest using `dialect: "yara"`,
  `extractor: "yara"`, `**/*.yar,**/*.yara`, the exact repo/pin, and an
  existing bounded YARA budget appropriate to the measured site count.
  Register the corpus as `private_first`; do not add it to `WAVE_CORPORA`.
- Run deterministic fraction measurement and the single-corpus batch:

  ```bash
  uv run python scripts/measure-corpus-fraction.py \
    --corpus certgraveyard-yara --assert-determinism
  uv run python -m regexproof.batch --corpus certgraveyard-yara
  ```

  Review completion status, site and file counts, encodable fraction, parse
  errors, timeout/budget outcomes, overlap, triage output, and emitted
  summaries.
- Keep all generated evidence private. Do not create conversion rows from
  fraction or scanner output.

If the decision is still pending, stop after the admission packet. Do not
materialize or batch the repository on the basis of a pending draft.

### 2:45–3:00 — close out

Record actual active minutes, exact source pin, commands, admission-condition
results, overlap measurement, any human decision, and completed/incomplete
Smith outputs. Name any unresolved engine, scope, or product-contract issue.
Do not start a second repository or a conversion slice in this work block.

## Stop conditions

- The ModSecurity contract decision remains open at the start.
- The candidate pin is stale, the exact checkout cannot be verified, the
  clone exceeds 500 MB, or the probe has unexplained errors.
- Neither condition 2 nor condition 3 is supported by the observed source
  evidence. A large repository metadata field does not satisfy condition 3.
- The exact rule overlap leaves no defensible incremental value, or the
  declared YARA source scope cannot be reproduced within the time/budget.
- The Smith run is incomplete, over budget, below the 0.30 fraction gate, or
  has unexplained parse errors. Record the result; do not convert it to a
  product success.

## Completion evidence

The block is complete when the exact-pin admission packet has a human-recorded
decision and, only for an admitted candidate, a deterministic complete Smith
triage result—or a precise stop record explaining which gate failed. No
product contract or conversion count is expected from this intake alone.
