# Nosey Parker dialect decision (Wave 3 / P3 / #114)

## Decision

**Route Nosey Parker builtin rules through the `re2` dialect** as a declared
ASCII approximation of the rust `regex` crate (the engine Nosey Parker
actually uses). Do **not** silently claim rust≡RE2.

`rust_regex` remains inventory-only in this repo (Wave-2 P2 did not land a
membership compiler). Until that lands, re2 + differential-fuzz vs go-re2 is
the fallback route (issue #114 round-1 fold A).

## Why re2

| Factor | Note |
|---|---|
| Syntax surface | Builtin rules are largely RE2-shaped after `(?x)` strip |
| Helper | `helpers/go-re2` gives parse + replay for fidelity gates |
| Fold | `re2_fold_closure` matches go-re2 `i` / FoldCase probes used elsewhere |
| Gap | rust `regex` Unicode / `(?s)` / crate-specific edges ≠ go-re2 |

Manifest field: `declared_semantics: ascii_approx_rust_regex` (same pattern as
semgrep_rules).

## `(?x)` / `(?s)`

- `(?x)`: stripped at extraction (`strip_verbose_x`); residual `x` →
  `x-flag-unstripped` in `compile_re2`.
- `(?s)` / lifted `s`: **reject fail-closed** (`s-flag`). Records that need
  dotall are unencodable until a rust_regex or helper-`s` path exists — never
  silent ignore.

## Differential-fuzz expectation

Mirror-fidelity / corpus fuzz should probe the **stripped** pattern against
go-re2 (see `sweep/corpus-wave3/fixtures/noseyparker.json` +
`wrong_xflag_caught`). Disagreements vs rust `regex` are out of declared
domain until a rust engine adapter lands.

## shhgit

shhgit uses Go `regexp` with FoldCase intent → `dialect=re2`, `flags=i`,
`call_kind=fullmatch`. No rust approximation claim.
