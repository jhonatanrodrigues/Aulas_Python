print(' ______________________________')
print('|Cadastro de clientes          |')
print('|Desenvolvido por Jhonatan Dias|')
print('|Versao 1.0                    |')
print('|______________________________|')

def formataData(data):
    novaData = data[0] + data[1] + '/' + data[2] + data[3] + '/' + data[4] + data[5] + data[6] + data[7]
    return novaData

def formataCPf(cpf1):
    novoCpf = cpf1[0] + cpf1[1] + cpf1[2] + '.' + cpf1[3] + cpf1[4] + cpf1[5] + '.' + cpf1[6] + cpf1[7] + cpf1[8] + '-' + cpf1[9] + cpf1[10]
    return novoCpf


nome =       input('Nome do Cliente: ')
cpf =        input('CPF            : ')
cpf = formataCPf(cpf)
nascimento = input('Nascimento     : ')
nascimento = formataData(nascimento)
logradouro = input('Logradouro     : ')
numeroCasa = input('Numero         : ')
bairro =     input('Bairro         : ')
cidade =     input('Cidade         : ')
estado =     input('Estado         : ')

cliente = {
    'nome' : nome,
    'cpf' : cpf,
    'nascimento': nascimento,
    'logradouro' : logradouro,
    'numero' : numeroCasa,
    'bairro' : bairro,
    'cidade' : cidade,
    'estado' : estado
}

print(cliente.items())
print(cliente.keys())
print(cliente.values())