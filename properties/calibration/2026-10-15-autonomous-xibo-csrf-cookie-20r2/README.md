# Xibo OAuth consent CSRF-cookie capture calibration

This is a one-question, retrospective calibration at the frozen 20-r2 pin
`xibosignage/xibo-cms@978def55c8e68cab3a50a7ee4725039da753f0a1`. It is not a
15-site review wave, a prospective sample, or a claim about conversion yield.

## Source and contract

The regex is
`(?:^|;\s*)XSRF-TOKEN=([^;]*)` in
`frontend/src/pages/Administration/Applications/Authorize/AuthorizeApplication.tsx:42`.
The exact P2 inventory identity is `:42:38`, regex ID
`ea730a13393d4601bafd7a851cf69403`; the initial helper-name anchor was
corrected to this file/line/column identity before the final roster and
checkpoint were rebuilt. The exact source-file SHA-256 is
`8377f717735d9efe5c0148e2691c3d36e91395b91ebaaa61045601d073128513`.
The frozen raw source inventory had this row marked `unreviewed`; the
contract and one-site replay are retrospective source-backed evidence and do
not stand in for the cohort's 15-site review procedure.

The caller places `getCsrfTokenFromCookie()` in the hidden `csrfToken` field of
the native POST to `json/application/authorize`. The pinned route table registers
the authorization POST, `web/json/index.php` installs `CsrfGuard`, and that
middleware checks the form field against the session token with `hash_equals`.
`issueToken()` creates a 40-character lowercase-hex value with
`bin2hex(random_bytes(20))`. The other three source files and their hashes are
bound in [`gate-report.json`](gate-report.json). The adopted contract and the
pre-outcome one-question roster are
[`contract.json`](contract.json) and
[`pre-outcome-roster.json`](pre-outcome-roster.json).

The P2 extractor recorded `per-alternative-anchor`, so it did not compile the
whole expression. The formal harness therefore proves the exact capture-body
claim only: every ASCII character admitted by `[^;]` differs from `;`, with no
string-length bound. It does not claim that the Z3 model formalizes JavaScript
search or duplicate-cookie ordering.

## Proof and product gate

The capture-body property is UNSAT. A mutation widens the exact pinned group
from `([^;]*)` to `(.*)`; Z3 finds `;`, and a ground-truth callback runs the
mutated source helper in Node and reproduces the spill into `; session=neighbor`.
The real, unmodified helper agreed with an independent cookie-pair parser on
1,000 generated valid-token cookie strings plus seven missing, empty, tab, and
similar-name controls. The gate verifies the exact clean source pin and
checks the caller, route, JSON entrypoint, and middleware source digests.

This is a useful CSRF-token extraction and regression invariant, not a finding:
the current helper passes, and an over-captured value fails the backend's
exact token comparison. No security impact was confirmed. The replay runs the
browser helper in Node but does not launch a browser or Xibo's PHP application;
duplicate cookie names and native browser ordering are outside its domain.
No external report was sent.

## Reproduction

```sh
.venv/bin/python scripts/xibo-csrf-cookie-regression-gate.py \
  --output properties/calibration/2026-10-15-autonomous-xibo-csrf-cookie-20r2/gate-report.json

.venv/bin/python scripts/build-xibo-csrf-cookie-evidence.py
.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-autonomous-xibo-csrf-cookie-20r2/checkpoint.json

.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --checkpoint-root properties/calibration \
  --conversion-root properties/generated \
  --repo-root /home/lalbers/gitroot/regexproof \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v6

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v6/checkpoint.json
.venv/bin/python scripts/freeze-question-history-index.py
```

The gate is wired into the CI proof job. The local proof-and-gate run took
1.073 phase-sum seconds and recorded one reviewed site, one adopted contract,
one UNSAT question, one local gate, one mutation, and 1,007 differential cases.
Review/adoption time, token use, cost, and human active time remain unknown.

The refreshed P2 v6 aggregate has 22 unique questions (16 UNSAT and six
ground-truthed SAT pending product triage), 11 useful local gates, 17
product-engine replays, and 47,328 differential cases. Its 50-question
shortfall is 28. The Xibo row adds one useful proof/gate, not a SAT candidate.
Full details are in the [v6 aggregate](../2026-10-15-p2-existing-evidence-20r2-v6/README.md)
and [agent-only scorecard](../2026-10-15-autonomous-scorecard-20r2-after-xibo-csrf.json).
