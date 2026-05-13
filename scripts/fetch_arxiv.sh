#!/usr/bin/env bash
# Fetch arXiv metadata + abstract for a given arXiv ID.
# Usage:  scripts/fetch_arxiv.sh <arxiv-id>
# Example: scripts/fetch_arxiv.sh 2310.12345
# Example: scripts/fetch_arxiv.sh hep-th/0503158
#
# Rate-limit safe:
#   * Cross-process mutex via mkdir (portable; works on macOS without flock).
#   * Per-host minimum interval between requests (arXiv asks for >= 3s).
#   * curl retries on 429/5xx with backoff.
# Concurrent invocations queue politely instead of racing.

set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: $0 <arxiv-id>" >&2
  exit 1
fi

ID="$1"
URL="http://export.arxiv.org/api/query?id_list=${ID}"

# --- Throttle config ------------------------------------------------------
THROTTLE_DIR="${TMPDIR:-/tmp}/physicsos-arxiv-throttle"
LOCK_DIR="$THROTTLE_DIR/lock"
LAST_FILE="$THROTTLE_DIR/last_call"
MIN_INTERVAL_SEC=4          # arXiv's stated policy: 1 req / 3 s; pad to 4.
LOCK_TIMEOUT_SEC=120        # max time we'll wait for our turn.
mkdir -p "$THROTTLE_DIR"

# --- Acquire mutex (atomic mkdir; portable) -------------------------------
acquire_lock() {
  local waited=0
  while ! mkdir "$LOCK_DIR" 2>/dev/null; do
    sleep 1
    waited=$((waited + 1))
    if [ "$waited" -ge "$LOCK_TIMEOUT_SEC" ]; then
      # Stale lock? Force it. (Should be rare.)
      echo "fetch_arxiv: lock held >${LOCK_TIMEOUT_SEC}s; forcing." >&2
      rm -rf "$LOCK_DIR"
      mkdir "$LOCK_DIR"
      break
    fi
  done
}
release_lock() { rmdir "$LOCK_DIR" 2>/dev/null || true; }
trap release_lock EXIT INT TERM

acquire_lock

# Temp file for the response body — heredoc would clobber stdin if we
# tried to pipe curl into python alongside the script.
TMPRAW=$(mktemp -t physicsos-arxiv.XXXXXX)
cleanup() { rm -f "$TMPRAW"; release_lock; }
trap cleanup EXIT INT TERM

# --- Enforce min interval since last call ---------------------------------
now=$(date +%s)
if [ -f "$LAST_FILE" ]; then
  last=$(cat "$LAST_FILE" 2>/dev/null || echo 0)
  delta=$((now - last))
  if [ "$delta" -lt "$MIN_INTERVAL_SEC" ]; then
    wait=$((MIN_INTERVAL_SEC - delta))
    sleep "$wait"
  fi
fi
date +%s > "$LAST_FILE"

# --- Fetch with retry-on-429/5xx ------------------------------------------
PY="/usr/bin/python3"
[ -x "$PY" ] || PY="python3"

# --retry-all-errors makes --retry honour 429 too (curl >= 7.71.0).
curl -fsSL \
  --retry 4 \
  --retry-delay 5 \
  --retry-all-errors \
  --max-time 30 \
  -A "physicsOS/0.1 (fetch_arxiv.sh; mailto:joaommontenegro1@gmail.com)" \
  -o "$TMPRAW" \
  "$URL"

# --- Parse (regex-based; survives broken pyexpat) -------------------------
"$PY" - "$TMPRAW" <<'PY'
import re, sys, html

with open(sys.argv[1], "r", encoding="utf-8") as f:
    raw = f.read()

entry = re.search(r"<entry>(.*?)</entry>", raw, re.DOTALL)
if not entry:
    sys.exit("no <entry> in response — id may not exist")
e = entry.group(1)

def field(pattern):
    m = re.search(pattern, e, re.DOTALL)
    return html.unescape(" ".join(m.group(1).split())) if m else ""

title    = field(r"<title>(.*?)</title>")
summary  = field(r"<summary>(.*?)</summary>")
publish  = field(r"<published>(.*?)</published>")

primary = ""
m = re.search(r'<arxiv:primary_category[^>]*term="([^"]+)"', e)
if m: primary = m.group(1)

authors = [html.unescape(" ".join(n.split()))
           for n in re.findall(r"<author>\s*<name>(.*?)</name>", e, re.DOTALL)]

print(f"title:     {title}")
print(f"authors:   {', '.join(authors)}")
print(f"published: {publish}")
print(f"category:  {primary}")
print()
print("abstract:")
print(summary)
PY
