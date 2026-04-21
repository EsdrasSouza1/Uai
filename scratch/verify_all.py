import re, os

pages = [
    'index.html',
    'passeio-carneiros.html',
    'passeio-maragogi.html',
    'passeio-maragogi-ponta-de-mangue.html',
    'passeio-porto-de-galinhas.html',
    'passeio-cabo-santo-agostinho.html',
    'passeio-ilha-santo-aleixo.html',
    'passeio-milagres.html',
    'passeio-city-tour.html',
    'quem-somos.html',
    'politica-de-privacidade.html',
]

print('=== VERIFICATION REPORT ===\n')
for page in pages:
    if not os.path.exists(page):
        print(f'{page}: FILE NOT FOUND')
        continue
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    has_insta = 'instagram.com/uai_turismo/' in content and 'navMenu' in content
    has_credit = '@Souza.Web_' in content

    pct = re.search(r'<div class="pctrack"[^>]*>(.*?)</div>\s*<button class="pcprev"', content, re.DOTALL)
    slides = len(re.findall(r'<div class="pcs">', pct.group(1))) if pct else 'N/A'

    dots_m = re.search(r'<div class="pcdots"[^>]*>(.*?)</div>', content, re.DOTALL)
    dots = len(re.findall(r'<button class="pcd', dots_m.group(1))) if dots_m else 'N/A'

    ok = 'OK' if (has_insta and has_credit) else 'ISSUE'
    dots_ok = '' if dots == 'N/A' or slides == 'N/A' else (' [DOTS MISMATCH!]' if dots != slides else '')
    print(f'[{ok}] {page}')
    print(f'      Insta nav: {has_insta}  |  Footer credit: {has_credit}  |  Slides: {slides}  |  Dots: {dots}{dots_ok}')
