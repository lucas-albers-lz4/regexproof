# Corpus and contract throughput plan

**Evidence snapshot:** 2026-10-08; adoption policy updated 2026-10-13.
**Purpose:** raise the rate of completed, product-valid contract work while
using corpus ingestion to test compiler coverage.

The current implementation/campaign plan is
[AUTONOMOUS-CORPUS-PLAN.md](AUTONOMOUS-CORPUS-PLAN.md), with an Oct 13
GitHub-main baseline. [AUTONOMOUS-CONTRACTS.md](AUTONOMOUS-CONTRACTS.md)
supersedes the human-only adoption requirement. The figures below remain the
dated Oct 8 snapshot, not live mine status.

## What the current evidence says

- The latest successful mine run admitted 10 candidates at the daily cap,
  found the 100-item overflow queue full, and dropped 410 overflow candidates
  after ranking. The Oct 8 scheduled attempt then failed on a remote connection
  drop before producing a summary or updating artifacts. The successful-run
  figures show candidate supply; they do not measure completed repository
  processing. See [`MINE-SETUP.md`](MINE-SETUP.md).
- A daily cap of 10 allows up to 70 admissions in a full week, compared with
  the 5–7 repository weekly processing target. That is a configured ceiling,
  not an observed weekly average; use the committed pipeline artifacts for the
  actual rate.
- The operating target is about 5–7 gated repositories processed per week.
  Local `pipeline-status.py` is behind the latest committed mine artifacts, so
  use a current committed snapshot before quoting survival or backlog rates;
  see [`PIPELINE.md`](PIPELINE.md).
- The newest complete calibration is 20 pinned repositories with no failures.
  All four dialect families remain productive by the compiler novelty rule,
  while the original baseline artifact had **0 embedded human product
  properties** and no PR4 conversion checkpoint. The Oct 13 Forge integration
  fixture is retrospective and does not replace a prospective cohort wave.
  See [`SATURATION.md`](SATURATION.md) and the
  [autonomous implementation fixture](../properties/calibration/2026-10-13-autonomous-forge-cli-integration/README.md).
- No frozen 30-repository manifest exists yet; candidate supplements from the
  older 20-repository pool cannot be assumed to extend the 20-r2 manifest.
  Select and freeze ten new eligible repositories before checkout work.
- The latest committed conversion ledger has 41 product questions, 8 SAT
  witnesses ground-truthed, and 1 accepted upstream fix; its cohort-wide
  counts do not replace the frozen-cohort checkpoint. The generated ledger is
  a changing artifact, so take the count from its current revision when
  reporting it.
- Existing conversion SOP caps each idiom wave at 15 reviewed sites and 5
  adopted contracts. A new append-only recorder is available for manually
  timed reviews, including skips; no conversion-review minutes have been
  recorded yet. It is separate from repository admission time.

## Operating plan

### 1. Keep intake steady; spend effort on processing

Keep the daily candidate cap at 10 while the overflow queue is full. Do not
raise it to compensate for a processing backlog. Each week, rank candidates
from the current queue, complete the existing 5–7 repository processing
target, and record probe outcomes and gate decisions. Revisit intake capacity
only after queue depth falls and processing is keeping up with new admissions.

### 2. Process one cluster at a time

For each admitted cluster, finish the probe, batch inventory, and gate decision
before opening another cluster. Reuse the score-v1 allocator and existing
pipeline; do not change allocator weights based on the current sample. Keep
the weekly scorecard focused on completed repositories, GO / triage-trial
survival, sites extracted, and encodable fraction. Mining volume alone is not
a throughput result.

### 3. Convert the admitted surface into product evidence

For each wave, rank 15 sites within one unused idiom bucket, read their source
context, and record the outcome and appropriate timing for every reviewed site,
including skips. The operator adopts at most five evidenced contracts with
named sinks, encodes the cheapest valid shape, runs the real product engine,
grounds SAT witnesses, and emits the conversion rows. Report:

- reviewed sites and skip reasons;
- adopted contracts by provenance and contracts per measured review effort;
- properties asked → SAT → ground-truthed → filed/private-first → accepted;
- any claims that source replay or engine comparison refuted.

Use [`CLUSTER-CONVERSION.md`](CLUSTER-CONVERSION.md) and
[`metrics-operator-minutes.md`](metrics-operator-minutes.md). The stopwatch is
for a human's active review; agents must not invent or backfill human minutes.
Agent runtime/usage belongs in a separate series.

### 4. Continue the staged calibration, with product coverage in parallel

Prepare a 30-repository calibration manifest by preserving every exact pin in
the completed 20-r2 manifest and adding ten eligible independent repositories
from the current admitted pool. Freeze its digest before cloning or observing.
In parallel, derive the independent product-coverage manifest for the frozen
cohort and work toward the first checkpoint of 50 eligible product
properties (100 is the preferred target). Product rows need evidenced adoption,
ground truth as required, and binding to the exact cohort pins. Do not treat
the 30-repository run as evidence of product success by itself.

## Weekly decision rule

At the end of each week, use one of these actions:

| Evidence | Action |
|---|---|
| Queue full; fewer than 5 gated repositories completed | Improve processing capacity or remove the specific probe blocker; keep intake cap unchanged. |
| Queue falling; 5–7 or more gated repositories completed | Continue the current cadence and refresh the next cohort candidate pool. |
| Compiler novelty remains above the `<0.03` stop threshold | Continue the staged calibration for that dialect family. |
| Frozen-cohort product denominator below 50 or PR4 absent | Continue conversion and coverage work; make no efficacy claim. |
| At least 50 eligible product properties plus migrated PR4 checkpoint | Review useful gates and the asked→SAT→ground-truth→filing→acceptance funnel; decide whether to expand toward 100, retarget, or stop. |

The existing numerical checkpoints are retained; crossing them is not a
success threshold. Routine contract adoption is autonomous under the new
policy once its executable eligibility migration lands. Owner input remains
appropriate for investment/success criteria and authorized disclosure. Those
choices do not block independent queue, inventory, or conversion work.
