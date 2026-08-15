# Rank shortlist 2026-08-15 (`origin/main` `0b2a448`)

Ledger: 893 rows (`gated:no-go` 706, `gated:go` 64, `gated:triage-trial` 40, `mined` 83). Queue still capped. Rank skips gated URLs by default.

## Allocator

`python scripts/rank-mine-candidates.py --allocator score-v2 --limit 10 --status mined` on ungated rows returned `tree_probe.reason=missing-probed-pin` (ledger rows have `pin`, not `pin_probed`; score-v2 only joins `pin_probed` from existing `*_gate_decision.json`). **Probe order is score-v1.**

## score-v1 top 10 (probe order)

| # | repo | stars | pin | query family |
|---|---|---|---|---|
| 1 | NVIDIA-NeMo/Speech | 18119 | `ef41369156bd` | detect-secrets |
| 2 | elizaOS/eliza | 19036 | `f2d016e0abf5` | gitleaks.toml |
| 3 | langflow-ai/langflow | 153170 | `976ec789d288` | detect-secrets |
| 4 | openSUSE/open-build-service | 1068 | `3cb887bc02e3` | gitleaks.toml |
| 5 | NVIDIA-BioNeMo/bionemo-recipes | 841 | `0a66c65ae3c8` | .gitleaks.toml |
| 6 | code-dot-org/code-dot-org | 896 | `107b390a3380` | secrets.yml |
| 7 | superdoc/docx-editor | 958 | `1c57bb1f19ee` | gitleaks.toml |
| 8 | Pinvou/pinvou-agent | 710 | `2dba215dcc91` | gitleaks.toml |
| 9 | tufantunc/ssh-mcp | 603 | `22363b2f13ef` | gitleaks.toml |
| 10 | itbench-hub/ITBench | 492 | `fb1a358fa4a2` | detect-secrets |

None of these URLs had `*_gate_decision.json` or `batch/corpora/<slug>/` before this wave.

## Gate outcomes (2026-08-15)

All 10 **NO-GO**. No new GOs → no Smith PRs this wave.

| repo | sites | boundary | decision | note |
|---|---|---|---|---|
| NVIDIA-NeMo/Speech | 256 | unknown | no-go | ASR/TTS product regex |
| elizaOS/eliza | 0 (unprobed) | unknown | no-go | clone TimeoutExpired 300s |
| langflow-ai/langflow | 1051 | unknown | no-go | frontend tests, not detect-secrets pack |
| openSUSE/open-build-service | 1402 | deterministic-true | no-go | vendored swagger-ui |
| NVIDIA-BioNeMo/bionemo-recipes | 138 | deterministic-true | no-go | below-scale ML recipes |
| code-dot-org/code-dot-org | 0 (unprobed) | unknown | no-go | clone TimeoutExpired 300s |
| superdoc/docx-editor | 2202 | deterministic-true | no-go | editor unit tests |
| Pinvou/pinvou-agent | 2082 | deterministic-true | no-go | agent contract tests |
| tufantunc/ssh-mcp | 136 | deterministic-true | no-go | small guard, below pack scale |
| itbench-hub/ITBench | 16 | unknown | no-go | below-scale |

Probes walked ledger `pin` with `--allow-stale-pin` (default-branch HEAD had moved on every clone).
