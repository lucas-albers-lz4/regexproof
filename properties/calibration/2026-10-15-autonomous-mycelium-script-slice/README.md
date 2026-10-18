# Mycelium release checksum preflight calibration

**Status:** source-pinned contract and local gate pass; separate from the
autonomous 20-r2 campaign.

## Pin and cohort boundary

This slice uses Mycelium `4b53dc7629ca3bc88bf5467db481ad2af7130711`, the pin
in the current Mycelium `gated:go` decision. The 20-r2 manifest pins the same
repository at `d4f01ba6202d50909d1977810d322259482e0b82`. The cohort roster
freezer rejected the current contract because those pins differ. No 20-r2
roster entry, campaign question, or P7 yield is claimed here.

## Review and contract

The current-pin inventory shortlist reviewed 15 ranked `scripts/` sites: one
selected contract, two unresolved systemd-output parsers, and 12 skipped sites.
The rank-16 site was not reviewed. The adopted contract covers the release
helper's `SHA256SUMS` preflight at line 60. Repository docs describe empty or
truncated responses, including HTTP 200 proxy or captive-portal content, and
explain that integrity-only mode does not establish authenticity.

The full top-15 review is now bound to source in
[`review-evidence.json`](review-evidence.json). It contains a 51-line window
for every reviewed site, exact source-file hashes at the pin above, and hashes
for the review, shortlist, and run-context inputs. The explicit
`batch/corpora/mycelium/rules/` prefix maps the shortlist's corpus-overlay paths
to paths in the upstream checkout; both forms of each site are retained in the
artifact. Its SHA-256 is
`7414a3cb6e36df6fcb1510b439e130dc82d44b61af2c9d3a99d149c4688b76f8`.

The initial source-bound review confirms one adopted candidate, twelve
explicit skips, and two unresolved candidates (ranks 1 and 4). Its original
evidence remains frozen at SHA-256
`7414a3cb6e36df6fcb1510b439e130dc82d44b61af2c9d3a99d149c4688b76f8`.
The follow-up review is in [`review-v2.ndjson`](review-v2.ndjson), with a new
source-bound top-15 record in [`review-evidence-v2.json`](review-evidence-v2.json)
(SHA-256
`6faf430bc5411749dd0cf1b402e0f778c961406187b61531de6a7bf6d1a43923`). Rank 1
is now adopted for a narrow diagnostic-preservation guarantee; rank 4 is
skipped as a duplicate symptom. The updated top-15 has two adopted candidates
and thirteen explicit skips.
The revised NDJSON review digest is
`3e149afff6e7e96914ff9d74e80d475518d40b3ee7747dbee9d0a4131bd731df`.

The unresolved serialization question was settled for systemd 255.4. A
harmless transient user unit produced the raw `systemctl show` output in
[`systemd-execstart-semicolon-replay.json`](systemd-execstart-semicolon-replay.json)
(SHA-256
`3851dfac4e512a086bfc8f36b4d9f62c7a2dcd573aa70d625e19e7385279cd46`). The
literal semicolon in an argv path was not escaped. The pinned `[^;]*` capture
stopped inside that path, dropped the later `--insecure-no-verify` flag, and
left the downstream repo-ref capture empty. Mycelium's pinned
`_insecure_bypass_permitted` guard refuses that flag under systemd and when
stdin is not a TTY, so this replay establishes a reachable diagnostic defect,
not unsigned root execution or a confirmed security-boundary violation.

The contract is in
[`contract-execstart-diagnostic.json`](contract-execstart-diagnostic.json)
(whole-file SHA-256
`c0760a7faa9dba2659f1d9ccf8abf3f758443938f3f576395242bd37829281d6`; the
adoption-bound contract digest is
`16113f8c1d77c200771d0e484fd20bc7efeb3288a21df31caf53da5c465bd586`). Its
local counterexample/replay gate is
[`mycelium-execstart-diagnostic-reproduction-gate.py`](../../../scripts/mycelium-execstart-diagnostic-reproduction-gate.py).
The gate produced a ground-truthed SAT witness and a passing parser mutation
check (2/2 solver records, 0.366 seconds measured gate time). The corresponding
autonomous-work row records one replayed reachable diagnostic defect, zero
confirmed security impact, one local evidence gate, and zero external reports,
confirmations, or fixes. Contract review/adoption time and human active time
were not measured. The run is off-cohort and is excluded from the 20-r2 and P7
question-yield totals.

The cumulative off-cohort scorecard is
[`autonomous-scorecard.json`](autonomous-scorecard.json) (SHA-256
`8dd4f0d7f4ffc547b34f40f9506ffd0884a24d29b9f0af1f575cbcbe464dd886`). Across
the two recorded gate-only runs it reports two decided questions (one UNSAT,
one SAT with replay), two local gates, two passing mutation checks, and 3,814
differential cases. The bug track has one reachable diagnostic defect and zero
confirmed security impact; the external track has zero reports, confirmations,
or fixes. The scorecard's contract-adoption count is zero because adoption was
outside both timed gate intervals. Combined measured agent execution is
11.929 seconds wall-clock plus 0.366 seconds phase-sum; human time, tokens, and
cost remain unmeasured.

The `conversion-queue-transition.py` CLI supports source-snapshot claims,
contract transitions, and evidence-noted skips under the shared corpus event
lock. An isolated active-wave replay then exercised 17 real CLI transitions
over this source-bound top-15: the two adopted contracts were claimed and
contracted, all thirteen skips were recorded, and the wave closed at generation
1. The replay artifact is
[`queue-transition-replay.json`](queue-transition-replay.json). It used a
temporary queue directory and event log; the repository campaign queue and
event log were not changed. This closes P3's local transition-workflow
validation, while campaign integration and P7 cohort yield remain open. Its
artifact SHA-256 is
`421a64890a5b0a8566de96021c1a560dcaf08fa79bb040d61eafa492c1bcb6fb`; all 15
review rows were joined to the matching source-bound evidence before recording
the transition result.

The contract asks whether an ASCII checksum line shorter than 64 characters
can pass the preflight. Its solver domain is one LF-delimited line of length
0–63, excluding NUL. The guarantee is limited to checksum-record preflight;
it does not prove the checksum source is authentic or model a platform's
checksum utility.

## Gate evidence

`scripts/mycelium-release-preflight-regression-gate.py` passed at the exact
source pin with Z3 5.0.0. The short-line property is UNSAT. Weakening the
64-hex requirement is SAT for witness `\x0b\x04`, and the callback reproduced
the changed behavior by running the pinned Bash helper with real `grep` and a
lenient checksum-command fixture. Empty and longer checksum-free inputs fail
before that command; a well-formed record reaches the fixture. The source
pattern mirror agreed with real grep on 3,814 differential inputs.

P4 registration now admits `mycelium/scripts-bootstrap` at this exact pin,
and the scheduler selected it as `named-next-unused`. The registrar also
handles repository-qualified `contract.site` values without treating the
identity prefix as a checkout path. The scheduler reports `active-wave` and
withholds selection when the corpus lock has an open wave. Focused registry
and scheduler coverage passed: 38 tests.

This is a local calibration and useful regression gate. It is not evidence of
a current product bug, reachable impact, upstream adoption, report, maintainer
confirmation, fix, or 20-r2 campaign throughput. The two unresolved
systemd-output sites remain outside this contract.

The gate-only run is recorded as
`mycelium-release-preflight-gate-offcohort-20261015-r1` in
`properties/generated/autonomous_work.jsonl`, under cohort ID
`off-cohort-mycelium-current-pin`. Measured gate execution was 11.929 seconds:
one attempted and decided UNSAT question, one local gate, one passing mutation
check, and 3,814 differential cases. The bug-discovery track and external
report/confirmation/fix track each have zero outcomes. Contract review and
adoption time, human active time, token use, and cost are not included in this
gate-only measurement; this row is excluded from 20-r2 question yield.
