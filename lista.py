listaCompras = ['nescau', 'carne', 'batata', 'sorvete']
print(listaCompras)
listaCompras[1] = 'toddy'
print(listaCompras)
listaCompras.append('bolacha') #adiciona item no final
print(listaCompras)
listaCompras.insert(1, 'bolo') #Adiciona item em uma posição
print(listaCompras)
listaCompras.sort() #ordena a lista
print(listaCompras) 
listaCompras.reverse() #Inverte a lista
print(listaCompras)
listaCompras.remove('toddy') #Remove o item da lista pelo nome
print(listaCompras)
listaCompras.pop(3) #Remove o item da lista pela posição 
print(listaCompras)