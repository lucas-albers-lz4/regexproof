# Why regexproof

> **Last updated:** 2026-08-15 · **Next review:** 2026-11-15 — the point-in-time stats in "Where it stands" and the conversion ledger age fast; re-verify them before quoting.

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
4. **Measurement at corpus scale.** A batch scanner inventories regex sites in real open-source repos, compiles them through the current compiler, and reports an *encodable fraction* — turning "is the toolkit any good" into a number you can track and improve. Encodable fraction is toolkit quality. The product number is the [conversion ledger](../properties/generated/conversion-ledger.md): properties asked, SAT + ground-truth, and accepted upstream.
5. **A disciplined acquisition pipeline.** An admission gate (21-bucket reject taxonomy, schema-validated decision artifacts, mandatory escape hatch for security corpora) decides what gets scanned. The planned end-state is a continuously-running GitHub Actions mining job. ReDoS is explicitly out of scope. It is documented as complementary, with the right tools mapped per case.

## Two machines, then a conversion step

The repo is two machines in series, plus a conversion step that is still mostly manual:

1. **Funnel.** Mine, score, probe, admit or no-go. Goal: spend compile budget on security-boundary regex, not on more of the same.
2. **Prove / don't prove.** Encode the pattern into Z3, reject unsoundly, then ask a shape-1–5 property. SAT + ground-truth against the real engine is a candidate finding; UNSAT is "holds in the declared domain"; timeout is not a pass.
3. **Convert.** A finding only becomes a real security result if it reproduces in the real code *and* someone files it. That last step is the product. The first two are the factory.

Heap's law (and the Good-Turing-ish singleton work) saturates **(1) and the compiler half of (2)**. It does not saturate **(3)**.

What the repo already measured is vocabulary growth: novel reject buckets flatten around 6–10 repos per dialect family; user-code pattern novelty was still steep at n=4 (singleton fraction ~0.98). The written stopping rule is a trailing window — last two repos, novel rate under ~3% — not a formal Heap fit. That is the right stop for "we are done teaching the compiler." After that, more ingest mostly buys more of the same surface, which is useful for rate estimates and useless for new encode paths.

The claim that still needs proof is a different quantity:

**P(real bug) ≈ P(site is on a security boundary) × P(encodable) × P(right property written) × P(SAT and ground-truthed) × P(it is actually a security miss, not a mirror error)**

Encodable fraction is tracked. Boundary classification is gated, and it already false-positives. Ground-truth on witnesses is enforced. What was missing as a ledger is conversion: sites → properties written → SAT → reproduced → disclosed → accepted upstream.

One filed issue is an existence proof, not a rate. The cleanest existence proofs so far are also the weakest for "in the wild": usrmanage #6 and fwlive #120 are own code; CRS rule_diff gaps (for example `942220` / `JSon.1e309`) are real, machine-checked, and stuck behind `private_first` because they are security-tool findings. The method works. It has not yet shown how often this class appears in other people's validators, sanitizers, and parsers.

Two independent parameters:

- **Accuracy** — of the five factors above, the ones the toolkit controls are encode soundness, property shape, and ground-truth. The worst failure is a false UNSAT (saying safe when it isn't). The noisy failure is SAT that does not reproduce, or reproduces and is not security-relevant. Heap's law does not move these.
- **Prevalence** — how often regex-on-a-boundary is wrong in the wild. Heap's law on *pattern types* is a weak proxy. After the compiler saturates, more corpora *do* help here, because you need a denominator: N boundary sites with a property actually asked. Until that denominator exists, "keep ingesting" is still compiler-coverage work dressed as product-eval.

The ingest-until-diminishing-returns plan is correct **for the toolkit**. The product claim needs a second stop condition: conversion yield over a frozen admitted set, not novel-bucket yield. A small accepted-upstream count with a known false-positive rate proves more than another hundred GO corpora.

## Conversion ledger

Live artifact: [`properties/generated/conversion-ledger.md`](../properties/generated/conversion-ledger.md) (JSON beside it). Regenerated from committed scanner NDJSON, batch summaries, rule_diff reports, and the curated last mile in [`conversion-upstream.jsonl`](conversion-upstream.jsonl). Golden CI drift-checks it, same as compiler-feature-yield.

Headline counts (re-verify from the artifact before quoting):

| stage | count |
|---|---|
| sites extracted / encodable | 123,643 / 76,955 (fraction 0.622) |
| scanner rows | 7,141 — of which 5,558 are classification (`usage_mismatch` / `intent_mismatch`), not security bugs |
| properties asked | 649 (616 UNSAT / 33 SAT; all 33 SAT ground-truthed) |
| rule_diff report SAT + GT (CRS + gitleaks pilots) | 12 |
| accepted upstream (`fixed_upstream`) | 1 (usrmanage P3, own code, later fixed) |
| existence proofs | 2 (that one + CRS 942220 `private_first`) |
| filed false positives | 1 (happycow interpolated `re.search`, already `re.escape`'d) |
| third-party public accepted | 0 |

Most scanner "findings" are call-kind classification. Most asked properties are synthesized validator.js shape-1/2 rows, and most of those hold (UNSAT). SAT + ground-truth is cheap to count and is not the same as a filed bug. `docs/verified-findings.jsonl` remains the toolkit-trap log (10 VF-* rows); it is not this numerator.

The next measurement that speaks to the end result is conversion yield on already-admitted security-boundary corpora, not another mine flush.

## Progress — what has actually been accomplished

**1. Foundations, dogfooded on your own code first.** The whole thing was extracted from real verification work on usrmanage (#6) and fwlive (#120), with every trap and timing measured against `z3-solver==5.0.0` and ground-truthed against real BusyBox behavior. The first dogfooding wave closed three fundamental mirror-fidelity gaps: case-insensitive fold, Unicode-vs-ASCII class semantics, and dynamic `re.compile` classification.

**2. Corpus wave 1 (10 repos) took fractions from near-zero to usable.** gitleaks 18.5% → 60.2% → **82.4%**, CRS 38.4% → **64.8%**, trufflehog 23.3% → **93.5%**, ids_rules **87.9%**, validator.js **68.4%**. Each corpus also surfaced new dialect surface (YARA fullword boundaries, Perl, ModSecurity).

**3. Compiler fix waves, including the critical soundness wave.** Lazy quantifiers (the biggest single reject-bucket fix), hex escapes, negated classes, ASCII `\b`/`\B` encoding (the last genuine size limit for ASCII engines), and — most important — **the false-UNSAT soundness fix**: per-alternative anchors now *reject* instead of unsoundly hoisting, eliminating the false-proof failure mode. The follow-up trailing-`(?:…|$)` lowering (A1B) took gitleaks from 22.6% back up to **81.9%** after that fix temporarily dropped it below the gate.

**4. Rigorous measurement infrastructure.** `remeasure-from-inventory.py` recompiles *frozen* inventories through the current compiler with per-record flip deltas and no silent sample fallback. Every fraction quoted is reproducible, and soundness regressions show up as exactly attributable flips. The compiler feature-yield artifact ([`../properties/generated/compiler-feature-yield.md`](../properties/generated/compiler-feature-yield.md)) aggregates `unencodable_reason` across the triage corpus and weights each reason by corpus admission (GO=3, triage-trial=2, no-go=1), giving a stable map of where compile budget buys coverage.

**5. The admission gate, validated by its first live trial.** The 2026-08-09 trial run probed 9 real candidates and **reproduced the prior wave-3 manual admission judgments exactly** — the strongest possible validation signal for a gate. It also found a real schema over-constraint on first use and produced the first live escape-hatch admission (java-html-sanitizer, triage-trial).

**6. A measured strategy for scale.** The diminishing-returns analysis (novel buckets knee at ~6–10 repos, user-regex value at ~20–50) plus the measured compile bottleneck (Z3 is ~99.9% of wall-clock and super-linear — Perl compiles at 177× the cost of RE2 per site) drove the decision: **mine broadly, score-and-sort, spend compile cycles on high-P(compiles) candidates**. The mine-and-approve pipeline (#129–#133) is filed and closed. It has probe automation, a mining scanner, and decision authoring. The authoring uses classify-then-template, so artifacts are schema-valid by construction. An LLM never approves a GO.

**7. A security-and-reliability audit pass.** The 2026-08 audit (#202, #184, #205) closed 30+ issues: the CI verify workflow that silently did not run, fail-open compiler helper gates, probe clone URL allowlists, subprocess timeouts, non-atomic artifact writes, plus a wave of structural refactors (harness moved into the package, extractor registry, template-method compilers).

**8. Backend research, delivered.** The Noodler escalation + cvc5 cross-check wave (#212/#213, phases #216–#221) is implemented and merged (PRs #222–#237). It verified verdict parity on 11 registry queries and 0 ECMA-pilot divergences on 5,622 decided comparisons. The U9 decision dropped `re.from_ecma2020` from harness scope. Lookaheads compile away to exact regular mirrors (13/13 equivalence measured) instead. Java dialect graduation (#150) is the next corpus frontier.

**9. Conversion ledger (product measure).** Heap's-law ingest saturates the compiler. The conversion ledger saturates the claim "we find real security problems." First freeze: 123,643 extracted sites → 649 properties asked → 33 SAT (all ground-truthed) → 1 accepted upstream, 0 third-party public. Script: `scripts/conversion-ledger.py`.

## Where it stands

Six days in (as of 2026-08-12): 217 commits, 116 merged PRs, 137 closed issues, 23 corpora in the cross-corpus matrix. The admission gate is validated, the compiler is soundness-hardened, and the scale strategy is decided. A dogfooding singleton analysis (PR #259, frozen at `properties/generated/dogfooding_novelty_2026-08-12.json`) measures the user-code P(compiles) distribution: 2,857 regex sites / 1,990 distinct (canonicalized) across usrmanage, fwlive, happycow, and the hermes-agent fork. The singleton fraction is 0.984 on distinct patterns and 0.912 per-observation (n1/N over sites); both are convenience-sample estimates, not a formal Good-Turing estimator. The shell gap is quantified: 273 sites (9.6% of the surface) come from shell scripts, which no project extractor covered — the posix-shell dialect wave (#264–#269) closes that gap. The P2.5 re-freeze via the registered shell extractor (`dogfooding_novelty_2026-08-12_POST_P2.json`) now shows 2,856 sites / 272 shell sites: the +8 vs P1 were the command-substitution sites the context guard wrongly suppressed (fixed in #274), and the −9 vs 281 are the false positives the wave's cumulative zen-MCR review removed (heredoc data bodies, `grep -P` PCRE-in-shell, escaped sed delimiters, `sed -E` → ERE). The P1 snapshot stands as the historical pre-fix freeze; each correction is a documented, test-covered precision fold. (The feed probe re-measure is net-zero: 713 sites — the OpenWrt heredoc bodies contain no regex patterns.) Open forward-looking work: the dogfooding + shell-dialect + OpenWrt-probe wave (#264–#269), Smith batch-4 admits (#260–#262) — **malcontent (#261) measured GO 0.6993 (5,540/7,922 encodable, 9 private-first findings; the largest yara corpus in the matrix, own `rules/` pack only)** — Smith batch-5/6 admits (#277–#283, #284–#290), Smith automation (#149), and the Java dialect (#150). Smith batch-3 admits #241 (xibo-cms) and #242 (ail-yara-rules) are merged; #245 (coraza-coreruleset) was superseded to no-go (its `@owasp_crs` tree is unmodified OWASP CRS v4.25.0 — duplicate of admitted `coreruleset`). There is no open correctness debt. The honest framing for explaining it: **it started as a verification method for your own repos, and it has become a measured, gated, continuously-improving engine for proving regex security properties across the ecosystem.**

Note caveat for accuracy: the [docs/verified-findings.jsonl](verified-findings.jsonl) file holds 10 *implementation/toolkit* findings (the trap lessons), while security-relevant findings from scanned corpora go `private_first` per [SECURITY.md](../SECURITY.md). So "10 verified findings" is a toolkit artifact, not a vulnerability count. The product count is the [conversion ledger](../properties/generated/conversion-ledger.md): accepted upstream and existence proofs, with false positives enumerated rather than buried.
