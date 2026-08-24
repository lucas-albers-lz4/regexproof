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
3. Pass `--active-minutes <float>` on the promote CLI. The CLI appends one
   jsonl row with a fresh `measurement_id` (uuid4). Do not reuse ids.
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
survivors only.

## Artifact contract

Each jsonl line:

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
