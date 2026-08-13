# PEpper ↔ sec_check — shared-ruleset overlap analysis

**Date:** 2026-08-13 · **Follow-on** from [#317](https://github.com/lucas-albers-lz4/regexproof/issues/317) (both READMEs flagged "likely a shared/derived ruleset").

## Question

Both corpora are yara packs with near-identical `rules/` directory structure.
Are they independent packs, or one derived from the other — and how much of
the measured surface is actually duplicated across the two matrix rows?

## Method

Materialized both at their Smith pins and compared four levels:

| Level | PEpper | sec_check |
|---|---|---|
| Pin | `9dfcade0` (0x0be/PEpper) | `b7b98414` (netxfly/sec_check) |
| Repo created | 2019-07-13 | **2018-09-21** (≈10 mo earlier) |
| `rules/` files | 552 | 542 |
| `index.yar` header | "On 13-07-2019" | "On 06-02-2018" |

1. **File inventory** — filename intersection + sha256 byte-identity
2. **Directory layout** — shared dirs vs PEpper-only dirs
3. **Pattern strings** — `$x = /re/`, `$x = "str"`, `$x = { hex }` literal
   extraction, exact-string comparison
4. **Findings** — batch `.ndjson` finding signatures, pattern-level overlap

## Results

### 1. File level: 96.7% of shared filenames are byte-identical

```
PEpper files:      552
sec_check files:   542
shared filenames:  538
  byte-identical:  520  (96.7% of shared)
  modified:         18
only in PEpper:     14   (incl. Capabilities/, CVE_Rules/, Webshells/, 2 Maldoc)
only in sec_check:   4   (2 maldoc .doc samples, 2 yar)
```

### 2. Derivation direction: sec_check → PEpper (vendored + extended)

- sec_check predates PEpper by ~10 months (2018-09 vs 2019-07); the index
  headers match the creation dates.
- PEpper's tree is a **superset**: it contains sec_check's entire directory
  layout plus added dirs (`Capabilities/`, `CVE_Rules/`, `Antidebug_AntiVM/`,
  `Malicious_Documents/`, `Webshells/`) and 14 files sec_check lacks.
- The 18 modified shared files are extensions, not rewrites: PEpper adds
  rules (`SEH_Save` in antidebug_antivm.yar, a `WindowsPE` private helper),
  flips a private/public visibility (`000_common_rules.yar`), and the index
  files add `include` lines for the new dirs. sec_check's versions are the
  earlier, smaller set.

### 3. Pattern level: 99.4% of PEpper's patterns are sec_check's, verbatim

```
PEpper patterns:     19,986
sec_check patterns:  19,866
identical strings:   19,858   (99.86% of sec_check, 99.36% of PEpper)
only in PEpper:         128   (112 str, 13 hex, 3 re)
only in sec_check:        8
```

The 3 PEpper-only regex literals all live in the PEpper-only
`Maldoc_APT19_CVE-2017-1099.yar` (VBA `Chrw(...) & ` chains — new surface
only in that one added file).

### 4. Findings: 45/64 pattern-identical

PEpper and sec_check each produced **64 findings**; **45 are the same
finding at pattern level** (kind + pattern string). The 19 divergent ones
trace to the 18 modified shared files (PEpper's added rules introduce new
findings on the same files) and the PEpper-only files.

### 5. Fractions: 0.6229 vs 0.6189 — the near-tie is the overlap's echo

Both corpora measured nearly identical encodable fractions (PEpper
9,733/15,626 = 0.6229; sec_check 9,567/15,459 = 0.6189) with identical
finding counts (64 each). That is exactly what a shared ruleset predicts.

## Conclusion

**PEpper's `rules/` is sec_check's ruleset, vendored and extended.** ~99.4%
of PEpper's pattern surface (19,858/19,986 literals) is byte-identical to
sec_check's; the delta is 128 added patterns concentrated in ~15 added/modified
files. The two matrix rows therefore measure **the same underlying corpus
twice** — the shared 96-99% contributes nothing novel to the second row.

**Corpus-side implications:**
- The sec_check row is the canonical one (original author, earlier pin).
  PEpper's marginal value is its added surface: the `Capabilities/`,
  `CVE_Rules/`, `Antidebug_AntiVM/`, `Malicious_Documents/`, `Webshells/`
  dirs and the 3 novel Maldoc regex literals.
- No admission change is proposed: both are already `go` + measured, and the
  overlap analysis is documentation, not a reversal. If matrix dedup is ever
  wanted, PEpper's row could be re-scoped to its additive surface
  (PEpper-only files) rather than dropped — it does carry real novel rules.
- **Extractor lesson (confirmed):** the `yara` extractor counts every
  `$x = /re/` literal including vendored/derived packs. When two mined
  candidates share a rules lineage, cross-corpus overlap analysis (file
  byte-identity + pattern-string intersection) should precede any
  scale-based GO — same class as the vendored-bundle and testdata
  inflation checks (exchange-api, typenix, magento).

## Reproduce

```bash
git clone --filter=blob:none https://github.com/0x0be/PEpper.git /tmp/pepper-check
git -C /tmp/pepper-check fetch --depth 1 origin 9dfcade04b41422b5c8457956f984cd25fe3e6d2
git -C /tmp/pepper-check checkout 9dfcade04b41422b5c8457956f984cd25fe3e6d2
git clone --filter=blob:none https://github.com/netxfly/sec_check.git /tmp/sec-check
git -C /tmp/sec-check fetch --depth 1 origin b7b9841432f0f4c69f360d910c5fcce4d0e4a01f
git -C /tmp/sec-check checkout b7b9841432f0f4c69f360d910c5fcce4d0e4a01f
# file byte-identity: sha256 over every rules/ file, intersect by relative path
# pattern strings: regex `\$[A-Za-z_]\w*\s*=\s*/(?:[^/\\]|\\.)+/` (+ "str" / { hex } variants)
```
