import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I want to remove the badge division and the 8 destinos badge.
# It looks like:
# <div class="badge-divider"></div>
# <div class="badge"><strong>8</strong><span>Destinos exclusivos</span></div>

import sys
new_content, count = re.subn(r'\s*<div class=\"badge-divider\"></div>\s*<div class=\"badge\"><strong>8.*?Destinos exclusivos.*?</div>', '', content, flags=re.DOTALL|re.IGNORECASE)

if count > 0:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("REMOVED", count)
else:
    # Maybe it's without divider? Or order is different?
    print("NO MATCH. Let's find what is around 8")
    m = re.search(r'(?i).{0,50}<strong>8.{0,50}', content)
    if m:
        print(m.group(0).encode('ascii', 'ignore').decode('ascii'))
    else:
        print("Still nothing. Let me look at heroBadges")
        m2 = re.search(r'id=\"heroBadges\".*?</div>\s*</div>', content, flags=re.DOTALL)
        if m2:
            print(m2.group(0).encode('ascii', 'ignore').decode('ascii'))
