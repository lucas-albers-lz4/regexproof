# Corpus Admission Gate — decide what NOT to scan, before it costs a phase

**Status:** process spec (sweep/) · **Scope:** candidate-repo admission for all future corpus waves
**Related:** wave-3 plan (#110) "Rejected with evidence" list · detect-secrets NO-GO (wave-2 precedent) · `phase3_decision_matrix.json` · probe prediction vocabulary (umbrella C5; not live inventory `compile_reason` cardinality)

## Objective

Decide **before extraction** whether a candidate repo is worth the full corpus pipeline
(extractor, inventory, fraction, goldens, triage, docs, review rounds). Make the rejection
decision cheap, explicit, and evidence-backed — a 10-minute probe + a lookup, not a
mid-wave NO-GO or a review-round re-litigation.

This gate is the **admission** gate: *should we scan it at all?* It is orthogonal to the
**readiness** gate you already own (wave-3 P1 spikes, perl/pcre2 helper pre-gates,
mirror-fidelity REQUIRED-INPUT assertions) — *can we scan it correctly?* Admission runs
first, costs a tenth as much, and feeds the plan template's "Verified probe facts" section
so plan reviews start with evidence instead of finding its absence in round-1 folds.

## Why this exists (evidence, not vibes)

| Signal | Number | Implication |
|---|---|---|
| Reject-bucket taxonomy across all corpora | Historical gate note cited **17** reasons (top-5 ≈ **90.2%** of then-7,932 rejects). Live inventories now have **57** distinct `compile_reason` values — probe predictions use a separate **prediction vocabulary** (C5), not inventory cardinality | New corpora overwhelmingly re-hit known buckets; do not treat 17/22/21 as live truth |
| Last corpus to introduce a *novel* bucket | `ids_rules` (wave 1: unclosed-class, bad-range, m-flag) | Bucket-discovery yield ≈ zero after ~2 big corpora per dialect family |
| Biggest corpus ever admitted | semgrep 9,186 patterns → **27.4% no-go** (composite-pattern structural) | Size alone is not value; fraction risk is predictable pre-extraction |
| Best fix wave ever | gitleaks 221 patterns → A1B lowered **22.6% → 81.9%** | Small + security-boundary CAN pay off massively — the gate needs an escape hatch |
| NO-GO cost precedent | detect-secrets (wave-2): mid-wave NO-GO → document + propose + umbrella re-approval | A full phase + review rounds burned; an admission probe would have killed it in minutes |
| Wave-3 round-1 folds | 3/3 reviewers caught *unverified probe claims* ("~146 DOMPurify — verify") | Probe evidence must exist *before* the plan reaches review |

## The probe stage (minutes, not a phase)

Run BEFORE any plan-issue is written. No extractor code, no inventory, no commit of
corpus artifacts. A probe is: clone/pin the repo → count and classify. Output is the
"Verified probe facts" section of the plan (same role as wave-3 plan-issue.md's list).

1. **Regex-site count** — grep the target's pattern surface (`/pattern/flags`, `re.compile`,
   `regexp.MustCompile`, `@rx`, `pattern:`/`regex:` keys per the target's shape). Record
   total sites and per-file distribution. `<200` sites is a scale red flag unless another
   condition holds.
2. **Dialect + flag inventory** — classify patterns by dialect (py / pcre / re2 / ecma /
   perl / rust-regex) and flag/construct surface: `(?x)` verbose, `(?i)`, `(?s)`, `(?m)`,
   `\K`, `\g{`, POSIX classes, lookarounds, backrefs, wide/ascii encoding domains.
   A surface with zero prior corpus coverage is the strongest admission signal there is.
3. **Bucket-overlap prediction** — map the observed constructs onto the probe
   **prediction vocabulary** (machine-readable construct → bucket map; see mine-and-approve
   umbrella C5 / P1 task 0). Do not assume vocabulary size equals live inventory
   `compile_reason` cardinality. If ≥80% of predicted rejects land in buckets already owned
   by other corpora (composite-pattern, internal-anchor, pattern-too-long, lookaround,
   m-flag, unclosed-class), the corpus adds regression coverage, not discovery.
4. **Security-boundary classification** — is this a security tool / sanitizer / validator
   whose patterns sit on trust boundaries (secret detectors, XSS sanitizers, IP/username/
   email gates)? If yes, it gets the findings-triage trial regardless of scale (escape hatch).
5. **Findings-pipeline potential** — will this corpus produce *verified findings* (shape-1–5
   properties, rule_diff gaps) or only fraction statistics? Findings are the deliverable;
   fractions are bookkeeping.

## Admission conditions (any ONE passes)

| # | Condition | Probe evidence required |
|---|---|---|
| 1 | **New dialect / flag / encoding surface** not covered by any admitted corpus | dialect + flag inventory showing a first-seen construct class (perl `\K`, `(?x)` at scale, FoldCase→`i`, wide/ascii, …) |
| 2 | **Security-boundary corpus** with verified-findings potential | boundary classification + at least one concrete candidate property shape (injection alphabet, allowlist exclusion, counterexample finder, rule_diff) |
| 3 | **Large + under-saturated**: ≥1,000 patterns in a dialect still below ~85% encodable | site count + dialect mix + current fraction of the nearest admitted corpus in that dialect |

**Fails all three → NO-GO with evidence.** Typical NO-GO shape: same dialect, <200
patterns, no novel surface, no findings pipeline. The wave-3 "rejected with evidence" list
(django 12, wtforms 2, secretlint 5, url-regex 2 — "below batch scale; a python validators
pack would need 10+ repos to matter") is the first instance of this rule applied by hand;
the gate makes it a lookup.

**Mine-and-approve auto-NO-GO bar (pipeline, not a fourth admission condition):** the
author script may auto-file a schema-valid `no-go` (umbrella C4) when either
(a) `security_boundary` is `deterministic-false` and `regex_sites < 200`, or
(b) `regex_sites == 0` (zero-sites override — no regex surface to reason about;
boundary may still be `unknown`). Non-zero `unknown` and `deterministic-true` never
auto-file. Auto-path rationale is always `below-scale`. The ≥1000 bar remains only
for condition 3 (large-under-saturated).

**Probe boundary decision rule (pipeline):** ordered — positive signal →
`deterministic-true`; else explicit negative-category match →
`deterministic-false`; else → `unknown`. Absence of positive signals alone is not
sufficient for `false`.

## Escape hatch (mandatory, not optional)

Condition 2 is the hatch — and it exists because the best corpus decision you ever made
(gitleaks, 221 patterns, same-dialect, small) would otherwise have been rejected. Any
security-tool corpus **always** gets a findings-triage trial: admit at triage scope, run the
property pipeline on the encodable subset, and let the findings decide. The A1B lesson is
explicit: *small + security-boundary beat large + same-dialect for bug discovery.*

## Decision artifact

Each candidate commits `properties/generated/<corpus>_gate_decision.json` (schema:
`regexproof/schemas/gate_decision.schema.json`) BEFORE the plan-issue reaches review.
One sweep/ line per candidate in the plan ("admission: GO — condition 1, perl `\K` first-seen").

The `decision` field holds the **admission** outcome only: `go`, `no-go`, or
`triage-trial`. It never holds the fraction-gate outcome. The fraction gate
(>= 0.30 encodable) is sequential and separate — admission decides whether to
extract, fraction decides whether the result is usable. When they disagree
(for example historically semgrep: admission GO on conditions, fraction no-go
at 0.2741 — **superseded**: Wave-2 P3 live fraction is **0.4941 go**; keep the
split-field pattern, not the stale number),
record `fraction_decision` separately and keep `decision` for admission only.

Every `go` decision needs a defensible basis, enforced by schema
cross-constraints:

- `decision: go` with zero conditions met requires `decision_basis:
  grandfathered` (pre-gate corpus already admitted and running) or
  `escape_hatch` (security-boundary triage trial).
- `decision: no-go` while any admission condition is met is a schema
  contradiction — per the plan, any-one-passes => GO. The fraction outcome
  belongs in `fraction_decision`, never in `decision`.
- A fresh (non-grandfathered) decision must carry real probe evidence:
  `probe.regex_sites >= 1`. Grandfathered corpora are exempt (they predate
  the probe).

**Triage-trial lifecycle:** `triage-trial` is a security-boundary findings
trial, not a terminal state. The corpus runs the property pipeline on its
encodable subset; the findings decide the outcome. Graduation: when the trial
produces verified findings, re-admit as `go` (new artifact, `decision_basis:
escape_hatch`, supersedes the trial). Rejection: if the encodable subset is
too small to prove anything, record `no-go` (new artifact) and close the
trial. Record the outcome in the artifact's `related` field and one sweep/
line — a triage-trial must never persist un-resolved into the next wave.

**Grep-clean rule (concrete, per house style):** every candidate named in a wave plan's
scope must have a `*_gate_decision.json` whose `decision` field is `go` / `no-go` /
`triage-trial`; any candidate in a plan WITHOUT a committed decision artifact is a
plan-writing error, caught by the same grep discipline as the fraction-artifact check
(wave-3 P6 AC: "fraction values in `properties/generated/*_fraction.json` vs sweep decision
docs; mismatch = fail"). Note: the runtime gate enforces committed artifacts for
`CORPUS_MANIFESTS` rule corpora (backfill-invariant test); wave-PLAN candidates are caught
by this grep rule at review time, not by CI.

## NO-GO procedure (folded from wave-3 cross-cutting gate)

On NO-GO: document reason in the decision artifact + one sweep/ line, propose
threshold/scope adjustment if the evidence suggests one (e.g., "needs 10+ repos to matter —
revisit as a pack"), and record it in the wave umbrella. No silent NO-GO, no mid-wave
reversal without re-admission. The detect-secrets precedent is the canonical example.

## Non-goals

- NOT a replacement for the readiness gate (helpers, spikes, mirror-fidelity) — admission
  does not prove we can scan a corpus correctly, only that it is worth trying.
- NOT a corpus-update policy for already-admitted repos (re-pin/refresh cadence is a
  separate decision, untouched here).
- NOT a threshold change: the ≥0.30 fraction gate and `inventory_only` exemption in
  `phase3_decision_matrix.json` remain the post-extraction GO/NO-GO rule. Admission and
  fraction gates are sequential: admission decides *whether to extract*, fraction decides
  *whether the result is usable*.

## Falsifiable acceptance criteria

- [ ] Probe stage has a defined command sequence (step 1–5 above) that takes <10 minutes
      on a candidate repo and produces the plan's "Verified probe facts" section
- [ ] A candidate failing all three conditions can be rejected with evidence and zero
      extractor code committed
- [ ] `gate_decision.schema.json` validates every committed `*_gate_decision.json`;
      `pytest tests/` green
- [ ] Grep-clean: every candidate in a wave plan has a committed decision artifact
      (`decision` ∈ go/no-go/triage-trial) — enforced by the same grep discipline as
      existing fraction-artifact checks
- [ ] Security-tool corpora never rejected on scale alone (escape hatch path documented
      with the gitleaks precedent as the worked example)
- [ ] No mid-wave NO-GO without the candidate's admission decision artifact on record
      (detect-secrets precedent: admission artifact would have preceded the wave)
