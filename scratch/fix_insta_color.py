import os
import re

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We find the footer-social div and replace the color of the instagram link.
        # Let's match `<div class="footer-social">...</div>`
        def fix_footer(match):
            footer_content = match.group(0)
            # Find the instagram anchor tag inside the footer
            # Replace its style to make it gold (#FFD700)
            footer_content = re.sub(r'(<a[^>]*href="https://www\.instagram\.com/uai_turismo/"[^>]*style=")([^"]*)(")', 
                                    r'\1display:inline-flex;align-items:center;gap:8px;margin-top:10px;color:var(--amber);font-weight:600;\3', 
                                    footer_content)
            # if it doesn't have style="...", this won't match, so let's match the whole a tag
            def replace_a_tag(a_match):
                a_tag = a_match.group(0)
                # remove existing style
                a_tag = re.sub(r'\s*style="[^"]*"', '', a_tag)
                # add new style
                return a_tag.replace('>', ' style="display:inline-flex;align-items:center;gap:8px;margin-top:10px;color:var(--amber);font-weight:600;">', 1)
                
            footer_content = re.sub(r'<a[^>]*href="https://www\.instagram\.com/uai_turismo/"[^>]*>', replace_a_tag, footer_content)
            return footer_content

        content = re.sub(r'<div class="footer-social">.*?</div>', fix_footer, content, flags=re.DOTALL)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print('Done fixing instagram colors in footers.')
