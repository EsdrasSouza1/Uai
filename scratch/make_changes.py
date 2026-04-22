
import re
import os

os.chdir(r'c:\Users\nerds\OneDrive\Área de Trabalho\Uai')

# ============================================================
# DICAS HTML - Praia
DICAS_PRAIA = '''
        <!-- DICAS PARA O PASSEIO -->
        <div class="pinc" style="background: linear-gradient(135deg, #e8f6f9 0%, #d0eef5 100%); border: 1px solid #a0d9e8; border-radius: 20px; padding: 32px 28px; margin-bottom: 24px;">
          <h3 style="font-family: 'Playfair Display', serif; font-size: 1.15rem; color: #004D5C; margin-bottom: 18px;">💡 Dicas para o Passeio</h3>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 10px;">
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span style="flex-shrink:0;">☀️</span> Use protetor solar e reaplique ao longo do dia (mesmo nublado, o sol queima forte)</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span style="flex-shrink:0;">💧</span> Leve água — o calor é intenso</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span style="flex-shrink:0;">👕</span> Vá com roupa leve, já com roupa de banho por baixo e leve roupa seca para a volta</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span style="flex-shrink:0;">🏖️</span> Leve toalha ou canga</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span style="flex-shrink:0;">👟</span> Use chinelo ou sandália confortável</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span style="flex-shrink:0;">🕶️</span> Leve óculos de sol e boné/chapéu</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span style="flex-shrink:0;">📱</span> Proteja o celular com capa à prova d'água</li>
          </ul>
        </div>
'''

DICAS_CITY = '''
        <!-- DICAS PARA O PASSEIO -->
        <div class="pinc" style="background: linear-gradient(135deg, #e8f6f9 0%, #d0eef5 100%); border: 1px solid #a0d9e8; border-radius: 20px; padding: 32px 28px; margin-bottom: 24px;">
          <h3 style="font-family: 'Playfair Display', serif; font-size: 1.15rem; color: #004D5C; margin-bottom: 18px;">💡 Dicas para o Passeio</h3>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 10px;">
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span style="flex-shrink:0;">👕</span> Use roupas leves e confortáveis</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span style="flex-shrink:0;">👟</span> Vá de tênis ou sandália firme (ruas de pedra e ladeiras)</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span style="flex-shrink:0;">💧</span> Leve água — caminhadas são frequentes</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span style="flex-shrink:0;">☀️</span> Use protetor solar (mesmo sendo passeio urbano)</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span style="flex-shrink:0;">🕶️</span> Óculos de sol e boné ajudam bastante</li>
          </ul>
        </div>
'''

DICA_MARKER = '        <!-- DICAS -->'

files_praia = [
    'passeio-carneiros.html',
    'passeio-maragogi.html',
    'passeio-maragogi-ponta-de-mangue.html',
    'passeio-porto-de-galinhas.html',
    'passeio-cabo-santo-agostinho.html',
    'passeio-ilha-santo-aleixo.html',
    'passeio-milagres.html',
]

# 1) Adicionar dicas em paginas de praia
for fname in files_praia:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        if DICA_MARKER in content:
            content = content.replace(DICA_MARKER, DICAS_PRAIA + DICA_MARKER)
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'[OK] Dicas praia: {fname}')
        else:
            print(f'[SKIP] Marker nao encontrado: {fname}')
    except Exception as e:
        print(f'[ERR] {fname}: {e}')

# 2) Dicas city tour - insere antes da closing div da coluna principal
try:
    with open('passeio-city-tour.html', 'r', encoding='utf-8') as f:
        content = f.read()
    marker = '        \n        \n      </div>\n\n      <div class="psidebar">'
    if marker in content:
        content = content.replace(marker, DICAS_CITY + marker, 1)
    else:
        # Try simpler approach
        content = content.replace(
            '      </div>\n\n      <div class="psidebar">',
            DICAS_CITY + '      </div>\n\n      <div class="psidebar">',
            1
        )
    with open('passeio-city-tour.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('[OK] Dicas city tour')
except Exception as e:
    print(f'[ERR] city-tour: {e}')

# ============================================================
# 3) INDEX.HTML - múltiplas alterações
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        idx = f.read()

    # a) Texto principal heroP - Os melhores roteiros
    idx = idx.replace(
        'Os melhores roteiros de <strong>Porto de Galinhas, Maragogi, Carneiros e Milagres</strong>',
        'Os melhores roteiros da região de Porto de Galinhas. <strong>🌊 Maragogi, Carneiros, Milagres e muito mais!</strong>'
    )

    # b) hero tag - adicionar emoji de mar nos Maragogi
    idx = idx.replace(
        '🏝️ Maragogi &bull; Carneiros &bull; Milagres &bull; Buggy',
        '🏝️ 🌊 Maragogi &bull; Carneiros &bull; Milagres &bull; Buggy em Porto'
    )

    # c) Slide caption Maragogi Barra Grande - adicionar onda
    idx = idx.replace(
        '<div class="hero-slide-caption"> Maragogi - Barra Grande</div>',
        '<div class="hero-slide-caption">🌊 Maragogi - Barra Grande</div>'
    )
    idx = idx.replace(
        '<div class="hero-slide-caption"> Maragogi - Ponta de Mangue</div>',
        '<div class="hero-slide-caption">🌊 Maragogi - Ponta de Mangue</div>'
    )

    # d) Marquee - adicionar onda nos dois Maragogi
    idx = idx.replace(
        '<span class="marquee-item"> Maragogi <span class="marquee-sep">✦</span></span><span class="marquee-item">⛵',
        '<span class="marquee-item">🌊 Maragogi <span class="marquee-sep">✦</span></span><span class="marquee-item">⛵'
    )
    idx = idx.replace(
        '<span class="marquee-item"> Maragogi <span\n                    class="marquee-sep">✦</span></span>',
        '<span class="marquee-item">🌊 Maragogi <span\n                    class="marquee-sep">✦</span></span>'
    )

    # e) Foto Santo Aleixo no carrossel de destinos (card 6)
    idx = idx.replace(
        'src="foto/Santo Aleixo/image-10.jpeg" alt="Ilha de Santo Aleixo"\n                                loading="lazy">',
        'src="foto/Santo Aleixo/IMG_2395.jpg" alt="Ilha de Santo Aleixo"\n                                loading="lazy">'
    )

    # f) Foto Milagres no carrossel de destinos (card 7)
    idx = idx.replace(
        'src="foto/milagres/IMG_0303.jpg" alt="São Miguel dos Milagres"\n                                loading="lazy">',
        'src="foto/milagres/IMG_2767.jpg" alt="São Miguel dos Milagres"\n                                loading="lazy">'
    )

    # g) Momentos reais - dar espaço entre instagram badge e widget
    idx = idx.replace(
        '<div class="instagram-widget-container" style="margin-top:30px;"',
        '<div class="instagram-widget-container" style="margin-top:56px;"'
    )

    # h) Nossos Destinos - adicionar silhueta de peixe-boi (watermark SVG)
    PEIXE_BOI_SVG = '''
    <!-- Silhueta peixe-boi decorativa na seção destinos -->
    <style>
    .destinos-section { position: relative; overflow: hidden; }
    .destinos-section::before {
        content: '';
        position: absolute;
        right: -60px;
        top: 50%;
        transform: translateY(-50%);
        width: 420px;
        height: 420px;
        background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 130'%3E%3Cellipse cx='90' cy='65' rx='70' ry='42' fill='%230097A7' opacity='.07'/%3E%3Cellipse cx='155' cy='50' rx='25' ry='18' fill='%230097A7' opacity='.07'/%3E%3Cellipse cx='80' cy='60' rx='10' ry='8' fill='%230097A7' opacity='.07'/%3E%3Cpath d='M25 65 Q10 55 15 75 Q20 85 35 80' fill='%230097A7' opacity='.07'/%3E%3Cpath d='M90 23 Q80 10 100 15' stroke='%230097A7' stroke-width='3' fill='none' opacity='.07'/%3E%3Cpath d='M60 107 Q50 120 70 115' stroke='%230097A7' stroke-width='3' fill='none' opacity='.07'/%3E%3C/svg%3E") center/contain no-repeat;
        pointer-events: none;
        z-index: 0;
    }
    </style>
'''

    # Inserir antes de </section> da seção destinos
    idx = idx.replace(
        '<!-- CARROSSEL 3 CARDS DE DESTINOS -->',
        PEIXE_BOI_SVG + '<!-- CARROSSEL 3 CARDS DE DESTINOS -->'
    )

    # i) Preloader - garantir fonte Playfair correta (já tem, ok)
    
    # j) Footer do index - trocar logo-text para ter img
    old_footer_brand = '''            <div class="footer-brand">
                <div class="footer-logo-text"><span class="logo-uai">Uai</span><span class="logo-turismo">
                        Turismo</span></div>'''
    new_footer_brand = '''            <div class="footer-brand">
                <div class="footer-logo-text" style="display:flex;align-items:center;gap:4px;font-family:'Playfair Display',serif;font-size:1.4rem;line-height:1;margin-bottom:10px;">
                    <span style="color:var(--amber-light);font-weight:900;font-style:italic;">Uai</span>
                    <span style="color:rgba(255,255,255,.85);font-weight:900;font-style:italic;">Turismo</span>
                </div>'''
    idx = idx.replace(old_footer_brand, new_footer_brand)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx)
    print('[OK] index.html atualizado')
except Exception as e:
    print(f'[ERR] index.html: {e}')

# ============================================================
# 4) Política de privacidade - substituir footer simples pelo padrão
try:
    with open('politica-de-privacidade.html', 'r', encoding='utf-8') as f:
        pol = f.read()

    OLD_FOOTER = '''    <!-- FOOTER -->
    <footer class="pp-footer">
        <p>© 2026 Uai Turismo — CNPJ 54.181.357/0001-42 | Porto de Galinhas, PE</p>
        <p style="margin-top:8px;"><a href="index.html">← Voltar ao site</a></p>
        <p style="margin-top:10px;font-size:.72rem;opacity:.45;">Desenvolvido por <a href="https://www.instagram.com/Souza.Web_/" target="_blank" style="color:inherit;opacity:.7;transition:opacity .3s" onmouseover="this.style.opacity=\'1\'" onmouseout="this.style.opacity=\'.7\'">@Souza.Web_</a></p>
    </footer>'''

    NEW_FOOTER = '''    <!-- FOOTER PADRONIZADO -->
    <footer class="main-footer">
      <div class="footer-inner">
        <div class="footer-brand">
          <div style="display:flex;align-items:center;gap:4px;font-family:'Playfair Display',serif;font-size:1.4rem;line-height:1;margin-bottom:10px;">
            <span style="color:var(--amber-light);font-weight:900;font-style:italic;">Uai</span>
            <span style="color:rgba(255,255,255,.85);font-weight:900;font-style:italic;">Turismo</span>
          </div>
          <p>Passeios privativos e compartilhados,<br>Buggy em Pernambuco e Alagoas.</p>
          <p style="margin-top:8px;font-size:.78rem;color:rgba(255,255,255,.4);">CNPJ: 54.181.357/0001-42<br>MARCOS VINICIUS SILVA SOUZA</p>
        </div>
        <div class="footer-links"><h5>Links Rápidos</h5><a href="index.html#hero">Início</a><a href="index.html#destinos">Destinos</a><a href="index.html#galeria">Galeria</a><a href="index.html#faq">Dúvidas</a><a href="quem-somos.html">Sobre nós</a><a href="https://uaiturismo.surishop.ai/catalog" target="_blank">Catálogo</a></div>
        <div class="footer-contact"><h5>Contato</h5><a href="https://wa.me/5581997484915?text=Ol%C3%A1%2C%20vim%20pelo%20site%20e%20gostaria%20de%20saber%20mais" target="_blank">📞 (81) 99748-4915</a><p>📍 Porto de Galinhas, PE</p><p>✉️ contato@uaitur.com</p></div>
        <div class="footer-social"><h5>Siga no Instagram</h5><p>Veja mais fotos dos nossos passeios!</p><a href="https://www.instagram.com/uai_turismo/" target="_blank" style="display:inline-flex;align-items:center;gap:8px;margin-top:10px;color:var(--amber-light);font-weight:600;"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>@uai_turismo</a></div>
      </div>
      <div class="footer-bottom"><p>© 2026 Uai Turismo. Todos os direitos reservados. &nbsp;|&nbsp; <a href="politica-de-privacidade.html" style="color:rgba(255,255,255,.55);transition:color .3s" onmouseover="this.style.color=\'#FFD166\'" onmouseout="this.style.color=\'rgba(255,255,255,.55)\'">Política de Privacidade</a></p>
        <p style="margin-top:6px;font-size:.72rem;color:rgba(255,255,255,.3);">Desenvolvido por <a href="https://www.instagram.com/Souza.Web_/" target="_blank" style="color:rgba(255,255,255,.4);transition:color .3s" onmouseover="this.style.color=\'#FFD166\'" onmouseout="this.style.color=\'rgba(255,255,255,.4)\'">@Souza.Web_</a></p>
      </div>
    </footer>
    <link rel="stylesheet" href="style.css">'''

    pol = pol.replace(OLD_FOOTER, NEW_FOOTER)
    with open('politica-de-privacidade.html', 'w', encoding='utf-8') as f:
        f.write(pol)
    print('[OK] politica-de-privacidade.html atualizado')
except Exception as e:
    print(f'[ERR] politica: {e}')

# ============================================================
# 5) passeio-maragogi.html - adicionar onda emoji no texto
try:
    with open('passeio-maragogi.html', 'r', encoding='utf-8') as f:
        mar = f.read()
    # Adicionar onda antes do primeiro paragrafo da desc
    mar = mar.replace(
        '<div class="pdesc">\n          <p>',
        '<div class="pdesc">\n          <p>🌊 '
    )
    with open('passeio-maragogi.html', 'w', encoding='utf-8') as f:
        f.write(mar)
    print('[OK] maragogi emoji onda adicionado')
except Exception as e:
    print(f'[ERR] maragogi: {e}')

# ============================================================
# 6) passeio-porto-de-galinhas.html - adicionar horário correto buggy
try:
    with open('passeio-porto-de-galinhas.html', 'r', encoding='utf-8') as f:
        porto = f.read()
    porto = porto.replace(
        '<li><span class="ii">⏱</span><span>Passeio privativo (manhã ou tarde)</span></li>',
        '<li><span class="ii">⏱</span><span>Passeio privativo — saída às <strong>07:30</strong> (manhã) ou <strong>13:00</strong> (tarde)</span></li>'
    )
    # Adicionar titulo Passeio de Buggy em Porto
    porto = porto.replace(
        '<h1>Porto de Galinhas<br><span>o litoral mais charmoso de Pernambuco</span></h1>',
        '<h1>Passeio de Buggy em Porto de Galinhas<br><span>o litoral mais charmoso de Pernambuco</span></h1>'
    )
    with open('passeio-porto-de-galinhas.html', 'w', encoding='utf-8') as f:
        f.write(porto)
    print('[OK] porto-de-galinhas atualizado')
except Exception as e:
    print(f'[ERR] porto: {e}')

# ============================================================
# 7) passeio-city-tour.html - adicionar Servico de guia
try:
    with open('passeio-city-tour.html', 'r', encoding='utf-8') as f:
        ct = f.read()
    ct = ct.replace(
        '<li><span class="ii">✓</span><span>Serviço de guia em história local. 🎭</span></li>',
        '<li><span class="ii">✓</span><span>Serviço de guia em city tour com orientações históricas. 🎭</span></li>'
    )
    with open('passeio-city-tour.html', 'w', encoding='utf-8') as f:
        f.write(ct)
    print('[OK] city-tour servico de guia ok')
except Exception as e:
    print(f'[ERR] city-tour guia: {e}')

# ============================================================
# 8) Foto Santo Aleixo e Milagres nos outros arquivos de passeio (outros roteiros)
for fname in ['passeio-carneiros.html', 'passeio-maragogi.html', 'passeio-maragogi-ponta-de-mangue.html',
              'passeio-porto-de-galinhas.html', 'passeio-cabo-santo-agostinho.html',
              'passeio-ilha-santo-aleixo.html', 'passeio-milagres.html', 'passeio-city-tour.html']:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        changed = False
        c2 = c.replace('src="foto/Santo Aleixo/image-10.jpeg"', 'src="foto/Santo Aleixo/IMG_2395.jpg"')
        if c2 != c: changed = True
        c2 = c2.replace('src="foto/milagres/IMG_0303.jpg"', 'src="foto/milagres/IMG_2767.jpg"')
        if c2 != c: changed = True
        if changed:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(c2)
            print(f'[OK] fotos atualizadas: {fname}')
    except Exception as e:
        print(f'[ERR] fotos {fname}: {e}')

print('=== TUDO CONCLUIDO ===')
