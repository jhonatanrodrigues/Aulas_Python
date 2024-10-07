print(" ___________________________________")
print("|Calc - Sistema de operações simples|")
print("|Desenvolvido por: Jhonatan Dias    |")
print("|Criado em 24/08/2024               |")
print("|Versão 1.0                         |")
print("|___________________________________|")
print("")

while True:
   
    try:
        realizar = int(input("\nDigite (1 - CONTINUAR) ou (2 - SAIR): "))
        if realizar not in [1, 2]:
            print("\nNúmero digitado inválido, por favor digite 1 ou 2.")
            continue
        if realizar == 2:
            print("Saindo do programa...")
            break

        print(" _________________________")
        print("|Escolha a operação:      |")
        print("|1 - Converter para Dolar |")
        print("|2 - Converter para Euro  |")
        print("|_________________________|")
        
        op = int(input("\nDigite o numero ref da operação: "))
        

        if 1 <= op <= 2:
            
            
            if op == 1:
                pdolar = float(input("Digite o valor do produto em dolar: "))
                dolar = float(input("Digite o valor do dolar: "))
                cal = pdolar * dolar
                print("\nO valor do produto em reais é = ",cal)
            elif op == 2:
                peuro = float(input("Digite o valor do produto em Euro: "))
                euro = float(input("Digite o valor do euro: "))
                cal = peuro * euro
                print("\nO valor do produto em reais é = ",cal)
            
            
            

            


    except ValueError:
       print("")
   