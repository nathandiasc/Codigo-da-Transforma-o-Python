def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor
numeros = [10, 5, 8, 20, 3]
maior, menor = maior_menor(numeros)
print("Maior número:", maior)
print("Menor número:", menor)