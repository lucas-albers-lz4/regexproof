# AutoAR loopback script-source candidate

This is a one-question exact-pin P6 calibration for AutoAR at frozen 20-r2
pin `01cd447ad3b1acfed7e0680596c2c74458a4cf06`. It was selected as a
source-follow-up after the assignment-capture calibration, not from a ranked
15-site shortlist. Keep it out of P7 yield and allocation-quality claims.

## Contract and source route

The adopted contract binds `scriptSrcRe` at line 22 of
`internal/scanner/jsendpoints/jsendpoints.go`; parser, caller, and README
digests plus the reviewed flow are in [`source-evidence.json`](source-evidence.json).
The pinned `subdomainmonitor.diffJSEndpoints` obtains HTTP(S) URLs for live
subdomains of the scanned domain and passes them to
`CollectEndpointsForHosts`. The collector fetches each host's HTML, applies
`scriptSrcRe`, resolves captured references against the page URL, checks that
the result uses HTTP(S) and that the path contains `.js`, and then calls
`downloadFile`. For an absolute script URL, `ResolveReference` keeps the
script URL's origin. There is no same-origin or IP-address-class check on this
path.

AutoAR's README restricts scanning to systems with written permission or
targets that are in scope. The repository does not document whether following
cross-origin CDN bundles is expected or whether the operator's loopback network
is outside the intended scan boundary. The contract therefore asks a narrow
security-boundary question: can untrusted HTML cause a fetch to IPv4 loopback?
The result establishes reachability in the pinned collector. It does not
establish access to sensitive responses, a production deployment scenario,
security impact, or maintainer agreement that this violates intended behavior.

## Proof and replay

`AA-autoar-jsendpoint-loopback-script-src-fetch` is a Shape-3-style
counterexample finder over one concrete ASCII script element. Z3 5.0.0 found
the body in the pinned Go RE2 search mirror (SAT). Its required ground-truth
callback then compiled the exact collector, regex declarations, URL resolver,
and downloader extracted from the clean pin with Go 1.25.7.

The replay binds two disposable HTTP servers to `127.0.0.1` on distinct
ephemeral ports. One serves the scanned-host HTML; that HTML names the second
server's `/bundle.js`. The second server received the request and returned a
harmless body from which AutoAR extracted `/api/v1/users`. A same-origin
relative-bundle control also fetched and parsed successfully. The gate made
zero external-network requests. Exact request paths and ephemeral URLs from
the product gate are captured in [`gate-report.json`](gate-report.json).

The P6 runner passed exact-pin verification, the existing family mutation
guard, the SAT witness replay, and the local gate. Its terminal wave status is
`needs_review` because a reproduced SAT candidate requires disposition; this
is the expected finding path, not a solver or gate failure. Artifacts are in
[`p6-wave-r1/`](p6-wave-r1/). The pinned candidate replay gate is also wired
into CI; it preserves local evidence and is not a consumer-adopted AutoAR
security gate.

## Measurement and limits

This calibration adds one reviewed site and one adopted question. The P6 run
found one SAT candidate, replayed it, and established a reachable loopback
request. The gate covers a cross-origin loopback fetch and a same-origin
control. Security impact confirmed: zero. Consumer-adopted gates, external
reports, maintainer confirmations, and fixes: zero. No report was sent.

The P6 runner returns nonzero while the wave is `needs_review`; inspect the
persisted state rather than treating that code as a harness failure. The
result remains pending impact and maintainer-intent triage. In particular,
AutoAR may intentionally fetch CDN-hosted scripts, but that does not explain
why arbitrary loopback URLs are permitted; the local replay alone cannot
resolve the product's intended scope policy.
