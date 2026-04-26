import os
import glob

# Files to update golden numbers
privacidade = "politica-de-privacidade.html"
bio = "bio/bio.html"

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Update politica-de-privacidade.html
if os.path.exists(privacidade):
    content = read_file(privacidade)
    content = content.replace(
        'WhatsApp <strong>(81) 99748-4915</strong>.</p>',
        'WhatsApp <strong style="color: var(--amber);">(81) 99748-4915</strong>.</p>'
    )
    content = content.replace(
        'WhatsApp\n                <strong>(81) 99748-4915</strong>. Responderemos em até 15 dias úteis.</p>',
        'WhatsApp\n                <strong style="color: var(--amber);">(81) 99748-4915</strong>. Responderemos em até 15 dias úteis.</p>'
    )
    write_file(privacidade, content)

# Update bio/bio.html
if os.path.exists(bio):
    content = read_file(bio)
    # Golden number
    content = content.replace(
        'WhatsApp <strong style="color:white">(81) 99748-4915</strong>.</p>',
        'WhatsApp <strong style="color:var(--amber-light)">(81) 99748-4915</strong>.</p>'
    )
    # Favicon
    content = content.replace(
        '<link rel="icon" type="image/png" href="foto/logoo.png">',
        '<link rel="icon" type="image/png" href="../foto/logoo.png">'
    )
    content = content.replace(
        '<link rel="apple-touch-icon" href="foto/logoo.png">',
        '<link rel="apple-touch-icon" href="../foto/logoo.png">'
    )
    write_file(bio, content)

# Update og:image and twitter:image across all html files
html_files = glob.glob("**/*.html", recursive=True)
new_img = "https://www.uaitur.com/bio/fotos/Logo%20_uai%20TURISMO_%20na%20Praia%20Tropical%20(1).png"
old_img = "https://www.uaitur.com/foto/logoo.png"

for file in html_files:
    content = read_file(file)
    original_content = content
    
    # If the file already has old_img, just replace it
    if old_img in content:
        content = content.replace(old_img, new_img)
    else:
        # Check if it has an og:image already. If not, add one before </head>
        if "og:image" not in content and "</head>" in content:
            meta_tags = f'\n    <meta property="og:image" content="{new_img}">\n    <meta property="og:image:width" content="400">\n    <meta property="og:image:height" content="400">\n    <meta name="twitter:card" content="summary">\n    <meta name="twitter:image" content="{new_img}">\n'
            content = content.replace("</head>", meta_tags + "</head>")
            
    if content != original_content:
        write_file(file, content)
        print(f"Updated {file}")
