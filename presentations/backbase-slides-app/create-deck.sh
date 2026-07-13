#!/bin/bash
#
# create-deck.sh — Scaffold a new Backbase presentation deck
#
# Usage:
#   ./create-deck.sh <deck-name> ["Deck Title"]
#
# Example:
#   ./create-deck.sh q1-review "Backbase — Q1 2026 Review"
#
# Creates:
#   ../deck-name/
#   ├── index.html    (loads shared engine)
#   ├── slides.js     (starter content)
#   └── images/       (deck-specific images)

set -e

if [ -z "$1" ]; then
  echo "Usage: ./create-deck.sh <deck-name> [\"Deck Title\"]"
  echo ""
  echo "Example: ./create-deck.sh q1-review \"Backbase — Q1 Review\""
  exit 1
fi

DECK_NAME="$1"
DECK_TITLE="${2:-Backbase — New Presentation}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DECK_DIR="$SCRIPT_DIR/../$DECK_NAME"

if [ -d "$DECK_DIR" ]; then
  echo "Error: Directory $DECK_DIR already exists"
  exit 1
fi

# Create deck structure
mkdir -p "$DECK_DIR/images"

# Copy index.html template and replace title
sed "s/DECK_TITLE/$DECK_TITLE/g" "$SCRIPT_DIR/deck-template.html" > "$DECK_DIR/index.html"

# Create starter slides.js
cat > "$DECK_DIR/slides.js" << 'SLIDES_EOF'
window.BB_SHARED_ASSETS = '../backbase-slides-app';

const SPEAKER_NOTES = {};

const SLIDES = [
  // ── COVER ──
  { layout: 'cover-color-block', label: 'BACKBASE', title: 'Presentation\nTitle', date: 'March 2026' },

  // ── AGENDA ──
  { layout: 'toc', label: 'CONTENTS', title: 'Agenda', numbered: true, items: [
    'Topic 1',
    'Topic 2',
    'Topic 3'
  ]},

  // ── SECTION 1 ──
  { layout: 'chapter-numbered', theme: 'navy', number: '01', label: 'SECTION', title: 'First Section', subtitle: 'Section description' },
  { layout: 'content-standard', theme: 'light', label: 'TOPIC', title: 'Slide Title', subtitle: 'Supporting text', body: '<p>Content goes here</p>' },

  // ── THANK YOU ──
  { layout: 'thank-you' }
];
SLIDES_EOF

echo ""
echo "  Created deck: $DECK_DIR"
echo ""
echo "  Files:"
echo "    index.html   — presentation viewer (loads shared engine)"
echo "    slides.js    — slide content (edit this file)"
echo "    images/      — deck-specific images"
echo ""
echo "  To preview:"
echo "    npx serve $(dirname "$DECK_DIR") -l 3000"
echo "    Open http://localhost:3000/$DECK_NAME/"
echo ""
