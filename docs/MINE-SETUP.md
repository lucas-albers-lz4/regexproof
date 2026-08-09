# Daily mine setup (#147)

Scheduled GitHub Actions job that runs
[`scripts/mine-corpus-candidates.py`](../scripts/mine-corpus-candidates.py),
then commit-backs
[`properties/generated/candidate-ledger.json`](../properties/generated/candidate-ledger.json)
and [`properties/generated/mine-queue.json`](../properties/generated/mine-queue.json)
to `main`. Pattern matches sre-ai-llm-work `daily-scan.yml` (one scanner, no
issue filing).

## Secret: `PROJECT_PAT`

1. Create a classic PAT (or fine-grained token) with **`repo`** (contents read/write
   on this repository) and enough scope for **GitHub Code Search**.
2. Repo → Settings → Secrets and variables → Actions → New repository secret
   named exactly **`PROJECT_PAT`**.
3. The workflow **fail-closes** if the secret is missing. Code Search uses
   `GITHUB_TOKEN=${{ secrets.PROJECT_PAT }}` — no Actions default-token fallback.

## Branch protection

Ledger commits push as `regexproof-bot` using `PROJECT_PAT`. If `main` requires
reviews or status checks, ensure the PAT account can push those commits (admin
bypass or an allowlisted bot), same as the sister-repo scanner.

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

## Local dry-run

```bash
export GITHUB_TOKEN=ghp_...   # same PAT
python scripts/mine-corpus-candidates.py --dry-run
```

Stdout ends with a `{"kind": "mine_run_summary", ...}` line. Dry-run does not
write the ledger/queue.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Job fails immediately: `PROJECT_PAT secret is required` | Secret unset | Add `PROJECT_PAT` |
| Mine exit 2 / auth failure | Bad/expired PAT or missing search scope | Rotate PAT; confirm Code Search works with the token |
| Mine exit 1, empty accept | Search errors, no hits after exclusions | Read step logs; try `--dry-run` locally |
| `run.capped: true` / summary `capped: true` | Query budget or ~1000-result search cap | Expected; next day or raise `daily_mine_cap` on dispatch |
| Accepted 0 but queue growing | Day cap already filled (`DAILY_MINE_CAP`) | Wait for UTC day roll or dispatch with higher cap |
| Rebase/push conflict on commit-back | Concurrent human push to ledger files | Re-run workflow; concurrency prevents two mine jobs overlapping |

## Non-goals (this job)

Score-and-sort, Smith extract/compile, auto-GO, and native Java dialect are
tracked separately (#148–#150).
