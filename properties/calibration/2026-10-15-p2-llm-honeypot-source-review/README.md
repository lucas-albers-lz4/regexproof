# llm-honeypot-intelligence exact-pin P2 source review

This retrospective review expands P2 source coverage and adds two source-bound
product questions to the 20-r2 evidence checkpoint. It is not a prospective
sample, a 15-site ranked allocation, a claim that sensitive data was exposed,
or evidence that a deployed Tor rotation failed.

## Source review

- Repository: `Leviticus-Triage/llm-honeypot-intelligence`
- Exact commit: `65624396e263074bb8cb2e049f9a9ec6215ea5c1`
- Frozen cohort: `2026-09-12-calibration-20-r2`
- Inventory: P2 source inventory v2, 16 raw POSIX-shell sites at this pin.
- Outcome: 14 evidence-backed skips, zero unresolved sites, two adopted
  contracts. `reviews.json` records each site; `evidence.json` binds those
  dispositions to the source inventory and checkout.
- All 16 reviewed sites are included in the repository's refreshed
  duplicate-prevention history index; the two proof attempts are also recorded
  as asked identities.
- Both adoptions were reviewed and adopted under the standing user delegation.
  The review artifact records that author and second reviewer used the same
  model; it should not be read as independent human review.

The first contract concerns `scripts/sync-to-github.sh:76`. The helper is
described as stripping private IPs from eligible generated artifacts before
commit and push, but its expression only covers `192.168.*.*`. RFC 1918 also
defines `10/8` and `172.16/12`; exact-function replay leaves representative
addresses from those ranges unchanged. The formal SAT witness is a canonical
`10/8` address. This proves an expression gap in the pinned helper, not that a
real artifact contained an address or that one was published.

The second contract concerns `spiderfoot-toolbox/tor-gateway/rotate-tor.sh:34`.
`send_newnym` sends AUTHENTICATE, SIGNAL NEWNYM, and QUIT, then searches the
combined response for `250 OK`. A local fixture with successful
AUTHENTICATE, failed SIGNAL NEWNYM, and a final QUIT response makes the exact
function report success. This proves the pinned response-sequencing behavior;
it does not show that a deployed Tor service returned this sequence or that a
scan continued on an unchanged exit.

## Proof and product replay

`proof-report.ndjson` contains six contract-bound harness results:

| Property | Result | Ground truth |
|---|---|---|
| 192.168/16 coverage | UNSAT | The property is limited to the pinned expression's covered range. |
| RFC 1918 redaction | SAT | Exact pinned `sed` leaves a 10/8 witness unchanged. |
| Embedded-address mutation guard | SAT | Real helper leaves embedded input unchanged under the weakened regex. |
| Constrained Tor failure-only response | UNSAT | The fixed failure-only transcript is rejected by the success predicate. |
| Tor response sequencing | SAT | Exact `send_newnym` reports success after AUTHENTICATE 250 and SIGNAL NEWNYM 5xx. |
| Tor matcher mutation guard | SAT | The widened matcher accepts a failure-only fixture in the real function. |

The Tor failure-only property uses a bounded response family (the registered
550/551/552/553/555 statuses and fixed `Internal error` text). It does not
prove behavior for every possible Tor ControlPort response. The primary Tor
counterexample includes `250 OK\r\n552 Internal error\r\n250 closing connection\r\n`.

`product-replay.json` records the source-function replays and engine versions.
The local regression gate checks all 65,536 canonical `192.168/16` addresses,
65,541 sanitizer sample, mutation, and differential cases total, and four Tor
response fixtures. It uses GNU sed 4.9, GNU grep 3.11, and a local fake `nc`;
it makes no external network request and reads no project data or credentials.

The P6 runner artifacts are under `p6-wave-r1/`; its gate result is also
persisted as `product-replay-p6.json`. The dry run verified the
source pin and gate coverage. The real run verified both adopted contracts,
passed both family mutation guards and the local gate, reproduced both SAT
witnesses, and persisted both attempts as `pending_product_triage`. Its
terminal state is `needs_review` and the command exits 1 because SAT findings
require disposition. No question was dropped or marked a successful campaign
close-out.

The gate configuration binds a local source checkout at
`/tmp/regexproof-pinned-sources/llm-honeypot-intelligence-65624396e263074bb8cb2e049f9a9ec6215ea5c1`.
Reproduction requires a clean checkout at that exact commit or changing the
`--source-root` argument to the same clean pin; the runner itself verifies
the commit and source file digests.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-source-review-evidence.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --reviews properties/calibration/2026-10-15-p2-llm-honeypot-source-review/reviews.json \
  --checkout /tmp/regexproof-pinned-sources/llm-honeypot-intelligence-65624396e263074bb8cb2e049f9a9ec6215ea5c1 \
  --repo-id Leviticus-Triage/llm-honeypot-intelligence \
  --pin 65624396e263074bb8cb2e049f9a9ec6215ea5c1 \
  --output properties/calibration/2026-10-15-p2-llm-honeypot-source-review/evidence.json

.venv/bin/python scripts/z3-verify.py \
  LH-llm-honeypot-private-ip-192-168-coverage \
  LH-llm-honeypot-private-ip-rfc1918-redaction \
  LH-llm-honeypot-private-ip-embedded-search-mutation \
  LH-llm-honeypot-tor-failure-only-response-rejected \
  LH-llm-honeypot-tor-newnym-response-sequencing \
  LH-llm-honeypot-tor-mutated-response-acceptance \
  --require-ground-truth --require-contract --require-domain \
  --fail-on-property-failure --json \
  > properties/calibration/2026-10-15-p2-llm-honeypot-source-review/proof-report.ndjson

.venv/bin/python scripts/llm-honeypot-boundary-regression-gate.py \
  --source-root /tmp/regexproof-pinned-sources/llm-honeypot-intelligence-65624396e263074bb8cb2e049f9a9ec6215ea5c1 \
  --output properties/calibration/2026-10-15-p2-llm-honeypot-source-review/product-replay.json

.venv/bin/python scripts/run-autonomous-proof-wave.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --roster properties/calibration/2026-10-15-p2-llm-honeypot-source-review/roster.json \
  --campaign properties/calibration/autonomous-corpus-campaign.json \
  --state-dir properties/calibration/2026-10-15-p2-llm-honeypot-source-review/p6-wave-r1 \
  --wave-id llm-honeypot-boundary-p2-r1 \
  --corpus llm-honeypot-intelligence \
  --idiom-bucket p2-shell-boundary-calibration \
  --checkout Leviticus-Triage/llm-honeypot-intelligence=/tmp/regexproof-pinned-sources/llm-honeypot-intelligence-65624396e263074bb8cb2e049f9a9ec6215ea5c1 \
  --gate properties/calibration/2026-10-15-p2-llm-honeypot-source-review/gate.json \
  --status
```

The final P2 aggregate is documented in
[`2026-10-15-p2-existing-evidence-20r2-v7`](../2026-10-15-p2-existing-evidence-20r2-v7/README.md).
Confirmed security impact, consumer adoption, external reports, maintainer
confirmations, and third-party fixes: zero.
