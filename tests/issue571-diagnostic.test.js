'use strict';

const assert = require('node:assert/strict');
const test = require('node:test');
const { spawnSync } = require('node:child_process');
const path = require('node:path');
const { CASES, observe } = require('../scripts/issue571-diagnostic.js');

// Deliberately synthetic APIs test diagnostic mechanics, never source fidelity.
function stub() {
	const api = {};
	for (const name of ['ACTION_RE', 'DENY_ACTION', 'NON_FIREWALL_PREFIX', 'FIREWALL_HINT']) {
		api[name] = /unused/i;
		api[name].test = input => CASES.find(row => row[0] === name && row[1] === input)[2];
	}
	api.parseFlags = (input, kv) => {
		assert.deepEqual(kv, {});
		return CASES.find(row => row[0].startsWith('TCP_FLAG_TAIL') && row[1] === input)[2];
	};
	return api;
}

test('finite observations have exactly the declared corpus', () => {
	const rows = observe(stub());
	assert.equal(rows.length, 28);
	assert.ok(rows.every(row => row.ok));
	assert.ok(CASES.every(row => row[1].length < 64));
});

test('sensitivity: an always-accept boundary mutation is caught', () => {
	const api = stub();
	api.ACTION_RE = /(?:)/i;
	const rows = observe(api);
	assert.equal(rows.find(row => row.input === 'XaCcEpTY').ok, false);
});

test('missing export and changed flags fail closed', () => {
	const api = stub();
	delete api.DENY_ACTION;
	assert.throws(() => observe(api), /DENY_ACTION/);
	api.DENY_ACTION = /DROP/iu;
	assert.throws(() => observe(api), /only i flag/);
});

test('CLI requires an explicit trusted source and emits no success evidence on error', () => {
	const script = path.resolve(__dirname, '../scripts/issue571-diagnostic.js');
	for (const args of [[], ['/no-such-issue571-source.js']]) {
		const result = spawnSync(process.execPath, [script, ...args], { encoding: 'utf8', timeout: 10000 });
		assert.equal(result.status, 1);
		assert.equal(result.stdout, '');
		assert.notEqual(result.stderr, '');
	}
});
