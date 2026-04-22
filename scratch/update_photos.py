
import os
os.chdir(r'c:\Users\nerds\OneDrive\Área de Trabalho\Uai')

# ============================================================
# 1) ILHA DE SANTO ALEIXO
# Foto galeria e capa = "Foto galeria e capa do passeio - Ilha de Santo Aleixo.jpg"
# ============================================================
try:
    with open('passeio-ilha-santo-aleixo.html', 'r', encoding='utf-8') as f:
        c = f.read()

    nova = 'foto/Santo Aleixo/Foto galeria e capa do passeio - Ilha de Santo Aleixo.jpg'

    # Capa hero (background-image no CSS inline do .ph::before)
    c = c.replace(
        "url('foto/Santo Aleixo/image-10.jpeg')",
        f"url('{nova}')"
    )
    c = c.replace(
        "url('foto/Santo Aleixo/IMG_2395.jpg')",
        f"url('{nova}')"
    )
    c = c.replace(
        "url('foto/Santo Aleixo/image-1.jpeg')",
        f"url('{nova}')"
    )

    # Primeiro slide do carrossel
    c = c.replace(
        'src="foto/Santo Aleixo/image-1.jpeg"',
        f'src="{nova}"'
    )
    c = c.replace(
        'src="foto/Santo Aleixo/IMG_2395.jpg"',
        f'src="{nova}"'
    )
    c = c.replace(
        'src="foto/Santo Aleixo/image-10.jpeg"',
        f'src="{nova}"'
    )

    with open('passeio-ilha-santo-aleixo.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('[OK] Ilha Santo Aleixo - fotos atualizadas')
except Exception as e:
    print(f'[ERR] Santo Aleixo: {e}')

# ============================================================
# 2) CABO DE SANTO AGOSTINHO
# Foto carrossel = "Foto carrossel - Cabo de Santo Agostinho.jpeg"
# ============================================================
try:
    with open('passeio-cabo-santo-agostinho.html', 'r', encoding='utf-8') as f:
        c = f.read()

    nova_cabo = 'foto/Cabo de Santo Agostinho Passeios de Buggy/Foto carrossel - Cabo de Santo Agostinho.jpeg'

    # Substitui o primeiro slide do carrossel
    c = c.replace(
        'src="foto/Cabo de Santo Agostinho Passeios de Buggy/image-0 (1).jpeg"',
        f'src="{nova_cabo}"'
    )

    with open('passeio-cabo-santo-agostinho.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('[OK] Cabo de Santo Agostinho - foto carrossel atualizada')
except Exception as e:
    print(f'[ERR] Cabo: {e}')

# ============================================================
# 3) CITYTOUR
# Foto Carrossel = "Foto Carrossel - Citytour.JPEG"
# Foto capa passeio e galeria = "Foto capa passeio e galeria - Citytour.jpg"
# ============================================================
try:
    with open('passeio-city-tour.html', 'r', encoding='utf-8') as f:
        c = f.read()

    nova_capa_ct = 'foto/Citytour Recife e Olinda/Foto capa passeio e galeria - Citytour.jpg'
    nova_carrossel_ct = 'foto/Citytour Recife e Olinda/Foto Carrossel - Citytour.JPEG'

    # Capa hero (bg image)
    c = c.replace(
        "url('foto/Citytour Recife e Olinda/principal.jpeg')",
        f"url('{nova_capa_ct}')"
    )

    # Primeiro slide carrossel (principal.jpeg -> nova capa)
    c = c.replace(
        'src="foto/Citytour Recife e Olinda/principal.jpeg" alt="Recife Antigo"',
        f'src="{nova_capa_ct}" alt="City Tour Recife e Olinda"'
    )

    # Segundo slide carrossel (image-2.jpeg -> nova foto carrossel)
    c = c.replace(
        'src="foto/Citytour Recife e Olinda/image-2.jpeg" alt="Olinda"',
        f'src="{nova_carrossel_ct}" alt="City Tour Recife e Olinda"'
    )

    with open('passeio-city-tour.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('[OK] City Tour - fotos atualizadas')
except Exception as e:
    print(f'[ERR] CityTour: {e}')

# ============================================================
# 4) MILAGRES
# Foto Carrossel = "Foto Carrossel - Milagres.jpeg"
# Foto capa passeio, galeria = "Foto capa passeio, galeria - Milagres.jpeg"
# ============================================================
try:
    with open('passeio-milagres.html', 'r', encoding='utf-8') as f:
        c = f.read()

    nova_capa_mil = 'foto/milagres/Foto capa passeio, galeria - Milagres.jpeg'
    nova_carrossel_mil = 'foto/milagres/Foto Carrossel - Milagres.jpeg'

    # Capa hero (bg image) - find current hero bg
    for old in [
        "url('foto/milagres/IMG_0303.jpg')",
        "url('foto/milagres/IMG_2767.jpg')",
        "url('foto/milagres/IMG_0997.jpg')",
    ]:
        c = c.replace(old, f"url('{nova_capa_mil}')")

    # Primeiro slide carrossel -> nova capa
    for old in [
        'src="foto/milagres/IMG_0303.jpg"',
        'src="foto/milagres/IMG_2767.jpg"',
        'src="foto/milagres/IMG_0997.jpg"',
    ]:
        if old in c:
            c = c.replace(old, f'src="{nova_capa_mil}"', 1)
            break

    # Segundo slide carrossel -> nova foto carrossel
    for old in [
        'src="foto/milagres/IMG_2773.jpg"',
        'src="foto/milagres/IMG_2809.jpg"',
        'src="foto/milagres/IMG_9090.jpg"',
        'src="foto/milagres/Sem título-1.JPG"',
    ]:
        if old in c:
            c = c.replace(old, f'src="{nova_carrossel_mil}"', 1)
            break

    with open('passeio-milagres.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('[OK] Milagres - fotos atualizadas')
except Exception as e:
    print(f'[ERR] Milagres: {e}')

# ============================================================
# 5) MARAGOGI BARRA GRANDE
# Foto Capa passeio, galeria = "Foto Capa passeio, galeria - Maragogi Barra Grande.jpeg"
# ============================================================
try:
    with open('passeio-maragogi.html', 'r', encoding='utf-8') as f:
        c = f.read()

    nova_capa_mar = 'foto/Maragogi - Barra Grande/Foto Capa passeio, galeria - Maragogi Barra Grande.jpeg'

    # Capa hero bg
    for old in [
        "url('foto/Maragogi - Barra Grande/image-7.jpeg')",
        "url('foto/Maragogi - Barra Grande/image-0.jpeg')",
        "url('foto/Maragogi - Barra Grande/image-6.jpeg')",
    ]:
        c = c.replace(old, f"url('{nova_capa_mar}')")

    # Primeiro slide carrossel
    for old in [
        'src="foto/Maragogi - Barra Grande/image-7.jpeg"',
        'src="foto/Maragogi - Barra Grande/image-0.jpeg"',
        'src="foto/Maragogi - Barra Grande/image-6.jpeg"',
    ]:
        if old in c:
            c = c.replace(old, f'src="{nova_capa_mar}"', 1)
            break

    with open('passeio-maragogi.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('[OK] Maragogi Barra Grande - fotos atualizadas')
except Exception as e:
    print(f'[ERR] Maragogi: {e}')

# ============================================================
# 6) CARNEIROS
# Foto capa passeio, galeria = "Foto capa passeio, galeria - Carneiros.jpeg"
# ============================================================
try:
    with open('passeio-carneiros.html', 'r', encoding='utf-8') as f:
        c = f.read()

    nova_capa_car = 'foto/carneiros/Foto capa passeio, galeria - Carneiros.jpeg'

    # Capa hero bg
    for old in [
        "url('foto/carneiros/image-18.jpeg')",
        "url('foto/carneiros/image-17.jpeg')",
        "url('foto/carneiros/Carneiros 1.jpeg')",
        "url('foto/carneiros/image-6.jpeg')",
    ]:
        c = c.replace(old, f"url('{nova_capa_car}')")

    # Primeiro slide carrossel
    for old in [
        'src="foto/carneiros/image-18.jpeg"',
        'src="foto/carneiros/Carneiros 1.jpeg"',
        'src="foto/carneiros/image-17.jpeg"',
    ]:
        if old in c:
            c = c.replace(old, f'src="{nova_capa_car}"', 1)
            break

    with open('passeio-carneiros.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('[OK] Carneiros - fotos atualizadas')
except Exception as e:
    print(f'[ERR] Carneiros: {e}')

# ============================================================
# 7) INDEX.HTML - atualizar fotos nos cards de destinos e carrossel
# ============================================================
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        c = f.read()

    # Carneiros
    c = c.replace(
        'src="foto/carneiros/image-18.jpeg"',
        'src="foto/carneiros/Foto capa passeio, galeria - Carneiros.jpeg"'
    )
    # Milagres
    c = c.replace(
        'src="foto/milagres/IMG_2767.jpg"',
        'src="foto/milagres/Foto capa passeio, galeria - Milagres.jpeg"'
    )
    # Maragogi Barra Grande
    c = c.replace(
        'src="foto/Maragogi - Barra Grande/image-7.jpeg"',
        'src="foto/Maragogi - Barra Grande/Foto Capa passeio, galeria - Maragogi Barra Grande.jpeg"'
    )
    # Santo Aleixo
    c = c.replace(
        'src="foto/Santo Aleixo/IMG_2395.jpg"',
        'src="foto/Santo Aleixo/Foto galeria e capa do passeio - Ilha de Santo Aleixo.jpg"'
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('[OK] index.html - fotos dos cards atualizadas')
except Exception as e:
    print(f'[ERR] index: {e}')

# ============================================================
# 8) OUTROS ROTEIROS - atualizar fotos nos carrosseis de cada página
# ============================================================
all_pages = [
    'passeio-porto-de-galinhas.html',
    'passeio-maragogi.html',
    'passeio-maragogi-ponta-de-mangue.html',
    'passeio-carneiros.html',
    'passeio-cabo-santo-agostinho.html',
    'passeio-ilha-santo-aleixo.html',
    'passeio-milagres.html',
    'passeio-city-tour.html',
]

replacements = {
    'src="foto/carneiros/image-18.jpeg"': 'src="foto/carneiros/Foto capa passeio, galeria - Carneiros.jpeg"',
    'src="foto/milagres/IMG_0303.jpg"': 'src="foto/milagres/Foto capa passeio, galeria - Milagres.jpeg"',
    'src="foto/milagres/IMG_2767.jpg"': 'src="foto/milagres/Foto capa passeio, galeria - Milagres.jpeg"',
    'src="foto/Maragogi - Barra Grande/image-7.jpeg"': 'src="foto/Maragogi - Barra Grande/Foto Capa passeio, galeria - Maragogi Barra Grande.jpeg"',
    'src="foto/Santo Aleixo/image-10.jpeg"': 'src="foto/Santo Aleixo/Foto galeria e capa do passeio - Ilha de Santo Aleixo.jpg"',
    'src="foto/Santo Aleixo/IMG_2395.jpg"': 'src="foto/Santo Aleixo/Foto galeria e capa do passeio - Ilha de Santo Aleixo.jpg"',
    'src="foto/Citytour Recife e Olinda/principal.jpeg"': 'src="foto/Citytour Recife e Olinda/Foto capa passeio e galeria - Citytour.jpg"',
}

for fname in all_pages:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        original = c
        for old, new in replacements.items():
            c = c.replace(old, new)
        if c != original:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f'[OK] outros roteiros atualizados: {fname}')
    except Exception as e:
        print(f'[ERR] {fname}: {e}')

print('=== CONCLUIDO ===')
