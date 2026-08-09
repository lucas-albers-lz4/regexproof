# semgrep routing spike (Corpus Wave 2 / P1)

Pinned corpus: `semgrep/semgrep-rules` @ `40b8c63f` (existing
`batch/corpora/semgrep_rules` pin).

## Problem

Pre-P3 fraction **0.2842** (no-go) was a **denominator-precision artifact**:
generic `_YAML_REGEX` in `rule_file.py` matches YAML `pattern:` keys whose
values are semgrep **code-pattern language** (`$X`, `...`), not regex.
**Resolved in Wave-2 P3 (#106):** dedicated `extract_semgrep_yaml` →
**0.4941 go** (707/1431); see `semgrep_rules_p3_drift.json` and TRAPS §30.
Wave-3 P6 (`sweep/corpus-wave3/supersession.md`) records this as the live
fraction owner so phase-3 **0.2741** is never cited as current.

Sampled reject levers (pre-fix inventory): `composite-pattern` ≈ 3247,
`internal-anchor` ≈ 3113 — many are code-pattern sites miscounted as regex.

## True regex sites

- `pattern-regex:` (incl. block scalars `pattern-regex: |`)
- `metavariable-regex:`
- Nested under `pattern-either` / `pattern-inside` / `patterns:` lists

## Dialect

Runner maps `semgrep_rules` → `py_re` (`runner.py:129-133`). Semgrep evaluates
`pattern-regex` with the **rust `regex` crate** (Unicode `\d\w\s`).

**Decision for P3 (pending production extract):** prefer a `rust_regex` /
semgrep dialect route; if unavailable, declare **ASCII approximation** as the
domain and differential-fuzz against a rust-regex helper. Never silently keep
`py_re` Unicode semantics on a secret-adjacent corpus.

## Spike sample fraction

Fixture surface `semgrep` in `mirror-fidelity-gate.py` uses a tiny
`pattern-regex`-shaped probe under `py_re` to validate gate machinery only.
Full re-extraction + ≥0.30 gate flip is **P3** (`extract_semgrep_yaml`).

## Hand-off

P3 must:

1. Ship dedicated `extract_semgrep_yaml` (not in-place generic edits).
2. PR supersession map (baseline fraction + frozen inventory hashes).
3. Reclassify/eliminate `composite-pattern` / `internal-anchor` pseudo-sites.
