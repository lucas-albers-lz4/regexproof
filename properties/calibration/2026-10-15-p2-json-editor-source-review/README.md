# json-editor exact-pin P2 source review

This is a complete raw-regex review for one frozen cohort member. It covers
only `json-editor/json-editor` at the 20-r2 pin and does not close P2.

## Scope and result

- Repository: `json-editor/json-editor`
- Pin: `b31ddabecf4ed3209d37a2f5b29956120cd8f9ce`
- Extracted ECMA sites reviewed: **96**
- Evidence-backed skips: **94**
- Unresolved: **1**
- Adopted contracts / product questions: **1**

The review covers 23 implementation sites under `src/`, four webpack build
configuration sites, 53 regexes in the checked-in Ajv validator bundle loaded
by the docs demo, and 16 test or issue-fixture sites. The raw site count is not
a security-candidate count.

## Adopted question

`EnumEditor.build` precomputes each `schema.enum` value through `getHTML`, and
`refreshValue` assigns the cached value to `display_area.innerHTML`. The
string branch uses three ordered global replacements (`&`, `<`, `>`). One
source-anchored product question covers this composite transformation and
prevents counting its three regex literals as duplicate questions. Its input
is application schema configuration. The contract is limited to string
leaves; it does not cover object keys or other HTML contexts.

The adopted contract, source evidence, frozen one-question roster, Z3 property,
exact-source mutation guard, Node product gate, and P6 state are stored in this
bundle. The gate imports the pinned `EnumEditor` method, compares its output
with an independent character map across every Unicode scalar value and
additional whole-string cases, and verifies that weakening the `<` replacement
reproduces a raw delimiter.

## P6 wave history and outcomes

The first runner execution, [`p6-wave-r1/`](p6-wave-r1/), proved the property
UNSAT and reproduced the `<` mutation, but its Node differential command had a
quoting error while building a JavaScript test alphabet. The runner correctly
recorded a failed local gate and `needs_review`; the attempt remains in the
record. After correcting the gate command, a separate fresh run,
[`p6-wave-r2/`](p6-wave-r2/), passed the same proof and mutation guard and
compared 1,116,985 exact-source cases with an independent character map: zero
mismatches. The checkpoint join then exposed that the contract's generic
`:replace` anchor matched three regexes on the same source line, so it could
not identify the adopted ampersand site. The site identity now uses the
inventory's exact `column-24` selector, verified by both the runner and P2
checkpoint matcher. The fresh, correctly bound
[`p6-wave-r3/`](p6-wave-r3/) run passed the proof, mutation guard, and same
1,116,985-case gate. The duplicate executions add no extra unique question;
v11 matches one source question and retains the two earlier ambiguous attempts
as excluded history.

The autonomous phase-sum log records r1 as 0.6784 seconds, r2 as 1.7385
seconds, and the exact-identity r3 run as 1.7286 seconds. Those measurements
cover P6 execution only; source review, contract authoring, and checkpoint
identity repair preceded r3. Human active minutes, tokens, and cost remain
unknown. Useful evidence adds one contract-backed proof and one unique local
runnable gate. The only SAT result is the intentional mutation witness; no
product bug, reachable violation, or security impact was established. No
external report, maintainer confirmation, or fix was produced.

## Unresolved site

`Base64Editor.refreshPreview` captures everything before the first `;` or `,`
in a data URI and interpolates the capture into `preview.innerHTML`. The regex
does not restrict the capture to MIME-token characters. The source establishes
the HTML sink, but does not establish whether initial editor values can be
controlled by an untrusted party or document a separate safe-rendering
requirement for malformed media metadata. Keep this as an unresolved review
item; it is not an adopted contract, product question, or confirmed XSS.

Other skipped sites support build-path selection, editor/UI formatting, UUID
generation, format UX, documentation examples, and tests. The Upload editor's
MIME wildcard comparison is a client-side UI filter before an application
callback and is not a server-side file authorization guarantee. The iMask
regex parser accepts configured patterns dynamically; it has no independent
security-boundary property at this call site. ReDoS and dynamic-pattern claims
are outside this review's proof count.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-source-review-evidence.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --reviews properties/calibration/2026-10-15-p2-json-editor-source-review/reviews.json \
  --checkout /tmp/regexproof-pinned-sources/json-editor-b31ddabecf4ed3209d37a2f5b29956120cd8f9ce \
  --repo-id json-editor/json-editor \
  --pin b31ddabecf4ed3209d37a2f5b29956120cd8f9ce \
  --output properties/calibration/2026-10-15-p2-json-editor-source-review/evidence.json
```
