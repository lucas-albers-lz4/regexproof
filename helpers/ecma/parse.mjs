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
  const literal = `/${pattern.replace(/\//g, "\\/")}/${flags}`;
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

function findReject(node) {
  if (!node || typeof node !== "object") return null;
  if (node.type === "Assertion") {
    if (node.kind === "lookahead" || node.kind === "lookbehind") return "lookaround";
    if (node.kind === "word") return "word-boundary";
    if (node.kind === "start" || node.kind === "end") return null; // handled in compiler
  }
  if (node.type === "Backreference") return "backref";
  for (const v of Object.values(node)) {
    if (Array.isArray(v)) {
      for (const item of v) {
        const r = findReject(item);
        if (r) return r;
      }
    } else if (v && typeof v === "object") {
      const r = findReject(v);
      if (r) return r;
    }
  }
  return null;
}
