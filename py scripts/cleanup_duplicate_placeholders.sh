#!/bin/bash
# cleanup_duplicate_placeholders.sh
# Removes placeholder files that have _thumbnail in the filename
# (These are duplicates created by the broken script)

PLACEHOLDERS="gallery-blur-placeholders"

echo "Finding duplicate placeholders with _thumbnail in filename..."

find "$PLACEHOLDERS" -type f -name "*_thumbnail.*" | while read -r file; do
  echo "Deleting: $file"
  rm "$file"
done

echo ""
echo "Cleanup complete!"
echo "Run 'find gallery-blur-placeholders -name \"*_thumbnail.*\"' to verify."
