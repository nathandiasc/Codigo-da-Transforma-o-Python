def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    print(f"Média: {media:.2f}")
    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado.")
calcular_media(8, 7, 9)