import glob

files = glob.glob('*.html')
count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        text = file.read()
    
    new_text = text.replace('Serviço de guia especializado em história local.', 'Serviço de guia em história local.')
    new_text = new_text.replace('Serviço de guia especializado.', 'Serviço de guia.')
    
    if new_text != text:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_text)
        count += 1

print('Replaced in', count, 'files')
