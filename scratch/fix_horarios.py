import glob

files = ['passeio-milagres.html', 'passeio-maragogi.html', 'passeio-maragogi-ponta-de-mangue.html']

old_str = "Passeio das 07:30 às 17:30"
new_str = "05:00/07:30 (depende da maré) às 17:30"

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        text = file.read()
    
    if old_str in text:
        text = text.replace(old_str, new_str)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(text)
        count += 1

print("Replaced in", count, "files.")
