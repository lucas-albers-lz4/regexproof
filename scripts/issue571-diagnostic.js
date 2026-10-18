#!/usr/bin/env node
'use strict';

// Issue #571: finite real-engine observations, NOT a solver or formal proof.
// The supplied module is trusted operator code: require() executes it.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

const CASES = [
	['ACTION_RE', 'aCcEpT', true],
	['ACTION_RE', 'x aCcEpT y', true],
	['ACTION_RE', 'XaCcEpTY', false],
	['ACTION_RE', '_aCcEpT_', false],
	['ACTION_RE', '\u017fPASS', true], // non-/u ASCII boundary, not Unicode word boundary
	['DENY_ACTION', 'DrOp', true],
	['DENY_ACTION', 'aCcEpT', false],
	['DENY_ACTION', 'XDrOpY', false],
	['DENY_ACTION', 'reject_from_wan', false], // underscore helper is a separate rule
	['NON_FIREWALL_PREFIX', 'DnSmAsQ[123]:', true],
	['NON_FIREWALL_PREFIX', 'DnSmAsQ', true],
	['NON_FIREWALL_PREFIX', 'x DnSmAsQ:', false],
	['NON_FIREWALL_PREFIX', 'wPaD-drop', false],
	['NON_FIREWALL_PREFIX', 'wPaD:', true],
	['FIREWALL_HINT', 'FiReWaLl:', true],
	['FIREWALL_HINT', 'XFiReWaLlY', false],
	['FIREWALL_HINT', '_KeRnEl_', false],
	['TCP_FLAG_TAIL via parseFlags', 'sYn aCk', 'SYN,ACK'],
	['TCP_FLAG_TAIL via parseFlags', 'sYn eCe cWr', 'SYN,ECE,CWR'],
	['TCP_FLAG_TAIL via parseFlags', 'sYn aCk WINDOW=1 RES=0x00', 'SYN,ACK'],
	['TCP_FLAG_TAIL via parseFlags', 'sYn window=1', ''],
	['TCP_FLAG_TAIL via parseFlags', 'sYn\u00a0aCk', 'SYN,ACK'],
	['TCP_FLAG_TAIL via parseFlags', 'sYn\u2028aCk', 'SYN,ACK'],
	['TCP_FLAG_TAIL via parseFlags', 'XsYn', ''],
	['TCP_FLAG_TAIL via parseFlags', '_sYn', ''],
	['TCP_FLAG_TAIL via parseFlags', '\u017fsYn', ''],
	['TCP_FLAG_TAIL via parseFlags', 'sYnACK', ''],
	['TCP_FLAG_TAIL via parseFlags', 'sYn\n', 'SYN']
];

function observe(api) {
	for (const name of ['ACTION_RE', 'DENY_ACTION', 'NON_FIREWALL_PREFIX', 'FIREWALL_HINT']) {
		if (!(api[name] instanceof RegExp) || api[name].flags !== 'i')
			throw new Error(`${name}: expected exported non-/u RegExp with only i flag`);
	}
	if (typeof api.parseFlags !== 'function')
		throw new Error('parseFlags: missing exported real consumer');
	return CASES.map(([site, input, expected]) => {
		const observed = site.startsWith('TCP_FLAG_TAIL')
			? api.parseFlags(input, {}) : api[site].test(input);
		return { site, input, expected, observed, ok: observed === expected };
	});
}

function main(argv) {
	if (argv.length !== 1)
		throw new Error('Usage: node scripts/issue571-diagnostic.js /trusted/fwlive/core/fwlive-log.js');
	const source = path.resolve(argv[0]);
	const bytes = fs.readFileSync(source);
	const api = require(source);
	const rows = observe(api);
	const patterns = Object.fromEntries(
		['ACTION_RE', 'DENY_ACTION', 'NON_FIREWALL_PREFIX', 'FIREWALL_HINT'].map(
			name => [name, { source: api[name].source, flags: api[name].flags }])
	);
	console.log(JSON.stringify({
		issue: 571, evidence_kind: 'finite-real-engine-diagnostic',
		product: false, formal_proof: false,
		domain: 'only the listed finite strings; includes non-ASCII boundary and whitespace probes',
		engine: process.version, source, source_sha256: crypto.createHash('sha256').update(bytes).digest('hex'),
		patterns, tcp_flag_route: 'parseFlags(input, {}) real consumer; no KV override',
		rows, ok: rows.every(row => row.ok)
	}, null, 2));
	return rows.every(row => row.ok) ? 0 : 1;
}

module.exports = { CASES, observe, main };
if (require.main === module) {
	try {
		process.exitCode = main(process.argv.slice(2));
	} catch (error) {
		console.error(error.message);
		process.exitCode = 1;
	}
}
