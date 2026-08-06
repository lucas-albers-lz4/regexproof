# fwlive classifier regexes — inventory + verification route

Source: `lucas-albers-lz4/fwlive` umbrella issue #120 (2026-08). Target: the
LuCI firewall-log classifier (`core/fwlive-log.js` → generated `log.js` +
shell classifier). These are **ECMA (JS) regexes** on untrusted log input.

## Why JS patterns matter here

The classifier's authoritative source is the JS `CLASSIFY_SPEC`
(`core/fwlive-log.js`). The generated shell classifier mirrors it. Verifying
the *shell mirror* (a generated artifact) is weaker than verifying the
**authoritative ECMA source** — which is exactly what Z3-Noodler's
`re.from_ecma2020` enables (see docs/BACKENDS.md).

## Pattern inventory

| Pattern | Location | Feature risk | Verification route |
|---|---|---|---|
| `ACTION_RE` (7-word alternation) | log.js | finite alternation, word boundaries | per-alternative (decomposition rule 3) |
| `DENY_ACTION` | log.js | finite alternation | per-alternative |
| `FIREWALL_HINT` | log.js | word boundaries | alphabet-level boundary classes + token set |
| `NON_FIREWALL_PREFIX` | log.js | prefix logic | string ops / `PrefixOf` |
| `TCP_FLAG_TAIL` | log.js | `\s*$` anchor + finite flag alternation | friendliest pattern — anchored form solves easily |
| `NETFILTER_KV_GLUE` | log.js:27 | **lookahead `(?=(IN|OUT|SRC|…)=)`** | **cannot go to stock Z3 as written** — see below |

## The lookahead blocker: `NETFILTER_KV_GLUE`

`/([^\s])(?=(IN|OUT|SRC|DST|PROTO|SPT|DPT|LEN|MAC|TYPE|CODE|TTL|TOS|PREC|DF)=)/g`
uses a **lookahead** `(?=...)`. Stock Z3's regex theory is the regular-language
theory — there are no lookahead/lookbehind/backreference constructors, so this
pattern **cannot be encoded in stock `z3-solver` as written**. Two valid paths:

- **Rewrite as string-ops:** the lookahead "char X followed by `IN=`/`OUT=`/…"
  models as a prefix/substring check on the remainder — the standard
  decomposition, keeps the stock-z3 path.
- **Route through Z3-Noodler `re.from_ecma2020`:** converts the ECMA regex
  directly — the *only* way to verify the pattern *as written*, valuable for a
  codegen'd spec.

`NETFILTER_KV_GLUE` is the **only** classifier pattern with a lookahead; the
rest are regular-language expressible.

## Decomposition route per pattern (in preference order)

1. **Alphabet-level split:** containment properties become character-class
   disjointness — instant, length-independent. The `is_resolvable_address`
   check is the canonical case.
2. **Alternation flattening:** `ACTION_RE`/`DENY_ACTION`'s 7-word alternations
   are finite sets — check per-alternative or prove equivalence to the
   enumerated set.
3. **Word-boundary patterns are already decomposed:** `(^|[^A-Za-z0-9_])…`
   splits into prefix-boundary check + core token + suffix-boundary check —
   prove boundary classes (alphabet-level) separately from the token set
   (per-alternative).
4. **String ops for extraction:** `\b([A-Z]+)=([^\s]+)/g` and the
   strip/normalize pipeline (log.js:139-303) model as
   `IndexOf`/`SubString`/`Contains` — regex for membership, string ops for
   transformation. (The usrmanage P3 pattern, 2ms.)
5. **Anchor and bound:** anchored forms are dramatically easier;
   `TCP_FLAG_TAIL`'s `\s*$` anchor + finite flag alternation is the friendliest
   pattern in the spec.

## F-scope notes from the umbrella (#120)

- F2: model classify predicates from the **ECMA regexes** via
  `re.from_ecma2020` (requires Z3-Noodler binary) — verifies the source, not
  the mirror.
- F3: Z3-Noodler-generated adversarial log lines feed the existing JS↔shell
  parity harness.
- Keep stock `z3-solver` as the default path; use Noodler for the
  ECMA-direct properties. Noodler is a separate binary (cmake build,
  auto-fetches Mata) — CI wiring needs a build step or vendored binary.
