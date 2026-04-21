import re
import glob

def get_footer(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'<div class=\"footer-links\">(.*?)</div>', content, re.DOTALL)
    return m.group(1).strip() if m else None

def get_nav(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'<ul id=\"navMenu\">(.*?)</ul>', content, re.DOTALL)
    return m.group(1).strip() if m else None

print("Index Footer:")
print(get_footer("index.html"))
print("\nIndex Nav:")
print(get_nav("index.html"))
