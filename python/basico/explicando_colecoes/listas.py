# Lista é uma coleção de valores indexada, em que cada valor é identificado por um índice. O primeiro item na lista está no índice 0, o segundo no índice 1 e assim por diante.

#Para criar uma lista com elementos deve-se usar colchetes e adicionar os itens entre eles separados por vírgula..

programadores = ['Victoria', 'Juliana', 'Samuel', 'Caio', 'Luana'] 

print(programadores) # Exibindo os valores da lista
print(type(programadores)) # type ‘list’
print(len(programadores)) # Descobrindo o tamanho da lista, o resultado é 5
print(programadores[4]) # Retornando o valor do index 4 que é Luana


# Subistituindo um valor na lista 

programadores[1] = 'Carolina'
print(programadores) # ['Victoria', 'Carolina', 'Samuel', 'Caio', 'Luana']


# Adicionando um item a lista

programadores.append('Renato')
print(programadores) # ['Victoria', 'Carolina', 'Samuel', 'Caio', 'Luana', 'Renato']


# Removendo um item da lista

programadores.remove('Victoria')
print(programadores) # ['Carolina', 'Samuel', 'Caio', 'Luana', 'Renato']


# Removendo pelo index 

programadores.pop(0)
print(programadores) # ['Samuel', 'Caio', 'Luana', 'Renato']



#Outra característica das listas é que elas podem possuir diferentes tipos de elementos na sua composição. Isso quer dizer que podemos ter strings, booleanos, inteiros e outros tipos diferentes de objetos na mesma lista.

aluno = ['Murilo', 19, 1.79] # Nome, idade e altura

print(type(aluno)) # type 'list'
print(aluno) # ['Murilo', 19, 1.79]