
import os
os.chdir(r'c:\Users\nerds\OneDrive\Área de Trabalho\Uai')

ALL_PAGES = [
    'passeio-porto-de-galinhas.html',
    'passeio-maragogi.html',
    'passeio-maragogi-ponta-de-mangue.html',
    'passeio-carneiros.html',
    'passeio-cabo-santo-agostinho.html',
    'passeio-ilha-santo-aleixo.html',
    'passeio-milagres.html',
    'passeio-city-tour.html',
    'index.html',
]

# Mapeamento CORRETO: foto para cada destino no carrossel "Outros Roteiros"
# (e também nas galerias de cada página)
FOTO_MAP = {
    # Cabo - usa a foto específica de carrossel
    'foto/Cabo de Santo Agostinho Passeios de Buggy/image-0 (1).jpeg':
        'foto/Cabo de Santo Agostinho Passeios de Buggy/Foto carrossel - Cabo de Santo Agostinho.jpeg',
    'foto/Cabo de Santo Agostinho Passeios de Buggy/image-1.jpeg':
        'foto/Cabo de Santo Agostinho Passeios de Buggy/Foto carrossel - Cabo de Santo Agostinho.jpeg',
    # Milagres - carrossel usa a foto "Foto Carrossel"
    'foto/milagres/Foto capa passeio, galeria - Milagres.jpeg':
        'foto/milagres/Foto Carrossel - Milagres.jpeg',
    # Citytour - carrossel usa a foto "Foto Carrossel"
    'foto/Citytour Recife e Olinda/Foto capa passeio e galeria - Citytour.jpg':
        'foto/Citytour Recife e Olinda/Foto Carrossel - Citytour.JPEG',
}

# Mas ATENÇÃO: no rc-card (Outros Roteiros) de cada página, precisamos usar as fotos certas
# Vamos fazer a substituição diretamente no contexto dos rc-cards

for fname in ALL_PAGES:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        original = c

        # Para o carrossel "Outros Roteiros" (rc-card), usar fotos específicas por destino:

        # Cabo de Santo Agostinho no rc-card
        c = c.replace(
            'src="foto/Cabo de Santo Agostinho Passeios de Buggy/image-1.jpeg" alt="Cabo de Santo Agostinho"',
            'src="foto/Cabo de Santo Agostinho Passeios de Buggy/Foto carrossel - Cabo de Santo Agostinho.jpeg" alt="Cabo de Santo Agostinho"'
        )

        # Milagres no rc-card - usar Foto Carrossel
        c = c.replace(
            'src="foto/milagres/Foto capa passeio, galeria - Milagres.jpeg" alt="São Miguel dos Milagres"',
            'src="foto/milagres/Foto Carrossel - Milagres.jpeg" alt="São Miguel dos Milagres"'
        )

        # Citytour no rc-card - usar Foto Carrossel
        c = c.replace(
            'src="foto/Citytour Recife e Olinda/Foto capa passeio e galeria - Citytour.jpg" alt="City Tour Recife e Olinda"',
            'src="foto/Citytour Recife e Olinda/Foto Carrossel - Citytour.JPEG" alt="City Tour Recife e Olinda"'
        )
        # variação sem alt especifico
        c = c.replace(
            'src="foto/Citytour Recife e Olinda/principal.jpeg" alt="City Tour Recife e Olinda"',
            'src="foto/Citytour Recife e Olinda/Foto Carrossel - Citytour.JPEG" alt="City Tour Recife e Olinda"'
        )

        if c != original:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f'[OK] carrossel outros roteiros: {fname}')
        else:
            print(f'[--] sem mudanca: {fname}')
    except Exception as e:
        print(f'[ERR] {fname}: {e}')

# ============================================================
# POLITICA DE PRIVACIDADE - Navbar padrão completo
# ============================================================

NAV_PADRAO = '''  <!-- NAV -->
  <nav id="nav">
    <a class="nav-logo" href="index.html">
      <img src="foto/logoo.png" alt="Uai Turismo" class="nav-logo-img">
    </a>
    <button class="nav-toggle" id="navToggle" aria-label="Abrir menu"><span></span><span></span><span></span></button>
    <ul id="navMenu">
      <li><a href="index.html#hero">Início</a></li>
      <li><a href="index.html#destinos">Destinos</a></li>
      <li><a href="index.html#galeria">Galeria</a></li>
      <li><a href="index.html#faq">Dúvidas</a></li>
      <li><a href="quem-somos.html">Sobre nós</a></li>
      <li><a href="https://uaiturismo.surishop.ai/catalog" target="_blank">Catálogo</a></li>
      <li><a href="https://www.instagram.com/uai_turismo/" target="_blank" aria-label="Instagram" title="@uai_turismo" style="display:flex;align-items:center;padding:4px 8px;color:rgba(255,255,255,.75);transition:color .2s" onmouseover="this.style.color='#FFD166'" onmouseout="this.style.color='rgba(255,255,255,.75)'"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg></a></li>
      <li><a href="https://wa.me/5581997484915?text=Olá%2C%20vim%20pelo%20site%20e%20gostaria%20de%20saber%20mais" class="nav-cta" target="_blank"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z" /></svg> Solicitar Orçamento</a></li>
    </ul>
  </nav>'''

NAV_CSS_EXTRA = '''
    <link rel="stylesheet" href="style.css" />
    <link rel="stylesheet" href="style-upgrade.css" />
    <style>
      #cursor-dot, #cursor-ring { position: fixed; top: 0; left: 0; border-radius: 50%; pointer-events: none; z-index: 99999; transform: translate(-50%, -50%); transition-property: opacity, background, border-color, transform; transition-timing-function: ease; }
      #cursor-dot { width: 8px; height: 8px; background: var(--amber); transition-duration: .08s; }
      #cursor-ring { width: 36px; height: 36px; border: 2px solid rgba(245,168,0,.5); background: transparent; transition-duration: .18s; }
    </style>
    <style id="nav-mobile-fix">@media (max-width: 768px) {
      #navMenu { display: flex !important; position: fixed !important; top: 0 !important; left: 0 !important; right: 0 !important; bottom: 0 !important; width: 100% !important; height: 100% !important; z-index: 99990 !important; background: var(--teal-deeper) !important; flex-direction: column !important; align-items: center !important; justify-content: center !important; gap: 8px !important; transform: none !important; opacity: 0; visibility: hidden; pointer-events: none; transition: opacity 0.35s ease, visibility 0.35s ease; }
      #navMenu.open { opacity: 1 !important; visibility: visible !important; pointer-events: all !important; }
      #navMenu li { width: 100%; text-align: center; }
      #navMenu li a { display: block; font-size: 1.2rem !important; padding: 14px 24px !important; color: white !important; border-radius: 12px; transition: background 0.2s ease; }
      #navMenu li a:hover { background: rgba(255,255,255,0.10); }
      #navMenu .nav-cta { background: var(--amber) !important; color: var(--text) !important; border-radius: 50px !important; font-weight: 700 !important; margin-top: 8px; display: inline-flex !important; width: auto !important; padding: 12px 28px !important; }
      .nav-toggle { z-index: 99995 !important; position: relative; }
      #nav { z-index: 99992 !important; }
    }</style>'''

NAV_SCRIPT = '''
  <div id="cursor-dot"></div>
  <div id="cursor-ring"></div>
  <script>
    const dot = document.getElementById('cursor-dot'), ring = document.getElementById('cursor-ring');
    if (window.matchMedia('(pointer: fine)').matches) { document.addEventListener('mousemove', e => { dot.style.left = e.clientX + 'px'; dot.style.top = e.clientY + 'px'; ring.style.left = e.clientX + 'px'; ring.style.top = e.clientY + 'px'; }); }
    (function () {
      var nt = document.getElementById('navToggle'), nm = document.getElementById('navMenu'), nav = document.getElementById('nav');
      if (!nt || !nm) return;
      var newT = nt.cloneNode(true); nt.parentNode.replaceChild(newT, nt); nt = newT;
      nt.addEventListener('click', function () { var o = nm.classList.toggle('open'); nt.classList.toggle('open', o); nt.setAttribute('aria-expanded', o); document.body.style.overflow = o ? 'hidden' : ''; document.documentElement.style.overflow = o ? 'hidden' : ''; });
      nm.querySelectorAll('a').forEach(function (l) { l.addEventListener('click', function () { nm.classList.remove('open'); nt.classList.remove('open'); nt.setAttribute('aria-expanded', false); document.body.style.overflow = ''; document.documentElement.style.overflow = ''; }); });
      if (nav) window.addEventListener('scroll', function () { nav.classList.toggle('scrolled', window.scrollY > 60); }, { passive: true });
    })();
  </script>'''

try:
    with open('politica-de-privacidade.html', 'r', encoding='utf-8') as f:
        pol = f.read()

    # 1) Substituir o nav simples pelo nav completo
    OLD_NAV = '''    <!-- NAV -->
    <nav id="nav">
        <a href="index.html">
            <img src="foto/logoo.png" alt="Uai Turismo" class="logo-img">
        </a>
        <a href="index.html" class="nav-back">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
            Voltar ao site
        </a>
        <a href="https://uaiturismo.surishop.ai/catalog" target="_blank" class="nav-back">Catálogo</a>
    </nav>'''

    if OLD_NAV in pol:
        pol = pol.replace(OLD_NAV, NAV_PADRAO)
        print('[OK] Nav substituido')
    else:
        print('[SKIP] Nav nao encontrado exatamente')

    # 2) Adicionar CSS do nav e cursor antes de </head>
    if 'nav-mobile-fix' not in pol:
        pol = pol.replace('</head>', NAV_CSS_EXTRA + '\n</head>', 1)
        print('[OK] CSS nav adicionado')

    # 3) Adicionar cursor divs e script após <body>
    if 'cursor-dot' not in pol:
        pol = pol.replace('<body>\n', '<body>\n' + NAV_SCRIPT + '\n', 1)
        print('[OK] Script cursor/nav adicionado')

    with open('politica-de-privacidade.html', 'w', encoding='utf-8') as f:
        f.write(pol)
    print('[OK] politica-de-privacidade.html atualizado')
except Exception as e:
    print(f'[ERR] politica: {e}')

print('=== DONE ===')
