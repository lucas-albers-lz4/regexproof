# P2 SAT impact triage

This dated overlay triages the six ground-truthed SAT questions in the frozen
20-r2 retrospective checkpoint v6. It preserves the proof and run artifacts;
it records only downstream product and disclosure decisions.

## Results

- **Six** questions remain in the SAT denominator.
- The two historical Doberman terminal-LF questions are false positives as
  security-bypass claims. `_is_root_or_home_target` strips surrounding
  whitespace before the Windows-root regex, and a `_DISK_WIPE` match feeds a
  fail-closed `BLOCK`. Their former `private_first` status and 2026-09-13
  `filed_at` values were internal disposition metadata; no upstream report was
  sent. The curated rows now say `false_positive` and retain the correction in
  their notes.
- Four questions remain plausible product-issue candidates, grouped into three
  issue families: Doberman Windows secret-store coverage, AutoAR cross-origin
  loopback fetching, and Malcontent third-party metadata in Markdown output.
- Confirmed security impact, external reports sent, maintainer confirmations,
  third-party fixes, and consumer-adopted gates remain **zero**.

The AutoAR loopback and Malcontent Markdown replays establish behavior in the
pinned implementation, with the limits described in their source calibration
READMEs. Doberman's Windows secret-path gate runs the exact pinned code on
Linux with Windows-shaped paths; native Windows behavior and a real secret
read were not exercised. The candidate rows are held private-first. No
third-party contact was made.

`triage.json` is the machine-readable join by exact `(site, question_id)`. The
curated disposition source is [`docs/conversion-upstream.jsonl`](../../../docs/conversion-upstream.jsonl).
The original v6 checkpoint remains an immutable pre-triage snapshot and still
shows the status that was current when it was built.

The repository question-history index was refreshed after the dispositions
changed. Its post-outcome snapshot has 176 sources, 75 asked sites, 129
reserved sites, and seven unbound legacy records; SHA-256 is
`92f1217d0c38e15510ee3f3531eb843dcfaa76529ac159fbd4fd8ef01a5de8d7`. This
index supports duplicate prevention and does not serve as allocation evidence.

## Pushback recorded

The prior Doberman dispositions treated regex-engine membership and
quoted-token preservation as evidence of a security-boundary bypass. Reading
the pinned callers disproves that inference: one caller strips the terminal
LF; both regexes are deny-list checks whose match blocks the command. Those
rows remain as measured SAT questions, but they are no longer counted as
security-bug candidates or reports.
