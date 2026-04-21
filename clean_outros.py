import glob

files = glob.glob('passeio-*.html')
for fn in files:
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # We need to find the lines for the HTML div <div class="outros-sec">
        # inside the body of the html (after <body> tag or just not in <style>)
        start_line = -1
        end_line = -1
        
        for i, line in enumerate(lines):
            if '<div class="outros-sec">' in line:
                start_line = i
                break
                
        if start_line != -1:
            for i in range(start_line, len(lines)):
                if '<!-- OUTROS ROTEIROS - Carrossel -->' in lines[i]:
                    end_line = i
                    break
                    
        if start_line != -1 and end_line != -1:
            # We found the block! Delete it.
            new_lines = lines[:start_line] + lines[end_line:]
            with open(fn, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f'Fixed duplicates in {fn}')
    except Exception as e:
        print(f"Failed on {fn}: {e}")
