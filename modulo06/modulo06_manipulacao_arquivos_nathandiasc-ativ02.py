import json
clientes = {
    "João": {
        "idade": 25,
        "cidade": "São Paulo"
    },
    "Maria": {
        "idade": 30,
        "cidade": "Rio de Janeiro"
    }
}
with open("clientes.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)
with open("clientes.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
print("Clientes cadastrados:")
for nome, info in dados.items():
    print(f"{nome} - Idade: {info['idade']} - Cidade: {info['cidade']}")