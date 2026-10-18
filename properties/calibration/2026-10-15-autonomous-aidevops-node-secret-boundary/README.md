# Aidevops Node secret-read boundary calibration

This is a source-bound slice at the frozen Aidevops 20-r2 pin
`8666b6c6c52472b5535aa295f2df593918152cb1`. It treats the Node plugin as a
separate product engine from the existing BusyBox shell family. The original
20-r2 entry registers POSIX shell for Aidevops; this ECMA work is therefore a
separate one-repository calibration cohort in `cohort-manifest.json`, with its
own contract roster. It is not a 20-r2/P7 question and does not change that
cohort's denominator.

The representative property covers the case-insensitive secret-file extension
regex in `quality-hooks-secret-read.mjs`. The declared boundary is a
model-controlled OpenCode read path. `quality-hooks.mjs` routes pre-tool calls
through `checkSecretReadWithApproval`; for this extension reason,
`source-access-approval.mjs` falls back to `checkSecretReadGate`, which throws
before a read. The property covers only `.pem`, `.key`, `.p12`, `.pfx`,
`.kdbx`, `.age`, `.asc`, and `.gpg` suffixes. It does not claim complete secret
path coverage; `.pub` is deliberately allowed by an earlier branch.

The P4-selected line-7 `SECRET_BASENAME_RE` is a separate source predicate and
has its own contract, product roster, harness property, and gate. Its source
anchor is recorded as `:7:SECRET_BASENAME_RE` for the proof-wave runner's
line-and-symbol check; the P4 allocation retains its original source-column
identity `:7:27`.

This exact-pin source evidence justifies revisiting the earlier ECMA deferral
as a new Node slice. The prior GO decision still records whole-corpus
`security_boundary=false` and scale as its admission basis; this slice makes no
claim that Aidevops as a whole is a security-tool corpus. It does not reuse the
`AI-aidevops` BusyBox family.

`contract.json` is autonomously adopted under `autonomous-contracts-v1`.
`source-evidence.json` records the pinned helper and caller hashes;
`roster.json` binds the adopted contract to the separate ECMA calibration.

The Z3 query checks all 66 ASCII case variants of the eight declared extension
suffixes. This is an exhaustive finite-domain proof of the regex vocabulary,
not a theorem over arbitrary filenames. The ground-truth replay loads the exact
pinned Node helper, checks those suffixes with representative ordinary and
Unicode stems, checks the `.pub` exception, and mutates the real pinned rule by
removing `.pem`; the mutation witness must reach the read gate without a block.
The gate also checks the pre-read caller path against exact pinned source
hashes.

## P2 source inventory and P4 allocation

The original 20-r2 admission artifact declares 1,042 ECMA sites for Aidevops.
The separate P2 source freezer was run against the exact pin with its
registered, hidden-path-aware Babel extractor and emitted 1,018 ECMA rows
(complete repository, no submodule or oversized-file omissions). These counts
come from distinct extractors and scopes; the raw 1,018-row inventory is the
source for this allocation, and neither count is boundary coverage. The frozen
files are [`source-inventory/inventory.json`](source-inventory/inventory.json)
and [`source-inventory/sites.ndjson`](source-inventory/sites.ndjson).

The registry admits only the three encodable predicates from
`quality-hooks-secret-read.mjs`: secret basename, private-key extension, and
public-key exception. The two path predicates on lines 10–11 compile as
`per-alternative-anchor` and were excluded from this solver allocation. The
already adopted extension site is reserved by the frozen question-history
index, leaving two eligible candidates. Scheduler output selected
`aidevops/ecma-plugins` at the exact GO pin using `named-next-unused`.

Population `aidevops-ecma-secret-read-p4-20261015-r1` froze those two
candidates before review or solving. The pre-outcome ledger does not support
calling either predicate productive or novel, so both were classified
`unclassified`; no class share was inferred from a similar Forge
`secret-redaction` bucket. The committed seed produced one uniform unbiased
selection: `.agents/plugins/opencode-aidevops/quality-hooks-secret-read.mjs:7:27`
(`secret-file-basename-deny`). The representative contract at line 8 was not
eligible for selection.

The population SHA-256 is
`f18c79c5b74a17157cfb0629dd4bc1d3922b438df726095746289f17e6b8cc68`; the
selection seed commitment is
`7c1a674d3c592f5f93bc13726d67dad3a729249f0ecbb2ed21b818c0618f0105`.
The output in [`allocation.json`](allocation.json) reverified two inventory
rows, two class records, both history identities, and the clean pinned source
file. Actual arm counts are one unbiased, zero productive, zero novel, and
zero reallocated. This is the first real P4 allocation path, but a two-site
population and one-site selection cannot estimate yield or allocator quality;
it is not an original 20-r2/P7 question or a product finding. The selected
predicate was subsequently source-reviewed, including its model-controlled
pre-read callers, then contracted and proved as described below.

## P5/P6 basename proof and gate

The selected basename rule now has a narrow adopted contract in
[`contract-basename.json`](contract-basename.json), a separate frozen roster,
and an independent question ID from the extension property. Its guarantee is
limited to the 64 ASCII upper/lower-case variants of basename `secret`; it
does not assert secret-policy completeness or false-positive rates. The P4
population and allocator outputs remain unchanged.

The exact source compiler mirror returned UNSAT for the finite-domain property
with Z3 5.0.0. Weakening the real pinned source expression by deleting its
`.*secret.*` alternative produced the SAT witness `secret`, and Node replay
confirmed that `/tmp/secret` then reaches the read without a block. The current
product regression gate checks the 73 read paths across Read, Glob, and
NotebookRead, plus one Write bypass: 220 product calls total. This covers all
64 case variants, seven representative sensitive basenames, `.pub`, a negative
basename, and a non-read call. It reported zero mismatches under local Node
v26.11.1. CI runs the same gate under its pinned Node 22 runtime and saves a
machine-readable report; runtime versions are therefore recorded separately.

P6 wave `aidevops-secret-basename-20261015-r2` verified the clean exact-pin
checkout and contract roster, ran the family mutation guard and UNSAT property,
passed the then-74-call local Node gate, and emitted a complete checkpoint and
conversion row. Its measured runner phases were about 0.30 s solver time,
0.43 s gate time, 0.02 s source verification, and 0.06 s mutation checking.
These are one-question runner timings, not end-to-end authoring or review
throughput. The first wave (`r1`) correctly recorded a failed local gate
because its command resolved the virtualenv interpreter symlink to a global
Python missing `jsonschema`; no question was retried in place. A fresh r2 wave
used the venv path and passed.

After expanding the product replay to all three read tools, the contract roster
was re-frozen and P6 wave `aidevops-secret-basename-20261015-r3` completed with
the 220-call gate. It again recorded UNSAT, a SAT mutation witness reproduced
through all three real read-tool names, a passing local gate, and a complete
checkpoint. Runner phases were 0.30 s solver, 0.42 s gate, 0.02 s source
verification, and 0.05 s mutation checking. The original r1 and r2 snapshots
remain immutable. See [`p6-basename-wave-r2/checkpoint.json`](p6-basename-wave-r2/checkpoint.json),
[`p6-basename-wave-r3/checkpoint.json`](p6-basename-wave-r3/checkpoint.json),
and [`basename-gate-report.json`](basename-gate-report.json).

The phase-only P6 r3 measurement is recorded in
[`../../generated/autonomous_work.jsonl`](../../generated/autonomous_work.jsonl)
under the separate ECMA cohort. It counts one attempted/decided UNSAT
question, one local gate, one mutation check, and 220 differential calls over
0.7955 measured runner seconds. Contract authoring, source review, whole-turn
tokens/cost, and human active time were outside that interval and remain
unknown; this row is excluded from the 20-r2 scorecard.
