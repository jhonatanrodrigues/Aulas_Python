
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

        print(" ____________________")
        print("|Escolha a operação: |")
        print("|1 - Adição          |")
        print("|2 - Subtração       |")
        print("|3 - Multiplicação   |")
        print("|4 - Divisão         |")
        print("|___________________ |")

        op = int(input("\nDigite o numero ref da operação: "))
        
        if 1 <= op <= 4:
            num1 = float(input("\nDigite o primeiro numero da operação: "))
            num2 = float(input("\nDigite o segundo numero da operação : "))

            if op == 1:
                resultado = num1 + num2
                print("\nA soma dos numeros é = ",resultado)
            elif op == 2:
                resultado = num1 - num2
                print("\nA subtração dos numeros é = ",resultado)
            elif op == 3:
                resultado = num1 * num2
                print("\nA multiplicação dos numeros é = ",resultado)
            elif op == 4:
                
                if num2 != 0:
                    resultado = num1 / num2
                    print("\nA divisão dos numeros é = ",resultado)
                else:
                    print("\nERRO!! Divisão por 0 não é permitido.")
                    continue      
        else:
            print("\nNumero digitado invalido, digite entre 1 e 4.")
            continue
            
    except ValueError:
        print("\nNumero digitado invalido, digite um numero valido.")
   