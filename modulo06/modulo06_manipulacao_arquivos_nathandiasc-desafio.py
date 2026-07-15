import shutil
import os
origem = "documento.txt"
destino = "backup"
os.makedirs(destino, exist_ok=True)
shutil.copy(origem, destino)
print("Backup realizado com sucesso!")

# Se quiser copiar todos os arquivos de uma pasta:

import shutil
import os
origem = "arquivos"
destino = "backup"
os.makedirs(destino, exist_ok=True)
for arquivo in os.listdir(origem):
    caminho_origem = os.path.join(origem, arquivo)
    if os.path.isfile(caminho_origem):
        shutil.copy(caminho_origem, destino)
print("Todos os arquivos foram copiados para a pasta backup.")