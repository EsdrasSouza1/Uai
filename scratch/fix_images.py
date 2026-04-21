import os

pages = [
    'passeio-carneiros.html',
    'passeio-maragogi.html',
    'passeio-maragogi-ponta-de-mangue.html',
    'passeio-porto-de-galinhas.html',
    'passeio-cabo-santo-agostinho.html',
    'passeio-ilha-santo-aleixo.html',
    'passeio-milagres.html',
    'passeio-city-tour.html',
    'index.html',
]

# Global src replacements across all pages
src_fixes = {
    # Carneiros - "Carneiros Capela.jpg" doesn't exist
    'foto/carneiros/Carneiros Capela.jpg': 'foto/carneiros/image-18.jpeg',
    # Carneiros - IMG_3079 doesn't exist
    'foto/carneiros/IMG_3079.JPG': 'foto/carneiros/image-17.jpeg',
    # Old maragogi folder path (wrong folder name)
    'foto/maragogi/Maragogi Ponta de Mangue (4) (1).JPEG': 'foto/Maragogi - Ponta de Mangue/image-8.jpeg',
    'foto/maragogi/IMG_9109.jpg': 'foto/Maragogi - Ponta de Mangue/image-10.jpeg',
    'foto/maragogi/IMG_4327.JPG': 'foto/Maragogi - Ponta de Mangue/image-17.jpeg',
    # Porto de Galinhas - wrong folder name "porto galinha"
    'foto/porto galinha/IMG_20221122_095438_121.jpg': 'foto/Passeio Buggy - Porto de Galinhas/image-0.jpeg',
    'foto/porto galinha/Mergulho.jpg': 'foto/Passeio Buggy - Porto de Galinhas/image-2.jpeg',
    'foto/porto galinha/porto-de-galinhas-beleza-de-praia.jpg': 'foto/Passeio Buggy - Porto de Galinhas/image-3.jpeg',
    # Mascote path fix
    'foto/mascote.png': 'foto/Mascote Uai Chatbot.png',
}

# Fix "Outros Roteiros" carousel - wrong images used for wrong destinations
outros_fixes_by_page = {
    # Santo Aleixo card in Outros Roteiros uses carneiros photo - fix to Santo Aleixo
    'passeio-carneiros.html': {
        # Carneiros card wrongly uses Cabo Buggy image - already OK
        # Santo Aleixo card uses carneiros/Carneiros 1 - fix to Santo Aleixo
    },
}

# Fix the Outros Roteiros carousel "Santo Aleixo" and "City Tour" cards across all pages
outros_card_fixes = {
    # The card for Ilha de Santo Aleixo in "Outros Roteiros" uses a carneiros img
    # but these carneiros imgs still exist so let's just keep them but fix truly broken ones
    # City Tour card uses carneiros/Carneiros Capela.jpg -> already handled by src_fixes
}

for page in pages:
    if not os.path.exists(page):
        print(f'SKIP (not found): {page}')
        continue

    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = 0

    for old, new in src_fixes.items():
        if old in content:
            content = content.replace(old, new)
            count = original.count(old)
            changes += count
            print(f'  [{page}] Fixed {count}x: {old} -> {new}')

    if content != original:
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  => Saved {page} ({changes} changes)')
    else:
        print(f'  => No changes needed: {page}')

print('\nDone!')
