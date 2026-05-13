#!/usr/bin/env bash
# Build a sandbox directory containing only the premises a peer reviewer
# needs to see, with the audit's conclusion-bearing sections stripped.
#
# Usage:   scripts/prepare-review.sh <audit-slug> [round-number]
# Example: scripts/prepare-review.sh 2026-05-13-casimir-energy-budget 1
#
# Prints the sandbox path on the LAST line of stdout so it can be captured
# by the orchestrator.

set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "usage: $0 <audit-slug> [round-number]" >&2
  exit 1
fi

SLUG="$1"
ROUND="${2:-1}"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AUDIT_DIR="$ROOT/audits/$SLUG"

if [ ! -d "$AUDIT_DIR" ]; then
  echo "error: audit directory not found: $AUDIT_DIR" >&2
  exit 1
fi

if [ ! -f "$AUDIT_DIR/README.md" ] || [ ! -f "$AUDIT_DIR/audit.py" ]; then
  echo "error: audit must have both README.md and audit.py" >&2
  exit 1
fi

# Prefer the project venv's Python; fall back to system.
PY="$ROOT/.venv/bin/python"
[ -x "$PY" ] || PY="/usr/bin/python3"

TS="$(date -u +%Y%m%dT%H%M%SZ)"
SANDBOX="${TMPDIR:-/tmp}/physicsos-review-${SLUG}-r${ROUND}-${TS}"
mkdir -p "$SANDBOX" "$SANDBOX/_reports" "$SANDBOX/prompts"

echo "[prepare-review] sandbox: $SANDBOX" >&2

# --- Copy protocol docs ---------------------------------------------------
cp "$ROOT/CLAUDE.md" "$SANDBOX/CLAUDE.md"
cp "$ROOT/AGENTS.md" "$SANDBOX/AGENTS.md"
cp "$ROOT/audits/README.md" "$SANDBOX/audits_README.md"
cp "$ROOT/papers/README.md" "$SANDBOX/papers_README.md"
cp "$ROOT/claims/README.md" "$SANDBOX/claims_README.md"

# --- Strip the audit README to premises only ------------------------------
STRIP_REPORT="$(
  "$PY" "$ROOT/scripts/_strip_audit_readme.py" \
    "$AUDIT_DIR/README.md" \
    "$ROOT" \
    "$SANDBOX/audit_premises_README.md"
)"

# --- Copy the audit script verbatim ---------------------------------------
cp "$AUDIT_DIR/audit.py" "$SANDBOX/audit_script.py"

# --- Run the script and capture raw output --------------------------------
echo "[prepare-review] running audit.py to capture raw output..." >&2
if ! ( cd "$ROOT" && "$PY" "$AUDIT_DIR/audit.py" ) > "$SANDBOX/audit_raw_output.txt" 2>&1; then
  echo "[prepare-review] WARNING: audit.py exited non-zero; raw output captured anyway" >&2
fi

# --- Extract claim file path from audit frontmatter -----------------------
CLAIM_REL="$(
  "$PY" - "$AUDIT_DIR/README.md" <<'PY'
import re, sys
text = open(sys.argv[1]).read()
m = re.search(r"^claim:\s*(.+?)\s*$", text, re.MULTILINE)
print(m.group(1) if m else "")
PY
)"

if [ -n "$CLAIM_REL" ]; then
  # Resolve relative to the audit directory.
  CLAIM_ABS="$(cd "$AUDIT_DIR" && cd "$(dirname "$CLAIM_REL")" 2>/dev/null && pwd)/$(basename "$CLAIM_REL")" || true
  if [ -f "$CLAIM_ABS" ]; then
    "$PY" "$ROOT/scripts/_strip_claim_file.py" "$CLAIM_ABS" "$SANDBOX/claim_statement_only.md"
  fi
fi

# --- Generate per-role prompts and the manifest via Python ----------------
"$PY" "$ROOT/scripts/_build_review_manifest.py" \
  --sandbox "$SANDBOX" \
  --repo-root "$ROOT" \
  --audit-slug "$SLUG" \
  --round "$ROUND" \
  --timestamp "$TS" \
  --strip-report "$STRIP_REPORT"

echo "[prepare-review] manifest:    $SANDBOX/manifest.json" >&2
echo "[prepare-review] reports dir: $SANDBOX/_reports"       >&2
echo "[prepare-review] prompts dir: $SANDBOX/prompts"        >&2

# Print sandbox path on the LAST line of stdout for capture.
echo "$SANDBOX"
