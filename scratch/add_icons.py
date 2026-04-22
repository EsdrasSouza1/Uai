
import os
os.chdir(r'c:\Users\nerds\OneDrive\Área de Trabalho\Uai')

# Caminho relativo dos ícones (do HTML)
ICON_PATH = 'foto/\u00cdcones/\u00cdcones/'

# CSS a injetar antes do </style> principal de cada página
DECO_CSS = """
    /* === Ícones decorativos === */
    .deco-icon {
      position: absolute;
      pointer-events: none;
      user-select: none;
      opacity: 0.07;
      z-index: 0;
    }
    .deco-wrap {
      position: relative;
      overflow: hidden;
    }"""

# Mapeamento: página → ícones a adicionar
# Cada item: (arquivo_icone, seção_html_alvo, posição_inline_style, alt)
# Vamos injetar dentro do div.pbody e/ou .outros-sec

PAGES = {
    'passeio-maragogi.html': [
        ('1.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'top:40px;right:-60px;width:280px;transform:rotate(-15deg)',
         'Peixe-boi decorativo'),
        ('2.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'bottom:60px;left:-50px;width:220px;transform:rotate(10deg)',
         'Tartaruga decorativa'),
    ],
    'passeio-maragogi-ponta-de-mangue.html': [
        ('1.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'top:30px;right:-50px;width:260px;transform:rotate(-12deg)',
         'Peixe-boi decorativo'),
        ('5.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'bottom:80px;left:-40px;width:200px',
         'Água-viva decorativa'),
    ],
    'passeio-carneiros.html': [
        ('14.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'top:20px;right:-70px;width:300px;transform:rotate(-8deg)',
         'Barco decorativo'),
        ('3.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'bottom:100px;left:-40px;width:200px',
         'Sol decorativo'),
    ],
    'passeio-cabo-santo-agostinho.html': [
        ('4.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'top:30px;right:-55px;width:260px;transform:rotate(10deg)',
         'Âncora decorativa'),
        ('7.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'bottom:60px;left:-60px;width:240px;transform:rotate(-10deg)',
         'Golfinho decorativo'),
    ],
    'passeio-ilha-santo-aleixo.html': [
        ('2.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'top:40px;right:-50px;width:250px;transform:rotate(-15deg)',
         'Tartaruga decorativa'),
        ('6.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'bottom:80px;left:-50px;width:220px;transform:rotate(12deg)',
         'Peixe decorativo'),
    ],
    'passeio-milagres.html': [
        ('15.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'top:30px;right:-55px;width:260px',
         'Cavalo-marinho decorativo'),
        ('6.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'bottom:70px;left:-45px;width:210px;transform:rotate(15deg)',
         'Peixe decorativo'),
    ],
    'passeio-porto-de-galinhas.html': [
        ('4.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'top:40px;right:-60px;width:270px;transform:rotate(8deg)',
         'Âncora decorativa'),
        ('3.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'bottom:90px;left:-40px;width:190px',
         'Sol decorativo'),
    ],
    'passeio-city-tour.html': [
        ('4.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'top:30px;right:-55px;width:250px',
         'Âncora decorativa'),
        ('7.png', 'style="background:var(--off-white);padding-bottom:80px;"',
         'bottom:80px;left:-50px;width:230px;transform:rotate(-8deg)',
         'Golfinho decorativo'),
    ],
}

# Para index.html - seções brancas diferentes
INDEX_ICONS = [
    # Destinos section (div#destinos)
    ('<div class="rc3-wrapper"', '7', 'top:40px;right:-80px;width:300px;transform:rotate(-10deg)', 'Golfinho decorativo'),
    ('<div class="rc3-wrapper"', '2', 'bottom:60px;left:-70px;width:280px;transform:rotate(15deg)', 'Tartaruga decorativa'),
    # FAQ section
    ('<section class="faq-section"', '4', 'top:30px;right:-60px;width:250px;transform:rotate(10deg)', 'Âncora decorativa'),
    ('<section class="faq-section"', '6', 'bottom:50px;left:-50px;width:220px', 'Peixe decorativo'),
]

def add_deco_css(content):
    """Adiciona CSS dos ícones decorativos se ainda não existir."""
    if 'deco-icon' in content:
        return content
    # Insere antes do primeiro </style>
    idx = content.find('</style>')
    if idx > 0:
        return content[:idx] + DECO_CSS + '\n' + content[idx:]
    return content

def make_icon_html(icon_file, position_style, alt):
    path = ICON_PATH + icon_file
    return f'<img loading="lazy" src="{path}" class="deco-icon" alt="{alt}" aria-hidden="true" style="position:absolute;{position_style};">'

def add_icons_to_pbody(content, icons):
    """Insere ícones dentro do div com padding-bottom:80px (corpo principal)."""
    TARGET = 'style="background:var(--off-white);padding-bottom:80px;">'
    if TARGET not in content:
        return content, False
    
    icon_html = '\n    '
    for icon_file, _, pos_style, alt in icons:
        icon_html += make_icon_html(icon_file, pos_style, alt) + '\n    '
    
    # Make the div position:relative if it doesn't have it
    content = content.replace(
        '<div style="background:var(--off-white);padding-bottom:80px;">',
        '<div style="background:var(--off-white);padding-bottom:80px;position:relative;overflow:hidden;">'
    )
    
    # Re-check TARGET after modification
    NEW_TARGET = 'style="background:var(--off-white);padding-bottom:80px;position:relative;overflow:hidden;">'
    if NEW_TARGET in content:
        content = content.replace(NEW_TARGET, NEW_TARGET + icon_html, 1)
        return content, True
    return content, False

# ---- Processar páginas dos passeios ----
for fname, icons in PAGES.items():
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        original = c
        
        # 1. Adicionar CSS
        c = add_deco_css(c)
        
        # 2. Adicionar ícones no pbody
        c, ok = add_icons_to_pbody(c, icons)
        if not ok:
            print(f'[WARN] nao encontrou pbody em {fname}')
        else:
            print(f'[OK] {fname}: {len(icons)} ícones adicionados')
        
        if c != original:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(c)
    except Exception as e:
        print(f'[ERR] {fname}: {e}')

# ---- Processar index.html ----
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        c = f.read()
    original = c
    
    # CSS
    c = add_deco_css(c)
    
    # Adicionar no rc3-wrapper (destinos section)
    # Precisamos verificar a estrutura
    TARGET_RC3 = '<div class="rc3-wrapper"'
    TARGET_FAQ = '<section class="faq-section"'
    
    icons_rc3 = [(i, p, a) for (t, i, p, a) in INDEX_ICONS if 'rc3' in t]
    icons_faq = [(i, p, a) for (t, i, p, a) in INDEX_ICONS if 'faq' in t]
    
    if TARGET_RC3 in c:
        icon_html = ''
        for ic, ps, alt in icons_rc3:
            icon_html += '\n    ' + make_icon_html(ic + '.png', ps, alt)
        c = c.replace(TARGET_RC3, icon_html + '\n' + TARGET_RC3, 1)
        print('[OK] index.html: ícones na seção destinos')
    else:
        print('[WARN] index.html: rc3-wrapper não encontrado')
    
    if TARGET_FAQ in c:
        icon_html = ''
        for ic, ps, alt in icons_faq:
            icon_html += '\n    ' + make_icon_html(ic + '.png', ps, alt)
        c = c.replace(TARGET_FAQ, icon_html + '\n' + TARGET_FAQ, 1)
        print('[OK] index.html: ícones na seção FAQ')
    else:
        print('[WARN] index.html: faq-section não encontrado')
    
    # Make RC3 wrapper position relative
    c = c.replace(
        '<div class="rc3-wrapper"',
        '<div class="rc3-wrapper deco-wrap"',
        1
    )
    # Make FAQ section position relative
    c = c.replace(
        '<section class="faq-section"',
        '<section class="faq-section deco-wrap"',
        1
    )
    
    if c != original:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print('[OK] index.html salvo')
except Exception as e:
    print(f'[ERR] index.html: {e}')

print('=== DONE ===')
