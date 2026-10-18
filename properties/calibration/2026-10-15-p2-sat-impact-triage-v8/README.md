# P2 SAT impact triage v8

This is a retrospective outcome overlay for the nine ground-truthed SAT
questions in the strict v8 checkpoint. The checkpoint remains the source of
the 25-question denominator and still records all nine SAT rows as pending
product triage.

## Results

- Nine SAT questions were ground-truthed.
- Two historical Doberman terminal-LF security-bypass claims are refuted by
  their pinned callers: preprocessing strips the LF and deny-list matches
  contribute to a blocking decision.
- Seven candidate questions remain across six issue families: one Doberman
  secret-path candidate, one AutoAR loopback-fetch candidate, two Malcontent
  Markdown-output candidates, two llm-honeypot helper candidates, and one
  Panther pre-commit path-policy mismatch candidate.
- Confirmed security impact, consumer-adopted gates, external reports,
  maintainer confirmations, and third-party fixes remain zero.

The Panther candidate has an inferred requirement: a separate slash-command
review policy excludes paths containing `secrets`, while the pre-commit helper
uses a different exclusion regex. The slash command is not invoked by the
pre-commit hook. Its synthetic `secrets.py` replay establishes a policy
mismatch under the adopted contract; it does not establish that a real secret
was present or sent to a Claude service.

The two llm-honeypot replays establish code-level behavior only. No actual
generated artifact or published repository data was inspected; no live Tor
service was exercised. Existing AutoAR, Malcontent, and Doberman limitations
are retained in the machine-readable groups in [`triage.json`](triage.json).

This overlay does not update the upstream disposition ledger. No third-party
contact or report was authorized or sent. The source checkpoint and current
disposition-ledger digests are bound in `triage.json`.
