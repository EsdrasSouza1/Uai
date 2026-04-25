import os
import re

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove all instances of <div class="deco-container">...</div>
        new_content = re.sub(r'<div class="deco-container">.*?</div>', '', content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Removed drawings from {file}')

print('Done removing all background drawings.')
