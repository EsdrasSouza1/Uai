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
        print(f'FILE NOT FOUND: {page}')
        continue
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    imgs = re.findall(r'src="(foto/[^"]+)"', content)
    print(f'--- {page} ---')
    for img in imgs:
        exists = os.path.exists(img)
        status = 'OK' if exists else 'BROKEN'
        print(f'  [{status}] {img}')
