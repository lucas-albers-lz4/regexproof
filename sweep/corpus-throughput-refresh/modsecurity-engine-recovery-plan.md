# Three-hour follow-up: resolve the ModSecurity product-engine gate

**Candidate:** `Rev3rseSecurity/wordpress-modsecurity-ruleset`

**Pin:** `6bdd250e3b121f79c9b06ea48231cdada8e9dac9`

**Starting state:** the corpus is at `triage-trial`. Its 21 root product
sites were measured and the documented `HEAD /?author=1` request was blocked
on a pinned, maintained alternate ModSecurity image. The historical CI image
tag, `owasp/modsecurity:v3-ubuntu-nginx`, did not resolve during the first
trial. The alternate image is corroboration, not product-engine ground truth.
The narrow rule 22200029 contract remains `agent_derived`; human adoption or
rejection is still required. See
[`modsecurity-triage-trial-closeout.md`](modsecurity-triage-trial-closeout.md).

## Objective

Use up to three hours of active work to recover the exact historical test
runtime or establish that the available evidence cannot recover it. If
recovered, replay the documented CI behavior against that runtime and make
the narrow contract candidate reproducible. If not, leave a precise human
decision packet and stop this cluster. Do not open another candidate cluster
while the ModSecurity human gate remains pending.

This is engine recovery and evidence close-out, not contract adoption, a new
corpus wave, or permission to file or disclose a security finding.

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

### 2:25–3:00 — close the technical gate and hand off the human decision

- Update the close-out with actual active minutes, recovery attempts, runtime
  identity, request results, and any refuted assumptions. Do not backfill
  timings for earlier work.
- Keep the contract candidate `agent_derived` unless a human adopts its
  exact guarantee. Do not add a product property row or conversion count
  from the alternate engine alone.
- If the historical runtime is recovered and the narrow behavior reproduces,
  prepare the exact contract adoption packet for review. If not, state the
  remaining engine limitation and present the existing narrow candidate for
  human adoption/rejection based on the available source evidence.
- Keep rank 3 and later candidates held until this human gate is resolved.
  After the active cluster closes, the next intake screen is the rank-5
  YARA candidate `tjnel/certgraveyard_yara` at the pin in the parent plan;
  rank 3 (`AvalZ/modsecurity-cli`) remains deferred as a likely wrapper.

## Stop conditions and completion evidence

Stop the engine-recovery work if no immutable historical image or fully
pinned source rebuild is found within the search block, if the CI setup cannot
be reproduced, or if the runtime request semantics remain ambiguous. Record
the blocker rather than substituting the alternate image as ground truth.

The block is complete when the close-out states one of these outcomes:

1. Historical runtime recovered and the documented behavior replayed with
   versions, immutable inputs, and audit evidence; or
2. Historical runtime not recoverable, search paths and evidence recorded,
   alternate-engine limits preserved, and the human contract decision packet
   ready.

Do not claim a vulnerability or product proof from corpus fraction, generic
scanner output, or a mirror-only result. The remaining human gate decides
whether the narrow, documented request guarantee is adopted or rejected.
