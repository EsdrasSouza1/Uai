import glob
import re
import os

target_btn = '''<a href="https://wa.me/5581997484915?text=Ol%C3%A1%21+vim+pelo+site+e+tenho+uma+duvida%21" class="btn-primary" target="_blank" style="width:100%;justify-content:center;background:#25D366;border-color:#25D366;margin-top:4px;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z" /></svg> Falar no WhatsApp
          </a>'''

# 1. Update chatbot button size on index.html
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make it 85px desktop, 65px mobile
text = re.sub(r'#uai-chat-btn\s*\{[^}]*width:\s*\d+px;\s*height:\s*\d+px;', r'#uai-chat-btn {\n            position: fixed;\n            bottom: 92px;\n            right: 24px;\n            z-index: 997;\n            width: 85px;\n            height: 85px;', text)
text = re.sub(r'#uai-chat-btn img\s*\{[^}]*width:\s*\d+px;\s*height:\s*\d+px;', r'#uai-chat-btn img {\n            width: 85px;\n            height: 85px;', text)

# mobile media query size
text = re.sub(r'#uai-chat-btn\s*\{\s*right:\s*12px;\s*bottom:\s*90px;\s*width:\s*\d+px;\s*height:\s*\d+px;', r'#uai-chat-btn {\n                right: 12px;\n                bottom: 90px;\n                width: 65px;\n                height: 65px;', text)
text = re.sub(r'#uai-chat-btn img\s*\{\s*width:\s*\d+px;\s*height:\s*\d+px;', r'#uai-chat-btn img {\n                width: 65px;\n                height: 65px;', text)

text = re.sub(r'#uai-chat-notif\s*\{([^}]*?)bottom:\s*\d+px;', r'#uai-chat-notif {\1bottom: 187px;', text)
# mobile notif
text = re.sub(r'#uai-chat-notif \{(.*?)(bottom:\s*\d+px;.*?)?\}', lambda m: m.group(0).replace(m.group(2), 'bottom: 167px;') if m.group(2) else m.group(0), text, count=1, flags=re.DOTALL) # Need to be careful here...
# Easier substitution:
text = text.replace('bottom: 174px;', 'bottom: 187px;')
text = text.replace('bottom: 164px;', 'bottom: 165px;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)


# 2. Add WPP button in mascot boxes & remove floating wpp from non-index files
for fpath in glob.glob('*.html'):
    if fpath == 'index.html':
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove floating wpp
    content = re.sub(r'<!-- Floating WhatsApp Button -->.*?</a>', '', content, flags=re.DOTALL)
    
    # Add new specific WhatsApp button inside mascote-box
    if 'class="mascote-box"' in content:
        # Check if we already added it
        if "Falar no WhatsApp" not in content and "text=Ol" in target_btn: 
            # Find the closing tag of mascote-box's <p> and insert button
            content = re.sub(r'(<div class="mascote-box".*?</p>)', r'\1\n' + target_btn, content, flags=re.DOTALL)
            
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
