# Malcontent Git submodule CR calibration, 20-r2

This is a one-question, exact-pin calibration for
`chainguard-dev/malcontent@ea3e83e24676a1678a9522141da29b636c9451ab`.
The frozen 20-r2 manifest digest is
`5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
The source rule is `rules/impact/exploit/cve-2025-48384.yara`, SHA-256
`b6d017494cd9ecc7a9843832229fa45789c7edc06ccba093c0381d151a2a2552`.

## Existing corpus evidence

This slice did not require another bulk ingest. The pinned GO artifact already
records 19,578 probe sites (15 RE2 and 19,563 YARA, including the admitted
third-party corpus). The completed batch run over the product's own `rules/`
inventory records 7,922 extracted entries, 5,540 encodable entries, and 2,382
triage entries in 28.804 seconds. See
[`malcontent_gate_decision.json`](../../generated/malcontent_gate_decision.json),
[`malcontent_batch_summary.json`](../../generated/malcontent_batch_summary.json),
and [`malcontent_encodable_fraction.json`](../../generated/malcontent_encodable_fraction.json).

[`malcontent.ndjson`](../../generated/malcontent.ndjson) is a pre-fix snapshot
with five `usage_mismatch` scanner findings and four generic `planned` shape
questions. Those templates are not independently contracted product results
under the repo's property-contract precondition. Review of the five scanner
rows refuted three escaped-dollar false positives; the detector now checks
escape parity. The other two are intentional EOF anchors per the pinned rule
comments and remain behavior-only triage, not product findings. See
[`scanner-triage-review.json`](scanner-triage-review.json). The GO admission
artifact also records two unclassified parse-error rows and an escape-hatch
decision. Intake volume and compiler encodability therefore do not establish
product-proof yield; the next throughput work is source-backed contract
disposition and faithful gates.

## Contract and source review

The independent security context is Git's
[GHSA-vwqx-4fm8-6qc9 advisory](https://github.com/git/git/security/advisories/GHSA-vwqx-4fm8-6qc9)
and the pinned YARA rule's own explanation of the CVE. The property is scoped
to the terminal `[^\n]` class in `$path_embedded_cr`: after its required CR,
the next byte cannot be LF. The declared domain is one ASCII byte. It does not
claim a formal proof of the complete YARA rule.

The shortlist records every one of the rule's seven extracted regex sites.
One component contract was adopted under the standing autonomous-adoption
policy. The URL branch is a deferred sibling; anchored EOF branches remain
unresolved after exploratory Z3 queries returned `unknown`; trailing-CR
branches and `$bare_lf` remain behavior-only composition sites. This is a
rule-level vertical slice, not a ranked top-15 Malcontent sample or a 15/5
campaign wave. A source-text scan of explicit CVE metadata found only eight
inline regex declarations across two YARA files (seven in this CVE rule); this
is not a canonical AST inventory, but it shows that this one CVE idiom cannot
support a 15-site shortlist on its own. Expand to other justified product
idioms rather than padding this one with siblings.

## Proof and regression evidence

The P6 runner verified the clean exact-pin source checkout and frozen roster,
then completed one serial property attempt:

- `MC-malcontent-cve48384-embedded-cr-excludes-lf`: UNSAT in the declared
  ASCII-byte domain.
- `MC-malcontent-cve48384-mutated-embedded-cr-allows-lf`: SAT with LF as the
  witness; ground truth reproduced by weakening the pinned source class and
  scanning a benign CRLF fixture with YARA-X.
- Exact YARA-X CLI 1.19.0 binary SHA-256:
  `dd5e5c07a0397ad922b597b8d6c35c22485ec9fe4bf26f064d242045042cdca2`.
- The full-rule product gate compared 139 synthetic ASCII `.gitmodules`
  fixtures against the source-derived expectation: 8 line-ending matrix cases,
  3 boundary cases, and 128 seeded cases; 58 expected matches, 81 expected
  nonmatches, and 0 mismatches.
- The P6 state is `complete`; the per-question gate records exact source-pin
  verification, mutation coverage, full-rule product replay, and 139 cases.

The serial wave artifacts are in [`p6-wave/`](p6-wave/):
`state.json`, `attempts.json`, `conversion.ndjson`, and `checkpoint.json`.
The gate report from that wave is [`p6-gate-report.json`](p6-gate-report.json).
The gate's complete fixture list and post-wave replay are in
[`post-wave-gate-report.json`](post-wave-gate-report.json). The original
standalone calibration run is retained as [`gate-report.json`](gate-report.json).
The run's proof/gate and outcome counts are appended to
[`../../generated/autonomous_work.jsonl`](../../generated/autonomous_work.jsonl).
Review and contract adoption occurred before the timed runner interval and are
not included in that row's review/adoption throughput counts.

The P4 scheduler selected `malcontent/git-crlf-smuggling` at the matching GO
pin; the frozen output is [`scheduler-selection.json`](scheduler-selection.json).
The registration limits the slice to one candidate.

## Limits and next work

The fixtures are synthetic examples derived from the pinned rule comments; no
vulnerable Git command or exploit repository was run. The 128 generated cases
are a regression sample, not an exhaustive proof over repository files. No
YARA wide-string behavior is claimed. The standalone anchored-search Z3 probes
that returned `unknown` remain unresolved and are not counted as passes.

This run found no SAT product candidate, reachable violation, or confirmed
security impact. It sent no third-party report and received no maintainer
confirmation or fix. It did produce one contract-backed UNSAT guarantee and
one runnable local gate with a passing real-engine mutation check. Next, P2/P3
still need a campaign-level coverage/attempt roster and prospective serial
wave. Reuse the existing Mycelium 15-candidate review instead of repeating
it; this Malcontent seven-site rule slice cannot fill that shortlist. P6 still
needs queue/admission lifecycle composition; P7 still needs its first
prospective campaign wave and 50-question checkpoint or a documented coverage
limit.
