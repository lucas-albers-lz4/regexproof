# Mycelium 20-r2 release checksum preflight

**Status:** exact-pin contract, pre-outcome roster, proof, replay, mutation,
and local regression gate pass. This is a one-question cohort calibration,
not a completed P7 conversion wave.

## Source inventory and review

The checkout is the frozen 20-r2 pin
`d4f01ba6202d50909d1977810d322259482e0b82`. The scripts-slice inventory
contains 28 extracted sites; 23 are encodable under the current local
compiler. The literal extracted patterns are preserved in `inventory.ndjson`;
compiler encodability is carried separately. This matters for two `sed` BREs
in the systemd drift drill, whose normalized compiler form differs from the
source syntax.

The ranked shortlist reviewed 15 sites: one selected at rank 11, two
unresolved systemd-output captures, and 12 skipped status/normalization or
diagnostic sites. The adopted candidate is
`scripts/verify-release.sh:60`, which counts well-formed SHA256 records before
calling the checksum command. The pinned helper and its README, QUICKSTART,
and release documentation describe empty, truncated, and HTTP 200 HTML
responses and state that integrity-only mode does not establish authenticity.

## Contract and frozen roster

The contract covers one ASCII LF-delimited checksum/error line, excluding
NUL. The solver question is whether any line of length 0–63 matches the
64-hex preflight. It does not model authenticity or the platform checksum
utility.

The contract was adopted under `autonomous-contracts-v1`. Before solver
execution, `freeze-product-roster.py` produced a one-identity roster bound to
the 20-r2 manifest digest `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
The roster coverage digest is
`98dc95c108a34f7790a3aedb82ef076e1fb16da351d828df80b8a8bd5e6cef96`.

After that proof run, the P6 runner's source validator showed that the
descriptive site suffix `SHA256SUMS preflight` was not a literal on source
line 60. I revised only the site anchor to `sums_n`; guarantee, input, trust,
domain, provenance, source pin, and source-file digest are unchanged. The
result-independent revision record is `contract-revision-1.json`. The
original contract and pre-outcome roster remain as `contract-v1.json` and
`roster.json`. `roster-v2.json` (coverage digest
`235e77364ea380931cce5c133ec6813045e0dca013013b44a91b9d008d41dc35`) is the
runner-compatible identity after proof, so it is used only for P6 input
validation, not as prospective-yield evidence.

## Gate evidence

Run with:

```sh
.venv/bin/python scripts/mycelium-release-preflight-regression-gate.py \
  --source-pin d4f01ba6202d50909d1977810d322259482e0b82 \
  --source-root /path/to/clean/mycelium-d4f-checkout
```

At the exact d4f pin, Z3 reports the short-line property UNSAT. Weakening the
64-hex requirement is SAT for witness `\x0b\x04`; the callback replays the
changed behavior against the pinned Bash helper with real grep and a lenient
checksum-command fixture. Empty and longer checksum-free inputs fail before
that command, and a valid record reaches the fixture. The source-pattern
mirror agreed with real grep on 3,814 inputs. The gate is also wired into CI.

P6 dry-run with `roster-v2.json`, `gate.json`, and the clean d4f checkout
verified the exact source pin/bytes and gate coverage. The following actual
runner invocation then completed as wave
`mycelium-release-preflight-20r2-p6-r1`: one UNSAT property, both registered
mutation guards passed, the 3,814-case Bash/product gate passed, and the exact
source and contract digests verified. The complete checkpoint is
[`p6-wave-r1/checkpoint.json`](p6-wave-r1/checkpoint.json).

This is a second execution of the same checksum-preflight question already
recorded by the earlier gate-only run below. It validates the bounded P6 runner
on the frozen 20-r2 source, but contributes no new question identity to P7.

## Campaign boundary and outcomes

The current Mycelium admission decision is `go` at newer pin
`4b53dc7629ca3bc88bf5467db481ad2af7130711`. The registrar bound
`scripts-bootstrap` to that current pin, so the scheduler will not select that
registration for d4f. This exact-pin proof is valid frozen-cohort evidence,
but the d4f bucket is not registered and this run is not a P7 wave. Resolve
the pin-specific admission/registration path before using it as campaign
throughput.

I also ran `probe-corpus-admission.py` against the exact d4f checkout. Its
draft records 1,034 regex sites (1,023 POSIX shell, 11 RE2), zero extractor
errors, and a deterministic-true boundary classification; see
`admission-probe-d4f.json`. It is probe evidence only: the draft leaves the
decision and condition dispositions open, and no d4f GO decision was authored.
The scheduler's current GO decision still selects the 4b53 registration.

The source bytes for `verify-release.sh` are identical at d4f and 4b53, so
these two pin-bound runs exercise the same site and guarantee. Do not report
them as two distinct product questions without deduplicating that lineage.

Both Mycelium runs are recorded separately in
`properties/generated/autonomous_work.jsonl` under the frozen 20-r2 cohort.
The original gate-only row records 11.877 seconds; the P6 row records 12.1304
seconds of summed runner phases, including 1.5 ms solver, 58 ms mutation
checks, 11.8 ms source verification, and 12.0591 s product gate. The P6 row is
marked as a repeated execution of the same question identity, not new yield.
Review/adoption effort, human active time, tokens, and cost remain unmeasured.

The current cohort-filtered scorecard has six proof attempts, five decided
attempts (all UNSAT), seven local gates, eight passing mutation checks, and
215,761 differential cases. The attempts represent four distinct question
identities because both the Mycelium and AutoAR questions have repeated runs;
one AutoAR attempt remains undecided after an emitter integration error. The
bug-discovery track and external report/confirmation/fix track each have zero
outcomes. `reviewed_sites=0` and `contracts_adopted=0` describe timed runner
intervals, not the larger review/adoption work. End-to-end contract throughput
is still unmeasured.
