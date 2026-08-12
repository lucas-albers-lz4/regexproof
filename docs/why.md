# Why regexproof

> **Last updated:** 2026-08-12 · **Next review:** 2026-11-12 — the point-in-time stats in "Where it stands" age fast; re-verify them before quoting.

## What regexproof is

**regexproof is a Z3-based verification toolkit.** It turns "I think this regex is safe" into "no string in the declared domain can violate this property — machine-checked." It is a playbook and an installable toolkit that coding agents can consume directly (Hermes, Claude Code, Codex). It also comes with a corpus-scale measurement pipeline. That pipeline quantifies how much of the real-world regex surface the toolkit can prove.

**The core capability is relational, not syntactic.** regexproof does not "verify a regex" in the abstract. It verifies that two symbolic descriptions of the allowed/denied input space relate in a specified way: equivalence, containment, or non-overlap. Each property in the 5-shape taxonomy is such a relation. Regex is the first domain where that description space is expressible in string theory.

## The problem it solves

Regexes sit on security boundaries everywhere. They appear in input validators, whitelists, deny-lists, sanitizers, parsers, log classifiers, and secret detectors. A regex that accepts one wrong string is a security bug. One example: a `;` that slips past a shell gate, an escaped quote that gets truncated, or a secret format that a detector misses.

The gap in the ecosystem: **existing tooling is almost entirely ReDoS-focused** (catastrophic backtracking — *complexity* analysis of the matching engine). Almost nothing proves *language membership* — containment, exclusion, capture correctness, rule equivalence. And that problem is genuinely hard because:

- Real regexes span many dialects (Python `re`, PCRE, RE2, ECMA/JS, YARA, ModSecurity `@rx`, Go `regexp`, POSIX/busybox `sed`) with different semantics.
- Z3's native regex theory is a subset. It has no lookarounds or backreferences as written, no ASCII-vs-Unicode class consistency, and no `Complement` as char-class negation.
- The worst failure mode is not being unable to prove something. It is a *mirror error* that produces a **false proof** (UNSAT for the wrong reason).

## How it solves it

1. **A method, not just code.** A 5-shape property taxonomy (alphabet disjointness, whitelist exclusion, counterexample finder, per-token image, rule_diff), 33 documented traps, and `AGENTS.md` as the decision tree for any agent dropped into the repo.
2. **Soundness over coverage in the compiler.** Dialect compilers lower real patterns into Z3's theory and **reject** what cannot be encoded soundly rather than silently mis-encode. `unknown` (timeout) is a hard failure, never a pass.
3. **Proof hygiene enforced by the harness.** Mutation guards (a harness that cannot fail proves nothing), differential fuzzing (mirror ≡ real engine), and **ground-truthing every counterexample against the real implementation** — real `sed`, `busybox sed`, `grep -qE`. An unverified witness is never reported as a finding.
4. **Measurement at corpus scale.** A batch scanner inventories regex sites in real open-source repos, compiles them through the current compiler, and reports an *encodable fraction* — turning "is the toolkit any good" into a number you can track and improve.
5. **A disciplined acquisition pipeline.** An admission gate (21-bucket reject taxonomy, schema-validated decision artifacts, mandatory escape hatch for security corpora) decides what gets scanned. The planned end-state is a continuously-running GitHub Actions mining job. ReDoS is explicitly out of scope. It is documented as complementary, with the right tools mapped per case.

## Progress — what has actually been accomplished

**1. Foundations, dogfooded on your own code first.** The whole thing was extracted from real verification work on usrmanage (#6) and fwlive (#120), with every trap and timing measured against `z3-solver==5.0.0` and ground-truthed against real BusyBox behavior. The first dogfooding wave closed three fundamental mirror-fidelity gaps: case-insensitive fold, Unicode-vs-ASCII class semantics, and dynamic `re.compile` classification.

**2. Corpus wave 1 (10 repos) took fractions from near-zero to usable.** gitleaks 18.5% → 60.2% → **82.4%**, CRS 38.4% → **64.8%**, trufflehog 23.3% → **93.5%**, ids_rules **87.9%**, validator.js **68.4%**. Each corpus also surfaced new dialect surface (YARA fullword boundaries, Perl, ModSecurity).

**3. Compiler fix waves, including the critical soundness wave.** Lazy quantifiers (the biggest single reject-bucket fix), hex escapes, negated classes, ASCII `\b`/`\B` encoding (the last genuine size limit for ASCII engines), and — most important — **the false-UNSAT soundness fix**: per-alternative anchors now *reject* instead of unsoundly hoisting, eliminating the false-proof failure mode. The follow-up trailing-`(?:…|$)` lowering (A1B) took gitleaks from 22.6% back up to **81.9%** after that fix temporarily dropped it below the gate.

**4. Rigorous measurement infrastructure.** `remeasure-from-inventory.py` recompiles *frozen* inventories through the current compiler with per-record flip deltas and no silent sample fallback. Every fraction quoted is reproducible, and soundness regressions show up as exactly attributable flips.

**5. The admission gate, validated by its first live trial.** The 2026-08-09 trial run probed 9 real candidates and **reproduced the prior wave-3 manual admission judgments exactly** — the strongest possible validation signal for a gate. It also found a real schema over-constraint on first use and produced the first live escape-hatch admission (java-html-sanitizer, triage-trial).

**6. A measured strategy for scale.** The diminishing-returns analysis (novel buckets knee at ~6–10 repos, user-regex value at ~20–50) plus the measured compile bottleneck (Z3 is ~99.9% of wall-clock and super-linear — Perl compiles at 177× the cost of RE2 per site) drove the decision: **mine broadly, score-and-sort, spend compile cycles on high-P(compiles) candidates**. The mine-and-approve pipeline (#129–#133) is filed and closed. It has probe automation, a mining scanner, and decision authoring. The authoring uses classify-then-template, so artifacts are schema-valid by construction. An LLM never approves a GO.

**7. A security-and-reliability audit pass.** The 2026-08 audit (#202, #184, #205) closed 30+ issues: the CI verify workflow that silently did not run, fail-open compiler helper gates, probe clone URL allowlists, subprocess timeouts, non-atomic artifact writes, plus a wave of structural refactors (harness moved into the package, extractor registry, template-method compilers).

**8. Backend research, delivered.** The Noodler escalation + cvc5 cross-check wave (#212/#213, phases #216–#221) is implemented and merged (PRs #222–#237). It verified verdict parity on 11 registry queries and 0 ECMA-pilot divergences on 5,622 decided comparisons. The U9 decision dropped `re.from_ecma2020` from harness scope. Lookaheads compile away to exact regular mirrors (13/13 equivalence measured) instead. Java dialect graduation (#150) is the next corpus frontier.

## Where it stands

Six days in (as of 2026-08-12): 207 commits, 109 merged PRs, 131 closed issues, 23 corpora in the cross-corpus matrix. The admission gate is validated, the compiler is soundness-hardened, and the scale strategy is decided. Open forward-looking work: Smith automation (#149), the Java dialect (#150), and deferred Smith batch-3 admits (#241 xibo-cms, #242 ail-yara-rules, #245 coraza-coreruleset). Smith #243/#244/#246/#247 are merged. There is no open correctness debt. The honest framing for explaining it: **it started as a verification method for your own repos, and it has become a measured, gated, continuously-improving engine for proving regex security properties across the ecosystem.**

Note caveat for accuracy: the [docs/verified-findings.jsonl](verified-findings.jsonl) file holds 10 *implementation/toolkit* findings (the trap lessons), while security-relevant findings from scanned corpora go `private_first` per [SECURITY.md](../SECURITY.md). So "10 verified findings" is a toolkit artifact, not a vulnerability count.
