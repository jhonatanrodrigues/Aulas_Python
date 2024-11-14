while True:
    peso = float(input("Digite seu peso: (0 para sair): "))
    if peso == 0:
        break
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura*altura)
    print("Seu imc é :", imc)
    if imc > 40:
        print("Obesidade grau 3")
    elif imc > 35:
        print("Obesidade grau 2")
    elif imc > 30:
        print("Obesidade grau 1")
    elif imc > 25:
        print("Sobrepeso")
    elif imc > 18.5:
        print("Peso normal")
    else:
        print("Baixo Peso")
