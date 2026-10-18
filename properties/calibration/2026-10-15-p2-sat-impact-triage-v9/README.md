# P2 SAT impact triage v9

This is an outcome overlay for the eleven ground-truthed SAT questions in the strict v9 checkpoint. The checkpoint remains the denominator and records all eleven SAT rows as pending product triage.

## Results

- Eleven SAT questions were ground-truthed.
- Two historical Doberman terminal-LF security-bypass claims are refuted by their pinned callers: preprocessing strips the LF and deny-list matches contribute to a blocking decision.
- Nine candidate questions remain across seven issue families. The Inhale file and directory output-path questions are grouped as one issue family.
- Confirmed security impact, consumer-adopted gates, external reports, maintainer confirmations, and third-party fixes remain zero.

The Inhale exact-pin replays reproduce writes outside the documented `-o OUTDIR` for two concrete operator-supplied URL inputs. The synthetic response bytes remained inside temporary fixtures. The source evidence does not establish that an untrusted party controls `-u`, `-l`, or `-r` in a supported deployment, or that files outside the selected output directory affect another security boundary. No report was sent.

A separate crawl-scope exploration reproduces a cross-origin fetch when an absolute `href` shares the root URL text prefix. That item remains unresolved and outside the SAT denominator because the repository does not state an independent same-origin requirement.

The two llm-honeypot replays establish code-level behavior only. No actual generated artifact or published repository data was inspected; no live Tor service was exercised. Existing AutoAR, Malcontent, Doberman, and Panther limitations remain in the machine-readable groups in [`triage.json`](triage.json).

This overlay does not update the upstream disposition ledger. No third-party contact or report was authorized or sent. The source checkpoint and current disposition-ledger digests are bound in `triage.json`.
