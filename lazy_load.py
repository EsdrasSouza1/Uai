import glob
import re

files = glob.glob('*.html')
for fn in files:
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            html = f.read()
            
        old_html = html
        def replacer(m):
            img_tag = m.group(0)
            # Skip if already has loading=
            if 'loading=' in img_tag:
                return img_tag
                
            # Naive check to see if it's the hero carousel in index.html
            context_before = html[max(0, m.start()-50):m.start()]
            if 'hero-carousel-slide' in context_before or 'heroRight' in context_before:
                return img_tag
                
            # Check if it's a generic logo or something we want immediate (skip)
            if 'logoo.png' in img_tag or 'cadastur' in img_tag.lower():
                return img_tag
                
            # Otherwise, add loading="lazy"
            return img_tag.replace('<img ', '<img loading="lazy" ')

        html = re.sub(r'<img\s+[^>]+>', replacer, html)
        
        if html != old_html:
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'Added lazy loading to {fn}')
    except Exception as e:
        print(f"Failed {fn}: {e}")
