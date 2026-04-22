
import os
os.chdir(r'c:\Users\nerds\OneDrive\Área de Trabalho\Uai')

MOBILE_FIX = b"""
    @media(max-width:600px) {
      .pinc li { flex-direction: column; gap: 4px; }
      .pinc li .ii { margin-top: 0; }
      .pbody { padding: 36px 4%; }
      .pinc { padding: 22px 18px; }
      .ph { padding: 100px 5%% 60px; }
      .pcprev, .pcnext { width: 36px; height: 36px; font-size: .9rem; }
    }"""

MOBILE_FIX = b"""
    @media(max-width:600px) {
      .pinc li { flex-direction: column; gap: 4px; }
      .pinc li .ii { margin-top: 0; }
      .pbody { padding: 36px 4%; }
      .pinc { padding: 22px 18px; }
      .ph { padding: 100px 5%% 60px; }
    }"""

# Use raw bytes to avoid encoding issues
# The pattern found: `}\r\n  </style>\r\n  </style>`
# We insert before the inner </style>

files = [
    'passeio-cabo-santo-agostinho.html',
    'passeio-ilha-santo-aleixo.html',
    'passeio-maragogi-ponta-de-mangue.html',
]

MARKER = b'  </style>\r\n  </style>'
INSERT = b"""
    @media(max-width:600px) {
      .pinc li { flex-direction: column; gap: 4px; }
      .pinc li .ii { margin-top: 0; }
      .pbody { padding: 36px 4%; }
      .pinc { padding: 22px 18px; }
    }
  </style>\r\n  </style>"""

for fname in files:
    try:
        with open(fname, 'rb') as f:
            raw = f.read()
        if b'pinc li { flex-direction' in raw:
            print(f'[SKIP] ja tem fix: {fname}')
            continue
        if MARKER in raw:
            raw2 = raw.replace(MARKER, INSERT, 1)
            with open(fname, 'wb') as f:
                f.write(raw2)
            print(f'[OK] mobile fix: {fname}')
        else:
            print(f'[SKIP] marker nao encontrado: {fname}')
            # show context
            idx = raw.find(b'</style>')
            print(f'  First </style> at {idx}: {raw[idx-10:idx+50]}')
    except Exception as e:
        print(f'[ERR] {fname}: {e}')

print('=== DONE ===')
