# Decomposition playbook + how to read a proof correctly

## What a Z3 proof actually claims (domain vs. search constraints)

Z3 is **not a fuzzer** — an `unsat` result means *no string in the declared
domain violates the property*, simultaneously and symbolically. Constraints
come in two kinds, and conflating them produces false confidence:

- **Domain constraints (semantic — keep them, they make the proof stronger):**
  facts about the real input space. "POSIX shell strings cannot contain NUL"
  is a domain constraint. A proof is only honest if its declared domain
  matches reality.
- **Search constraints (performance — watch them):** `Length ≤ 16` does **not**
  mean "inputs are ≤16 chars" — it means "proven for all strings ≤16,
  unproven beyond." If the real domain is ≤64, a ≤16-bound proof is *silently
  weaker*.

**Rule:** prefer alphabet-level/length-independent proofs wherever the
property allows (they cover all strings with no bound at all); use length
bounds only when the property is genuinely length-sensitive; and *document
the declared domain of every property in the harness output* so a reader
knows exactly what was proven. When in doubt, state the domain constraint
explicitly in the property's comment — an over-constrained proof that
"passes" is a liability.

## Decomposition playbook (in preference order)

Complex regexes blow up because Z3 unfolds regex membership lazily via
symbolic derivatives, and the guide states this is **not a complete procedure
when combined with string constraints**. Decompose in this order:

1. **Alphabet-level split (strongest).** Containment properties become
   character-class disjointness (`forbidden ∩ allowed = ∅`) — instant,
   length-independent, covers all data. Use for containment rows of any
   whitelist/validator proof.
2. **Per-token decomposition.** Prove each output token separately (backslash
   handling, quote handling, raw-control absence) rather than one monolithic
   image-language regex. Each is a tiny solver; the conjunction is the
   property. (The P4 escape-image pattern.)
3. **Alternation flattening.** Big `(a|b|c|d|e|f|g)` alternations are
   effectively finite sets — check per-alternative or prove equivalence to
   the enumerated set, avoiding exponential path exploration on overlapping
   alternatives. (Relevant to fwlive's `ACTION_RE`.)
4. **String ops for structure.** Extraction/capture logic (sed `[^\"]*`,
   greedy `.*` prefix) models as `IndexOf`/`SubString` — the P3 pattern solved
   in **2ms** vs. regex formulations that time out. Regexes for *membership*;
   string ops for *transformation*.
5. **Anchor and bound.** Anchored regexes (`^...$`) are dramatically easier;
   explicit `Loop`/`re.loop` bounds beat unbounded `Star` where a real bound
   exists.
6. **Lookahead/lookbehind routing.** Not expressible in stock Z3. Rewrite as
   equivalent non-lookahead forms (string-ops prefix checks work for most) or
   route through Z3-Noodler's `re.from_ecma2020` for JS patterns — the only
   way to verify the pattern *as written*.

## Reading a solver result honestly

| Result | Meaning | Action |
|---|---|---|
| `unsat` | property holds for the declared domain | report with declared domain |
| `sat` | counterexample exists | print model; **ground-truth against the real implementation** |
| `unknown` | timeout | hard failure in CI; never report as pass or as counterexample |

## Recurring formulation bugs in verification plans

When a plan for Z3 verification is reviewed, these formulation bugs recur:

1. **Property formulation bug** — "no raw C0 controls" is false when NUL
   falls through the escaper's `else` branch. Fix: state the input-domain
   assumption (shell strings cannot contain NUL) as an explicit constraint.
2. **Invariant formulation bug** — "no `=` in audit values / fixed `=` count"
   is false when `reason=from=readonly` legitimately embeds `=` in a value.
   Fix: per-field invariants ("no value contains unescaped space", "no value
   starts with `key=`"), never a global `=` count.
3. **Temporal coupling** — verifying a *proposed* whitelist before the fix
   ships. Gate the property on the fix being present in the code (grep;
   skip-with-warning if absent), or verify the weaker conditional.
4. **Unvalidated composition inputs** — for example, `src` is an
   env-influenceable
   var; encode all value domains in ONE solver context; don't compose
   separately-proven subsets.
