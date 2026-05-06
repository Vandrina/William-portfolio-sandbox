#!/bin/bash

# Directory paths
LIVE="/Users/jessewhitaker/Desktop/Work/Live Sites/William-portfolio"
SANDBOX="/Users/jessewhitaker/Desktop/Work/Live Sites/William-portfolio-sandbox"

# Files to compare
FILES=(
    "_redirects"
    "404.html"
    "about.html"
    "contact.html"
    "gallery.html"
    "index.html"
    "privacy.html"
    "shop.html"
    "terms.html"
    "style.css"
    "data/manifest.json"
)

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "Comparing files between Live and Sandbox..."
echo "==========================================="
echo ""

DIFF_COUNT=0
MISSING_COUNT=0

for file in "${FILES[@]}"; do
    LIVE_FILE="$LIVE/$file"
    SANDBOX_FILE="$SANDBOX/$file"
    
    # Check if files exist
    if [[ ! -f "$LIVE_FILE" ]]; then
        echo -e "${YELLOW}⚠ Missing in Live:${NC} $file"
        ((MISSING_COUNT++))
        continue
    fi
    
    if [[ ! -f "$SANDBOX_FILE" ]]; then
        echo -e "${YELLOW}⚠ Missing in Sandbox:${NC} $file"
        ((MISSING_COUNT++))
        continue
    fi
    
    # Compare files
    if ! diff -q "$LIVE_FILE" "$SANDBOX_FILE" > /dev/null 2>&1; then
        echo -e "${RED}✗ Different:${NC} $file"
        ((DIFF_COUNT++))
        
        # Show detailed diff (optional - uncomment to see full diff)
        # echo "  Differences:"
        # diff -u "$LIVE_FILE" "$SANDBOX_FILE" | head -20
        # echo ""
    else
        echo -e "${GREEN}✓ Identical:${NC} $file"
    fi
done

echo ""
echo "==========================================="
echo "Summary:"
echo "  Different files: $DIFF_COUNT"
echo "  Missing files: $MISSING_COUNT"

if [[ $DIFF_COUNT -gt 0 ]]; then
    echo ""
    echo "To see detailed differences for a file, run:"
    echo "  diff -u \"$LIVE/<filename>\" \"$SANDBOX/<filename>\""
fi
