
import os
os.chdir(r'c:\Users\nerds\OneDrive\Área de Trabalho\Uai')

checks = [
    ('passeio-cabo-santo-agostinho.html', 'Foto carrossel - Cabo de Santo Agostinho.jpeg'),
    ('passeio-milagres.html', 'Foto Carrossel - Milagres.jpeg'),
    ('passeio-city-tour.html', 'Foto Carrossel - Citytour.JPEG'),
    ('passeio-carneiros.html', 'Foto capa passeio, galeria - Carneiros.jpeg'),
    ('passeio-maragogi.html', 'Foto Capa passeio, galeria - Maragogi Barra Grande.jpeg'),
    ('passeio-ilha-santo-aleixo.html', 'Foto galeria e capa do passeio - Ilha de Santo Aleixo.jpg'),
    ('index.html', 'Foto Carrossel - Citytour.JPEG'),
    ('politica-de-privacidade.html', 'navToggle'),
    ('politica-de-privacidade.html', 'nav-logo'),
]
for fname, term in checks:
    with open(fname, 'rb') as f:
        raw = f.read()
    found = term.encode('utf-8') in raw
    status = 'OK' if found else 'MISS'
    print(status + ' | ' + fname + ': ' + term[:45])
