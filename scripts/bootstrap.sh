#!/usr/bin/env bash
# Create the project Python venv at .venv/ and install requirements.txt.
# Idempotent: safe to re-run.
#
# Usage:
#   scripts/bootstrap.sh           # create/refresh .venv and install
#   scripts/bootstrap.sh --upgrade # also upgrade pinned packages within constraints

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Need Python 3.10+ for the modern stack (numpy 2 + astropy 6.1+).
# Skip brew python3.14 — its pyexpat is broken on macOS as of 2026-05.
# Prefer the highest working minor in the 3.10–3.13 range.
PY=""
for candidate in \
  /opt/homebrew/bin/python3.13 \
  /opt/homebrew/bin/python3.12 \
  /opt/homebrew/bin/python3.11 \
  /opt/homebrew/bin/python3.10 \
  /usr/local/bin/python3.13 \
  /usr/local/bin/python3.12 \
  /usr/local/bin/python3.11 \
  /usr/local/bin/python3.10 \
  python3.13 python3.12 python3.11 python3.10
do
  if command -v "$candidate" >/dev/null 2>&1; then
    if "$candidate" -c 'import xml.etree.ElementTree; xml.etree.ElementTree.fromstring("<a/>")' >/dev/null 2>&1; then
      PY="$candidate"
      break
    fi
  fi
done

if [ -z "$PY" ]; then
  echo "error: no working Python 3.10+ found." >&2
  echo "       install one via:  brew install python@3.13" >&2
  exit 1
fi

echo "[bootstrap] using $PY ($("$PY" --version))"

if [ ! -d ".venv" ]; then
  echo "[bootstrap] creating .venv"
  "$PY" -m venv .venv
else
  echo "[bootstrap] .venv exists, reusing"
fi

# shellcheck disable=SC1091
. .venv/bin/activate

pip install --upgrade pip --quiet

if [ "${1:-}" = "--upgrade" ]; then
  pip install --upgrade -r requirements.txt
else
  pip install -r requirements.txt
fi

echo
echo "[bootstrap] done. Activate with:"
echo "    source .venv/bin/activate"
echo
echo "Or invoke audits directly:"
echo "    .venv/bin/python audits/<date>-<slug>/audit.py"
