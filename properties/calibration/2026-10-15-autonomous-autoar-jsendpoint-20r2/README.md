# AutoAR Go JavaScript endpoint capture calibration

This is a one-question, source-bound P6 calibration for AutoAR at frozen 20-r2
pin `01cd447ad3b1acfed7e0680596c2c74458a4cf06`. It is retrospective runner
evidence, not a prospective P7 yield sample: a standalone mirror check and
real source replay occurred before the product roster was frozen. P4's ranked
15-site shortlist and pre-outcome allocation are also still open.

## Contract and reviewed path

The adopted contract is in [`contract.json`](contract.json). It binds the
source file SHA-256
`e9c03be11f7aab2a4310ea4944de5620e500f2400b13e22a3e1ea5b16745c549` and the
URL-assignment expression at line 181. The pinned `Run` method reads
JavaScript URLs from the domain scan list, downloads response bodies, and
passes those bodies to `extractEndpoints`. The extractor returns group 1 from
the assignment expression, applies its noise filter, and `Run` writes returned
values to both the endpoint text file and structured dashboard results. The
review trace is summarized in [`source-evidence.json`](source-evidence.json).

The guarantee is limited to the selected capture class: it excludes ASCII
double quote, apostrophe, backtick, space, tab, LF, form feed, and CR. The
capture token is bounded to 4–200 Go RE2 characters. This does not establish
endpoint validity, scope safety, or extraction completeness.

## Proof and product gate

`AA-autoar-jsendpoint-assignment-capture-delimiter` is a Shape-1 alphabet
property over a one-character ASCII projection of the source capture class.
Z3 5.0.0 returned UNSAT. The registered mutation guard removed the double
quote exclusion, returned SAT with `"`, and the weakened exact-source Go
extractor stored that quote in the endpoint. The product wrapper requires Go
1.25.7, matching AutoAR's `go.mod` declaration.

The local product gate compared the source extractor over 163 bodies: five
capture-length boundaries, 128 seeded safe assignments, 24 forbidden-delimiter
insertions, three Unicode samples, and three malformed assignments. It saw
zero forbidden delimiters in outputs and matched every expected safe capture.
The real-source mutation emitted `service/v1/users";`. The runner recorded the
same gate and mutation pass in
[`p6-wave-r1/`](p6-wave-r1/).

The end-to-end observation window was 513 seconds (19:01:53–19:10:26 UTC)
for one reviewed site, one adopted contract, one decided proof, and one local
gate. The P6 runner phases themselves summed to 0.760 seconds. Token use,
cost, and human active minutes were unavailable; this single calibration is
not a stable throughput estimate.

The first standalone formal invocation was rejected by the harness registration
gate because the one-character projection pattern lacked `^...$`. The property
annotation was anchored, preserving the inner source class, and then the
registered proof and mutation guard passed. This was a harness preflight issue,
not a product counterexample.

## Limits and disposition

The source-bound property establishes delimiter exclusion for the declared
ASCII domain. The product replay samples additional Unicode values, but those
samples do not widen the formal theorem. No current product bug or reachable
violation was found; there is no external report, maintainer confirmation, or
fix. The gate is locally runnable and wired into CI, but AutoAR has not adopted
it as a consumer gate.

The initial product checks preceded roster freeze, so do not count this
question as prospective allocation yield. Future P7 work should freeze a
ranked shortlist and identities before any proof or product outcome is
inspected.
