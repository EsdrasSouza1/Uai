import glob

files=['passeio-carneiros.html', 'passeio-maragogi.html', 'passeio-maragogi-ponta-de-mangue.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        text = file.read()
    new_text = text.replace('Passeio de lancha exclusivo.', 'Passeio de lancha.')
    new_text = new_text.replace('Passeio de lancha exclusivo para as', 'Passeio de lancha para as')
    if new_text != text:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_text)

with open('index.html', 'r', encoding='utf-8') as file: text = file.read()
text = text.replace('<h2>Destinos <span>Exclusivos</span></h2>', '<h2>Nossos <span>Destinos</span></h2>')
text = text.replace('Siga-nos no Instagram para acompanhar nossos roteiros exclusivos', 'Siga-nos no Instagram para acompanhar nossos roteiros')
text = text.replace("'exclusivo', ", "")
text = text.replace('o carro é exclusivo para o seu grupo', 'o carro é somente para o seu grupo')
with open('index.html', 'w', encoding='utf-8') as file: file.write(text)

with open('quem-somos.html', 'r', encoding='utf-8') as file: text = file.read()
text = text.replace("'exclusivo', ", "")
text = text.replace('o carro é exclusivo para o seu grupo', 'o carro é somente para o seu grupo')
with open('quem-somos.html', 'w', encoding='utf-8') as file: file.write(text)

print("Done")
