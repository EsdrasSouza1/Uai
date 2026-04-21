import re, os

# Fix 1: Add missing 4th dot to pages that have 4 slides but only 3 dots
# The pattern that failed had a different dot HTML format. Let's inspect and fix directly.

DOT_PAGES = [
    'passeio-maragogi.html',
    'passeio-porto-de-galinhas.html',
    'passeio-milagres.html',
]

NEW_DOT = '<button class="pcd" data-i="3" aria-label="Foto 4"></button>'

for page in DOT_PAGES:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find pcdots div and show current content for debugging
    dots_m = re.search(r'<div class="pcdots"[^>]*>(.*?)</div>', content, re.DOTALL)
    if dots_m:
        print(f'{page} dots block:')
        print(repr(dots_m.group(1)[:300]))

        # Try to find data-i="2" button and insert after it
        # The format may vary - let's try multiple patterns
        patterns = [
            (r'(data-i="2"[^>]*></button>)(\s*</div>)', r'\1' + NEW_DOT + r'\2'),
            (r'(data-i="2"[^/]*/>\s*</button>)(\s*</div>)', r'\1' + NEW_DOT + r'\2'),
            (r'(<button[^>]*data-i="2"[^>]*>)(<\/button>)(\s*<\/div>)', r'\1\2' + NEW_DOT + r'\3'),
        ]

        fixed = False
        for pat, repl in patterns:
            new_content = re.sub(pat, repl, content, count=1)
            if new_content != content:
                content = new_content
                fixed = True
                print(f'  Fixed with pattern: {pat[:40]}')
                break

        if not fixed:
            # Manual: find closing </div> of pcdots and insert before it
            new_content = re.sub(
                r'(class="pcdots"[^>]*>)(.*?)(</div>)',
                lambda m: m.group(1) + m.group(2).rstrip() + NEW_DOT + '\n' + m.group(3),
                content, count=1, flags=re.DOTALL
            )
            if new_content != content:
                content = new_content
                fixed = True
                print(f'  Fixed with manual insertion')

        if fixed:
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'  SAVED {page}')
        else:
            print(f'  COULD NOT FIX {page}')
