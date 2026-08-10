# Security policy — disclosure for scanner findings

## Private-disclosure-first (security-tool corpora)

Findings against **secret scanners and similar security tools** (including
`gitleaks`, `detect-secrets`, and peers listed in
`regexproof.batch.disclose.SECURITY_TOOL_CORPORA`) are tagged
`disclosure=private_first`.

Do **not** open a public upstream issue or PR that publishes a novel detector
bypass / gap without a human approval signal. The batch pipeline writes a
**PR dry-run** artifact (`properties/generated/<corpus>-pr-dry-run.json`) and
asserts `would_open_public_upstream_issue=false` / `publish=false` unless an
explicit approval file is present (and even then only records intent — no
network publish).

Implementation: [`regexproof/batch/disclose.py`](regexproof/batch/disclose.py).
Reporting field contracts: [`docs/REPORTING.md`](docs/REPORTING.md).

## What this is not

- Not a CVE process for third-party product vulnerabilities found elsewhere.
- Not permission to commit live credentials. Fixture keywords (e.g. gitleaks
  detector test strings) were resolved in GitHub secret scanning as
  `used_in_tests` (API), and [`.github/secret_scanning.yml`](.github/secret_scanning.yml)
  narrowly `paths-ignore`s those fixture/pilot paths so they do not re-open
  as alerts. Witnesses in committed artifacts must stay redacted
  (`docs/REPORTING.md`).

## Reporting a concern about this repo

If you believe regexproof itself has shipped an unverified SAT witness or a
leak of a real secret, open a private report with the project maintainers
before filing a public issue.

## Auditing this repo's own security

This file covers **disclosure of findings against third-party scanners**. For
auditing regexproof itself — trust-boundary map, the controls that already
exist, settled decisions that should not be re-filed, and copy-paste sweeps —
see [`docs/SECURITY-AUDIT.md`](docs/SECURITY-AUDIT.md).
