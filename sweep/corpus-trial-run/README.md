# Corpus Admission Gate — Trial Run (2026-08-09)

First real stress test of the corpus admission gate (issue #120 / PR #121).
Nine candidate repos probed live; each got a `*_gate_decision.json` validated
against `regexproof/schemas/gate_decision.schema.json`.

## Results

| Candidate | Sites | Decision | Basis | Probe evidence (live) |
|---|---|---|---|---|
| noseyparker | 189 | **go** | admission_conditions | 90 YAML rule files, `pattern:` key; 136 `(?x)` + 69 `(?i)` + 8 `(?s)` + 3 `(?m)` + 41 `\b` |
| shhgit | 95 | **go** | admission_conditions | config.yaml: 95 regex entries of 150 signatures; `syntax.FoldCase` → `i` lift |
| dompurify | 146 | **go** | admission_conditions | src/purify.ts + src/regexp.ts (33 literals by narrow grep; plan count authoritative) |
| java-html-sanitizer | 22 | **triage-trial** | escape_hatch | 2 files with `Pattern.compile`; Java = first-seen dialect surface |
| wtforms | 2 | **no-go** | — | below batch scale; py dialect covered |
| django-validators | 12 | **no-go** | — | wave-3 rejected-with-evidence, re-confirmed |
| secretlint | 5 | **no-go** | — | wave-3 rejected-with-evidence |
| url-regex | 2 | **no-go** | — | wave-3 rejected-with-evidence |
| git-secrets | 0 | **no-go** | — | shell grep-based, no regex corpus |

## What the trial proved

1. **The probe stage works end-to-end.** Live clones + real counts for 5
   candidates; wave-3 verified numbers for the rejected set. Noseyparker and
   shhgit counts matched the wave-3 plan exactly — the plan's probe facts
   were trustworthy.
2. **The gate reproduces the wave-3 admission judgment.** Every corpus the
   wave-3 plan wanted in (noseyparker, shhgit, dompurify) got GO; every
   corpus it rejected with evidence (wtforms, django, secretlint, url-regex)
   got NO-GO. The gate encoded the team's existing instincts as a lookup.
3. **`triage-trial` is now a real, exercised state.** java-html-sanitizer is
   the first live triage-trial (Java dialect frontier + sanitizer boundary,
   small corpus) — the escape hatch graduated from hypothetical example to
   committed artifact.
4. **The gate found its own schema bug on first use.** git-secrets (0 regex
   sites) failed the fresh-probe `regex_sites >= 1` constraint — but zero
   regex sites is itself valid NO-GO evidence. Fixed: the evidence minimum
   now applies to go/triage-trial only (commit pending).

## Trial-run findings for the toolkit

- **Java dialect is the next frontier.** java-html-sanitizer shows a
  first-seen dialect with a sanitizer boundary. A java dialect compiler
  pass + helper would be the wave-4 prize candidate.
- **git-secrets is a probe lesson:** "security tool" does not imply "regex
  corpus." Filename/grep-based matching has no regex surface — the probe
  must count regex literals, not trust the tool category.
- **The rejected-with-evidence list aged well.** All four wave-3 rejections
  re-confirmed by the gate's conditions; no candidate flipped.

## Artifacts

- 9 decision files: `properties/generated/{corpus}_gate_decision.json`
  (all with `related.trial_run: true`)
- All 16 committed decisions validate against the current schema
- Probe clones: `/tmp/tr-*` (disposable; not committed)
