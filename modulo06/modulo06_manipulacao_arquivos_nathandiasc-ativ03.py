import csv
notas = [
    ["Nome", "Nota"],
    ["Ana", 8.5],
    ["Carlos", 7.0],
    ["Beatriz", 9.3]
]
with open("notas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(notas)
print("Notas dos alunos:")
with open("notas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)