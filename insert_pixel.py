import os
import glob

# The Meta Pixel Code to insert
pixel_code = """
    <!-- Meta Pixel Code -->
    <script>
    !function(f,b,e,v,n,t,s)
    {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', '1936582633666731');
    fbq('track', 'PageView');
    </script>
    <noscript><img height="1" width="1" style="display:none"
    src="https://www.facebook.com/tr?id=1936582633666731&ev=PageView&noscript=1"
    /></noscript>
    <!-- End Meta Pixel Code -->
"""

# Directory to search
base_dir = r"c:\Users\nerds\OneDrive\Área de Trabalho\Uai"

# Find all HTML files
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid injecting multiple times
    if "1936582633666731" in content:
        print(f"Skipping {filepath}, already contains pixel.")
        continue

    # Insert just before </head>
    if "</head>" in content:
        new_content = content.replace("</head>", pixel_code + "\n</head>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected into {filepath}")
    else:
        print(f"Could not find </head> in {filepath}")

print("Done.")
