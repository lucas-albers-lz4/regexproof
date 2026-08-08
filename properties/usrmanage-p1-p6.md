# usrmanage property suite (P1–P6) — worked example

Source: `lucas-albers-lz4/usrmanage` verification work (issue #6, 2026-08).
Target: OpenWrt local user-management CLI (POSIX sh + rpcd + LuCI). The
verification target was regex-shaped sanitation on security boundaries:
audit actor, usernames, JSON escaping, sed JSON fallback.

## Spike empirical timings (z3-solver 5.0.0, Python 3.13)

| Property | Formulation | Result |
|---|---|---|
| Username validator containment (10 chars × 10 props) | `InRe(s, ^[a-z_][a-z0-9_-]{0,31}$)` + len 1..32 + deny-list, assert ¬Contains | All UNSAT, <1s each |
| Actor whitelist containment, len ≤ 16 | same shape | All UNSAT, instant |
| Actor whitelist containment, len ≤ 64 | same shape | **TIMEOUT at 60s** — length bound is load-bearing |
| sed-fallback truncation | string ops: `IndexOf`/`SubString` | SAT witness `v = "\""` |
| json_escape image (one big regex) | `Star(Union(safe,esc))` + Contains | **TIMEOUT at 30s** — must decompose per-token |

Lessons: containment properties are alphabet-disjointness (no length bound
needed); length bounds matter for the membership sanity query; escape-image
verification must be per-token.

## Encoded property suite

| # | Property | Encoding | Spike result |
|---|---|---|---|
| P1 | Username validator admits no injection chars + deny-list unreachable | `InRe(s, [a-z_][a-z0-9_-]*) ∧ 1≤len≤32 ∧ s∉{root,daemon,ftp,network,nobody,nogroup,admin,ubus,sync}` → `¬Contains(s, X)` for X ∈ {space,=,\n,\t,;,|,$,`,&} | 10/10 unsat |
| P2 | C1 actor whitelist `[A-Za-z0-9._@-]{1,64}` admits no audit-line-breaking chars | same shape, `Length ≤ 16` (slice for 17-64) | 9/9 unsat |
| P3 | sed fallback truncates escaped-quote values | `∃v: Contains(v, '\\"') ∧ SubString(v,0,IndexOf(v,'"',0)) != v` | sat, witness `\"` |
| P4 | `um_json_escape` output has no raw controls / unescaped quotes | per-token decomposition + differential fuzz | timeout as one regex; per-token planned |
| P5 | Audit line keeps exactly N key=value fields | composition of P1+P2 alphabets (values contain no space/`=`) | planned — formulation corrected (below) |
| P6 | Password policy len≥8 ∧ ≠username | `Length(p) ≥ USRMANAGE_PASS_MINLEN ∧ p != u` | trivial |

## Ground truth (BusyBox vs GNU sed)

The rpcd `json_get` sed fallback (`[^\"]*` capture) on `{"password":"a\"b"}`:

- GNU sed: `a\` (truncated at escaped quote)
- BusyBox sed 1.37.0: **identical** `a\`
- Boolean `"purge_home":true` → empty under both (sed pattern requires quoted
  strings)
- Z3 witness `v = "\""` reproduces: real sed on `{"password":"\""}` yields
  `\` — matches the model byte-for-byte.

Device fidelity: OpenWrt ships BusyBox; even when behavior is identical, pin
`busybox` in CI and run the repro through `busybox sed`.

## Formulation corrections from verification-plan review

These are the formulation bugs that recur in Z3-verification plans:

1. **P5 "no `=` in values" is WRONG as stated.** Real audit lines contain
   `reason=from=readonly` — `um_audit role "$_name" ok "from=${_cur}" "$_role"`
   (lib:842) passes `from=${_cur}` as the reason arg, embedding an `=` inside
   a value. Correct invariant: "no value contains unescaped space" + "no value
   starts with `key=`" per-field. A fixed `=` count is also wrong (role/reason
   are optional).
2. **P4 needs an input-domain assumption.** `um_json_escape`'s awk guards
   `o > 0 && o < 32` and `o == 127` — NUL (0x00) falls through printed raw.
   "No raw C0 controls" is false unless you state the domain: shell strings
   cannot contain NUL, so encode the input alphabet excluding NUL.
3. **`src` is not whitelisted in the current code** — `USRMANAGE_SRC` is an
   env var (default `cli`) settable to anything via `--src`. P5's premise
   "all values post-whitelist" is false until the C1 fix lands. Gate such
   properties on the fix being present, or verify the weaker conditional.
4. **"regex ≠ case statements" was REFUTED.** `um_validate_username`'s three
   `case` statements ARE equivalent to `^[a-z_][a-z0-9_-]{0,31}$` + deny-list.
   The general mirror-equivalence concern stands — add differential fuzz.
5. **"P3 model gives `a` not `a\`" was REFUTED.** `IndexOf(v,'"',0)` on
   `a\"b` finds the quote at position 2, so `SubString(v,0,2)` = `a\` —
   byte-identical to real sed (od-verified on GNU and BusyBox). The genuine
   residual gap is sed's greedy `.*` prefix (last-key-wins on duplicate keys)
   — acceptable single-field abstraction; document it.
6. **Version pin:** `z3-solver==5.0.0` or `>=4.13,<6` — the `Re()`/regex API
   changed across versions; unpinned CI goes flaky.
