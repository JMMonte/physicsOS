#!/usr/bin/env bash
# Scaffold a new claim file.
# Usage:  scripts/new_claim.sh <slug>
# Example: scripts/new_claim.sh cosmological-constant-positive

set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: $0 <slug>" >&2
  exit 1
fi

SLUG="$1"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATE="$ROOT/claims/_template.md"
DEST="$ROOT/claims/${SLUG}.md"

if [ -e "$DEST" ]; then
  echo "error: $DEST already exists" >&2
  exit 1
fi

cp "$TEMPLATE" "$DEST"
echo "created: $DEST"
echo "next: write the precise statement and seed the evidence ledger."
