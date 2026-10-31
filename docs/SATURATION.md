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

## PR5: first calibration execution

The executable calibration procedure is documented in
[`CALIBRATION.md`](CALIBRATION.md). It verifies ten local checkouts at the
manifest pins, records canonical-ID observations, writes a skip/failure log,
and emits a close-out memo. Missing or partial repositories prevent a
saturation report; a family with fewer than two completed repositories is
explicitly `insufficient_data`.

## Current calibration state (2026-10-31)

The newest complete bundle is
`properties/calibration/2026-09-12-calibration-20-r2/`: 20 pinned repositories,
zero failures, with a saturation report. All four observed families remain
productive under the strict trailing-two rule: ECMA 0.9259, Go 1.0000,
POSIX-shell 0.9474, and Python `re` 0.9792. The rule therefore supports
preparing a 30-repository increment; it does not establish product value.

The frozen-cohort PR4 checkpoint is now supplied at
`properties/calibration/2026-09-12-calibration-20-r2/conversion-checkpoint.json`.
Its report records 2 asked, 2 SAT, 2 ground-truthed, 2 private-first filed, and
0 accepted properties. The two dispositions reconcile to
`docs/conversion-upstream.jsonl`; both are `private_first`. The cohort's
product denominator is **2**, below the 50-property checkpoint. The original
canonical observation artifact still carries zero product rows, so the closeout
preserves that separate value as `observation_product_denominator: 0` and uses
the bound PR4 checkpoint for the human product denominator. The checkpoint
digest and report hash are retained in the close-out JSON and Markdown.
The source checkpoint reports two ground-truthed rows, but executable replay
against the pinned product paths is unavailable in this artifact; the closeout
marks zero rows independently verified and does not treat those reported rows
as verified ground truth.

The refreshed close-out sets `continue_to_20` false and `continue_to_30` true.
Compiler novelty remains productive in all four families; the product result
is still below its first denominator checkpoint. Both arms therefore remain
visible without treating compiler coverage as accepted security value.

Next actions:

1. Prepare a new 30-repository manifest by retaining the exact 20-r2 cohort
   pins and adding ten eligible, independent repositories across the measured
   families. Freeze its digest before checkout or observation work.
2. Work another bounded conversion wave on the frozen cohort, adding only
   human-adopted contracts with ground-truth and disposition evidence to the
   independent product coverage manifest. Do not count the global ledger or
   synthesized/agent-derived rows toward its denominator.
3. Run the next calibration only after all exact-pin checkouts are ready;
   publish the observation, failure, saturation, conversion-checkpoint, and
   close-out artifacts together.

The mine job is active intake, not processing. Current run status and the
working tree's as-of date belong in [`MINE-SETUP.md`](MINE-SETUP.md); do not
raise the mine cap to compensate for a conversion backlog.

## PR4: product conversion checkpoint

PR4 is a separate, read-only product checkpoint. It is not a compiler
saturation report and it does not modify `scripts/conversion-ledger.py` or
generated ledger artifacts. Run it with:

```text
python scripts/conversion-checkpoint.py path/to/conversion-checkpoint.json
```

The root object is exact: checkpoint `schema_version` (`"2"`), `cohort_id`,
`manifest_digest`, the embedded PR2 `cohort`,
`product_coverage_manifest`, and `rows`. The product coverage manifest has
schema version `"1"`, binds its `cohort_id` and `cohort_manifest_digest` to
the frozen cohort, and contains the complete product identity list plus a
`coverage_digest` over its canonical content. It must be independently derived
from the product inventory, not from the canonical rows being checked. Omitted
or extra product identities fail closed before construction. The embedded
cohort is validated and its digest is recomputed. Each row binds the exact `repo_id`/URL/lowercase
40-character pin from that cohort. Its stable identity is `(cohort_id, repo
URL, pin, site, question_id)`; duplicate keys, stale cohorts, unknown fields,
non-finite JSON, and repositories outside the cohort fail closed.
The report emits the product `coverage_digest`. Row and canonical contract
schemas remain version `"1"` inside checkpoint schema `"2"`.

Rows use the normalized product result vocabulary `sat`/`unsat`. The
`canonical_row_to_checkpoint()` adapter normalizes upstream `gap` rows to
`sat` and null UNSAT ground-truth markers to `not_applicable`, while retaining
the complete canonical row under `canonical`. Product rows require kind
`property`, `counterexample_finder`, or `bug_demo`, `synthesized: false`, and
the canonical contract fields `schema_version`, `site`, `guarantee`,
`input_source`, `trust`, `declared_domain`, and `provenance: "human"`.
`trust` must be `untrusted-input`, `config`, or `internal`, and the row's
`domain` must be explicit. Rule-diff, classification, mutation, synthesized,
and agent-derived rows are not product yield and cannot inflate this
denominator.

`ground_truth_status` is explicit; only `reproduced` and `PASS` advance a SAT
row to ground-truthed. Disposition status is also explicit and follows
`check-disposition-coverage.py`, including `approval_missing` and its required
escape metadata. Filing and resolution dates must be ISO dates or timestamps.
In the same semantics as `conversion-ledger.py`, filed means status `filed`,
`private_first`, or `fixed_upstream`, or a non-null explicit `filed_at`.
`filed_plan` is retained in the disposition breakdown but does not count as
filed. `private_first` remains separately visible while counting as filed.
Accepted means `fixed_upstream` only. That is an accepted upstream fix; it is
not automatically a third-party remediation, so own-code and third-party
interpretations must remain separate in the close-out. `false_positive`,
`wont_file`, and `out_of_scope_redos` are preserved as dispositions and are
not accepted yield.

The report emits deterministic counts and rates for asked → SAT →
ground-truthed → filed/private-first → accepted, a disposition breakdown,
observed sample sizes, explicit reached/sub-target flags for 50 and 100 human
product-property targets, and separate `filing_interpretation` and
`idiom_interpretation` fields. Its
interval method is a stdlib-only, two-sided 95% Wilson score interval. The
reported widths for targets 50 and 100 are the maximum width over every
possible success count at that sample size: they describe worst-case precision
of the target, not uncertainty around this cohort's observed rate. A zero
ground-truth-to-filed hop therefore does not prove idiom exhaustion; it is a
filing/product signal requiring separate interpretation.
