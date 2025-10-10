import csv
import os

entrada = "commits_por_usuario.csv"
saida = "pastas_por_usuario.csv"

linhas_unicas = set()

with open(entrada, "r", encoding="utf-8") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        if not linha:
            continue
        # Junta caso a linha tenha mais de 2 campos
        usuario = linha[0].strip()
        caminho = ",".join(linha[1:]).strip().strip('"').strip("'")
        pasta = os.path.dirname(caminho).replace("\\", "/") + "/"
        linhas_unicas.add((usuario, pasta))

with open(saida, "w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    for usuario, pasta in sorted(linhas_unicas):
        escritor.writerow([usuario, pasta])

print(f"✅ Arquivo '{saida}' gerado com sucesso com {len(linhas_unicas)} linhas únicas.")
