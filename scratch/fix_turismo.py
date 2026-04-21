import glob

old_str = '<span style="color:rgba(255,255,255,.85);font-weight:700;font-size:1rem;">Turismo</span>'
new_str = '<span style="color:rgba(255,255,255,.85);font-weight:900;font-style:italic;">Turismo</span>'

count = 0
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        text = file.read()
    
    if old_str in text:
        text = text.replace(old_str, new_str)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(text)
        count += 1

print('Replaced in', count, 'files')
