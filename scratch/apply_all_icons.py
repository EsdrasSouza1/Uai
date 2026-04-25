import os
import re

def get_icons(color, top_shape, top_side, bottom_shape, bottom_side):
    star = f'''<svg class="deco-item deco-starfish" style="{{y}}:15%; {{side}}:3%; width:60px; fill:{color};" viewBox="0 0 24 24"><path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z" /></svg>'''
    turtle = f'''<svg class="deco-item deco-turtle" style="{{y}}:15%; {{side}}:3%; width:100px; fill:{color};" viewBox="0 0 100 100"><ellipse cx="50" cy="50" rx="28" ry="22"/><ellipse cx="35" cy="35" rx="7" ry="5"/><ellipse cx="65" cy="35" rx="7" ry="5"/><ellipse cx="35" cy="65" rx="7" ry="5"/><ellipse cx="65" cy="65" rx="7" ry="5"/></svg>'''
    
    top_svg = star.format(y='top', side=top_side) if top_shape == 'star' else turtle.format(y='top', side=top_side)
    bottom_svg = star.format(y='bottom', side=bottom_side) if bottom_shape == 'star' else turtle.format(y='bottom', side=bottom_side)
    
    return f'''
        <div class="deco-container">
            {top_svg}
            {bottom_svg}
        </div>'''

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove existing
        content = re.sub(r'<!-- Silhueta.*?<style>\s*\.destinos-section.*?\{.*?</style>', '', content, flags=re.DOTALL)
        content = re.sub(r'<div class="deco-container">.*?</div>', '', content, flags=re.DOTALL)

        # Photo 5: "A experiência Uai Turismo" (diferenciais) -> Blob on left (top), Star on right (bottom)
        # Actually photo 5 has blob on left, star on right. Let's do top left blob, bottom right star.
        content = re.sub(r'(<section[^>]*id="diferenciais"[^>]*>)', r'\1' + get_icons('#0097A7', 'turtle', 'left', 'star', 'right'), content)
        
        # Photo 4: "Galeria" -> left and right empty circles. Let's do star top left, turtle bottom right
        content = re.sub(r'(<section[^>]*class="experience-gallery"[^>]*>)', r'\1' + get_icons('#FFFFFF', 'star', 'left', 'turtle', 'right'), content)
        
        # Photo 3: "Depoimentos" (avaliacoes) -> left and right empty.
        content = re.sub(r'(<section[^>]*id="avaliacoes"[^>]*>)', r'\1' + get_icons('#0097A7', 'turtle', 'right', 'star', 'left'), content)
        
        # Photo 2 & 1: "FAQ" -> blob right (top), star left (bottom)
        content = re.sub(r'(<section[^>]*id="faq"[^>]*>)', r'\1' + get_icons('#0097A7', 'turtle', 'right', 'star', 'left'), content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
print('Done processing all HTML files.')
