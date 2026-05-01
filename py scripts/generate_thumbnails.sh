#!/bin/bash
# generate_thumbnails.sh
# Creates 600px-wide thumbnails from full-res originals using mogrify
# Run from ~/Documents/William-portfolio

SOURCE="/Users/jessewhitaker/Desktop/WilliamMcGuire_Business/full res jpg"
DEST="$(pwd)/thumbnails"

echo "Starting thumbnail generation..."

# Get all subdirectory names from source
find "$SOURCE" -mindepth 1 -maxdepth 1 -type d | while read -r folder; do
  dirname=$(basename "$folder")
  dest_folder="$DEST/$dirname"
  mkdir -p "$dest_folder"

  echo "Processing: $dirname"

  # Copy originals to destination folder first
  cp "$folder"/*.jpg "$dest_folder/" 2>/dev/null
  cp "$folder"/*.jpeg "$dest_folder/" 2>/dev/null
  cp "$folder"/*.png "$dest_folder/" 2>/dev/null

  # Run mogrify in place on the copies
  magick mogrify \
    -resize "600x600>" \
    -quality 80 \
    -intent Perceptual \
    "$dest_folder"/*.jpg 2>/dev/null

  echo "✓ Done: $dirname"
done

echo ""
echo "All done. Check thumbnails/ folder."
