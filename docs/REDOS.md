# ReDoS — complexity analysis (the complement to SMT)

SMT verification (this repo's core) answers **language** questions: "does any
string in the domain violate the boundary?" ReDoS (Regular expression Denial
of Service / catastrophic backtracking) is a different question — **complexity**
of the matching engine: "is there an input that makes the matcher take
exponential (or super-linear) time?" Use both:

| Question | Tool | Example |
|---|---|---|
| "can a string reach the shell with `;` after validation?" | Z3 (this repo) | whitelist exclusion proof |
| "is `^(a+)+$` going to hang on crafted input?" | ReDoS checker | recheck, safe-regex2 |
| "is this JS pattern safe on untrusted input?" | both | recheck for complexity + Z3-Noodler for semantics |

## Why SMT doesn't answer ReDoS

Z3's regex theory decides membership of a *regular language* — it has no
notion of backtracking, NFA state explosion, or engine-specific matching
cost. A regex can be semantically trivial and computationally catastrophic
(`(a|a)*` over a backtracking engine). Conversely, an engine can be
nonbacktracking (RE2, Rust `regex`, V8's linear-time optimizations) and immune
to exponential backtracking — but still vulnerable to *polynomial* blowups in
some engines (see USENIX Sec'22 "Exposing ReDoS Vulnerability of
Nonbacktracking Matchers").

## Tool map (deep-research findings, 2026-08)

| Tool | Type | Coverage | Notes |
|---|---|---|---|
| **recheck** (makenowjust-labs; orig. by TSUYUSATO, ex-Microsoft) | static + fuzz | ECMA-262 RegExp incl. **backreferences and lookarounds** | State of the art; JS/Scala lib; ESLint plugin; also usable via gixy-next for nginx configs |
| **safe-regex2** (fastify) | static heuristic | exponential-time detection | star-height-1 heuristic; fast, has false pos/neg; `limit` option |
| **safe-regex** (davisjam) | static heuristic | exponential-time detection | predecessor of safe-regex2; README admits false pos/neg — prefer vuln-regex-detector |
| **vuln-regex-detector** (davisjam) | dynamic (evil-input generation) | Python/JS/Go/Java/Rust… | Powers the npm ecosystem ReDoS study; detector service at VT |
| **RXXR / RXXR2** (Birmingham) | static pumping analysis | exponential ReDoS | Can't catch polynomial ReDoS; no lookarounds/backrefs |
| **ReDoSHunter** (USENIX Sec'21) | static + dynamic | power-DFA attack strings | Combined approach; beats single-method tools |
| **ReScue** (IEEE S&P 2023) | static + exploit gen | polynomial + exponential | Principled vulnerability modeling; exploit generation |
| **VulcanBoost** (USENIX Sec'25) | symbolic repair | fix generation | Detects + proposes semantics-preserving regex repairs |
| **Regulator** (UCSB, USENIX Sec'22) | dynamic | instrumentation of backtracking engine | Broad syntax support; 7× true positives vs prior work |
| **Regexploit** (pip) | dynamic | attack-string generation | Interactive; quick triage |
| **CodeQL / Semgrep** | static rules | in-repo scanning | CodeQL has ~90 regex-related patterns; Semgrep 1 ReDoS pattern for JS (as of 2022) — shallow coverage, use as triage |
| **rexploiter** (Wustholz et al. 2017) | static | exponential | Academic; attack automata |
| **gixy-next** | static | nginx `location`/rewrite regexes | Wraps recheck |

## Recommended stack for agents

1. **CI triage:** `safe-regex2` (npm) or CodeQL/Semgrep rule — cheap, catches
   obvious exponential patterns at review time.
2. **Deep check on boundary regexes:** `recheck` — the trustworthy checker;
   supports lookarounds/backrefs that SMT can't. JavaScript/TypeScript and
   Scala APIs, plus ESLint plugin.
3. **Exploit confirmation:** `regexploit` or `ReScue`-style attack strings;
   confirm with a timing test against the real engine on the real platform
   (device fidelity: BusyBox/GNU, Node/V8 versions matter).
4. **Semantics + language properties:** this repo's Z3 workflow.

## Phase 4 runner (this repo)

Isolated complexity stage (never install into the Z3 proof job):

```bash
npm install --prefix helpers/redos          # recheck@4.5.0, safe-regex2@5.1.1
python -m venv redos-env && redos-env/bin/pip install -e ".[dev]" -r requirements-redos.txt
redos-env/bin/python -m regexproof.redos.runner --input extractor.jsonl --out findings.jsonl
```

- Findings are versioned JSONL keyed by `regex_id` (see `regexproof/schemas/redos_finding.schema.json`).
- ECMA → `recheck` (required) + `safe-regex2` (triage); Python → `regexploit` (pip stand-in for vuln-regex-detector, which is not on PyPI); RE2 → `unsupported` (linear-time engine; USENIX Sec'22 super-linear caveat — do not claim safe).
- Join Z3 + ReDoS with `regexproof.redos.join.join_findings` — separate sections, no combined verdict.
- Error/timeout/unsupported must never be recorded as `safe`.

## Related reading

- Wikipedia: ReDoS (history, examples, tool list)
- payloadplayground.com/blog/regular-expression-denial-of-service-redos — practical payloads
- joshua.hu/comparing-redos-detection-tools — independent benchmark of Semgrep/CodeQL/regexploit, and more, on a vulnerable corpus
- HackTricks ReDoS page — exploitation playbook
