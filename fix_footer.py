import glob
import re

new_footer_logo = '''<div class="footer-logo-text"
                    style="display:flex;align-items:center;gap:4px;font-family:'Playfair Display',serif;font-size:1.6rem;line-height:1;margin-bottom:10px;">
                    <span style="color:var(--amber-light);font-weight:800;font-style:italic;">Uai</span>
                    <span style="color:white;font-weight:800;font-style:italic;">Turismo</span>
                </div>'''

pattern = re.compile(r'<div class="footer-logo-text".*?</div>', re.DOTALL)

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if pattern.search(content):
        new_content = pattern.sub(new_footer_logo, content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Fixed footer in', f)
