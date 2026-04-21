import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # 1. Remove wave emojis 🌊
    new_text = text.replace('🌊', '')
    
    # 2. Fix list layout for flex containers (<li><span class="ii">...</span><strong>...</strong>...)
    # The issue is that <li> is display:flex and its children span, strong and text become separate flex items.
    # We should match: <li><span class="ii">CHAR</span><strong>TITLE</strong> TEXT</li>
    # and change it to: <li><span class="ii">CHAR</span><span><strong>TITLE</strong> TEXT</span></li>
    
    # We can do this with regex:
    # Match: (<li>\s*<span class="ii">.*?</span>)\s*(<strong>.*?)</li>
    # Replacement: \1<span>\2</span></li>
    
    new_text = re.sub(r'(<li>\s*<span class="ii">[^<]*</span>)\s*(<strong>.*?</li>)', r'\1<span>\2', new_text)
    
    # Wait, the closing </li> is captured in \2, so replacing with \1<span>\2 isn't fully correct because it puts the </span> after </li>.
    # Let's fix that.
    # Match: (<li>\s*<span class="ii">[^<]*</span>)\s*(<strong>.*?)</li>
    # Repl:  \1<span>\2</span></li>
    
    new_text = re.sub(r'(<li>\s*<span class="ii">[^<]*</span>)\s*(<strong>.*?)</li>', r'\1<span>\2</span></li>', text.replace('🌊', ''))

    # Let's also do it for checkmarks that don't have strong but are just text
    # Actually, <span class="ii">✓</span>Text...</li> -> the text is a single node so it's a single flex child, which is fine!
    # The problem only occurs when there are MULTIPLE children after the span, e.g. <strong>Title</strong> Text.
    # So wrapping ALL text after <span class="ii"> in a <span> is the safest for all.
    # Match: (<li>\s*<span class="ii">[^<]*</span>)\s*(.*?)\s*</li>
    # Replace: \1<span>\2</span></li>
    new_text = re.sub(r'(<li>\s*<span class="(?:ii|rstep)">[^<]*</span>)\s*(?!<span)(.*?)\s*</li>', r'\1<span>\2</span></li>', new_text, flags=re.DOTALL)
    
    if new_text != text:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_text)

print("Formatting fixed and wave emojis removed.")
