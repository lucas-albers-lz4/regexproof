# Autonomous contract adoption

**Policy version:** `autonomous-contracts-v1`
**Authorized:** 2026-10-13 by the repository owner in the planning session.

Agents may draft, review, and adopt security property contracts without asking
the owner to approve each contract. This supersedes the human-adoption
requirement in earlier conversion plans and issue bodies. The owner requested
useful contract-backed proofs and runnable regression gates as the primary
output, with reproduced bugs, independent confirmation, and fixes measured too.

## Adoption requirements

Adoption requires evidence for each of the following:

1. Exact repository URL, commit pin, file, source pattern, flags, and real call
   semantics. Verify context against that checkout, including relevant callers,
   preprocessing, and the downstream sink. A consistent snippet alone is not
   source authentication.
2. A concrete security guarantee, input source, trust class, and named sink.
   Derive the expected behavior from a specification, documented boundary, or
   surrounding product behavior independently of the regex being proved.
3. An explicit input-format constraint and evidence that the relevant inputs
   can reach the sink. Distinguish a justified input restriction from a solver
   length bound. An unreachable witness class is a skip. An unverified path
   remains unresolved; a real product replay can supply missing reachability
   evidence, followed by review.
4. A declared proof domain and a feasible encoding/replay route. Capture,
   parser-composition, and output-image questions need their actual behavior
   modeled; regex membership alone does not establish those guarantees.
5. A separate review pass checking the source, guarantee, reachability, domain,
   and proposed semantics. Record author and reviewer identities and whether
   the same model performed both passes. Agent review is not human annotation
   or independent third-party confirmation.

Freeze the adopted contract and its evidence digest before the solver result
is used to assess yield. A change to the guarantee or domain creates a recorded
revision with a reason. Do not narrow a failed property silently until it passes.

## Provenance and counting

Keep agent-authored contracts at `provenance=agent_derived`. Use `human` only
when a person actually supplied or adopted the guarantee. `version_diff` and
`cross_engine` retain their existing independent-pair and `family_contract`
requirements. A draft, stub, or untargeted synthesized question is not an
adopted contract.

An agent-derived contract becomes eligible for product measurement only with
a validated `adoption` record bound to its exact source and contract digests.
The `adoption` object has its own strict nested schema; it does not change the
meaning of the contract-v1 core fields. It includes the policy version,
adoption decision, author/reviewer, source references, independent guarantee
evidence, input-format/reachability evidence, and domain justification.

Eligible product questions and their outcomes must be reported by provenance,
policy version, repository, site, and question. Preserve historical human
results and publish the autonomous series separately alongside combined
totals. Existing `agent_derived` smoke rows do not become product results
automatically; they require an evidenced adoption under this policy.

Adoption establishes the question. A useful proof or regression gate additionally
requires source-faithful semantics, the applicable mutation guards and
differential checks, a decided outcome, and reproducible execution. SAT is a
candidate counterexample until replay and security-impact review establish a
real boundary violation. `unknown`, timeout, missing engines, replay failure,
and source mismatch remain failed/not-proven outcomes. Preserve them in the
attempt denominator.

## Autonomy and resources

Routine source review, contract adoption, encoding, replay, artifact emission,
and wave close-out proceed without per-contract human approval. Preserve the
serial 15-reviewed/at-most-5-adopted wave discipline and stopped-cluster
decisions. Agents can register a genuinely new source-backed idiom through the
reviewed workflow; an unused name is not evidence of a new idiom.

Record agent elapsed time, usage/cost when available, and actual human time as
separate measurements. Never enter agent runtime into the human stopwatch
series or invent human minutes. Human intervention is measured when it occurs.

Contract adoption does not authorize third-party communications or disclosure.
Apply the existing [security policy](../SECURITY.md) to those actions. Prepare
the evidence packet and record an actual pending disposition when transmission
is awaiting authorization. A `private_first` tag alone does not prove a report
was transmitted or accepted.

## Implementation status

The shared predicate and strict adoption schema are implemented in
`regexproof/contract_adoption.py` and
`regexproof/schemas/property_contract.schema.json`. Harness emission, the
conversion queue/ledger, saturation observations, and PR4 checkpoint use the
same rule. Historical v2 PR4 checkpoints remain human-only and readable; v3
requires a contract-hash-bound roster and complete attempt outcomes. The
Forge CLI helper-image row is the first agent-derived product row. Autonomous
runtime and cost measurements use a separate `autonomous_work.jsonl` log; the
human stopwatch artifact remains unchanged. The recorder reads historical
v1/v2 rows and writes v3 rows. V2 and v3 label elapsed time as `wall_clock` or
`phase_sum`, so subsecond runner stages remain measurable when the runner's
timestamps are stored only to whole seconds. V3 also requires a `work_items`
array recording every reviewed site and each attempted question ID; those
identities must exactly match the aggregate reviewed-site and attempted-question
counts.
