# hippo corpus

Pinned NHS-digital-website/hippo first-party regex surfaces for Smith
batch [#155](https://github.com/lucas-albers-lz4/regexproof/issues/155).

Admission probe reported **2899** sites; ~2782 were vendored bundles
(highlight.js, swagger-ui, rapidoc, ckeditor/quail, jquery-ui, highcharts).
Smith measures an explicit allowlist only (DOMPurify lesson).

## Materialize the corpus

```bash
PIN=4879bd48c50c712236f99413cb1f68091cea599c
git clone https://github.com/NHS-digital-website/hippo.git /tmp/hippo
git -C /tmp/hippo fetch --depth 1 origin "$PIN"
git -C /tmp/hippo checkout "$PIN"
ln -sfn /tmp/hippo batch/corpora/hippo/rules
test "$(git -C /tmp/hippo rev-parse HEAD)" = "$PIN"
```

Manifest pin: `4879bd48c50c712236f99413cb1f68091cea599c`.

## Allowlist (ecma / `js_dir`)

| File | Role |
|---|---|
| `…/eforms/eforms.js` | NHS easy-forms wiring |
| `…/eforms/formcheck/formcheck.js` | FormCheck validators (MODIFIED_HIPPO) |
| `…/eforms/jquery-hippo-validate.js` | NHS jquery-validate extensions |
| `…/table-sort/table-sort-date.js` | date sort parsers |
| `…/statistics/statistics-countup.js` | count-up formatting |
| `…/utils/vanilla-js-utils.js` | small util |

**Excluded:** swagger/rapidoc/highlight/ckeditor/jquery-ui/highcharts;
formcheck `documentation/` + `lang/`; jquery-validate-1.1.2.js (upstream);
eforms `localization/`; acceptance-tests; webpack/gulp.

Precise `extract_js` counts at this pin (allowlist): **183** sites.
Ecma measure: **62/183 = 0.3388** → fraction go.

## Java slice (not in CORPUS_MANIFESTS)

Nine `Pattern.compile` sites under NHS `src/main` Java. Artifacts use
stem `hippo_java_*` so they do not clobber the ecma fraction/batch.
Approximation: `java→pcre`. Native Java dialect remains #150.

```bash
PIN=4879bd48c50c712236f99413cb1f68091cea599c
python scripts/java-html-sanitizer-triage.py \
  --root batch/corpora/hippo/rules \
  --corpus hippo --artifact-stem hippo_java \
  --pin "$PIN" --url https://github.com/NHS-digital-website/hippo \
  --files site/components/src/main/java/uk/nhs/digital/common/components/apispecification/handlebars/HeadingsHyperlinksFromMarkdownHelper.java \
  --files site/components/src/main/java/uk/nhs/digital/website/utils/VideoPlayer.java \
  --files cms/src/main/java/uk/nhs/digital/apispecs/model/SpecificationSyncData.java \
  --files site/components/src/main/java/uk/nhs/digital/common/components/ComponentUtils.java \
  --files site/components/src/main/java/uk/nhs/digital/crisp/SvgSimpleJacksonRestTemplateResourceResolver.java \
  --files site/components/src/main/java/uk/nhs/digital/svg/colour/SvgColourMagic.java
```

At this pin: **9** sites, **5** encodable (fraction 0.5556), differential pass.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus hippo --assert-determinism
python -m regexproof.batch --corpus hippo
```
