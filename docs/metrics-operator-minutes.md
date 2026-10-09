# Operator-minutes metric (#575 Wave 6)

The #550 speed AC is **operator-minutes per human-reviewed survivor**, not
probes per UTC-day and not batch idle time. This document is the SOP.
Numbers live in [`properties/generated/operator_minutes.jsonl`](../properties/generated/operator_minutes.jsonl)
— **never** in `phase0_freeze.json` (hash-anchored).

## Two clocks (never merge)

| Clock | Source | What it is |
|---|---|---|
| **Wall-clock** | Artifact timestamps (`batch/state.json` `started_at`/`completed_at`, gate `decision_date` / `promoted_at`) | Elapsed time including clone, queue, and idle. |
| **Active minutes** | Stopwatch, uuid'd per review | Time the operator spent on that survivor. |

A ≥5× claim that only uses wall-clock is mostly batch idle. Report both.
Aggregation: **median primary, mean secondary** (outliers from a 300s clone
timeout must not dominate).

## Stopwatch SOP

1. Start the timer when the operator opens the staged draft / probe for a
   candidate that will become `go` or `triage-trial`.
2. Stop when the gate decision is authored (`bulk-review-staged.py --go` /
   `--triage-trial` or `author-gate-decision.py --human`).
3. Pass `--active-minutes <float>` on the promote CLI (`bulk-review-staged.py --go` / `--triage-trial`, or `author-gate-decision.py --human`). The CLI appends one jsonl row with a fresh `measurement_id` (uuid4). Do not reuse ids.
4. Do **not** record active minutes on deterministic `--no-go` (not a
   human-reviewed survivor).

## Baseline

Seed ≥5 rows **before Wave 5 unattended scale** (Phase 2 cache/batch already
landed; the unattended manifest loop is Wave 5). Seed rows may have
`active_minutes: null` when only a calendar `decision_date` exists; they still
count toward the ≥5-row floor so pre/post Wave 5 can be compared once
stopwatch rows exist.

Post Wave 5: same jsonl, `source: "stopwatch"`. Speedup =
`median(active_minutes)_pre / median(active_minutes)_post` on human-reviewed
survivors only. Deterministic `auto_nogo` walks are **not** survivors — do
not start a stopwatch on them. The unattended drain is
`python3 scripts/batch-run.py --limit N` (hashed `batch/manifest.json`,
resume on `(manifest_digest, url, pin)`). `batch_state.projection()["clone_ms_p95"]`
is the Phase-2 clone-time evidence Wave 4 (#563) is waiting on; do not
activate that trigger until a real drain has populated it.

## Conversion-site review clock

Admission time ends at the GO / triage-trial gate. Contract work has a separate
clock and artifact so admission speed cannot be mistaken for conversion speed.
For each site in the ranked top 15, start a stopwatch when opening its source
context and stop when recording either a human-adopted contract or a skip.
Include skipped sites: they consume reading time and are part of
conversion-yield-per-hour.

Record one completed site review with:

```text
python3 scripts/record-conversion-review.py \
  --corpus <cluster> --pin <40-char-sha> --wave-id <wave> \
  --idiom-bucket <bucket> --site <file:line:token> --rank <1..15> \
  --outcome contracted --question-id <stable-question-id> \
  --active-minutes <positive-minutes>
```

For a skip, use the queue outcome (`skipped_unreachable`,
`skipped_out_of_scope`, `skipped_no_response`, or `skipped_duplicate`) and omit
`--question-id`. The recorder writes append-only rows to
`properties/generated/conversion_review_minutes.jsonl`; it rejects duplicate
completed reviews for the same `(corpus, wave_id, site)` and rejects a wave
that mixes source pins or idiom buckets, or repeats a rank. Enter a positive
active-time value. Use `contracted` only after a human has adopted the
contract. It does not alter the queue, contract, conversion ledger, or frozen
checkpoint.

Summarize the measured waves with:

```text
python3 scripts/conversion-review-metrics.py
```

Report reviewed sites, contracted and skipped outcomes by reason,
total/median/mean active minutes, and contracts adopted per active hour. The
summary is grouped by corpus, source pin, wave, and idiom bucket. Keep this metric
separate from the admission `operator_minutes.jsonl` series and from unattended
clone / solver wall time. Treat an in-progress wave's rate as provisional;
compare yield per hour only after every site in that wave's ranked shortlist
has a recorded outcome.

## Admission artifact contract: `operator_minutes.jsonl`

Each admission-clock line has this shape; admission and conversion clocks are
stored in separate files.

```json
{
  "measurement_id": "uuid4",
  "url": "https://github.com/org/repo",
  "pin": "40-char sha",
  "decision": "go",
  "source": "seed-artifact-timestamps | stopwatch",
  "wall_minutes": null,
  "active_minutes": null,
  "recorded_at": "2026-08-24T00:00:00+00:00",
  "decision_date": "2026-08-13"
}
```

`wall_minutes` and `active_minutes` stay separate fields forever.

## Conversion artifact contract: `conversion_review_minutes.jsonl`

Each conversion-clock line has this shape:

```json
{
  "schema_version": "1",
  "measurement_id": "uuid4",
  "corpus": "forge-cli",
  "pin": "40-char lowercase sha",
  "wave_id": "forge-cli_helper_image",
  "idiom_bucket": "helper-image",
  "site": "build_runners/base.py:54:SENSITIVE_ENV_KEY_RE",
  "rank": 3,
  "question_id": "redacted-env-command-image",
  "outcome": "contracted",
  "source": "stopwatch",
  "active_minutes": 11.5,
  "recorded_at": "2026-10-08T18:00:00+00:00"
}
```

`question_id` is null for skips. `outcome` is `contracted` or one of the
`skipped_*` values listed above. Ranks are unique from 1 through 15 within a
`(corpus, wave_id)`; a wave also has one source pin and one idiom bucket.
