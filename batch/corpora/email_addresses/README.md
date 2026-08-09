# email-addresses corpus

Pinned jackbearheart/email-addresses `lib/` for Corpus Wave 3 Phase 4
(issue #115). RFC5322 address parser (hand-written; regexes are whitespace
normalizers).

## Materialize the corpus

```bash
PIN=8e6be27770b7be223c2de035d7e52849f938c959
git clone https://github.com/jackbearheart/email-addresses.git /tmp/email-addresses
git -C /tmp/email-addresses fetch --depth 1 origin "$PIN"
git -C /tmp/email-addresses checkout "$PIN"
ln -sfn /tmp/email-addresses/lib batch/corpora/email_addresses/rules
test "$(git -C /tmp/email-addresses rev-parse HEAD)" = "$PIN"
```

Manifest pin: `8e6be27770b7be223c2de035d7e52849f938c959`.
Path: `batch/corpora/email_addresses/rules` → `lib/` with
`files: ["email-addresses.js"]` (minified build skipped).

Plan claim of **71** sites was a false-positive grep over ABNF comments.
Precise scan finds **4** real JS regex literals.

## Sample vs full

Wave corpus. `sample/ws.js` holds whitespace-normalize regexes for smoke.
Missing `rules/` → measure hard-error.

## Extractor + dialect

- Extractor: `email_addresses` (`regexproof/extractors/email_addresses.py`)
- Dialect: `ecma`
- Not a security tool — **not** in `SECURITY_TOOL_CORPORA`

## Measure command

```bash
python scripts/measure-corpus-fraction.py --corpus email_addresses --assert-determinism
```
