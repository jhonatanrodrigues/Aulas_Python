while True:
    nome = input("Digite um nome ('Sair' para sair): ")
    #if nome.lower() == "sair":
    if nome.upper() == "SAIR":
        break
    for letra in nome:
        print(letra)
print("Bye")