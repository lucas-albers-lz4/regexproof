# Snyk Language Server exact-pin P2 source review

This is a complete raw-regex review for one frozen cohort member. It does not
cover the other 19 repositories or close P2.

## Scope and result

- Repository: `snyk/snyk-ls`
- Pin: `1cf40fcabd330a1fe4e8eb9493b15a99a392e17f`
- Extracted Go regex sites reviewed: **37**
- Evidence-backed skips: **36**
- Unresolved: **1**
- Adopted contracts / product questions: **0**

Most sites parse compatibility-matrix metadata, test fixtures, issue/diff
presentation text, URI navigation fragments, local Git branch labels, or
Maven project metadata for user-requested code actions. These uses do not
enforce an authorization boundary or sanitize an output for a separate trust
domain, and no independent language guarantee was established for them.

The unresolved site is `domain/ide/converter/converter.go:42`. In Markdown
hover mode the helper replaces `<br>` tags with line breaks and sends the
message over the LSP hover channel. The source comment calls this
sanitization, but the regex only handles `<br>` and leaves other markup
untouched. The pinned source does not establish the supported clients' HTML
rendering behavior or an independent sanitization requirement. The item stays
unresolved and is not counted as a product question.

The frozen extractor labels regex compile sites as `call_kind=search`; source
review checked their real consumers. Several sites are used through
`ReplaceAllString`, while others use `Match` or `FindStringSubmatch`. The raw
inventory remains unchanged.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-source-review-evidence.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --reviews properties/calibration/2026-10-15-p2-snyk-ls-source-review/reviews.json \
  --checkout /tmp/regexproof-pinned-sources/snyk-ls-1cf40fcabd330a1fe4e8eb9493b15a99a392e17f \
  --repo-id snyk/snyk-ls \
  --pin 1cf40fcabd330a1fe4e8eb9493b15a99a392e17f \
  --output properties/calibration/2026-10-15-p2-snyk-ls-source-review/evidence.json
```
