import sys

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

def get_icons(color, side1='left', side2='right'):
    return f'''
        <div class="deco-container">
            <svg class="deco-item deco-starfish" style="top:15%; {side1}:3%; width:60px; fill:{color};" viewBox="0 0 24 24">
                <path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z" />
            </svg>
            <svg class="deco-item deco-turtle" style="bottom:25%; {side2}:3%; width:100px; fill:{color};" viewBox="0 0 100 100">
                <ellipse cx="50" cy="50" rx="28" ry="22"/>
                <ellipse cx="35" cy="35" rx="7" ry="5"/>
                <ellipse cx="65" cy="35" rx="7" ry="5"/>
                <ellipse cx="35" cy="65" rx="7" ry="5"/>
                <ellipse cx="65" cy="65" rx="7" ry="5"/>
            </svg>
        </div>'''

# 1. diferenciais-section
old_dif = '<section id="diferenciais" class="diferenciais-section">'
if old_dif in content:
    content = content.replace(old_dif, old_dif + get_icons('#0097A7', 'right', 'left'))
else:
    print('diferenciais not found')

# 2. experience-gallery
old_gal = '<section class="experience-gallery" id="galeria">'
if old_gal in content:
    content = content.replace(old_gal, old_gal + get_icons('#FFFFFF'))
else:
    print('galeria not found')

# 3. avaliacoes-section
old_ava = '<section id="avaliacoes" class="avaliacoes-section">'
if old_ava in content:
    content = content.replace(old_ava, old_ava + get_icons('#0097A7'))
else:
    print('avaliacoes not found')

# 4. faq-section
old_faq = '<section id="faq" class="faq-section">'
if old_faq in content:
    content = content.replace(old_faq, old_faq + get_icons('#0097A7', 'left', 'right'))
else:
    print('faq not found')

# 5. chatbot-card
old_chat = '<div class="chatbot-card-wrapper">'
if old_chat in content:
    content = content.replace(old_chat, '<div class="chatbot-card-wrapper" style="position:relative;">' + get_icons('#0097A7', 'left', 'right'))
else:
    print('chatbot not found')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done index.html')
