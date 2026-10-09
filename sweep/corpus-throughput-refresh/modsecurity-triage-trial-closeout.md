# ModSecurity triage-trial close-out

**Candidate:** `Rev3rseSecurity/wordpress-modsecurity-ruleset`

**Pin:** `6bdd250e3b121f79c9b06ea48231cdada8e9dac9`

**Trial decision:** continue triage on the narrow rule 22200029 contract
candidate. The evidence supports review of the exact CI request, but does not
support product counting or a broader claim that all WordPress user
enumeration is blocked.

## Ingest and Smith results

- Admission probe: 11 files walked, 23 ModSecurity PCRE sites, zero extractor
  errors. Counts: `03-BRUTEFORCE.conf` 4, `04-EVENTS.conf` 8,
  `05-HARDENING.conf` 9, and test fixture `test/modsecurity.conf` 2.
- Smith product allowlist: the five root configuration files, excluding
  `test/` and `99-TEST.conf`. The resulting inventory has 21 sites; all 21
  compile (`21/21`, fraction `1.0`), with deterministic output and zero parse
  errors. See [encodable fraction](../../properties/generated/wordpress_modsecurity_ruleset_encodable_fraction.json)
  and [inventory](../../properties/generated/wordpress_modsecurity_ruleset-inventory.ndjson).
- The isolated batch completed with 21 extracted/encodable sites, 19 generic
  scanner flags, and no ReDoS findings. These are not product findings.
  The disclosure-gated PR dry run records all 19 as `private_first`, with
  `publish=false` and no public upstream issue; see
  [dry-run artifact](../../properties/generated/wordpress_modsecurity_ruleset-pr-dry-run.json).

The scanner's 18 `usage_mismatch` claims were refuted by source context. The
extractor represents ModSecurity `SecRule` PCRE as `call_kind=search`; the
scanner then calls anchored expressions mismatches because that generic call
kind is substring-oriented. In these rules, anchors intentionally constrain
the PCRE match. The affected IDs are:

`01a873c095c72b4268891d9381455cf8`,
`1d2e9ad593471c45ba7439907157d613`,
`3b1aa93b812f8eeae3c8ba3ac2160347`,
`5ea35327454917b117bca40d137d8976`,
`6409918c5b1f8ac917f6397d871a352b`,
`658150d8ddb998e7a78a7cc0561d0348`,
`6637dc9aacd2828fcc99b2109a2e3a8c`,
`7b38758e1a9df8f7c7371852614f7381`,
`7c3f571421ff4315f7ed6207b1466a61`,
`805a4c00e98b626adfa7b34e68bd42d8`,
`8693c8d5476c3c60b117b8cfebdbba65`,
`a869164d8e4e7a3699ed13e512d42774`,
`aba7d8e7cc5bc47cf575eb6d83bc4e4f`,
`d7a766291a424fda5cf5c71528b3976d`,
`dd981c4a54227bc2e82d921de3baa0b5`,
`e46d47bf080298e6996147d58b1981a3`,
`e6bec4836bf2d92fdd779f90a89b980e`,
and `feeb5af7c2a7131768eef3bb6c39eaf7`.

The one `intent_mismatch` claim (`5ea35327454917b117bca40d137d8976`)
asserted that the `load[]` anti-DoS URI pattern validates URLs by excluding
newline. Its source is rule 22200039, a request-threshold rule for repeated
load parameters; the source does not claim a URL-validation property or
declare an input domain. This remains unproven and is not reported as a
product issue.

## Rule 22200029 replay

The repository's CI image, `owasp/modsecurity:v3-ubuntu-nginx`, cannot be
resolved. The replay below is alternate-engine corroboration, not exact
historical-CI ground truth.

Replay environment:

- Image: `ghcr.io/coreruleset/modsecurity-crs@sha256:133267aa811e1a57a23b52ef04b3c30e802bcbe5454588f6d6af1f69f4b2b667`
- Platform: `linux/amd64`; image config digest `sha256:c771ea3ed89693745988aca1987f4383d9fa5567388d59f2e80388c314515fe3`
- Runtime: ModSecurity 3.0.17, ModSecurity-Nginx 1.0.4, Nginx 1.30.5
- Loaded the exact-pin root rules in source order, overlaid the pinned
  repository's `test/crs-setup.conf`, and reproduced the Dockerfile's
  `wprs_allow_user_enumeration=0` setting. The container used a dummy Nginx
  backend on an isolated Docker network; only loopback port 18081 was
  published. Built-in CRS rules were replaced by the candidate rule files.
- Matched the CI method and host: `HEAD`, `Host: localhost`.
- Dummy backend image: `nginx:stable-alpine`, resolved digest
  `sha256:0985e772fb9f729e6fa0980da05fca5d9c468e870eed43071545afa9d2e27d94`.
- SHA-256 of the included candidate files: `01-SETUP.conf`
  `f901bee5e346e9930a4ada815fe17e95542b72756e393436904a6841abc10b24`,
  `02-INITIALIZATION.conf`
  `9d89be4a0fa22f920b13584d3b95a1c5009635d31998fb0695da3b06857eee55`,
  `03-BRUTEFORCE.conf`
  `04fcf022437c1e1e8bedaa34a797c12e0a142ecfa79cb1c391afd536ae50e2fb`,
  `04-EVENTS.conf`
  `c154fca0dae95837092335624d1baffca9bc53b45b568eea42728855c7a4143c`,
  and `05-HARDENING.conf`
  `04848139c47bd63419ec03172443710218055fe1faccfc82578db8d582654e73`.
  The test `crs-setup.conf` hash is
  `a17fa5df1ecc6295c37a64f2481437b222deba6a221199782a090c8a806d1247`.

| Request target | HTTP status | Evidence |
|---|---:|---|
| `/` | 200 | Baseline reached dummy backend |
| `/?author=1` | 403 | Audit event names rule 22200029, phase 1 |
| `/?author=12345` | 403 | Audit event names rule 22200029, phase 1 |

Additional exploratory requests showed that the unanchored rule also blocks
`/?notauthor=1`, `/?foo=author=1`, and `/foo?author=1`; uppercase and
percent-encoded variants also trigger it. `/?author=abc` returned 200. These
observations disprove the broader interpretation that the regex recognizes
only a syntactically valid `author` query parameter. They do not establish a
false-positive vulnerability without an independent application contract.

The schema-valid draft
[`wordpress_modsecurity_ruleset_contract_candidate.json`](../../properties/generated/wordpress_modsecurity_ruleset_contract_candidate.json)
captures only the exact CI-shaped request domain. Its provenance remains
`agent_derived`; it is not a human-adopted contract, product result, or
conversion-ledger row. The corpus is not in `WAVE_CORPORA`.

## Historical runtime recovery check

**Checked:** 2026-10-09; **active time:** 4 minutes (09:16–09:20 UTC).
This records only the recovery check; it does not backfill time for the
earlier corpus trial.

- Confirmed the candidate checkout is exactly
  `6bdd250e3b121f79c9b06ea48231cdada8e9dac9` (2021-02-25). Its
  `test/Dockerfile` uses `FROM owasp/modsecurity:v3-ubuntu-nginx` without a
  digest and runs `apt-get update` plus unpinned package installs. The Travis
  config passes `COMMIT` as a build argument, but the checked Dockerfile has no
  `ARG COMMIT` declaration.
- `docker manifest inspect owasp/modsecurity:v3-ubuntu-nginx` returned `no
  such manifest`; the Docker Hub tag API returned `count: 0`. No ModSecurity
  image for that tag was present in the local Docker cache.
- The former image builder,
  [`coreruleset/modsecurity-docker`](https://github.com/coreruleset/modsecurity-docker),
  is archived; its README says it stopped building the standalone
  `owasp/modsecurity` image and points users to the
  [current official CRS container project](https://github.com/coreruleset/modsecurity-crs-docker).
  The archived builder history nearest this candidate pin (commit
  `bca1ded4e75390b1bb51aa64ff052f107c896daa`, 2021-02-02) uses
  `nginx:1.17.9`, ModSecurity `v3.0.4`, and connector `v1.0.1`; its tag script
  maps that Dockerfile to `3.0.4-nginx`. It does not establish which image
  digest, base, or engine versions the candidate's `v3-ubuntu-nginx` tag used.
- Rebuilding from the candidate Dockerfile would not recover that runtime:
  its base tag and apt packages are not pinned, and no historical image digest
  or build record was recovered. The Travis API checks returned 404; Travis
  documents that logs older than 365 days are unavailable by default
  ([job-log availability](https://www.travis-ci.com/blog/22-9-30-joblogs/)).

**Outcome:** historical runtime not recoverable from the checked public
artifacts. Stop product-engine replay at this blocker. The pinned CRS image
replay above remains alternate-engine evidence only. Resume historical-engine
work only if an immutable image export/digest or equivalent pinned build
record becomes available.

## Remaining gate

Before this candidate can become a product contract, a human must adopt or
reject the exact guarantee. Do not infer Smith GO from a 1.0 encodable
fraction or from alternate-engine replay. The historical-engine recovery
trial is closed; the human decision packet remains `agent_derived` until the
guarantee is adopted or rejected. The earlier corpus trial did not instrument
active minutes, so it is not an operator-throughput timing sample.
