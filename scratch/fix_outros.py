import os, re

pages = [
    'passeio-carneiros.html',
    'passeio-maragogi.html',
    'passeio-maragogi-ponta-de-mangue.html',
    'passeio-porto-de-galinhas.html',
    'passeio-cabo-santo-agostinho.html',
    'passeio-ilha-santo-aleixo.html',
    'passeio-milagres.html',
    'passeio-city-tour.html',
]

# The "Outros Roteiros" carousel in all pages uses wrong images for some cards.
# Fix: replace the entire rc-track block with a standardized correct one in each file.
CORRECT_OUTROS = '''          <div class="rc-card"><img src="foto/Passeio Buggy - Porto de Galinhas/image-8.jpeg" alt="Porto de Galinhas" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Pernambuco</span><h4>Porto de Galinhas – Buggy</h4><a href="passeio-porto-de-galinhas.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/Maragogi - Barra Grande/image-7.jpeg" alt="Maragogi – Barra Grande" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Alagoas</span><h4>Maragogi – Barra Grande</h4><a href="passeio-maragogi.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/Maragogi - Ponta de Mangue/image-8.jpeg" alt="Maragogi – Ponta de Mangue" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Alagoas</span><h4>Maragogi – Ponta de Mangue</h4><a href="passeio-maragogi-ponta-de-mangue.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/carneiros/image-18.jpeg" alt="Praia dos Carneiros" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Pernambuco</span><h4>Praia dos Carneiros</h4><a href="passeio-carneiros.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/Cabo de Santo Agostinho Passeios de Buggy/image-1.jpeg" alt="Cabo de Santo Agostinho" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Pernambuco</span><h4>Cabo de Santo Agostinho – Buggy</h4><a href="passeio-cabo-santo-agostinho.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/Santo Aleixo/image-10.jpeg" alt="Ilha de Santo Aleixo" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Pernambuco</span><h4>Ilha de Santo Aleixo</h4><a href="passeio-ilha-santo-aleixo.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/milagres/IMG_0303.jpg" alt="São Miguel dos Milagres" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Alagoas</span><h4>São Miguel dos Milagres</h4><a href="passeio-milagres.html">Ver passeio &rarr;</a></div></div>
          <div class="rc-card"><img src="foto/Citytour Recife e Olinda/principal.jpeg" alt="City Tour Recife e Olinda" loading="lazy"><div class="rc-overlay"><span class="rc-tag">Pernambuco</span><h4>City Tour Recife &amp; Olinda</h4><a href="passeio-city-tour.html">Ver passeio &rarr;</a></div></div>'''

# Pattern to find the rc-track content
pattern = re.compile(
    r'(<div class="rc-track" id="rc-track">)(.*?)(</div>\s*</div>\s*<button class="rc-next-btn")',
    re.DOTALL
)

for page in pages:
    if not os.path.exists(page):
        print(f'SKIP: {page}')
        continue

    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    def replacer(m):
        return m.group(1) + '\n' + CORRECT_OUTROS + '\n        ' + m.group(3)

    content = pattern.sub(replacer, content)

    if content != original:
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Updated outros roteiros: {page}')
    else:
        print(f'  No outros roteiros found (or already correct): {page}')

print('Done!')
