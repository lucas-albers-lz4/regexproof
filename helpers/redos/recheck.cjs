#!/usr/bin/env node
/**
 * Argv-only recheck wrapper.
 * Usage: node recheck.cjs <pattern> [flags]
 * Always prints one JSON object on stdout (result in JSON, not only exit code).
 */
"use strict";

const recheck = require("recheck");
const pkg = require("recheck/package.json");

const pattern = process.argv[2];
const flags = process.argv[3] ?? "";

function emit(obj) {
  process.stdout.write(JSON.stringify(obj) + "\n");
}

if (pattern === undefined) {
  emit({
    tool: "recheck",
    tool_version: pkg.version,
    result: "error",
    error_message: "usage: node recheck.cjs <pattern> [flags]",
  });
  process.exit(0);
}

const timeoutMs = Number(process.env.REGEXPROOF_RECHECK_TIMEOUT_MS || 30000);

Promise.race([
  recheck.check(pattern, flags),
  new Promise((_, reject) =>
    setTimeout(
      () => reject(Object.assign(new Error("recheck timeout"), { code: "TIMEOUT" })),
      timeoutMs,
    ),
  ),
])
  .then((r) => {
    const status = r && r.status ? String(r.status) : "error";
    let result = "error";
    if (status === "vulnerable" || status === "safe") result = status;
    else if (status === "unknown") result = "error";
    emit({
      tool: "recheck",
      tool_version: pkg.version,
      result,
      severity: r.complexity && r.complexity.type ? r.complexity.type : null,
      confidence: r.checker || null,
      detail: {
        status,
        complexity: r.complexity || null,
        hotspot: r.hotspot || null,
      },
      error_message: result === "error" ? `recheck status=${status}` : null,
    });
    process.exit(0);
  })
  .catch((err) => {
    const isTimeout =
      err && (err.code === "TIMEOUT" || /timeout/i.test(String(err.message || err)));
    emit({
      tool: "recheck",
      tool_version: pkg.version,
      result: isTimeout ? "timeout" : "error",
      severity: null,
      confidence: null,
      error_message: String(err && err.message ? err.message : err),
    });
    process.exit(0);
  });
