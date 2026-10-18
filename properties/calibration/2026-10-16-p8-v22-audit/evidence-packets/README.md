# Private evidence packets for P8

These packets collect the exact-pin local evidence for the 12 SAT product candidates in ten groups. They are prepared for internal review only. No repository maintainer or third party was contacted, and no report was transmitted. Each packet keeps its evidence gap and impact boundary explicit.

## `doberman-windows-secret-store-coverage`

**Questions:** `PY-doberman-secret-store-windows-miss`

**Classification:** `reproduced_security_control_gap_candidate`; security impact: `plausible_not_confirmed`.

**Demonstrated:** The exact-pin gate reports PASS for Windows-shaped .npmrc/credentials targets and AUTH for slash-separated controls on Linux. Native Windows execution and a real secret read were not exercised.

**Next evidence:** Verify native Windows path normalization and an end-to-end intercepted fs_read decision using a disposable path.

**Evidence files and source references:**
- [README.md](../../../../properties/calibration/2026-10-15-autonomous-doberman-win-secret-path-20r2/README.md) (SHA-256 `4115c3da7ac975324f01af342de60b524db3b3510237eba8caa9c7caa640a6b1`)
- [gate-report.json](../../../../properties/calibration/2026-10-15-autonomous-doberman-win-secret-path-20r2/gate-report.json) (SHA-256 `3d5c239ca776df5190c31e4431964ea079dc2a11f14e0ceb9b5bf221336db091`)
- https://github.com/fu351/Doberman-Core/blob/53ae43c5298a2426c6696147fdd75e2a4aef10e2/src/doberman/engine/rules/secrets.py#L223-L235 (source pin `53ae43c5298a2426c6696147fdd75e2a4aef10e2`)

**External status:** Private-first posture; no report sent, maintainer confirmation, or fix.

## `autoar-cross-origin-loopback-js-fetch`

**Questions:** `AA-autoar-jsendpoint-loopback-script-src-fetch`

**Classification:** `reproduced_cross_origin_loopback_fetch_candidate`; security impact: `plausible_not_confirmed`.

**Demonstrated:** The pinned collector replay fetched a harmless JavaScript body from a second disposable 127.0.0.1 listener after receiving an absolute script URL from scanned-host HTML. It establishes a loopback request, not sensitive access or production impact.

**Next evidence:** Review documented target/scope expectations and impact in a representative operator deployment.

**Evidence files and source references:**
- [README.md](../../../../properties/calibration/2026-10-15-autonomous-autoar-jsendpoint-scope-escape-20r2/README.md) (SHA-256 `855dc9cd89d570d0c39b9cf4d6e9167f464340f509bcce4bffdda46f80ec3027`)
- [gate-report.json](../../../../properties/calibration/2026-10-15-autonomous-autoar-jsendpoint-scope-escape-20r2/gate-report.json) (SHA-256 `9e0c849f54c713b9237f27c22428fc9200b5a050ef121ff432ca79317f0ebce9`)
- https://github.com/h0tak88r/AutoAR/blob/01cd447ad3b1acfed7e0680596c2c74458a4cf06/internal/scanner/jsendpoints/jsendpoints.go#L21-L26 (source pin `01cd447ad3b1acfed7e0680596c2c74458a4cf06`)

**External status:** Private-first posture; no report sent, maintainer confirmation, or fix.

## `malcontent-third-party-metadata-markdown-rendering`

**Questions:** `MC-malcontent-author-metadata-extra-markdown-link`, `MC-malcontent-description-metadata-extra-markdown-link`

**Classification:** `reproduced_markdown_structure_injection_candidate`; security impact: `not_confirmed`.

**Demonstrated:** Two distinct third-party YARA metadata fields reach raw Markdown link/table output. Exact-pin replays show structure changes; no browser or downstream Markdown consumer was tested, so XSS or user impact is unproven.

**Next evidence:** Identify a supported Markdown consumer and test whether it activates attacker-selected links or altered table structure.

**Evidence files and source references:**
- [README.md](../../../../properties/calibration/2026-10-15-autonomous-malcontent-author-markdown-20r2/README.md) (SHA-256 `9e175f454413d9f6e2b48ed666e13ce50908498c85d24e6832a7552a83344ffa`)
- [product-replay.json](../../../../properties/calibration/2026-10-15-autonomous-malcontent-author-markdown-20r2/product-replay.json) (SHA-256 `ea3ec08ff1555afa3730a11b40cc17da416fff29a9442f2165b9e9c4284112de`)
- [README.md](../../../../properties/calibration/2026-10-15-autonomous-malcontent-description-markdown-20r2/README.md) (SHA-256 `bafcb1e397c5ee53023be5b7a2bc2eaa652ad6b2765aae89ac60cb4cfa591022`)
- [product-replay.json](../../../../properties/calibration/2026-10-15-autonomous-malcontent-description-markdown-20r2/product-replay.json) (SHA-256 `63a9d5fda295e0581da90deb5acffde9aad1142bc8b336b1489b76661a4ba0d0`)

**External status:** Private-first posture; no report sent, maintainer confirmation, or fix.

## `llm-honeypot-rfc1918-redaction-coverage`

**Questions:** `LH-llm-honeypot-private-ip-rfc1918-redaction`

**Classification:** `reproduced_redaction_coverage_candidate`; security impact: `plausible_not_confirmed`.

**Demonstrated:** Exact pinned shell-function replay shows 10/8 and 172.16/12 IPv4 tokens pass unchanged through the generated-artifact redaction helper. No actual generated artifact was inspected or published.

**Next evidence:** Inspect only an authorized disposable/generated fixture and establish whether affected output is published or consumed.

**Evidence files and source references:**
- [README.md](../../../../properties/calibration/2026-10-15-p2-llm-honeypot-source-review/README.md) (SHA-256 `c17a33382953ae529d06e5db4f6fb4129e8d09f0727e56cee3eb785f4af7562e`)
- [product-replay.json](../../../../properties/calibration/2026-10-15-p2-llm-honeypot-source-review/product-replay.json) (SHA-256 `d6b582e313ceee9cc2320a603396980ceba1a9e702a1fa14c5a12158865e8b9b`)
- https://github.com/Leviticus-Triage/llm-honeypot-intelligence/blob/65624396e263074bb8cb2e049f9a9ec6215ea5c1/scripts/sync-to-github.sh (source pin `65624396e263074bb8cb2e049f9a9ec6215ea5c1`)

**External status:** No report sent, maintainer confirmation, or fix.

## `llm-honeypot-tor-newnym-response-sequencing`

**Questions:** `LH-llm-honeypot-tor-newnym-response-sequencing`

**Classification:** local response-handling defect confirmed; security impact remains `not_confirmed`.

**Demonstrated:** The exact pinned helper and local fixture confirm that an earlier AUTHENTICATE 250 OK can make the helper report success after a later SIGNAL NEWNYM 551 failure. The repository documents periodic NEWNYM as required and says scans stop if the rotator fails; the official Tor protocol defines 5yz replies as unsuccessful and 551 as an internal error preventing fulfillment. No live Tor service or deployed scan was exercised, so security/privacy impact remains unconfirmed.

**Next evidence:** Establish whether this failure response occurs in a supported deployment and whether a scan continues on the old exit. Do not infer that impact from the local fixture alone.

**Evidence files and source references:**
- [README.md](../../../../properties/calibration/2026-10-15-p2-llm-honeypot-source-review/README.md) (SHA-256 `c17a33382953ae529d06e5db4f6fb4129e8d09f0727e56cee3eb785f4af7562e`)
- [product-replay.json](../../../../properties/calibration/2026-10-15-p2-llm-honeypot-source-review/product-replay.json) (SHA-256 `d6b582e313ceee9cc2320a603396980ceba1a9e702a1fa14c5a12158865e8b9b`)
- [P8 disposition follow-up](../tor-newnym-disposition/README.md) (local bug confirmed; impact still unconfirmed)
- https://github.com/Leviticus-Triage/llm-honeypot-intelligence/blob/65624396e263074bb8cb2e049f9a9ec6215ea5c1/spiderfoot-toolbox/tor-gateway/rotate-tor.sh (source pin `65624396e263074bb8cb2e049f9a9ec6215ea5c1`)

**External status:** No report sent, maintainer confirmation, or fix.

## `panther-precommit-secret-path-policy-mismatch`

**Questions:** `PA-panther-staged-secrets-file-excluded-from-review-prompt`

**Classification:** `reproduced_policy_mismatch_candidate`; security impact: `not_confirmed`.

**Demonstrated:** A synthetic staged secrets.py is selected and its marker reaches the pre-commit prompt helper. The expectation comes from the separate slash-command review policy; that command is not wired to the pre-commit helper, so shared intent remains an inference. No real secret, Claude invocation, or external transmission was observed.

**Next evidence:** Confirm whether the repository intends the slash-command sensitive-path rule to govern the pre-commit helper, then maintain the local regression gate against that requirement.

**Evidence files and source references:**
- [README.md](../../../../properties/calibration/2026-10-15-p2-panther-source-review/README.md) (SHA-256 `bc69a679ca8c6be56c98df03ec48a3daeef2035a4f5c1f56a7b972d1da300362`)
- [proof-report.ndjson](../../../../properties/calibration/2026-10-15-p2-panther-source-review/proof-report.ndjson) (SHA-256 `3b3a93b428307b29fb534343e9b8bceacf36e49f49e55133da5355e01a0986e3`)
- [product-replay.json](../../../../properties/calibration/2026-10-15-p2-panther-source-review/product-replay.json) (SHA-256 `fe614f324011737b0918088b2c188ea12327bb4f2dc9cefacac65949898a6e7d`)
- https://github.com/panther-labs/panther-analysis/blob/0cd0f5bd33469c9f03b578fe0104a4ebf23d9f4a/.scripts/claude_review.py#L20-L55 (source pin `0cd0f5bd33469c9f03b578fe0104a4ebf23d9f4a`)
- https://github.com/panther-labs/panther-analysis/blob/0cd0f5bd33469c9f03b578fe0104a4ebf23d9f4a/.claude/commands/pr-review.md#L5-L8 (source pin `0cd0f5bd33469c9f03b578fe0104a4ebf23d9f4a`)

**External status:** No report sent, maintainer confirmation, or fix.

## `inhale-url-output-path-confinement`

**Questions:** `IH-inhale-file-url-output-root-confinement`, `IH-inhale-directory-url-output-root-confinement`

**Classification:** `reproduced_local_output_path_escape_candidate`; security impact: `not_confirmed`.

**Demonstrated:** The README documents -o OUTDIR as the location for scraped files. Exact-pin local replays show two traversal-shaped operator-supplied URLs cause the single-file and remote-directory helpers to write synthetic response bytes outside that configured directory while remaining inside disposable temporary fixtures. This establishes a reproducible local path-confinement gap for the concrete CLI inputs, but the URLs are operator-provided config and neither attacker control in a deployed caller nor downstream security impact is established.

**Next evidence:** Establish whether a supported deployment lets an untrusted party select the -u, -l, or -r URL, and whether a file written outside -o affects another product boundary. No real filesystem outside an isolated temporary fixture or deployment was tested.

**Evidence files and source references:**
- [README.md](../../../../properties/calibration/2026-10-15-p2-inhale-source-review/README.md) (SHA-256 `857ca04570b6e0a83f51c685d3d19a3ffaaf70b791f3531100841dd18449a6ca`)
- [proof-report.ndjson](../../../../properties/calibration/2026-10-15-p2-inhale-source-review/proof-report.ndjson) (SHA-256 `785eb562e9101d64fb176fd744da9bd8d1984f8ab9951f4da81d5acfcb9e18d9`)
- [product-replay-p6.json](../../../../properties/calibration/2026-10-15-p2-inhale-source-review/p6-wave-r1/product-replay-p6.json) (SHA-256 `14dc9402b2c388eadea5bb8fb82a1850ac050648bf79aed339e4366d52daff15`)
- https://github.com/netspooky/inhale/blob/889bbe2ab4a40a85c7ccd8399b2fd3cfddf539e8/README.md#L118-L130 (source pin `889bbe2ab4a40a85c7ccd8399b2fd3cfddf539e8`)
- https://github.com/netspooky/inhale/blob/889bbe2ab4a40a85c7ccd8399b2fd3cfddf539e8/iModules/rDownload.py#L106-L123 (source pin `889bbe2ab4a40a85c7ccd8399b2fd3cfddf539e8`)
- https://github.com/netspooky/inhale/blob/889bbe2ab4a40a85c7ccd8399b2fd3cfddf539e8/iModules/rDownload.py#L128-L135 (source pin `889bbe2ab4a40a85c7ccd8399b2fd3cfddf539e8`)

**External status:** No report sent, maintainer confirmation, or third-party fix.

## `tracecat-mcp-stdio-env-key-grammar-mismatch`

**Questions:** `TC-mcp-env-key-accepts-terminal-lf`

**Classification:** `reproduced_policy_mismatch_candidate`; security impact: `not_confirmed`.

**Demonstrated:** At the frozen pin, the validator comment and public error promise [A-Za-z_][A-Za-z0-9_]*, but CPython re.match with the source pattern’s terminal $ accepts a final-line-feed key. The full configuration validator accepts it and the local POSIX child receives it. POSIX permits implementation-specific environment names, and no harmful MCP-server behavior, security boundary crossing, or deployed impact was demonstrated; this remains a reproduced policy-mismatch candidate.

**Next evidence:** Determine whether the declared Tracecat key grammar is a required product invariant in supported integrations and whether a permitted downstream MCP server assigns harmful meaning to a newline-containing environment key. The local child-process replay establishes delivery only, not such an effect.

**Evidence files and source references:**
- [README.md](../../../../properties/calibration/2026-10-15-autonomous-tracecat-mcp-env-key/README.md) (SHA-256 `898d4aa1a1b03d740b03ed8010d5c31c6100a6bff9b885aaa48f9ee1b06d288d`)
- [product-gate.json](../../../../properties/calibration/2026-10-15-autonomous-tracecat-mcp-env-key/p6-wave/product-gate.json) (SHA-256 `1cf8ec4d628a6c223eb8d281a5daf1297db0ca587046929e85882faf918e1c1e`)
- https://github.com/TracecatHQ/tracecat/blob/c84d52528a489821f355fc63976fbc7783ae0ad5/tracecat/integrations/mcp_validation.py#L174-L179 (source pin `c84d52528a489821f355fc63976fbc7783ae0ad5`)

**External status:** No report sent, maintainer confirmation, or third-party fix.

## `aidevops-predispatch-cited-file-path-escape`

**Questions:** `AE-aidevops-predispatch-cited-file-traversal-read`

**Classification:** `reproduced_local_path_escape_candidate`; security impact: `not_confirmed`.

**Demonstrated:** The exact pinned helper parses cited_file from issue-body text, joins it below the fresh clone, and runs wc -l without path containment. With ../oracle.txt it measured a 37-line fixture outside the mock clone. The captured replay then closed the issue as premise-falsified; it did not read file contents, prove public disclosure, or access user data.

**Next evidence:** Trace the supported dispatch trigger, issue-author control, automation-token permissions, and log visibility; determine whether the line-count side channel or issue-closing behavior crosses a documented product/security boundary.

**Evidence files and source references:**
- [README.md](../../../../properties/calibration/2026-10-16-autonomous-aidevops-predispatch-github-text-20r2/README.md) (SHA-256 `317e55de9abf8f57c252c25f6bd8075d2bb107c31f6ffb3227697e9d143c48a3`)
- [replay-cited-file.json](../../../../properties/calibration/2026-10-16-autonomous-aidevops-predispatch-github-text-20r2/replay-cited-file.json) (SHA-256 `6a4939f043642ae047f1ac3f9eb0436c8ffeb92b99578b98054a270edbfb725b`)
- [contract-cited-file-path.json](../../../../properties/calibration/2026-10-16-autonomous-aidevops-predispatch-github-text-20r2/contract-cited-file-path.json) (SHA-256 `cfd06ff6245fc5f6649150c48a4e04c22d773721774854a2492220cbff7d9e07`)
- [review-evidence.json](../../../../properties/calibration/2026-10-16-autonomous-aidevops-predispatch-github-text-20r2/review-evidence.json) (SHA-256 `f32b433d50bfcba88e6add7f8370bcc91de2c9e09e3e0ae02b8527435236a371`)

**External status:** No report sent, maintainer confirmation, or fix.

## `aidevops-predispatch-threshold-leading-zero`

**Questions:** `AE-aidevops-predispatch-threshold-leading-zero-fail-open`

**Classification:** `reproduced_fail_open_workflow_validation_candidate`; security impact: `not_confirmed`.

**Demonstrated:** The exact pinned helper accepts threshold=08 from a marker, then Bash rejects the arithmetic operand as invalid octal. For a five-line fixture the failed [[ -lt ]] check takes the premise-holds return-0 path and logs that dispatch proceeds; the decimal control threshold=8 returns 10. This confirms a local validation fail-open, not its downstream security impact.

**Next evidence:** Trace whether an untrusted issue author can supply or alter this marker in the supported workflow and what dispatch performs after validation; compare that consequence with the documented large-file gate contract.

**Evidence files and source references:**
- [README.md](../../../../properties/calibration/2026-10-16-autonomous-aidevops-predispatch-github-text-residual-20r2/README.md) (SHA-256 `cc259d0bbaa0aac93d98c998c41d8cada7cef0bc5c2b8862f226813c43199205`)
- [replay-threshold.json](../../../../properties/calibration/2026-10-16-autonomous-aidevops-predispatch-github-text-residual-20r2/replay-threshold.json) (SHA-256 `e98af94b9a028411b7e029fc6fffcfacff7e138d10f12c519818785f05658eb2`)
- [contract-threshold-decimal.json](../../../../properties/calibration/2026-10-16-autonomous-aidevops-predispatch-github-text-residual-20r2/contract-threshold-decimal.json) (SHA-256 `d1461b3030bee5eb05933993bf6229bd86739f57c41edfaa867d800ea52d16f2`)
- [review-evidence.json](../../../../properties/calibration/2026-10-16-autonomous-aidevops-predispatch-github-text-residual-20r2/review-evidence.json) (SHA-256 `0ca1fc438fb317b3fdc8dc4b649c227e097353c81312200aaca6068b0d9f4209`)

**External status:** No report sent, maintainer confirmation, or fix.

## Refuted historical claims

`doberman-terminal-newline-denylist` covers `PY-doberman-windows-root-token`, `PY-doberman-disk-wipe-token`. The Windows root helper strips surrounding whitespace before the regex. Both matching paths are deny-list checks whose true result contributes to BLOCK. The SATs establish regex membership, not a bypass.

No bug packet or external report is prepared for this refuted-bypass group. The pinned caller evidence is retained in the [machine-readable manifest](manifest.json).
