# Track B — 40 triage-trial review (2026-08-13)

Not a re-gate. Skip already-Smith / already in `batch/corpora`. Keep only novel security-boundary surface.

## Skip (33)

Already have a `*_smith_decision.json` and/or `batch/corpora/<slug>/`. Includes the #240 Smith landings (ail-yara-rules, lonkero, gigachad-grc, bartblaze-yara-rules, serviceradar, octo-server, magic-js, crust, yara-rules, tracecat, everclaw-community-branches).

## Drop (2)

- **semgrep** (`semgrep/semgrep`, 597 sites) — duplicate of admitted `semgrep_rules`. Product tree, not a new rule pack.
- **panther-analysis** (`panther-labs/panther-analysis`, 57 sites, `security_boundary=unknown`) — no deterministic boundary; below a useful Smith bar.

## Keep for Smith (5)

All `escape_hatch` / `deterministic-true` except as noted. No `batch/corpora` dir yet.

| Corpus | Sites | Surface | URL |
|---|---|---|---|
| llm-honeypot-intelligence | 617 | yara 559 + py_re/posix-shell/pcre | https://github.com/Leviticus-Triage/llm-honeypot-intelligence |
| inhale | 375 | yara 372 | https://github.com/netspooky/inhale |
| Doberman-Core | 108 | py_re 108 | https://github.com/fu351/Doberman-Core |
| devguard | 50 | re2 47 | https://github.com/l3montree-dev/devguard |

Smith as separate PRs from new-funnel GOs. Luna + Bugbot + verify CI before merge.

## Smith measure (this wave)

| Corpus | Fraction | Smith |
|---|---|---|
| inhale | 306/372 = 0.8226 | GO, WAVE |
| llm-honeypot-intelligence | 68/68 = 1.0000 (live `rules/yara` only) | GO, WAVE |
| Doberman-Core | 40/69 = 0.5797 | GO, WAVE |
| devguard | 9/9 = 1.0000 | GO, WAVE |
| titus | 15/57 = 0.2632 | **NO-GO** (below 0.30). Manifest kept; not in WAVE_CORPORA. |
