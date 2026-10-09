# Historical plan: ModSecurity product-engine recovery

**Status:** superseded on 2026-10-09. The user directly approved the exact
narrow contract recorded in
[`wordpress_modsecurity_ruleset_contract_candidate.json`](../../properties/generated/wordpress_modsecurity_ruleset_contract_candidate.json).
The remaining historical-engine limitation does not block its adoption or
the next corpus intake. The technical recovery outcome below remains useful
context and does not change the adopted contract's narrow scope.

**Candidate:** `Rev3rseSecurity/wordpress-modsecurity-ruleset`

**Pin:** `6bdd250e3b121f79c9b06ea48231cdada8e9dac9`

**Starting state:** the corpus is at `triage-trial`. Its 21 root product
sites were measured and the documented `HEAD /?author=1` request was blocked
on a pinned, maintained alternate ModSecurity image. The historical CI image
tag, `owasp/modsecurity:v3-ubuntu-nginx`, did not resolve during the first
trial. The alternate image is corroboration, not product-engine ground truth.
At the time this plan was written, the narrow rule 22200029 contract remained
`agent_derived` and awaited a user decision. The current adoption record is in
the candidate artifact. See
[`modsecurity-triage-trial-closeout.md`](modsecurity-triage-trial-closeout.md).

## Original objective (superseded)

Use up to three hours of active work to recover the exact historical test
runtime or establish that the available evidence cannot recover it. If
recovered, replay the documented CI behavior against that runtime and make
the narrow contract candidate reproducible. Otherwise, the plan was to leave
a decision packet and pause this cluster until the then-pending user decision
was resolved. That decision is now recorded above, so this pause no longer
applies.

This plan was for engine recovery and evidence close-out. It does not change
the separate disclosure gate or authorize public filing.

## Work blocks

### 0:00–0:25 — freeze the target and verify current artifacts

- Confirm the gate, candidate URL, exact pin, allowlist, and close-out still
  agree. Rebuild gate labels and require byte-identical output.
- Read the pinned test Dockerfile, CI command, Compose/configuration files,
  and referenced image tags from the candidate tree. Record the exact request
  method, target, expected status, enabled rules, and relevant environment
  variables.
- Record current image availability checks and hashes so this attempt does
  not repeat the alternate-engine trial as if it were new evidence.

### 0:25–1:15 — try bounded historical-runtime recovery

- Check the original image registry/tag and archived repository metadata for
  a retained manifest digest. Prefer immutable registry metadata or an
  existing CI artifact over a similarly named image.
- If the old tag is gone, inspect the Dockerfile history and source pin for a
  reproducible build path. A rebuild qualifies as the target runtime only if
  its base image and build inputs can be pinned to the versions used by the
  documented CI; otherwise label it a reconstruction, not the historical
  product engine.
- Capture registry/image digests, platform, ModSecurity engine, connector,
  web-server versions, and the evidence establishing each. Stop this search
  after 50 active minutes if the required versions or immutable inputs cannot
  be established.

### 1:15–2:25 — replay only if the runtime is qualified

- Run the candidate test setup on an isolated local container network, with
  only loopback access from the host. Replay the exact CI-shaped requests:
  `HEAD /` and `HEAD /?author=1` with user enumeration disabled.
- Capture response status and the audit-log rule ID/phase. Then exercise a
  bounded matrix that varies ASCII digit length, letter case, and percent
  encoding only where the documented URI transformation semantics define
  the expected result. Do not expand the contract to arbitrary query strings
  or imply that the rule validates a complete query parameter.
- If a mismatch appears, reduce it to one byte-for-byte witness and replay it
  again on the same qualified runtime. If the runtime was not qualified,
  keep all results explicitly labeled as alternate-engine or reconstruction
  evidence.
- Clean up the isolated containers and network; retain commands, versions,
  statuses, audit excerpts, and hashes needed to reproduce the run.

### 2:25–3:00 — close the technical gate and record the decision packet

- Update the close-out with actual active minutes, recovery attempts, runtime
  identity, request results, and any refuted assumptions. Do not backfill
  timings for earlier work.
- Keep the contract candidate's `agent_derived` provenance and record adoption
  separately. Do not add a product property row or conversion count from the
  alternate engine alone.
- If the historical runtime is recovered and the narrow behavior reproduces,
  record the additional evidence. If not, preserve the engine limitation and
  keep the candidate's claim narrow.
- Rank 3 was held pending the user decision at the time. That hold has now
  been lifted; intake decisions still use the current corpus plan.
  This original plan named rank 5 `tjnel/certgraveyard_yara` as the next intake;
  that intake is now closed out in the parent plan. Rank 3
  (`AvalZ/modsecurity-cli`) remains deferred as a likely wrapper.

## Stop conditions and completion evidence

Stop the engine-recovery work if no immutable historical image or fully
pinned source rebuild is found within the search block, if the CI setup cannot
be reproduced, or if the runtime request semantics remain ambiguous. Record
the blocker rather than substituting the alternate image as ground truth.

The block is complete when the close-out states one of these outcomes:

1. Historical runtime recovered and the documented behavior replayed with
   versions, immutable inputs, and audit evidence; or
2. Historical runtime not recoverable, search paths and evidence recorded,
   alternate-engine limits preserved, and the then-pending user decision
   packet ready.

Do not claim a vulnerability or product proof from corpus fraction, generic
scanner output, or a mirror-only result. The historical user decision gate is
resolved by the adoption record linked above. The alternate-engine limitation
remains part of the evidence record.

## Recorded outcome (2026-10-09)

Outcome 2: the original image tag has no current registry manifest, its image
builder is archived, and the source available for a rebuild does not pin the
base image or OS packages. The archived Dockerfile history does not identify
the digest behind `v3-ubuntu-nginx`. The bounded recovery check took 4 active
minutes; the recovery evidence and alternate-engine limits are in the
[trial close-out](modsecurity-triage-trial-closeout.md#historical-runtime-recovery-check).
At the time of this recorded outcome, rank 3 and later remained held pending
the contract decision. That hold was later lifted as stated above.
