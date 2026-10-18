# P2 SAT impact triage v11

This outcome overlay joins the 14 ground-truthed SAT questions in the v22
retrospective checkpoint. The v22 checkpoint remains immutable and still shows
its original `pending_product_triage` states. The separate overlays now cover
all 14 questions: v10 reviewed the first 12; this update adds the two Aidevops
pre-dispatch findings.

## Results

- Two historical Doberman terminal-LF claims remain refuted as security
  bypasses by their pinned callers.
- Ten prior candidate questions remain across eight issue families.
- The two new Aidevops witnesses reproduce local workflow behavior:
  - `cited_file=../oracle.txt` makes the exact helper count a 37-line fixture
    outside its mock clone, then close the issue as premise-falsified. The
    replay does not read file contents or establish public disclosure.
  - `threshold=08` triggers Bash's invalid-octal comparison behavior. For a
    five-line fixture the helper follows the premise-holds/return-0 path and
    logs that dispatch proceeds; the decimal `threshold=8` control returns 10.
- The two Aidevops questions are retained as separate local product candidates
  pending evidence about supported dispatch, permissions, and downstream
  effects. Their security impact is not confirmed.
- Across the 14 SAT questions, the overlay records 12 potential product issues
  in ten groups and two refuted security-bypass claims. Confirmed security
  impacts, consumer-adopted gates, reports, maintainer confirmations, and fixes
  remain zero.

This changes no entry in `docs/conversion-upstream.jsonl` and sends no external
report. The exact-pin checkpoint and disposition-ledger digests are bound in
[`triage.json`](triage.json). The original evidence is in the
[Aidevops 15/5 wave](../2026-10-16-autonomous-aidevops-predispatch-github-text-20r2/README.md)
and [residual census](../2026-10-16-autonomous-aidevops-predispatch-github-text-residual-20r2/README.md).
