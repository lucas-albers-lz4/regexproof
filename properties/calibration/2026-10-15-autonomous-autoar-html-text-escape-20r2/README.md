# AutoAR HTML text escaping, 20-r2 pin

This one-question calibration is bound to the frozen AutoAR commit
`01cd447ad3b1acfed7e0680596c2c74458a4cf06` and its matching GO decision.
An earlier cached directory had a misleading AutoAR-prefixed name but a
different `HEAD`; it was excluded. The clean exact-pin checkout and all caller
files were re-fetched and verified before contract adoption.

## Contract and reachable boundary

The adopted contract covers `HtmlEscapePage.esc` at
`internal/api/ui/pages/html-escape.js:2`, whose source SHA-256 is
`8b3dd2cc810e7e5c0a88095ca04257a0755f0d22d2fa7d05f2e3479c1f70a900`.
The exact-pinned source evidence is in [`source-evidence.json`](source-evidence.json).
`index.html` loads this helper before `app.js`; the global `esc` wrapper calls
it. Scan detail fetches stored result rows, flattens them, renders rows through
`findings-rows.js`, and assigns the composed rows to `tbody.innerHTML`. The
shared row renderer documents its input as a raw API finding and escapes its
display value in generated text nodes.

The security claim is deliberately limited to untrusted scan-result strings
passed through `esc` and inserted into HTML text nodes. It does not claim
context safety for JavaScript, URLs, CSS, arbitrary attributes, the separate
`escAttr` helper, or dynamic raw rendering paths.

The Z3 property asks whether the per-codepoint image contains any raw `<`,
`>`, double quote, or apostrophe; it returns UNSAT in 2.6 ms. The exact pin has
five ordered global replacements, and source checks bind those literals and
their order to the model. Global composition is checked against the real
helper with an independent character-wise reference. This is a per-token
proof plus a product regression gate, not a stand-alone whole-string Z3
theorem.

## Product gate

The product gate executes the actual pinned helper in Node's ECMAScript runtime
and compares it with an independent codepoint map:

- 63,488 valid BMP scalar values, including every HTML-sensitive token;
- four supplementary-plane scalar values;
- 2,954 exhaustive one-, two-, and three-codepoint sequences over the
  special-character/control/Unicode alphabet;
- five targeted strings and 2,048 deterministic strings up to 255 codepoints.

Total: 68,500 cases, zero output mismatches, and zero raw HTML delimiters in
the output. The mutation changes only the pinned `<` replacement from `&lt;`
to literal `<`; the solver returns SAT for `<`, and replaying the edited source
in Node returns `<`. This is a sensitivity check, not a current AutoAR bug.
The local run used Node 26.11.1; CI installs Node 22 per `ci/toolchain.toml`.

Artifacts: [`contract.json`](contract.json),
[`contracts.json`](contracts.json), [`roster.json`](roster.json),
[`gate-report.json`](gate-report.json), and the successful P6
[`p6-wave-r2/`](p6-wave-r2/) state and report.

## P6 runner history and limits

The initial P6 attempt and recovery are retained under [`p6-wave/`](p6-wave/).
It ran the mutation guard and 68,500-case product gate, then failed while
serializing the decided property because the canonical conversion emitter had
no shape entry for this property. The initial runner state was closed as
interrupted/needs-review with no solver retry. I added the shape-4 emitter
mapping and froze a fresh runner state at [`p6-wave-r2/`](p6-wave-r2/). That
run completed one UNSAT question, one real-source mutation replay, and one
passing exact-pin product gate. Its checkpoint is valid and records one
eligible, attempted, decided autonomous contract.

The standalone proof was run before the roster was frozen, so this is
retrospective calibration data rather than a prospective unbiased cohort
sample. The successful runner execution used the frozen roster and exact
source checkout. Only five regex substitutions belong to `esc` (the sibling
attribute helper has three); no ranked top-15 idiom shortlist was produced.
This calibration does not close P4's allocation requirement, P6's queue and
disposition lifecycle, or P7's prospective 50-question checkpoint.

No current vulnerability, reachable violation, third-party report,
maintainer confirmation, or fix was found. The three outcome tracks remain
separate: one useful contract-backed proof/gate; zero reproduced product bugs;
zero external outcomes.
