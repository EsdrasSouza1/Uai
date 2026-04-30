import os
import glob
import re

favicon_code = """
    <!-- Favicon -->
    <link rel="icon" type="image/png" href="foto/logoo.png">
    <link rel="apple-touch-icon" href="foto/logoo.png">
"""

base_dir = r"c:\Users\nerds\OneDrive\Área de Trabalho\Uai"
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'rel="icon"' not in content:
        # Check if there's a title tag
        if '<title>' in content:
            # Let's insert the favicon right after the </title> tag
            new_content = re.sub(r'(</title>)', r'\1' + favicon_code, content, count=1)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added favicon to {filepath}")
        else:
            print(f"No <title> found in {filepath}")
    else:
        print(f"Favicon already exists in {filepath}")

print("Done.")
