#!/usr/bin/env bash
# Sync reviewer reports out of a sandbox into the live repo, write a copy
# of the sandbox manifest alongside them, and delete the sandbox.
#
# Usage: scripts/finalize-review.sh <sandbox-path> <audit-slug> [round-number]

set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "usage: $0 <sandbox-path> <audit-slug> [round-number]" >&2
  exit 1
fi

SANDBOX="$1"
SLUG="$2"
ROUND="${3:-1}"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AUDIT_DIR="$ROOT/audits/$SLUG"
ROUND_DIR="$AUDIT_DIR/round${ROUND}"

if [ ! -d "$SANDBOX" ]; then
  echo "error: sandbox not found: $SANDBOX" >&2
  exit 1
fi

if [ ! -d "$AUDIT_DIR" ]; then
  echo "error: audit directory not found: $AUDIT_DIR" >&2
  exit 1
fi

REPORTS_DIR="$SANDBOX/_reports"
EXPECTED_REPORTS=(devil_advocate.md source_fidelity.md reproducibility.md)

# Validate every expected report exists and is non-trivial (> 200 bytes).
missing=()
for r in "${EXPECTED_REPORTS[@]}"; do
  if [ ! -f "$REPORTS_DIR/$r" ]; then
    missing+=("$r (file does not exist)")
  else
    size=$(stat -f %z "$REPORTS_DIR/$r" 2>/dev/null || stat -c %s "$REPORTS_DIR/$r")
    if [ "$size" -lt 200 ]; then
      missing+=("$r (suspiciously small: ${size} bytes)")
    fi
  fi
done

if [ "${#missing[@]}" -gt 0 ]; then
  echo "error: review incomplete — the following reports are missing or trivially small:" >&2
  printf '  - %s\n' "${missing[@]}" >&2
  echo "" >&2
  echo "sandbox preserved at: $SANDBOX" >&2
  exit 1
fi

mkdir -p "$ROUND_DIR"

# Copy reports.
for r in "${EXPECTED_REPORTS[@]}"; do
  cp "$REPORTS_DIR/$r" "$ROUND_DIR/$r"
done

# Copy manifest.
cp "$SANDBOX/manifest.json" "$ROUND_DIR/_sandbox_manifest.json"

echo "[finalize-review] reports landed in: $ROUND_DIR" >&2
ls -la "$ROUND_DIR" >&2

# Delete the sandbox now that everything is captured.
rm -rf "$SANDBOX"
echo "[finalize-review] sandbox deleted: $SANDBOX" >&2

echo
echo "Next steps:"
echo "  1. Read $ROUND_DIR/*.md"
echo "  2. Address each finding (revise audit or document counter-argument)"
echo "  3. Update audit frontmatter:"
echo "       peer_reviewed: $(date -u +%Y-%m-%d)"
echo "       reviewer_verdicts:"
echo "         devil_advocate:  <verdict>"
echo "         source_fidelity: <verdict>"
echo "         reproducibility: <verdict>"
echo "  4. Commit the round."
