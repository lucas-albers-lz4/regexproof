"""Pinned detect-secrets-style Python plugin patterns for Phase 5 batch.

Not a full clone of Yelp/detect-secrets — a minimal dialect exercise corpus.
"""

import re

# Classic AWS access key id shape (simplified)
AWS_ACCESS_KEY = re.compile(r"AKIA[0-9A-Z]{16}")

# Generic high-entropy-ish token (for extract; may be unencodable depending on flags)
GITHUB_TOKEN = re.compile(r"ghp_[0-9A-Za-z]{36}")

# Anchored validator-style email-ish (intent/usage demos)
EMAIL_LIKE = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

# Hostname claim with overly broad pattern (intent mismatch candidate)
HOSTNAME_PATTERN = re.compile(r".*")
