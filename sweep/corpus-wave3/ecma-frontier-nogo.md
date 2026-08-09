# Wave-3 P4 ecma frontier — admission NO-GO (isemail + email_addresses)

**Umbrella:** [#111](https://github.com/lucas-albers-lz4/regexproof/issues/111)
**Phase:** [#115](https://github.com/lucas-albers-lz4/regexproof/issues/115)
**Date:** 2026-08-09

## Summary

Fraction gate: **GO** for all three P4 corpora (≥ 0.30).
Admission gate: **GO** for `dompurify`; **NO-GO** for `isemail` and
`email_addresses` after correcting the plan's site counts.

## Count correction

| Corpus | Plan claim | Measured (precise scan) | False-positive source |
|---|---|---|---|
| dompurify | ~146 | **16** (14 `regexp.ts` + 2 `purify.ts`; attrs/tags/utils = 0) | `/…/` grep matched comments/URLs in TS |
| isemail | 121 | **5** | ABNF alternatives (`a / b`) in block comments |
| email_addresses | 71 | **4** | Same ABNF `/` noise; minified twin skipped |

## Admission conditions (isemail / email_addresses)

- `new-surface`: false — ecma already covered by validatorjs
- `security-boundary`: false — RFC validators, **not** in `SECURITY_TOOL_CORPORA`
- `large-under-saturated`: false — 5 / 4 sites ≪ 1000

Per `gate_decision.schema.json`, 0/3 met ⇒ `decision=no-go`.
`fraction_decision=go` is recorded separately (sequential fraction gate).

## Fraction results (still GO)

| Corpus | Encodable | Sample | Fraction | Fraction decision |
|---|---|---|---|---|
| dompurify | 9 | 16 | 0.5625 | go |
| isemail | 4 | 5 | 0.8000 | go |
| email_addresses | 2 | 4 | 0.5000 | go |

## Ask for umbrella (#111)

Re-approve whether `isemail` / `email_addresses` remain wave-3 pack members
as **measure-only** (extractor + fraction + goldens + mirror-fidelity surfaces)
despite admission NO-GO, or drop them from the wave roster now that the probe
scale claim is refuted. DOMPurify stays admitted (security-boundary).
