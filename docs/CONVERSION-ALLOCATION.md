# Conversion candidate allocation

**Status:** allocator and repository-backed history index implemented; a
first real pre-outcome allocation is recorded for the separate Aidevops Node
calibration. **Scope:** choose which eligible sites enter one review
shortlist after the scheduler selects a source-pinned idiom bucket.

The scheduler chooses a cluster/bucket. The allocator chooses source sites in
that bucket. It does not create a property contract, open a wave, or run a
solver. Keep those states separate.

`source_sites` in the bucket registry is the bounded eligible source pool
(maximum 10,000 sites). `max_candidates` is the review-shortlist cap (maximum
15). Keep those limits separate: a 15-site pool sampled at size 15 is a census
and cannot demonstrate seed-based allocation from a larger population.

## Frozen population

One population belongs to one exact GO cluster, source pin, and registered
idiom bucket. Freeze it before solving any question. The JSON shape is defined
by [`conversion_candidate_population.schema.json`](../regexproof/schemas/conversion_candidate_population.schema.json).
Each candidate records its regex/site identity, exact source file hash,
inventory `site`, product engine, call kind, trust class, encoding eligibility,
stable idiom key, classification evidence, and prior question IDs. The
allocator joins every candidate by `regex_id` to the exact inventory site,
pattern, flags, dialect, call kind, encoding flag, and corpus. It also requires
the source site to be listed in the bucket registration and the trust class to
be present in its trust map. It refuses internal-only or unencodable rows,
rows carrying prior question IDs, duplicate identities, and source files that
do not match the clean pinned checkout. The population also binds a frozen
question-history index. The allocator checks that the index still matches the
current recognized source set and file digests, then rejects candidates
already asked, reserved, or covered by unresolved site history. It checks both
the source site and inventory-site alias; an empty `prior_question_ids` list
is no longer accepted as evidence by itself.

When an exact GitHub repository URL is present, the index uses the lowercase
`owner/repo` as its canonical cluster. This coalesces runner rows keyed by
repository ID with conversion rows keyed by the shorter corpus label; the
source URL, pin, and site remain bound in the identity. P2 exact-pin source
review evidence is also indexed as a reservation for every reviewed site,
including skips and unresolved sites, so a later allocation cannot silently
re-review a previously assessed site.

The separate classification JSON is bound by digest and must contain exactly
one matching label/evidence row per candidate, plus the population ID, source
pin, and conversion-ledger digest. The allocator checks those joins; it does
not decide whether a `productive` or `novel_idiom` claim is true. The evidence
note still has to cite the completed proof and product gate (for productive),
or the frozen ledger search (for novel). A hash proves which note was used,
not that the note's reasoning is sound.

The pre-outcome classes are:

- `productive`: the same stable idiom key already has a completed
  contract-backed useful proof and product gate in the conversion ledger.
- `novel_idiom`: the idiom key is absent from the completed conversion ledger
  frozen with the population.
- `unclassified`: evidence cannot support either label. These candidates are
  available to the unbiased arm only.

Every class needs a written `classification_evidence` note. The population
binds the classification artifact and conversion-ledger snapshot with separate
SHA-256 fields; the classification artifact repeats the ledger digest. A
candidate with no trustworthy label stays unclassified; do not infer novelty
from a new filename or a regex text hash.

## Allocation rule

The nominal review shares are 70% productive, 20% novel idiom, and 10%
unbiased. The unbiased arm draws uniformly from the full eligible population
using the pre-outcome SHA-256 seed. Productive and novel selections then draw
from their labeled pools without duplicating a site already selected by the
unbiased arm. If a class is too small, the allocator records the shortfall and
fills remaining slots with a second uniform draw. Actual arm counts are
reported, so a declared ratio never substitutes for the realized allocation.

Quotas use largest remainders with a stable tie order. When at least one slot
exists for each available arm, reserve one per arm first. For fifteen sites
with all arms available, the nominal mix is 10 productive, 3 novel, and 2
unbiased. For five sites, it is 3/1/1. If an arm has no candidates, its share
is reallocated across the available arms. The sample size is at most fifteen
and cannot exceed the registered bucket's `max_candidates` cap. The registered
source pool can be larger than the shortlist; it must include every eligible
site that may be selected.

The population stores a SHA-256 commitment to the 64-character seed. The
allocator rejects a revealed seed that does not match that commitment.
Candidates are ranked by a keyed SHA-256 of seed, arm, and regex ID. This makes
the result stable across input-row order and Python random-library changes.
The CLI cannot prove when the population file was frozen: `frozen_at` is a
self-reported timestamp. Preserve the population hash in an immutable or
versioned record before queue review or solver execution so the seed
commitment is meaningfully pre-outcome.

## Run it

This example requests the full review shortlist. It requires a bucket with a
`max_candidates` cap of at least fifteen and a frozen eligible population
larger than the requested sample if the goal is to measure selection rather
than census the pool.

```sh
python3 scripts/freeze-question-history-index.py \
  --output "$QUESTION_HISTORY_INDEX_JSON"

python3 scripts/allocate-conversion-candidates.py \
  --population "$POPULATION_JSON" \
  --gate-decision "$GO_DECISION_JSON" \
  --schedule "$CONVERSION_SCHEDULE_JSON" \
  --bucket-registry properties/conversion_bucket_registry.json \
  --checkout "$PINNED_CHECKOUT" \
  --inventory-file "$PINNED_INVENTORY_NDJSON" \
  --classification-file "$FROZEN_CLASSIFICATION_JSON" \
  --conversion-ledger "$PRE_OUTCOME_CONVERSION_LEDGER_JSON" \
  --question-history-index "$QUESTION_HISTORY_INDEX_JSON" \
  --selection-seed "$PRE_OUTCOME_SHA256_SEED" \
  --sample-size 15 \
  --output "$ALLOCATED_SHORTLIST_JSON"
```

The command requires an exact matching GO pin, the scheduler's
`named-next-unused` registered bucket, registered candidate sites and trust
classes, a clean source checkout, matching inventory/classification/ledger
digests and row joins, a seed matching the frozen population commitment, and
no active corpus wave. It writes the input digests, source rechecks, seed,
nominal quotas, selected sites, and actual counts into the output. It does not
silently create a population or assign idiom labels.

For a cohort campaign, generate the schedule with `--cohort-manifest` so GO
decisions and registrations are scoped to the frozen repository pins and
dialect families:

```sh
python3 scripts/conversion-scheduler.py \
  --cohort-manifest properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --out properties/generated/conversion_schedule_20r2.json
```

The registry's optional `dialect_family` field is required for a bucket to be
eligible in this mode. Entries outside the manifest pin or with a different
dialect are emitted as rejected registrations. This keeps separate
calibrations, such as Aidevops ECMA work, out of the cohort's POSIX-shell
schedule. The schedule records the manifest digest. Campaign inventories must
also preserve dialect-specific selectors such as POSIX-shell `shell_flags`;
the P2 inventory v4 does so, while v3 remains preserved for historical joins.

The index command currently recognizes conversion NDJSON, aggregate
autonomous-run measurements, runner state/checkpoints/attempts, frozen rosters
and shortlists, contract artifacts, conversion-queue JSON, source-bound review
evidence and decisions, queue-transition replays, and
`docs/conversion-upstream.jsonl`. It records every recognized source path and
SHA-256; allocation rebuilds that set and fails on changed or newly discovered
history files. Aggregate work records without site identities are reported as
unbound and block matching repository pins until reconciled. The index covers
those repository artifacts, not undocumented external work or records outside
the listed source families. The current post-outcome scan is
[`question-history-index.json`](../properties/calibration/question-history-index.json);
review its source manifest and unbound-record list before freezing a real
population. The dated snapshots below preserve earlier pre- and post-outcome
views.

## Current evidence boundary

The allocator's synthetic coverage checks determinism, duplicate/previously
asked and reserved-site rejection, stale-history rejection, the 10/3/2
fifteen-site allocation, unbiased selection from the whole pool, and exact
inventory/classification joins. Those checks validate the allocation code
only. A registry validation bug originally applied the 15-site review cap to
`source_sites` as well, preventing a real registered pool from exceeding the
shortlist. Registration now accepts up to 10,000 source sites while retaining
the 15-candidate review cap. The registry has four buckets: Mycelium
scripts-bootstrap (one site, cap 5), Malcontent git-crlf-smuggling (seven
sites, cap 1), Aidevops Node secret-read policy (three registered sites
including its reserved representative, cap 2), and the Real-Router navigation
control calibration (one site, cap 1). The Mycelium representative is reserved,
all seven Malcontent shortlist sites are reserved, and the Real-Router
singleton site is consumed. For Aidevops, the exact-pin source inventory and compiler
check left two encodable, unasked candidates after excluding the adopted
representative; one was selected from that two-site pool with a committed
seed. Both classifications were honestly left `unclassified`, so the realized
allocation was one unbiased site and no productive or novel-idiom selections.
The pre-outcome population, history, ledger, inventory, classification,+scheduler, registry, and allocation digests are frozen in
[`2026-10-15-autonomous-aidevops-node-secret-boundary/`](../properties/calibration/2026-10-15-autonomous-aidevops-node-secret-boundary/).
This satisfies P4's minimum real-allocation path for a separately scoped
calibration; it is too small to estimate allocation quality or conversion
throughput, does not exercise productive/novel strata, and is not a 20-r2/P7
result. A larger original-cohort allocation and the rationale review for any
future class labels remain outstanding.

**History-index refresh (2026-10-15):** the first current-tree refresh stopped
on that Aidevops calibration's legacy queue-transition summary, which stores
`second_wave_transitions` as phase names and `contracted_sites` as explicit
site/status rows rather than raw `transitions` with command stdout. The
indexer now reads only those explicit `contracted` site rows as reservations;
it does not infer a proof attempt from phase names. The rebuilt, post-outcome
snapshot is
[`2026-10-15-question-history-index-after-autoar-jsendpoint.json`](../properties/calibration/2026-10-15-question-history-index-after-autoar-jsendpoint.json),
SHA-256 `28d869d6c370a52cedf3cc37c4f26c4355baa2d87437cc0172ffe3e800eddaec`:
102 recognized sources, 61 asked sites, 119 reserved sites, and 7 unresolved
unbound records. It includes the new AutoAR endpoint identity as both asked
and reserved. This refreshed index is for duplicate prevention; it is not a
pre-outcome allocation artifact.

**Post-AutoAR scope-candidate history refresh (2026-10-15):** after the
source-bound `scriptSrcRe` contract and P6 counterexample were recorded, I
rebuilt and verified
[`2026-10-15-question-history-index-after-autoar-jsendpoint-scope.json`](../properties/calibration/2026-10-15-question-history-index-after-autoar-jsendpoint-scope.json),
SHA-256 `44f6e7f52fb1a96c89a31883e9344975ef3b8be04b0894c4ef2e974178eac43c`.
It covers 110 recognized sources, 63 asked sites, 120 reserved sites, and 7
unbound records. The new AutoAR question is indexed as asked and reserved for
duplicate prevention. This post-outcome snapshot does not establish that the
site was available to a pre-outcome allocator and is not allocation evidence.

**Post-SAT-triage history refresh (2026-10-15):** after curating four new
private-first candidate dispositions and correcting two Doberman false
positive dispositions, the current index was rebuilt at
[`question-history-index.json`](../properties/calibration/question-history-index.json),
SHA-256 `92f1217d0c38e15510ee3f3531eb843dcfaa76529ac159fbd4fd8ef01a5de8d7`.
That prior snapshot covered 176 recognized sources, 75 cluster-keyed asked
entries, 129 reserved entries, and seven unbound records. It is preserved as a
historical refresh, not a pre-outcome allocation artifact.

**P2 source-review integration and identity refresh (2026-10-15):** the
history index now consumes the exact-pin P2 `evidence*.json` source-review
format. A frozen index at
[`question-history-index.json`](../properties/calibration/question-history-index.json),
SHA-256 `a3a50afd0eb21881509da18f08921e603570453aecb9a791acfc3e4148ee5de8`,
covers 192 recognized source artifacts, 55 asked source identities, 204
reserved entries, and seven unbound records. The asked count is lower than the
prior 75 because repo-ID and corpus-name aliases now coalesce under the exact
GitHub repository identity; the two new P6 questions add two distinct asked
source identities. The four P2 review slices contribute 91 raw reviewed sites
(one superseded Anax evidence snapshot is also retained as a source artifact).
This is a post-outcome duplicate-prevention snapshot, not allocation evidence.

**Panther P2 review and v8 identity refresh (2026-10-15):** the history index
now includes the exact-pin Panther review, contract, P6 runner, and v8
checkpoint evidence. The frozen snapshot
[`2026-10-15-question-history-index-after-panther.json`](../properties/calibration/2026-10-15-question-history-index-after-panther.json)
and current
[`question-history-index.json`](../properties/calibration/question-history-index.json)
are byte-identical, SHA-256
`6016a174a6c7b95cf3cb6bd4235c0f9fb27972f295d3ef3929e794e9aaa55755`.
They cover 204 source artifacts, 56 asked identities, 250 reserved sites, and
seven unbound records. The five reviewed P2 slices now account for 136 raw
sites. The former 75 asked count included 22 repeated cluster aliases; this
is a post-outcome duplicate-prevention snapshot, not allocation evidence.

**Inhale P2 and v9 history refresh (2026-10-15):** after freezing the Inhale
source-review, contracts, P6 runner, and v9 retrospective checkpoint, the
duplicate-prevention index was rebuilt to
[`2026-10-15-question-history-index-after-inhale.json`](../properties/calibration/2026-10-15-question-history-index-after-inhale.json).
It is byte-identical to the current
[`question-history-index.json`](../properties/calibration/question-history-index.json),
SHA-256
`d64f9005324359f5190cd3a50ae2bc7854772daf8429269249c9d9dfc831a3ac`:
215 recognized source artifacts, 58 asked identities, 255 reserved sites,
and seven unbound records. The six reviewed P2 slices now account for 139 raw
sites. This post-outcome snapshot is for duplicate prevention, not allocation
evidence.

**BinaryAlert and Snyk Language Server P2 review (2026-10-15):** the two new
exact-pin source reviews add 38 raw sites: BinaryAlert's one documentation
version-extraction site is skipped, while Snyk LS has 36 skips and one
unresolved hover-formatting candidate. Across the eight completed P2 review
slices, this brings coverage to 177 sites (149 skipped, 17 unresolved, 11
adopted). The latest frozen index is
[`2026-10-15-question-history-index-after-snyk-ls.json`](../properties/calibration/2026-10-15-question-history-index-after-snyk-ls.json),
byte-identical to the current
[`question-history-index.json`](../properties/calibration/question-history-index.json),
SHA-256
`7b9db4a152232ec69aed85e62200b16fea5f05f6189ed6bbd590dd34d5e3e874`:
217 recognized source artifacts, 58 asked identities, 293 reserved sites,
and seven unbound records. The index remains a post-outcome duplicate
prevention snapshot, not allocation evidence.

**Json Editor source review, exact-column join, and v11 checkpoint
(2026-10-15):** the 96-site review adds one source-backed EnumEditor
string-escaping contract, 94 evidence-backed skips, and one unresolved
Base64-preview sink. The contract's regex literal shares a line with two other
regexes. The retrospective join previously excluded any contract at such a
line as ambiguous, even though the frozen inventory records extractor
columns. The P2 matcher and P6 runner now accept a `column-N` source selector;
the exact `column-24` row binds to regex id
`21a271471f4c1c1fbc13a331e0f706da`. The completed r3 wave is counted once;
two earlier attempts with the ambiguous `replace` anchor remain explicitly
excluded. The v11 checkpoint reports 28 unique questions (17 UNSAT, 11 SAT),
15 useful local gates, 23 product replays, and 1,229,873 differential cases.
Across the nine P2 source-review slices there are 273 sites: 243 skips, 18
unresolved, and 12 adopted. See the
[Json Editor review/P6 bundle](../properties/calibration/2026-10-15-p2-json-editor-source-review/README.md)
and [v11 checkpoint](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v11/README.md).

**Post-Json Editor duplicate-prevention refresh (2026-10-15):** the frozen
[`2026-10-15-question-history-index-after-json-editor.json`](../properties/calibration/2026-10-15-question-history-index-after-json-editor.json)
is byte-identical to
[`question-history-index.json`](../properties/calibration/question-history-index.json),
SHA-256 `c7a18561c80e0e57530564817a84885d113d48e43d0e547d4f963081e1ca9e39`.
It recognizes 243 source artifacts, 60 asked identities, 391 reserved sites,
and seven unbound records. This post-outcome snapshot only prevents future
duplicate questions; it is not evidence that a site was eligible before the
Json Editor outcomes were observed.

**Magic JS review, P6 waves, and v12 refresh (2026-10-15):** the ECMA
hashbang false-positive correction produced inventory v3 with 20,705 sites
(19 complete repositories; Everclaw still lacks six submodules). The exact-pin
Magic JS review covers 64 sites: 53 skips, one unresolved wallet-kit email
validator, and ten adopted Base64URL contracts. The runner completed two
serial five-question waves; both verified the source pin, ran the shared
mutation guard and exact-source Node gate, and proved all five properties
UNSAT. The ten properties and one shared gate are new compatible product
evidence. The ten per-question Node replay counts sum to 481,034 with zero
mismatches. Each P6 execution reran the complete ten-question Node command,
so the two recorded runs performed 962,068 comparisons; v12 counts the
question-specific coverage once. Phase sums were 1.0245 and 1.0204 seconds.
The run recorder keeps the two actual executions separate in
[`autonomous_work.jsonl`](../properties/generated/autonomous_work.jsonl),
including exact work-item IDs. The contracts cover output formatting only;
the missing CryptoJS dependency means the PKCE modules were checked through
their source-authenticated replacement chains and an RFC 7636 test vector,
not imported directly.

The v12 retrospective checkpoint joins 38 questions (27 UNSAT, 11
ground-truthed SAT), 16 useful local gates, 33 product replays, and 1,710,907
question-attributed differential cases; the shortfall to 50 is 12. No new SAT
candidate, reachable violation, confirmed impact, external report,
maintainer confirmation, or third-party fix arose from Magic JS. See the
[Magic JS review/P6 bundle](../properties/calibration/2026-10-15-p2-magic-js-source-review/README.md),
[v12 checkpoint](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v12/README.md),
and [v3 inventory note](../properties/calibration/2026-10-15-p2-source-inventory-v3/README.md).

The post-outcome index at
[`2026-10-15-question-history-index-after-magic-js.json`](../properties/calibration/2026-10-15-question-history-index-after-magic-js.json)
is byte-identical to the current index, SHA-256
`ce17b4a627a4517ac2c2f37cec74242b09fbced4f44bf31c579d218a6a75a71c`.
It covers 261 recognized artifacts, 70 asked identities, 465 reserved sites,
and seven unbound records. As with the earlier snapshots, it prevents
duplicate questions after outcomes are known; it is not pre-outcome allocation
evidence.

**Doberman Core P2/P6 follow-up and v13 checkpoint (2026-10-15):** the
source-bound review covers 104 exact-pin Python regex sites (19 skips, 83
unresolved heuristics, two adopted Codex path-extraction questions). The two
UNSAT theorems are deliberately limited to one-character printable-ASCII path
destinations. The exact pinned helper AST gate additionally ran 514 cases over
all four documented directive forms, leading whitespace, CRLF, and a mixed
multi-directive patch, with zero mismatches. A mutation that removes `Delete`
is SAT and reproduces against the exact helper. This is finite regression
evidence and does not prove arbitrary-length path completeness or the
correctness of Doberman's protected-path policy. The checkout could not import
the full adapter because Pydantic is absent locally; the gate executed only
the exact regex definitions and adapter helper AST using the standard library.

The P6 wave completed two questions, one local gate, one mutation guard, and
514 question-attributed comparisons. Its measured phase sum was 0.9681
seconds. Review/contract-authoring time, tokens, cost, and human active time
were not separately measured. It added no SAT candidate or downstream
outcome. The strict v13 checkpoint is 40 questions (29 UNSAT, 11
ground-truthed SAT), 17 useful local gates, 35 product replays, and 1,711,421
question-attributed differential cases; the shortfall to 50 is 10. See the
[Doberman review/P6 bundle](../properties/calibration/2026-10-15-p2-doberman-source-review/README.md)
and [v13 checkpoint](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v13/README.md).

The separately generated
[20-r2 run scorecard](../properties/calibration/2026-10-15-autonomous-scorecard-20r2-after-doberman.json)
summarizes 22 recorded runs and 36 proof-question attempts. It keeps the
three requested measures distinct: throughput/resource totals; useful proof,
gate, mutation, and replay output; and downstream SAT/reachability/impact and
external-confirmation/fix outcomes. This run log has six SAT candidates, six
replayed witnesses, six reachable violations, and zero confirmed security
impacts, consumer-adopted gates, reports, maintainer confirmations, or fixes.
Across its 22 rows, cost, token usage, and human active time remain unknown.
The post-outcome duplicate-prevention index is byte-identical to the current
[`question-history-index.json`](../properties/calibration/question-history-index.json),
SHA-256 `2a40020be4dd99f6e18d55d8d37bf1f09f73a2116ba8431c2d77772705cc7ee7`;
it covers 273 recognized artifacts, 72 asked identities, 571 reserved sites,
and seven unbound records. It is a post-outcome history refresh, not evidence
of pre-outcome eligibility.
