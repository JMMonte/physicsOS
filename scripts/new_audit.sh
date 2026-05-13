#!/usr/bin/env bash
# Scaffold a new audit directory.
# Usage:  scripts/new_audit.sh <slug>
# Example: scripts/new_audit.sh blackbody-peak-wavelength

set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: $0 <slug>" >&2
  exit 1
fi

SLUG="$1"
DATE="$(date -u +%Y-%m-%d)"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/audits/_template"
DEST="$ROOT/audits/${DATE}-${SLUG}"

if [ -e "$DEST" ]; then
  echo "error: $DEST already exists" >&2
  exit 1
fi

cp -R "$SRC" "$DEST"
echo "created: $DEST"
echo "next: edit README.md and audit.py."
