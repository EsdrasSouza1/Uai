
import os
os.chdir(r'c:\Users\nerds\OneDrive\Área de Trabalho\Uai')

# Esses 3 arquivos usam CSS compacto sem bloco @media(max-width:600px)
# Vamos inserir um bloco antes do </style> principal

MOBILE_FIX = """
    @media(max-width:600px) {
      .pinc li { flex-direction: column; gap: 4px; }
      .pinc li .ii { margin-top: 0; }
      .pbody { padding: 36px 4%; }
      .pinc { padding: 22px 18px; }
      .ph { padding: 100px 5% 60px; }
      .pcprev, .pcnext { width: 36px; height: 36px; font-size: .9rem; }
    }"""

files = [
    'passeio-maragogi-ponta-de-mangue.html',
    'passeio-cabo-santo-agostinho.html',
    'passeio-ilha-santo-aleixo.html',
]

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()

        if 'Fix roteiro mobile' in c or 'flex-direction: column' in c:
            print(f'[SKIP] ja tem fix: {fname}')
            continue

        # Esses arquivos tem um <style> principal que termina com
        # .outro-overlay a:hover { color:white; }
        # e depois </style> (pode ser com ou sem newline)
        # Vamos inserir antes do </style> que fecha o bloco principal

        # Encontra o marcador: o </style> logo antes da segunda <style> do wpp
        marker = "  </style>\n\n    <style>\n        .floating-wpp"
        if marker in c:
            c2 = c.replace(marker, MOBILE_FIX + "\n  </style>\n\n    <style>\n        .floating-wpp", 1)
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(c2)
            print(f'[OK] mobile fix: {fname}')
        else:
            # Try alternative closing
            alt = "</style>\n\n    <style>\n        .floating-wpp"
            if alt in c:
                c2 = c.replace(alt, MOBILE_FIX + "\n  </style>\n\n    <style>\n        .floating-wpp", 1)
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write(c2)
                print(f'[OK-alt] mobile fix: {fname}')
            else:
                # Last resort: find the nav-mobile-fix style tag
                nav_marker = '<style id="nav-mobile-fix">'
                if nav_marker in c:
                    c2 = c.replace(nav_marker, MOBILE_FIX + "\n    <style id=\"nav-mobile-fix\">", 1)
                    with open(fname, 'w', encoding='utf-8') as f:
                        f.write(c2)
                    print(f'[OK-nav] mobile fix: {fname}')
                else:
                    print(f'[SKIP] nao encontrou ponto: {fname}')
    except Exception as e:
        print(f'[ERR] {fname}: {e}')

print('=== DONE ===')
