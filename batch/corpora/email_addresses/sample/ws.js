'use strict';

// Minimal email-addresses whitespace-normalize sample (Wave 3 / #115).
function collapse(s) {
    return s.replace(/([ \t]|\r\n)+/g, ' ').replace(/^\s*/, '').replace(/\s*$/, '');
}

function strip(s) {
    return s.replace(/\s+/g, '');
}

module.exports = { collapse, strip };
