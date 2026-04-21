import re
files = ['passeio-city-tour.html', 'passeio-ilha-santo-aleixo.html', 'passeio-cabo-santo-agostinho.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's find the location of the .pdesc and .psidebar
    m = re.search(r'(<div class=\"pdesc\">.*?</div>).*?(<!-- SIDEBAR -->)', content, re.DOTALL)
    if m:
        print(f"Found block in {f}")
    else:
        print(f"Not matched in {f}")
