# DOMPurify corpus

Pinned cure53/DOMPurify TypeScript sources for Corpus Wave 3 Phase 4
(issue #115). XSS sanitizer boundary (`IS_ALLOWED_URI`, `IS_SCRIPT_OR_DATA`).

## Materialize the corpus

```bash
PIN=7392211bda80f9c1038db32fc090119685bfe425
git clone https://github.com/cure53/DOMPurify.git /tmp/DOMPurify
git -C /tmp/DOMPurify fetch --depth 1 origin "$PIN"
git -C /tmp/DOMPurify checkout "$PIN"
ln -sfn /tmp/DOMPurify batch/corpora/dompurify/rules
test "$(git -C /tmp/DOMPurify rev-parse HEAD)" = "$PIN"
```

Manifest pin: `7392211bda80f9c1038db32fc090119685bfe425`.
Path: `batch/corpora/dompurify/rules` with explicit `files:` listing
`src/purify.ts`, `src/regexp.ts`, plus `attrs.ts` / `tags.ts` / `utils.ts`
(verified: those three contribute **0** regex literals at this pin — the plan's
`~146` count was a false-positive grep over comments/URLs; precise scan finds
**16** sites: 14 in `regexp.ts` + 2 in `purify.ts`).

## Sample vs full

Wave corpus (full pin required for measure). `sample/` holds a minimal
`regexp.ts` slice with `IS_ALLOWED_URI` / `IS_SCRIPT_OR_DATA` for local smoke.
If `rules/` is missing/empty, measure **hard-error**.

## Extractor + dialect

- Extractor: `dompurify` (`regexproof/extractors/dompurify.py`)
- Dialect: `ecma` (node helper for ground truth)
- `seal(/…/)` wrappers enriched with export name in `context_snippet`

## Measure command

```bash
python scripts/measure-corpus-fraction.py --corpus dompurify --assert-determinism
```
