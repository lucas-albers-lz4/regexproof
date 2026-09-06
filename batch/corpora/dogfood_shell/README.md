# dogfood_shell corpus — Smith intake decision (funnel #615)

**Decision:** GO to mine (registration-only entry exists; materialization is
the follow-on per the manifest note below).

## Probe facts (measured 2026-09-06, current HEAD)

- **Candidate:** dogfooding universe (usrmanage / fwlive / happycow /
  hermes-agent-fork) via `scripts/dogfood-singleton-analysis.py`
  (P1-frozen shell semantics: `grep -F` skipped, sed `s///` search part
  only, awk address/`-F` forms only, `[[ =~ ]]` unquoted RHS only).
- **Sites:** 6,648 total (ecma 3,460 / posix-shell 1,670 / py_re 1,518).
  Frozen P1 pins (2026-08-12) recorded 2,856 (shell 272) — the universe
  grew, led by hermes-agent-fork (4,331 sites, only 63 shell).
- **Per-repo shell:** usrmanage 1,274 / fwlive 333 / happycow 0 /
  hermes-agent-fork 63.
- **Encodable (posix-shell compiler):** 1,575/1,670 = **0.9431** —
  passes the `>= 0.30` fraction gate 3× over.
- **Rejects (actual, not predicted):** internal-anchor 79, parse-error 15,
  gnu-word-boundary 1. The predicted `stateful: 329` bucket did NOT
  materialize — the backend handles stateful `s///` fine.

## Blocker answers (funnel #615 A1–A2)

1. **`corpus_pin: local` — resolved as procedural, not structural.**
   `regexproof/batch/manifests.py` already carries a registration-only
   `dogfood_shell` entry (posix-shell, `shell_posix` extractor,
   `path = batch/corpora/dogfood_shell/rules`, NOT in `WAVE_CORPORA`).
   Materialize: symlink the merged dogfooding tree at that path, then add
   to `WAVE_CORPORA` **together** (the manifest note: a 0-site silent pass
   would otherwise read `go` against an empty tree).
2. **Pin drift — pin-refresh rule.** 3/4 repos moved since the P1 freeze
   (usrmanage `abe0fe7→7116f8d`, fwlive `3477ace→a3d6c54`,
   hermes-agent `7b5ba20→843ff82`; happycow pinned at `ee7212c`).
   Rule: re-freeze (`--snapshot-out` + pin record) at materialization
   time; never mine against the 2026-08-12 denominator.
3. **Shell encodability — answered 0.9431.** Fraction gate passes;
   dominant reject is internal-anchor (variable-bearing candidates like
   `$_u` — extractor-false-positive class, not a backend gap).

## Smith scope (follow-on mine, not this wave)

- Materialize merged tree at pin → symlink
  `batch/corpora/dogfood_shell/rules` → add to `WAVE_CORPORA`
- Measure (`measure-corpus-fraction.py --corpus dogfood_shell`)
- Findings triage per `docs/REPORTING.md`
- `dogfood_shell_smith_decision.json` + measure recipe (this file)
- NOT a security tool → public-first disclosure

## Acceptance

- [x] `dogfood_shell_gate_decision.json` committed (2026-08-12, `go`)
- [x] A1 fractions measured (this file + funnel #615 audit trail)
- [x] First conversion-hop property landed (wave 1: `normalize-fixpoint`,
      `properties/generated/dogfood_shell_conversion_wave.md`)
- [ ] Merged-tree materialization + `WAVE_CORPORA` (follow-on mine)
- [ ] `dogfood_shell_smith_decision.json` schema-valid, fraction recorded
