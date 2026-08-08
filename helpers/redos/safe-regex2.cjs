#!/usr/bin/env node
/**
 * Argv-only safe-regex2 triage wrapper.
 * Usage: node safe-regex2.cjs <pattern>
 * Prints one JSON object. Does not override recheck — triage only.
 */
"use strict";

const safe = require("safe-regex2");
const pkg = require("safe-regex2/package.json");

const pattern = process.argv[2];

function emit(obj) {
  process.stdout.write(JSON.stringify(obj) + "\n");
}

if (pattern === undefined) {
  emit({
    tool: "safe-regex2",
    tool_version: pkg.version,
    result: "error",
    error_message: "usage: node safe-regex2.cjs <pattern>",
  });
  process.exit(0);
}

try {
  const ok = safe(pattern);
  emit({
    tool: "safe-regex2",
    tool_version: pkg.version,
    result: ok ? "safe" : "vulnerable",
    severity: ok ? null : "heuristic",
    confidence: "low",
    error_message: null,
  });
} catch (err) {
  emit({
    tool: "safe-regex2",
    tool_version: pkg.version,
    result: "error",
    severity: null,
    confidence: null,
    error_message: String(err && err.message ? err.message : err),
  });
}
