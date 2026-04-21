import glob
import os

folders = [
    "Cabo de Santo Agostinho Passeios de Buggy",
    "carneiros",
    "Citytour Recife e Olinda",
    "Santo Aleixo",
    "Maragogi - Barra Grande",
    "Maragogi - Ponta de Mangue",
    "milagres",
    "Passeio Buggy - Porto de Galinhas"
]

for folder in folders:
    path = f"foto/{folder}"
    print(f"\n[{folder}]:")
    try:
        files = [f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        for f in files[:5]: # just print first 5
            print(f"  {f}")
    except Exception as e:
        print(f"  Error: {e}")
