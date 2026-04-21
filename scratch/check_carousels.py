import re, os

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

for page in pages:
    if not os.path.exists(page):
        print(f'NOT FOUND: {page}')
        continue
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count pctrack pcs divs
    pct_match = re.search(r'<div class="pctrack"[^>]*>(.*?)</div>\s*<button class="pcprev"', content, re.DOTALL)
    if pct_match:
        slides = re.findall(r'<div class="pcs">', pct_match.group(1))
        print(f'{page}: {len(slides)} slides in pctrack')
    else:
        print(f'{page}: NO pctrack found')
