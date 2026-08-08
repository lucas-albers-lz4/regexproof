# Dynamic compiles — what to prove when the pattern is built at runtime

Many real regexes are `re.compile`d from variables (f-strings, `.format`,
concatenation). A pattern like `re.compile(r"\b" + trigger + r"\b")` cannot
be proven as written: the harness has no value for `trigger`. This document
is the procedure for dynamic compiles (hermes-agent dogfooding,
[issue #11](https://github.com/lucas-albers-lz4/regexproof/issues/11),
gap 3 — ~518 `re.compile` sites in a 3000-file corpus).

## Classify the site first

| Class | Shape | What to prove |
|---|---|---|
| **Constant** | `re.compile(r"...")` with only literal parts | Prove the pattern as a normal property. |
| **Escaped-dynamic** | interpolation wrapped in `re.escape(x)` | Prove the *schema* with the variable as a finite set (see below). The `re.escape` guarantees no metacharacter leaks, so the mirror can treat each variable value as a literal. |
| **Raw-dynamic (config)** | interpolation WITHOUT `re.escape` | This is a **regex-injection surface** (operator config → pattern). Prove *escape-safety of the interpolation site* — or better, fix the code to `re.escape`. |
| **Constant-alternation** | `'|'.join(known_literals)` | Prove the alternation as a finite union of literals. |

## Procedure

1. **Find the variable source.** Where does the interpolated value come
   from — hardcoded constant, config file, env, user input? The trust level
   decides the class.

2. **Bound the variable space.** For escaped-dynamic sites, enumerate the
   actual values (a config table has ≤50 entries; a trigger list is finite).
   The mirror replaces the variable with `Union(Re(v1), Re(v2), ...)` over
   the enumerated values — or, when the set is too large, prove the
   *schema invariant*: the skeleton (`\b ... \b`) holds for ANY literal
   value, using `ci()`-style construction with a free string constrained to
   not contain the pattern's own metacharacters.

3. **Check for `re.escape`.** The single most important line. If the value
   is interpolated raw, the property to prove is not about the regex — it
   is about the injection surface. File a fix (escape the value) or prove
   the value space itself cannot contain metacharacters (charset proof on
   the config schema).

4. **Ground-truth the witness** as usual: run the REAL compiled pattern on
   the witness (build it exactly the way the code does, interpolation
   included).

## Worked example — escaped-dynamic

```python
# agent/reasoning_timeouts.py (hermes-agent): slug comes from a hardcoded
# model-slug table; re.escape makes it injection-proof.
compiled = re.compile(r"^" + re.escape(slug) + r"(?:$|[\-._])")
```

- Variable space: the finite `_REASONING_STALE_TIMEOUT_FLOORS` keys
  (≤50 known slugs).
- Mirror: `Concat(Re("^") or anchor, Union(*[Re(re.escape(s)) for s in SLUGS]), ...)`
- What the property proves: "no slug from the table, when escaped, can
  contain a metacharacter that escapes the pattern" — trivially true
  because `re.escape` neutralizes them; the proof is the escape itself.
- Verdict without Z3: **the `re.escape` is the security boundary.** Note it
  in the inventory; a charset proof on the slug table is optional belt.

## Worked example — raw-dynamic (the injection case)

```python
# agent/shell_hooks.py:179 (hermes-agent): matcher from user config, raw.
self.compiled_matcher = re.compile(self.matcher)
```

- Variable space: unbounded user config.
- The mirror CANNOT be built (no value for `self.matcher`).
- Correct action: **this is a finding, not a proof** — operator-config
  regex injection (ReDoS via `(a+)+$`, logic bypass via `.*`). The
  regexproof deliverable is the inventory line + severity, not a property.

## When to skip

- `re.compile` inside tests (no boundary).
- Patterns built from constants with no interpolation.
- A dynamic site whose output only feeds display text (no security
  decision downstream) — LOW value, note and move on.

## Checklist

- [ ] Variable source identified and trust-classified
- [ ] `re.escape` presence/absence recorded
- [ ] If escaped: schema property or finite-union mirror; if raw:
      injection finding with severity, not a property
- [ ] Ground-truth uses the REAL construction path (interpolation included)
