# Cluster conversion waves

**Status:** design · **Scope:** how to turn one distinct corpus *cluster* into
conversion-ledger product rows (`properties_asked` → SAT + ground-truth),
without a taint engine and without proving every extracted site.

**Related:** [`CONTRACTS.md`](CONTRACTS.md) (what a countable property is) ·
[`why.md`](why.md) (two machines + conversion; Heap saturates the compiler,
not this) · [`PLAYBOOK.md`](PLAYBOOK.md) (spike first) ·
[`DYNAMIC.md`](DYNAMIC.md) (interpolated patterns) ·
[`AGENTS.md`](../AGENTS.md) (shapes 1–6) · first application:
[`sweep/openwrt-conversion/plan.md`](../sweep/openwrt-conversion/plan.md)
· latest posix-shell cluster:
[`sweep/claude-code-plugins-conversion/plan.md`](../sweep/claude-code-plugins-conversion/plan.md)
· deterministic sampling implementation:
[`CONVERSION-ALLOCATION.md`](CONVERSION-ALLOCATION.md)

A **cluster** is a source-native unit with one trust map and one device
engine: an OpenWrt feed, an agent-runtime tree (OpenClaw), a distro’s init
scripts. It is not “one GitHub URL” and not “every repo in the mine queue.”

This document is the conversion SOP. Admission ([`sweep/corpus-admission-gate.md`](../sweep/corpus-admission-gate.md))
decides whether to scan. Batch decides encodable fraction. **This** decides
whether anyone asks a real property.

**Adoption policy:** [AUTONOMOUS-CONTRACTS.md](AUTONOMOUS-CONTRACTS.md), authorized
2026-10-13, permits agent adoption with source-bound evidence and a separate
review pass. The executable counting migration is the first implementation
slice in [AUTONOMOUS-CORPUS-PLAN.md](AUTONOMOUS-CORPUS-PLAN.md).

## Why this exists

The factory already scales. Conversion does not:

| Machine | Job | Stop when |
|---|---|---|
| Funnel | mine → score → probe → GO / no-go | compiler novelty (trailing-window novel rate) |
| Prove | compile; reject unsoundly | encodable fraction + mutation coverage |
| Convert | contract + encode + ground-truth + file | **yield on a frozen cluster**, not more sites |

Heap’s-law / singleton novelty saturates the first two. The conversion ledger
saturates the third. Untargeted shape-1/2 synthesis (`synth_max_sites`,
`properties_asked_synthesized`) is compiler smoke. `agent_derived` contracts
require source-bound evidence for product eligibility
([`CONTRACTS.md`](CONTRACTS.md) provenance table).

Site-level taint is **out of architecture** ([`CONTRACTS.md`](CONTRACTS.md)
#475). Do not invent a dataflow engine to rank sites. Rank with cheap
signals, then *read*.

Optimize **conversion yield per hour of reading**, not contracts per site.

## Object: a conversion wave

One wave is one **idiom slice**, not “finish the tree.” Same gates every
time; only the **trust map**, **path vocabulary**, and **current bucket**
change. A large feed (OpenWrt packages, an agent runtime) is a *campaign*
of serial 15/5 waves, not one lifetime cap of 10 contracts.

**Hard caps (load-bearing):**

- Rank **15** survivors for reading **from the current idiom bucket**.
- Adopt **≤5** evidenced contracts per wave (mix below).
- Wave 1 expand: **at most +5** if the stop rule fires, and only on a
  **new idiom** (not another `is_hostname`).
- Further 15/5 waves on the **same cluster** are allowed when the close-out
  names an unused idiom bucket. Still no coverage climb, no parallel
  clusters, no `WAVE_CORPORA` until budgeted.
- Do **not** start cluster N+1 until the current wave is in the ledger
  (including skip reasons). Different dialect or product engine (LuCI JS vs
  packages ash) is a new cluster, not a slice.

**Default mix** (quality/cost compromise):

| Slots | Shape | Why |
|---|---|---|
| 2–3 | 1 alphabet disjointness | cheapest; length-independent; **only if a new alphabet** |
| 1–2 | 3 capture / truncation | highest chance of a real SAT (usrmanage P3) |
| 0–1 | 2 whitelist | only if length is load-bearing; skip if shape 1 covers it |
| 0–1 | 4 / 5 | not wave 1 unless an escaper or version/engine pair is in the **bucket**; later slices same |

A contract is the **correct type** when all four hold:

1. `trust` is `untrusted-input` or `config` (not `internal`).
2. The pattern is **constant**, or escaped-dynamic with a finite table
   ([`DYNAMIC.md`](DYNAMIC.md)). Raw `$var` interpolation is a finding or a
   skip, not a membership proof of the call site.
3. The `guarantee` names a **sink** (“token reaches nft/iptables / the
   shell / a DDNS provider”), not a regex shape (“class contains no space”).
4. The shape is the cheapest one that asks that question.

## Gates

### Gate 0 — admit the cluster (minutes, machine)

Reuse the existing funnel. A probe + decision artifact is enough to start.
Run batch if the cluster is not already compiled.

**Stop here** if the cluster is testdata, a fork of an already-GO parent, or
`deterministic-false` on the repo-level boundary classifier with no escape
hatch. Batch output is a **filter**, not product: encodable vs not,
`call_kind`, path, `usage_mismatch`. Classification rows do not move
`properties_asked`.

Do not add the cluster to `WAVE_CORPORA` in wave 1. Manifest + batch is
enough (anax pattern). Golden-wave membership is a later budget decision.

### Gate 1 — cheap reject (no reading)

From inventory / extractor NDJSON, drop mechanically:

| Drop | Why |
|---|---|
| `tests/`, `testdata`, `*.test.sh`, fixtures | no boundary |
| literal `grep -q "CONST"` / feature-detect | no language to prove |
| pattern is `$2`, `$IPv4_REGEX`, `$URL_PASS`, … | DYNAMIC: classify the *definition* if it is a nearby constant; otherwise skip or file interpolation |
| `call_kind=substitution` with no capture and no charset class | not shape 1 or 3 |
| unencodable | compiler already refused |

Keep a candidate pile. Concentration beats coverage: OpenWrt’s 713 sites
live in 140 packages; four packages hold the interesting density.

A small ranker script is allowed. It must be **deterministic** (same NDJSON
→ same order) and must **not** call Z3. It is not a second mine allocator
and not a taint engine.

### Gate 2 — rank 15, write 5

Score survivors with cheap signals only:

| Points | Signal |
|---|---|
| +2 | path hits the cluster’s boundary vocabulary |
| +2 | `untrusted-input` likely (argv, HTTP body, LuCI/UCI from a web UI, tool-call args) |
| +1 | `config` likely |
| +2 | capture group (`\(...\)` / sed `s/.*/\1/`) → shape 3 candidate |
| +2 | explicit charset / whitelist class → shape 1 candidate |
| +1 | already encodable |
| −2 | `internal` likely (`ip route` parse, feature detect) |
| −3 | interpolated / dynamic |

**Cluster vocabulary** is the only per-cluster input. Write it as one
paragraph (trust map) plus a token list. Examples:

- OpenWrt: `init.d`, `uci`, `nft`, `iptables`, `firewall`, `passwd`, `ddns`,
  `mwan`, `banip`, `adblock`, `pbr`, `hotplug`
- Agent runtime: tool-call args, shell spawn, URL/path allowlists, prompt
  gates, secret redaction

Take the top 15. **Read 50–150 lines around each call site.** That read is
the quality gate (happycow interpolated `re.search` already had `re.escape`;
usrmanage P5 “no `=` in values” was false because audit lines embed
`from=`). Reject if you cannot name a sink in one sentence.

When the scheduler has selected a registered bucket, freeze the eligible site
population, classification evidence, conversion-ledger snapshot, and selection
seed before asking properties. The deterministic allocator described in
[`CONVERSION-ALLOCATION.md`](CONVERSION-ALLOCATION.md) produces the shortlist;
its nominal shares do not override the 15-site review and ≤5-contract wave
caps above.

Adopt at most 5 contracts after that read and the separate evidence review.
Keep agent-authored contracts at `provenance=agent_derived` with their adoption
records. Use `human` only for actual human adoption. Per-contract owner
approval is not required.

Spike in a throwaway script first ([`PLAYBOOK.md`](PLAYBOOK.md)). Then
register and emit the ledger join (below). Each shipped family needs at
least one mutation guard. Run with `--require-contract --require-ground-truth`.
TIMEOUT is not a pass.

### Bind reviews and advance the queue

Build source-bound evidence from the frozen review, shortlist, run context, and
clean source checkout. The builder checks all 15 identities, source pin, and
repository URL, then records bounded source windows and file hashes. If the
shortlist uses a corpus-overlay path, pass its exact root with
`--site-path-prefix`; do not infer aliases from suffixes.

```sh
python3 scripts/build-conversion-review-evidence.py \
  --reviews "$REVIEW_NDJSON" --shortlist "$SHORTLIST_JSON" \
  --run-context "$RUN_CONTEXT_JSON" --checkout "$PINNED_CHECKOUT" \
  --repository-url "$REPOSITORY_URL" --pin "$SOURCE_PIN" \
  --cohort-id "$COHORT_ID" --output "$REVIEW_EVIDENCE_JSON"
```

Add `--site-path-prefix "$OVERLAY_ROOT"` only when the shortlist paths include
a corpus overlay that is absent from the upstream checkout path. Keep a
candidate `unresolved` when sink or serialization evidence is insufficient;
do not convert uncertainty into an out-of-scope skip.

After the queue artifact is emitted for an active wave, use
`scripts/conversion-queue-transition.py` instead of editing queue JSON:

```sh
python3 scripts/conversion-queue-transition.py claim \
  --cluster "$CLUSTER" --site "$SITE" \
  --gate-decision "$GO_DECISION_JSON" \
  --conversion-ledger properties/generated/conversion-ledger.json

python3 scripts/conversion-queue-transition.py contract \
  --cluster "$CLUSTER" --site "$SITE" \
  --contract "$ADOPTED_CONTRACT_JSON" --checkout "$PINNED_CHECKOUT"

python3 scripts/conversion-queue-transition.py skip \
  --cluster "$CLUSTER" --site "$SITE" \
  --reason out_of_scope --note "$EVIDENCE_NOTE"
```

Run one transition per reviewed site. A claim snapshots the GO decision and
conversion ledger and requires their source pin to match the queue row. A
contract transition requires an adopted `agent_derived` contract and rechecks
its source bytes against the pinned checkout. Skip reasons are enumerated and
need an evidence note. All transitions validate wave ID/generation and write
under the shared corpus-event lock; a closed or stale wave cannot accept a
late transition. Leave unresolved rows open, so the wave cannot close until
they receive evidence-backed dispositions.

### Gate 3 — ground-truth the cluster engine

The **product engine** is the one the cluster actually runs. A second
engine (GNU grep/sed on a developer box) is logged when it can disagree;
**agreement is not required**. Disagreement is a recorded delta, not a GT
failure. Absence of the product engine is a hard fail — never GNU-only
collapse.

Harness `ground_truth` callbacks run only on **SAT** witnesses. For
expected-UNSAT shape-3, the fidelity check is **differential fuzz**
(cluster engine vs mirror), not witness replay. Dispatch by tool
(`grep`/`sed`/`awk`); do not clone the usrmanage P3 helper
(`p3_ground_truth_dual` requires GNU∩BusyBox agreement and is sed-only).

Do not ground-truth the rest of the encodable set.

### Stop / expand

After ≤5 asked, record the wave (asked, SAT+GT, skip-with-reason). The
close-out **is the deny-list** for the next wave — efficiency is skips,
not speed. Seams from wave 1 (family, emit, product-engine checker, ledger
glob) are reused; later waves are rank-slice → read → ≤5 → emit.

Time each top-15 site review separately from admission review. Record actual
human stopwatch time under [`metrics-operator-minutes.md`](metrics-operator-minutes.md)
when a person reviews; autonomous review needs its own agent-runtime/usage
series. Include skipped candidates. Do not count clone, batch, solver, or
agent wall time as human operator minutes.

Then pick **exactly one**:

- **Next idiom slice (same cluster)** — unused bucket with a named sink
  (`config` / `untrusted-input`). Rank 15 *in that bucket only*. Same pin
  until reconcile fails. Same JSON `[^"]*` / hostname / IPv4-MAC class as
  a prior ask is **not** a new idiom (one-line skip).
- **Stop this cluster** — yield is flat, leftover keep-list is the same
  idiom, or no unread survivor has a sink. A logged “5 UNSAT / 0 SAT” is
  still a prevalence datapoint. A named DESIGN_TAIL is not a go once the
  close-out says stop.
- **Next cluster** — only after the current wave is in the ledger.
  Parallel clusters duplicate the same learning. New dialect or engine
  (ECMA LuCI vs BusyBox shell) waits until the current cluster’s close-out
  names it.

Wave-1 **Expand +5** still requires SAT reproduced (or the first 5 were
the wrong type). Do not climb toward coverage. Compiler novelty stop
(trailing-window novel rate) is a **different** stop.

## Ledger join (required seam)

Harness registry properties (usrmanage P1–P6) do **not** automatically
increment conversion-ledger `properties_asked`. The ledger joins these
explicit sources:

- scanner NDJSON product kinds on files whose **stem** matches a
  `*_batch_summary.json` (`scripts/conversion-ledger.py`
  `scanner_ndjson_files` — `<corpus>.ndjson` only)
- contracted batch shape-5 rows
- `*_conversion.ndjson` for harness-backed wave outcomes, through the
  fail-closed special case below
- `docs/conversion-upstream.jsonl` for the last mile (filed / fixed / FP)

`openwrt_packages_conversion.ndjson` does **not** match
`openwrt_packages_batch_summary.json` (stems differ). Batch regenerates
`<corpus>.ndjson`. Hand-editing it is not a join. Do **not** broaden the
generic `*.ndjson` scan.

**Required special case (one glob, fail-closed):**

`conversion-ledger.py` includes files named exactly `*_conversion.ndjson`
**in addition to** the existing summary-gated `<corpus>.ndjson` list.
Independent of whether a batch summary exists. Do not glob arbitrary
sidecars (`crs_cross_engine_findings.ndjson` stays excluded).

**Count rule:** a conversion row increments `properties_asked` only when
`product_reportable(entry)` is true **and** `synthesized` is absent/false
**and** its provenance/adoption evidence passes the shared eligibility policy.
`kind` alone is not enough. A bare `agent_derived` draft or contract-less
product kind cannot count. The conversion-ledger uses the shared eligibility
predicate and publishes separate human, autonomous, and machine-pair series.
Mutation guards stay out of this file.

**Required artifact:** `properties/generated/<corpus>_conversion.ndjson`

- Generated from harness `run_one` result records for that wave’s family
  (source of truth = `REGISTRY` + run results). Do not hand-author a
  second copy. A drift test fails on missing, extra, or mismatched rows
  (stable property id + contract digest).
- Each product row must conform to **both** `scanner_finding.schema.json`
  and `property_contract.schema.json`. Require `contract.site`,
  `guarantee`, `input_source`, `trust`, `declared_domain`,
  truthful provenance and, for autonomous adoption, the validated review record.
- Scanner top-level `domain` is required (`product_reportable` reads it).
  Map harness `ground_truth` (string) → scanner `ground_truth_status`; do
  not leave `ground_truth` as a string or `sat_ground_truthed` stays 0.
- `kind` ∈ {`property`, `counterexample_finder`, `bug_demo`}.
- Also require `shape`, `result`, `engine_versions`. `synthesized` absent
  or false.
- Batch must not write this filename.

A fixture test must prove: (a) a `product_reportable` `*_conversion.ndjson`
row increments `properties_asked` with **no** matching batch summary; (b)
a scanner-schema-valid row with an incomplete contract or unadopted
`agent_derived` draft is **rejected** and does not increment the numerator;
(c) an evidenced autonomous adoption counts. A wave that only lands
harness registry entries is invisible to the conversion ledger.

Last mile (file / wont_file / false_positive) still goes through
`docs/conversion-upstream.jsonl` and [`SECURITY.md`](../SECURITY.md).
OpenWrt-class third-party product bugs are not `SECURITY_TOOL_CORPORA`; do
not auto-open public upstream issues. Human approval before filing.

## What a wave must record

| Artifact | Role |
|---|---|
| Cluster trust map (paragraph + vocab tokens) | Gate 2 input |
| Ranked shortlist JSON (top 15 + drop reasons) | reproducible Gate 1–2 |
| ≤5 contracts + spike/registry properties | Gate 2 output |
| `<corpus>_conversion.ndjson` | ledger join |
| Dual-engine GT log (product engine is authoritative; peer is logged) | Gate 3 |
| Wave close-out (asked / skip / **next bucket or stop**) | deny-list for the next slice |

## Non-goals

- Site-level taint / `input_source` on every extractor record (#475).
- Auto-generated shape-3 questions (#478).
- Synthesized shape-1/2 over `synth_max_sites` as product (#479).
- A contract-worthiness allocator (score-v1 is mine admit, not this).
- Re-teaching the compiler; that stop already exists.
- Scanning every package / every feed / every repo in the cluster.
- Adding the cluster to `WAVE_CORPORA` in wave 1.

## Copy-paste for a new cluster

1. One-paragraph trust map + vocab tokens.
2. Probe (if missing) + batch (minutes). Not `WAVE_CORPORA`.
3. Cheap reject + rank 15 with that vocab.
4. Read 15, adopt at most 5 (2–3 shape 1, 1–2 shape 3 where suitable), with
   truthful provenance and source-backed adoption evidence.
5. Record the appropriate human or agent review time/usage and outcome for
   each top-15 candidate, including every skip.
6. Ground-truth on the engine that actually runs.
7. Generate `*_conversion.ndjson` from harness run records; regenerate the
   conversion ledger (special-case glob, not a broader `*.ndjson` scan).
8. Close-out: asked / skip / **next idiom bucket or stop-cluster**.
   Do not start the next cluster yet.
