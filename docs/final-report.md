# Corpus wave final report (#51–#57)

**Wave:** corpus stress-test (issues #51–#57).  
**Disclosure:** security-tool findings remain `private_first` ([SECURITY.md](../SECURITY.md)).

## Encodable fractions (Phase 1 matrix)

See [properties/generated/cross_corpus_matrix.md](../properties/generated/cross_corpus_matrix.md).

| Corpus | Decision | Fraction |
|---|---|---|
| gitleaks | go | **0.8235** (was 0.6018 pre-`\b`) |
| validatorjs | go | 0.684 |
| coreruleset | go | **0.7168** (was 0.6478) |
| trufflehog | **go** | **0.9349** (was 0.2326 no-go) |
| ids_rules | go | 0.879 |
| semgrep_rules | no-go | 0.2741 |
| pcre2/re2/cpython/busybox samples | go | ≥0.53 |
| rust_regex | inventory_only | — |

> **Corpus Wave 2 (2026-08-09):** authoritative current fractions are in
> `cross_corpus_matrix.*` (semgrep **0.4941 go**, yara **0.6563 go**,
> test262 sample **0.8095**). The table above is the original wave-#51 snapshot.
>
> **Corpus Wave 3 (2026-08-09):** matrix rollup adds spamassassin **0.7479**,
> noseyparker **0.7354**, shhgit **0.9263**, dompurify **0.5625**, isemail
> **0.8000**, email_addresses **0.5000**, perl_tre **0.3541**,
> go_regexp_tests **0.7524**, v8_mjsunit **0.5383**. See TRAPS §34–§38 and
> `sweep/corpus-wave3/supersession.md`.

## Gap closure (Phase 2–3)

- Toolkit-fix vehicle #45 accepted: lazy strip, hex soundness (TRAPS #23),
  negated-class, scoped `(?i:)`, pattern-too-long policy (TRAPS #21).
- Gitleaks: **18.5% → 60.2%**. Residual rows classified a/b/c in
  `gitleaks_residual_abc.json` (unexplained=0).
- Non-lazy needle: CRS **38.4% → 64.8%** (hex + class/flag lifts), recorded in
  `phase3_delta_table.json`.
- Hermes-agent before/after recorded in `hermes_agent_delta.json` (sample IDs frozen).
- No-go corpora re-decided in `phase3_decision_matrix.md`.

## Rule_diff + ReDoS (Phase 4)

- Three families with declared pair semantics:
  `phase4_rule_diff_families.{json,md}`.
- Issue **#44** CRS SAT gaps folded as `private_first` (no auto upstream publish).
- ReDoS stage: count cap replaced by **wall-clock** `--redos-timeout-s` /
  `budget.redos_wall_s`.

## Findings / lessons (Phase 5)

- Hex escape must lower to the codepoint, not literal text (pre-gate + TRAPS #23).
- Presence of `parse-error` unclassified rows is a Phase-1 hard fail — prefer
  typed reasons (`unclosed-class`, `unsupported-syntax`, …).
- Cross-scanner rule_diff requires shared detector intent; unrelated rules are
  not pairs.
- Next-wave candidates (remaining): semgrep `composite-pattern` / `internal-anchor`
  surface; optional `(?-i:)` if measured surface rises; py_re `re.ASCII` `\b` wiring.

## Word-boundary wave (#62–#66)

- Spike **GO** (`word_boundary_spike.json`): edge `\b` under ASCII `\w` agrees with
  `re.ASCII` / RE2; Unicode-default Python diverges (domain gate required).
- Landed: `WordBounded` rewrite in `simple_parse` / `lower`; re2/pcre/ecma encode;
  py_re Unicode-default still rejects; mid-pattern / `\B` reject (TRAPS #25).
- Remeasure: gitleaks **60.2% → 82.4%** (49 IDs flipped); trufflehog **23.3% → 93.5%**
  (decision flip to go); CRS **64.8% → 71.7%**. See `word_boundary_wave_delta.json`.

## Artifact index

| Artifact | Phase |
|---|---|
| `cross_corpus_matrix.*` | 1 |
| `phase2_toolkit_fix_closeout.md` | 2 |
| `remeasure-frozen-ids.py` | 2→3 |
| `phase3_delta_table.json` | 3 |
| `gitleaks_residual_abc.json` | 3 |
| `hermes_agent_delta.json` | 3 |
| `phase3_decision_matrix.*` | 3 |
| `phase4_rule_diff_families.*` | 4 |
| `mirror_fidelity_gate.json` | pre-gate |
| `word_boundary_spike.json` | `\b` spike |
| `word_boundary_wave_delta.json` | `\b` remeasure |
