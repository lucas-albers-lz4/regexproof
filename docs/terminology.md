# Corpus pipeline terminology

Use these terms when talking about discovering and admitting regex corpora.
Avoid calling probe/gate/Smith steps “mining jobs” — **mine** is only the
search + ledger/queue step.

## Cheat sheet

| Step | Term | What it means | Primary artifact / command |
|---|---|---|---|
| 1 | **Mine** | GitHub Code Search → admit up to the day cap into the ledger; park overflow in the queue | GHA `daily-mine.yml`, `scripts/mine-corpus-candidates.py` → `candidate-ledger.json`, `mine-queue.json` |
| 1b | **Queue drain** | Move queued candidates into the ledger on later UTC days (or a high-cap flush), ordered by **score-v1** | Same mine job with `DAILY_MINE_CAP`; flush via `gh workflow run daily-mine.yml -f daily_mine_cap=80` |
| 2 | **Rank** | Score ledger rows and print the next batch to hand-probe (no network, no writes) | `python scripts/rank-mine-candidates.py --limit 10` (gated rows skipped by default; `--no-skip-gated` to include them) |
| 3 | **Probe** | Clone a pinned repo and walk it for regex sites / dialects / boundary signals; emit an admission draft | `python scripts/probe-corpus-admission.py <url> --pin <sha>` |
| 4 | **Gate** (author-gate) | Human or auto decision: GO / NO-GO / triage on the probe draft | `*_gate_decision.json` under `properties/generated/`; `scripts/author-gate-decision.py` |
| 5 | **Smith** | After GO: extract → compile → encodable-fraction / tickets / allowlists | Smith scripts and `feat(smith): …` PRs |

Related ops terms (not numbered steps):

| Term | Meaning |
|---|---|
| **Ledger** | `properties/generated/candidate-ledger.json` — admitted candidates (`status=mined` until later workflow advances them) |
| **Queue** | `properties/generated/mine-queue.json` — overflow waiting for drain (cap 100; when full, a newcomer replaces the lowest-scored item only if it outscores it, max 10 replacements/run, logged) |
| **score-v1** | Deterministic metadata score used for admit/drain and rank (boundary heuristic, query family, stars, recency, capped penalty) |
| **Day cap** | `DAILY_MINE_CAP` (default 10) — max new ledger admits per UTC mine day |
| **Capped** | Search or admit hit a budget; expected on rich days, not a job failure |

## Longer explanations

### Mine

**Mine** is the automated discovery job. It runs Code Search with `PROJECT_PAT`,
applies exclusions, scores hits with score-v1, writes up to the day cap into the
**ledger**, and parks the rest in the **queue**. When the queue is already full
(100), the queue replaces the lowest-scored item when a newcomer outscores it (bounded, logged) — that is congestion, not a crashed job. A
healthy schedule run may still report `capped: true` and `accepted: 10`.

Do not use “mine” for local clone/walk work; that is **probe**.

### Queue drain

**Queue drain** is how parked overflow becomes ledger admits. The daily mine
job drains highest score-v1 first within the day cap. Waiting for cron is the
normal path; raising `daily_mine_cap` on `workflow_dispatch` is an intentional
**flush** when you want more ledger depth before probing.

### Rank

**Rank** only reads the ledger (and optionally skips URLs that already have a
`*_gate_decision.json`). It prints NDJSON lines with `url`, `pin`, `score`, and
breakdown — the shortlist for the next probe wave. It is instant and never
filters by cloning a repo. After a wave is gated, always prefer
gated rows are skipped by default; `--no-skip-gated` includes them when you want the already-decided batch again.

### Probe

**Probe** is the expensive local step: partial-clone at `--pin`, walk the tree,
run extractors, classify boundary signals, emit a flagged admission draft.
This is the step that burns CPU on fat trees (skip-dir prune + unread
non-extractor files help). Output is a draft for gating, not a final corpus
admit.

### Gate (author-gate)

**Gate** records the decision on a probed candidate: GO, NO-GO, or triage,
with rationale and evidence. Decisions live as
`properties/generated/<slug>_gate_decision.json`. Auto-NO-GO may apply for
some shapes; GO / triage usually need a human. Ledger rows can remain
`status=mined` even after a gate file exists — use gate files (and
`rank` (gated rows skipped by default) as the operator source of truth for “already decided.”

### Smith

**Smith** is post-GO corpus work: inventory extract, dialect compile, encodable
fraction, allowlists, and follow-on PRs/tickets. Mine does **not** auto-file
Smith issues. Only gate GO (or an explicit triage path you choose) should
start Smith effort.

## Suggested phrasing

| Prefer | Avoid |
|---|---|
| “Drain the mine queue” / “flush with `daily_mine_cap=80`” | “Run mining jobs to process the queue” (ambiguous with probe) |
| “Rank the ungated ledger batch” | “Filter prospects” (unclear whether rank or probe) |
| “Probe this URL at pin …” | “Mine this repo locally” |
| “Gate decision for …” | “Approve the mine” |
| “Smith extract/compile for …” | “Mining compile step” |
