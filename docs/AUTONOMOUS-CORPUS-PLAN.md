# Parent issue draft: autonomous corpus conversion and product evidence

**Status:** active implementation; campaign and parent close-out remain open.
**Owner/worker:** Luna operates the child work and conversion campaign.
**Policy:** [autonomous-contracts-v1](AUTONOMOUS-CONTRACTS.md).
**Reviewed:** local `HEAD=cd0d906` and GitHub `main=53b9c3455cbde29a3d6695101fe215e21b5fa706`, 2026-10-13.

**Implementation update (2026-10-14; refreshed 2026-10-17):** P1's shared
adoption/counting path is implemented. P2's contract-hash roster and v22
attempt checkpoint are implemented. The current raw exact-pin inventory v5
contains 21,956 sites across the frozen 20-repository cohort's declared
dialect surfaces, with hidden paths included. It removes 79 JavaScript
hashbang false positives found while reviewing Magic JS; 19 repositories are
complete under the registered file selection, and Everclaw remains incomplete
because its six gitlinks were excluded from the scan. The exact-pin follow-up
found no `.gitmodules` file; exact commit lookup now identifies source repos
for four gitlinks while two remain unresolved. An additive scan records 8,361
raw rows from two incomplete child snapshots; those rows are not merged into
v5's 21,956-site total. See the [Everclaw submodule audit](../properties/calibration/2026-10-16-p2-everclaw-submodule-audit/README.md)
and [inventory addendum](../properties/calibration/2026-10-16-p2-everclaw-submodule-inventory-v1/README.md).
Raw rows remain distinct
from reviewed security boundaries and prospective cohort yield. V4 introduced
preservation of `shell_flags`; v5 carries them on all 14,833 POSIX-shell rows.
V3 dropped those selectors, which could default ERE sites to BRE during later compilation. V5
fixes the Bash `[[ ... =~ ... ]]` scanner: compound and continued comparisons
were previously omitted, and 26 existing rows truncated at `]]` inside POSIX
character classes. It removes 26 truncated records and adds 1,277 corrected or
new records, for a net increase of 1,251. See the [v5 inventory record](../properties/calibration/2026-10-16-p2-source-inventory-v5/README.md).
The additive v27 strict retrospective aggregate joins 55 product questions to
exact source identities: 40 UNSAT, 14 ground-truthed SAT, and one timeout. It
records 29 useful local gates, 50 product-engine replays, and 1,762,364
question-attributed differential cases. The 50-question evaluation target is
reached, with 54 decided and one not proven; it is not a success threshold.
The frozen v22 aggregate remains unchanged at 50 questions; v23-v26 remain
preserved as historical checkpoints. Five attempts across three unique questions remain excluded: three
source sites are outside the declared P2 dialect inventory and two Json Editor
attempts use an ambiguous line-only selector. This is compatible evidence,
not new prospective yield. Separately, the cohort-filtered run scorecard has
39 measured runs and 60 proof-question attempts; it tracks useful proofs/gates,
bug discovery, and external outcomes separately. It records 58 decided
attempts, 48 UNSAT guarantees, ten SAT candidates, ten replayed witnesses,
ten reachable violations, and zero confirmed impacts or external outcomes.
The latest P6 wave took 1.4864 seconds in measured phases; source-review and
contract-authoring time, cost, tokens, and human active time are unknown. Across
those runs, the scorecard records 39 local runnable gates, 50 passing mutation
checks, and 3,506,570 differential cases; zero gates have been adopted by
consumers. Logged elapsed time totals 2,265.412 seconds (172.752 phase-sum and
2,092.660 wall-clock); all 39 scorecard rows lack token, cost, and human-active-
time measurements. These cumulative fields are throughput measures, not new
unique P2 yield. The first environment-key encoding attempt timed out during
development; its correction is preserved alongside the successful P6 wave. See
the [current run scorecard](../properties/calibration/2026-10-17-autonomous-tracecat-sandbox-env-equals/scorecard-after-tracecat-sandbox-env-key.json)
and [v27 checkpoint](../properties/calibration/2026-10-17-p2-existing-evidence-20r2-v27/README.md).
The [v11 SAT triage overlay](../properties/calibration/2026-10-16-p2-sat-impact-triage-v11/README.md)
covers all 14 ground-truthed SAT questions: it refutes two historical
security-bypass claims and retains 12 product candidates across ten groups,
including two Aidevops local workflow findings. It records zero confirmed
security impact. P2 now has complete source-review artifacts
for twelve selected repo slices: Malcontent (15 Go sites: 11 skips, two
unresolved, two adopted), Anax (26: 15 skips, 10 unresolved after transport
follow-up, one adopted), AutoAR (34: 28 skips, three unresolved, three
adopted), llm-honeypot-intelligence (16 POSIX-shell sites: 14 skips, two
adopted), Panther (45 Python sites: 44 skips, one adopted), Inhale (3 Python
sites: one unresolved, two adopted), BinaryAlert (one Python site: one skip),
snyk-ls (37 Go sites: 36 skips, one unresolved), json-editor (96 ECMA sites:
94 skips, one unresolved Base64 preview, one adopted), Magic JS (64 ECMA sites:
53 skips, one unresolved email validator, ten adopted Base64URL contracts),
and Doberman Core (104 Python sites: 19 skips, 83 unresolved heuristics, and
two narrowly scoped Codex path-extraction contracts), plus Tracecat (115
Python sites: 78 skips, 29 unresolved, and eight adopted rows). These twelve
slices comprise 556 raw sites: 393 skips, 131 unresolved, and 32 adopted
rows. The complete Tracecat slice includes its previously targeted
environment-key and server-name contracts, the origin-slug contract, two path-
component questions, the RBAC scope-pattern question, and the table-identifier
quote-exclusion question. Two separate targeted Real-Router reviews add two
inventory sites/contracts without claiming complete-slice coverage. These
artifacts cover 558 individually reviewed sites and 33 adopted rows in
total. The v11 checkpoint remains preserved against inventory v2,
v12 against its prior question set, v13 against its prior question set, and
v14 uses corrected inventory v3, and v15 adds two Tracecat questions from
separate targeted source rows.
The llm-honeypot slice also adds two source-bound SAT candidates: RFC 1918 redaction misses
two address blocks in a generated-artifact sync helper, and a Tor rotator can
report success from an AUTHENTICATE reply even when SIGNAL NEWNYM fails. Both
reproduce in exact-source local fixtures; neither establishes that sensitive
data was published or that a deployed Tor rotation failed. A retrospective
Forge integration fixture also
exists; it is not prospective cohort-yield evidence. P3 has source-pin adoption and queue
transition commands, source-authenticated top-15 review evidence, and an
end-to-end isolated active-wave replay on a real pinned Mycelium shortlist
(2 contracts, 13 skips, closed under lock); campaign queue integration remains
open. P4 has its first pre-outcome allocation: the separately frozen Aidevops
Node secret-read slice registered `ecma-plugins`, and the allocator selected
one site from two eligible source predicates. Source review and a narrow
basename contract now drive a separate one-question P6 proof wave: finite
64-variant coverage is UNSAT, its real source mutation reaches the read, and
the Node product gate passes 220 calls across all three supported read tools.
The first P6 attempt recorded an interpreter-path gate failure; the corrected
fresh waves completed. This is a small calibration, not 20-r2/P7 yield;
stratified allocation and a 15-site review wave remain unmeasured.
P5 has the local Forge proof/replay/mutation gate and an Aidevops basename
proof/replay/mutation gate wired into the CI proof job. P6 now has a bounded
serial runner for already-adopted local harness properties; it does not yet
orchestrate ranking, probing, queue transitions, contract creation, or
downstream dispositions. A source-bound Aidevops shell roster also completed
five historical properties through P6 with a pinned BusyBox v1.36.1 replay;
this is runner calibration, not new site review or P7 yield. The exact-pin
Json Editor EnumEditor wave also completed one UNSAT question, a real-source
mutation guard, and a 1,116,985-case Node gate. Its first gate attempt failed
on command quoting and its second run used an ambiguous line anchor; both are
retained. The completed source-matched wave uses the inventory's `column-24`
selector and counts as one unique question. P0's clean current-main status
and issue reconciliation was reproduced at `fbc7aa6` on 2026-10-15; refresh it
after later main changes. A prospective P2 cohort wave, the complete P6
operator loop, and the P8 investment decision remain open. P4's minimum
real-allocation criterion is met by the separate calibration described below;
the first original-cohort 15/5 campaign wave is complete. The retrospective
50-question evaluation target is reached; v24 now contains 52 questions, but
this does not represent 50 new prospective P7 reviews. P3's local source-bound transition workflow is now
exercised end to end; campaign integration remains open. The
autonomous work recorder reads historical v1/v2 rows and writes v3 rows with
explicit `wall_clock` or `phase_sum` elapsed-time bases plus exact reviewed
site and attempted-question identities.
See the
dated implementation record in
[`2026-10-13-autonomous-forge-cli-integration/README.md`](../properties/calibration/2026-10-13-autonomous-forge-cli-integration/README.md)
and [`AUTONOMOUS-CONTRACTS.md`](AUTONOMOUS-CONTRACTS.md).

**P2 checkpoints (2026-10-17; v22 frozen, v23-v27 additive):** v22 remains
unchanged at 50 distinct exact-pin product questions: 35 UNSAT, 14
ground-truthed SAT, and one timeout. Its 50-question target was reached with
49 decided; that is not a success threshold. The later Tracecat
artifact-path-segment question adds one source-matched UNSAT property and a
passing local gate. A second question proves the workspace-sync path-segment
image invariant and adds one more local gate. A third question proves the
RBAC create path excludes non-star `fnmatch` syntax; its exact-source gate
also records that the request model rejects a final line feed accepted by the
standalone Python helper. A fourth post-v22 question proves the table and
column request allowlist excludes double quotes. The exact service rejects
quotes and final line feeds before DDL, so this is a defense-in-depth gate, not
a SQL-injection finding. Additive v26 has 54 questions, 53 decided (39 UNSAT
and 14 SAT), and the same one timeout. V26 records 28 useful local gates, 49
product-engine replays, and 1,758,132 question-attributed differential cases.
A fifth post-v22 question proves that the Tracecat nsjail environment-key
alphabet excludes POSIX's `=` name/value separator, with no length bound. Its
shape-1 proof is UNSAT, the weakened regex admits a ground-truthed
`TRACE=TOKEN` mutation, and its exact-source gate checks 4,232 cases with zero
mismatches. The source also admits a final LF due Python `$` semantics; the
contract does not claim complete POSIX name validity or impact. The v27
aggregate has 55 questions, 54 decided (40 UNSAT and 14 SAT), and the same one
timeout. It records 29 useful local gates, 50 product-engine replays, and
1,762,364 question-attributed differential cases. A first development
encoding timed out and a mutation callback mismatch was corrected; both are
preserved in the [sandbox bundle](../properties/calibration/2026-10-17-autonomous-tracecat-sandbox-env-equals/development-attempts.json).
The latest cohort scorecard has 39 runs, 60 attempts, 58 decided, 48 UNSAT
guarantees, ten SAT candidates/replays, ten reachable local violations, 39
local gate executions, and 3,506,570 differential cases. Its latest P6 phase
sum is 1.4864 seconds. Confirmed security impacts, consumer-adopted gates,
reports, maintainer confirmations, and fixes remain zero; source-review and
contract-authoring time, cost, tokens, and human active time remain unknown.
The measured phase sum excludes source review and contract authoring. Useful
contract-backed proofs/gates, bug discovery, and external outcomes stay
separate measures. See [v22](../properties/calibration/2026-10-16-p2-existing-evidence-20r2-v22/README.md),
[v23](../properties/calibration/2026-10-16-p2-existing-evidence-20r2-v23/README.md),
[v24](../properties/calibration/2026-10-16-p2-existing-evidence-20r2-v24/README.md),
[v25](../properties/calibration/2026-10-16-p2-existing-evidence-20r2-v25/README.md),
[v26](../properties/calibration/2026-10-17-p2-existing-evidence-20r2-v26/README.md),
[v27](../properties/calibration/2026-10-17-p2-existing-evidence-20r2-v27/README.md),
the [artifact path P6 bundle](../properties/calibration/2026-10-16-autonomous-tracecat-artifact-path-segment/README.md),
the [workspace-sync path P6 bundle](../properties/calibration/2026-10-16-autonomous-tracecat-workspace-sync-path-segment/README.md),
the [table-identifier P6 bundle](../properties/calibration/2026-10-17-autonomous-tracecat-table-identifier/README.md),
the [sandbox environment-key P6 bundle](../properties/calibration/2026-10-17-autonomous-tracecat-sandbox-env-equals/README.md),
the [current scorecard](../properties/calibration/2026-10-17-autonomous-tracecat-sandbox-env-equals/scorecard-after-tracecat-sandbox-env-key.json),
and the [v22 scorecard snapshot](../properties/calibration/2026-10-16-p8-v22-audit/scorecard-after-shape6.json).

**P8 audit addendum (2026-10-16):** repository/dialect stratification is now
reported for all 50 questions. Contract provenance is 43 agent-derived and
seven human; the series are selected and unmatched, and the historical
baseline has no comparable exact-pin human denominator or review-time/cost
series. A fresh same-model pass reviewed all 11 rows in the webhook census.
It confirmed the six skips and one unresolved numeric-config site, and found
that the historical SHA and PR guarantees exceeded the scope of their UNSAT
queries. New active contracts narrow those claims to the regex-language
theorems; the old contracts and v22 checkpoint remain preserved. The focused
gate passes three UNSAT properties, four mutation replays, 671 Bash/compiler
comparisons, and 48 integrated helper cases, with zero mismatches; the
unbounded slug-helper inclusion remains not proven. Private evidence packets
now cover the 12 candidate questions across ten groups, while the two
refuted Doberman bypass claims stay excluded. No outside contact or report was
made. The audit rerun took 6.115 seconds; review time, cost, tokens, and human
active time remain unknown. See the [stratification](../properties/calibration/2026-10-16-p2-existing-evidence-20r2-v22/stratification.md),
[audit record](../properties/calibration/2026-10-16-p8-v22-audit/README.md),
[private evidence packets](../properties/calibration/2026-10-16-p8-v22-audit/evidence-packets/README.md),
and [latest scorecard](../properties/calibration/2026-10-16-autonomous-scorecard-20r2-after-p8-audit.json).

**P7 first serial 15/5 wave (2026-10-16):** Aidevops's frozen 20-r2
`pre-dispatch-github-text` bucket completed its first sample: 15 source-bound
reviews, one adopted contract, and 14 evidence-backed skips. The adopted
`cited_file` contract has a Z3 SAT witness (`../oracle.txt`) that the exact
pinned helper resolves to a fixture outside its fresh clone and measures with
`wc -l`. This establishes local path reachability only: no remote helper,
public disclosure, or confirmed security impact was demonstrated. Its product
triage is pending. The wave closed in an isolated queue replay at generation
1; the shared campaign queue was not changed. The first 15/5 wave completed
at the then-current 45/50 checkpoint; the residual review later moved the
retrospective total to 46/50. The initial queue replay used a different
same-pin GO decision file than the frozen allocation; it is preserved as an
initial mismatch, and the corrected replay binds to the allocation's exact GO
decision digest. See the
[wave bundle](../properties/calibration/2026-10-16-autonomous-aidevops-predispatch-github-text-20r2/README.md).

**P7 residual census (2026-10-16):** the complete 14-site complement of that
frozen Aidevops population was reviewed without backfill. It added one
source-backed threshold contract and thirteen evidence-backed skips. The
`threshold=08` counterexample reproduces Bash's invalid-octal comparison path
in the exact pinned helper with local `gh`/`git` stubs; the same five-line
fixture with decimal `threshold=8` takes the intended below-threshold return.
This establishes a local workflow-gate violation only; product triage is
pending and no security impact or external outcome is confirmed. Its isolated
queue replay advanced generation 1 to 2 using the exact GO and ledger
snapshots recorded for the frozen allocation. Together, the two review bundles
cover all 29 bucket identities (two contracts, 27 skips). The strict P2
checkpoint was 46/50 at this residual-census close-out; the follow-on webhook
census below later moved the retrospective aggregate to 50/50, with one
timeout and three previously counted question identities.
See the [residual census](../properties/calibration/2026-10-16-autonomous-aidevops-predispatch-github-text-residual-20r2/README.md).

**P7 follow-on webhook protocol census (2026-10-16):** a source-order census
reviewed all 11 regex records in the exact pinned Aidevops webhook receiver:
four source-backed contracts were adopted, six internal/duplicate rows were
skipped, and one positive-integer helper remains unresolved because its
leading-zero and Bash arithmetic contract is ambiguous. The admission remains
scale-based with `security-boundary=false`; this census claims no remote
vulnerability. Three narrow contract properties are UNSAT with four
ground-truthed SAT mutation guards. Those three question identities already
appeared in v21; the only new question identity in v22 is the whole-slug
inclusion attempt, which timed out. This wave contributes one local runnable
gate and four product-engine mutation replays. Its Bash/compiler gate passes
671 pattern comparisons and 48 integrated helper cases (719 total, zero
mismatches). The whole slug-helper inclusion property timed out at 30 seconds,
so the slug contract's unbounded end-to-end inclusion claim is not proven.
This follow-on source census is not a randomized 15/5 sample and adds no
confirmed security impact, consumer-adopted gate, external report,
maintainer confirmation, or third-party fix. Details and artifacts are in the
[webhook protocol review bundle](../properties/calibration/2026-10-16-autonomous-aidevops-webhook-action-protocol-20r2/review-memo.md)
and [v22 checkpoint](../properties/calibration/2026-10-16-p2-existing-evidence-20r2-v22/README.md).

**P8 evidence review (2026-10-16):** the frozen primary checkpoint is 49 decided
questions, 35 UNSAT guarantees, 24 useful local regression
gates, and zero consumer-adopted gates. The separate bug track has 14
ground-truthed SAT questions. The v11 outcome overlay refutes two historical
security-bypass claims and retains 12 candidates across ten groups; the two
new Aidevops cases establish local path/validation behavior but no security
impact. The run scorecard records nine reachable local violations; this is not
the same denominator as candidate issue groups or a confirmed-impact count.
The external-outcome track remains at zero reports, confirmations, and fixes.
Throughput is 30 scorecard runs and 49 attempts (47 decided); the newest
gate-only phase measured 6.115 seconds. The scorecard's 30 local gate executions
are distinct from the checkpoint's 24 unique gate IDs. The 11-row source census
adopted four contracts, skipped six rows, and left one unresolved; the fresh
audit narrowed two contract scopes and reran the gate. Review duration, tokens,
cost, and human active time are unknown, so those sites are not counted in
measured review throughput. Private evidence packets cover all 12 candidate
questions across ten groups and preserve each group's missing impact evidence;
no outside report was sent. Recommendation: hold expansion to 100 while testing
candidate significance and consumer adoption of useful local gates. The
evidence does not establish downstream security value or make fifty a success
threshold. The owner investment direction remains pending, so P8 is open. See
the [v11 outcome overlay](../properties/calibration/2026-10-16-p2-sat-impact-triage-v11/README.md),
[stratification](../properties/calibration/2026-10-16-p2-existing-evidence-20r2-v22/stratification.md),
[audit and packets](../properties/calibration/2026-10-16-p8-v22-audit/README.md).

**P8 candidate-significance follow-up (2026-10-16):** the llm-honeypot Tor
rotation candidate is now a confirmed local response-handling defect: the
pinned helper accepts an earlier AUTHENTICATE `250 OK` after `SIGNAL NEWNYM`
returns `551`, logs rotation success, and continues. The repository calls
rotation mandatory and says scans stop if the rotator fails; the Tor protocol
defines `5yz` replies as unsuccessful and `551` as an internal error that
prevents the request from being fulfilled. This is stronger than an
unclassified SAT candidate, but the exact evidence is still a local protocol
fixture: no live Tor instance, deployed scan, old-exit persistence, or
security/privacy impact was established. Scorecard counts do not change; the
same question was already counted as a replayed reachable violation. No
outside report was sent. See the [disposition follow-up](../properties/calibration/2026-10-16-p8-v22-audit/tor-newnym-disposition/README.md).

The Real-Router navigation-control P6 singleton completed exact-pin intake,
source review, autonomous contract adoption, locked queue transitions, proof,
source mutation replay, product differential gate, conversion emission, and
close-out. It adds one useful UNSAT proof and one local regression gate, with
zero product SAT candidates or downstream outcomes. This remains a calibration:
the admission GO is scale-based, its security-boundary condition is false,
and no remote attacker input is established. It is not a sampled 15/5 wave.
At that stage, the generic P6 operator loop and remainder of P7 remained open;
the first P7 15-reviewed/up-to-5-adopted wave recorded below has since closed,
and its retrospective checkpoint now reaches fifty. The [singleton bundle](../properties/calibration/2026-10-16-p2-real-router-navigation-source-review/README.md)
records source pins, runner resumptions, exact replay adaptations, and limits.

An additional Tracecat contract is now adopted at the exact frozen-cohort pin
for the origin-to-S3-key slug image. Its proof and product regression gate are
authored, wired into the CI proof job, and passed locally. Tracecat's current
gate decision is `triage-trial`, so the P4 registrar correctly prevents
treating this as a new conversion bucket until the candidate receives a current
`go` decision. See
[`2026-10-14-autonomous-tracecat-origin-slug/README.md`](../properties/calibration/2026-10-14-autonomous-tracecat-origin-slug/README.md).

**Gate update (2026-10-15):** the Tracecat origin-slug proof and exact-pin
product regression gate now pass: UNSAT image property, SAT slash mutation
with real helper replay, 22 source-pattern fuzz cases, and 2,472 composed
helper/key-layout comparisons. This is a useful local gate calibration, not a
current bug or a conversion wave. The run surfaced and fixed a registration
gate mismatch for `call_kind=substitution`; Tracecat's `triage-trial` decision
still blocks P4 bucket registration and campaign counting. Run
`tracecat-origin-gate-20261015-r1` is in
[`properties/generated/autonomous_work.jsonl`](../properties/generated/autonomous_work.jsonl):
2.915 seconds, one decided UNSAT question, one local gate, 2,494 differential
cases, and zero outcomes in either downstream bug or external-report track.
Token usage and cost are null; human active time was not measured.

**Off-cohort Mycelium slice (2026-10-15):** the current `gated:go` source pin
is `4b53dc7629ca3bc88bf5467db481ad2af7130711`, while the frozen 20-r2
manifest pins Mycelium at `d4f01ba6202d50909d1977810d322259482e0b82`. The
roster freezer rejected this mismatch, so this slice is a separate
calibration, not a 20-r2/P7 question. Its release-checksum preflight contract
and local gate pass: short-line property UNSAT, weakened-rule mutation SAT
with exact pinned-helper replay, and 3,814 differential inputs with no
mismatch. P4 registered `mycelium/scripts-bootstrap` and the scheduler chose
it as the next unused bucket. This work also fixed repository-qualified
contract-site path resolution and added an explicit active-wave scheduling
block. Registry and scheduler coverage passed (38 tests). Allocation testing
and the prospective frozen-cohort wave remain open. The 11.929-second,
gate-only run is recorded under `off-cohort-mycelium-current-pin`: one UNSAT
question and useful local gate, zero reproduced/reachable bugs, and zero
external reports, confirmations, or fixes. Contract-review time, tokens,
cost, and human active time are unmeasured; the row is not 20-r2 question
yield. Details:
[`2026-10-15-autonomous-mycelium-script-slice/README.md`](../properties/calibration/2026-10-15-autonomous-mycelium-script-slice/README.md).

**Exact-pin Mycelium 20-r2 calibration (2026-10-15):** the d4f frozen source
contains the same documented release preflight. I regenerated the `scripts/`
inventory from that clean pin, preserving literal BRE source patterns,
reviewed 15 candidates, adopted the rank-11 contract, and froze a one-question
roster before solving. Its exact-pin gate passed: UNSAT property, SAT mutation
with pinned-helper replay, and 3,814 differential inputs. Gate-only execution
was 11.877 seconds; it is logged under the 20-r2 manifest and has zero
bug-discovery and external-report/confirmation/fix outcomes. The gate decision
and P4 bucket registration are still pinned to 4b53, so the scheduler does not
admit the d4f contract as a P7 wave. The d4f and 4b53 source files are
byte-identical, so these runs are one site/guarantee lineage and must not be
presented as two distinct campaign questions. This one-question roster is P2
evidence, not a completed 15/5 wave. See
[`2026-10-15-autonomous-mycelium-20r2-slice/README.md`](../properties/calibration/2026-10-15-autonomous-mycelium-20r2-slice/README.md).

**P3 source-bound review and queue transitions (2026-10-15):** added
`scripts/build-conversion-review-evidence.py` to bind all 15 ranked Mycelium
review decisions to 51-line source windows, pinned file hashes, and frozen
review/shortlist/run-context digests. It requires the explicit path-prefix
mapping from the corpus overlay to the pinned upstream checkout. The output
confirms 1 adopted, 12 skipped, and 2 unresolved candidates; see
[`review-evidence.json`](../properties/calibration/2026-10-15-autonomous-mycelium-script-slice/review-evidence.json).
Added `scripts/conversion-queue-transition.py` for claims tied to the exact GO
decision and ledger snapshot, contract transitions replayed against the pinned
checkout, and evidence-noted top-15 skips. State changes share the corpus event
lock and reject stale wave generations. The focused transition/source-evidence
suite passes (47 tests) and Ruff passes. This is off-cohort calibration; the
real campaign queue was not changed. At this first pass ranks 1 and 4 remained
unresolved, and P3 remained open pending a transition-wave exercise.

**P3 Mycelium parser follow-up (2026-10-15):** the original review and its
evidence digest remain unchanged. A second source-bound review resolves rank 1
as a narrow adopted diagnostic contract and rank 4 as its duplicate downstream
symptom, leaving two adopted and thirteen skipped candidates in the revised
top-15. A harmless systemd 255.4 user-manager unit reproduced the exact
`ExecStart` serialization: a literal semicolon in an argv path is unescaped,
the pinned `[^;]*` capture drops a later `--insecure-no-verify` flag, and the
dependent `--repo-ref` parse is empty. The pinned updater independently
refuses the bypass under systemd and non-TTY execution, so this is one
reachable diagnostic defect and zero confirmed security-boundary violations.
The adopted property and counterexample/mutation replay gate pass locally;
the off-cohort record has one local evidence gate, one replayed reachable
diagnostic defect, zero confirmed security impact, and zero external reports,
confirmations, or fixes. It is excluded from 20-r2/P7 yield. This follow-up
still did not exercise the queue transition CLI in a prospective active wave,
so P3 remained open at that point. A follow-on isolated active-wave replay
then used the actual Mycelium GO decision, ledger snapshot, exact-pin top-15,
both adopted source-bound contracts, and the transition CLI for every
contract/skip decision. All 17 transitions succeeded; two sites were
contracted, twelve were skipped out of scope, one duplicate was skipped, and
the temporary event log closed the wave from generation 0 to 1. The artifact
is [`queue-transition-replay.json`](../properties/calibration/2026-10-15-autonomous-mycelium-script-slice/queue-transition-replay.json).
This satisfies P3's source-backed transition workflow for an off-cohort local
calibration. It changed no campaign queue state and does not count toward
P7. P3's local workflow validation is complete; campaign integration and
cohort yield remain open. Details and digests are in the
[`Mycelium script-slice calibration`](../properties/calibration/2026-10-15-autonomous-mycelium-script-slice/README.md).

**P6 source-validation preflight (2026-10-15):** after the d4f proof, I
revised its descriptive source anchor from `SHA256SUMS preflight` to the
literal `sums_n` on line 60. The guarantee, trust/domain, source pin, and
source bytes did not change; the original contract and pre-outcome roster are
preserved, and a separate post-proof roster exists only for runner
compatibility. The P6 dry-run verified the cohort, exact clean checkout,
adopted contract digest, and gate coverage. It ran no proof or local gate and
wrote no wave state. The 4b53-vs-d4f admission/registration mismatch still
blocks an actual campaign wave, so this closes no P4, P6, or P7 milestone.
An exact d4f admission probe now records 1,034 regex sites (1,023 POSIX shell,
11 RE2) with zero extraction errors. It remains a draft with no decision or
condition dispositions; the only GO decision and scheduler registration are
still at 4b53. See
[`admission-probe-d4f.json`](../properties/calibration/2026-10-15-autonomous-mycelium-20r2-slice/admission-probe-d4f.json).
The scorecard snapshot after the AutoAR phase-key run had 13 run records and 17
proof attempts: 16 decided (13 UNSAT and three SAT), plus one undecided
attempt. It records 14 local gate executions, 15 passing mutation checks, and
252,590 differential cases. All three SAT witnesses were replayed and marked
reachable; security impact is confirmed for zero. Consumer adoption,
third-party reports, maintainer confirmations, and fixes remain zero. The
separate strict P2 checkpoint counts 18 unique exact-pin questions and nine
unique useful local gates; the denominators differ because the agent scorecard
counts timed executions and retries while the P2 checkpoint deduplicates
product-question identities. Across timed rows, elapsed is 1,361.346 wall
seconds plus 102.468 seconds of phase sums; tokens, cost, and human active
time remain unknown. The snapshot is
[`2026-10-15-autonomous-scorecard-20r2-after-autoar-phasekey.json`](../properties/calibration/2026-10-15-autonomous-scorecard-20r2-after-autoar-phasekey.json),
bound to work-log SHA-256
`b2c754f10a55d01e862c10dd09e1815222a64967c614eec9f3b4f5caa430d173`.

**P4 history-index compatibility repair (2026-10-15):** refreshing after the
new AutoAR result exposed an existing legacy Aidevops queue-transition summary
that the history index rejected. I updated the parser to reserve only its
explicit `contracted_sites` and not interpret phase labels as proof attempts.
The rebuilt post-outcome index covers 102 recognized sources, 61 asked sites,
119 reserved sites, and 7 still-unresolved unbound records. It now records the
AutoAR question for future duplicate checks. The original pre-outcome index
remains preserved; the refreshed index is not allocation evidence. Details:
[`CONVERSION-ALLOCATION.md`](CONVERSION-ALLOCATION.md).

**Malcontent exact-pin P4/P6 calibration (2026-10-15):** the 20-r2
`chainguard-dev/malcontent` pin has a rule explicitly tied to Git's
CVE-2025-48384 advisory. More ingestion is not the immediate bottleneck for
this corpus: the existing pinned GO record already covers 19,578 probe sites
(15 RE2 and 19,563 YARA, including third-party rules), and the complete local
rules batch has 7,922 extracted entries, 5,540 encodable entries, and 2,382
triage entries. Its generated report has five `usage_mismatch` scanner
findings plus four generic planned templates; those templates are not
contract-backed product results. The GO admission artifact also records two
unclassified parse-error rows and an escape-hatch decision. These source and
batch facts are in [`malcontent_gate_decision.json`](../properties/generated/malcontent_gate_decision.json),
[`malcontent_batch_summary.json`](../properties/generated/malcontent_batch_summary.json),
[`malcontent_encodable_fraction.json`](../properties/generated/malcontent_encodable_fraction.json),
and [`malcontent.ndjson`](../properties/generated/malcontent.ndjson).

Those five scanner rows are a pre-fix snapshot, not five product findings.
Pinned-source review showed three end-dollar reports were false positives:
the sources contain escaped literal dollars, including two YARA string
definitions. I fixed the mechanical detector to honor escape parity and added
a regression test. The remaining two rows are actual EOF anchors that the
source comments explain; the rule's intended use is behavior-only here and
the solver probes remain `unknown`. The historical NDJSON is unchanged; the
row-by-row refutations and residual dispositions are recorded in
[`scanner-triage-review.json`](../properties/calibration/2026-10-15-autonomous-malcontent-git-cr-20r2/scanner-triage-review.json).

I reviewed all seven regex sites in the CVE-2025-48384 rule and adopted one
narrow terminal-class contract; sibling and composition sites remain deferred
or unresolved. A source-text scan of explicit CVE metadata found eight inline
regex declarations across two YARA files (seven in this rule); it is not a
canonical AST inventory, but confirms that this CVE idiom cannot supply a
15-site shortlist alone. The registered `git-crlf-smuggling` bucket matches
the frozen GO pin and is selected by the scheduler. The P6 runner then
completed one frozen-roster question: UNSAT for the declared ASCII-byte
property, SAT for the weakened-class mutation with pinned YARA-X replay, and
139 full-rule fixtures with zero mismatches. The P6 artifacts are in
[`2026-10-15-autonomous-malcontent-git-cr-20r2/`](../properties/calibration/2026-10-15-autonomous-malcontent-git-cr-20r2/);
the exact YARA-X archive and binary digests are checked in the CI proof job.
This establishes one useful contract-backed gate and one successful local
runner wave. It does not establish a ranked 15-site sample, a 15/5 wave, a
current product bug, or any external outcome. The timed runner row counts one
question, one UNSAT guarantee, one local gate, one passing mutation check, and
139 differential cases; review/adoption happened outside that interval.
Anchored EOF probes that returned `unknown` remain unresolved. Full-rule
fixtures are synthetic ASCII examples, and no YARA wide-string or vulnerable
Git execution is claimed.

**AutoAR exact-pin P2/P6 calibration (2026-10-15):** AutoAR's frozen-cohort
pin and its GO decision match at
`01cd447ad3b1acfed7e0680596c2c74458a4cf06`. An earlier cached directory had a
misleading name and a different `HEAD`; it was excluded and a clean exact-pin
checkout was fetched. Caller review traced scan-result rows from the results
API through `findings-rows.js` into `tbody.innerHTML`. I adopted a narrow
contract for the shared `esc` helper's HTML text-node path; it does not claim
JavaScript, URL, CSS, arbitrary attribute, or all-path XSS safety. The
per-codepoint image property is UNSAT, and changing the pinned `<` entity to
literal `<` gives SAT and reproduces through Node against the mutated source.
The exact helper matches an independent character-wise image on 68,500 cases
with zero mismatches. Local replay used Node 26.11.1; CI pins Node 22.

The first P6 state exposed an emitter gap after source and product checks
passed: the new property had no canonical shape mapping. That unresolved
attempt remains in [`p6-wave/`](../properties/calibration/2026-10-15-autonomous-autoar-html-text-escape-20r2/p6-wave/).
I added the shape-4 mapping, froze a fresh state, and completed one UNSAT
question with its source mutation and product gate in
[`p6-wave-r2/`](../properties/calibration/2026-10-15-autonomous-autoar-html-text-escape-20r2/p6-wave-r2/).
The r1 recovery reran the mutation and local gate without retrying its
question. The two r1 gate executions and one r2 execution are counted
separately; P6 r2 is the successful run. The roster was frozen after an
initial standalone solver check, so this is retrospective calibration, not a
prospective cohort-yield sample. This helper slice alone does not provide
the required ranked top-15 shortlist; P4 allocation remains open. No current
product bug or reachable violation was found, and no external report,
confirmation, or fix exists for this slice. Details and exact scope are in
[`AutoAR calibration notes`](../properties/calibration/2026-10-15-autonomous-autoar-html-text-escape-20r2/README.md).

Suggested issue labels: `plan`, `tracking`, `scanner-pipeline`. File this body
as the parent and use P0–P8 as child issue titles/scopes; link existing work
where the ownership table says reuse. The policy decision is already authorized.

## Objective and corrections to the working premise

Build a resumable workflow that turns real source sites into independently
specified contracts, faithful proofs/counterexamples, and runnable regression
gates. Measure useful gates first, then reproduced bugs, third-party
confirmation, and fixes. Luna adopts contracts under the authorized policy
without per-contract human approval.

Keep three linked outcome tracks visible: contract-backed proofs and useful
regression gates; reproduced, reachable product bugs; and external report,
confirmation, and fix outcomes. A confirmed external bug can lead to a new
proof/gate and can contribute additional bug evidence, so preserve the links
between those records instead of collapsing them into one conversion count.

The repository already has real corpus data. More ingestion tests compiler
coverage, but product effectiveness depends on completed contract work and its
outcomes. Increasing candidate intake while conversion is stalled grows the
backlog. Automation must increase completed, trustworthy conversions per unit
of effort; generating more contracts or SATs alone is not success.

An UNSAT theorem establishes a guarantee only in its declared domain. A SAT
replayed against a regex is not necessarily reachable through the product or
a security defect. A useful gate can prevent a later regression even when no
current bug is found. These are related outcomes, not interchangeable counts.

## Evidence baseline

The following global counts are from the pinned GitHub-main revision above;
the frozen-cohort figures come from its committed calibration artifacts.

| Measure | Observed state | Consequence |
|---|---|---|
| Extracted / encodable sites | 149,212 / 96,030 | Corpus supply already exists. |
| Global product questions / UNSAT / SAT / replayed SAT | 41 / 32 / 8 / 8 | Most extracted sites never become questions; decided outcomes do not cover every asked row. |
| Accepted upstream fixes | 1, own-code | Not evidence of third-party remediation yield. |
| Recorded public third-party acceptance | 0 | No measured public third-party success rate yet. |
| Current mine ledger | 1,463 candidates; 610 mined, 64 GO, 41 triage-trial, 748 NO-GO | Ledger status is not authoritative processing completion; reconcile with gate artifacts. |
| Latest mine attempt | [Oct 13 successful run](https://github.com/lucas-albers-lz4/regexproof/actions/runs/38453277927) | Oct 8's failure is historical; successful workflow status does not establish conversion throughput. |
| Completed calibration | 20-r2, 20 exact-pin repositories, zero processing failures | All four measured dialect families remain productive by the current novelty rule. |
| Embedded calibration product evidence | 0 properties; no PR4 checkpoint | Global product rows have not been attached to a complete frozen-cohort evaluation. |
| Committed conversion schedule | Aug 24 snapshot: 80 clusters, zero selected buckets | Not a fresh operational measurement. Code has five cluster-specific progression entries; new-cluster registration needs a path. |
| Contract queue / review timing | No local committed queue directory or conversion-review stopwatch series | Shipped tools need to be exercised; absence of artifacts is not absence of implementation. |

Local uncommitted work reports 42 global questions after a forge-cli replay
addition. That is provisional and excluded from this baseline. Other dirty
files cover #448, #551, and #571. Reconcile those changes in their owned work
before regenerating shared artifacts. Preserve the baseline revision and
artifact digests so later mine commits cannot silently change the comparison.

Sources: [throughput plan](THROUGHPUT-PLAN.md), [pipeline](PIPELINE.md),
[saturation protocol](SATURATION.md), [20-r2 close-out](../properties/calibration/2026-09-12-calibration-20-r2/closeout.md),
[conversion ledger](../properties/generated/conversion-ledger.json),
[scheduler](../scripts/conversion-scheduler.py), and
[curated dispositions](conversion-upstream.jsonl).

## Reuse and issue ownership

Reuse the probe/cache/batch state machines, corpus lock, conversion queue,
ranker, harness, emitters, and checkpoint. [#553](https://github.com/lucas-albers-lz4/regexproof/issues/553)
records that the #550/#551 implementation waves landed. Do not rebuild those
components because their design umbrellas remain open.

| Existing issue | Treatment in this parent |
|---|---|
| [#551](https://github.com/lucas-albers-lz4/regexproof/issues/551) conversion | Audit remaining acceptance gaps; extend policy and integration, preserve landed work. |
| [#550](https://github.com/lucas-albers-lz4/regexproof/issues/550) admission | Reuse batch/cache; preserve its shipped shared gate and escape protocol. Changing review provenance requires a new comparable measurement series. |
| [#623](https://github.com/lucas-albers-lz4/regexproof/issues/623) measurement | Own the frozen experiment and versioned checkpoint extension here; link the resulting evidence back. |
| [#648](https://github.com/lucas-albers-lz4/regexproof/issues/648) forge-cli replay | First real vertical slice if its pending implementation passes review; do not create a duplicate replay ticket. |
| [#448](https://github.com/lucas-albers-lz4/regexproof/issues/448) clone timeouts | Land/reconcile the existing fix; timeouts remain ungated/retryable, not auto-NO-GO. |
| [#563](https://github.com/lucas-albers-lz4/regexproof/issues/563) parallel walk | Keep conditional on measured walk/clone bottlenecks. Start with serial conversion. |
| [#571](https://github.com/lucas-albers-lz4/regexproof/issues/571) ECMA route | Separate backend scope decision; the issue's `re.from_ecma2020` request conflicts with normative U9 in `docs/BACKENDS.md`. |

## Child work, ordered by dependency

Create one child per slice below. The listed commands and modules are existing
entry points unless explicitly described as new. Each implementation child
ships a reviewable PR, relevant checks, and an evidence close-out; each campaign
child ships pinned manifests and wave artifacts. Estimates should be refined
from the first measured slice rather than assumed from prior review counts.

### P0 — Freeze the baseline and reconcile pending work

**Depends:** none.

- Capture source revision, generated-artifact revisions/digests, current gate
  inventory, queue pressure, processing events, runtime availability, and issue
  status. Distinguish working-tree output from committed results.
- Audit the remaining #551/#623 acceptance gaps against source and landed PRs.
  Reconcile #448/#648 owned changes before shared-artifact regeneration.
- Check the actual meanings of curated `private_first` and filing dates against
  evidence. Report disclosure intent, transmitted reports, maintainer response,
  and fixes separately; preserve historical rows rather than inventing contact.
- Record resource limits in the campaign configuration: one active conversion
  wave, existing clone/cache limits, bounded subprocess/solver calls, maximum
  work per run, and retry budget. Budget-exhausted work is resumable.

**Done when:** a dated baseline report and dependency map reproduce the counts
from exact revisions and identify the next runnable child. Unknown cost or
human-time values are explicit nulls.

**P0 reconciliation update (2026-10-15):** the live issue map and clean
current-main artifact boundary are recorded in
[`2026-10-15-autonomous-p0-reconciliation.md`](../properties/calibration/2026-10-15-autonomous-p0-reconciliation.md).
The audit reproduced the status inventory at `fbc7aa6`, records the working
checkout's 16-commit divergence and uncommitted changes, and caught an
incorrect PR #636 link in #623's latest Doberman comment. P0 is complete for
that revision; subsequent main changes require a new dated snapshot. The
current 30.5-week backlog and missing conversion queue artifacts make a
prospective conversion wave the next campaign milestone. #571's requested
backend route conflicts with the normative U9 decision.

### P1 — Implement autonomous contract eligibility consistently

**Depends:** P0. **Critical path.**

- Define a strict adoption-record schema under `autonomous-contracts-v1` and a
  shared eligibility predicate. Retain `agent_derived` provenance; require
  adoption evidence and source/contract digest binding before counting it.
- Apply the same rule in `harness/contract.py`, conversion emission, ledger
  counting, queue adoption validation, saturation observations, and the PR4
  checkpoint adapter/validator. Inspect every path and test their agreement.
- Version report/checkpoint schemas as needed; continue reading historical
  human-only artifacts without rewriting provenance or historic totals.
  Expose human, autonomous, and permitted machine-pair series explicitly.
- Extend timing/usage records for agents. Keep agent execution/cost separate
  from the existing human active-minute metric and admission baseline.
- Reject missing evidence, edited source/context, stale pins, duplicate
  identities, stub adoption, synthesized smoke, and result-driven contract
  edits without revision records. Test actual rejection paths, not just enums.

**Done when:** one evidenced autonomous fixture counts consistently across all
reports, a bare `agent_derived` fixture does not, historical reports still
validate, and no workflow requires a person to adopt a routine contract.

### P2 — Assemble a frozen product roster and reuse compatible evidence

**Depends:** P0; executable autonomous counting depends on P1.

- Start with `2026-09-12-calibration-20-r2` and retain its exact pins and digest.
  Independently enumerate product candidate identities from the source
  inventory, before solver outcomes are used to choose survivors.
- Import existing contracts/run records only where repository, pin, site,
  question, domain, provenance, and evidence match. Identify missing replay or
  mutation evidence explicitly. Previously completed questions are not new yield.
- Freeze reviewed/adopted identities and their coverage manifest independently
  of the result rows being checked. Record every ranked review and skip reason.
- Maintain an attempt roster containing encoding failures, timeout/unknown,
  missing engines, unresolved reachability, and behavioral-only questions.
  Current PR4 supports decided SAT/UNSAT rows; P1/P2 must define the versioned
  completeness report so unresolved work cannot disappear from evaluation.

**Done when:** the original cohort can be evaluated without silently changing
membership or dropping failed questions, and exact-pin historical evidence is
distinguished from newly executed work.

**P2 inventory binding audit (2026-10-15):** the frozen 20-r2 cohort has a
matching generated scanner inventory for each of its 20 repositories (26,702
regex rows total; 20,984 marked encodable). Those are scanner rows, not
security-boundary product candidates. The generated inventories have no
source-pin field or extraction attestation tied to the cohort manifest, so
none is independently bound to its cohort pin. Only 7 of the 20 exact-pin
checkouts are currently available locally. Per-repository digests, row counts,
and checkout availability are recorded in
[`2026-10-15-p2-cohort-inventory-audit.json`](../properties/calibration/2026-10-15-p2-cohort-inventory-audit.json).
P2 remains open until product candidates are re-enumerated from exact pinned
sources and the independent coverage roster includes reviewed, skipped,
unsupported, and attempted questions.

**Everclaw submodule metadata correction (2026-10-15):** the exact root pin
contains six gitlinks but no `.gitmodules` file. The earlier v1 note calling
the file malformed was incorrect. The gitlink commit IDs are recorded, but
there is no complete path-to-URL mapping to reproduce the six child checkouts;
do not add child rows or infer remote URLs. The v5 root inventory and counts
are unchanged. See the [submodule audit](../properties/calibration/2026-10-16-p2-everclaw-submodule-audit/README.md).
The 2026-10-16 follow-up below partially resolves this: four exact commit
sources are now checked out and scanned in an additive, incomplete inventory.

**Everclaw partial Gitlink recovery (2026-10-16):** exact commit lookup
identified public sources for four of the six root Gitlinks. The additive ECMA
scan found 8,361 raw rows in two snapshots of `morpheus-agent`, but both contain
15 nested Gitlinks and remain incomplete; the other two verified child trees
have no registered ECMA sites. Two root Gitlinks remain unresolved. The v5
total remains 21,956 and still marks Everclaw incomplete; the addendum rows are
unreviewed and are not unique product yield. See the
[submodule audit](../properties/calibration/2026-10-16-p2-everclaw-submodule-audit/README.md)
and [inventory addendum](../properties/calibration/2026-10-16-p2-everclaw-submodule-inventory-v1/README.md).

**Everclaw unresolved Gitlink follow-up (2026-10-16):** the public
`profbernardoj/everclaw-fork` repository is a plausible candidate for the
`603157...` Gitlink, but its exact commit endpoint returned 422 and exact-SHA
fetch returned `not our ref`; public exact-commit search returned no result.
No `everclaw-template` source mapping was found for `f161a75...` either. These
checks do not prove original URLs, so both Gitlinks remain unresolved and no
rows are added. See the [follow-up evidence](../properties/calibration/2026-10-16-p2-everclaw-unresolved-followup-v1/README.md).

**P2 identity accounting extension (2026-10-15):** new autonomous run rows use
schema v3 and include `work_items` with each reviewed site and its attempted
question IDs. The recorder checks those identities against the row's reviewed
and attempted counts; the history index records reviewed sites as reserved and
attempted questions as asked. Existing v1/v2 aggregate rows remain readable,
but their seven nonzero run records have no site identities and remain
unresolved. The index blocks those matching pins until the missing identities
are evidenced; no identities were inferred from aggregate metrics.

**Aidevops shell contract reuse (2026-10-15):** five source-bound autonomous
contract revisions now bind the historical Aidevops shell-hook questions to
the exact frozen pin. They preserve each earlier guarantee, input, trust, and
domain; source-site anchors and adoption records add the exact source binding.
The five-entry roster completed a P6 proof wave, but its questions come from
the existing 15-reviewed/5-contract close-out, so this adds no new review or
P7 yield. See the
[Aidevops shell calibration](../properties/calibration/2026-10-15-autonomous-aidevops-posix-shell-20r2/README.md).

**P2 exact-pin source-site inventory v1 (2026-10-15, superseded):** prepared clean local
checkouts for all 20 frozen repository pins and ran the registered
`dogfood.extract_repo(include_hidden=True)` extractor by each cohort member's
declared dialect family. An initial 10,231-row pass inherited the extractor's
default hidden-path exclusion; it omitted Aidevops's `.agents/` product tree
(only 820 Aidevops sites instead of the 11,330 shell sites recorded by its
exact-pin corpus scan). That pass is superseded. The corrected deterministic
output contains 20,779 raw site records: 19 repositories completed under the
registered file selection, and Everclaw has 464 root-repository sites with six
gitlinks explicitly excluded. The v1 note incorrectly called Everclaw's
`.gitmodules` malformed. A later exact-pin audit found no `.gitmodules` file
in the pinned tree; the six gitlinks have no complete path-to-URL mapping
there, so this member remains incomplete until the sources can be bound to
their recorded commit IDs. The frozen cohort was not reduced. The other 19 members have no
oversized files or submodule omissions. Hidden source paths are included;
`.git`, `node_modules`, virtualenvs, `dist`, `build`, `.tox`, coverage, HTML
coverage, Next.js, and Python cache directories remain excluded by the registered
walker. Every row carries the
cohort and manifest digest, repository pin and tree OID, registered regex ID,
source path, worktree byte hash, Git blob OID, and `review_status=unreviewed`.
Counts are still zero for reviewed sites, adopted contracts, attempted
questions, and solver outcomes. This is a pinned source inventory, not 20,779
product candidates: the 26,702 historical scanner rows remain a distinct
artifact, and this inventory does not claim a security boundary or trust class.

Artifacts:
[`inventory.json`](../properties/calibration/2026-10-15-p2-source-inventory/inventory.json)
(SHA-256 `9d9c36714b8084cf37084fe60279524802a4e21689201b5e4628eea50359a717`)
and [`sites.ndjson`](../properties/calibration/2026-10-15-p2-source-inventory/sites.ndjson)
(SHA-256 `a1996ab9b4a90314aa69b8476c913199bb0de6b4299ccd696035976b121799ff`).
The superseded default-hidden-filter pass and its digests are recorded in
[`superseded-pass.json`](../properties/calibration/2026-10-15-p2-source-inventory/superseded-pass.json).
Reproduce with the same clean checkouts using:

```sh
python scripts/freeze-p2-source-inventory.py \\
  --manifest properties/calibration/2026-09-12-calibration-20-r2/manifest.json \\
  --checkout-root /tmp/regexproof-pinned-sources \\
  --out-dir properties/calibration/2026-10-15-p2-source-inventory
```

The command exits 1 while any frozen repository is incomplete, after atomically
writing per-repository status and available site records. P2 remains open for
boundary review decisions, an independent reviewed/adopted coverage roster,
and complete attempted-question dispositions.

**P2 exact-pin source-site inventory v2 (2026-10-15):** while reviewing Anax,
I found that the registered Go extractor recognized `regexp.Compile` and
`MustCompile`, but omitted static literal patterns passed directly to
`regexp.Match`, `MatchString`, and `MatchReader`. The extractor now records
those literal calls and leaves computed patterns for the separate
dynamic-pattern classification workflow. Re-freezing the exact pins adds five
source sites: one AutoAR production `MatchString`, two Anax production
`MatchString` calls, and two test-only Snyk calls. The deterministic inventory
now has 20,784 rows (19 complete repositories; Everclaw still has six
unavailable submodules). Its NDJSON digest is
`381c0ca4d80c8f050b5446f378f6d95bd9b54ec83c02a48e5072a10beaabc73c`.
The previous v1 inventory remains preserved. See the
[v2 inventory note](../properties/calibration/2026-10-15-p2-source-inventory-v2/README.md)
and the
[Anax 26-site review](../properties/calibration/2026-10-15-p2-anax-source-review/README.md).

**P2 exact-pin source inventory v3 (2026-10-15):** the Magic JS review found
that the ECMA scanner read a leading `#!/usr/bin/env …` hashbang as the
apparent `/usr/` regex. The scanner now skips an initial BOM and hashbang
before scanning tokens. Re-freezing removes 79 false rows from Magic JS,
Gigachad GRC, Everclaw, and Real Router, leaving 20,705 extracted sites.
Nineteen repositories are complete; Everclaw remains incomplete because six
submodules are unavailable. The v2 inventory and its exact review history
remain preserved. See the
[v3 inventory note](../properties/calibration/2026-10-15-p2-source-inventory-v3/README.md)
and [Magic JS source review](../properties/calibration/2026-10-15-p2-magic-js-source-review/README.md).

**P2 retrospective evidence checkpoint v1 (2026-10-15, superseded):** added
[`build-p2-evidence-checkpoint.py`](../scripts/build-p2-evidence-checkpoint.py)
and its reproducible output at
[`2026-10-15-p2-existing-evidence-20r2/`](../properties/calibration/2026-10-15-p2-existing-evidence-20r2/).
The builder verifies the frozen manifest and raw-inventory digests, joins
historical checkpoint questions to a unique exact-pin source file and line,
and preserves all contributing checkpoint digests. Fourteen distinct
questions match the inventory: thirteen UNSAT and one replayed/reachable SAT
with `pending_product_triage`; the report counts five useful local gates and
9,729 differential-case executions. It records three excluded attempts rather
than folding them into the declared-dialect denominator: two AutoAR HTML
escaper attempts (including the earlier error) and one Malcontent YARA rule.
The strict report was initially 14/50 (shortfall 36), with no consumer-adopted
gate, no external report, no maintainer confirmation, and no fix. This snapshot
is retrospective evidence reuse, not a prospective 15/5 allocation or a claim
that the remaining source surface cannot supply 50 questions.

**P2 Malcontent source review and Markdown replays (2026-10-15):** all 15 raw
Go-regex inventory rows at the exact Malcontent pin have now received a second
source review: 11 skips, 2 unresolved candidates, and 2 adopted contracts.
The unresolved rows are rule-removal/detection integrity and temporary
report-path privacy. Each contract digest was frozen in a one-question roster
before its solver run. Both SAT witnesses were replayed through YARA-X 1.19.0,
Malcontent's `report.Generate`, and the pinned Markdown renderer. The author
metadata path emits an attacker-chosen HTTPS link after the generated author
link; the threat-hunting description path emits a raw HTTPS link plus an
unescaped table delimiter. These runs establish reachable Markdown structure
for their concrete witnesses. They do not confirm downstream consumer impact;
both dispositions remain `pending_product_triage`. No external report was
sent.

The first P6 runner attempt exposed a missing canonical shape entry after the
real-engine gate and solver had returned SAT. Shape 3 is now registered for
this counterexample finder, and the runner has a recovery path that accepts
only the matching same-run gate artifact and exact source/roster/contract
digests. It recovered the already emitted SAT result without a solver retry;
the failed serialization is retained in the run record, and the exact runner
solver timing is marked unknown rather than inferred. The local gate passed
its mutation guard and 2,034 Go RE2/Z3 differential cases with zero
mismatches. The second description-to-Markdown gate reproduced the raw link
and table delimiter, passed its mutation guard, and recorded 33,209 Go
RE2/Z3 differential cases with zero mismatches. Its bounded P6 wave completed
the proof and local gate but correctly remains `needs_review` for the SAT
disposition.

At this stage, the v1 strict aggregate joined 16 questions: 13 UNSAT and 3 replayed
SAT, all pending product triage. It records seven useful local gates, eleven
product-engine replays, and 44,972 differential executions. Consumer-adopted
gates, confirmed security impacts, external reports, maintainer confirmations,
and fixes are all zero. The checkpoint is 16/50 (shortfall 34). The complete
member review and replay artifacts are in
[`2026-10-15-p2-malcontent-source-review/`](../properties/calibration/2026-10-15-p2-malcontent-source-review/README.md),
[`2026-10-15-autonomous-malcontent-author-markdown-20r2/`](../properties/calibration/2026-10-15-autonomous-malcontent-author-markdown-20r2/README.md),
[`2026-10-15-autonomous-malcontent-description-markdown-20r2/`](../properties/calibration/2026-10-15-autonomous-malcontent-description-markdown-20r2/README.md),
and the refreshed
[`2026-10-15-p2-existing-evidence-20r2/`](../properties/calibration/2026-10-15-p2-existing-evidence-20r2/README.md).
P2 remains open for review coverage and complete question/disposition
accounting across the other cohort members, plus the incomplete Everclaw
submodules; the retrospective result does not satisfy a prospective 15/5 wave.

**P2 strict checkpoint v2 and Anax review (2026-10-15):** the Go extractor
repair added five static literal `regexp.Match*` sites, including the Anax
validator. A source-bound review covers all 26 Anax literal sites. A raw HTTP
replay and Go 1.25.7 parser-source check resolve the two CORS newline sites as
skips, leaving 15 skips, 10 unresolved, and one adopted narrow organization
deny-list contract. That
contract completed a one-question P6 proof/gate wave, adding one UNSAT
question to the strict retrospective aggregate. The refreshed result is 17
questions (14 UNSAT, three replayed SAT pending product triage), eight useful
local gates, 12 product-engine replays, and 45,659 differential cases; the
shortfall to 50 is 33. The builder now detects prior aggregate output through
its sidecar manifest and does not re-ingest it as a source run. The earlier
16-question aggregate remains preserved. See
[`2026-10-15-p2-existing-evidence-20r2-v2/`](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v2/)
and the [Anax source review](../properties/calibration/2026-10-15-p2-anax-source-review/README.md).

**P2/P6 AutoAR phase-key follow-up and v3 checkpoint (2026-10-15):** a
second-pass source review covers all 34 Go-regex sites in AutoAR: 28 skips,
three unresolved target-scope questions, and three adopted contracts (two
existing endpoint questions plus the phase-log component). The new contract
was roster-frozen before its solver run. The Shape-1 punctuation property is
UNSAT; its weakened-class mutation is SAT and the exact Go 1.25.7 helper
reproduces a path escape. The local gate checked 662 mixed inputs with zero
mismatches. Two failed P6 gate attempts are preserved; the final resume passed
the mutation and product gate without retrying its solver question. The v3
strict aggregate now has 18 exact questions (15 UNSAT, three replayed SAT
pending triage), nine useful gates, 13 product-engine replays, and 46,321
differential cases. It is 32 questions short of 50. The refreshed history
index has 155 sources, 69 asked sites, 125 reserved sites, and seven
unresolved unbound legacy records. V1 and v2 aggregates remain preserved. See
the [AutoAR review](../properties/calibration/2026-10-15-p2-autoar-source-review/README.md),
[phase-key P6 evidence](../properties/calibration/2026-10-15-autonomous-autoar-phasekey-20r2/README.md),
and [v3 aggregate](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v3/README.md).

**P2 v4 retrospective import (2026-10-15):** the aggregate builder now also
joins canonical conversion NDJSON rows to the frozen source inventory, while
recording exact duplicates as corroboration instead of counting them twice.
This recovers two older Doberman-Core human-contract questions already in the
conversion ledger: both SAT witnesses have persisted reproduced product
replays, but neither artifact records a reusable local regression gate. Six
Forge CLI rows are exact duplicates and only corroborate existing checkpoint
questions. The strict aggregate is now 20 questions (15 UNSAT, five replayed
SAT pending product triage), 15 product-engine replays, nine useful local
gates, and 46,321 differential cases; the shortfall to 50 is 30. The two
historical Doberman questions are compatible evidence, not new prospective
yield, and do not change the agent-only scorecard. See the
[v4 aggregate and evidence limits](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v4/README.md).

**P2 v5 retrospective import and Doberman source review (2026-10-15):** the
new Doberman-Core question is bound to the frozen Windows-supported source
pin and its adopted contract. The source regex misses backslash-separated
Windows paths to `.npmrc` and `credentials`; the real pinned Python rule and
ObjectiveGuardrail both reproduce `PASS` for those targets. The formal
counterexample is SAT with a real-`re` replay, and the mutation guard is SAT.
The local gate also replays slash-separated controls as `AUTH`, refutes
`.env.local` because the separate `.env.*` protected-path glob covers it, and
checks a separator-fix sensitivity control. It did not run on native Windows,
so native path canonicalization and product impact remain open. The candidate
is `pending_product_triage`; no external report was sent. Its proof, gate, and
conversion artifacts are in
[`2026-10-15-autonomous-doberman-win-secret-path-20r2/`](../properties/calibration/2026-10-15-autonomous-doberman-win-secret-path-20r2/).

The strict v5 retrospective checkpoint now joins 21 unique questions: 15
UNSAT and six replayed SAT pending product triage, with 10 useful local gates,
16 product-engine replays, and 46,321 differential cases. Provenance is 14
autonomous and seven historical human contracts; three attempts remain
excluded from the declared-dialect denominator. The shortfall to 50 is 29.
Two older Doberman human-contract questions remain in the aggregate without
reusable local-gate claims; the new Doberman question is the third canonical
row. Six Forge CLI rows remain duplicates used only as corroboration. The
refreshed question-history index has 168 sources, 73 asked sites, 128
reserved sites, and seven unbound legacy records. These are retrospective
counts, not prospective yield. The agent-only scorecard has 14 measured runs
and 18 proof attempts (17 decided: 13 UNSAT and four SAT executions), 15 local
gates, 16 mutation checks, and 252,590 differential cases. The Doberman
proof/gate replay adds one execution retry, not a second unique P2 question;
its measured interval is 0.811 seconds. Full review/adoption time, tokens,
cost, and human active time remain unknown. Security impact remains confirmed
for zero candidates; reports, maintainer confirmations, and fixes remain zero.
The scorecard row's fourth SAT execution is not evidence of a fourth distinct
root cause. The refreshed history index is
[`question-history-index.json`](../properties/calibration/question-history-index.json)
and the scorecard snapshot is
[`after-doberman-proof-gate`](../properties/calibration/2026-10-15-autonomous-scorecard-20r2-after-doberman-proof-gate.json).
See the
[v5 aggregate and evidence limits](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v5/README.md).

**P2 v6 retrospective checkpoint (2026-10-15):** the Xibo one-site
calibration adds one autonomous UNSAT contract question and one useful local
gate. The refreshed aggregate has 22 questions (16 UNSAT and six replayed
SAT pending product triage), 11 useful local gates, 17 product-engine
replays, and 47,328 differential cases. Provenance is 15 autonomous and
seven historical human contracts; the 50-question shortfall is 28. The Xibo
question is retrospective evidence, not prospective cohort yield. The
refreshed history index covers 176 sources, 74 asked sites, 129 reserved
sites, and seven unbound legacy records. The agent-only scorecard has 15 runs
and 19 proof attempts (18 decided: 14 UNSAT and four SAT executions), 16
local gates, 17 mutations, and 253,597 differential cases. Xibo's measured
proof/gate phase is 1.073 seconds; review/adoption time, tokens, cost, and
human active time remain unknown. This run is bound to autonomous work-log
SHA-256 `2d2eb9aaee21029efab7d526acd5a7a0418b394e3f587b5b2fedc38f14d75eb2`.
Security impact remains confirmed for zero
candidates; third-party reports, maintainer confirmations, and fixes remain
zero. See the
[v6 aggregate and limits](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v6/README.md),
[Xibo gate evidence](../properties/calibration/2026-10-15-autonomous-xibo-csrf-cookie-20r2/README.md),
and [agent scorecard](../properties/calibration/2026-10-15-autonomous-scorecard-20r2-after-xibo-csrf.json).

**P2 SAT impact triage (2026-10-15):** source review closed the first
downstream pass for all six v6 SAT questions. The two historical Doberman
terminal-LF claims are now `false_positive` in the curated disposition source:
the root-target helper strips the LF, and a `_DISK_WIPE` match blocks the
command. Four questions remain plausible product issues in three families:
the Doberman Windows secret-path classifier, AutoAR cross-origin loopback
fetch, and Malcontent's two metadata-to-Markdown paths. Security impact is
confirmed for zero; no external report was sent, no maintainer confirmed an
issue, no third-party fix exists, and no consumer-adopted gate exists. The
private-first labels record a disclosure posture only. Machine-readable
details, exact question joins, evidence links, and refuted claims are in the
[SAT triage overlay](../properties/calibration/2026-10-15-p2-sat-impact-triage/README.md).
The history index was refreshed after these dispositions: 176 sources, 75
asked sites, 129 reserved sites, and seven unbound records.

**P2 llm-honeypot-intelligence review and v7 checkpoint (2026-10-15):** the
exact pin `65624396e263074bb8cb2e049f9a9ec6215ea5c1` contributed 16 raw
POSIX-shell sites to a full source pass: 14 evidence-backed skips, no
unresolved sites, and two adopted contracts. The sanitizer contract covers
all canonical RFC 1918 addresses in generated files eligible for sync; the
pinned `192.168/16` expression leaves `10/8` and `172.16/12` representatives
unchanged. A second contract covers Tor control reply sequencing: an earlier
`250 OK` from AUTHENTICATE makes the pinned helper report success even if the
subsequent SIGNAL NEWNYM reply is `551 Internal error`. Z3 witnesses for both
questions replayed against exact pinned shell functions. The regression gate
exhaustively checked all 65,536 canonical `192.168/16` addresses, 65,541
sanitizer cases total, and four Tor response cases; both mutation guards
reproduced. The P6 runner captured two SAT attempts with verified source pin,
passing mutation and local gates, then correctly persisted `needs_review`
because candidate disposition is unresolved. It is retrospective
calibration, not a 15/5 allocation or prospective yield.

**P2 Panther review and v8 retrospective checkpoint (2026-10-15):** the
exact pin `0cd0f5bd33469c9f03b578fe0104a4ebf23d9f4a` contributed 45 raw Python
regex sites: 44 evidence-backed skips and one adopted contract. The contract
tests a staged `secrets.py` path against the pre-commit review helper. Its
policy expectation is inferred from a separate slash-command review policy;
that command is not wired to the hook. The exact helper selected the synthetic
path and included its sentinel in the locally built prompt. A nine-path local
gate matched Python `re.search` and helper selection, and an empty-regex
mutation let `password.secret.py` through. No real secret, Claude process, or
external request was involved. P6 verified source, mutation, and gate, then
recorded `needs_review` because impact disposition is unresolved. See the
[Panther source review](../properties/calibration/2026-10-15-p2-panther-source-review/README.md).

The refreshed v8 aggregate has 25 exact-pin questions (16 UNSAT, nine
ground-truthed SAT), 13 useful local gates, 20 product-engine replays, and
112,882 differential cases; 25/50 leaves a shortfall of 25. The strict report
still counts all nine SAT rows as pending product triage. The separate
[v8 impact overlay](../properties/calibration/2026-10-15-p2-sat-impact-triage-v8/README.md)
refutes two historical Doberman claims and retains seven candidate questions
across six issue families. Across five reviewed repo slices, 136 raw sites
comprise 112 skips, 15 unresolved reviews, and nine adopted contracts.
Confirmed security impact, consumer-adopted gates, external reports,
maintainer confirmations, and third-party fixes remain zero. The aggregate
and its limits are in the
[v8 checkpoint](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v8/README.md).

The duplicate-prevention index coalesces exact GitHub repo/pin/site identities
across repo-ID and corpus-name labels. Its latest snapshot covers 217
recognized source artifacts, 58 asked source identities, 293 reserved sites,
and seven unbound records; SHA-256
`7b9db4a152232ec69aed85e62200b16fea5f05f6189ed6bbd590dd34d5e3e874`. The
former 75 asked count included repeated cluster aliases. See
[`question-history-index.json`](../properties/calibration/question-history-index.json)
and the [allocation history](CONVERSION-ALLOCATION.md); the frozen dated copy
is [`2026-10-15-question-history-index-after-snyk-ls.json`](../properties/calibration/2026-10-15-question-history-index-after-snyk-ls.json).

**P2 Inhale review and v9 retrospective checkpoint (2026-10-15):** the
exact-pin review covers three Python sites: two adopted output-path contracts
and one unresolved recursive-link scope candidate. The README promises that
`-o OUTDIR` stores scraped files there; exact local helper replays show that
two parent segments in a `-u`/`-l` file URL or `-r` directory URL write
synthetic bytes outside that output root. A six-case gate matches both pinned
save helpers to Python's path model, and a widened substitution mutation
flips the one-parent control from inside to outside. These are config-trust
candidates because the examples come from operator-supplied URLs; no
untrusted caller or downstream impact is established. The runner verified
the source, witnesses, mutation, and gate and correctly recorded
`needs_review`. Separately, a shared-hostname-prefix link produces a
cross-origin fetch for a root URL without a trailing slash, but the repo does
not state a same-origin contract, so that finding remains unresolved and is
not counted as a product question. See the
[Inhale review bundle](../properties/calibration/2026-10-15-p2-inhale-source-review/README.md).

The BinaryAlert review skips its sole Python site because it extracts a
repository-owned version literal for Sphinx documentation metadata. The
Snyk Language Server review covers 37 Go sites: 36 skips and one unresolved
hover-formatting candidate. Its `<br>` replacement is described as
sanitization, but this source does not establish whether supported clients
render the resulting Markdown as HTML or require a separate markup boundary.
It remains unresolved and outside the product-question count. See the
[BinaryAlert review](../properties/calibration/2026-10-15-p2-binaryalert-source-review/README.md)
and [Snyk review](../properties/calibration/2026-10-15-p2-snyk-ls-source-review/README.md).

The strict v9 checkpoint has 27 exact-pin questions (16 UNSAT, eleven
ground-truthed SAT), 14 useful local gates, 22 product-engine replays, and
112,888 differential cases. Its 50-question shortfall is 23. The separate
[v9 impact overlay](../properties/calibration/2026-10-15-p2-sat-impact-triage-v9/README.md)
retains nine candidates across seven issue families, including one Inhale
output-path family; it refutes the same two Doberman claims. Confirmed impact,
consumer-adopted gates, external reports, maintainer confirmations, and fixes
remain zero. The eight complete P2 source-review slices cover 177 raw sites:
149 skips, 17 unresolved reviews, and 11 adopted contracts. The frozen
post-outcome history index covers 217 source artifacts, 58 asked identities,
293 reserved sites, and seven unbound records; SHA-256
`7b9db4a152232ec69aed85e62200b16fea5f05f6189ed6bbd590dd34d5e3e874`. Review
coverage over the rest of the cohort, Everclaw submodules, and dispositions
for unresolved sites remain open.

**P2 Json Editor review and v11 checkpoint (2026-10-15):** the exact-pin
review covers all 96 inventoried ECMA regex sites: 94 evidence-backed skips,
one unresolved Base64-preview capture, and one adopted composite EnumEditor
string-escaping question. The editor routes schema enum string leaves through
three ordered replacements before assigning the result to
`display_area.innerHTML`. One contract and gate cover that composite chain;
the supporting `<` and `>` regex literals on the same line are not counted as
separate product questions. The first P6 run kept its UNSAT/mutation evidence
but failed on a test-command quoting error; the second gate passed but its
`:replace` source anchor collided with three inventory sites. The source
identity now uses the frozen inventory's exact `column-24` selector, supported
by both the P6 runner and retrospective P2 matcher. The third run passed the
property, real-source `<` mutation, and 1,116,985-case Node differential gate.
The strict v11 checkpoint has 28 questions (17 UNSAT, eleven ground-truthed
SAT), 15 useful local gates, 23 product replays, and 1,229,873 differential
cases; the 50-question shortfall is 22. Its separate bug-candidate and
external-outcome tracks are unchanged: nine candidate SAT questions across
seven families, zero confirmed impact, and zero reports, maintainer
confirmations, or fixes. The Base64 preview concern remains unresolved because
source documents neither an untrusted initial-value path nor a separate
safe-rendering guarantee. See the
[Json Editor review and P6 artifacts](../properties/calibration/2026-10-15-p2-json-editor-source-review/README.md)
and [v11 checkpoint](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v11/README.md).

The duplicate-prevention index was then refreshed at
[`2026-10-15-question-history-index-after-json-editor.json`](../properties/calibration/2026-10-15-question-history-index-after-json-editor.json),
byte-identical to the index at that refresh, SHA-256
`c7a18561c80e0e57530564817a84885d113d48e43d0e547d4f963081e1ca9e39`.
It covers 243 recognized artifacts, 60 asked identities, 391 reserved sites,
and seven unbound records. The freezer omits the retained P6
`roster-input.json` array; its canonical frozen `roster.json` remains indexed.
This is a post-outcome duplicate-prevention refresh, not allocation evidence.

**P2 Magic JS review and v12 checkpoint (2026-10-15):** inventory v3 corrects
the hashbang false positives and supplies the 64 exact ECMA sites reviewed for
`magiclabs/magic-js`. The review adopts ten narrowly scoped Base64URL output
contracts (three PKCE, five WebAuthn, and two DPoP encoders), skips 53 sites,
and leaves the wallet-kit email validator unresolved because the pinned source
does not establish accepted syntax or authoritative server enforcement. Ten
per-codepoint image properties prove UNSAT; one weakened plus mapping has a
ground-truthed SAT witness. Two serial P6 waves of five contracts each passed
the exact-pin source check, mutation guard, and Node product gate. The exact
Node run reports zero mismatches across 481,034 unique question-attributed
comparisons. Because each capped wave invoked the shared ten-question gate,
the two executions performed 962,068 comparisons in total; v12 deduplicates
them by question. The contracts cover output formatting only, not verifier
entropy, authentication, signature validity, or server acceptance. There is
no new SAT product candidate or confirmed impact. The v12 checkpoint has 38
questions (27 UNSAT, 11 SAT), 16 useful local gates, 33 product replays, and
1,710,907 differential cases; the shortfall to 50 is 12. See the
[Magic JS review/P6 bundle](../properties/calibration/2026-10-15-p2-magic-js-source-review/README.md),
[v12 checkpoint](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v12/README.md),
and [inventory v3 correction](../properties/calibration/2026-10-15-p2-source-inventory-v3/README.md).

The post-outcome duplicate-prevention index was refreshed at
[`2026-10-15-question-history-index-after-magic-js.json`](../properties/calibration/2026-10-15-question-history-index-after-magic-js.json),
byte-identical to the index at that refresh, SHA-256
`ce17b4a627a4517ac2c2f37cec74242b09fbced4f44bf31c579d218a6a75a71c`.
It covers 261 recognized source artifacts, 70 asked identities, 465 reserved
sites, and seven unbound records. This post-outcome refresh prevents future
duplicate questions; it is not pre-outcome allocation evidence.

**Doberman Core P2 review, Codex path gate, and v13 checkpoint (2026-10-15):**
the exact-pin review covers 104 Python regex sites: 19 skips, 83 unresolved
security-facing heuristics, and two adopted Codex apply_patch path questions.
Each theorem is limited to a one-character printable-ASCII destination; the
exact pinned AST replay separately checks 514 directive cases for Add, Update,
Delete, and Move-to extraction, leading whitespace, CRLF, and a mixed
multi-directive patch. Both questions are UNSAT, the weakened Delete mutation
is SAT with exact-helper reproduction, and the product gate has zero mismatches.
This does not prove unbounded path completeness or protected-path rule
correctness. The full Doberman module was not imported because Pydantic is
missing in the local environment; the gate executed only the exact regex and
adapter helper AST with the standard library. The gate is now wired into the
`proof` CI job, alongside the normal harness run; the hosted CI result for this
change has not yet been observed. P6 measured a 0.9681-second phase sum for two questions, one local gate, one mutation check, and 514
differential cases; review-authoring time and token/cost usage are unknown.
No new SAT candidate or downstream outcome arose. The v13 checkpoint has 40
questions (29 UNSAT, 11 SAT), 17 useful gates, 35 product replays, and
1,711,421 differential cases, leaving a shortfall of 10 to 50. See the
[Doberman review/P6 bundle](../properties/calibration/2026-10-15-p2-doberman-source-review/README.md)
and [v13 checkpoint](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v13/README.md).
The post-outcome duplicate-prevention index was byte-identical to the current index at that refresh:
[`question-history-index.json`](../properties/calibration/question-history-index.json),
SHA-256 `2a40020be4dd99f6e18d55d8d37bf1f09f73a2116ba8431c2d77772705cc7ee7`;
it covers 273 recognized artifacts, 72 asked identities, 571 reserved sites,
and seven unbound records. This refresh prevents later duplicate questions;
it is not pre-outcome allocation evidence.

**Tracecat MCP validator questions and v15 checkpoint (2026-10-16):**
a targeted P2 source review covered exactly one of 115 Tracecat inventory rows.
The pinned `validate_mcp_env_key` comment and validation error declare the
ASCII grammar `[A-Za-z_][A-Za-z0-9_]*`, while `re.match` with `$` accepts a key
ending in one final line feed. The full stdio configuration validator accepts
the witness, and a local POSIX child receives it. POSIX permits
implementation-specific environment names, so this is recorded as a mismatch
with Tracecat's declared grammar; no command injection, privilege escalation,
or downstream security impact is claimed. The adopted agent-derived contract
has a Z3 SAT witness with exact-source replay; its strict-anchor mutation
rejects the witness, and a mutation guard confirms restoring `$` reintroduces
acceptance. The local exact-source product gate compared 1,442 deterministic
cases with an independent model and found zero mismatches. P6 measured a
0.6948-second phase sum for one attempted/decided SAT question, one replayed
reachable configuration-validation gap, one local gate, one mutation check,
and 1,442 differential cases; the run status is `needs_review` pending product
triage. Timed source review/contract authoring is excluded; tokens, cost, and
human active time are unknown. No security impact or external outcome is
confirmed. The gate is wired into the proof CI job; its hosted CI result has
not been observed. The v14 checkpoint has 41 exact-pin questions (29 UNSAT,
12 SAT), 18 useful gates, 36 product replays, and 1,712,863 differential
cases, leaving a shortfall of nine.

A second targeted P2 review covered the distinct server-name regex row at
`mcp_validation.py:267`; the validator's declared alphabet is alphanumeric,
hyphen, and underscore. The contract asks only whether the accepted alphabet
can contain `/` or `\`. Z3 proved the alphabet-level property UNSAT without a
length bound. A mutation adding `/` is SAT and ground-truthed through the
complete `validate_mcp_command_config` path. The exact pinned CPython gate
compared 714 deterministic values with the independent model and found zero
mismatches. Its P6 wave completed in a 0.6676-second phase sum with one local
gate and one mutation check. This positive invariant does not establish path
traversal or security impact. It is a second targeted site review, not a full
Tracecat review. Both gates are wired into the proof CI job; their hosted CI
results have not been observed.

Together, v15 has 42 exact-pin questions (30 UNSAT, 12 SAT), 19 useful gates,
37 product replays, and 1,713,577 differential cases, leaving a shortfall of
eight. The v10 SAT overlay remains applicable because v15 adds only an UNSAT
question; the Tracecat terminal-LF candidate remains unconfirmed pending
downstream consequence evidence. See the [environment-key bundle](../properties/calibration/2026-10-15-autonomous-tracecat-mcp-env-key/README.md),
[server-name bundle](../properties/calibration/2026-10-16-autonomous-tracecat-server-name/README.md),
[server-name source review](../properties/calibration/2026-10-16-p2-tracecat-server-name-review/README.md),
[v15 checkpoint](../properties/calibration/2026-10-16-p2-existing-evidence-20r2-v15/README.md),
and [v10 SAT impact triage](../properties/calibration/2026-10-16-p2-sat-impact-triage-v10/README.md).
The post-outcome [question-history index snapshot](../properties/calibration/2026-10-16-question-history-index-after-server-name.json)
was byte-identical to the current index at that refresh, SHA-256
`64500ff147c039dd6ef344170a20c1d068833deb75f737e9ab4b6faa7fe213cd`; it
covers 295 recognized artifacts, 74 asked identities, 573 reserved sites, and
seven unbound records. This refresh prevents re-asking both Tracecat questions;
it is post-outcome history, not pre-outcome allocation evidence.

**Tracecat complete P2 source review (expanded 2026-10-17):** the exact-pin source
review covers all 115 Tracecat rows in inventory v5. The source-bound review
records 78 skips, 29 unresolved rows, and eight adopted rows: the MCP stdio
environment-key and server-name contracts, origin-slug and RBAC scope-pattern
contracts, two path-component questions, the table-identifier quote-exclusion
contract, and the sandbox executor environment-key separator contract. The
mount-only artifact helper and workspace-sync normalizer each add one useful
local proof and gate; the RBAC scope-pattern proof adds a third; table
identifier and sandbox environment-key add two more. The table proof and new
sandbox proof join the v27 aggregate without a current bug finding or confirmed
impact. The RBAC and table request schemas accept a final line feed in their
standalone Python patterns, but their exact service paths reject it before the
sensitive sink. The table request-model and service gate excludes double
quotes, reproduces a weakened-allowlist mutation, and compares 2,227 inputs
without mismatches; it makes no SQL-injection or impact claim. The sandbox key
proof uses shape-1 alphabet disjointness to show that all characters admitted
by its source classes and Python's possible final LF exclude `=`. Its
`TRACE=TOKEN` mutation reproduces after weakening; the exact-source gate checks
4,232 inputs with zero mismatches. The full source pattern is not fully POSIX
conforming because `.match()` with `$` accepts one final LF; the contract only
covers the POSIX name/value separator. Its measured P6 phase sum was 1.4864
seconds, excluding source review and contract authoring. The initial
whole-string query timeout and mutation-callback mismatch are documented in
the bundle and are not hidden as a second unique product question. The two
token-scope UUID patterns are source-backed skips: they populate claimed
identity sets, while authorization resolves database roles and memberships;
Watchtower also intersects ambiguous org claims with memberships after the
issuer’s single-org check. The stdio MCP tool-name filter is a compatibility
skip, the separate agent sandbox environment-key validator has no untrusted
source at this pin, and the email regex composes with EmailMessage and call
ordering rather than providing a standalone security guarantee. These four
dispositions add no contract or product question. The remaining 29 unresolved
rows include other live authorization and credential paths, template/Git
parsers, sandbox configuration, log/error redaction, workspace-sync
resource-reference parsing, and export-root enforcement; these stay outside
product-question counts until their complete input-to-sink contracts are
evidenced. The pass is by the same model as the first inventory triage, not
independent third-party review. The builder bound 52 files and all 115
identities to the exact commit. See the
[review bundle](../properties/calibration/2026-10-16-p2-tracecat-full-source-review/README.md),
[artifact path P6 bundle](../properties/calibration/2026-10-16-autonomous-tracecat-artifact-path-segment/README.md),
[workspace-sync path P6 bundle](../properties/calibration/2026-10-16-autonomous-tracecat-workspace-sync-path-segment/README.md),
[RBAC scope-pattern P6 bundle](../properties/calibration/2026-10-16-autonomous-tracecat-rbac-scope-pattern/README.md),
[table-identifier P6 bundle](../properties/calibration/2026-10-17-autonomous-tracecat-table-identifier/README.md),
and [sandbox environment-key P6 bundle](../properties/calibration/2026-10-17-autonomous-tracecat-sandbox-env-equals/README.md).

**Question-history index refresh after workspace-sync (2026-10-16):** both new
path-component questions were added to the index at that refresh and its
dated snapshot. The refresh exposed that `roster-contracts.json` is a JSON array, while the index
reader only accepted object-form frozen rosters. The reader now accepts both
that pre-freeze contract-row array and the canonical object-form roster. That
snapshot recognizes 412 sources, 86 asked site identities, 814 reserved
sites, and seven unbound records; it includes both Tracecat path questions. This
is duplicate-prevention bookkeeping, not a new question or product outcome.
See the [dated index](../properties/calibration/2026-10-16-question-history-index-after-tracecat-workspace-sync-path-segment.json).

**Question-history index refresh after RBAC scope work (2026-10-16):** the
RBAC question was reserved in the index at that refresh and its dated snapshot. The
index recognizes 426 sources, 87 asked site identities, 815 reserved sites,
and seven unbound records. This is duplicate-prevention bookkeeping, not a
new product question beyond the P6/v25 result. See the
[dated index](../properties/calibration/2026-10-16-question-history-index-after-tracecat-rbac-scope-pattern.json).

**Question-history index refresh after table identifier work (2026-10-17):**
the table-name question is now reserved in the current index and dated
snapshot. The index recognizes 441 sources, 88 asked site identities, 816
reserved sites, and seven unbound records. This is duplicate-prevention
bookkeeping, not a new product question beyond the P6/v26 result. See the
[dated index](../properties/calibration/2026-10-17-question-history-index-after-tracecat-table-identifier.json).


**Question-history index refresh after sandbox environment-key work (2026-10-17):**
the no-equals contract question is reserved in the current index and its dated
snapshot. The index recognizes 457 sources, 89 asked identities, 817 reserved
sites, and seven unbound records. After recording the P6 run and rebuilding
the Tracecat review evidence, the canonical index was refreshed and now matches
this dated snapshot byte-for-byte. This post-outcome refresh prevents duplicate
allocation; it is not pre-outcome allocation evidence. See the
[dated index](../properties/calibration/2026-10-17-question-history-index-after-tracecat-sandbox-env-equals.json).

**Real-Router route-segment invariant and v16 checkpoint (2026-10-16):** a
targeted review covered the exact `SAFE_SEGMENT_PATTERN` inventory row at the
frozen Real-Router pin, not the repository's other regex rows. The constant
documents JavaScript `\\w` as ASCII letters, digits, and underscore, and adds
dot and hyphen. The shared validator applies it to all three exported route
segment testers; the package invariant table declares the same allowed
alphabet. The source-backed contract is scoped to application route/API
configuration and asserts no remote attacker input or security impact. The
shape-1 alphabet proof is UNSAT without a length bound. Adding `/` to a
source-mutated class is SAT; the exact source mutation rejects `/` before the
mutation and all three pinned helpers accept it after the mutation. A local
Node 26.11.1 gate compared 17,027 deterministic values per helper (51,081
helper comparisons) with zero mismatches, including every ASCII code point,
every two-character ASCII string, 512 seeded mixed strings, Unicode/control
examples, and the 10,000/10,001 length boundary. Its P6 phase sum was 1.6433
seconds for source verification, mutation replay, proof, and gate. Source
review and adoption were untimed; cost, token use, and human active time are
unknown. No product SAT candidate or downstream impact was found. The gate is
wired into proof CI on Node 22; its hosted result has not been observed. The
exact-source [contract and P6 bundle](../properties/calibration/2026-10-16-p2-real-router-segment/README.md)
adds one targeted reviewed site and one useful local gate.

The retrospective v16 checkpoint has 43 exact-pin questions (31 UNSAT, 12
SAT), 20 useful gates, 38 product replays, and 1,730,604 question-attributed
differential cases, leaving a shortfall of seven. The SAT set is unchanged,
so the v10 triage overlay still applies. Three targeted reviews now cover the
two Tracecat validator rows and the one Real-Router route-segment row; they do
not imply complete review of either repository. The post-outcome
[v16 checkpoint](../properties/calibration/2026-10-16-p2-existing-evidence-20r2-v16/README.md)
and [run-level scorecard](../properties/calibration/2026-10-16-autonomous-scorecard-20r2-after-real-router.json)
keep unique questions separate from timed run outcomes. The refreshed
[question-history index](../properties/calibration/2026-10-16-question-history-index-after-real-router.json)
covers 307 recognized sources, 75 asked identities, 574 reserved sites, and
seven unbound records; this is duplicate-prevention history, not pre-outcome
allocation evidence.

**Real-Router navigation-control singleton P6 lifecycle (2026-10-16):** the
exact `CONTROL_CHARS_RE` row was checked against the frozen inventory and was
unasked in the pre-outcome history. Pinned implementation comments, opt-in
plugin wiring, a functional test, and the changelog supported a narrow
application-config contract for rejecting C0/DEL from string parameter
values. The standing autonomous-adoption policy was used truthfully; the
contract does not claim a remote attacker or a security impact. One row was
reviewed, ranked only as singleton queue rank 1, source-bound and adopted,
then claimed and contracted through the existing locked queue transitions.
The scheduler selected its registered bucket before outcomes were observed.
The P6 runner produced one unique UNSAT question; the DEL-omission mutation
was SAT and reproduced on the pinned helper. The Node 26.11.1 product gate
compared 17,014 input values with zero mismatches. Four runner invocations
preserved three failed resumptions (incorrect mutation formula, witness-key
mismatch, and a gate interpreter missing `jsonschema`); the successful resume
did not repeat the product solver question. The corpus wave closed at
generation 1 with a valid event log. The run-level measurement is 676 seconds
wall clock; cost, token use, and human active time are unknown. The refreshed
v17 checkpoint is 44 questions (32 UNSAT, 12 SAT), 21 useful local gates,
39 product replays, and 1,747,618 differential cases, short of 50 by six.
There are zero SAT product candidates or downstream impacts, reports,
confirmations, fixes, or consumer-adopted gates from this singleton. This is
one prospective P6 integration calibration, not the P7 15/5 wave, a ranking
quality measurement, or a security finding. See the
[source-review and P6 bundle](../properties/calibration/2026-10-16-p2-real-router-navigation-source-review/README.md),
[v17 checkpoint](../properties/calibration/2026-10-16-p2-existing-evidence-20r2-v17/README.md),
and [scorecard](../properties/calibration/2026-10-16-autonomous-scorecard-20r2-after-navigation-control.json).

**Duplicate-prevention repairs after the P6 singleton (2026-10-16):** the
follow-up scheduler audit found that completed-wave attribution preferred a
wave-specific id over the ledger's canonical `corpora`/`corpus` identity. The
Real-Router bucket therefore appeared unused on the next schedule. The
scheduler now prefers canonical corpus attribution, with legacy wave-id
fallback, and a focused regression check proves this P6 bucket is consumed;
the refreshed schedule now reports no unused Real-Router bucket. The source
history audit also found old token-name selectors could alias current
`path:line:column` inventory rows. History matching now checks exact
repository and pin plus normalized source line and regex signature when
available, and conservatively blocks a same-line alias when old history has
no signature. The index stores signatures for new rows. The refreshed index
covers 324 recognized sources, 76 asked identities, 576 reserved sites, and
seven unbound records. These repairs prevent repeat scheduling and duplicate
review; they did not create P7 candidates. The required 15/5 allocation has
since completed in the Aidevops pre-dispatch bucket. Focused scheduler and
history regressions passed (6 checks).

**P2 semantics and campaign scheduler follow-up (2026-10-16):** a pre-adoption
audit found that P2 inventory v3 omitted POSIX-shell `shell_flags`. For the
Aidevops detector marker, the pinned call is `grep -oE` (ERE), while the
compiler defaults a missing selector to BRE; an UNSAT from that old join would
not establish the product property. V4 preserves the extractor's syntax and
grep mode, and the exact `pre-dispatch-validator-helper.sh:1881:47` row now
compiles as an exact ERE mirror. The source inventory remains raw extraction,
not boundary review or yield. Campaign scheduling now accepts an optional
frozen cohort manifest and filters GO decisions by exact repository/pin and
registered buckets by exact dialect family. The generated
[20-r2 campaign schedule](../properties/generated/conversion_schedule_20r2.json)
excludes the separate Aidevops ECMA calibration and the off-cohort Mycelium pin.
The Aidevops POSIX-shell `pre-dispatch-github-text` bucket was registered and
its first 15-site P7 review wave has now closed; follow-on yield remains open.

### P3 — Make source-backed contract adoption executable

**Depends:** P1, P2.

- Reuse `context-extractor.py` and the existing queue. Bind source windows to
  the pinned checkout and source hash; show the actual pattern, flags, call
  site, and cited sink/caller evidence. Read beyond the window when the path
  needs it, with the additional source references recorded.
- Implement the evidence review in the adoption policy. A separate review pass
  checks the guarantee against the product requirement independently of the
  mirror; record corrections and refuted claims. Freeze the decision before
  using solver verdicts to score yield.
- Keep unreachable candidates as skips, unverified candidates unresolved, and
  parser/composition questions on an explicitly behavioral route when no
  faithful solver encoding exists. Replaying a witness may resolve an unknown
  input path; it cannot invent the product guarantee.
- Automate the queue's claimed-to-contracted/skip transition under the existing
  corpus lock. No `human` provenance labels or human time from an agent pass.

**Done when:** a real pinned top-15 shortlist yields at most five adopted
contracts plus explicit dispositions for the other reviews, without owner
adoption prompts or unauthenticated source snippets.

**P3 validation (2026-10-15):** the exact-pin Mycelium review-v2 top-15 was
run through an isolated active wave using the real GO decision, current ledger
snapshot, source-bound adoption records, and `conversion-queue-transition.py`.
Two candidates were claimed and contracted; thirteen were skipped with
source-backed reasons. All 17 transitions succeeded and the wave closed under
the corpus event lock. The queue and event log lived in a temporary directory;
the campaign queue was untouched. This completes P3's local workflow check,
not cohort yield or campaign integration. See the linked
[`queue-transition-replay.json`](../properties/calibration/2026-10-15-autonomous-mycelium-script-slice/queue-transition-replay.json).

### P4 — Register and schedule new idiom slices

**Depends:** P0, P3.

- Replace the requirement that a new bucket already appear in historical
  conversion output with a reviewed, explicit registration path. Reuse the
  scheduler's protections for malformed queues/history and active waves.
- A registration names its cluster, pin, product engine, trust map, vocabulary,
  source sites, independent question family, and bounded candidate count.
  Record exhausted/stopped decisions and semantic duplicate idioms.
- Preserve stopped OpenWrt clusters and existing close-out deny-lists. A new
  source-backed justification and recorded policy decision are required to
  revisit them; a renamed bucket cannot reopen exhausted work.
- Use the deterministic productive/novel/unbiased allocator against a frozen,
  eligible population. Freeze the sample seed before outcomes; report realized
  counts rather than treating the scheduler's 70/20/10 constants as allocation.

**Done when:** a previously unregistered eligible cluster can receive one
valid next slice, while stopped, duplicate, malformed, or active-wave cases
remain blocked with machine-readable reasons.

The source-pinned registrar and scheduler have now selected a new Malcontent
bucket at its matching GO pin. Existing registry/scheduler tests cover pin
mismatch, stopped clusters, duplicates, malformed queues, and active waves.
The scheduler emits 70/20/10 reservation constants, but its implementation
selects the first unused registered bucket per cluster; it does not allocate
candidate sites among productive, novel-idiom, and unbiased strata. The tests
assert those constants, not an allocation from a frozen eligible population.
The plan's reference to an “existing ... reservation design” is therefore
ahead of the code. P4 needs a specified candidate-population model and a
selection algorithm before it can produce allocation evidence; this plan does
not count the constants as that evidence.

**P4 allocation audit (2026-10-15, dirty checkout):** a scheduler snapshot
found 83 GO decision files representing 80 distinct clusters. It selected two
registered buckets (`mycelium/scripts-bootstrap` and
`malcontent/git-crlf-smuggling`); 74 clusters had no available progression,
two had an unregistered next bucket, and two were stopped. The conversion
queue directory and candidate-site population were absent. The scheduler
reported the 70/20/10 constants, with no candidate strata to allocate. Full
schedule and input digests are recorded in
[`2026-10-15-autonomous-p4-allocation-snapshot.json`](../properties/calibration/2026-10-15-autonomous-p4-allocation-snapshot.json).
These are diagnostics from the dirty checkout, not a clean-main allocation
experiment. P4 needs an explicit eligible population and productive/novel/
unbiased labels before the shares can be exercised or evaluated.

**P4 allocation implementation (2026-10-15):** added a versioned frozen
population schema, deterministic keyed-hash sampling with Hamilton quotas,
seed-commitment verification, registered-site/trust checks, exact inventory
and classification joins, clean source-file rechecks, ledger/input digests,
and an active-wave guard. The required history index scans recognized
conversion NDJSON, aggregate autonomous-run measurements, runner
state/checkpoints/attempts, frozen rosters and shortlists, contract artifacts,
queues, review decisions/evidence, queue-transition replays, and upstream
dispositions. It binds source paths and hashes, blocks previously asked and
reserved sites (including inventory-site aliases), fails closed on unresolved
history, and is rebuilt during allocation so changed or new history sources
invalidate the sample. The 2026-10-15 dirty-checkout scan found 56 sources, 45
asked site identities, 108 reserved site identities, and 7 aggregate run
records without site identity. Those seven are unresolved and block candidates
for their matching repository pins. This covers the listed repository
artifacts; undocumented external work and artifacts outside these source
families remain outside the index. The frozen scan is
[`2026-10-15-question-history-index.json`](../properties/calibration/2026-10-15-question-history-index.json)
with SHA-256 `85d8b9a341948eefaf37be0e80cf412e492a89d57a91ab35fb39622233c6ae96`.
Seventeen focused allocation/history unit
and CLI fixture tests pass, including row-order determinism, the 10/3/2
fifteen-site mix, full-population unbiased sampling, mismatched-seed,
duplicate/prior/reserved-site rejection, stale history, and tampered/missing
inventory or classification rows. This implements and unit-checks the
allocator, not corpus yield. The current
registrations expose one Mycelium source site with cap 5 and seven Malcontent
source sites with cap 1; neither supports a 15-site shortlist. The history
index finds the Mycelium representative already reserved and all seven
Malcontent shortlist sites reserved, so the existing registrations currently
have no allocatable candidates. No frozen population or pre-outcome class
evidence exists. Classification hashes bind the supplied notes but do not
certify that a productive/novel label is true; the cited ledger and proof/gate
evidence still need review. P4 therefore stays open until a new eligible pool,
pre-outcome seed, and realized allocation are recorded. See
[`CONVERSION-ALLOCATION.md`](CONVERSION-ALLOCATION.md).

**P4 pool/shortlist cap correction (2026-10-15):** source review found the
registry limited `source_sites` to 15, the same as the review shortlist cap.
Because the allocator can only select registered sites, any full 15-site
allocation was necessarily a census; it could not measure seed-based selection
from a larger eligible pool. The registry now permits up to 10,000 source
sites while keeping `max_candidates` at 15. A focused registry case covers a
30-site eligible pool with an 8-site shortlist cap. This repairs the data
model; see [`CONVERSION-ALLOCATION.md`](CONVERSION-ALLOCATION.md).

**First real P4 allocation (2026-10-15):** registered the separately scoped
Aidevops Node `ecma-plugins` secret-read policy at the exact GO pin. The P2
source freezer emitted 1,018 raw ECMA rows (the older admission artifact's
1,042 count uses a distinct extractor/scope). Compiler checks left three
encodable predicates in the single pre-read helper; the adopted extension
predicate is reserved, leaving two eligible candidates. The frozen ledger
could not substantiate productive or novel labels, so both remained
`unclassified`. With a seed committed in the frozen population, the allocator
selected one unbiased site, the secret-basename rule at line 7. Scheduler basis
was `named-next-unused`; the exact GO pin, history, inventory, classification,
registry, clean checkout, and source bytes were reverified. P4's minimum real
allocation criterion is now met. This two-site population is too small to
estimate allocation quality or throughput, exercises neither productive nor
novel allocation, and is not a 20-r2/P7 product question. The allocated site
was source-reviewed and given a narrow adopted contract; its proof-wave result
is recorded in the [Aidevops Node calibration](../properties/calibration/2026-10-15-autonomous-aidevops-node-secret-boundary/README.md).

### P5 — Complete a faithful proof-to-gate vertical slice

**Depends:** P1, P3; reuse #648 as the first concrete implementation.

- Execute the exact pinned product helper, not a reimplementation. Match flags,
  search/fullmatch, captures, preprocessing, and output semantics to the
  independently adopted guarantee.
- Prefer the cheapest faithful shape. Require mutation coverage, SAT callbacks,
  product-engine replay, and differential checks where appropriate. Pin Z3
  5.0.0 and applicable product runtimes. Missing engines and unknown fail.
- A mutation must demonstrate the property/harness can detect the targeted
  weakening; a synthetic mirror mutation alone does not establish the real
  product regression gate's sensitivity.
- Emit conversion rows from actual registry/run records, then produce a
  runnable consumer gate using the existing `newgate` machinery where suitable.
  Record local reproducibility separately from adoption by an upstream project.

**Done when:** one real site runs from adoption through faithful verification,
mutation, replay/fuzz, artifact emission, and a reproducible gate. Extend to
additional engines only when the next selected contracts require them.

### P6 — Add a bounded, resumable operator loop

**Depends:** P2–P5 and any required #448 reconciliation.

- Compose rank/probe/gate, materialization/batch, registered conversion slice,
  context/adoption, proof/replay, emission/disposition, and close-out. Reuse
  existing state stores: queue owns pre-contract states; later states derive
  from actual run records and curated disposition evidence.
- Separate candidate-intake, probe, conversion, and frozen-measurement stores.
  Resume by exact source pin, manifest/contract digest, and wave generation;
  never infer success from a subprocess finishing or a stale generated report.
- Audit admission promotion too: routine agent-authored GO decisions need
  truthful actor metadata and source-backed conditions. Existing `--human`
  command names do not license fabricated human review. Version the metrics
  and re-establish comparable baselines before any changed escape decision.
- Handle per-item failures with bounded retries and terminal reasons, release
  leases on close/abort, preserve partial NDJSON, and exit nonzero for failed
  required verification. A bad item does not erase completed work or pass its
  own gate. Use existing wave-aborted/compensation semantics.
- Provide dry-run, resume, bounded-work, and status modes. The run report shows
  completed work, unresolved work, resources consumed, and the next action.

**Shipped slice (2026-10-14):**
[`scripts/run-autonomous-proof-wave.py`](../scripts/run-autonomous-proof-wave.py)
accepts a frozen cohort and roster, verifies each selected registry contract
against the roster digest, checks a clean exact-pin source checkout and source
bytes, then runs properties serially under the campaign's five-question and
30-second solver caps. It uses a single-writer lock, writes an immutable input
snapshot, records an attempt before entering the solver, and atomically
refreshes the resumable state, conversion NDJSON, and v3 checkpoint after each
item. Timeout, unknown, replay failure, SAT, and interrupted work remain
visible; solver retries are disabled. An optional argv-only local gate names
the exact question IDs it covers. A reproduced SAT is recorded as
`pending_product_triage`, separate from filing or confirmation.
Gate configs also carry a reviewable per-question evidence map for product
replay and differential case counts. The Forge fixture's
[`gate.json`](../properties/calibration/2026-10-13-autonomous-forge-cli-integration/gate.json)
binds its 5,680-case claim to the test that asserts that exact case count.
That retrospective fixture has six identities, so it exceeds the five-contract
campaign cap and is a gate-evidence example rather than a directly runnable
P6 roster. A runnable wave must freeze a roster of at most five and a matching
gate coverage list before solving.

This runner is limited to non-synthesized `property` entries already registered
in the local harness and present in the canonical conversion emitter's shape
map. It does not own candidate intake, rank/probe, the pre-contract queue,
source fetch/materialization, contract authoring/adoption, or filing and
external-response dispositions. Its one-file lock serializes proof-wave
writers; it does not replace the corpus queue's claim/close/abort lifecycle.
Therefore the runner is still only an implementation slice. A later
Real-Router singleton did exercise the upstream queue claim/contract
transitions, proof, mutation, local gate, conversion emission, and corpus
close-out as one resumable serial lifecycle. These stages were composed by
bounded scripts and frozen artifacts; the proof runner itself still does not
orchestrate general intake, ranking, probing, contract authoring, or external
dispositions. P6 has a successful singleton lifecycle calibration, but its
general operator loop and a 15/5 campaign wave remain open.

**P6 shape-registration gap found during the P8 scope correction (2026-10-16):**
the standalone Aidevops webhook gate passed, but a frozen three-question roster
for its corrected Bash language-inclusion properties was rejected before
solving because the canonical conversion emitter had no shape entry for those
question IDs. The original preflight started zero solver questions, created no
wave state, and ran no gate. The gap is now resolved by documented shape 6:
unbounded inclusion of a source regex language in an independent contract
language. The three contracts remain `kind=property`; shape-5 `rule_diff`
semantics were not reused. The frozen preflight record is preserved in the
[scope-correction bundle](../properties/calibration/2026-10-16-p8-v22-audit/p6-scope-correction/README.md).

**P6 shape-6 Aidevops wave (2026-10-16):** the runner now completes this
three-question exact-pin wave. All three contract invariants were UNSAT, all
three associated mutation guards reproduced against Bash, and the gate passed
four mutation replays, 671 Bash/compiler pattern comparisons, and 48 integrated
helper cases with zero mismatches (719 total cases). The gate's four guards include the slug guard outside the
three-question roster. The run is a repeat of v22 questions, so it adds no new
P2 yield. It adds a working P6 integration path for full-domain contract
language inclusion; the general operator loop and 15/5 campaign wave remain
open. See the [shape-6 wave record](../properties/calibration/2026-10-16-p8-v22-audit/p6-shape6-r1/README.md).

**Gate-backed calibration (2026-10-15):** the Malcontent one-question roster
passed this runner end to end. It verified the exact checkout and contract
digest, ran the UNSAT property and SAT real-engine mutation guard, executed the
139-case YARA-X gate, and emitted a complete v3 checkpoint. The source pin,
fixture expectations, replay details, and limits are documented in
[`2026-10-15-autonomous-malcontent-git-cr-20r2/README.md`](../properties/calibration/2026-10-15-autonomous-malcontent-git-cr-20r2/README.md).
CI now installs YARA-X 1.19.0 only after checking both the release archive and
binary SHA-256 values, runs the full-rule product gate, and later runs the
registered proof/mutation callbacks with the full harness suite. This is useful
P6 evidence, but it does not compose candidate intake, ranking,
queue/admission transitions, or downstream dispositions.

**Aidevops Node calibration (2026-10-15):** the P4-selected basename rule was
source-reviewed through its model-controlled pre-read caller and adopted under
the standing contract policy. Its P6 r3 wave verified the exact clean pin,
ran the UNSAT finite 64-case regex property and SAT real-source mutation, and
passed the 220-call Node product gate across Read, Glob, and NotebookRead. The
earlier r1 run failed closed because the gate configuration resolved the
virtualenv interpreter to a global interpreter without `jsonschema`; that
terminal attempt is preserved separately and was followed by fresh, passing
r2 and r3 states. The calibration has its own ECMA cohort and does not count
toward 20-r2/P7 yield. Artifacts are in the
[Aidevops Node calibration](../properties/calibration/2026-10-15-autonomous-aidevops-node-secret-boundary/README.md).

**Mycelium frozen-cohort P6 replay (2026-10-15):** the d4f contract and
runner-compatible roster now complete a real one-question P6 wave on the exact
20-r2 source. The runner verified the pin, adopted contract, and source anchor;
the property was UNSAT, both family mutation guards reproduced, and the
3,814-case Bash gate passed. This re-executes the same checksum-preflight
question already counted by its earlier gate-only run, so it adds runner
evidence but no distinct P7 question. The current Mycelium GO decision and
scheduler registration still point to 4b53, not frozen pin d4f; this runner
result does not silently resolve that admission mismatch. See the
[Mycelium 20-r2 calibration](../properties/calibration/2026-10-15-autonomous-mycelium-20r2-slice/README.md).

**Aidevops shell P6 replay (2026-10-15):** five source-bound revisions of
historical shell-hook contracts completed on the exact 20-r2 pin. The runner
verified source bytes, resolved all five properties UNSAT, passed the family
mutation guard with real replay, and ran one 70-case BusyBox gate. The checker
now fails closed unless the product engine is BusyBox v1.36.1; the local build
was `BusyBox v1.36.1 (Ubuntu 1:1.36.1-6ubuntu3.1)`. The scope-heading source
anchor is `Files` on the pinned regex line because the POSIX character-class
text contains colons reserved by the site format; contract semantics did not
change. This repeats the existing 15-reviewed/5-contract Aidevops close-out,
so it adds P6 runner/gate evidence but no new review, novel question, security
finding, or P7 yield. Admission, candidate intake, and downstream queue
composition remain unproven. See the
[Aidevops shell calibration](../properties/calibration/2026-10-15-autonomous-aidevops-posix-shell-20r2/README.md).

**AutoAR Go endpoint P6 calibration (2026-10-15):** reviewed the pinned
`jsendpoints` assignment parser from downloaded JavaScript response body to
endpoint text/dashboard output, and adopted one delimiter-exclusion contract.
The one-character ASCII Shape-1 property is UNSAT; weakening the quote class
produces a SAT witness that the actual Go 1.25.7 extractor stores. The local
product gate covered 163 inputs with zero delimiter leaks, and is wired into
CI. The P6 runner recorded one proof, one mutation replay, and one local gate.
An initial standalone solver/product check happened before roster freeze, so
this is retrospective calibration and does not count as prospective P7 yield.
It is not a ranked 15-site shortlist or a security finding; endpoint validity,
scope safety, and extraction completeness remain outside the contract. The
workflow row records one reviewed site and one adopted contract over 513
seconds; cost, tokens, and human active time are unknown. Neither a reachable
bug nor any external report, maintainer confirmation, or fix resulted. Full
evidence is in the
[AutoAR Go endpoint calibration](../properties/calibration/2026-10-15-autonomous-autoar-jsendpoint-20r2/README.md).

**AutoAR loopback script-source P6 candidate (2026-10-15):** after reviewing
the adjacent HTML collector, adopted a separate source-bound contract for
`scriptSrcRe` at line 22. The subdomain monitor supplies live-host URLs; the
collector resolves absolute `<script src>` references, checks HTTP(S) and a
`.js` path, then fetches the result without an origin or address-class check.
The pinned README requires authorized, in-scope targets, but does not say
whether external CDN scripts are expected or how operator loopback should be
handled. Z3 found a concrete script element in the pinned Go RE2 search
language, and the exact Go 1.25.7 collector replay fetched `/bundle.js` from a
second local loopback origin and extracted `/api/v1/users`. The same-origin
control passed. The P6 gate covered two local cases; a follow-up product-only
replay repeated both, with no external network request. The P6 runner passed
source verification, the family mutation guard, witness replay, and local
gate, then persisted the reproduced SAT as `pending_product_triage` and marked
the wave `needs_review`. This establishes a reachable loopback request in the
pinned code; security impact and intended product policy remain unconfirmed.
No report was sent. This targeted follow-up is not a ranked 15-site
allocation or P7 yield. The evidence bundle is in the
[AutoAR scope-candidate calibration](../properties/calibration/2026-10-15-autonomous-autoar-jsendpoint-scope-escape-20r2/README.md).

**Anax organization deny-list P6 calibration (2026-10-15):** the corrected Go
inventory exposed a direct `regexp.MatchString` call omitted by the previous
extractor. I reviewed all 26 literal Go-regex sites at the frozen pin:
fifteen are skips after an exact Go 1.25.7 HTTP parser replay resolved both
CR/LF checks as unreachable from raw network header values, ten remain
unresolved pending parser or product-specification evidence, and one narrow
deny-list contract was adopted for `ValidateOrg`. It covers only underscore, comma, Go RE2 ASCII
whitespace, question mark, and apostrophe, and verifies that `OrgCreate` and
`OrgDel` reject those inputs before Exchange operations. The Shape-1 product
property is UNSAT; weakening the question-mark member is SAT and reproduces
through the exact pinned Go function. The Go 1.27.2 gate compared 687 inputs
with zero mismatches. The first mutation preflight was incorrectly UNSAT and
remains recorded; the runner resumed the same wave, corrected the guard, and
passed mutation plus product gates without retrying the solver question. This
is one useful local gate and one retrospective P2 question, not a new P7
sample or a complete allow-list/path-safety claim. Evidence is in the
[Anax source review](../properties/calibration/2026-10-15-p2-anax-source-review/README.md)
and [Anax P6 calibration](../properties/calibration/2026-10-15-autonomous-anax-org-validate-20r2/).

**AutoAR phase-key filename P6 calibration (2026-10-15):** source review
traced the request-controlled `module` query from `apiGetScanPhaseLogs` to
`ReadPhaseLogFile` and the `filepath.Join` sink. The adopted claim covers only
that module-derived component; `scanID`, the results root, symlinks, and
sanitized-name collisions remain outside scope. Its one-character Shape-1
property proves the pinned RE2 replacement class matches `.`, `/`, and `\\`.
The mutation guard allows dot and slash, finds `.`, and the exact Go 1.25.7
helper produces a path outside `phase-logs` for `../../outside`. The product
gate passed 662 exact-helper cases with zero mismatches. P6 retained two failed
gate attempts, resumed twice without repeating the solver question, and closed
with one UNSAT property, a reproduced mutation, and one useful local gate. Its
38-second runner interval contains no product violation or external outcome.
The [source review](../properties/calibration/2026-10-15-p2-autoar-source-review/README.md)
and [phase-key evidence](../properties/calibration/2026-10-15-autonomous-autoar-phasekey-20r2/README.md)
carry the exact artifacts.

**llm-honeypot-intelligence P6 candidate capture (2026-10-15):** the runner
verified both exact-pin contracts and source anchors, ran the two SAT
counterexample finders and their family mutation guards, and passed the local
shell regression gate. Both witnesses replayed; the private-IP gate covered
65,541 cases and the Tor gate covered four fixed response sequences. The run
persisted both findings as `pending_product_triage` and ended `needs_review`
with exit 1, which is the expected status for SAT findings, not a failed proof
or a successful campaign close-out. The local gate used an isolated exact
source checkout and a fake `nc`; it inspected no real generated artifact,
published repository data, live Tor service, or scan. P6 still lacks composed
candidate intake, ranking, queue/admission transitions, and downstream
dispositions. See the
[P2 source review bundle](../properties/calibration/2026-10-15-p2-llm-honeypot-source-review/README.md).

**Panther pre-commit review-path P6 candidate (2026-10-15):** the runner
verified the exact pin and source files, passed the family mutation guard, and
executed the nine-case local path gate. The SAT witness `secrets.py` was
selected by the helper and its synthetic marker entered the locally assembled
prompt; mutating the exclusion to `^$` also passed `password.secret.py` through.
The runner records `needs_review` because the shared-path policy is inferred
from a separate slash-command policy and product impact is unresolved. No real
secret, Claude process, or network request was involved. This is another
retrospective 20-r2 calibration, not a new 15-site P7 wave or confirmed issue.
See the
[Panther source review bundle](../properties/calibration/2026-10-15-p2-panther-source-review/README.md).

**Magic JS Base64URL P6 calibration (2026-10-15):** ten adopted exact-pin
contracts for PKCE, WebAuthn, and DPoP encoders completed in two serial waves
of five, the campaign cap. The canonical emitter now registers these shape-4
questions. Both rosters and source checkouts passed preflight; all ten
per-codepoint output-image properties were UNSAT, the shared weakened-plus
mutation was ground-truthed, and the Node gate returned zero mismatches. The
question-attributed replay totals are 481,034 cases. The gate command ran all
ten questions in each batch, so each run executed 481,034 comparisons; the
checkpoint counts question coverage once. The phase sums were 1.0245 and
1.0204 seconds. The local reproducible gate covers Base64URL output only; it
does not establish OAuth entropy, authentication, signature validity, or
server acceptance. It adds one useful local gate and no SAT product candidate
or confirmed impact. See the
[Magic JS review/P6 bundle](../properties/calibration/2026-10-15-p2-magic-js-source-review/README.md)
and [v13 checkpoint](../properties/calibration/2026-10-15-p2-existing-evidence-20r2-v13/README.md).

**Done when:** interrupted runs resume without duplicate questions/filings or
stale-pin reuse; malformed evidence and timeout cannot generate a successful
close-out; the first real serial wave finishes without routine owner input.

### P7 — Run the first autonomous campaign and reach the evidence checkpoint

**Depends:** P6. **This is data work, not another infrastructure-only phase.**

- Start with the original 20-r2 cohort and compatible existing wave work.
  Complete one serial 15/5 wave first; inspect cost, errors, and contract
  quality before increasing the work-per-run budget.
- The first serial wave is complete in Aidevops `pre-dispatch-github-text`:
  15 source-backed review decisions (one adopted, 14 skipped), one
  contract-backed SAT witness with exact-helper replay, and one mutation guard.
  The witness reads a local fixture outside the clone; product triage and
  downstream impact remain unresolved. Its isolated queue closed at generation
  1 without changing shared queue state. The wave adds one eligible question
  and one useful local gate, bringing v18 to 45/50. The 14 unselected sites
  remain outside the frozen first sample and may only be used in a separately
  declared follow-on review.
- Work toward 50 distinct eligible product questions in the frozen cohort,
  then 100 if continued work is justified. Publish resolved results, all
  attempts/not-proven outcomes, useful gates, unique sites, and repository mix.
  Fifty questions is an evaluation checkpoint, not a success threshold.
- Target the existing 5–7 completed repository-processing outcomes per week
  and at least one completed conversion wave per initial work cycle. Both are
  proposed cadence goals; measure feasibility before promising a speedup.
  Do not require five contracts from a weak slice or duplicate alphabets to
  fill a quota.
- Keep mine cap 10 while queue pressure persists. Finish conversion on admitted
  material before expanding intake. Defer scoring changes and parallel walks
  unless measured evidence identifies them as the limiting stage.
- If the original cohort cannot supply 50 defensible questions, publish that
  coverage result. Freeze an additive 30-repository cohort preserving all 20
  original pins before observing its ten new members. Report both cohorts;
  do not redefine the old denominator. The existing 50-repository ceiling is
  retained, with no automatic expansion to it.

**Done when:** a complete versioned frozen-cohort checkpoint reaches 50 eligible
questions or a documented resource/coverage limit supports an explicit retarget
or stop decision. An unsuccessful experiment is a valid completed outcome.

### P8 — Assess usefulness, bug yield, and the next investment

**Depends:** P7; reporting and SAT disposition start with the first wave.

- Produce the scorecard below and a reproducibility bundle. Include source
  corrections, vacuous/unsupported contracts rejected by review, model errors,
  nonreproducing witnesses, unreachable inputs, and refuted claims.
- Compare autonomous and historical human series where domains/populations
  permit. Report per-repository/per-idiom counts and audit a prespecified
  sample of adoptions, skips, and UNSATs using a fresh review pass. Correlated
  agent review is not a human gold label.
- Prepare concrete evidence packets for real candidate bugs. Record disclosure
  pending authorization without blocking independent proof/gate work. Track
  actual transmission and maintainer response separately from a private tag.
- Decide continue-to-100, retarget guarantees/corpora, improve a measured
  bottleneck, or stop. Owner chooses investment direction at checkpoints;
  routine contract adoption remains autonomous.

**Done when:** a written decision is supported by frozen evidence, cost and
coverage limits, and both primary gate outcomes and downstream bug outcomes.

## Evaluation scorecard

| Track | Counts and rates | What qualifies |
|---|---|---|
| Throughput | Completed repository outcomes, reviewed sites, adopted questions, completed waves, questions/gates per agent hour, cost per useful gate, retries and human interventions | Measured execution; report unavailable usage/cost as unknown. |
| Contract quality | Adoption rejection/correction rate, missing source/spec/sink evidence, unreachable/behavioral-only skips, audit corrections | Prespecified review/audit rules; preserve all reviewed candidates. |
| Useful proof/gate, primary | Decided faithful questions; UNSAT guarantees; local runnable gates; consumer-adopted gates; mutation sensitivity and replay/fuzz coverage | Named boundary, justified domain, pinned execution and applicable fidelity evidence. A narrow toy theorem or duplicate question is not a new useful gate. |
| Bug discovery | SAT candidates → real engine replay → reachable product violation → security-impact-confirmed candidate | Count candidate properties, unique sites, and deduplicated root-cause findings separately. |
| External outcome | Authorized reports actually sent → independent maintainer confirmation → fixes accepted/released | Linked external evidence. Separate own-code and third-party, public/private, and unresolved cases. |
| Coverage/limits | Eligible attempts vs decided vs not proven, rejected surface, domain bounds, dialect/engine/idiom mix | Failed and unresolved attempts stay visible; no general claim outside sampled coverage. |

Use the checkpoint's existing interval machinery for descriptive rate estimates
and state the sample size. Properties within a repository/idiom are correlated,
and the mined/ranked cohort is selected; a property-level Wilson interval is
not a population prevalence estimate. Do not tune selection on these results
and present the same cohort as unseen validation. Keep a prespecified
exploration slice and report it separately.

The repo provides a 50/100 sample checkpoint but no agreed minimum useful-gate
rate, dollar budget, or third-party bug rate. Freeze those investment criteria
before the campaign if the owner supplies them. Otherwise report the rates,
costs, uncertainty, and limits and make an explicit decision; do not manufacture
an efficacy claim from crossing fifty.

## Luna operating brief

Work P0, then P1, then the shortest real vertical path P2 → P3 → P5 using #648.
Complete P4/P6 only to support the next real waves; start reporting campaign
data immediately. Use one active conversion wave until its close-out is emitted.
Keep implementation PRs bounded and use the review/CI protocol applicable to
the runtime operating Luna, with fresh review after material fixes.

Read `docs/SECURITY-AUDIT.md` when changing the repo's evidence/counting gates,
and `docs/TRAPS.md` before encoding properties. Existing backend authority and
source-semantic restrictions still apply. An autonomous contract decision does
not turn a missing or unsound proof route into an admitted route.

At each child close-out record the exact revision, changed behavior, checks,
source evidence, remaining limitations, next runnable child, and artifact paths.
Do not declare the parent done because tooling landed. Execute P7 and publish
P8. Continue independent work when a candidate needs outside input; leave that
candidate unresolved rather than lowering evidence standards.

The policy authorizes routine agent adoption. Third-party communication still
follows [SECURITY.md](../SECURITY.md) and explicit communication authorization.
The runner can prepare those packets while continuing other waves.

## Parent completion checklist

- [x] P0 baseline and existing-issue reconciliation completed for current-main `fbc7aa6`; later revisions need a new dated snapshot.
- [x] P1 autonomous adoption/counting implemented across all report paths.
- [ ] P2 independent coverage roster and complete attempt accounting shipped. (All 20 exact pins have source checkout evidence. Current inventory v5 has 21,956 raw sites, 19 repositories complete under the registered file selection, and Everclaw incomplete because all six gitlinks were excluded from v5. An addendum maps four root commits and extracts 8,361 raw rows from two incomplete child snapshots; both snapshots omit 15 nested gitlinks, two other verified trees have zero ECMA rows, and two root URLs remain unresolved. A follow-up checked a plausible public `everclaw-fork` repository, but the exact gitlink commit is unavailable there; neither URL is inferred. These addendum rows remain unreviewed and are not merged into v5 or counted as unique yield. V5 also corrects omitted compound Bash tests and 26 truncated Bash patterns. Twelve complete source-review slices cover 556 raw sites: 393 skips, 131 unresolved, and 32 adopted rows. The complete Tracecat slice includes the previously targeted environment-key and server-name rows plus the origin-slug, two path-component, RBAC scope-pattern, and table-identifier quote-exclusion questions; the stdio MCP tool-name row is an evidence-backed compatibility skip, the separate agent sandbox environment-key validator is unreachable from untrusted input at this pin, the two token-scope patterns only parse claimed IDs before database membership authorization, and the email-address regex composes with EmailMessage normalization and call ordering rather than providing a regex-only security contract; the sandbox executor environment-key row adds an adopted no-equals separator contract; two separate targeted Real-Router reviews add two sites/contracts without claiming full-slice coverage. The separate P7 Aidevops bucket and its deterministic complement cover all 29 source identities: two adopted contracts and 27 evidence-backed skips. A follow-on webhook protocol census covers 11 additional regex records (four adopted, six skipped, one unresolved). The frozen v22 retrospective checkpoint remains 50 exact source questions (35 UNSAT, 14 ground-truthed SAT, one timeout); additive v26 adds four post-checkpoint Tracecat questions for 54 total (39 UNSAT, 14 SAT, one timeout), with 28 useful local gates, 49 product replays, and 1,758,132 question-attributed differential cases. Additive v27 adds one Tracecat sandbox environment-key separator question for 55 total (40 UNSAT, 14 SAT, one timeout), with 29 useful local gates, 50 product replays, and 1,762,364 differential cases. Its initial whole-string encoding timeout and callback mismatch are preserved separately; v27 counts the final outcome for this unique question, while complete raw attempt accounting remains open. Five attempts across three unique questions remain excluded from P2 coverage: three source sites are outside the declared dialect inventory and two Json Editor attempts have ambiguous line-only selectors. The v11 outcome overlay covers all 14 SAT questions: two refuted security-bypass claims and 12 product candidates across ten groups, including the two Aidevops workflow cases; confirmed impacts remain zero. Several documented product questions remain unresolved, including the Inhale same-origin prefix, Snyk LS hover formatter, Json Editor Base64 preview, Magic JS wallet-kit email validator, and Doberman's undocumented shell/command/secret heuristics. Review coverage across the rest of the cohort, Everclaw submodules, and final dispositions for unresolved sites remain open.)
- [x] P3 evidence-backed adoption and locked transitions run without per-contract owner approval. (A source-bound Mycelium top-15 was closed in an isolated active wave: two adopted contracts and thirteen evidence-backed skips. Campaign integration remains open. The P7 checkpoint was still pending at that off-cohort calibration and was reached later in v22.)
- [x] P4 new-slice registration schedules valid work and respects stop decisions. (Aidevops `ecma-plugins` received a source-pinned, pre-outcome one-site allocation from a two-candidate pool. This meets the minimum registration/allocation criterion only; productive/novel strata, a 15-site original-cohort allocation, and conversion throughput remain unmeasured.)
- [x] P5 real proof/replay/mutation-to-local-gate vertical slice completed.
- [ ] P6 bounded resumable operator loop completes a real wave. (The local
  runner completed gate-backed Malcontent, Mycelium frozen-pin, Aidevops Node,
  Aidevops shell, Json Editor, Magic JS, Doberman Core, and Tracecat calibration
  questions. The Tracecat MCP stdio environment-key question is SAT,
  ground-truthed, mutation-guarded, and passed an exact-source gate over 1,442
  deterministic comparisons; the runner correctly leaves it `needs_review`
  pending product triage. No security impact is confirmed. The separate
  server-name invariant wave completed one shape-1 UNSAT proof with a
  source-weakened SAT mutation, exact-source replay, and a 714-case product
  gate. These two targeted Tracecat questions reuse one serial idiom bucket;
  the first remains pending triage. Magic JS
  completed two serial five-question waves: all ten source-backed Base64URL
  image properties are UNSAT, each batch's weakened-plus mutation was
  ground-truthed, and the exact-source Node gate had zero mismatches. This
  adds one useful local gate, not a confirmed bug or consumer-adopted gate.
  Aidevops shell reused five
  historical questions at the pinned BusyBox engine; it contributes no new
  yield. The Aidevops Node r1 attempt demonstrates fail-closed gate handling;
  queue/admission composition and a prospective 15/5 campaign wave remain
  open. The AutoAR scope-candidate P6 run also recorded a reproduced SAT
  loopback request with `pending_product_triage`, but remains a targeted
  one-question calibration. The Malcontent author-Markdown P6 question
  reproduced SAT and entered `pending_product_triage`; its first attempt hit a
  canonical emitter shape-map gap and was recovered from the same-run gate
  artifact without a solver retry. Prospective campaign lifecycle and
  downstream disposition still remain open. The threat-hunting-description
  Markdown question also completed its P6 proof and real-engine differential
  gate, with the expected `needs_review` state for its SAT witness. The Anax
  one-question wave passed the property, corrected mutation guard, and 687-case
  exact-Go gate after preserving and resuming from its failed guard preflight.
  The AutoAR phase-key question passed one UNSAT property, a real weakened-path
  mutation, and a 662-case Go gate after two visible gate-failure resumes; its
  solver question ran only once. The Inhale r1 wave verified its exact source
  pin, two SAT path-escape witnesses, a real substitution mutation, and a
  six-case gate; it persisted `needs_review` for product-impact disposition.
  Its separately logged P6 phase sum is 0.2871 seconds, with two replayed
  witnesses, two reachable local path escapes, zero confirmed impacts, and no
  reports or fixes. Json Editor completed one source-bound EnumEditor P6
  question with an UNSAT result, a real-source mutation guard, and a
  1,116,985-case Node gate. Its first wave preserved a gate-command failure;
  the second gate passed but exposed an ambiguous line identity; the third
  wave used the inventory's exact source column and joined as one useful gate.
  The three P6 phase sums are recorded separately; no product bug or external
  outcome was established.
  Real-Router completed one additional exact-pin calibration: the shared
  route-segment alphabet property is UNSAT, its slash-allowlist mutation is
  SAT and reproduced through all three helpers, and a 17,027-case-per-helper
  Node gate had zero mismatches. The 1.6433-second phase sum and contract
  scope are recorded in its bundle. This adds one local gate and one
  retrospective P2 question, not a security finding, full-repository review,
  pre-outcome allocation, or prospective P7 yield.
  Real-Router then completed a separate one-site P6 queue-to-closeout
  calibration for navigation parameter controls: one UNSAT, one source
  mutation reproduced, and a 17,014-input Node gate with zero mismatches.
  The four runner invocations include three preserved failed resumes but only
  one unique solver-question execution. Its GO decision is scale-based, with
  the security-boundary condition false; no remote attacker, SAT candidate,
  bug impact, consumer adoption, report, confirmation, or fix is established.
  Tracecat then completed two new one-question P6 singletons. The artifact
  path-segment image theorem is UNSAT, its slash-allowlist mutation reproduces,
  and its exact-source gate compares 2,467 inputs with zero mismatches. The
  workspace-sync component-image theorem is UNSAT, its colon-allowlist
  mutation reproduces, and its exact-source gate compares 2,469 inputs with
  zero mismatches. Together the path-component questions add two useful
  local gates, not SAT product candidates or security impacts. Tracecat then
  completed a third one-question wave for RBAC scope names: the property excludes
  question-mark and bracket glob syntax, its weakened question-mark mutation
  broadens the exact `fnmatch` matcher, and the Pydantic/Python exact-source gate
  compares 2,632 inputs with zero mismatches. The helper alone accepts a
  terminal line feed, but the request schema rejects it before the pinned route
  reaches that helper; no current bug or impact is claimed. This adds one useful
  gate, with a 1.8441-second P6 phase sum. Review/contract authoring time,
  tokens, cost, and human active time remain unknown. Tracecat then completed a
  fourth one-question P6 wave for table and column identifiers. The
  shape-1 theorem proves the exact request allowlist excludes double quotes;
  the weakened schema mutation admits `a"`, while the unchanged service
  validator still rejects it before DDL. Its exact-source Pydantic/service
  gate checked 2,227 inputs with zero mismatches. The request schema accepts a
  final line feed, but the service rejects it before DDL. This is a useful
  defense-in-depth gate, not an SQL-injection finding or impact. Its 2.0391-
  second phase sum and one useful local gate are recorded in the bundle. The
  gate is wired into proof CI; its hosted result has not been observed.
  Tokens, cost, source-review time, and human active time remain unknown. P2
  v22 remains frozen at 50 exact-pin questions; additive v27 contains 55
  questions, 54 decided, and one timeout. The fifth post-v22 Tracecat question
  proves the sandbox environment-key alphabet excludes `=` at every position,
  with no length bound. Its weakened-pattern mutation reproduces
  `TRACE=TOKEN`, and the exact-source gate checks 4,232 deterministic inputs
  with zero mismatches. The gate is wired into proof CI; hosted CI has not yet
  been observed. The initial whole-string solver timeout and callback mismatch
  are preserved as development iterations of this same question. The current
  cohort scorecard has 39 runs and 60 proof-question attempts, with 58 decided:
  48 UNSAT guarantees and ten SAT candidates/replays. It records 39 local
  runnable gates, 50 passing mutation checks, 3,506,570 differential cases,
  zero confirmed impacts, and zero consumer-adopted gates. The latest P6 phase
  sum is 1.4864 seconds; source review, contract authoring, tokens, cost, and
  human active time remain unmeasured. The 6.115-second scope-audit gate run
  remains recorded. A later
  shape-6 P6 wave repeats three v22 questions,
  adding a gate-backed runner calibration without new yield. The v11 triage overlay covers all 14 SAT questions: two refuted
  claims and twelve remaining product candidates, with zero confirmed impact.
  The first P7 15/5 source-review and queue-transition wave is complete and
  documented in its Aidevops bundle. The general P6 operator loop, campaign
  integration, new-cohort yield, consumer adoption, and downstream impact
  confirmation remain open.)
- [x] P7 frozen campaign reaches checkpoint or an evidenced coverage/resource stop. (The first 15/5 wave and its 14-site deterministic complement are closed; v22 reaches 50 distinct eligible exact-pin questions, with 49 decided and one timeout. Three of the webhook census's four question identities were already counted in v21, so only the slug timeout increases the roster. Additive v26 later adds four post-checkpoint Tracecat proof questions; that is retrospective evidence, not a new P7 source review or a success-rate claim.)
- [ ] P8 primary gate outcomes and downstream bug outcomes support a written decision. (Evidence now includes per-repository/dialect stratification, a same-model 11-row fresh source audit, two corrected contract scopes, the reproduced gate, and private evidence packets for all 12 candidates across ten groups. The exact-pinned Tor NEWNYM follow-up confirms a local false-success response-handling defect against the protocol's 5yz failure semantics; deployment impact and external outcomes remain unconfirmed, and the existing reachable-violation count does not change. The matched historical human comparison is unavailable; review time, cost, and tokens are unknown. Recommendation: hold expansion to 100 while testing candidate significance and consumer gate adoption. The plan assigns investment direction to the owner, so the final direction remains pending.)
