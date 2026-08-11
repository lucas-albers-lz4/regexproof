# Noodler v1.6.1 binary pin (P1 baseline)

The parity matrix and all P1 probes run against this exact asset.

| Field | Value |
|---|---|
| Asset | z3-noodler-ubuntu-24.04-x86_64-shared |
| Release | v1.6.1 (published + last-updated 2026-06-21) |
| sha256 | 22b19f123d3e7f54e10fdc46af3f91de23d89148c9a259eb072bc9e12f083464 |
| Binary version string | `Z3 version 4.16.0` (build dcce9d2d) |
| Host | Debian 13 / glibc 2.41 (runs the Ubuntu 24.04 asset) |
| Verify | `sha256sum <asset>` must equal the sha256 above |

Provenance facts (design #213, verified 2026-08-11): MIT license; the README
SMT-COMP competition clause is scoped to competition participation and does not
affect pinned-CI-download usage; #316 (closed) and #325 (open) wrong-UNSAT reports
both replay `sat` on this build; the #344 segfault-without-set-logic class is dodged
by always emitting `(set-logic QF_SLIA)`.

Bump policy (design rev 7, R5): any version bump requires the pre-flight (R8
fixtures + determinism spot-check + parity matrix on the NEW binary) to pass and a
maintainer approval, recorded in the bump commit.
