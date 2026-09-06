# Vendored ground-truth fixture: fwlive normalize_log_prefix().
#
# Source: fwlive repo, openwrt-feed/luci-app-fwlive/root/usr/libexec/rpcd/fwlive
# Pinned at fwlive@a3d6c5421bf0a1df96d6c6caddda144be52283b3 (2026-09-06).
# Extracted verbatim (tabs preserved); do NOT hand-edit the function body.
# Refresh: re-extract with
#   sed -n '/^normalize_log_prefix/,/^}/p' <fwlive>/openwrt-feed/.../rpcd/fwlive
# and update the pin above. test_df_shipped_function_replays_under_dash
# fails on drift wherever the live checkout exists (local dev); CI replays
# THESE bytes under dash + BusyBox sed.
normalize_log_prefix() {
	printf '%s' "$1" | sed 's/[[:space:]:]*$//'
}
