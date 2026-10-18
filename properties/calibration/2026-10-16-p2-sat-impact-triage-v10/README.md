# P2 SAT impact triage v10

This is an outcome overlay for the twelve ground-truthed SAT questions in the strict v14 checkpoint. The checkpoint remains the denominator and records all twelve SAT rows as pending product triage.

## Results

- Twelve SAT questions were ground-truthed.
- Two historical Doberman terminal-LF security-bypass claims are refuted by their pinned callers: preprocessing strips the LF and deny-list matches contribute to a blocking decision.
- Ten candidate questions remain across eight issue families. The Inhale file and directory output-path questions are grouped as one issue family.
- Confirmed security impact, consumer-adopted gates, external reports, maintainer confirmations, and third-party fixes remain zero.

The Inhale exact-pin replays reproduce writes outside the documented `-o OUTDIR` for two concrete operator-supplied URL inputs. The synthetic response bytes remained inside temporary fixtures. The source evidence does not establish that an untrusted party controls `-u`, `-l`, or `-r` in a supported deployment, or that files outside the selected output directory affect another security boundary. No report was sent.

A separate crawl-scope exploration reproduces a cross-origin fetch when an absolute `href` shares the root URL text prefix. That item remains unresolved and outside the SAT denominator because the repository does not state an independent same-origin requirement.

The new Tracecat item reproduces a mismatch between `validate_mcp_env_key` and the ASCII grammar declared in its comment and error text: CPython accepts one final line feed because the source pattern ends with `$`. The complete MCP stdio configuration validator accepts the witness and a local POSIX child receives the key. POSIX permits implementation-specific environment names; the evidence does not show harmful downstream behavior, a security boundary crossing, or security impact. Keep it as a policy-mismatch candidate until a supported product invariant and consequence are established.

The two llm-honeypot replays establish code-level behavior only. No actual generated artifact or published repository data was inspected; no live Tor service was exercised. Existing AutoAR, Malcontent, Doberman, and Panther limitations remain in the machine-readable groups in [`triage.json`](triage.json).

This overlay does not update the upstream disposition ledger. No third-party contact or report was authorized or sent. The source checkpoint and current disposition-ledger digests are bound in `triage.json`.
