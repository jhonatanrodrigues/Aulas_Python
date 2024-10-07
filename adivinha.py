import random
numero = random.randint(1, 100)
tentativas = 0
while True:   
    chute = int(input("Chute um numero entre 1 e 100: "))       
    if chute < numero:
        tentativas += 1
        print("Você chutou baixo")
    elif chute > numero:
        tentativas += 1
        print("Você chutou alto")
    elif chute == numero:
        tentativas += 1
        print("Você Acertou, em",tentativas, "tentativas!!!")
        break