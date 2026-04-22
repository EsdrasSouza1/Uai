
import os
os.chdir(r'c:\Users\nerds\OneDrive\Área de Trabalho\Uai')

# ============================================================
# 1) "Ver destinos" -> destino aleatório em todos os passeios
# Replace the static back-link with a random redirect button

OLD_BACK = '<a href="index.html#destinos" class="back-link">&#8592; Ver todos os destinos</a>'
NEW_BACK = '''<button onclick="(function(){var d=['passeio-porto-de-galinhas.html','passeio-maragogi.html','passeio-maragogi-ponta-de-mangue.html','passeio-carneiros.html','passeio-cabo-santo-agostinho.html','passeio-ilha-santo-aleixo.html','passeio-milagres.html','passeio-city-tour.html'];var cur=window.location.pathname.split('/').pop();var opts=d.filter(function(x){return x!==cur;});window.location.href=opts[Math.floor(Math.random()*opts.length)];})();" class="back-link" style="background:none;border:none;cursor:pointer;padding:0;font-family:inherit;">&#8592; Ver outro destino</button>'''

files = [
    'passeio-porto-de-galinhas.html',
    'passeio-maragogi.html',
    'passeio-maragogi-ponta-de-mangue.html',
    'passeio-carneiros.html',
    'passeio-cabo-santo-agostinho.html',
    'passeio-ilha-santo-aleixo.html',
    'passeio-milagres.html',
    'passeio-city-tour.html',
]

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        if '&#8592; Ver todos os destinos' in c:
            c2 = c.replace(OLD_BACK, NEW_BACK)
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(c2)
            print(f'[OK] Ver destino aleatorio: {fname}')
        else:
            # Try alternative (some files may use ← directly)
            c2 = c.replace(
                '<a href="index.html#destinos" class="back-link">',
                '<button onclick="(function(){var d=[\'passeio-porto-de-galinhas.html\',\'passeio-maragogi.html\',\'passeio-maragogi-ponta-de-mangue.html\',\'passeio-carneiros.html\',\'passeio-cabo-santo-agostinho.html\',\'passeio-ilha-santo-aleixo.html\',\'passeio-milagres.html\',\'passeio-city-tour.html\'];var cur=window.location.pathname.split(\'/\').pop();var opts=d.filter(function(x){return x!==cur;});window.location.href=opts[Math.floor(Math.random()*opts.length)];})();" class="back-link" style="background:none;border:none;cursor:pointer;padding:0;font-family:inherit;">'
            )
            c2 = c2.replace(
                '&#8592; Ver todos os destinos</a>',
                '&#8592; Ver outro destino</button>'
            )
            if c2 != c:
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write(c2)
                print(f'[OK-alt] Ver destino aleatorio: {fname}')
            else:
                print(f'[SKIP] back-link nao encontrado: {fname}')
    except Exception as e:
        print(f'[ERR] {fname}: {e}')

# ============================================================
# 2) Apresentacao UAI no video section - usar Playfair Display no h2
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        idx = f.read()
    # The video section h2 currently has DM Sans - change to Playfair
    idx = idx.replace(
        "font-family: 'DM Sans', sans-serif; font-size: clamp(2rem, 4vw, 2.8rem); font-weight: 800;",
        "font-family: 'Playfair Display', serif; font-size: clamp(2rem, 4vw, 2.8rem); font-weight: 900;"
    )
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx)
    print('[OK] Apresentacao UAI - fonte Playfair aplicada')
except Exception as e:
    print(f'[ERR] index fonte apresentacao: {e}')

# ============================================================
# 3) Preloader - garantir DM Sans no texto "Turismo" 
# (ja tem Playfair Display na classe .preloader-logo, ok)
# Adicionar font-family no body do index para DM Sans
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        idx = f.read()
    # Ensure body uses DM Sans
    if 'body {' not in idx[:2000]:
        # Add body font-family after <style> opening in head inline styles
        idx = idx.replace(
            '        /* CURSOR */',
            '        body { font-family: \'DM Sans\', sans-serif; }\n\n        /* CURSOR */'
        )
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx)
    print('[OK] body DM Sans garantido no index')
except Exception as e:
    print(f'[ERR] body font: {e}')

# ============================================================
# 4) index.html - section header font (h2 nos destinos)
# Garantir que o h2 "Nossos Destinos" use Playfair
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        idx = f.read()
    # The section-label and section-header h2 should use playfair
    # These are defined in style.css, nothing to change inline
    # But let's add a general rule in the index style block
    idx = idx.replace(
        '        body { font-family: \'DM Sans\', sans-serif; }',
        '''        body { font-family: 'DM Sans', sans-serif; }
        h1, h2, h3, h4 { font-family: 'Playfair Display', serif; }
        .section-header h2, .destinos-section h2, #diferenciais h2, #faq h2 { font-family: 'Playfair Display', serif; }'''
    )
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx)
    print('[OK] fontes h1/h2/h3/h4 padronizadas no index')
except Exception as e:
    print(f'[ERR] fontes headers: {e}')

print('=== CONCLUIDO ===')
