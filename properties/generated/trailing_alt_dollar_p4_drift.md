# P4 — Secret-detector corpus + drift (#84)

Post-P3 (#90) compiler baseline. Extraction re-runs vs frozen `regex_id`
sets; `(***)` shared-prefix gitleaks rows bucketed as corpus artifacts.

## gitleaks (in-repo 221 rules)

| Check | Result |
|---|---|
| `measure-corpus-fraction.py` | **0.8190** (181/221) — stable vs P3 |
| `remeasure-frozen-ids.py` vs `gitleaks-frozen-ids.ndjson` | missing=0, extra=0; one enc→unenc flip (below) |
| `python -m regexproof.batch --corpus gitleaks` | ok |

### Encodability flip vs frozen IDs (not extraction drift)

| regex_id | Now | Classification |
|---|---|---|
| `1c97a66dcdc9e6d11a16e998a7fa8a92` | `per-alternative-anchor` | Same residual caret-boundary shape locked in #89 / P3 (`(?:^|…)(…)(?:$|…)`); compiler soundness, not id churn |

### `(***)` shared-prefix bucket (corpus-artifact)

Issue #86 labeled Anthropic key patterns with disclosure-style `(***)`
placeholders. They are **not** compiler rejects:

| regex_id prefix | Pattern shape | Encodable |
|---|---|---|
| `a6e8f5ff…` | `\b(sk-ant-admin01-…)(?:…\|$)` | yes (A1B) |
| `7659754f…` | `\b(sk-ant-api03-…)(?:…\|$)` | yes (A1B) |

Classify as **corpus-artifact / disclosure labeling**, not toolkit rejects.
Standalone match-time parsing of a redacted `(***)` token is out of scope.

## detect-secrets (full pin v1.5.0)

| Field | Value |
|---|---|
| Pin | `v1.5.0` / `01886c8a910c64595c47f186ca1ffc0b77fa5458` |
| Path | `batch/corpora/detect-secrets/plugins` (`python_dir` / `**/*.py`) |
| Fraction | **0.3725** (19/51) — `decision=go` (≥0.30) |
| Reasons | ok=19, composite-pattern=23, lookaround=7, per-alternative-anchor=2 |

Artifacts: `detect-secrets_encodable_fraction.json`,
`detect-secrets-inventory.ndjson`. Sample fallback:
`batch/corpora/detect-secrets/sample/` (Phase-5 mini pilot).

## trufflehog (pin v3.88.29 / `90190de`)

| Check | Result |
|---|---|
| Re-clone HEAD | `90190deac64289cb10bb694894be8db9ead8790b` |
| Fraction | **0.9302** (200/215) — stable vs P3 |
| `regex_id` set vs `trufflehog-frozen-ids.ndjson` | missing=0, extra=0 |

### Encodability flip (not extraction drift)

| regex_id | Pattern | Frozen | Now |
|---|---|---|---|
| `34ea8d912295a1980a82a1e8e93e8774` | `^[xX]+\|\*+$` | encodable | `per-alternative-anchor` |

Classification: **compiler soundness** from fix-wave #76 (reject-over-hoist
for per-alternative anchors). Same `regex_id` / site; extractor unchanged.
Not rule churn.

## Findings routing

No new facts-only security findings opened in this phase — fraction/drift
only. Disclosure policy for secret-detector rows remains `private_first`.
