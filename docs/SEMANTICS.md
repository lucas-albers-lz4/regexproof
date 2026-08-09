# Semantics — dialects, `call_kind`, fold closures, shorthands

Z3's regex theory is the **regular-language theory**: languages of strings
over an alphabet. Backtracking engines (Python `re`, JS RegExp, PCRE, sed)
accept a *superset* of syntax but with **operational semantics** (priority
ordering, greediness, backtracking) that matter when you ask questions about
what a match *captures* — not just what matches.

Taxonomy source of truth: `regexproof/kinds.py` (`CALL_KINDS`, `DIALECTS`,
`PROPERTY_KINDS`).

## `call_kind` taxonomy

| `call_kind` | Real API (examples) | Z3 mirror wrapping |
|---|---|---|
| `fullmatch` | Python `re.fullmatch`, JS `^…$` with full-string intent | Bare body (whole-string `InRe`) |
| `match` | Python `re.match` (implicit `^`) | Prefix: `Concat(body, Star(any))` — **not** bare `InRe` |
| `search` | Python `re.search`, JS `RegExp.test` / unanchored RE2 | `Concat(Star(any), body, Star(any))` |
| `exec` | JS `RegExp.exec` (membership + captures) | Same wrap as `search` for membership; captures are string-ops (deferred) |
| `substitution` | `re.sub` / replace | Search-style wrap for “what matches”; replacement is string-ops |

**verified-finding: VF-009** — `InRe` is always whole-string membership.
`re.match(r"AND", "AND foo")` matches while `InRe("AND foo", Re("AND"))` is
unsat. Use `prefix_match()` / compiler `call_kind` wrappers
(`regexproof/compiler/base.py`, `lower.py`).

Anchors `^` / `$` in the pattern are stripped into metadata and combined with
`call_kind` — do **not** equate “has `^`” with full-string membership when the
call is `search` or `match`.

## What carries over 1:1 (membership questions)

| Feature | Z3 encoding |
|---|---|
| literals | `Re(s)` — **literal**, not a pattern parse (`VF-004`) |
| char classes `[a-z]` | `Range` / `Union` |
| alternation / concat | `Union` / `Concat` |
| `*` `+` `{n,m}` | `Star`, `Plus`, `Loop` |
| `?` (optional) | `Union(r, Re(""))` — **not** `z3.Opt` (that is the optimizer class) |
| case-insensitive | **fold closures** per dialect (below) — Z3 has no flag |

## Per-dialect case-fold closures

Implementation: `regexproof/compiler/fold.py`. Closures, not pair lists.

| Dialect | Fold function | Distinguishing probes |
|---|---|---|
| `py_re` (default Unicode) | `python_fold_closure` | **İ** (U+0130) and **ı** (U+0131) fold into `[i]` |
| `py_re` + ASCII/`re.A` | `python_fold_closure(..., ascii_only=True)` | ASCII letter pairs only |
| `re2` | `re2_fold_closure` | İ/ı do **not** fold into `[i]`; residual `x` → `x-flag-unstripped`, `s` → `s-flag` (fail-closed; strip `(?x)` at extract via `strip_verbose_x`) |
| `ecma` (non-`u`) | `js_nonsu_fold_closure` | **ß** does not expand to `SS` (no multi-char folds) |
| `pcre` (encodable subset) | ASCII-style fold when `i` set | Same discipline as ASCII py-re for the subset |
| `perl` (encodable subset) | ASCII-style fold when `i` set | POSIX `[[:alpha:]]` etc. rewritten; `\K` stripped; lookarounds / `(?{` / `\g{` / `\p{` / `\Q` rejected — see `PERL_REJECT_MARKERS` |
| `yara` | `re2_fold_closure` when `nocase`→`i` | Ascii-domain compile delegates to `compile_re2`; wide domain is NUL-interleaved literals (non-literals reject) |

**verified-finding: VF-008** — Python vs RE2 divergence on İ/ı is load-bearing
for any cross-dialect “same pattern” claim.

**verified-finding: VF-005** — a containment proof against `Re("bot")` under
`re.I` is a silently narrower language; use `ci()` / dialect fold tables.

## `\d` / `\s` / `\w` and line terminators

Compilers expand shorthands to dialect alphabets (see `py_re.py`, `ecma.py`,
`re2.py`, `pcre.py`). Approximate tables for the encodable subset:

| Class | `py_re` (ASCII-bound domain) | `ecma` | `re2` / `pcre` subset |
|---|---|---|---|
| `\d` | `[0-9]` when domain is ASCII; Unicode digits otherwise (state domain!) | `[0-9]` in common subset | `[0-9]` |
| `\w` | ASCII word or Unicode word per flags / domain | JS word class per flags | RE2/PCRE word class in subset |
| `\s` | whitespace incl. dialect-specific | JS whitespace | dialect whitespace |
| `.` terminators | `\n` (`_PY_LINE_TERMINATORS`) | `\n`, `\r`, U+2028, U+2029 (`JS_TERMINATORS`) | `\n` (`RE2_TERMINATORS` / `PCRE_TERMINATORS`) |
| `[^…]` negated class | ASCII/BMP **range complement** (not `Star(Complement)` — TRAPS #1) | same | same |
| Scoped `(?i:…)` | via `sre` flag bits when modeled | **reject** `inline-flag` (JS has no scoped flags) | encode via `Folded` + dialect `case_fold` |

**verified-finding: VF-006** — Unicode-aware Python classes vs ASCII Z3
mirrors can yield false safety (`\b`) or false findings (`\d`). Declare
`input_domain` and use `--require-domain` when proving ASCII-only boundaries.

## What does NOT carry over

| Feature | Problem | Workaround |
|---|---|---|
| Lookahead / lookbehind | not in regular-language theory | string ops or Z3-Noodler `re.from_ecma2020` (JS) |
| Backreferences | not regular | ReDoS / behavioral tooling (`docs/REDOS.md`) |
| Capture position / greediness | membership ignores match position | `IndexOf` / `SubString` (P3 pattern) |
| `re.sub` / `replace_all` | unsupported in stock z3 | string ops / unroll |
| Search-wrapped **shape-5** gap queries | Z3 times out / `unknown` | compile R1/R2 as `fullmatch` + tight length (`VF-007`) |

## Ground truth beats assumptions

Wherever match *position* or *capture* matters, run the real engine on
witnesses. Mirror the `call_kind` the code actually uses. See
`docs/REPORTING.md` and `--require-ground-truth`.

## ModSecurity negation

Negated `@rx` / selectors are **never** silent-positive. Per-dialect policy
table: [`docs/NEGATION.md`](NEGATION.md) / `regexproof.batch.negation_policy`.

## Practical rules

1. **Ask the question the code asks** (`call_kind` first).
2. **Restrict the alphabet to the input domain** and declare it.
3. **Lookahead?** Prefer string-ops rewrite; Noodler when verifying JS as written.
4. **Capture correctness** is string-ops, never pure membership.
