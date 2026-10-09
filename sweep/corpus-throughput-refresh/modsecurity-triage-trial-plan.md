# Three-hour ModSecurity triage-trial work plan

**Candidate:** `Rev3rseSecurity/wordpress-modsecurity-ruleset`

**Pin:** `6bdd250e3b121f79c9b06ea48231cdada8e9dac9`

**Admission:** human-authored `triage-trial`, condition 2, filed in
[`wordpress_modsecurity_ruleset_gate_decision.json`](../../properties/generated/wordpress_modsecurity_ruleset_gate_decision.json).

**Objective:** establish whether this small WordPress WAF ruleset supports a
reproducible, contract-worthy boundary property. The trial centers on the
documented CI request `/?author=1` and a deliberately narrow candidate domain
for rule 22200029. Broader WordPress query semantics are out of scope unless
the source or an independent spec supplies them.

This is a three-hour active-work budget. It does not authorize contract
adoption or disclosure. Do not add the corpus to `WAVE_CORPORA` in this block.

## Work blocks

### 0:00–0:25 — freeze scope and check overlap

- Validate the gate schema, exact pin, candidate-ledger resolution, and
  deterministic gate-label rebuild.
- Compare the candidate's rule family and patterns with the existing
  `coreruleset` inventory and the prior `SEC642/modsec` triage/Smith close-out.
  That older corpus was a CRS fork and ended Smith as NO-GO; do not assume this
  WordPress-specific ruleset is either novel or a duplicate.
- Establish the product file set. The admission probe counted 23 sites,
  including two under `test/`; Smith's ModSecurity extractor scans root-level
  `.conf` files. Exclude test fixtures from product counts and record the
  resulting site count.

**Stop condition:** if the candidate is a duplicate of the already-closed CRS
cluster or the root rule surface cannot be distinguished from tests/vendor
data, document the evidence and propose a Smith re-NO-GO without compiling.

### 0:25–1:10 — materialize and measure the pinned rule set

- Use `scripts/scaffold-smith-corpus.py` and
  `scripts/materialize-corpus.py --gate` to prepare an exact-pin local tree.
- Register the corpus for local Smith measurement with an explicit rule-file
  scope; leave `WAVE_CORPORA` unchanged.
- Run `scripts/measure-corpus-fraction.py --corpus
  wordpress_modsecurity_ruleset --assert-determinism`.
- Record included files, extracted count, encodable count/fraction, compile
  reasons, extractor errors, solver version, artifact hashes, and active
  elapsed time. Keep generated reports and the manifest aligned with the
  fixed pin.

### 1:10–2:35 — spike the `author` enumeration property

- Read the exact source context for rule 22200029, the surrounding
  `wprs_allow_user_enumeration` guard, the test Dockerfile, README, and CI
  request. Write an independent contract candidate before encoding:
  `untrusted-input` HTTP request URI → ModSecurity `block`, with a declared
  request/encoding domain and provenance links.
- Build the repository's Docker test image at the pinned commit if Docker is
  available. Replay the documented baseline (`/` succeeds;
  `/?author=1` returns 403), then test a bounded set of case, percent-encoding,
  delimiter, and numeric-ID variants against both the engine and the mirror.
  If the historical base tag is unavailable, an official maintained image at
  an immutable digest may be used for alternate-engine corroboration; label it
  as such and do not treat it as product-engine ground truth.
- Spike the cheapest valid property shape. If a witness appears, replay it
  byte-for-byte through the pinned ModSecurity engine. For transformation
  behavior, run differential fuzz against the real engine or reduce the claim
  to a documented finite domain. A model result without engine replay is not a
  finding; no witness within a bounded sweep is not a proof.

**Stop condition:** if the target container cannot be built or the engine
version/request URI semantics cannot be pinned, stop product-engine proof at
inventory-only. Record any alternate-engine replay separately. Do not promote
a mirror-only or alternate-engine result to a product contract.

### 2:35–3:00 — close the trial block

- Reconcile extraction/compile totals with the admission probe and explain the
  test-file exclusion.
- Record the property-spike outcome, ground-truth evidence, and actual elapsed
  time. If a candidate survives, write an `agent_derived` draft with trust,
  source, domain, named sink, shape, and provenance; do not add a
  `properties_asked` product row until the user adopts it.
- Close with one of: continue the triage trial on the named survivor, document
  an evidence-backed re-NO-GO, or record an engine/tooling blocker and the
  next smallest action. Only then consider rank 3.

## Completion checks

- Gate and corpus pin agree; labels rebuild byte-for-byte.
- Smith inventory is deterministic and excludes test-only regexes from the
  product denominator.
- Every claimed counterexample has exact-engine replay evidence. Unsupported
  engine behavior, timeout, or unavailable runtime is reported as not proven.
- No product conversion count, contract adoption, public disclosure, or new
  wave membership is inferred from the trial alone.

## Current result (2026-10-09)

- Scope and deterministic Smith measurement completed: 21 root product sites,
  all 21 encodable, zero parse errors. The two sites under `test/` remain
  outside the product denominator.
- The isolated batch produced 19 scanner flags, all source-reviewed and
  recorded in the close-out. No ReDoS finding was reported.
- The historical test base image `owasp/modsecurity:v3-ubuntu-nginx` cannot be
  resolved. The maintained official image was pinned by digest and ran the
  exact candidate rules with the candidate's test `crs-setup.conf`. On
  ModSecurity 3.0.17/Nginx 1.30.5, `HEAD /` returned 200 and `HEAD
  /?author=1` returned 403 with an audit event for rule 22200029. This is
  alternate-engine corroboration only.
- Additional probes confirmed substring overmatching (`?notauthor=1`,
  `?foo=author=1`, and `/foo?author=1`). Those cases are excluded from the
  narrow candidate contract because no independent application contract
  describes their intended behavior.
- A schema-valid `agent_derived` contract draft was written. It is not a
  product result, `properties_asked` row, conversion count, or WAVE member.
- Trial disposition: `triage-continues` on the exact CI-shaped contract
  candidate. The next action is human adoption/rejection of that guarantee or
  recovery of the historical engine; do not advance rank 3 while this cluster
  is held. Active minutes were not separately instrumented, so this is not an
  operator-throughput timing sample.

Full source dispositions and engine evidence:
[`modsecurity-triage-trial-closeout.md`](modsecurity-triage-trial-closeout.md).
