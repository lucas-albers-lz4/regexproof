'use strict';

/* Bounded native diagnostic for the frozen fwlive origin/master snapshot. */
const crypto = require('node:crypto');
const { execFileSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');
const util = require('node:util');

const root = __dirname;
const defaultSourceRoot = path.join(root, 'source');
const sourceRoot = process.env.SOURCE_ROOT
	? path.resolve(process.env.SOURCE_ROOT)
	: defaultSourceRoot;
const expectedCommit = 'aa1554730999de8cf3660f959c8ffd1e554b8992';
const expectedCoreSha256 = '52983d7c0a629de4ee23a13873e5ac54cf7d08dfaf03383614fceb59a4d1da12';
const expectedLuciSha256 = 'efddb7eab758c5c86038248274fddf4ce1b2d7b6003e5d81cb423f1c151cc336';
const corePath = path.join(sourceRoot, 'core/fwlive-log.js');
const luciPath = path.join(sourceRoot, 'openwrt-feed/luci-app-fwlive/htdocs/luci-static/resources/fwlive/log.js');
const viewPath = path.join(sourceRoot, 'openwrt-feed/luci-app-fwlive/htdocs/luci-static/resources/view/status/fwlive.js');
const gatePath = path.join(sourceRoot, 'scripts/gen-luci-wrapper.js');
const genAllPath = path.join(sourceRoot, 'scripts/gen-all.sh');
const z3Path = path.join(sourceRoot, 'scripts/z3-verify.py');
const z3DocPath = path.join(sourceRoot, 'docs/developer/z3-verification.md');

function sha256(file) {
	return crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
}

function readSourceCommit() {
	const commitFile = path.join(sourceRoot, 'source-commit.txt');
	if (fs.existsSync(commitFile))
		return { commit: fs.readFileSync(commitFile, 'utf8').trim(), method: 'source-commit.txt' };
	return {
		commit: execFileSync('git', ['-C', sourceRoot, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim(),
		method: 'git rev-parse -C SOURCE_ROOT HEAD'
	};
}

function isReadOnlyTree(directory) {
	if ((fs.statSync(directory).mode & 0o222) !== 0)
		return false;
	for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
		const child = path.join(directory, entry.name);
		if (entry.isSymbolicLink())
			return false;
		if (entry.isDirectory() && !isReadOnlyTree(child))
			return false;
		if (entry.isFile() && (fs.statSync(child).mode & 0o222) !== 0)
			return false;
	}
	return true;
}

const sourceCommit = readSourceCommit();
const commit = sourceCommit.commit;
if (commit !== expectedCommit)
	throw new Error('source commit mismatch: expected ' + expectedCommit + ', got ' + commit);
const coreSha256 = sha256(corePath);
if (coreSha256 !== expectedCoreSha256)
	throw new Error('core/fwlive-log.js SHA256 mismatch: expected ' + expectedCoreSha256 + ', got ' + coreSha256);
const luciSha256 = sha256(luciPath);
if (luciSha256 !== expectedLuciSha256)
	throw new Error('LuCI log.js SHA256 mismatch: expected ' + expectedLuciSha256 + ', got ' + luciSha256);

/* The commit and both source-byte pins are checked before either module is loaded. */
const core = require(corePath);

function loadLuciModule(file) {
	const source = fs.readFileSync(file, 'utf8');
	const body = source
		.replace(/^'use strict';\s*/m, '')
		.replace(/^'require [^']+';[^\n]*\n/gm, '');
	const baseclass = { extend: function(descriptor) { return descriptor; } };
	return new Function('baseclass', body)(baseclass);
}

function classifyTrim(message, spec) {
	const whitespace = spec.trimWhitespace;
	let start = 0;
	let end = message.length;
	while (start < end && whitespace.indexOf(message.charAt(start)) >= 0)
		start++;
	while (end > start && whitespace.indexOf(message.charAt(end - 1)) >= 0)
		end--;
	return message.slice(start, end);
}

function codeUnits(text) {
	const units = [];
	for (let i = 0; i < text.length; i++)
		units.push('0x' + text.charCodeAt(i).toString(16).padStart(4, '0'));
	return units;
}

function utf16Length(text) {
	return text.length;
}

const luci = loadLuciModule(luciPath);
const actual = core.NON_FIREWALL_PREFIX;
const prefixes = core.CLASSIFY_SPEC.nonFirewallPrefixes;
const continuation = core.CLASSIFY_SPEC.nonFirewallPrefixHyphenContinuation
	? '[^A-Za-z0-9_-]'
	: '[^A-Za-z0-9_]';
const expectedSource = '^(' + prefixes.join('|') + ')(' + continuation + '|$)';
if (actual.source !== expectedSource)
	throw new Error('core NON_FIREWALL_PREFIX is not the regex derived from its CLASSIFY_SPEC');
if (actual.flags !== 'i')
	throw new Error('core NON_FIREWALL_PREFIX flags changed: ' + actual.flags);
if (actual.global || actual.sticky || actual.multiline || actual.unicode || actual.dotAll)
	throw new Error('unexpected core NON_FIREWALL_PREFIX mode flags');
if (!util.isDeepStrictEqual(core.CLASSIFY_SPEC, luci.CLASSIFY_SPEC))
	throw new Error('core and LuCI CLASSIFY_SPEC values differ');
if (actual.source !== luci.NON_FIREWALL_PREFIX.source || actual.flags !== luci.NON_FIREWALL_PREFIX.flags)
	throw new Error('core and LuCI NON_FIREWALL_PREFIX source/flags differ');

const probes = [
	{ id: 'nonunicode-ignorecase-long-s-in-daemon-word', input: 'dn\u017Fmasq[', expected: false },
	{ id: 'wpad-open-bracket', input: 'wpad[1]:', expected: true },
	{ id: 'wpad-mixed-case-open-bracket', input: 'WpAd[1]:', expected: true },
	{ id: 'wpad-drop-nft-prefix', input: 'wpad-drop', expected: false },
	{ id: 'wpad-underscore-continuation', input: 'wpad_drop', expected: false },
	{ id: 'wpad-ascii-letter-continuation', input: 'wpad0', expected: false },
	{ id: 'wpad-exact-end', input: 'wpad', expected: true },
	{ id: 'wpad-space-boundary', input: 'wpad IN=', expected: true },
	{ id: 'start-anchor-discriminator', input: 'xwpad[', expected: false },
	{ id: 'leading-lf-trimmed-before-guard', input: '\nwpad[', expected: true },
	{ id: 'leading-ascii-ws-and-nbsp-trimmed', input: ' \t\u00a0WpAd[', expected: true },
	{ id: 'em-space-is-not-classify-trimmed', input: '\u2003wpad[', expected: false },
	{ id: 'nul-after-prefix-boundary', input: 'wpad\u0000', expected: true },
	{ id: 'nul-before-prefix', input: '\u0000wpad[', expected: false },
	{ id: 'isolated-high-surrogate-after-prefix', input: 'wpad\ud800', expected: true },
	{ id: 'isolated-low-surrogate-after-prefix', input: 'wpad\udfff', expected: true },
	{ id: 'isolated-surrogate-before-prefix', input: '\ud800wpad[', expected: false },
	{ id: 'nonascii-letter-boundary', input: 'wpad\u00e9', expected: true },
	{ id: 'nonascii-hyphen-like-boundary', input: 'wpad\u2014drop', expected: true },
	{ id: 'supplementary-character-boundary', input: 'wpad\u{1f600}', expected: true },
	{ id: 'nonascii-before-prefix', input: '\u00e9wpad[', expected: false }
];

const results = probes.map(function(probe) {
	const normalized = core.normalizeNetfilterMessage(probe.input);
	const guardInput = classifyTrim(normalized, core.CLASSIFY_SPEC);
	const match = actual.test(guardInput);
	const luciMatch = luci.NON_FIREWALL_PREFIX.test(guardInput);
	if (match !== probe.expected)
		throw new Error('unexpected native result for ' + probe.id + ': ' + match);
	if (luciMatch !== match)
		throw new Error('LuCI native result differs for ' + probe.id);
	return {
		id: probe.id,
		inputUtf16Length: utf16Length(probe.input),
		inputCodeUnits: codeUnits(probe.input),
		normalizedUtf16Length: utf16Length(normalized),
		guardInputUtf16Length: utf16Length(guardInput),
		guardInputCodeUnits: codeUnits(guardInput),
		coreMatch: match,
		luciMatch: luciMatch,
		expectedMatch: probe.expected
	};
});

const anchorInput = 'xwpad[';
const weakenedAnchor = new RegExp(actual.source.replace(/^\^/, ''), actual.flags);
const hyphenInput = 'wpad-drop';
const weakenedHyphen = new RegExp(actual.source.replace('[^A-Za-z0-9_-]', '[^A-Za-z0-9_]'), actual.flags);
if (actual.source === weakenedAnchor.source || actual.source === weakenedHyphen.source)
	throw new Error('mutation control failed to alter the regex source');
const mutations = {
	weakenStartAnchor: {
		mutation: 'remove leading ^',
		inputCodeUnits: codeUnits(anchorInput),
		actualMatch: actual.test(anchorInput),
		mutantMatch: weakenedAnchor.test(anchorInput)
	},
	allowHyphenAsBoundary: {
		mutation: 'replace [^A-Za-z0-9_-] with [^A-Za-z0-9_]',
		inputCodeUnits: codeUnits(hyphenInput),
		actualMatch: actual.test(hyphenInput),
		mutantMatch: weakenedHyphen.test(hyphenInput)
	}
};
if (mutations.weakenStartAnchor.actualMatch !== false || mutations.weakenStartAnchor.mutantMatch !== true)
	throw new Error('start-anchor mutation did not distinguish its control input');
if (mutations.allowHyphenAsBoundary.actualMatch !== false || mutations.allowHyphenAsBoundary.mutantMatch !== true)
	throw new Error('hyphen mutation did not distinguish its control input');

const sourceInventory = [
	{
		path: 'core/fwlive-log.js',
		sha256: sha256(corePath),
		gitBlob: 'cc77bc663fc1bae0b2cb473eca2f10b2eedc2079',
		lines: {
			classifySpec: '9-21',
			nonFirewallRegex: '137-144',
			normalization: '174-184',
			consumerGuard: '389-410',
			callers: '592-620',
			exports: '669-704'
		}
	},
	{
		path: 'openwrt-feed/luci-app-fwlive/htdocs/luci-static/resources/fwlive/log.js',
		sha256: sha256(luciPath),
		gitBlob: 'c6b19cb6d24b2825d2a19252d05e46c0e97d96da',
		lines: {
			classifySpec: '13-50',
			classifyTrim: '153-161',
			nonFirewallRegex: '164-169',
			consumerGuard: '483-489'
		}
	},
	{
		path: 'openwrt-feed/luci-app-fwlive/htdocs/luci-static/resources/view/status/fwlive.js',
		sha256: sha256(viewPath),
		gitBlob: 'a6a4fc63c0cdb67a82a9cdec0c81b09a76231bd6',
		lines: { consumerCallsite: '1177' }
	},
	{
		path: 'scripts/gen-luci-wrapper.js',
		sha256: sha256(gatePath),
		gitBlob: 'bd100a47b08a2ea3025e371b09a3ba5b1c70b4eb',
		lines: { regexDerivationAndParityGate: '36-127' }
	},
	{
		path: 'scripts/gen-all.sh',
		sha256: sha256(genAllPath),
		gitBlob: '797c9fc3f78eda5bc86c2c140b05f1344152bf67',
		lines: { generatorAndGateWorkflow: '1-17' }
	},
	{
		path: 'scripts/z3-verify.py',
		sha256: sha256(z3Path),
		gitBlob: '268cfbf5b3068e123b5ec0719af5ad80b4f0b6a1',
		lines: { manuallyMaintainedPrefixMirror: '70-100,250-263' }
	},
	{
		path: 'docs/developer/z3-verification.md',
		sha256: sha256(z3DocPath),
		gitBlob: '089a212d389b9e93525f3f69eb43c3a316b4975a',
		lines: { documentedModelGapAndUtf16Boundary: '77-96,165-179' }
	},
	{
		path: 'AGENTS.md',
		sha256: sha256(path.join(sourceRoot, 'AGENTS.md')),
		gitBlob: '379180ebcef3e28653667444e659643f18651961',
		lines: { classifySpecAndGeneratorInstructions: '1-20' }
	},
	{
		path: 'docs/developer/contributing.md',
		sha256: sha256(path.join(sourceRoot, 'docs/developer/contributing.md')),
		gitBlob: 'af19d5000946bb7639464f2ddec1da9882054a31',
		lines: { singleSourceOfTruth: '103-126', tabsAndWorkflow: '10-34' }
	}
];

const report = {
	artifact: 'regexproof-653-native-diagnostic',
	classification: 'finite native diagnostic; no universal theorem or solver witness',
	issue653: {
		command: 'gh issue view 653 --repo lucas-albers-lz4/regexproof --json number,title,body,state,url',
		state: 'OPEN',
		title: 'Plan: one-consumer Rocq feasibility pilot for fwlive prefix guard',
		url: 'https://github.com/lucas-albers-lz4/regexproof/issues/653',
		constraintsObserved: 'This artifact covers the bounded source inventory and actual-Node finite diagnostic only. It makes no proof-feasibility, trusted-base, solver-witness, or universal-theorem claim.'
	},
	sourceSnapshot: {
		origin: 'fwlive origin/master',
		commit: commit,
		sourceRoot: sourceRoot,
		sourceRootMode: process.env.SOURCE_ROOT ? 'SOURCE_ROOT environment override' : 'adjacent source/ archive',
		commitReadMethod: sourceCommit.method,
		snapshotCommands: process.env.SOURCE_ROOT ? ['Set SOURCE_ROOT to a fwlive checkout at the pinned commit.'] : [
			'git fetch origin master',
			'git archive --format=tar origin/master | tar -xf - -C /tmp/regexproof-653-luna',
			'git rev-parse origin/master > /tmp/regexproof-653-luna/source-commit.txt',
			'extracted tree moved into source/ and made read-only'
		],
		readOnlyTree: isReadOnlyTree(sourceRoot)
	},
	pinnedLoadGuards: {
		expectedCommit: expectedCommit,
		expectedCoreSha256: expectedCoreSha256,
		expectedLuciSha256: expectedLuciSha256,
		observedCommit: commit,
		observedCoreSha256: coreSha256,
		observedLuciSha256: luciSha256,
		allVerifiedBeforeModuleLoad: true
	},
	reproduction: {
		command: 'node /tmp/regexproof-653-luna/regexproof-653-native.js > /tmp/regexproof-653-luna/regexproof-653-native.json',
		sourceRootOverride: 'SOURCE_ROOT=/absolute/path/to/fwlive',
		runtime: process.version,
		platform: process.platform,
		architecture: process.arch,
		unicodeVersion: process.versions.unicode,
		icuVersion: process.versions.icu,
		v8Version: process.versions.v8,
		scriptSha256: sha256(__filename)
	},
	regex: {
		name: 'NON_FIREWALL_PREFIX',
		source: actual.source,
		flags: actual.flags,
		unicodeMode: actual.unicode,
		multilineMode: actual.multiline,
		globalMode: actual.global,
		stickyMode: actual.sticky,
		specPrefixes: prefixes,
		hyphenContinuation: core.CLASSIFY_SPEC.nonFirewallPrefixHyphenContinuation,
		coreSpecAndRegexDerivedSourceCheck: true,
		luciSpecEqualToCore: true,
		coreAndLuciRegexSourceFlagsEqual: true
	},
	consumerBoundary: {
		core: 'isFirewallEvent: normalizeNetfilterMessage((entry && entry.msg) || ""), then classifyTrim using CLASSIFY_SPEC.trimWhitespace, then NON_FIREWALL_PREFIX.test(msg), core/fwlive-log.js:400-407',
		luci: 'log.isFirewallEvent: normalizeNetfilterMessage((entry && entry.msg) || ""), then classifyTrim using CLASSIFY_SPEC.trimWhitespace, then NON_FIREWALL_PREFIX.test(msg), fwlive log.js:483-486; status view callsite at view/status/fwlive.js:1177',
		inputDomain: 'JavaScript strings measured as UTF-16 code units; no ASCII-only or maximum-length guard is present at this consumer. The probe preserves NUL, isolated surrogates, and supplementary characters.',
		preGuardTransforms: 'normalization may insert one ASCII space before the first exact-case glue key; classifyTrim removes only space, tab, LF, CR, NBSP from either end. The diagnostic applies the actual core normalizer and reproduces the small classifyTrim loop from the pinned source.',
		invocations: 'core.filterLogEntries and core.statsLogEntries call isFirewallEvent; LuCI status view calls log.isFirewallEvent.'
	},
	sourceInventory: sourceInventory,
	finiteNativeCases: results,
	mutationControls: mutations,
	limits: [
		'Examples are a finite diagnostic corpus, not a universal claim over all JavaScript strings.',
	'The native runs use the installed Node ECMAScript RegExp engine; no solver, Z3 model, Rocq proof, or solver-generated witness is included.',
	'The core/LuCI equality checks here cover the loaded CLASSIFY_SPEC values and the NON_FIREWALL_PREFIX source and flags at this pinned snapshot; they are not a universal source-to-model theorem.'
	]
};

process.stdout.write(JSON.stringify(report, null, 2) + '\n');
