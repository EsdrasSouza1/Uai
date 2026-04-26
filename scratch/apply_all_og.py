import os
import glob
import re

html_files = glob.glob('*.html') + glob.glob('bio/*.html')
new_og_image = 'https://www.uaitur.com/foto/Logo%20_uai%20TURISMO_%20na%20Praia%20Tropical.png'

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace any existing og:image with the new one
    new_content = re.sub(
        r'<meta\s+property="og:image"\s+content="[^"]+">',
        f'<meta property="og:image" content="{new_og_image}">',
        content
    )
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {fpath}")
    else:
        print(f"No changes in {fpath}")
