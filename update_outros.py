import glob

files = glob.glob('*.html')
for fn in files:
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Replace the 3 static grid images across all files (including index.html if present)
        # However, they might have literal strings as shown below:
        html = html.replace('src="foto/buggy.JPEG" alt="Porto de Galinhas – PE"', 'src="foto/Passeio Buggy - Porto de Galinhas/image-8.jpeg" alt="Porto de Galinhas – PE"')
        html = html.replace('src="foto/carneiro2.JPEG" alt="Praia dos Carneiros – PE"', 'src="foto/carneiros/Carneiros Capela.jpg" alt="Praia dos Carneiros – PE"')
        html = html.replace('src="foto/2.2.jpeg" alt="Maragogi – AL"', 'src="foto/Maragogi - Barra Grande/image-7.jpeg" alt="Maragogi – AL"')
        
        # Also clean up the double-spaces or specific src replacement just in case:
        html = html.replace('foto/buggy.JPEG', 'foto/Passeio Buggy - Porto de Galinhas/image-8.jpeg')
        html = html.replace('foto/carneiro2.JPEG', 'foto/carneiros/Carneiros Capela.jpg')
        html = html.replace('foto/2.2.jpeg', 'foto/Maragogi - Barra Grande/image-7.jpeg')

        with open(fn, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Cleaned up images in {fn}")
    except Exception as e:
        print(e)
