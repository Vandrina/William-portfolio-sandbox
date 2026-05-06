#!/bin/bash
# generate_missing_placeholders.sh
# Creates 20px-wide placeholder images for blur-up effect
# Reads from thumbnails/, writes to gallery-blur-placeholders/
# Strips _thumbnail from output filename to match original image names

SOURCE="thumbnails"
DEST="gallery-blur-placeholders"

echo "Generating blur-up placeholders from thumbnails..."

find "$SOURCE" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) | while read -r file; do

  relative="${file#$SOURCE/}"
  
  # Strip _thumbnail from the filename for the destination
  # Example: 001. Dragon_thumbnail.jpg -> 001. Dragon.jpg
  dest_relative=$(echo "$relative" | sed 's/_thumbnail\././')
  
  dest_file="$DEST/$dest_relative"
  dest_dir=$(dirname "$dest_file")

  mkdir -p "$dest_dir"

  # Skip if placeholder already exists
  if [ -f "$dest_file" ]; then
    continue
  fi

  magick "$file" \
    -resize "20x20>" \
    -quality 60 \
    "$dest_file"

  if [ $? -eq 0 ]; then
    echo "✓ $dest_relative"
  else
    echo "✗ ERROR: $dest_relative"
  fi

done

echo ""
echo "Done. Check gallery-blur-placeholders/ folder."
