# ECMA-route pilot (R9) — fwlive classifier patterns: three-route divergence study

Run 2026-08-11 on the pinned Noodler v1.6.1 (sha256 22b19f12…464), stock z3 5.0.0,
node v22.23.1. Patterns fetched verbatim from `lucas-albers-lz4/fwlive` master
`core/fwlive-log.js` (CLASSIFY_SPEC). Declared input domain: ASCII (D14 scoping;
\s gap NBSP/U+2028 noted).

**Pattern count: SIX** (the code's authoritative count — NON_FIREWALL_PREFIX,
FIREWALL_HINT, ACTION_RE, DENY_ACTION, TCP_FLAG_TAIL, NETFILTER_KV_GLUE). The
design's U9/R9 "5" referenced an earlier count that omitted DENY_ACTION's separate
name; corrected in #213 rev 7.1.

## Routes

| Route | Implementation | Form |
|---|---|---|
| R1 real | node, pattern AS WRITTEN with its flags | ground truth |
| R2 ECMA | Noodler `re.from_ecma2020`, ASCII case-expanded (U4 explicit expansion; no flags in the function), search-wrapped (`.*….*`, full-match semantics) | the as-written diagnostic route |
| R3 mirror | stock z3 standard encoding, same case-expanded words, boundary-exact | the proof-capable route |

Corpus: exhaustive strings over `{a A 0 _ space tab . :}` up to length 3 + targeted
strings (the words, boundary compositions, KV forms, flag sequences) = 937 strings
per pattern, 5,622 decided comparisons total.

## Results — ZERO divergences

| Pattern | corpus | R1 vs R2 | R1 vs R3 | R2 vs R3 | ECMA abstains |
|---|---|---|---|---|---|
| NON_FIREWALL_PREFIX | 937 | 0 | 0 | 0 | 41 (4.4%) |
| FIREWALL_HINT | 937 | 0 | 0 | 0 | 30 (3.2%) |
| ACTION_RE | 937 | 0 | 0 | 0 | 42 (4.5%) |
| DENY_ACTION | 937 | 0 | 0 | 0 | 24 (2.6%) |
| TCP_FLAG_TAIL | 937 | 0 | 0 | 0 | 26 (2.8%) |
| NETFILTER_KV_GLUE | 937 | 0 | 0 | 0 | 0 (0.0%) |
| **Total** | 5,622 | **0** | **0** | **0** | 163 (2.9%) |

- **R1 vs R3 (mirror fidelity): 0** — every mirror encoding is EXACT against the real
  JS implementation on the corpus, including NETFILTER_KV_GLUE (the C1 equivalence,
  now on a 937-string corpus, not just 13).
- **R1 vs R2 (translation fidelity): 0** — where from_ecma2020 decides, it agrees
  with real JS exactly (case-expanded forms included).
- **R2 vs R3 (route equivalence): 0** — the two routes agree on every decided string.

## Abstention class (measured, honest)

from_ecma2020 returns `unknown` (rc 0, spot-verified on the abstain sample:
`\tfw4`, `\tDENY`, `ACK`, `logd\t` all `unknown/rc=0` — never empty output or
crashes) on **exact-boundary anchored forms**: the `(^|…)`-alternation positions
(word + boundary compositions like `\tfw4`, `logd\t`, `\tDENY`) and `$`-anchored
tails at the exact string boundary (bare flag words for TCP_FLAG_TAIL: `ACK`,
`SYN`, …). Same family as the measured key=`=`-lookahead exact-boundary quirk. All
abstentions are honest `unknown`s; the tier logic caps them, and the mirror route
decides every abstaining string — the proof-capable path is complete for all six
patterns.

## Divergence rate → D10 / U9 evidence

**0 / 5,622 decided comparisons within the declared ASCII domain.** All six fwlive
classifier patterns have proof-capable mirror routes (flip-criterion DROP-branch
evidence). The ECMA route is exact where it decides (KEEP-branch support: the
as-written diagnostic is faithful on its decided set). Final U9 decision per the
pre-committed criterion goes into the P1 report (u9-decision.md).

## Runner-mechanics finding (feeds D6 / Phase 2 spec)

**Noodler does NOT decode Python-style short escapes in SMT-LIB input** — `\t` in a
quoted string is read as LITERAL backslash-t (measured twice: this pilot's first run
mis-encoded tabs and produced phantom "divergences"; the C1-probe repr bug was the
same class). The SMT-LIB input path must write **raw bytes** with quote-doubling
only (`""` → `"`), never Python/JSON escapes. Same class as the Z3-dialect
`\xHH`/`\u{}` escapes, which DO decode. Phase 2's runner spec (issue #218, D6)
adopts: raw-bytes encoding + an AC fixture asserting a control-char string
round-trips.
