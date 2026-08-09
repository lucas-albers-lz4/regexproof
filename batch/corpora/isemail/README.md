# isemail corpus

Pinned hapijs/isemail `lib/` sources for Corpus Wave 3 Phase 4 (issue #115).
RFC5321/5322 email validator (character-class parser + a few JS regex helpers).

## Materialize the corpus

```bash
PIN=8789d509d69f098350783fb2d8d2bf05f036b448
git clone https://github.com/hapijs/isemail.git /tmp/isemail
git -C /tmp/isemail fetch --depth 1 origin "$PIN"
git -C /tmp/isemail checkout "$PIN"
ln -sfn /tmp/isemail/lib batch/corpora/isemail/rules
test "$(git -C /tmp/isemail rev-parse HEAD)" = "$PIN"
```

Manifest pin: `8789d509d69f098350783fb2d8d2bf05f036b448`.
Path: `batch/corpora/isemail/rules` → `lib/` with explicit `files:` list.

Plan claim of **121** sites was a false-positive grep (ABNF `/` alternatives in
comments). Precise scan finds **5** real JS regex literals.

## Sample vs full

Wave corpus. `sample/parser_snippet.js` holds the IPv4/IPv6 helpers for smoke.
Missing `rules/` → measure hard-error.

## Extractor + dialect

- Extractor: `isemail` (`regexproof/extractors/isemail.py`)
- Dialect: `ecma`
- Not a security tool — **not** in `SECURITY_TOOL_CORPORA`

## Measure command

```bash
python scripts/measure-corpus-fraction.py --corpus isemail --assert-determinism
```
