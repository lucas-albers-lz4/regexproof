# #571 research snapshot

These are **diagnostic records**, not harness results or product proofs. The
owning [report](../../../docs/issue-571-feasibility-2026-10-18.md) defines the
scope and limitations. No script here is added as a CI proof gate.

## Reproduce

Use Linux, Python 3, Node and Git. Obtain clean fwlive source containing
`core/fwlive-log.js` with SHA-256
`52983d7c0a629de4ee23a13873e5ac54cf7d08dfaf03383614fceb59a4d1da12`
(e.g. commit `8a1228fa92572a05344004574ce088ac9b347864`). The runner executes
that trusted module; it is not a safe loader for arbitrary untrusted code.
The adjacent `issue571-diagnostic.js` is the unchanged 28-row diagnostic from
regexproof commit `2c1eb574f967cd5fd734a50016acdc25c29f52ec`, included so that
this snapshot does not depend on an unmerged branch or local checkout state.

Download the desired release binary and verify its hash **before execution**:

- v1.6.1: [Linux binary](https://github.com/VeriFIT/z3-noodler/releases/download/v1.6.1/z3-noodler-ubuntu-24.04-x86_64-shared), SHA-256 `22b19f123d3e7f54e10fdc46af3f91de23d89148c9a259eb072bc9e12f083464`.
- v1.8.0: [Linux binary](https://github.com/VeriFIT/z3-noodler/releases/download/v1.8.0/z3-noodler-linux-x86_64), SHA-256 `4a39a2b9e9066a8bfbe8b5363a85de82e43e27688b7dff456f4cd577bb47bab6`.

Set these to real absolute paths for one version; repeat with a different
output directory for the other version:

```sh
export PROBE_DIR=/tmp/issue571-v1.6.1
export FWLIVE_REPO=/absolute/path/to/clean/fwlive
export SOURCE_FILE="$FWLIVE_REPO/core/fwlive-log.js"
export REGEXPROOF_REPO=/absolute/path/to/regexproof
export NOODLER_BIN=/absolute/path/to/verified/noodler
export NOODLER_SHA256=22b19f123d3e7f54e10fdc46af3f91de23d89148c9a259eb072bc9e12f083464
python3 sweep/issue-571/2026-10-18/probe.py init
for probe_case in source-upper source-mixed ascii-mirror-mixed \
  negative-membership negative-membership-unconstrained m2e-diff \
  flags-second-argument inline-i-flag historical-negation-crash-control \
  property-escape-non-u-literal property-escape-letter \
  property-escape-u-argument non-u-dot-astral; do
  python3 sweep/issue-571/2026-10-18/probe.py "$probe_case"
done
```

Each invocation has a 20-second total subprocess budget and each subprocess
an eight-second limit, with process-group termination and disabled core dumps.
A successful diagnostic invocation means that a record was written; it does
**not** turn a backend crash, parser error, unknown or timeout into a proof.
The record checks process status before accepting a trailing `sat` line.
The script refuses source/binary/runner drift between initialization and queries.

Native context inventory, including UTF-16, captures and property-escape mode
controls:

```sh
node sweep/issue-571/2026-10-18/native-inventory.js "$SOURCE_FILE"
```

`comparison-summary.json` is a convenience index over the retained per-case
SMT inputs and result JSON (including unmodified stdout/stderr strings). Identical case names use identical
SMT hashes across versions. SHA-256s bind the actual executed script and input
bytes; baseline Git heads identify the investigation checkout before generated
evidence was committed. Absolute paths and timings are historical provenance,
not portability assumptions or stable expected output.
