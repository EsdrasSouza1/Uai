import os
import re

data = {
    "passeio-maragogi-ponta-de-mangue.html": {
        "duracao": "Passeio das 07:30 às 17:30",
        "roteiro_title": "Roteiro Lancha - 2 Horas",
        "roteiro_items": [
            "<strong>Crôa da Bruna:</strong> Banco de areia com águas cristalinas.",
            "<strong>Piscinas Naturais:</strong> Perfeitas para snorkel e mergulho.",
            "<strong>Praia do Xaréu:</strong> Praia paradisíaca com infraestrutura completa."
        ],
        "incluso_items": [
            "Buscamos e deixamos no local de hospedagem. 🚐🏖️",
            "Serviço de guia especializado. 🎭",
            "Fotos cortesia durante o passeio. 📸",
            "Passeio de lancha exclusivo. 🚤",
            "*Day use em restaurante à beira-mar não incluso."
        ]
    },
    "passeio-maragogi.html": {
        "duracao": "Passeio das 07:30 às 17:30",
        "roteiro_title": "Roteiro Lancha - 2 Horas",
        "roteiro_items": [
            "<strong>Caminho de Moisés:</strong> Bancos de areia que aparecem na maré baixa.",
            "<strong>Piscinas Naturais:</strong> Águas cristalinas.",
            "<strong>Praia de Antunes:</strong> Uma das praias mais bonitas da região."
        ],
        "incluso_items": [
            "Buscamos e deixamos no local de hospedagem. 🚐🏖️",
            "Serviço de guia especializado. 🎭",
            "Fotos cortesia durante o passeio. 📸",
            "Passeio de lancha exclusivo. 🚤",
            "*Day use em restaurante à beira-mar não incluso."
        ]
    },
    "passeio-carneiros.html": {
        "duracao": "Passeio das 07:30 às 17:30",
        "roteiro_title": "Roteiro Lancha - 2 Horas",
        "roteiro_items": [
            "<strong>Capela de São Benedito:</strong> A famosa igrejinha à beira-mar.",
            "<strong>Banho de Argila:</strong> Experiência relaxante e renovadora.",
            "<strong>Banco de Areia:</strong> Piscinas naturais de águas cristalinas.",
            "<strong>Encontro dos Rios/Manguezal:</strong> Beleza natural única."
        ],
        "incluso_items": [
            "Buscamos e deixamos no local de hospedagem. 🚐🏖️",
            "Serviço de guia especializado. 🎭",
            "Fotos cortesia durante o passeio. 📸",
            "Passeio de lancha exclusivo. 🚤",
            "*Day use em restaurante à beira-mar não incluso."
        ]
    },
    "passeio-milagres.html": {
        "duracao": "Passeio das 07:30 às 17:30",
        "roteiro_title": "Roteiro Jangada - 2 Horas",
        "roteiro_items": [
            "<strong>Piscinas Naturais:</strong> Águas cristalinas repletas de vida marinha.",
            "<strong>Fotos boia de melancia e rede:</strong> Registros incríveis para suas redes sociais.",
            "<strong>Parada do pulo:</strong> Diversão garantida para toda a família."
        ],
        "incluso_items": [
            "Buscamos e deixamos no local de hospedagem. 🚐🏖️",
            "Serviço de guia especializado. 🎭",
            "Fotos cortesia durante o passeio. 📸",
            "Passeio de jangada tradicional. 🚤",
            "*Day use em restaurante à beira-mar não incluso."
        ]
    },
    "passeio-porto-de-galinhas.html": {
        "duracao": "Passeio privativo (manhã ou tarde)",
        "roteiro_title": "Roteiro de Buggy - 4 Horas",
        "roteiro_items": [
            "<strong>Praia de Muro Alto:</strong> Piscina natural gigante formada por recifes.",
            "<strong>Pontal do Cupê:</strong> Piscinas naturais de águas cristalinas.",
            "<strong>Coqueiral de Maracaípe:</strong> Cenário paradisíaco com coqueiros.",
            "<strong>Pontal de Maracaípe:</strong> Encontro do rio com o mar e santuário dos cavalos-marinhos."
        ],
        "incluso_items": [
            "Buscamos e deixamos no local de hospedagem. 🚐🏖️",
            "Fotos cortesia durante o passeio. 📸",
            "*Obs: Todos os passeios de buggy são privativos."
        ]
    },
    "passeio-city-tour.html": {
        "duracao": "Passeio das 07:30 às 17:30",
        "roteiro_title": "Roteiro",
        "roteiro_items": [
            "<strong>Orla da Praia de Boa Viagem:</strong> Uma das praias urbanas mais famosas do Brasil.",
            "<strong>Marco Zero e Rua do Bom Jesus:</strong> Coração do Recife Antigo.",
            "<strong>Embaixada dos Bonecos Gigantes:</strong> Tradição do carnaval pernambucano.",
            "<strong>Alto da Sé:</strong> Vista panorâmica de Olinda e Recife.",
            "<strong>Igreja de São Salvador do Mundo:</strong> Patrimônio histórico.",
            "<strong>Feira de Artesanato:</strong> Arte e cultura local.",
            "<strong>Mosteiro de São Bento:</strong> Arquitetura barroca impressionante."
        ],
        "incluso_items": [
            "Buscamos e deixamos no local de hospedagem. 🚐🏖️",
            "Serviço de guia especializado em história local. 🎭",
            "Fotos cortesia durante o passeio. 📸",
            "*Valores de entrada em museus, feiras e igrejas não inclusos."
        ]
    },
    "passeio-ilha-santo-aleixo.html": {
        "duracao": "Passeio das 07:30 às 17:30",
        "roteiro_title": "Roteiro",
        "roteiro_items": [
            "<strong>Trilha Ecológica:</strong> Caminhada pela natureza preservada da ilha.",
            "<strong>Praia da Ferradura:</strong> Uma das praias mais bonitas da região.",
            "<strong>Piscinas Naturais:</strong> Águas cristalinas perfeitas para mergulho.",
            "<strong>Fotos com esquilos:</strong> Interação com os famosos esquilos da ilha."
        ],
        "incluso_items": [
            "Buscamos e deixamos no local de hospedagem. 🚐🏖️",
            "Serviço de guia especializado. 🎭",
            "Fotos cortesia durante o passeio. 📸",
            "Travessia em lancha compartilhada. 🚤"
        ]
    },
    "passeio-cabo-santo-agostinho.html": {
        "duracao": "Passeio das 07:30 às 17:30",
        "roteiro_title": "Roteiro de Buggy - 3 Horas",
        "roteiro_items": [
            "<strong>Praias de Calhetas, Enseada dos Corais e Gaibu:</strong> Belezas naturais imperdíveis.",
            "<strong>Mirantes do Faroleiro e do Paraíso:</strong> Vistas panorâmicas espetaculares.",
            "<strong>Degustação de doces e licores:</strong> Sabores típicos da região."
        ],
        "incluso_items": [
            "Buscamos e deixamos no local de hospedagem. 🚐🏖️",
            "Serviço de guia especializado. 🎭",
            "Fotos cortesia durante o passeio. 📸",
            "*Day use em restaurante à beira-mar não incluso.",
            "*Obs: Todos os passeios de buggy são privativos."
        ]
    }
}

for filename, info in data.items():
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # HTML template to generate
    html_out = []
    
    # Duracao
    html_out.append('        <!-- DURACAO -->\n        <div class="pinc" style="margin-bottom:24px;">\n          <h3>⏳ Duração</h3>\n          <ul>\n            <li><span class="ii">⏱</span>' + info['duracao'] + '</li>\n          </ul>\n        </div>')
    
    # Roteiro
    html_out.append('        <!-- ROTEIRO -->\n        <div class="pinc" style="margin-bottom:24px;">\n          <h3>🗺️ ' + info['roteiro_title'] + '</h3>\n          <ul>')
    for item in info['roteiro_items']:
        html_out.append('            <li><span class="ii">📍</span>' + item + '</li>')
    html_out.append('          </ul>\n        </div>')

    # Incluso
    html_out.append('        <!-- INCLUSO -->\n        <div class="pinc">\n          <h3>✅ O que está incluído</h3>\n          <ul>')
    for item in info['incluso_items']:
        if item.startswith('*'):
            html_out.append(f'            <li style="margin-top:10px;"><small style="color:var(--text-muted);font-weight:600;">{item}</small></li>')
        else:
            html_out.append(f'            <li><span class="ii">✓</span>{item}</li>')
    html_out.append('          </ul>\n        </div>')
    
    new_block = "\n".join(html_out)

    # find the existing INCLUSO block to replace
    # We will match from <!-- INCLUSO --> to the next <!-- DICAS --> or <!-- SIDEBAR -->
    pattern = re.compile(r'<!-- INCLUSO -->.*?</div>\s+(<!-- DICAS -->|<!-- SIDEBAR -->)', re.DOTALL)
    
    if pattern.search(content):
        # We append the matched footer (either DICAS or SIDEBAR) back
        def repl(m):
            return new_block + "\n\n        " + m.group(1)
        new_content = pattern.sub(repl, content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
        
    else:
        print(f"Could not find INCLUSO block in {filename}")

