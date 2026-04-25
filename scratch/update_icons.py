import re

def get_icons(color, shape1, pos1, shape2, pos2, shape3, pos3):
    shapes_svg = {
        'star': '<svg class="deco-item deco-starfish" style="{pos}; width:60px; fill:{color};" viewBox="0 0 24 24"><path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z" /></svg>',
        'turtle': '<svg class="deco-item deco-turtle" style="{pos}; width:100px; fill:{color};" viewBox="0 0 100 100"><ellipse cx="50" cy="50" rx="28" ry="22"/><ellipse cx="35" cy="35" rx="7" ry="5"/><ellipse cx="65" cy="35" rx="7" ry="5"/><ellipse cx="35" cy="65" rx="7" ry="5"/><ellipse cx="65" cy="65" rx="7" ry="5"/></svg>',
        'shell': '<svg class="deco-item deco-shell" style="{pos}; width:80px; fill:{color};" viewBox="0 0 100 100"><path d="M50 10 C70 10 85 25 85 45 C85 65 70 80 50 80 C30 80 15 65 15 45 C15 30 25 18 38 13"/></svg>'
    }
    
    return f'''
        <div class="deco-container">
            {shapes_svg[shape1].format(pos=pos1, color=color)}
            {shapes_svg[shape2].format(pos=pos2, color=color)}
            {shapes_svg[shape3].format(pos=pos3, color=color)}
        </div>'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all existing deco-containers
content = re.sub(r'<div class="deco-container">.*?</div>', '', content, flags=re.DOTALL)

# Re-insert with 3 icons per section
content = re.sub(r'(<section[^>]*id="diferenciais"[^>]*>)', r'\1' + get_icons('#0097A7', 'turtle', 'top:10%; left:5%;', 'star', 'bottom:15%; right:6%;', 'shell', 'top:55%; left:48%;'), content)
content = re.sub(r'(<section[^>]*class="experience-gallery"[^>]*>)', r'\1' + get_icons('#FFFFFF', 'star', 'top:15%; left:4%;', 'turtle', 'bottom:12%; right:5%;', 'shell', 'top:45%; right:45%;'), content)
content = re.sub(r'(<section[^>]*id="avaliacoes"[^>]*>)', r'\1' + get_icons('#0097A7', 'turtle', 'top:18%; right:4%;', 'star', 'bottom:10%; left:6%;', 'shell', 'top:60%; left:42%;'), content)
content = re.sub(r'(<section[^>]*id="faq"[^>]*>)', r'\1' + get_icons('#0097A7', 'turtle', 'top:8%; right:5%;', 'star', 'bottom:5%; left:4%;', 'shell', 'top:40%; left:50%;'), content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html with 3 icons per section')
