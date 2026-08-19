#!/usr/bin/env node
/** Replay: node match.mjs [--batch] <pattern> <flags> — reads stdin.
 *
 * Single mode (default): stdin is ONE witness (raw bytes); exit 0 on test().
 * Batch mode: `node match.mjs --batch <pattern> <flags>` — stdin is the
 * NUL-framed batch stream; emits one `<index>:<verdict>` line per witness on
 * stdout (0 = rejected, 1 = accepted). The `--batch` flag form (not a
 * positional `batch`) keeps a pattern literally named "batch" unambiguous.
 *
 * Exit codes (helper contract): 0 = accepted, 1 = rejected, 2 = compile /
 * engine error. Batch framing: each witness is escaped byte-wise (0x00 →
 * `\0`, `\` → `\\`) before being NUL-delimited, so witnesses containing NUL
 * round-trip exactly across the NUL delimiter.
 *
 * Pattern/flags are CLI args to this ground-truth replay harness. Escaping
 * them would change language membership (the pattern *is* the SUT). Compile
 * failures exit 2; hang/ReDoS is bounded by the caller subprocess timeout.
 * Not an untrusted-service injection boundary — see docs/SECURITY-AUDIT.md. */
const batch = process.argv[2] === "--batch";
const pattern = batch ? process.argv[3] ?? "" : process.argv[2] ?? "";
const flags = batch ? process.argv[4] ?? "" : process.argv[3] ?? "";
let re;
try {
  // codeql[js/regex-injection] Harness argv is the pattern under test; escaping would change fuzzing semantics.
  re = new RegExp(pattern, flags);
} catch (e) {
  console.error(e);
  process.exit(2);
}

async function readStdin() {
  const chunks = [];
  for await (const c of process.stdin) chunks.push(c);
  return Buffer.concat(chunks);
}

/** Split a Buffer on raw NUL bytes (the escaped frames contain none). */
function splitNul(buf) {
  const parts = [];
  let start = 0;
  for (let i = 0; i < buf.length; i++) {
    if (buf[i] === 0) {
      parts.push(buf.subarray(start, i));
      start = i + 1;
    }
  }
  parts.push(buf.subarray(start));
  return parts;
}

/** Decode one NUL-framed witness: 0x00 → `\0`, `\` → `\\` escape layer. */
function decodeFrame(buf) {
  const out = [];
  for (let i = 0; i < buf.length; i++) {
    const b = buf[i];
    if (b === 0x5c) {
      const n = buf[i + 1];
      if (n === 0x5c) {
        out.push(0x5c);
        i++;
      } else if (n === 0x30) {
        out.push(0x00);
        i++;
      } else {
        out.push(b);
      }
    } else {
      out.push(b);
    }
  }
  return Buffer.from(out).toString("utf8");
}

async function main() {
  const raw = await readStdin();
  if (!batch) {
    const s = raw.toString("utf8");
    process.exit(re.test(s) ? 0 : 1);
  }
  const frames = splitNul(raw);
  if (frames.length && frames[frames.length - 1].length === 0) frames.pop();
  for (let i = 0; i < frames.length; i++) {
    const s = decodeFrame(frames[i]);
    console.log(`${i}:${re.test(s) ? 1 : 0}`);
  }
}

main();
