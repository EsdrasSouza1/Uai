import re

with open('quem-somos.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Desktop overrides
content = re.sub(r'(#uai-chat-btn\s*\{\s*position:\s*fixed;\s*)bottom:\s*\d+px;\s*right:\s*\d+px;', r'\1bottom: 24px;\n            right: 24px;', content)
content = re.sub(r'(#uai-chat-notif\s*\{\s*position:\s*fixed;\s*)bottom:\s*\d+px;\s*right:\s*\d+px;', r'\1bottom: 110px;\n            right: 86px;', content)
content = re.sub(r'(#uai-chat-window\s*\{\s*position:\s*fixed;\s*)bottom:\s*\d+px;\s*right:\s*\d+px;', r'\1bottom: 32px;\n            right: 24px;', content)

# Mobile overrides
# Find the @media block containing #uai-chat-window
content = re.sub(
    r'(@media\s*\(max-width:\s*480px\)\s*\{\s*#uai-chat-window\s*\{\s*width:\s*calc\(100vw\s*-\s*24px\);\s*right:\s*12px;\s*)bottom:\s*\d+px;',
    r'\1bottom: 24px;',
    content
)

content = re.sub(
    r'(#uai-chat-btn\s*\{\s*)right:\s*12px;\s*bottom:\s*90px;',
    r'\1right: 16px;\n                bottom: 20px;',
    content
)

content = re.sub(
    r'(#uai-chat-notif\s*\{\s*)right:\s*\d+px;\s*bottom:\s*\d+px;',
    r'\1right: 70px;\n                bottom: 90px;',
    content
)

with open('quem-somos.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
