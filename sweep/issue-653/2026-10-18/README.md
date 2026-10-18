# #653 prefix-guard Rocq feasibility snapshot

Research only. **PARTIAL feasibility; NO-GO for an as-written fwlive proof claim
or consumer-gate registration from these artifacts.** See the
[disposition](../../../docs/issue-653-prefix-rocq-feasibility-2026-10-18.md).

No runtime, harness route, production tool pin, U9 or fwlive gate changes.
Native examples, the hand-built AST probe and the return-logic sublemma are
separate kinds of evidence. None proves source parsing or a concrete
full-UTF-16 instantiation of the fwlive regex.

## Pins and preparation

Linux amd64, Docker available. Fetch source without executing it, then verify
these revisions before building:

```sh
git clone https://github.com/LindenRegex/Warblre.git /tmp/issue653-warblre
git -C /tmp/issue653-warblre checkout --detach 87af3ccaea96015d4104c0b2d9de758fa8d9ee87
git clone https://github.com/ocaml/dune.git /tmp/issue653-dune
git -C /tmp/issue653-dune checkout --detach 6f6eee69eda59e355bae2ca4e3ad1af678271883

docker pull rocq/rocq-prover@sha256:9a1e969649a3cc3c6f310d5be5a842e2187384560337c6c0807aba9f8565efba
docker run --rm --network none --cpus 4 --memory 8g \
  -v /tmp/issue653-dune:/dune -w /dune \
  rocq/rocq-prover@sha256:9a1e969649a3cc3c6f310d5be5a842e2187384560337c6c0807aba9f8565efba \
  bash -lc 'ocaml boot/bootstrap.ml -j 4'
```

The image contains Rocq 9.1.1, Stdlib 9.0.0 and OCaml 4.14.2. Its bundled
Dune 3.21.1 cannot read the unmodified Warblre Dune 3.23 language declaration
(`initial-upstream-build.log`); Dune 3.23.1 is bootstrapped from the pinned
release source instead. The digest pins all published image bytes, including
its installed packages (`toolchain.log`). It is not a claim of reproducible
compiler/container builds or a signed publisher attestation.

Run from this regexproof snapshot:

```sh
WARBLRE_BUILD=/tmp/issue653-warblre DUNE_SOURCE=/tmp/issue653-dune \
  python3 sweep/issue-653/2026-10-18/run-rocq-checks.py
```

This uses prepared, operator-controlled directories. It rejects wrong Git
revisions, tracked-source edits and unexpected nonignored untracked files
before executing build code. Existing copies of the two research `.v` inputs
are accepted only when their bytes match this snapshot; missing copies are
installed exclusively. The Dune source tree must have no extra untracked
source. Pre-existing `Mutant*.v` paths are rejected, and cleanup removes only
mutant files created by this run whose bytes still match. It copies the two
research `.v` files into the example directory, cleans and rebuilds the
unmodified upstream proof plus the probes, runs `rocqchk` on their compiled
modules and dependencies, then requires three specific theorem rejections.
Each Docker invocation has no network, four CPUs, 8 GiB and a 600-second
subprocess timeout; timeout cleanup removes the named container. Negative
sources are removed after their runs. No arbitrary failure counts as a
successful negative control. `rocq-results.json` contains commands, statuses,
timings, raw streams and proof/runner hashes; a failed run exits nonzero and
retains partial records. Replay overwrites that results file.

The Dune bootstrap command above is preparation, not a proof gate. Its captured
output is `dune-bootstrap.log`; no dependency fetch occurs inside proof runs.
Build trees, images, source archives and `.vo` binaries are not committed.

## Native observations

Prepare an isolated clean fwlive checkout at
`aa1554730999de8cf3660f959c8ffd1e554b8992`, then run:

```sh
SOURCE_ROOT=/path/to/fwlive \
  node sweep/issue-653/2026-10-18/regexproof-653-native.js > /tmp/issue653-native.json
```

The script checks the expected commit and core/LuCI hashes **before** loading
those modules. It also computes and checks each inventory Git blob ID from the
listed file bytes before loading or evaluating either module. An optional
`source-commit.txt` identifies an archived tree; otherwise HEAD is read with
Git. It exercises the actual guard on 21 finite inputs, plus two weakened
native regexes. The small classifyTrim loop is
reproduced in this diagnostic and is not a proved preprocessing adapter.
Results and expected code-unit sequences are in `regexproof-653-native.json`.
No source tree, Node binary or generated witness is bundled. A fresh run from
a different path changes reproduction metadata; compare semantic records and
pins rather than demanding whole-JSON byte identity across paths.

## Artifact meanings

- `PrefixAstProbe.v`: manually constructed full daemon-prefix AST, `i=true` and the other represented boolean flags false, with the Unicode
  field erased to `unit`, **upstream ASCII-oriented NaiveEngine**.
  Four finite computational facts; this is not source-parsing correspondence,
  a faithful full UTF-16 engine or the proposed universal equivalence theorem.
- `CanonicalizeBoundary.v`: two universal facts about explicitly defined
  return logic with abstract uppercase-to-UTF16 output, plus two concrete
  examples. The Unicode uppercase function and its correspondence with the
  ECMA algorithm and Warblre parameters remain outside these facts.
- `source-provenance.json`: source revisions/trees, selected byte hashes,
  image identity, specification and remaining trust limits.
- `rocq-image-tag.json`: upstream Docker Hub metadata used to bind the
  release tag to the executed digest; runtime invocation uses the digest.
- `criteria.md`: initial acceptance criteria/time box, recorded before build.

An initial draft canonicalization negative control failed at an obsolete proof
rewrite after the definition was weakened. That was rejected as insufficient
counterexample evidence; the retained control instead evaluates the concrete
383→83 mismatch and requires the corresponding equality theorem to fail.
Only the final measured outcomes are in `rocq-results.json`.
