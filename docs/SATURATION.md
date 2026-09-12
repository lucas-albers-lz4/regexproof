# Corpus saturation measurement

Issue: [#623](https://github.com/lucas-albers-lz4/regexproof/issues/623)

This measurement has two separate questions:

1. Has a dialect family stopped contributing materially new compiler surface?
2. Is the verification workflow producing product value on a frozen set of
   real boundary sites?

Heap's law / singleton novelty answers only the first question. It must not be
used as a proxy for accepted security findings.

## PR1: deterministic cohort report

The first slice is a read-only calculator:

```text
python scripts/saturation-report.py path/to/cohort.json
```

The input is a pinned cohort plus an ordered observation envelope. The order is
meaningful within each `dialect_family`, because the report evaluates the
trailing two repositories in that family. The embedded `cohort` is the exact
output of the PR2 builder; its digest is recomputed before observations are
accepted.

```json
{
  "schema_version": "1",
  "canonicalization_version": "dogfood-singleton-analysis-v1",
  "cohort_id": "2026-09-calibration-10",
  "manifest_digest": "<64 lowercase hex characters>",
  "cohort": {
    "schema_version": "1",
    "cohort_id": "2026-09-calibration-10",
    "manifest_digest": "<same digest>",
    "repos": [
      {
        "repo_id": "owner/repo",
        "url": "https://github.com/owner/repo",
        "pin": "0123456789abcdef0123456789abcdef01234567",
        "dialect_family": "py_re",
        "boundary_family": "validator",
        "score": 1.0,
        "sites": 100
      }
    ]
  },
  "observations": [
    {
      "repo_id": "owner/repo",
      "url": "https://github.com/owner/repo",
      "pin": "0123456789abcdef0123456789abcdef01234567",
      "dialect_family": "py_re",
      "sites": 100,
      "novel_sites": 2,
      "new_reject_buckets": [],
      "product_properties": [
        {
          "site": "src/validator.py:10:4",
          "question_id": "no-space",
          "kind": "property",
          "provenance": "human",
          "synthesized": false,
          "result": "unsat",
          "ground_truthed": false,
          "filed": false,
          "accepted": false
        }
      ]
    }
  ]
}
```

`canonicalization_version` is a required producer identity: PR1 verifies the
declared singleton-analysis version but does not recompute canonical pattern
IDs from repository source. The separate processing log is checked with the
same frozen cohort binding:

```text
python scripts/check-measurement-events.py \
  --cohort path/to/frozen-cohort.json \
  path/to/measurement_events.jsonl
```

Every event has a lowercase-hex `previous_digest` and `event_digest`. The
first event points at 64 zeroes; each later event points at the prior digest.
Valid statuses include `attempted`, `completed`, `ok`, `auto_nogo`,
`needs_human`, `retry`, `cache_hit`, `timeout`, `unknown`, `error`, and
`partial`. The checker requires the cohort file, verifies its digest, binds
each event's repository URL and pin to it, and rejects a broken chain.

The report fails closed on malformed counts, a missing or mismatched cohort
digest, duplicate repository IDs or URL/pin attempts, observation order or
metadata that differs from the frozen cohort, invalid pins, empty site denominators, duplicate product
identities, non-human or synthesized product rows, non-finite JSON numbers,
and impossible funnel orderings. Rates are emitted as deterministic decimal
strings rather than binary floats. Product counts are derived from the
validated property rows, so rule-diff pilots, classification rows, mutation
guards, and agent-derived rows cannot inflate the denominator.

Compiler saturation is true for a family only when both trailing repositories
have a novelty rate strictly below `0.03` and neither introduces a new reject
bucket. The product denominator is total `properties_asked`; the first
checkpoint is `>=50`, with `>=100` as the preferred target.

This report does not infer cohort membership from the live candidate queue,
does not write artifacts, and does not add telemetry to
`corpus_events.jsonl`. That file is reserved for the conversion-wave lock
state machine. PR3 adds the separate immutable processing-event log and its
read-only checker.

The PR2 CLI rejects duplicate JSON keys and input/output aliases, and writes
the generated manifest through an fsync'd temporary file plus atomic replace.

## Operating interpretation

The mine job is intake, not processing: the live policy is one scheduled job
per day with a default cap of 10 candidates. The queue is currently full, so
raising that cap is not a saturation experiment. The working processing target
is approximately 5–7 gated repositories per week, or about one per workday.

Use a staged cohort:

- calibrate on 10 independent repositories;
- continue to 20 only if novelty or conversion remains material;
- continue to 30 if the 20-repository result is still productive;
- use 50 as a hard ceiling, not an automatic quota.

The compiler decision is per dialect family. The product decision is based on
human contracts, ground truth, filing, and upstream disposition over a frozen
cohort. Synthesized or agent-derived rows do not silently become product
yield.

## Next slices

- Define the immutable cohort manifest, pin/digest identity, and stratified
  target selection without changing the live score-v1 allocator.
- Add a separate append-only processing event log for mine, probe, gate,
  conversion, and disposition stages. Keep it distinct from the wave-lock
  log and fail closed on rewrite, duplicate identity, or unknown status.
- Join frozen cohorts to conversion-ledger identities and report
  asked → SAT → ground-truthed → filed/private-first → accepted.
- Run the first 10-repository calibration cohort, then publish a measured
  continue/retarget/stop close-out.
