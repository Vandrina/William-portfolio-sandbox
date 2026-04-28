#!/bin/bash
# generate_placeholders.sh
# Creates 20px-wide placeholder images for blur-up effect
# Reads from thumbnails/, writes to placeholders/
# Run from ~/Documents/William-portfolio

SOURCE="thumbnails"
DEST="placeholders"

echo "Generating blur-up placeholders from thumbnails..."

find "$SOURCE" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) | while read -r file; do

  relative="${file#$SOURCE/}"
  dest_file="$DEST/$relative"
  dest_dir=$(dirname "$dest_file")

  mkdir -p "$dest_dir"

  if [ -f "$dest_file" ]; then
    continue
  fi

  magick "$file" \
    -resize "20x20>" \
    -quality 60 \
    "$dest_file"

  if [ $? -eq 0 ]; then
    echo "✓ $relative"
  else
    echo "✗ ERROR: $relative"
  fi

done

echo ""
echo "Done. Check placeholders/ folder."
