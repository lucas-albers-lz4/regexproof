# tarcoin — locale-inflation writeup (probe-count correction)

**Date:** 2026-08-13 · **Follow-on** from [#314](https://github.com/lucas-albers-lz4/regexproof/issues/314)
(README note: translation catalogs inflate ecma site counts).

## The incident

tarcoin's admission probe reported **1,238 regex sites** — comfortably
above the 1,000-site scale bar (condition 3), suggesting a
large-under-saturated ecma GO. The Smith materialization then revealed the
true shape:

| Metric | Value |
|---|---|
| Probe `regex_sites` | 1,238 |
| Qt locale translation catalogs (`bitcoin_*.ts`) | **1,113 sites (89.9%)** |
| Honest first-party surface | **129 sites** (40-file app allowlist) |
| Measured encodable | **118/129 = 0.9147** |
| `complete_run` | False (238.5MB > 200MB disk budget) |

The 1,113 "sites" were **translation strings, not regex code**: Qt `.ts`
plural catalogs (`bitcoin_am.ts`, `bitcoin_ar.ts`, …) contain
`<translation>%1...%2</translation>`-style format strings that the probe's
ecma literal finder counts as regex literals. They are data, not
executable patterns.

## Why the probe over-counts

The admission probe (`probe-corpus-admission.py`) walks files and counts
regex-literal candidates by dialect. For ecma it uses the precise JS
extractor, which correctly skips comments/strings **in code files** — but
`.ts` Qt translation catalogs are XML-ish data files whose *content*
happens to be quoted text with `%`-placeholders. The extractor classifies
them by extension as JS-ish surface and counts the quoted payloads.

Same inflation class, three variants seen so far (2026-08-12/13 Smith):

1. **Locale/translation catalogs** — tarcoin `bitcoin_*.ts` (88-90% of
   probe sites), gettext `.po` files.
2. **Testdata baselines** — typenix 5,126/5,207 sites were TS-compiler
   test fixtures; typescript-go 98% of 5,952 sites were ported test-suite
   baselines.
3. **Vendored third-party bundles** — exchange-api 1,305/1,309 sites were
   `swagger-ui-*.js`; rastrea2r-server 107/121 were Sphinx coverage-report
   jquery artifacts; magento 206/246 were `corpus/` malware samples.

## Detection recipe (apply BEFORE any scale-based GO)

1. **Bucket `regex_sites_per_file` by top-level dir**
   (`collections.Counter({f.split('/')[0]: c for f, c in sf.items()})`).
   One dominant non-source dir = inflation suspect.
2. **Eyeball the top files** in the dominant bucket — `.ts`/`.po`/`.min.js`
   under `locale/`, `testdata/`, `vendor/`, `docs/`, `corpus/`, `samples/`
   are the tell.
3. **Correct the basis**: exclude the inflated dirs from the Smith manifest
   allowlist; re-state the honest first-party site count in the
   `*_smith_decision.json` (`sites_by_bucket` carries both numbers — the
   tarcoin pattern: `{'ecma app allowlist (40 files, 129 sites…': 129,
   'Qt locale translation catalogs …excluded': 1088}`).
4. **Decision remains honest either way**: a scale-GO on the corrected
   number still stands when the real surface clears the bar (tarcoin: GO
   kept at 129 sites, second-highest fraction in the matrix); a GO that
   collapses to <100 real sites becomes a superseding no-go (typenix,
   exchange-api, rastrea2r, magento precedents).

## Outcome

tarcoin was **kept as GO with corrected basis** — 118/129 = 0.9147, the
second-highest encodable fraction in the matrix (behind pm_shredder
1.0000). The correction strengthened the corpus's standing: the honest
first-party surface is small but nearly perfectly encodable, which is a
better signal than the inflated 1,238-site count suggested.

## Reproduce

```bash
# probe → inspect per-file map
python3 scripts/probe-corpus-admission.py https://github.com/Tarcoin/tarcoin \
  --pin a6552d17180dbf4a43a74c875db3e9a77f9437d6 -o /tmp/tarcoin_probe_draft.json
python3 -c "import json,collections; d=json.load(open('/tmp/tarcoin_probe_draft.json'));
sf=d['probe']['regex_sites_per_file'];
print(collections.Counter({f.split('/')[0]: c for f,c in sf.items()}).most_common())"
```
