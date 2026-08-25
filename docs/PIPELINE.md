# Operator pipeline

The proof harness (`scripts/z3-verify.py`) is the product. This page is the
**corpus funnel** an operator runs beside it: discover candidates, probe them,
gate them, then conversion-wave the GO set.

Entry status command (latest mine-day drain, queue pressure, 7-day survival,
backlog weeks):

```bash
python scripts/pipeline-status.py
python scripts/pipeline-status.py --weekly   # markdown for daily-mine
```

Terms match [`docs/terminology.md`](terminology.md).

## Flow

```
mine  →  rank  →  probe  →  gate  →  conversion wave
```

| Step | Command | Artifact |
|---|---|---|
| **Mine** | GHA [`daily-mine.yml`](../.github/workflows/daily-mine.yml) / `python scripts/mine-corpus-candidates.py` | ledger + queue (below) |
| **Rank** | `python scripts/rank-mine-candidates.py --limit 10` | stdout NDJSON (no writes) |
| **Probe** | `python -m regexproof.probe --single <url> --pin <sha>` or `--batch …` | staged draft under `properties/staged_probes/` (gitignored) |
| **Gate** | `python scripts/author-gate-decision.py` / Wave 5 auto-NO-GO | `properties/generated/*_gate_decision.json` |
| **Wave** | [`docs/CLUSTER-CONVERSION.md`](CLUSTER-CONVERSION.md) | `*_conversion.ndjson` + ledger hop table |

Legacy CLIs `scripts/probe-corpus-admission.py` (single) and
`scripts/batch-probe.py` (leased batch) still run; they point at
`python -m regexproof.probe`.

## Two stores

| Store | Path | Role |
|---|---|---|
| **Ledger** | [`properties/generated/candidate-ledger.json`](../properties/generated/candidate-ledger.json) | admitted candidates (`mined` until a later status) |
| **Queue** | [`properties/generated/mine-queue.json`](../properties/generated/mine-queue.json) | overflow waiting for the next UTC day (cap 100) |

The day admit cap is `DAILY_MINE_CAP` (default **10**). Query mix (Wave 10
feed share) does not raise that cap. Ops: [`docs/MINE-SETUP.md`](MINE-SETUP.md).

## Shared gate

A probe is not an admit. The stop signal is the committed gate decision
joined to the 7-day escape window (`regexproof.mine.escape_window`):
`go ∪ triage-trial` over probes **completed** in the window. Batch
`probe_success_rate` is a walk-outcome rate, not that survivor.

Staged drafts must not become contract material: `.gitignore` covers
`properties/staged_probes/`, and CI still runs
`scripts/ci-check-probe-walkers.py` (Wave 2 walker exclusion).

## Filing visibility

GT-confirmed conversion SATs without a curated row fail
`scripts/check-disposition-coverage.py`. To list items that are GT-confirmed
and not `wont_file`:

```bash
python scripts/check-disposition-coverage.py --ready-to-file
```
