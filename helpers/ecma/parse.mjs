#!/usr/bin/env node
/**
 * ECMA regex parse helper via regexpp (Phase 1).
 * Usage: node parse.mjs <pattern> <flags>
 * Prints JSON {ok, ast_type} or {ok:false, error, unencodable_reason}.
 */
import { parseRegExpLiteral } from "regexpp";

const pattern = process.argv[2] ?? "";
const flags = process.argv[3] ?? "";

const rejectFlags = new Set(["u", "v", "m", "g", "y"]);
for (const f of flags) {
  if (rejectFlags.has(f)) {
    console.log(
      JSON.stringify({
        ok: false,
        unencodable_reason: f === "u" || f === "v" ? `${f}-flag` : f === "m" ? "m-flag" : "stateful",
        error: `rejected flag ${f}`,
      }),
    );
    process.exit(1);
  }
}

try {
  const literal = `/${escapeForLiteral(pattern)}/${flags}`;
  const ast = parseRegExpLiteral(literal);
  const reason = findReject(ast.pattern);
  if (reason) {
    console.log(JSON.stringify({ ok: false, unencodable_reason: reason }));
    process.exit(1);
  }
  console.log(
    JSON.stringify({
      ok: true,
      helper: "ecma-regexpp",
      ast_type: ast.type,
      flags: ast.flags.raw,
      structure: structureReport(ast.pattern),
    }),
  );
} catch (err) {
  console.log(
    JSON.stringify({
      ok: false,
      unencodable_reason: "parse-error",
      error: String(err.message || err),
    }),
  );
  process.exit(1);
}

// Escape only *unescaped* slashes; existing escape sequences (including `\/`)
// pass through verbatim. Escaping `\` first would corrupt source-text
// semantics (`\d` would become `\\d` — literal backslash + "d").
function escapeForLiteral(p) {
  let out = "";
  for (let i = 0; i < p.length; i++) {
    if (p[i] === "\\" && i + 1 < p.length) {
      out += p[i] + p[i + 1];
      i++;
    } else if (p[i] === "/") {
      out += "\\/";
    } else {
      out += p[i];
    }
  }
  return out;
}

function findReject(node, seen = new Set()) {
  if (!node || typeof node !== "object") return null;
  // regexpp ASTs are cyclic (parent / Backreference.resolved back-edges) —
  // without a visited set this walk overflows the stack on every pattern.
  if (seen.has(node)) return null;
  seen.add(node);
  if (node.type === "Assertion") {
    if (node.kind === "lookahead" || node.kind === "lookbehind") return "lookaround";
    // word/start/end: handled in compiler (ASCII edge \b encode; mid-pattern
    // \b and \B are honest rejects there — TRAPS #25).
    if (node.kind === "word" || node.kind === "start" || node.kind === "end") return null;
  }
  if (node.type === "Backreference") return "backref";
  for (const v of Object.values(node)) {
    if (Array.isArray(v)) {
      for (const item of v) {
        const r = findReject(item, seen);
        if (r) return r;
      }
    } else if (v && typeof v === "object") {
      const r = findReject(v, seen);
      if (r) return r;
    }
  }
  return null;
}

// Per-alternative structural facts for the D7 registration gate (design #213
// S1 + S1-parser). Facts are AST-derived (never string-regex on the pattern):
// each alternative reports whether it is fully anchored (^ first, $ last), has
// a leading/trailing `.*` wrap element, and how many top-level alternatives
// exist (top-level alternation is a registration-check input).
function dotStar(el) {
  return (
    el &&
    el.type === "Quantifier" &&
    el.min === 0 &&
    el.max === Infinity &&
    el.element &&
    el.element.raw === "."
  );
}

function structureReport(pattern) {
  return {
    alternatives: pattern.alternatives.map((alt) => {
      const els = alt.elements;
      const first = els[0];
      const last = els[els.length - 1];
      return {
        leading_anchor:
          first && first.type === "Assertion" && first.kind === "start",
        trailing_anchor:
          last && last.type === "Assertion" && last.kind === "end",
        leading_dotstar: dotStar(first),
        trailing_dotstar: dotStar(last),
        element_count: els.length,
      };
    }),
    top_level_alternation: pattern.alternatives.length > 1,
  };
}
