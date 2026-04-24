#!/usr/bin/env python3
import glob
import re
from pathlib import Path

# Path to the footer component
footer_file = Path('components/footer')

# Read the footer content
footer_content = footer_file.read_text()

# Regex to match the existing footer block from <footer class="footer"> through </footer>
footer_block_pattern = re.compile(
    r'<footer class="footer">.*?</footer>\s*',
    re.DOTALL,
)

# Find all HTML files in the root directory
html_files = glob.glob('*.html')

for html_file in html_files:
    path = Path(html_file)
    content = path.read_text()

    if footer_block_pattern.search(content):
        new_content = footer_block_pattern.sub(footer_content + '\n\n', content, count=1)
        path.write_text(new_content)
        print(f'Updated {html_file}')
    else:
        print(f'No footer block found in {html_file}')

print('Footer inclusion complete.')
