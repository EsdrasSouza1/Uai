import re
import glob

# Mapeamento do tour para suas 5 imagens da galeria
TOUR_GALS = {
    'passeio-cabo-santo-agostinho.html': [
        'foto/Cabo de Santo Agostinho Passeios de Buggy/image-0 (1).jpeg',
        'foto/Cabo de Santo Agostinho Passeios de Buggy/image-1.jpeg',
        'foto/Cabo de Santo Agostinho Passeios de Buggy/image-2.jpeg',
        'foto/Cabo de Santo Agostinho Passeios de Buggy/image-5.jpeg',
        'foto/Cabo de Santo Agostinho Passeios de Buggy/image-9.jpeg'
    ],
    'passeio-carneiros.html': [
        'foto/carneiros/Carneiros 1.jpeg',
        'foto/carneiros/image-17.jpeg',
        'foto/carneiros/image-18.jpeg',
        'foto/carneiros/image-2 (1).jpeg',
        'foto/carneiros/image-6.jpeg'
    ],
    'passeio-city-tour.html': [
        'foto/Citytour Recife e Olinda/image-13.jpeg',
        'foto/Citytour Recife e Olinda/image-14.jpeg',
        'foto/Citytour Recife e Olinda/image-2.jpeg',
        'foto/Citytour Recife e Olinda/image-4.jpeg',
        'foto/Citytour Recife e Olinda/image-8.jpeg'
    ],
    'passeio-ilha-santo-aleixo.html': [
        'foto/Santo Aleixo/image-1.jpeg',
        'foto/Santo Aleixo/image-10.jpeg',
        'foto/Santo Aleixo/image-2 (1).jpeg',
        'foto/Santo Aleixo/image-3.jpeg',
        'foto/Santo Aleixo/image-4.jpeg'
    ],
    'passeio-maragogi.html': [
        'foto/Maragogi - Barra Grande/image-0.jpeg',
        'foto/Maragogi - Barra Grande/image-1.jpeg',
        'foto/Maragogi - Barra Grande/image-11.jpeg',
        'foto/Maragogi - Barra Grande/image-4.jpeg',
        'foto/Maragogi - Barra Grande/image-6.jpeg'
    ],
    'passeio-maragogi-ponta-de-mangue.html': [
        'foto/Maragogi - Ponta de Mangue/image-10.jpeg',
        'foto/Maragogi - Ponta de Mangue/image-17.jpeg',
        'foto/Maragogi - Ponta de Mangue/image-2.jpeg',
        'foto/Maragogi - Ponta de Mangue/image-4.jpeg',
        'foto/Maragogi - Ponta de Mangue/image-7.jpeg'
    ],
    'passeio-milagres.html': [
        'foto/milagres/IMG_0303.jpg',
        'foto/milagres/IMG_0997.jpg',
        'foto/milagres/IMG_2767.jpg',
        'foto/milagres/IMG_2773.jpg',
        'foto/milagres/IMG_2809.jpg'
    ],
    'passeio-porto-de-galinhas.html': [
        'foto/Passeio Buggy - Porto de Galinhas/image-0.jpeg',
        'foto/Passeio Buggy - Porto de Galinhas/image-13.jpeg',
        'foto/Passeio Buggy - Porto de Galinhas/image-2.jpeg',
        'foto/Passeio Buggy - Porto de Galinhas/image-20.jpeg',
        'foto/Passeio Buggy - Porto de Galinhas/image-3.jpeg'
    ]
}

novo_outros_roteiros_inner = """
          <div class="rc-card"><img src="foto/Passeio Buggy - Porto de Galinhas/image-8.jpeg" alt="Porto de Galinhas" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Pernambuco</span><h4>Porto de Galinhas – Buggy</h4><a href="passeio-porto-de-galinhas.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/Maragogi - Barra Grande/image-7.jpeg" alt="Maragogi Barra Grande" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Alagoas</span><h4>Maragogi – Barra Grande</h4><a href="passeio-maragogi.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/Maragogi - Ponta de Mangue/image-8.jpeg" alt="Maragogi Ponta de Mangue" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Alagoas</span><h4>Maragogi – Ponta de Mangue</h4><a href="passeio-maragogi-ponta-de-mangue.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/carneiros/Carneiros Capela.jpg" alt="Praia dos Carneiros" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Pernambuco</span><h4>Praia dos Carneiros</h4><a href="passeio-carneiros.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/Cabo de Santo Agostinho Passeios de Buggy/image-1.jpeg" alt="Cabo de Santo Agostinho" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Pernambuco</span><h4>Cabo de Santo Agostinho</h4><a href="passeio-cabo-santo-agostinho.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/Santo Aleixo/image-1.jpeg" alt="Ilha de Santo Aleixo" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Pernambuco</span><h4>Ilha de Santo Aleixo</h4><a href="passeio-ilha-santo-aleixo.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/milagres/IMG_9090.jpg" alt="São Miguel dos Milagres" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Alagoas</span><h4>São Miguel dos Milagres</h4><a href="passeio-milagres.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/Citytour Recife e Olinda/principal.jpeg" alt="City Tour Recife e Olinda" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Pernambuco</span><h4>City Tour Recife &amp; Olinda</h4><a href="passeio-city-tour.html">Ver passeio &rarr;</a></div></div>
"""

for fn, images in TOUR_GALS.items():
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # 1. Atualizar a MAIN GALLERY (rc3-track) com EXATAS 5 FOTOS
    # Precisamos encontrar <div class="rc3-track" id="rc3-track"> e fechar após todas as divs
    match = re.search(r'<div class="rc3-track" id="rc3-track">.*?</div>\s*</div>\s*<div class="rc3-dots"', html, flags=re.DOTALL)
    if match:
        slides_html = ""
        for img in images:
            slides_html += f'          <div class="rc3-card"><img src="{img}" alt="Galeria"></div>\n'
            
        new_gallery = f'<div class="rc3-track" id="rc3-track">\n{slides_html}        </div>\n      </div>\n      <div class="rc3-dots"'
        html = html.replace(match.group(0), new_gallery)

    # 2. Atualizar "Outros Roteiros" (rc-track) com TODOS os itens com fotos novas
    match_outros = re.search(r'<div class="rc-track" id="rc-track">.*?</div>\s*</div>\s*<div class="rc-dots"', html, flags=re.DOTALL)
    if match_outros:
        new_outros = f'<div class="rc-track" id="rc-track">\n{novo_outros_roteiros_inner}        </div>\n      </div>\n      <div class="rc-dots"'
        html = html.replace(match_outros.group(0), new_outros)

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Sucesso!")
