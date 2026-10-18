# Magic JS exact-pin P2 source review

This source review covers the corrected v3 static ECMA inventory for
`magiclabs/magic-js` at the frozen 20-r2 pin
`e9fb233763160316989863b4739c4656133d45b0`.

## Scope and decisions

- 64 inventoried static regex sites reviewed.
- 53 evidence-backed skips, one unresolved email validator, and ten adopted
  contracts / product questions.
- The ten contracts cover three OAuth PKCE challenge encoders, five WebAuthn
  credential JSON encoders, and two DPoP compact-token encoders.
- The adopted contracts prove only the required Base64URL output mapping;
  they do not claim verifier entropy, signature validity, authentication, or
  remote server acceptance.

The ten rows adopted are the `verifierToBase64URL` substitutions in the web,
React Native bare, and React Native Expo OAuth packages; the `Base64URL.encode`
substitutions in OAuth2, Passkey, Wallet Kit, WebAuthn, and Provider; and the
`toBase64Url` / `binToUrlBase64` transformations used to form DPoP tokens.
Their source-bound contracts and independent RFC evidence are in
[`contracts.json`](contracts.json). The normative behavior comes from
[RFC 7636](https://www.rfc-editor.org/rfc/rfc7636) for PKCE,
[RFC 4648](https://www.rfc-editor.org/rfc/rfc4648) for base64url, and
[RFC 7515](https://www.rfc-editor.org/rfc/rfc7515) for JWS compact
serialization.

The wallet-kit email validator remains unresolved. It gates the local login
form, but the pinned repository does not establish its accepted email syntax
or an authoritative server-side enforcement boundary. The Base64-JSON UTF-8
conversion is skipped as transport correctness without a security boundary.
The Provider DPoP UTF-8 decoder is also skipped: its only callers encode
internally built ASCII header/claim objects, so a Unicode-token proof would be
unreachable in this product path. Platform user-agent tests, CSS build
selectors, and bundled semver parsing do not enforce security boundaries.

The scanner review found eleven `#!/usr/bin/env` rows in the v2 inventory;
these were hashbang directives, not regex literals. The ECMA scanner now
skips a leading BOM/hashbang, and inventory v3 removes all 79 matching rows
across Magic JS, Gigachad GRC, Everclaw, and Real Router. A separate dynamic
`new RegExp` at `scripts/utils/esbuild.ts:169` uses keys from the internal
globals build configuration. It is outside the static inventory and does not
receive untrusted runtime input.

## P6 proof wave

The ten adopted properties are registered as no-length-bound, per-codepoint
Base64URL output-image proofs, with one source-weakened plus mutation guard.
Z3 5.0.0 proves all ten properties UNSAT; the guard returns SAT and its `+`
witness is replayed against the exact transformation.

The campaign cap is five adopted contracts per wave, so the frozen roster was
split into [`p6-wave-r1/`](p6-wave-r1/) and
[`p6-wave-r2/`](p6-wave-r2/). Both exact-pin source checks, family mutation
guards, proof batches, and product gates passed. The ten contracts contribute
481,034 distinct per-question Node comparisons with zero mismatches. Each
wave's gate command executed the shared ten-question gate, so two executions
performed 962,068 comparisons in total; the checkpoint counts each question's
evidence once. The source-runner phase sums were 1.0245 and 1.0204 seconds.
The history and wave state record exact source sites and question identities.

The gate imports the five WebAuthn Base64URL encoder modules and the React
Native bare DPoP encoder. It parses and checks the exact source replacement
chains for the three PKCE helpers and Provider DPoP helper. The pinned source
checkout does not contain the CryptoJS dependency, so those four helpers are
not imported: the PKCE replay applies their exact pinned replacement chains
to Node-generated SHA-256 digests, including the RFC 7636 Appendix B test
vector. For the encoder and DPoP byte inputs, the finite differential run
exhausts lengths zero, one, and two, then checks seeded longer buffers. For
each PKCE helper, it checks the RFC vector and 2,048 seeded verifier digests.
This is product-engine regression evidence for Base64URL formatting. It does
not establish verifier entropy, DPoP signature validity, WebAuthn
authentication, or server acceptance.

P6 adds ten contract-backed UNSAT questions and one reusable regression gate,
with no new SAT product candidate, reachable violation, or confirmed impact.
No provider, relying party, or external maintainer was contacted. The latest
retrospective join is [v12](../2026-10-15-p2-existing-evidence-20r2-v12/README.md).

## Reproduction

```sh
.venv/bin/python scripts/build-p2-source-review-evidence.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v3/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v3/sites.ndjson \
  --reviews properties/calibration/2026-10-15-p2-magic-js-source-review/reviews.json \
  --checkout /tmp/regexproof-pinned-sources/magic-js-e9fb233763160316989863b4739c4656133d45b0 \
  --repo-id magiclabs/magic-js \
  --pin e9fb233763160316989863b4739c4656133d45b0 \
  --output properties/calibration/2026-10-15-p2-magic-js-source-review/evidence.json
```

`reviews.json` records each source decision and call-context reference;
`evidence.json` binds those decisions to the exact cohort, source inventory,
source file hashes, and Git blobs. No OAuth provider, WebAuthn service,
DPoP server, or maintainer was contacted.

The P6 proof and Node gate are reproducible with:

```sh
.venv/bin/python scripts/z3-verify.py \
  ME-oauth2-pkce-s256-base64url ME-rn-bare-pkce-s256-base64url \
  ME-rn-expo-pkce-s256-base64url ME-oauth2-webauthn-base64url \
  ME-passkey-base64url ME-wallet-kit-base64url ME-webauthn-base64url \
  ME-provider-webauthn-base64url ME-rn-bare-dpop-base64url \
  ME-provider-dpop-base64url ME-base64url-mutated-plus-leaks \
  --require-ground-truth --json

.venv/bin/python scripts/magic-js-base64url-regression-gate.py \
  --source-root /tmp/regexproof-pinned-sources/magic-js-e9fb233763160316989863b4739c4656133d45b0 \
  --output /tmp/magic-js-base64url-replay.json
```
