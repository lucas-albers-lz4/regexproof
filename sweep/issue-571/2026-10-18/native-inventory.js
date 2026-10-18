#!/usr/bin/env node
'use strict';
// Research snapshot only. The supplied module is trusted operator code:
// require() executes it. Use the clean, hash-pinned fwlive source below.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const crypto = require('node:crypto');
const path = require('node:path');
assert.equal(process.argv.length, 3, 'usage: native-inventory.js /absolute/path/to/core/fwlive-log.js');
const file = path.resolve(process.argv[2]);
const bytes = fs.readFileSync(file);
const sha = crypto.createHash('sha256').update(bytes).digest('hex');
assert.equal(sha, '52983d7c0a629de4ee23a13873e5ac54cf7d08dfaf03383614fceb59a4d1da12', 'frozen source hash');
const m = require(file);
const patterns = {};
for (const name of ['ACTION_RE', 'DENY_ACTION', 'NON_FIREWALL_PREFIX', 'FIREWALL_HINT', 'DENY_ACTION_UNDERSCORE']) {
	assert.ok(m[name] instanceof RegExp, name);
	assert.equal(m[name].flags, 'i', `${name} original flags`);
	patterns[name] = { source: m[name].source, flags: m[name].flags };
}
const tcpLine = bytes.toString('utf8').split('\n').find(line => line.startsWith('const TCP_FLAG_TAIL = '));
assert.ok(tcpLine, 'TCP source literal');
const inputs = ['ACCEPT', 'aCcEpT', 'DROP ACCEPT', '\u0000aCcEpT\u0000',
	'\ud800aCcEpT\udfff', 'ſaCcEpT', 'aCcEpT_suffix', 'x aCcEpT!'];
const observations = inputs.map(input => {
	const match = m.ACTION_RE.exec(input);
	return { input, utf16: Array.from({ length: input.length }, (_, i) => input.charCodeAt(i)),
		match: match ? { index: match.index, captures: Array.from(match) } : null };
});
const flags = ['sYn eCe cWr', 'sYn\u00a0eCe\u2028cWr', 'sYn window=1', 'ſsYn']
	.map(input => ({ input, result: m.parseFlags(input, {}) }));
console.log(JSON.stringify({ product: false, formal_proof: false,
	purpose: 'finite native observations and source inventory; no solver witnesses',
	source_sha256: sha, node: process.version, patterns,
	tcp: { exported: false, sourceLiteral: tcpLine, consumer: 'parseFlags after stripKvSpans, except KV override' },
	actionObservations: observations, flagConsumerObservations: flags,
    capabilityControls: {
        propertyEscapeNonU: { source: '^\\p{L}$', flags: '', letter: new RegExp('^\\p{L}$').test('A'), literal: new RegExp('^\\p{L}$').test('p{L}') },
        propertyEscapeU: { source: '^\\p{L}$', flags: 'u', letter: /^\p{L}$/u.test('A'), literal: /^\p{L}$/u.test('p{L}') },
        nonUDotAstral: { source: '^.$', flags: '', input: '\u{1f600}', utf16Length: '\u{1f600}'.length, accepted: /^.$/.test('\u{1f600}') }
    } }, null, 2));
