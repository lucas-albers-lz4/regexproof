# Deep research — using Z3/SMT to evaluate regex security (2026-08)

Deep-research pass aggregated into this repo. Sources are cited inline.
"Verified" = reproduced/measured on `z3-solver==5.0.0` during the
usrmanage/fwlive work. "Researched" = from the cited external source.

## 1. The solver layer: what Z3 actually does with regexes

- **Official guide — Regular Expressions** (microsoft.github.io/z3guide,
  "Regular Expressions" under Theories):
  Z3's regex theory covers regular languages. It "is a decision procedure for
  equalities and disequalities between non-symbolic regular expressions".
  Membership is handled via **lazy unfolding (symbolic derivatives)** and is
  *not complete* when combined with string constraints. This is the mechanism
  behind every timeout we measured — decomposition is the documented remedy.
- **dZ3** — "Symbolic Boolean derivatives for efficiently solving extended
  regular expression constraints" (PLDI 2021, ACM 10.1145/3453483.3454066;
  PDF at microsoft.com/research pldi21-SBFA-final):
  extended regex constraints (Boolean combinations) over an arbitrary
  character theory. This is the technique underlying Z3's sequence-theory
  regex solving.
- **Z3str3RE** — "An SMT Solver for Regular Expressions and Linear Arithmetic
  over String Length" (arXiv:2010.07253): length-aware decision procedure for
  regex membership + length arithmetic.
- **Z3-Noodler** (github.com/VeriFIT/z3-noodler, branch `devel`): automata-
  based string solver (equation stabilization + Mata). Adds `str.to_lower`/
  `to_upper`/`trim`/`delete`, and **`re.from_ecma2020`** — converts ECMA/JS
  regexes to Z3 regexes. Separate binary (cmake build), not pip-installable.
- **cvc5**: string + regex theories (incl. regex intersection). Useful as a
  second opinion. Cross-solver soundness bugs exist (for example,
  Z3Prover/z3#10379 —
  incorrect SAT on a string/regex formula, found against cvc5).
- **AWS Zelkova / "Z3 Automata"** (ahelwer.ca/post/2022-01-19-z3-rbac/): AWS
  hit Z3 regex limitations pre-2018 and extended Z3 with their own
  automata-based regex solver for IAM policy analysis — production precedent
  for SMT regex reasoning.
- **String-solver ecosystem** (for context): S3P, Norn, HAMPI, Kaluza,
  Stranger — symbolic-execution-era solvers; the length-aware + automata
  approaches converge in modern forks like Noodler.

## 2. JavaScript regexes — formal semantics (major 2025 result)

- **"Formal Verification for JavaScript Regular Expressions: a Proven
  Semantics and its Applications"** (Barrière, Deng, Pit-Claudel; arXiv
  2507.13091, 2025-07): the first mechanized, succinct, practical, complete,
  proven-faithful semantics for a modern regex language with **backtracking
  semantics**, proved equivalent to a line-by-line embedding of the official
  ECMAScript spec. Captures the **full backtracking tree** (all matches +
  priority), not just the top-priority match. Two applications: (1) contextual
  equivalence for regex rewrites (prove/disprove "safe rewrite" claims from
  prior work), (2) the first formal proof of the **PikeVM** algorithm used in
  real engines (Go regexp, Rust regex). Mechanized in Rocq.
  → **Relevance:** the definitive answer to "what does this JS regex actually
  mean?"; a reference for correctness-preserving rewrites (the same rewrites
  that ReDoS-repair tools like VulcanBoost must respect).

## 3. ReDoS tooling (complexity analysis — complements SMT)

Static/dynamic detectors for catastrophic backtracking — see REDOS.md for the
full tool map. Key findings:

- **recheck** (makenowjust-labs, originally TSUYUSATO/Microsoft): state of
  the art; supports backreferences and lookaround (beyond regular languages);
  fuzzing + static analysis; JS/Scala; ESLint plugin; used by gixy-next for
  nginx ReDoS scanning (joshua.hu case study).
- **safe-regex2** (fastify): star-height-1 heuristic, `limit` option; cheap CI
  triage, known false pos/neg (safe-regex's README explicitly recommends
  vuln-regex-detector for accuracy).
- **vuln-regex-detector** (davisjam): evil-input generation across 5
  languages; basis of the npm-ecosystem-scale ReDoS empirical study.
- **Academic line:** RXXR/RXXR2 (pumping analysis; no polynomial detection,
  no lookarounds) → ReDoSHunter (USENIX Sec'21; power-DFA) → ReScue
  (IEEE S&P 2023; polynomial + exponential, exploit generation) →
  VulcanBoost (USENIX Sec'25; symbolic repair) → Regulator (UCSB, USENIX
  Sec'22; engine instrumentation, 7× true positives).
- **Nonbacktracking engines are not immune:** USENIX Sec'22 "Exposing ReDoS
  Vulnerability of Nonbacktracking Matchers" — linear-time engines can still
  exhibit super-linear behavior; don't assume RE2/Rust-regex/V8 "solves" ReDoS.
- **SAST coverage is thin:** as of 2022, Semgrep had 1 ReDoS pattern for JS;
  CodeQL ~90 regex-related patterns total (ACM TOSEM survey). Use as triage,
  not as proof.

## 4. Python and JS specifics (verified + researched)

- Python `re` is a backtracking engine (PCRE-flavored): ReDoS applies;
  `re.fullmatch`/`match`/`search` are three different questions to encode
  (SEMANTICS.md). Third-party `regex` module adds features (case folding and
  more) — not SMT-expressible as written.
- JS RegExp is ECMA-262 with backtracking; V8 has linear-time optimizations
  for some patterns but not all. For SMT: rewrite lookaheads to string ops or
  use Z3-Noodler `re.from_ecma2020`; backreferences are out of scope for SMT
  (use recheck).
- sed/awk/POSIX: `[^\"]*`-style captures model exactly with
  `IndexOf`/`SubString` (byte-verified vs GNU sed AND BusyBox sed on the
  escaped-quote repro — identical truncation behavior).

## 5. What is NOT out there (the gap this repo fills)

No established public playbook for *coding agents* applying SMT regex
verification to improve code. The ecosystem has: solver docs (Z3 guide),
academic papers (above), ReDoS detectors (REDOS.md), and SAST rules — but no
agent-consumable decision tree that says "inventory → classify property →
encode with these 4 shapes → ground-truth → mutation-guard → CI-gate".
This repo is that artifact, built from measured results rather than
assumption. Our own verification work (usrmanage#6, fwlive#120) is the
empirical backbone.

## Sources

- Z3 guide, Regular Expressions: https://microsoft.github.io/z3guide/docs/theories/Regular%20Expressions/
- Z3-Noodler: https://github.com/VeriFIT/z3-noodler
- JS regex formal semantics: https://arxiv.org/abs/2507.13091
- Z3str3RE: https://arxiv.org/abs/2010.07253
- dZ3: https://www.microsoft.com/en-us/research/wp-content/uploads/2020/08/pldi21-SBFA-final.pdf
- Zelkova/Z3-Automata: https://ahelwer.ca/post/2022-01-19-z3-rbac/
- Z3 cross-solver soundness bug: https://github.com/Z3Prover/z3/issues/10379
- recheck: https://github.com/makenowjust-labs/recheck
- safe-regex2: https://github.com/fastify/safe-regex2
- vuln-regex-detector: https://github.com/davisjam/vuln-regex-detector
- ReDoSHunter: https://www.usenix.org/system/files/sec21-li-yeting.pdf
- ReScue: https://cenzhang.github.io/files/pubs/2023-ieeesp-rengar.pdf
- VulcanBoost: https://www.usenix.org/system/files/usenixsecurity25-li-yeting.pdf
- Regulator: https://sites.cs.ucsb.edu/~chris/research/doc/usenix22_regulator.pdf
- Nonbacktracking matchers: https://www.usenix.org/system/files/sec22-turonova.pdf
- ReDoS tool benchmark: https://joshua.hu/comparing-redos-detection-tools
