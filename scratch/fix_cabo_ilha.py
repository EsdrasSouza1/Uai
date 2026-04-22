
import os
os.chdir(r'c:\Users\nerds\OneDrive\Área de Trabalho\Uai')

DICAS_PRAIA = '''
        <!-- DICAS PARA O PASSEIO -->
        <div class="pinc" style="background: linear-gradient(135deg, #e8f6f9 0%, #d0eef5 100%); border: 1px solid #a0d9e8; border-radius: 20px; padding: 32px 28px; margin-bottom: 24px;">
          <h3 style="font-family: 'Playfair Display', serif; font-size: 1.15rem; color: #004D5C; margin-bottom: 18px;">&#x1F4A1; Dicas para o Passeio</h3>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 10px;">
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span>&#x2600;&#xFE0F;</span> Use protetor solar e reaplique ao longo do dia (mesmo nublado, o sol queima forte)</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span>&#x1F4A7;</span> Leve agua - o calor e intenso</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span>&#x1F455;</span> Va com roupa leve, ja com roupa de banho por baixo e leve roupa seca para a volta</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span>&#x1F3D6;&#xFE0F;</span> Leve toalha ou canga</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span>&#x1F45F;</span> Use chinelo ou sandalia confortavel</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span>&#x1F576;&#xFE0F;</span> Leve oculos de sol e bone/chapeu</li>
            <li style="display: flex; align-items: flex-start; gap: 10px; font-size: .91rem; color: #2a5a66;"><span>&#x1F4F1;</span> Proteja o celular com capa a prova d'agua</li>
          </ul>
        </div>
'''

# marker: the empty line + closing div before psidebar
MARKER = '        \n      </div>\n\n      <div class="psidebar">'

for fname in ['passeio-cabo-santo-agostinho.html', 'passeio-ilha-santo-aleixo.html']:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        if MARKER in content:
            content = content.replace(MARKER, DICAS_PRAIA + MARKER, 1)
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'[OK] Dicas adicionadas: {fname}')
        else:
            # Try alternative marker
            alt = '      </div>\n\n      <div class="psidebar">'
            if alt in content:
                content = content.replace(alt, DICAS_PRAIA + alt, 1)
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'[OK-alt] Dicas adicionadas: {fname}')
            else:
                print(f'[SKIP] nenhum marker encontrado: {fname}')
    except Exception as e:
        print(f'[ERR] {fname}: {e}')

print('DONE')
