# `(?x)` verbose-flag semantics spike (Corpus Wave 3 / P1)

Pinned evidence: Nosey Parker builtin rules — **136 / 189** patterns carry `(?x)`.

## Status quo (code-verified at Wave-3 plan fold)

| Path | Behavior |
|---|---|
| `normalize_inline_flags` (`regexproof/compiler/normalize.py`) | Lifts leading `(?[imsx]+)` into the flags string; **never strips** whitespace / `#` comments |
| `compile_re2` | No unknown-flag reject for `x` → silent literal-whitespace lowering |
| `compile_ecma` | Rejects `x` fail-closed |
| go-re2 `syntax.Parse` | Rejects `(?x` — without strip, ~136 Nosey Parker records become parse-errors |

## Pre-pass CONTRACT (handoff to P3)

Single lexical strip at **extraction time**, before any flag lifting:

1. **Class-aware** — `#` and whitespace inside `[…]` stay literal.
2. **Mid-pattern** `(?x)` enabling **and** `(?-x)` disabling.
3. **Combined groups** (`(?xi)`, `(?sx)`, …) consumed entirely (flags lifted; body stripped when `x` is on).
4. After strip, re2/ecma compilers **reject residual `x`** fail-closed (no silent path).
5. Unit-test: every stripped pattern must pass go-re2 `syntax.Parse`.
6. Mirror-fidelity probes use the **STRIPPED** form (see fixture `noseyparker.json` + gate `wrong_xflag_caught`).

## Wrong-mirror catch (P1 gate)

- Correct mirror: `z3.Re("ab")` for stripped `(?x) a b`.
- Deliberately-wrong mirror: `z3.Re("a b")` (whitespace as literal).
- On probe `"a b"`: wrong says yes, real go-re2 on stripped `ab` says no → `wrong_xflag_caught=true`.

## Handoff

P3 implements the pre-pass + mutation guard (deliberately-unstripped mirror must fail).
No production extractor code in this phase.
