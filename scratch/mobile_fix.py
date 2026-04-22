
import os
os.chdir(r'c:\Users\nerds\OneDrive\Área de Trabalho\Uai')

MOBILE_FIX = """
      /* Fix roteiro mobile */
      .pinc li {
        flex-direction: column;
        gap: 4px;
      }
      .pinc li .ii {
        margin-top: 0;
      }
      .pinc li span:last-child {
        padding-left: 0;
      }
      .pbody {
        padding: 36px 4%;
      }
      .pinc {
        padding: 22px 18px;
      }"""

# Target: the closing brace of the @media(max-width:600px) block
OLD_MEDIA = """      .pcprev,
      .pcnext {
        width: 36px;
        height: 36px;
        font-size: .9rem;
      }
    }"""

NEW_MEDIA = """      .pcprev,
      .pcnext {
        width: 36px;
        height: 36px;
        font-size: .9rem;
      }
""" + MOBILE_FIX + """
    }"""

files = [
    'passeio-porto-de-galinhas.html',
    'passeio-maragogi-ponta-de-mangue.html',
    'passeio-carneiros.html',
    'passeio-cabo-santo-agostinho.html',
    'passeio-ilha-santo-aleixo.html',
    'passeio-milagres.html',
]

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        if OLD_MEDIA in c:
            c2 = c.replace(OLD_MEDIA, NEW_MEDIA, 1)
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(c2)
            print(f'[OK] mobile fix: {fname}')
        elif 'Fix roteiro mobile' in c:
            print(f'[SKIP] ja tem fix: {fname}')
        else:
            # Try compact version (single line in some files)
            OLD_COMPACT = """.pcprev,
      .pcnext { width: 36px; height: 36px; font-size: .9rem; }
    }"""
            if OLD_COMPACT in c:
                c2 = c.replace(OLD_COMPACT, """.pcprev,
      .pcnext { width: 36px; height: 36px; font-size: .9rem; }
""" + MOBILE_FIX + """
    }""", 1)
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write(c2)
                print(f'[OK-compact] mobile fix: {fname}')
            else:
                print(f'[SKIP] media block nao encontrado: {fname}')
    except Exception as e:
        print(f'[ERR] {fname}: {e}')

# Also fix city-tour (different structure - no .pcprev in media block)
try:
    fname = 'passeio-city-tour.html'
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'Fix roteiro mobile' not in c:
        # Add a separate media block before </style>
        FIX = """
    @media(max-width:600px) {
      .pinc li { flex-direction: column; gap: 4px; }
      .pinc li .ii { margin-top: 0; }
      .pbody { padding: 36px 4%; }
      .pinc { padding: 22px 18px; }
    }
  </style>"""
        c2 = c.replace('  </style>\n\n    <style>\n        .floating-wpp', FIX + '\n\n    <style>\n        .floating-wpp', 1)
        if c2 != c:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(c2)
            print(f'[OK] mobile fix city-tour')
        else:
            print(f'[SKIP] city-tour: nao encontrou ponto de insercao')
except Exception as e:
    print(f'[ERR] city-tour: {e}')

print('=== DONE ===')
