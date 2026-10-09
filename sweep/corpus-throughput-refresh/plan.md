# 12-hour plan: refresh mine intake and process eligible repositories

**Goal:** convert current mine inventory into exact-pin probe evidence,
completed gate decisions, and (where approved) post-GO compiler evidence.
The hard deliverable is a verified intake snapshot, bounded contract-slice
reconnaissance, and complete serial probe→gate cycles for as many
source-native clusters as fit. Do not forecast a fixed number of completed
clusters: a GO path includes inventory and conversion close-out, while a
NO-GO path may close faster. The documented 5–7 gated repositories per week
remains an operating target, not a measured 12-hour rate. Human gate
decisions, post-GO Smith work, and contract adoption are contingent on their
own gates. Intake volume alone is not a throughput result.

**As of:** 2026-10-09 02:18 UTC. The manual daily-mine dispatch completed
successfully, and its committed artifacts are validated below.

**Parents:** [`docs/THROUGHPUT-PLAN.md`](../../docs/THROUGHPUT-PLAN.md),
[`docs/MINE-SETUP.md`](../../docs/MINE-SETUP.md),
[`docs/PIPELINE.md`](../../docs/PIPELINE.md), and the exact 20-repository r2
calibration manifest. Keep `DAILY_MINE_CAP=10` while the queue is full.

## Starting snapshot

At the starting revision (`a318c3b`), `pipeline-status.py` reported the
latest successful mine-day drain as 10 admissions on Oct 7, queue pressure
100/100, no completed probes in the rolling seven-day window, 18
`needs_human` rows, and 30.5 backlog weeks. The Oct 8 scheduled mine attempt
failed before producing a summary.

Manual dispatch
`37870246297` completed successfully at the default cap on Oct 9 after about
30 minutes. It added 10 candidates (ledger size 1,413 → 1,423); the queue
remains full at 100. Candidate ledger, queue, gate labels, and conversion
ledger parse as JSON. Rebuilding gate labels from the committed candidate
ledger, tracked-tree features, and sorted gate-decision files produced a
byte-identical artifact; `inputs_hash` excludes the queue. The conversion
ledger is unchanged. Pipeline status now reports 10 admissions on Oct 9, 0
completed probes in the rolling seven-day window, 18 `needs_human` rows, and
30.5 backlog weeks. The work branch is synced through bot commits `f0d157d`
and `a3a808b`; do not dispatch another mine run.

## Calibration preflight result

The read-only audit of artifacts committed at `a318c3b` found **zero
defensible additions** for a 30-repository manifest. Ten off-cohort repos have
matching pins in the candidate ledger and gate probe, positive sites in a
supported family, and candidate-ledger `fork=false`, but the evidence does not
establish a complete/non-oversized scan or curated duplicate independence for
any of the ten. The old calibration pools also contain previously failed attempts, so
those repos are not counted as new additions. No 30-repository manifest will
be frozen in this package. The candidates below are provisional processing
options only; probing them cannot retroactively make them calibration
eligible.

| Family | Repository | Pin | Recorded family sites |
|---|---|---|---:|
| ECMA | `IBM/node-sdk-core` | `16ea5d64204a3b6a92406fe21314d49838981c65` | 52 |
| ECMA | `TimePulse/TimePulse` | `f01084a2e2fb63eaf305cce312d60b6aecd76314` | 411 |
| ECMA | `SveltyCMS/SveltyCMS` | `c48326afe2a9d429f105af9aa786738d970af848` | 2,226 |
| Python `re` | `wagtail/wagtail` | `a5ba34ae86909b3a2e995a8fcc0f1b93e30ee3e5` | 82 |
| Python `re` | `jython/jython3` | `e0d80bbddff0d5465f2da3f9de52bff89ab00e53` | 1,404 |
| Python `re` | `mattrobinsonsre/terrapod` | `5ba7d58bf9ae6c4d41c814e1489be9e42670664d` | 51 |
| Go `regexp` | `apache/pulsar-client-go` | `b47b690105f5063acf1200c58af8697ffcacf444` | 3 |
| Go `regexp` | `olivere/elastic` | `4cdb89f6e627228e7cb3b53e1b1ef8630cc71a0a` | 3 |
| POSIX shell | `open-edge-platform/orch-ci` | `b9d94768d2db3e1250a0416c8878c4c8086d27b9` | 30 |
| POSIX shell | `cyberark/conjur-authn-k8s-client` | `487e9772ef0fc6df463a2b808aa9f59099e63d56` | 35 |

Source fields: `properties/generated/candidate-ledger.json` and each repo's
`*_gate_decision.json`. The gate probe records family sites and per-file
counts, but not complete tree coverage or oversized-file outcomes. The
candidate ledger lacks `duplicate_of` and `partial` evidence. Re-check
current admissions/pins before processing any listed repo.

## Existing contract slice

The best committed lead for contract work is the already-admitted MY-mycelium
cluster's deferred `scripts-bootstrap` idiom. Its wave-1 close-out explicitly
names this as the next unused slice, and the same-pin inventory contains 12
sites (10 encodable) in `scripts/fungi` and `scripts/node-bootstrap.sh`.
There is no ranked list for this slice, and the committed patterns do not by
themselves establish trust boundaries or named sinks. Use it for bounded
Gate-1 source-context reconnaissance, not as a promised 15-site/5-contract
wave. Record all 12 keep/drop outcomes. If fewer than 15 viable survivor sites
exist, record the population shortfall and do not claim a full conversion
wave. Product rows still require human adoption, actual active-review timings,
and the full conversion close-out. Continue this cluster only; do not reopen
its closed `control-failclosed` sites or mix in another repo/cluster until the
slice has a documented close-out.

**Read-only exact-pin review outcome:** no defensible human contract survived.
Seven fixed-pattern sites are comment/help/version/status parsing; two raw
`$p` interpolation sites are unencodable. Three pattern shapes entered the
keep pile, but source context showed host-local `ss` or configuration/status
checks feeding display or availability rollback, not a proven security
boundary. `control/vocab.json:32–41` allowlists port keys, but
`nb_render_params.sh:145–166` does not establish a numeric-only value domain;
the possible `listen_port` metacharacter question therefore remains
unsupported. Close this slice with no product rows and no conversion-ledger
count change. Once that close-out is recorded, the next cluster may start.
Full row-by-row dispositions:
[`mycelium-scripts-bootstrap-closeout.md`](mycelium-scripts-bootstrap-closeout.md).

## First scored candidate — NO-GO filed

The refreshed score-v1 ranking put `iosifache/semgrep-rules-manager` first
among 50 rows. It is a Python repository (recorded size 1,288) and its YAML
regex-shaped files are scanned by the generic rule-file path. Exact probe:
`https://github.com/iosifache/semgrep-rules-manager@6b62771efadf16f8e7112d6918029c768cefba81`.
The first attempt was refused at disk admission because the 2,048 MB fetch cap
exceeded the 500 MB total budget; the corrected 500/500 MB run completed with
no disk or clone error (73,070 fetched bytes, 29 files walked, 1.25 s clone,
0 extractor errors).

The probe found one `py_re` site, `semgrep_rules_manager/sources.py:43:26`,
call kind `substitution`, pattern `\n- id: \".*\/(.*)\"\n`, and no predicted
buckets. It is in `IDStandardizationPreprocessor.process_content`: the tool
reads downloaded third-party Semgrep rule YAML, rewrites rule IDs, and writes
the file back. `sources.yaml` and the CLI/core call path confirm a source
management utility; the regex does not guard a security sink. The repository
name triggered `security_boundary=deterministic-true`, so batch returned
`needs_human` and its restricted auto-NO-GO refused. Under
[`sweep/corpus-admission-gate.md`](../corpus-admission-gate.md), the escape
hatch requires a security-boundary corpus with a concrete candidate property;
this repo manages external rules but the one scanned regex only normalizes a
rule ID. No new dialect/flag, property shape, or scale condition is met. The
name-level positive signal alone does not establish the escape hatch. No gate
artifact, Smith run, contract, or conversion row had been created at the time
of the probe. The user chose NO-GO on Oct 9. The human-authored
[`semgrep_rules_manager_gate_decision.json`](../../properties/generated/semgrep_rules_manager_gate_decision.json)
records that decision; candidate-ledger review state and gate labels were
rebuilt from it. No Smith run, contract, or conversion row was created. This
candidate is closed, so rank 2 was probed next.

## Second scored candidate — triage-trial filed

Exact pin:
`https://github.com/Rev3rseSecurity/wordpress-modsecurity-ruleset@6bdd250e3b121f79c9b06ea48231cdada8e9dac9`.
The first inventory reported four sites because the extractor missed `SecRule`
patterns that omit an explicit operator. [ModSecurity defaults those rules to
`@rx`](https://github.com/owasp-modsecurity/ModSecurity/wiki/Reference-Manual-%28v3.x%29/3abdf1ad6860e7ae7f5b1d4f19534052946bd2e8#rx);
its [`SecRule` action list is optional](https://github.com/owasp-modsecurity/ModSecurity/wiki/Reference-Manual-%28v3.x%29/3abdf1ad6860e7ae7f5b1d4f19534052946bd2e8#secrule).
The extractor now captures both forms, including an empty implicit regex,
and excludes operator arguments and variable selectors from the default-
operator path. The focused extractor suite passes (14 tests).

The exact-pin rerun completed as `needs_human`: 11 files walked, 23 `pcre`
sites, zero extractor errors, and `security_boundary=deterministic-true`. The
per-file counts are `03-BRUTEFORCE.conf` 4, `04-EVENTS.conf` 8,
`05-HARDENING.conf` 9, and `test/modsecurity.conf` 2. The initial cached probe
fetched 37,730 bytes; the verification rerun hit cache and fetched zero bytes.
Its manifest digest is
`1a05ff21d30922f951fc9629dc6df3d8cff3014057877d631a623e3d8ed0fe87`.

There is a concrete condition-2 property candidate: when user enumeration is
disabled, requests like `/?author=1` should be blocked. [Rule 22200029](https://github.com/Rev3rseSecurity/wordpress-modsecurity-ruleset/blob/6bdd250e3b121f79c9b06ea48231cdada8e9dac9/05-HARDENING.conf#L95-L108)
applies lowercase, URL decode, and trim to attacker-controlled `REQUEST_URI`,
then blocks `author=[0-9]+`. The [README](https://github.com/Rev3rseSecurity/wordpress-modsecurity-ruleset/blob/6bdd250e3b121f79c9b06ea48231cdada8e9dac9/README.md#L124-L135)
documents that setting 0 blocks the request, the [test Dockerfile](https://github.com/Rev3rseSecurity/wordpress-modsecurity-ruleset/blob/6bdd250e3b121f79c9b06ea48231cdada8e9dac9/test/Dockerfile#L18-L20)
sets it to 0, and [CI](https://github.com/Rev3rseSecurity/wordpress-modsecurity-ruleset/blob/6bdd250e3b121f79c9b06ea48231cdada8e9dac9/.travis.yml#L15-L18)
expects HTTP 403. Rule 22200039 is another possible blocked-URI property for
the load-scripts DoS pattern, but should be treated separately. Rule 22200040's
`wp-cron.php` pattern may be overly broad and is not a contract candidate
without more evidence. The user selected `triage-trial` on Oct 9; the
human-authored [`wordpress_modsecurity_ruleset_gate_decision.json`](../../properties/generated/wordpress_modsecurity_ruleset_gate_decision.json)
records condition 2, its source evidence, and the escape-hatch basis. This
starts a bounded Smith/property spike, not contract adoption. The trial work
measured 21/21 root product sites encodable and source-grounded every
generic batch flag. Rule 22200029 blocked the CI-shaped HEAD request with a
phase-1 audit event on a pinned alternate ModSecurity engine; the repository's
historical CI image could not be resolved. The exact CI-shaped contract is
available as an `agent_derived` draft only. The trial close-out records the
full findings and replay limits in
[`modsecurity-triage-trial-closeout.md`](modsecurity-triage-trial-closeout.md).
Keep the candidate at `triage-trial` and hold rank 3 pending the human contract
decision and any exact historical-engine recovery. The next bounded
autonomous task is the three-hour historical-runtime recovery/close-out plan
in [`modsecurity-engine-recovery-plan.md`](modsecurity-engine-recovery-plan.md);
it does not open another candidate while this gate is pending. After the
human gate closes, rank 5 `tjnel/certgraveyard_yara` is the next strong YARA
intake option; rank 3 remains deferred.

## Score-v1 ranked screening snapshot

Ranked from the refreshed admitted ledger (`score-v1`, top 15); screen notes
are source/metadata checks except for the exact-pin probes of ranks 1 and 2.
Keep this order as the provisional queue and process serially. `tjnel` is the
next strong YARA option after the rank-2 gate closes; its rule files match a
supported extractor, with a larger and more recent recorded tree than the
other top-ranked YARA options.

| Rank / score | Repository @ pin | Query; language / size | Screen result |
|---|---|---|---|
| 1 / 96 | `iosifache/semgrep-rules-manager` @ `6b62771efadf16f8e7112d6918029c768cefba81` | `filename:semgrep.yml OR filename:semgrep.yaml`; Python / 1,288 | NO-GO filed per user gate; internal ID-rewrite substitution, no contract candidate. |
| 2 / 91 | `Rev3rseSecurity/wordpress-modsecurity-ruleset` @ `6bdd250e3b121f79c9b06ea48231cdada8e9dac9` | `filename:crs-setup.conf OR filename:REQUEST-942-APPLICATION-ATTACK-SQLI.conf`; Dockerfile / 26 | Probe and Smith inventory complete: 23 admission sites / 21 product sites, all 21 encodable; 22200029 replayed on a pinned alternate engine; human contract decision pending. |
| 3 / 89 | `AvalZ/modsecurity-cli` @ `8ae8455ec58c65a8b204a1c6a40065b39fc67b73` | `filename:crs-setup.conf OR filename:REQUEST-942-APPLICATION-ATTACK-SQLI.conf`; Python / 59 | Likely a small wrapper rather than dense rule corpus; defer. |
| 4 / 89 | `RustyNoob-619/YARA` @ `0539dbed04026979ba00e140cfca6951b602890b` | `path:rules extension:yar OR extension:yara`; YARA / 845 | Direct supported YARA input, but smaller recorded tree than rank 5. |
| 5 / 89 | `tjnel/certgraveyard_yara` @ `cac568463861fdf80386a50958951cc06b3e9bbb` | `path:rules extension:yar OR extension:yara`; YARA / 15,374 | Strong follow-up: direct supported YARA files, larger tree, pushed Aug 2026. |
| 6 / 87 | `evild3ad/yara` @ `2f00826a4ee35323a10abbc788a6bbe6308f1215` | `filename:index.yar`; YARA / 652 | Supported direct input, lower expected yield. |
| 7 / 86 | `rakeshf/wordpress-yara` @ `3c2f25ad7f5951fae27742314b369b01060f0edf` | `path:rules extension:yar OR extension:yara`; YARA / 89 | Supported, but very small tree. |
| 8 / 85 | `Raspirus/yara-rules` @ `7a30e8d1ca0fcb3ba605a4bd18fae44fd6bf387a` | `path:rules extension:yar OR extension:yara`; YARA / 5,936 | Good fallback: direct rules and recent push (Aug 2026), smaller than rank 5. |
| 9 / 83 | `kjakub/docker-nginx-modsecurity-v3-waf` @ `e4b6a610111809b598fcd732a4e7aaf990861a3f` | `filename:crs-setup.conf OR filename:REQUEST-942-APPLICATION-ATTACK-SQLI.conf`; Shell / 152 | Supported `.conf` path, but small and last pushed 2022. |
| 10 / 83 | `quanticsoul4772/zeek-yara-integration` @ `450e46964332a0bed4de2448b0fa960ffcdef24e` | `filename:rules.yar path:rules`; Python / 1,111 | Supported YARA file; integration repo may have sparse rule content. |
| 11 / 75 | `RandomRhythm/YARA_Rules_Project_Sorted_Ruleset` @ `81d9e1fd3a194e95ff8b043784441b4e6e914ab1` | `filename:index.yar`; YARA / 1,828 | Supported; “sorted ruleset” suggests possible duplicate overlap, defer. |
| 12 / 71 | `ChrisPritchard/slack-yara-scanner` @ `d18c536e435470d642b93a307efcbb198cf48b32` | `path:rules extension:yar OR extension:yara`; YARA / 442 | Supported, small and last pushed 2022. |
| 13 / 71 | `ulisesrc/Yara-Rule` @ `5fa44ce2b6b660348fac34626df6f51fd1ba12d7` | `filename:index.yar`; YARA / 3,127 | Supported, but last pushed 2019. |
| 14 / 71 | `vulnerabivoro/filtered-yara-rules` @ `a5bcb5e2490f502b680de82371b4f0b4b342fa96` | `filename:index.yar`; YARA / 19,728 | Large supported surface, but last pushed 2019 and overlap risk; defer to recent candidates. |
| 15 / 70 | `cloudposse/atmos` @ `e4269500304cba367d6a204ba3901c539ca943fc` | `filename:.trufflehog.yml OR filename:.trufflehog.toml OR filename:trufflehog.yml`; Go / 191,455 | High clone/walk cost; query targets scanner config and does not establish a regex-bearing corpus. |

All score, pin, query, language, and size fields are from the refreshed
candidate ledger/ranker. The screen is not a complete clone-size, fork, or
site inventory; probe outcomes and gate evidence decide advancement.

## Work sequence

1. **0–1 hour — refresh and validate the intake snapshot.** The default-cap
   dispatch completed successfully; do not dispatch another. Its result,
   committed candidate ledger, overflow queue, gate-label `inputs_hash`, and
   conversion ledger were validated separately. The label hash binds candidate
   ledger bytes, tracked-tree features, and sorted gate decisions; it excludes
   queue bytes. The branch is synced through both bot commits.
2. **In parallel during hour 0–1 — calibration eligibility preflight, before
   probing.** This audit is complete using only artifacts committed at
   `a318c3b`; the result and provisional candidates are recorded above. No
   candidates meet the full evidence bar, so leave the 30-repository manifest
   absent. Do not use newly mined/probed rows to fill it or use a later probe
   to change this result.
3. **1–2 hours — rank and screen.** Use score-v1 to shortlist up to 15
   unprocessed candidates from the admitted candidate ledger. Rank does not
   drain or rank the overflow queue; that queue drains on later mine days.
   Record exact `url@pin`, query/language, and the reason each row advances or
   stops. Do not treat rank as evidence of supported dialect, nonempty sites,
   or non-fork status; verify those from pinned probe/gate evidence. Exclude
   any frozen calibration additions. Do not use score-v2 or expand the intake
   cap.
4. **2–4 hours — close the Mycelium `scripts-bootstrap` reconnaissance.**
   The exact-pin review of all 12 sites is complete; see the
   [`mycelium-scripts-bootstrap-closeout.md`](mycelium-scripts-bootstrap-closeout.md).
   No site supports a defensible contract, so no human adoption request or
   product row is due.
   This is a reconnaissance close-out, not a completed conversion wave. It
   closes the deferred slice without reopening `control-failclosed`.
5. **4–10 hours — serial candidate-cluster cycles.** Determine each source-
   native cluster from its trust map and product engine; do not assume one
   GitHub URL always equals one cluster. Finish the active cluster's probe,
   batch inventory, and gate before opening another; do not probe separate
   clusters in parallel. Use isolated checkouts and separate batch
   cache/state/output paths. Probe at the exact pin with
   `python -m regexproof.probe --batch`. Record resolved pin, outer-record
   `files_walked`, extracted regex sites and per-file sites, dialect counts,
   predicted buckets, construct/flag counts, extractor errors, and
   `security_boundary`. Have a subagent review evidence for the active cluster
   only. Apply documented auto-NO-GO rules; present GO/triage recommendations
   for human decisions and do not label a pending draft as gated. On GO or
   chosen triage, run the post-gate Smith inventory/compile. Before opening a
   conversion wave, rank up to 15 survivors from one unused idiom bucket and
   read 50–150 source lines around every site. Record a human review outcome
   and actual active-review time for every site, including skips. If fewer
   than 15 sites are available, record the population and do not claim a full
   15-site wave. A human adopts at most five contracts with named sinks.
   Spike each property in a throwaway script first, then encode the cheapest
   valid shapes. Every shipped family needs a mutation guard. Run the harness
   with `--all --require-contract --require-ground-truth`; TIMEOUT/`unknown`
   is not a pass. Ground-truth SAT witnesses in the product engine. For
   expected-UNSAT shape-3 properties, use differential fuzz against the real
   cluster engine rather than witness replay. Emit conversion rows and close
   the slice naming the next unused bucket or a stop decision before opening
   another cluster.
   On NO-GO, record the decision and rationale before moving on. The completed
   cycle count is observed, not a fixed promise.

   Probe walkers skip files over their configured per-file threshold; they do
   not emit a complete oversized-file or unsupported-dialect inventory.
   Treat zero extracted sites as an observed zero for this registered
   extractor set, not proof the repository has no regexes. Record explicit
   clone/disk-budget and extractor errors; defer full tree-size and
   unsupported-language findings to calibration/Smith scans. Do not count
   post-GO Smith extraction/compile as part of probe output. If a human
   gate/adoption decision is pending, hold the active cluster and continue
   only work that does not open another one.
6. **10–11.5 hours — reconcile throughput artifacts.** Verify the gate-label
   hash against the candidate ledger, inspect queue state separately, and
   verify the regenerated conversion ledger. Update pipeline status and record
   mine admits, completed probe drafts, actual gate outcomes, Smith
   completions, sites, dialects, contracts asked/adopted, and encodable
   fractions as separate counts. Keep repository processing time separate
   from human contract-review minutes.
7. **11.5–12 hours — independent close-out.** Have a read-only reviewer audit
   gate evidence, artifact hashes, candidate exclusions, and any manifest
   digest/order. Report exact counts and remaining blockers; make no product
   efficacy claim from ingestion alone.

## Stop and human gates

- Stop a candidate on pin drift, incomplete probe, zero registered sites,
  explicit clone/disk-budget failure, duplicate/fork status, or unresolved
  evidence; record the actual result and advance to the next candidate. Do
  not claim a full oversized-file or unsupported-dialect audit from probe
  output alone.
- Do not change mine cap, score-v1, or allocator weights. Do not publish,
  disclose, or file an upstream finding as part of this work.
- Queue refresh, ranking, probing, and gate recommendations require no new
  human decision. GO/triage decisions are usually human-authored; request those
  decisions with the exact probe drafts. Human input is also required to adopt
  product contracts, change the 50-property first checkpoint / 100 preferred
  product bar, or authorize disclosure. Do not invent human review minutes.
- Do not freeze a 30-repository manifest unless ten additions qualify from
  evidence committed at the starting revision, before any checkout or
  observation in this work package. Do not use new mine/probe output to fill
  the ten additions. A reasoned no-freeze result is an acceptable outcome.
