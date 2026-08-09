# Daily mine setup (#147)

Scheduled GitHub Actions job that runs
[`scripts/mine-corpus-candidates.py`](../scripts/mine-corpus-candidates.py),
then commit-backs
[`properties/generated/candidate-ledger.json`](../properties/generated/candidate-ledger.json)
and [`properties/generated/mine-queue.json`](../properties/generated/mine-queue.json)
to `main`. Pattern matches sre-ai-llm-work `daily-scan.yml` (one scanner, no
issue filing).

**Status (2026-08-09):** live. First `workflow_dispatch` succeeded with
`PROJECT_PAT` set — [run 31339610109](https://github.com/lucas-albers-lz4/regexproof/actions/runs/31339610109)
committed `chore(mine): daily candidate ledger + queue` (`4d1e17e`): **10**
ledger admits (day cap), **queue depth 100** (full), **`run.capped: true`**.

## Secret: `PROJECT_PAT`

This is a **GitHub classic Personal Access Token**, not an LLM/API key.

1. GitHub → Settings → Developer settings → Personal access tokens →
   **Tokens (classic)** → Generate new token.
2. Scopes for this job: **`repo`** (contents read/write + Code Search auth).
   You do **not** need `project` (unlike sre-ai-llm-work, which files issues /
   Projects).
3. Repo → Settings → Secrets and variables → Actions → New repository secret
   named exactly **`PROJECT_PAT`**.
4. The workflow **fail-closes** if the secret is missing. Code Search uses
   `GITHUB_TOKEN=${{ secrets.PROJECT_PAT }}` — no Actions default-token fallback.

Fine-grained tokens can work if they grant contents R/W on this repo and Code
Search; classic + `repo` is the low-friction path.

## Branch protection

Ledger commits push as `regexproof-bot` using `PROJECT_PAT`. If `main` requires
reviews or status checks, ensure the PAT account can push those commits (admin
bypass or an allowlisted bot), same as the sister-repo scanner. First-run
commit-back already proved the push path on this repo.

## Manual run / queue flush

```bash
# Default cap (10)
gh workflow run daily-mine.yml

# Flush overflow queue with a higher day cap
gh workflow run daily-mine.yml -f daily_mine_cap=80

gh run watch
```

Schedule: `12 12 * * *` (12:12 UTC). Concurrency group `daily-mine` serializes
runs (`cancel-in-progress: false`).

### What a healthy run looks like

- Job steps all green; “Fail job on mine soft failure” skipped.
- Step summary shows accepted / ledger / queue / capped.
- If ledger or queue changed: a bot commit
  `chore(mine): daily candidate ledger + queue` on `main`.
- Day cap filled + overflow queued is **normal**, not a failure. With default
  `DAILY_MINE_CAP=10`, a rich search day will fill the ledger slice and park
  the rest in `mine-queue.json` (cap 100). Cron drains FIFO on later UTC days;
  use `daily_mine_cap=80` to flush faster.

## Local dry-run

```bash
export GITHUB_TOKEN=ghp_...   # same PAT as PROJECT_PAT
python scripts/mine-corpus-candidates.py --dry-run
```

Stdout ends with a `{"kind": "mine_run_summary", ...}` line. Dry-run does not
write the ledger/queue.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Job fails immediately: `PROJECT_PAT secret is required` | Secret unset | Add `PROJECT_PAT` |
| Mine exit 2 / auth failure | Bad/expired PAT or missing search scope | Rotate classic PAT with `repo`; confirm Code Search works with the token |
| Mine exit 1, empty accept | Search errors, no hits after exclusions | Read step logs; try `--dry-run` locally |
| `run.capped: true` / summary `capped: true` | Query budget or ~1000-result search cap | Expected; next day or raise `daily_mine_cap` on dispatch |
| Accepted 0 but queue growing | Day cap already filled (`DAILY_MINE_CAP`) | Wait for UTC day roll or dispatch with higher cap |
| Queue at 100 / “mine-queue full” warnings | Overflow cap hit | Raise `daily_mine_cap` temporarily or wait for daily drain |
| Rebase/push conflict on commit-back | Concurrent human push to ledger files | Re-run workflow; concurrency prevents two mine jobs overlapping |

## Non-goals (this job)

Score-and-sort (#148), Smith extract/compile (#149), and native Java dialect
(#150) are follow-ons. This job only discovers and persists candidates.
