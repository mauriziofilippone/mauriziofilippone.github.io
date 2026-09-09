#!/usr/bin/env bash
# =============================================================================
# update_pubs.sh
# 
# Run from the ROOT of the Jekyll site (the directory containing _config.yml).
# 
# What it does:
#   1. Runs pubsFromBib.py to parse _bibliography/*.bib and generate
#      _publications/*.md files for the Jekyll site.
#   2. (Optional) Compiles the LaTeX CV PDF in webpage_up_to_2026/pages/utilities/
#      if pdflatex is available.
#
# Dependencies:
#   - Python 3 with pybtex  (pip install pybtex)
#   - pdflatex (optional, for CV PDF compilation)
#
# Usage:
#   chmod +x scripts/update_pubs.sh
#   ./scripts/update_pubs.sh
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "=== Site root: $SITE_ROOT ==="

# ---------------------------------------------------------------------------
# Step 1: Check _bibliography/ exists
# ---------------------------------------------------------------------------
BIB_DIR="$SITE_ROOT/_bibliography"
if [ ! -d "$BIB_DIR" ]; then
  echo "ERROR: _bibliography/ not found at $BIB_DIR"
  echo "Create the directory and copy your .bib files there:"
  echo "  mkdir -p _bibliography"
  echo "  cp webpage_up_to_2026/pages/utilities/journals.bib _bibliography/"
  echo "  cp webpage_up_to_2026/pages/utilities/conferences.bib _bibliography/"
  echo "  cp webpage_up_to_2026/pages/utilities/discussions.bib _bibliography/"
  echo "  cp webpage_up_to_2026/pages/utilities/theses.bib _bibliography/"
  exit 1
fi

echo "Found _bibliography/:"
ls "$BIB_DIR"/*.bib 2>/dev/null || echo "  (no .bib files yet)"

# ---------------------------------------------------------------------------
# Step 2: Run pubsFromBib.py
# ---------------------------------------------------------------------------
echo ""
echo "=== Generating _publications/ markdown files ==="
cd "$SITE_ROOT/markdown_generator"
python3 pubsFromBib.py
echo ""
echo "Number of .md files in _publications/:"
ls "$SITE_ROOT/_publications/"*.md 2>/dev/null | wc -l

# ---------------------------------------------------------------------------
# Step 3: (Optional) Compile LaTeX CV
# ---------------------------------------------------------------------------
echo ""
echo "=== Optional: LaTeX CV compilation ==="
if command -v pdflatex &>/dev/null; then
  CV_DIR="$SITE_ROOT/webpage_up_to_2026/pages/utilities"
  if [ -f "$CV_DIR/cv_en.tex" ]; then
    echo "Compiling cv_en.tex ..."
    (cd "$CV_DIR" && pdflatex -interaction=nonstopmode cv_en.tex && pdflatex -interaction=nonstopmode cv_en.tex)
    # Copy compiled PDF to files/ so Jekyll can serve it
    mkdir -p "$SITE_ROOT/files"
    cp "$CV_DIR/cv_en.pdf" "$SITE_ROOT/files/"
    echo "Copied cv_en.pdf to files/"
  fi
  if [ -f "$CV_DIR/short_cv.tex" ]; then
    echo "Compiling short_cv.tex ..."
    (cd "$CV_DIR" && pdflatex -interaction=nonstopmode short_cv.tex && pdflatex -interaction=nonstopmode short_cv.tex)
    mkdir -p "$SITE_ROOT/files"
    cp "$CV_DIR/short_cv.pdf" "$SITE_ROOT/files/"
    echo "Copied short_cv.pdf to files/"
  fi
else
  echo "pdflatex not found — skipping CV PDF compilation."
  echo "Run 'pdflatex cv_en.tex' in webpage_up_to_2026/pages/utilities/ manually."
fi

echo ""
echo "=== Done! ==="
echo "Commit the updated _publications/ (and files/*.pdf if compiled) to trigger a rebuild."
