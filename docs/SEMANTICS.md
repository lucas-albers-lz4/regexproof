# Semantics — mapping Python `re` and JS ECMA-262 regexes to Z3

Z3's regex theory is the **regular-language theory**: languages of strings
over an alphabet. Backtracking engines (Python `re`, JS RegExp, PCRE, sed)
accept a *superset* of syntax but with **operational semantics** (priority
ordering, greediness, backtracking) that matter when you ask questions about
what a match *captures* — not just what matches.

## What carries over 1:1 to Z3 (membership questions)

| Feature | Z3 encoding |
|---|---|
| literals, `.` (as literal) | `Re(".")`, `Re(s)` |
| char classes `[a-z]` | `Range('a','z')` / `Union(Range(...))` |
| alternation `a|b` | `Union` |
| concatenation | `Concat` |
| `*` `+` `?` `{n,m}` | `Star`, `Plus`, `Opt`, `Loop(Re("a"), n, m)` |
| anchors `^` `$` | model as full-string membership (the default in Z3) |
| case-insensitive flag | expand the alphabet explicitly (union of both cases) — Z3 has no flag |

**Key semantic point:** Z3 `InRe(s, r)` is *full-string* membership. An
unanchored Python `re.search(pattern, s)` / JS `regex.test(s)` corresponds to
`Contains(s, w)` for some word `w ∈ L(pattern)` — or equivalently
`InRe(s, Concat(Star(any), pattern, Star(any)))`. Decide which question you're
asking and encode it deliberately.

## What does NOT carry over

| Feature | Problem | Workaround |
|---|---|---|
| Lookahead `(?=...)`, lookbehind `(?<=...)` | no constructors in the regular-language theory | rewrite with string ops (`PrefixOf`/`SuffixOf`/`Contains` on the remainder), or Z3-Noodler `re.from_ecma2020` for JS |
| Backreferences `\1` | not regular | out of scope for SMT — use ReDoS/behavioral tooling (REDOS.md) |
| Greedy vs lazy capture semantics | Z3 membership ignores match position | model captures with string ops (`IndexOf`/`SubString`) — the P3 pattern |
| `re.sub` / `replace_all` | unsupported in stock z3 | model as string ops or unroll |
| Python-specific: `\A`, `\Z`, inline flags, `re.VERBOSE`, conditional groups | partial | strip/expand to the regular subset before encoding |
| Unicode classes `\w` `\d` (Python default) | huge alphabets blow up | restrict to the actual input domain (ASCII where the boundary is ASCII); state the domain |
| JS `u`/`v` flags, property escapes `\p{...}` | same | same — expand to the domain |

## Ground truth beats assumptions

The Z3 model is a mirror of *your* reading of the regex. Wherever a match
*position* or *capture* matters, run the real engine on witness strings:

- sed capture `s/.*"password"[[:space:]]*:[[:space:]]*"\([^\"]*\)".*/\1/p` —
  `IndexOf`/`SubString` mirror matches real sed byte-for-byte for the
  first-quote case (verified with `od` on both GNU and BusyBox sed), but sed's
  greedy `.*` prefix means **last-key-wins on duplicate keys** — a documented
  single-field abstraction.
- JS `RegExp.test` vs `RegExp.exec` — one answers membership, the other
  position+captures. Mirror the one the code actually calls.
- Python `re.fullmatch` vs `re.match` vs `re.search` — three different
  questions. `fullmatch` ↔ Z3 `InRe`; the others need the `Star(any)` wrapper.

## Practical rules

1. **Ask the question the code asks.** If the code checks `if re.match(...)`
   then a Z3 proof about full-match semantics is the wrong property.
2. **Restrict the alphabet to the input domain** (and say so in the declared
   domain). ASCII-boundary regexes don't need Unicode alphabets.
3. **Lookahead?** Prefer the string-ops rewrite; use `re.from_ecma2020` when
   verifying the JS source pattern as written matters (codegen'd specs).
4. **Capture correctness** is a string-ops question, never a regex-membership
   question.
