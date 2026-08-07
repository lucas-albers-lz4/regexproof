# Traps — solver gotchas that cost real debugging time

Every entry below was hit (or measured) during the usrmanage/fwlive work on
`z3-solver==5.0.0` (2026-08). Read this before writing constraints.

## 1. `Complement()` is LANGUAGE complement, not char-class negation

`Complement(Re('"'))` = all strings that aren't exactly `"` — so `a"`, `ba`,
`\"` are all "in the complement", and `Star(Complement(Re('"')))` is **NOT**
`[^\"]*`. Controlled tests:

| Query | Result |
|---|---|
| `s == "b"` ∧ `InRe(s, Complement(Re("a")))` | sat |
| `s == "a"` ∧ `InRe(s, Complement(Re("a")))` | unsat |
| `s == 'a"'` ∧ `InRe(s, Complement(Re('"')))` | **sat** ← the trap |
| `s == ""` ∧ `InRe(s, Complement(Re("a")))` | sat |

To exclude a char class, use `Union(Range(...))` of the allowed chars, or
string ops (`IndexOf`, `Contains`).

**✅ Valid use — single-char membership:** `InRe(c, Complement(Re('"')))`
with `Length(c) == 1` DOES correctly exclude `"` (the complement of the
one-char language restricted to one-char strings is the char-class
complement). Verified in the fwlive pilot (word-boundary check:
`Complement([A-Za-z0-9_])` with `Length==1` excludes alnum/underscore and
admits `.`). The trap is exclusively the multi-char / `Star(Complement(...))`
context — restrict to single-char membership and Complement is safe.

## 2. The `seq` backend solves regex; `z3str3` returns `unknown` instantly

Z3 has two string backends. `z3str3` (`smt.string_solver=z3str3`) solves pure
string equations but gives `unknown` (1ms) on `InRe` constraints. Do NOT set
it for regex work. The default `seq` backend solved P2 in 927ms, P3 in 2ms.

| Backend | Regex membership (`InRe`) | String eq |
|---|---|---|
| `seq` (DEFAULT) | ✅ solves | ✅ |
| `z3str3` | ❌ `unknown` instantly | ✅ |

## 3. NUL (0x00) is a real edge — state input-domain assumptions

An escaper with `if (o > 0 && o < 32)` prints NUL raw through its `else`
branch. "No raw C0 controls" is then FALSE as stated. Fix: state the
input-domain assumption explicitly — *POSIX shell strings cannot contain NUL*
(C strings are NUL-terminated) — and encode it as a solver constraint +
comment, or the property is false as stated.

## 4. "Deny-list unreachable" is ambiguous

`root` IS in the username-regex language; only the accept-language
(regex ∧ ¬deny-list) excludes it. Encode as `accept(s) ∧ s == "root"` → unsat,
NOT plain regex membership. Mirror deny-lists verbatim — forget the deny-list
and the proof silently passes for a name that must be rejected.

## 5. `re.replace_re` / `str.replace_all` are NOT supported

The Z3 guide: "currently not supported". Model replacements as string ops or
unroll (for example, `IndexOf`/`SubString`/`Concat` composition).

## 6. Regex unfolding is incomplete with string constraints

The default solver lazily unfolds memberships via symbolic derivatives — it
works for many membership/non-membership queries but "is not a complete
procedure when membership constraints are combined with constraints over
strings." Don't expect a decision procedure for the full combination. This is
the mechanism behind monolithic-image timeouts — decompose (see
DECOMPOSITION.md).

## 7. `SubString` with symbolic indices is expensive

Prefer concrete indices. `SubString(s, 0, IndexOf(...))` is fine; symbolic
offsets into loops are not.

## 8. `FullRe` is NOT exported in z3py 5.0.0

`NameError`. Use `Star(Re("..."))` over an explicit char set instead.

## 9. Length bounds are load-bearing

Same property shape (`InRe` + `Contains` exclusion), different caps:

- Username validator (`^[a-z_][a-z0-9_-]{0,31}$`, 9-name deny-list): all 10
  injection-char exclusions <1s each.
- Actor whitelist (`^[A-Za-z0-9._@-]{1,64}$`): 9/9 instant at `Length ≤ 16`;
  **`Length ≤ 64` timed out at 60s** on the same query.

Timing caveat: these numbers were measured on one machine (z3-solver 5.0.0,
2026-08, single-threaded). They are **order-of-magnitude guides**, not
portable benchmarks — a different CPU/container can shift the exact cutoffs
(16 vs 64) by a factor of 2-3. Use the shapes, not the raw milliseconds.

Mitigation for real bounds > ~16: prove the alphabet-level property
(single-char `InRe(c, class) ∧ c == bad` → unsat, instant, length-independent),
and/or length-slice with incremental push/pop (16, 32, 48, 64).

## 10. `unknown` is NOT sat

Treating solver timeout as SAT produced "FAIL ... SAT (counterexample!)" with
no model. Always check `r == sat` before reading a model. Report `unknown`
honestly — it is a hard failure in CI, never a pass.

## 11. Lookaheads/lookbehinds are not expressible in stock Z3

The regex theory is the *regular-language* theory — no `(?=...)` constructors.
Patterns with lookahead must be rewritten to equivalent non-lookahead forms
(string-ops prefix checks work for most) or routed through Z3-Noodler's
`re.from_ecma2020` (JS only). See BACKENDS.md and the fwlive classifier note
in properties/.

## 12. Presence-gates must use whole-word grep — substring matches lie

Gating a property on code presence ("is the fallback still there?", the
temporal-coupling gate) with a naive `grep -c sed file` matched the word
"pas**sed**" inside a comment and nearly produced a false "fallback absent"
verdict (count 1 instead of 0). Use whole-word or anchored patterns and
derive the verdict from the count explicitly:

```bash
grep -wc "sed" file           # whole-word count — 0 = truly absent
grep -cE "(^|[^A-Za-z])sed([^A-Za-z]|$)" file   # or anchored alternative
```

Print the verdict ("0 hits — path absent, finder flipped" vs "N hits — finder
stays active"), never just the raw count. This bit the regexproof pilot
(usrmanage P3 gate); ground-truthing the gate output caught it before the
false claim shipped.

## 13. `Re("...")` is a LITERAL, not a pattern parse

`z3.Re("[a-z]")` builds the regex matching the 5-character string `[a-z]`
literally — it does NOT compile a regex pattern. Verified:

```
InRe("a", Re("[a-z]"))  → unsat      (the 1-char string "a" is not "[a-z]")
InRe("[", Re("[a-z]"))  → sat        (the literal "[a-z]" contains "[")
```

This silently breaks any "mirror = Re(user_pattern_string)" design: the
mirror accepts a different language than the real regex and differential
fuzz reports mismatches on every input — or worse, a containment property
passes vacuously. The original `differential-fuzz.py --mirror-regex`
design shipped exactly this bug. It was caught in testing and the script
now requires a z3py EXPRESSION (Union/Range/Concat/Star), never a pattern
string. Build mirrors with the API, same as z3-verify.py properties.

## 14. Char-range boundaries are load-bearing — off-by-one silently includes neighbors

Building `[^A-Za-z0-9_]` as `Union(Range("[", "`"), ...)` wrongly includes
`_` (0x5F), which IS alnum: `Range("[","`")` spans 0x5B–0x60. The correct
complement is `Range("[","^")` (0x5B–0x5E) + `Re("`")` (0x60). A Z3
witness (`b = "_"`) exposed the error in the fwlive sweep (property
"trailing boundary rejects alnum" initially PASSED a wrong encoding).
Always write complements as explicit disjoint ranges and probe each
boundary char with a membership query before trusting the class.

## 15. `Opt` is the optimizer class, not regex optional

There is NO regex-optional `Opt`/`ReOpt` in z3py 5.0.0 — `z3.Opt` is the
optimization-solver class. Regex `?` is `Union(r, Re(""))` (verified:
accepts both the token and the empty string). This bit the
differential-fuzz mirror namespace (AttributeError at import). Documented
here so a mirror namespace never advertises `Opt` as regex-optional.
