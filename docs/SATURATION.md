# Corpus saturation measurement

Issue: [#623](https://github.com/lucas-albers-lz4/regexproof/issues/623)

**Policy update 2026-10-13:** [autonomous contract adoption](AUTONOMOUS-CONTRACTS.md)
allows evidenced agent adoption without a human approving every contract.
[The parent plan](AUTONOMOUS-CORPUS-PLAN.md) measures useful proofs/gates and
downstream bugs. The shipped saturation validator accepts evidenced autonomous
contracts and reports provenance separately. PR4 v2 remains a historical
human-only format; v3 uses a contract-hash-bound roster and complete attempt
accounting. Do not relabel agent contracts as human.

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
metadata that differs from the frozen cohort, invalid pins, empty site
denominators, duplicate product identities, synthesized rows, incomplete
contracts, non-finite JSON numbers, and impossible funnel orderings. Rates
are emitted as deterministic decimal strings rather than binary floats.
Product counts are derived from validated property rows. Agent-derived rows
need the shared source-bound adoption record; machine-pair rows need their
contract evidence. Rule-diff pilots, classification rows, mutation guards,
and unadopted drafts stay outside the denominator. The report separates
human, autonomous, and machine-pair counts.

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
evidenced contracts, useful regression gates, ground truth, filing, and upstream
disposition over a frozen cohort. Synthesized questions and unadopted agent
drafts do not become product yield. Autonomous adoption requires the validated
review record and migrated executable eligibility policy.

## PR5: first calibration execution

The executable calibration procedure is documented in
[`CALIBRATION.md`](CALIBRATION.md). It verifies ten local checkouts at the
manifest pins, records canonical-ID observations, writes a skip/failure log,
and emits a close-out memo. Missing or partial repositories prevent a
saturation report; a family with fewer than two completed repositories is
explicitly `insufficient_data`.

## Current calibration state (2026-10-08)

The newest complete bundle is
`properties/calibration/2026-09-12-calibration-20-r2/`: 20 pinned repositories,
zero failures, with a saturation report. All four observed families remain
productive under the strict trailing-two rule: ECMA 0.9259, Go 1.0000,
POSIX-shell 0.9474, and Python `re` 0.9792. The rule therefore supports
preparing a 30-repository increment; it does not establish product value.

The original close-out records a product denominator of **0** and no PR4
checkpoint. The Oct 13 retrospective Forge integration fixture adds six
frozen identities, but it is not a prospective cohort wave or close-out.
Global ledger rows are not a substitute for a frozen-cohort coverage manifest.
For a complete 20-repository run, the close-out now sets `continue_to_20` false and resolves
`continue_to_30` from the compiler stop result. The product denominator and
PR4 checkpoint remain separate reasons to continue product work.

Next actions:

1. Prepare a new 30-repository manifest by retaining the exact 20-r2 cohort
   pins and adding ten eligible, independent repositories across the measured
   families. Freeze its digest before checkout or observation work.
2. In parallel, work a conversion wave on an admitted cluster and create the
   independent product coverage manifest for the cohort. Do not count the
   global ledger as a cohort manifest, synthesized smoke, or bare
   `agent_derived` drafts toward its denominator. Fully adopted agent rows are
   eligible and remain attributed to the autonomous series.
3. Run the calibration only after all exact-pin checkouts are ready; publish
   the observation, failure, saturation, and close-out artifacts together.

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

The root object is exact and versioned. Historical schema `"2"` contains
`cohort_id`, `manifest_digest`, the embedded PR2 `cohort`,
`product_coverage_manifest`, and decided `rows`; it remains human-only and
readable. Schema `"3"` adds a frozen contract roster and `attempts`, with one
explicit status per roster identity so timeouts, encoding failures, skips,
and not-attempted questions remain visible. Its schema-`"2"` coverage
manifest binds each stable identity to a contract digest and provenance. The
roster is frozen before outcomes are supplied. Both versions bind repository
URL and exact lowercase 40-character pin to the frozen cohort; duplicate
identities, stale digests, unknown fields, non-finite JSON, and repositories
outside the cohort fail closed. Row and contract schemas remain version
`"1"`.

Rows use the normalized product result vocabulary `sat`/`unsat`. The
`canonical_row_to_checkpoint()` adapter normalizes upstream `gap` rows to
`sat` and null UNSAT ground-truth markers to `not_applicable`, while retaining
the complete canonical row under `canonical`. Product rows require kind
`property`, `counterexample_finder`, or `bug_demo`, `synthesized: false`, and
the canonical contract fields `schema_version`, `site`, `guarantee`,
`input_source`, `trust`, and `declared_domain`. Schema 2 accepts only human
contracts. Schema 3 accepts adopted human and agent-derived contracts plus
valid machine-pair contracts; an agent contract must carry the shared
source-bound adoption record. `trust` must be `untrusted-input`, `config`, or
`internal`, and the row's `domain` must be explicit. Rule-diff,
classification, mutation, synthesized, and unadopted draft rows remain outside
the product denominator.

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
ground-truthed → filed/private-first → accepted, separate provenance totals,
v3 useful-gate outcomes, a disposition breakdown, observed sample sizes,
explicit reached/sub-target flags for 50 and 100 eligible product-question
targets, and separate `filing_interpretation` and
`idiom_interpretation` fields. Its
interval method is a stdlib-only, two-sided 95% Wilson score interval. The
reported widths for targets 50 and 100 are the maximum width over every
possible success count at that sample size: they describe worst-case precision
of the target, not uncertainty around this cohort's observed rate. A zero
ground-truth-to-filed hop therefore does not prove idiom exhaustion; it is a
filing/product signal requiring separate interpretation.
