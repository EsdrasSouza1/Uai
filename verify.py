with open('passeio-city-tour.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<div class=\"ptips\">.*?</div>', text, re.DOTALL)
if m:
    print("MATCH 1:", m.group(0)[:100])
else:
    print("NO MATCH FOR div ptips...</div>")

m2 = re.search(r'<div class=\"ptips\".*?(<div class=\"psidebar\"|</div>\s*</div>\s*<div class=\"psidebar\")', text, re.DOTALL)
if m2:
    print("MATCH 2:", m2.group(0)[:100])
