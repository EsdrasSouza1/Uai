import glob, re

emojis = ['📱', '📍', '🌊', '🏝️', '🐊', '👇🏽', '👇', '🏽', '✅', '📸', '🤝', '🛶', '⛵', '🎭', '🏖️', '🌿', '🗺️', '🐠', '☀️', '🍤', '🐿️', '🥥', '🐊', '📸', '✅']

count = 0
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # We want to remove emojis ONLY from texts inside <a> and <button> tags that look like CTA buttons.
    # A generic approach: find <a class="...btn...">...</a> and remove emojis from ...
    
    def strip_emojis(m):
        content = m.group(0)
        for e in emojis:
            content = content.replace(e, '')
        return content

    # Match class containing 'btn' or 'nav-cta' or 'ctacard' -> wait, ctacard is the wrapper, we only want the button.
    new_text = re.sub(r'<a[^>]*class=\"[^\"]*(?:btn|cta)[^\"]*\"[^>]*>(.*?)</a>', strip_emojis, text, flags=re.DOTALL)
    new_text = re.sub(r'<button[^>]*class=\"[^\"]*(?:btn|cta)[^\"]*\"[^>]*>(.*?)</button>', strip_emojis, new_text, flags=re.DOTALL)

    if new_text != text:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_text)
        count += 1

print("Completed button emoji cleanup in", count, "files.")
