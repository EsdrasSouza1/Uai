import os
import re
import glob

files = glob.glob("passeio-*.html")
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    print(f"{f}: has_pinc={'class=\"pinc\"' in content}")
