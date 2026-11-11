#!/usr/bin/env bash
# Install Debian packages in GitHub Actions without depending on
# azure.archive.ubuntu.com DNS (hosted-runner flake: "Temporary failure
# resolving 'azure.archive.ubuntu.com'"). Rewrite that mirror to
# archive.ubuntu.com, skip busybox when busybox-static already provides it,
# and retry a short bounded number of times.
set -euo pipefail

usage() {
  echo "usage: $0 <apt-package>[=version] ..." >&2
  exit 2
}

rewrite_azure_mirrors() {
  local f
  shopt -s nullglob
  for f in /etc/apt/apt-mirrors.txt /etc/apt/sources.list \
           /etc/apt/sources.list.d/*.list /etc/apt/sources.list.d/*.sources; do
    [[ -e "$f" ]] || continue
    if grep -Fq 'azure.archive.ubuntu.com' "$f"; then
      sudo sed -i 's/azure[.]archive[.]ubuntu[.]com/archive.ubuntu.com/g' "$f"
    fi
  done
}

(( $# >= 1 )) || usage

need=()
for pkg in "$@"; do
  name="${pkg%%=*}"
  if [[ "$name" == busybox ]] \
      && command -v busybox >/dev/null 2>&1 \
      && busybox sed --help >/dev/null 2>&1; then
    echo "ci-apt-get: busybox already present at $(command -v busybox); skip apt"
    continue
  fi
  need+=("$pkg")
done

if (( ${#need[@]} == 0 )); then
  echo "ci-apt-get: nothing to install"
  exit 0
fi

rewrite_azure_mirrors

retry() {
  local n=0
  until "$@"; do
    n=$((n + 1))
    if (( n >= 3 )); then
      echo "ci-apt-get: giving up after ${n} attempts: $*" >&2
      return 1
    fi
    echo "ci-apt-get: retry ${n} after failure: $*"
    sleep $((n * 5))
    rewrite_azure_mirrors
  done
}

export DEBIAN_FRONTEND=noninteractive
retry sudo apt-get update -o Acquire::Retries=2
retry sudo apt-get install -y -o Acquire::Retries=2 "${need[@]}"
