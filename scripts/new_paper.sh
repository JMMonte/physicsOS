#!/usr/bin/env bash
# Scaffold a new paper note.
# Usage:  scripts/new_paper.sh <year> <first-author-lastname> <slug>
# Example: scripts/new_paper.sh 2023 maldacena eternal-traversable-wormhole

set -euo pipefail

if [ "$#" -ne 3 ]; then
  echo "usage: $0 <year> <first-author-lastname> <slug>" >&2
  exit 1
fi

YEAR="$1"
AUTHOR="$2"
SLUG="$3"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATE="$ROOT/papers/_template.md"
DEST="$ROOT/papers/${YEAR}-${AUTHOR}-${SLUG}.md"

if [ -e "$DEST" ]; then
  echo "error: $DEST already exists" >&2
  exit 1
fi

cp "$TEMPLATE" "$DEST"
echo "created: $DEST"
echo "next: open it, fill the frontmatter, and read the paper."
