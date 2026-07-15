with open("informacoes.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome: Nathan\n")
    arquivo.write("Idade: 18\n")
    arquivo.write("Curso: Programação em Python\n")
with open("informacoes.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
print("Conteúdo do arquivo:")
print(conteudo)