#!/usr/bin/env python3
import glob
import re
from pathlib import Path

# Read the header component
header_template = Path('components/header').read_text()

# Patterns to extract from existing pages
title_pattern = re.compile(r'<title>(.*?)</title>')
html_tag_pattern = re.compile(r'<html[^>]*>')
stylesheet_pattern = re.compile(r'<link rel="stylesheet" href="([^"]+)">')
inline_style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)

# Pattern to replace (everything from DOCTYPE to end of nav-wrap)
header_block_pattern = re.compile(
    r'<!DOCTYPE html>.*?</div>\s*</div>',
    re.DOTALL
)

html_files = glob.glob('*.html')

for html_file in html_files:
    path = Path(html_file)
    page_name = path.stem
    content = path.read_text()
    
    # Extract existing values
    title_match = title_pattern.search(content)
    title = title_match.group(1) if title_match else f'{page_name.title()} — William McGuire'
    
    html_tag_match = html_tag_pattern.search(content)
    html_tag = html_tag_match.group(0) if html_tag_match else '<html lang="en">'
    
    stylesheet_match = stylesheet_pattern.search(content)
    stylesheet = stylesheet_match.group(1) if stylesheet_match else 'style.css'
    
    inline_style_match = inline_style_pattern.search(content)
    inline_styles = '\n  ' + inline_style_match.group(0) if inline_style_match else ''
    
    # Build customized header
    custom_header = header_template
    custom_header = custom_header.replace('[PAGE_TITLE]', title)
    custom_header = custom_header.replace('href="style.css"', f'href="{stylesheet}"')
    custom_header = custom_header.replace('[INLINE_STYLES]', inline_styles)
    custom_header = custom_header.replace('<html lang="en">', html_tag)
    
    # Add active class if needed
    if page_name in ['gallery', 'about', 'contact']:
        custom_header = custom_header.replace(
            f'href="{page_name}.html" class="nav-item"',
            f'href="{page_name}.html" class="nav-item active"'
        )
    
    # Replace the entire header block
    if header_block_pattern.search(content):
        new_content = header_block_pattern.sub(custom_header, content, count=1)
        path.write_text(new_content)
        print(f'✓ Updated {html_file}')
    else:
        print(f'⚠ Could not find header block in {html_file}')

print('\nHeader inclusion complete.')