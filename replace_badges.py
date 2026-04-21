import re
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_badges = """<div class="hero-badges" id="heroBadges">
                    <div class="badge"><strong class="counter" data-target="5000">0</strong><span>Sonhos realizados</span></div>
                    <div class="badge-divider"></div>
                    <div class="badge"><strong>5★</strong><span>Avaliação no Google</span></div>
                    <div class="badge-divider"></div>
                    <div class="badge"><strong>100%</strong><span>Atendimento personalizado</span></div>
                </div>"""

# replace the block
new_text = re.sub(r'<div class=\"hero-badges\" id=\"heroBadges\">.*?</div>\s*</div>', new_badges, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("heroBadges updated successfully!")
