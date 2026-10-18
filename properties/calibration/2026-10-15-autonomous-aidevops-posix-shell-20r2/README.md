# Aidevops POSIX shell contract reuse at the frozen 20-r2 pin

**Status:** source-bound contract revisions, five-property P6 runner wave, and
BusyBox product replay pass. This is reuse of historical work, not new P7
yield.

## Source and prior work

The checkout is `marcusquinn/aidevops` at
`8666b6c6c52472b5535aa295f2df593918152cb1`, a member of the frozen
`2026-09-12-calibration-20-r2` cohort (manifest digest
`5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`). The
source-bound sites are:

| Question | Pinned source site | Property shape |
|---|---|---|
| `AI-aidevops-brief-tid-no-semicolon` | `.agents/hooks/brief-filename-guard.sh:84` | Shape 1, one-character alphabet |
| `AI-aidevops-brief-tid-capture` | `.agents/hooks/brief-filename-guard.sh:105` | Shape 3, bounded capture identity |
| `AI-aidevops-cred-ident-no-semicolon` | `.agents/hooks/credential-emission-pre-push.sh:103` | Shape 1, one-character alphabet |
| `AI-aidevops-scope-heading-no-semicolon` | `.agents/hooks/scope-guard-pre-push.sh:137` | Shape 1, one-character alphabet |
| `AI-aidevops-gh-issue-digit-capture` | `.agents/hooks/task-id-collision-guard.sh:378` | Shape 3, bounded capture identity |

These are the same five questions in the historical
[Aidevops conversion close-out](../../generated/aidevops_conversion_wave.md):
15 sites were reviewed and five contracts were asked (three shape 1, two
shape 3). That close-out already records five expected-UNSAT results and the
family mutation guard. The current calibration created adopted source-bound
contract revisions and a frozen five-identity runner roster without changing
the historical harness contracts or their guarantee, input, trust, or domain.
It does not claim another five reviews or five novel proof questions.

The scope-heading site's descriptive suffix is `Files`. The earlier suffix
`Files[[:space:]]+Scope` contains colons inside the POSIX character class, but
the source-site format reserves colons to delimit repository, path, line, and
symbol. The corrected suffix is a literal token on the same pinned line. The
contract semantics and source bytes did not change.

## P6 result

The bounded runner completed wave `aidevops-posix-shell-20r2-p6-r1`:

- The frozen cohort, five-contract roster, adoption digests, clean checkout,
  and exact source bytes verified.
- All five properties were UNSAT over their declared domains. The two capture
  properties are bounded to their listed lengths; the three alphabet proofs
  are length-independent single-character questions.
- `AI-aidevops-mutated-brief-tid-semicolon` returned SAT for `;`, and its real
  product replay reproduced the weakened behavior.
- The BusyBox product gate passed 70 cases: 32 brief task-ID captures, 32
  issue-number captures, and two cases for each of the three alphabet sites.
- The gate checks BusyBox upstream version `1.36.1` and fails closed on
  version drift. The locally measured build was
  `BusyBox v1.36.1 (Ubuntu 1:1.36.1-6ubuntu3.1) multi-call binary.` CI invokes
  the same version guard in the Aidevops BusyBox replay step.

The runner measured 2.8141 s in solver calls, 0.2791 s in the product gate,
0.0018 s in mutation guards, and 0.0331 s in source checks (3.1281 s phase
sum). The autonomous-work row records five attempted and decided UNSAT
properties, one local gate, one mutation check, and 70 differential cases.
Its `reviewed_sites` and `contracts_adopted` counters are zero because the
source review/adoption work happened before the measured P6 runner interval;
those end-to-end minutes are unknown. This avoids treating runner time as
contract authoring throughput.

The roster's coverage digest is
`d45208a4a83b70c89d4de135aa640de882f9a27d4514a565951f4d9b47f95341`.
The proof-wave records are [`checkpoint.json`](p6-wave-r1/checkpoint.json),
[`state.json`](p6-wave-r1/state.json), and
[`attempts.json`](p6-wave-r1/attempts.json). The adopted contracts, frozen
roster, gate definition, and override input are in this directory.

## Limits and next work

This run establishes source-bound proof and local product-gate execution for
the five historical properties. It does not prove an independent admission
decision, survey the Aidevops shell surface, exercise queue/admission
transitions, or create an upstream consumer gate. The corpus decision process
must still justify that these sites belong in the security-boundary product
sample. No SAT candidate, reachable violation, security impact, external
report, maintainer confirmation, or fix resulted. P2 coverage and P6 workflow
composition remain open, and the five historical questions must not be counted
as new P7 yield.
