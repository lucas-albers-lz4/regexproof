#!/usr/bin/env node
/** Replay: node match.mjs <pattern> <flags>  — reads stdin, exit 0 on test(). */
const pattern = process.argv[2] ?? "";
const flags = process.argv[3] ?? "";
let re;
try {
  // pattern/flags are operator-supplied CLI args to this ground-truth replay
  // harness (differential fuzzing); not an untrusted-input boundary.
  // codeql[js/regex-injection]
  re = new RegExp(pattern, flags);
} catch (e) {
  console.error(e);
  process.exit(2);
}
const chunks = [];
for await (const c of process.stdin) chunks.push(c);
const s = Buffer.concat(chunks).toString("utf8");
process.exit(re.test(s) ? 0 : 1);
