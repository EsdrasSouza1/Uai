import re, os

# ─── 4th slide for each tour page ───────────────────────────────────────────
FOURTH_SLIDES = {
    'passeio-carneiros.html':               ('foto/carneiros/image-6.jpeg',                                           'Praia dos Carneiros foto 4'),
    'passeio-maragogi.html':                ('foto/Maragogi - Barra Grande/image-6.jpeg',                            'Maragogi Barra Grande foto 4'),
    'passeio-maragogi-ponta-de-mangue.html':('foto/Maragogi - Ponta de Mangue/image-4.jpeg',                         'Maragogi Ponta de Mangue foto 4'),
    'passeio-porto-de-galinhas.html':       ('foto/Passeio Buggy - Porto de Galinhas/image-13.jpeg',                 'Porto de Galinhas foto 4'),
    'passeio-cabo-santo-agostinho.html':    ('foto/Cabo de Santo Agostinho Passeios de Buggy/image-5.jpeg',          'Cabo de Santo Agostinho foto 4'),
    'passeio-ilha-santo-aleixo.html':       ('foto/Santo Aleixo/image-3.jpeg',                                       'Ilha de Santo Aleixo foto 4'),
    'passeio-milagres.html':                ('foto/milagres/IMG_2767.jpg',                                           'São Miguel dos Milagres foto 4'),
    'passeio-city-tour.html':               ('foto/Citytour Recife e Olinda/image-8.jpeg',                           'City Tour Recife e Olinda foto 4'),
}

# ─── Instagram nav li ────────────────────────────────────────────────────────
INSTA_LI = '''<li><a href="https://www.instagram.com/uai_turismo/" target="_blank" aria-label="Instagram" title="@uai_turismo" style="display:flex;align-items:center;padding:4px 8px;color:rgba(255,255,255,.75);transition:color .2s" onmouseover="this.style.color='#FFD166'" onmouseout="this.style.color='rgba(255,255,255,.75)'"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg></a></li>'''

# ─── Footer developer credit ─────────────────────────────────────────────────
DEV_CREDIT = '\n      <p style="margin-top:6px;font-size:.72rem;color:rgba(255,255,255,.3);">Desenvolvido por <a href="https://www.instagram.com/Souza.Web_/" target="_blank" style="color:rgba(255,255,255,.4);transition:color .3s" onmouseover="this.style.color=\'#FFD166\'" onmouseout="this.style.color=\'rgba(255,255,255,.4)\'">@Souza.Web_</a></p>'

# ─── All HTML files ───────────────────────────────────────────────────────────
all_html = [f for f in os.listdir('.') if f.endswith('.html')]

def apply_nav_instagram(content, filename):
    """Insert Instagram icon right before the WhatsApp nav-cta li"""
    if 'nav-insta-link' in content:
        return content, False  # already added
    # Insert before the WhatsApp CTA li
    target = '<li><a href="https://wa.me/5581997484915'
    if target in content:
        content = content.replace(target, INSTA_LI + '\n      ' + target, 1)
        return content, True
    # Fallback: insert after Catálogo li
    target2 = 'target="_blank">Catálogo</a></li>'
    if target2 in content:
        content = content.replace(target2, target2 + '\n      ' + INSTA_LI, 1)
        return content, True
    return content, False

def apply_footer_credit(content, filename):
    """Add developer credit inside footer-bottom"""
    if '@Souza.Web_' in content:
        return content, False  # already added
    # Look for the copyright paragraph end in footer-bottom
    target = '</p>\n    </div>\n  </footer>'
    if target in content:
        content = content.replace(target, DEV_CREDIT + '\n    </div>\n  </footer>', 1)
        return content, True
    # Alternative pattern
    target2 = '</p>\n  </div>\n  </footer>'
    if target2 in content:
        content = content.replace(target2, DEV_CREDIT + '\n  </div>\n  </footer>', 1)
        return content, True
    # Try broader pattern: find footer-bottom closing
    m = re.search(r'(class="footer-bottom"[^>]*>.*?</p>)(\s*</div>\s*</footer>)', content, re.DOTALL)
    if m:
        content = content[:m.end(1)] + DEV_CREDIT + content[m.start(2):]
        return content, True
    return content, False

def apply_fourth_slide(content, filename):
    """Add 4th carousel slide if only 3 exist"""
    if filename not in FOURTH_SLIDES:
        return content, False

    img_src, img_alt = FOURTH_SLIDES[filename]

    # Find the pctrack section
    pct_match = re.search(r'(<div class="pctrack"[^>]*>)(.*?)(</div>\s*<button class="pcprev")', content, re.DOTALL)
    if not pct_match:
        print(f'  [SKIP] No pctrack in {filename}')
        return content, False

    track_content = pct_match.group(2)
    slides = re.findall(r'<div class="pcs">', track_content)

    if len(slides) >= 4:
        print(f'  [OK] Already {len(slides)} slides in {filename}')
        return content, False

    # Build new slide
    new_slide = f'\n                <div class="pcs">\n                  <img src="{img_src}" alt="{img_alt}" loading="lazy">\n                </div>'

    # Insert 4th slide at end of pctrack content
    new_track_content = track_content.rstrip() + new_slide + '\n              '

    # Replace in full content
    content = content[:pct_match.start(2)] + new_track_content + content[pct_match.end(2):]

    # Update count display "1 / 3" -> "1 / 4"
    content = re.sub(r'(\d+) / 3', lambda m: m.group(1) + ' / 4', content, count=1)

    # Add 4th dot to pcdots (insert before closing </div> of pcdots section)
    new_dot = '<button class="pcd" data-i="3" aria-label="Foto 4"></button>'
    content = re.sub(
        r'(class="pcd" data-i="2"[^>]*></button>)(\s*</div>)',
        lambda m: m.group(1) + new_dot + m.group(2),
        content, count=1
    )

    # Update JS total from 3 to 4
    content = re.sub(r'const total = 3;', 'const total = 4;', content, count=1)

    return content, True

# ─── Process all HTML files ───────────────────────────────────────────────────
for filename in sorted(all_html):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    content, changed = apply_nav_instagram(content, filename)
    if changed: changes.append('nav Instagram')

    content, changed = apply_footer_credit(content, filename)
    if changed: changes.append('footer credit')

    content, changed = apply_fourth_slide(content, filename)
    if changed: changes.append('4th slide')

    if content != original:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[SAVED] {filename}: {", ".join(changes)}')
    else:
        print(f'[SKIP]  {filename}: nothing to change')
