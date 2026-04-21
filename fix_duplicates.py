import glob

files = glob.glob('passeio-*.html')
for fn in files:
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            html = f.read()

        start_marker = '<div class="outros-sec">'
        end_marker = '<!-- OUTROS ROTEIROS - Carrossel -->'
        
        if start_marker in html and end_marker in html:
            start_idx = html.find(start_marker)
            end_idx = html.find(end_marker, start_idx)
            if end_idx != -1:
                # Remove everything between start_idx and end_idx
                new_html = html[:start_idx] + html[end_idx:]
                with open(fn, 'w', encoding='utf-8') as f:
                    f.write(new_html)
                print('Fixed duplicates in', fn)
    except Exception as e:
        print(e)
