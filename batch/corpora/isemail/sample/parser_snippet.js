'use strict';

// Minimal isemail regex sample (Wave 3 / #115).
const internals = {
    regex: {
        ipV4: /\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$/,
        ipV6: /^[a-fA-F\d]{0,4}$/,
        nonASCII: /[^\x00-\x7f]/,
    },
};

module.exports = internals;
