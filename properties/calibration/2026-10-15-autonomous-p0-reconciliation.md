# Autonomous corpus plan: P0 revision and issue reconciliation

**Observed:** 2026-10-15. **Purpose:** record the live dependency and source
state without replacing the frozen 2026-10-13 baseline in
[`docs/AUTONOMOUS-CORPUS-PLAN.md`](../../docs/AUTONOMOUS-CORPUS-PLAN.md).

## Revision boundary

- The shared checkout is branch `main` at
  `cd0d906a878afca7966efbef44a417d249d38537` (2026-10-08). The live GitHub
  `main` is `fbc7aa623227ca549f3ba35da699a1ff39f27ea4` (2026-10-14), 16
  commits ahead by the GitHub compare API.
- At the start of this reconciliation, the working tree had 49 modified
  tracked paths and 49 untracked paths; this report adds one untracked path.
  Its generated counts are provisional and are not a clean run of either
  exact revision. The 2026-10-13 baseline remains anchored to its stated local
  and remote revisions; current-main reconciliation must wait until the
  existing working changes are integrated safely.
- The latest pipeline status run against this working tree reports: last mine
  drain 10 admits on 2026-10-07; mine queue 100/100; open-GO demand 61;
  admission rate 2 per week; derived backlog 30.5 weeks; needs-human backlog
  18; and no observations in the current weekly survival window (`n=0`).
- The working tree contains 885 gate-decision files: 83 `go`, 45
  `triage-trial`, and 757 `no-go`. Six corpus names have conflicting pins in
  those artifacts: `SMAT`, `ci.docker`, `cpython`, `jython`, `python`, and
  `validator`. The append-only `corpus_events.jsonl` currently has zero rows.
  Treat the counts as working-tree diagnostics, not frozen cohort evidence.

## Clean current-main reproduction

A detached worktree at `fbc7aa623227ca549f3ba35da699a1ff39f27ea4` reproduced
the following. `python3 scripts/pipeline-status.py` reported the last mine
drain as 10 admits on 2026-10-14, a 100/100 mine queue, 61 open-GO clusters,
2 admissions per week, a derived backlog of 30.5 weeks, 18 needs-human items,
and no observations in the current weekly survival window (`n=0`). The
unchanged backlog since the working-tree check is a useful correction to a
simple “ingest more first” sequencing assumption: this snapshot has a full mine
queue and long open-GO backlog while conversion is still unmeasured on a
prospective wave.

The committed conversion ledger reports 41 distinct asked properties, 32
UNSAT, 8 SAT, and 8 ground-truthed SAT. It records one accepted upstream item,
while the third-party-public count is zero. The upstream disposition file has
16 rows, including 2 `private_first` rows. On this revision the conversion
queue health artifact says its queue artifacts are absent and records zero
emitted, claimed, contracted, or skipped items. The current main therefore
has conversion evidence and implemented machinery, with no committed
conversion-queue population or prospective campaign result.
`properties/generated/autonomous_work.jsonl` and the campaign configuration
are also absent from this revision; the current 20-r2 runner scorecard and
campaign bounds belong to the dirty worktree.

The 887 gate-decision files contain 83 `go`, 46 `triage-trial`, and 758
`no-go` decisions, with no invalid JSON or object shapes. Six corpus names
have conflicting pins: `SMAT`, `ci.docker`, `cpython`, `jython`, `python`, and
`validator`. The committed event log has zero rows. The frozen 20-r2 manifest
digest is `cfcfeaa19a37e8704adf84d8979e71a9887ced3a71030fc3572d96c1a8270a78`.

| Current-main artifact | SHA-256 |
|---|---|
| `properties/generated/conversion-ledger.json` | `e7f706a634e133cace34c4657f0b1ecaead856b64469ecc345a752f97e251a0e` |
| `properties/generated/mine-queue.json` | `b3b1e4a337088512f3c2fbf4ea1fc00dc00d6f1a214b48d031b8d97dddc97804` |
| `properties/generated/corpus_events.jsonl` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `docs/conversion-upstream.jsonl` | `c276dd21e0fa2dc262cf036d0b545a06b3804d9e2e872403b899968a3490c6ec` |
| 887 gate-decision files, sorted `filename NUL sha256 LF` stream | `d63805c6a971bb3ae93996b3dc42c9ccb54538e8ae465924dc902bd774c4c025` |
| `properties/calibration/2026-09-12-calibration-20-r2/manifest.json` | `cfcfeaa19a37e8704adf84d8979e71a9887ced3a71030fc3572d96c1a8270a78` |

The worktree campaign file
[`autonomous-corpus-campaign.json`](autonomous-corpus-campaign.json) sets
one active conversion wave, at most 15 ranked reviews and five adopted
contracts per wave, five new proof questions per run, a 30-second solver
timeout, a 300-second local-gate timeout, two source-fetch retries, and zero
solver retries. Parallel walk is disabled, and mine expansion is disabled
while the conversion queue is nonempty. This file is still uncommitted and is
not part of current `main`.

Runtime check in the shared environment: Python 3.15.0, virtualenv
`z3-solver` 5.0.0, Node 26.11.1, BusyBox, and the system Z3 CLI 5.1.0 are
available; `yara-x` is not on `PATH`. Product gates must continue checking
their pinned runtime or binary rather than assuming the host CLI is the
required engine.

## Live issue reconciliation

| Issue | Live state on 2026-10-15 | Reconciliation |
|---|---|---|
| [#448](https://github.com/lucas-albers-lz4/regexproof/issues/448) | Open | The local clone path still defaults to a 300-second per-command limit. The dirty worktree adds an explicit override and a typed retryable timeout that cleans the partial clone and produces no probe facts. No fat-tree timing comparison has been run, so this is reliability handling, not evidence for raising the default or closing the tracking issue. |
| [#550](https://github.com/lucas-albers-lz4/regexproof/issues/550) | Open | The local pipeline reports a full mine queue and 30.5 backlog weeks. `docs/MINE-SETUP.md` keeps score-v1 as the live drain; this queue-pressure snapshot supplies no grounds to switch allocator or increase mine intake while conversion is pending. |
| [#551](https://github.com/lucas-albers-lz4/regexproof/issues/551) | Open; last edited 2026-08-22 | Its current issue text still says human-contract-first. The owner-authorized `autonomous-contracts-v1` policy in this plan supersedes per-contract human adoption for this campaign. Existing hop/disposition, queue, and filing acceptance work remains distinct; this local policy decision does not close the umbrella. |
| [#553](https://github.com/lucas-albers-lz4/regexproof/issues/553) | Open | The umbrella remains open. [#562](https://github.com/lucas-albers-lz4/regexproof/issues/562), its conversion-scheduler implementation wave, is closed. |
| [#623](https://github.com/lucas-albers-lz4/regexproof/issues/623) | Open | Its latest comment says Doberman-Core was implemented in PR #636 at commit `fd7759c`. The commit exists, but has no associated PR; live PR #636 is the calibration-family-scope change. The implementation claim and commit can be retained, but the PR link is incorrect. The issue remains open and its Doberman counts are tied to that historical run, not this plan's 20-r2 scorecard. |
| [#648](https://github.com/lucas-albers-lz4/regexproof/issues/648) | Open | The shared worktree contains the Forge helper-image integration and exact-source regression evidence described by the issue. It is uncommitted here, so the code and local evidence do not establish a reviewed or merged issue completion. |
| [#571](https://github.com/lucas-albers-lz4/regexproof/issues/571) | Open | The issue requests `re.from_ecma2020`, while the repo's normative U9 backend decision drops that harness route. The issue comment identifies mirror expansion or differential parity as alternatives. Keep ECMA `/i` as a separate backend-scope decision; do not count the requested route as an available proof backend. |
| [#563](https://github.com/lucas-albers-lz4/regexproof/issues/563) | Open; marked deferred | Its walk-parallelism work remains conditional on measured walk or clone bottlenecks. No new concurrency is justified by the current queue and admission snapshot. |

The observations above came from local source/artifact reads and read-only
GitHub issue, commit, compare, and pull-request queries. No issue state,
comment, or external disposition was changed. `private_first` remains a
disclosure posture; it is not evidence that a report was transmitted.

## Reproduction and P0 exit status

The current-main report was generated in a detached clean worktree at the
commit above. Reproduce it with `python3 scripts/pipeline-status.py`, parse
`conversion-ledger.json` for its `funnel`, `upstream`, and `queue_health`
objects, count `*_gate_decision.json` files by their `decision` field, and
hash the listed files. The gate-inventory digest sorts filenames
lexicographically and updates SHA-256 with `filename`, a NUL byte, the
lowercase file SHA-256 hex digest, then LF for each file.

P0 baseline capture and dependency reconciliation are complete for this
revision. The exact current-main snapshot, live issue states, policy conflict,
incorrect #623 PR reference, runtime availability, and next runnable work are
recorded above. This does not close the referenced GitHub issues. The next
campaign step is a prospective ranked wave after a clean integration of the
local implementation; use the existing queue pressure as the gate on mine
expansion and leave #563 deferred until a measured walk or clone bottleneck
supports it.
