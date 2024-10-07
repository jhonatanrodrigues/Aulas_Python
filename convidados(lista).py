listaConvidados = []

while True:

    nome = input('Digite o nome do convidado: ')
    if nome == '':
        break
    listaConvidados.append(nome)
    
for convidado in listaConvidados:
    print(convidado)





