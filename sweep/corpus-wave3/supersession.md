# Corpus Wave 3 — supersession / ownership map

Wave-3 artifacts **own** their paths. Do not treat Wave-2 or phase-3
snapshots as live for these corpora.

| Path / corpus | Owner | Baseline | Replacement |
|---|---|---|---|
| `spamassassin_*` | wave3-p2 / #122 | absent / pre-admission | **0.7479 go** |
| `noseyparker_*` | wave3-p3 / #123 | trial probe | **0.7354 go** + `(?x)` strip |
| `shhgit_*` | wave3-p3 / #123 | trial probe | **0.9263 go** |
| `dompurify_*` | wave3-p4 / #125 | plan ~146 FP grep | **0.5625 go** (16 sites) |
| `isemail_*` | wave3-p4 / #125 | plan ~121 FP | fraction **0.8000**; admit **NO-GO** |
| `email_addresses_*` | wave3-p4 / #125 | plan ~71 FP | fraction **0.5000**; admit **NO-GO** |
| `perl_tre_*` | wave3-p5 / #127 | sample-only risk | **0.3541 go** full suite |
| `go_regexp_tests_*` | wave3-p5 / #127 | sample-only risk | **0.7524 go** full suite |
| `v8_mjsunit_*` | wave3-p5 / #127 | sample-only risk | **0.5346 go** full suite |
| `yara_rules_*` gate backfill | wave3 coordination | wave2-p2 measure | gate schema-valid; fraction still **0.6563** (wave2-p2) |
| `cross_corpus_matrix.*` | wave3-p6 / #117 | caret-in-x-103 rollup | wave `corpus-wave3` |
| `wave3_artifact_repro.sha256` | wave3-p6 / #117 | n/a | SHA256 of wave-3 fraction + inventory artifacts |
| `batch_repro.sha256` | CI Phase-6 gate | three corpora | **unchanged this wave** (still gitleaks/validatorjs/detect-secrets) |

## Superseded live claims (do not cite as current)

| Claim | Was | Now |
|---|---|---|
| semgrep fraction no-go **0.2741** / **0.2842** | phase-3 / pre-P3 denom | Wave-2 P3 **0.4941 go** (TRAPS §30) |
| DOMPurify / isemail / email_addresses plan site counts | ~146 / ~121 / ~71 | precise **16 / 5 / 4** |

Wave-2 coordination (`sweep/corpus-wave2/semgrep-routing.md`) remains the
owner of the semgrep denom lesson; Wave-3 only records the supersession
above so grep-clean does not revive 0.2741 as live.
