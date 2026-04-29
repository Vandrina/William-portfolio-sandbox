#!/usr/bin/env python3
import glob
import re
from pathlib import Path

# Path to the navigation component
nav_file = Path('components/navigation.html')

# Read the navigation content
nav_content = nav_file.read_text()

# Regex to match the existing nav block
nav_block_pattern = re.compile(
    r'<div class="nav-wrap">.*?</div>\s*</div>',
    re.DOTALL,
)

# Find all HTML files in the root directory
html_files = glob.glob('*.html')

for html_file in html_files:
    path = Path(html_file)
    content = path.read_text()

    if nav_block_pattern.search(content):
        new_content = nav_block_pattern.sub(nav_content + '\n\n', content, count=1)
        path.write_text(new_content)
        print(f'Updated {html_file}')
    else:
        print(f'No navigation block found in {html_file}')

print('Navigation update complete.')
