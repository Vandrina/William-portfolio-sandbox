#!/usr/bin/env python3
import json
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print('Pillow is required to run this script. Install it with: pip install Pillow')
    raise

root = Path(__file__).resolve().parent
images_root = root / 'images'
thumbs_root = root / 'thumbnails'
manifest_path = root / 'data' / 'manifest.json'

image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}

manifest = []

for image_path in sorted(images_root.rglob('*')):
    if not image_path.is_file():
        continue
    if image_path.suffix.lower() not in image_extensions:
        continue
    if image_path.name == '.DS_Store':
        continue

    relative_path = image_path.relative_to(root)
    thumb_path = thumbs_root / image_path.relative_to(images_root)

    if not thumb_path.exists():
        print(f'WARNING: thumbnail not found for {image_path} -> {thumb_path}')
        continue

    with Image.open(image_path) as img:
        full_width, full_height = img.size
    with Image.open(thumb_path) as img:
        thumb_width, thumb_height = img.size

    discipline = image_path.parent.name
    manifest.append({
        'file': str(relative_path).replace('\\', '/'),
        'thumbnail': str(thumb_path.relative_to(root)).replace('\\', '/'),
        'width': full_width,
        'height': full_height,
        'thumbWidth': thumb_width,
        'thumbHeight': thumb_height,
        'aspectRatio': round(full_width / full_height, 4),
        'thumbAspectRatio': round(thumb_width / thumb_height, 4),
        'discipline': discipline,
        'clients': [],
        'keywords': [],
        'sort': 999,
    })

manifest_path.parent.mkdir(parents=True, exist_ok=True)
with manifest_path.open('w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2)

print(f'Wrote {len(manifest)} items to {manifest_path}')