# \p gate table (R2) — every syntax position, gated + measured

Run 2026-08-11, pinned Noodler v1.6.1, node v22.23.1. Policy (U4/U8):
**REJECT all real `\p{}`/`\P{}` tokens at registration** — measured:
`from_ecma2020` does NOT error on `\p` — it silently treats it as an
identity escape (literal 'p', exactly like non-/u node). The property
intent (`\p{L}` = any letter) is silently dropped at solver level:
no error, no abstention, wrong semantics. That is the U4 class — the
registration gate must reject, or the intent is silently lost. The
mirror has no encoding without full Unicode tables. No silent folding;
the gate is conservative (node accepts, the harness rejects with a
rewrite suggestion: expand to explicit classes).

Corpus (node): `a A 1 _ é π <empty> ab` — bitstring per form.
Probe (from_ecma2020): 4 discriminating strings `a p{L} p é` — bits per
string (1=sat 0=unsat ?=unknown T=timeout C=crash). The literal
interpretation of `\p{L}` matches `p{L}` (bit 2 = 1) and misses `a`/`é`;
real property semantics would match `a` and `é`. NOTE: from_ecma2020 has
NO flag representation — the flag-i/flag-u rows probe the BASE form at
solver level (intentional; the flags exist only in the node column).

| position | form | flags | node | from_ecma2020 probe | gate |
|---|---|---|---|---|---|
| plain | `\p{L}` | — | 00000000 | 0100 | REJECT |
| plain | `\p{Lu}` | — | 00000000 | 0000 | REJECT |
| plain | `\p{ASCII}` | — | 00000000 | 0000 | REJECT |
| plain | `\p{Any}` | — | 00000000 | 0000 | REJECT |
| plain | `\P{L}` | — | 00000000 | 0000 | REJECT |
| in-class | `[\p{L}]` | — | 00000000 | 0110 | REJECT |
| in-class | `[\p{L}\d]` | — | 00100000 | 0110 | REJECT |
| quantified | `\p{L}+` | — | 00000000 | 0100 | REJECT |
| quantified | `\p{L}{2}` | — | 00000000 | 0000 | REJECT |
| flag-i | `\p{L}` | i | 00000000 | 0100 | REJECT |
| flag-i | `\p{Lu}` | i | 00000000 | 0000 | REJECT |
| script | `\p{Script=Greek}` | — | 00000000 | 0000 | REJECT |
| script | `\p{Greek}` | — | 00000000 | 0000 | REJECT |
| escaped | `\\p{L}` | — | 00000000 | 0000 | ACCEPT |
| escaped | `[\\p{L}]` | — | 00000000 | 0110 | ACCEPT |
| malformed | `\p{` | — | 00000000 | 0100 | REJECT |
| malformed | `\p{}` | — | 00000000 | 0000 | REJECT |
| malformed | `\p{L` | — | 00000000 | 0100 | REJECT |
| malformed | `\p{L}}` | — | 00000000 | 0000 | REJECT |
| malformed | `\p{L}{` | — | 00000000 | 0000 | REJECT |
| malformed | `\p{Xyz}` | — | 00000000 | 0000 | REJECT |
| flag-u | `\p{L}` | u | 11001101 | 0100 | REJECT |

## Reading
- **from_ecma2020 probe column**: RAW pattern text in the SMT-LIB
  literal (backslash is a literal char — no escaping; the measured
  escape-input class from the pilot). The 4-bit pattern discriminates:
  `p{L}` bit = 1 proves the pattern matches the literal string (identity
  escape), `a`/`é` bits = 0 prove no property semantics. `unsat/rc=0` on
  every probe = accepted and silently re-interpreted — never a parse
  error, never an abstention — the trap.
- **node without /u**: identical identity-escape semantics (bits match
  the literal interpretation, e.g. `[\p{L}\d]` = literal-p OR digit →
  only '1' matches). Node and the solver agree — but both are WRONG
  relative to the property intent.
- **node with /u** (`\p{L}` row): REAL property semantics — 'a', 'A',
  'é', 'π', 'ab' all match (11001101). The /u row shows what the user
  meant; the harness gate rejects it rather than silently folding to
  the literal form (U4).
- **escaped** (`\\p{L}`): ACCEPT — an even backslash chain makes it
  literal text (no `\p{` token); node treats it as literal (bits all 0
  — no string contains '\\pL'... consistent).
- **malformed** (`\p{`, `\p{}`, `\p{L`, `\p{L}}`, `\p{L}{`, `\p{Xyz}`):
  REJECT — node without /u silently literalizes (identity escapes, no
  throw); with /u node throws (strict). The harness rejects uniformly —
  no partial semantics, no reliance on the /u/non-/u divergence.

## Implementation hook (Phase 2, #218)
The registration gate calls the same Node-based ECMA parser as D7: a
`\p{`/`\P{` token (odd backslash chain) anywhere in the pattern →
registration error with the rewrite suggestion. Table-driven from this
matrix.
