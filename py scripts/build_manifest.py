import os
import json

# Map source folder names to clean slug names
folder_map = {
    "2D animation": "2d-animation",
    "3d animation": "3d-animation",
    "backgrounds": "backgrounds",
    "books": "books",
    "concept_art": "concept-art",
    "NFTs": "nft",
    "illustration": "illustration",
    "toy design": "toy-design"
}

source_base = "/Users/jessewhitaker/Desktop/WilliamMcGuire_Business/william_images_web_ready"
image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

manifest = []

for folder_name, discipline_slug in folder_map.items():
    folder_path = os.path.join(source_base, folder_name)
    if not os.path.exists(folder_path):
        print(f"WARNING: folder not found: {folder_path}")
        continue
    for filename in sorted(os.listdir(folder_path)):
        ext = os.path.splitext(filename)[1].lower()
        if ext in image_extensions:
            manifest.append({
                "file": f"images/{discipline_slug}/{filename}",
                "discipline": discipline_slug,
                "clients": [],
                "keywords": []
            })

with open("data/manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print(f"Done. {len(manifest)} images written to data/manifest.json")
