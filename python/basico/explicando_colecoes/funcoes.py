#O Python conta com funções úteis quando se trabalha com coleções.

# min() e max()

numeros = [15, 5, 0, 20, 10]
nomes = ['Caio', 'Alex', 'Renata', 'Patrícia', 'Bruno']

print(min(numeros)) # 0
print(max(numeros)) # 20
print(min(nomes)) # Alex
print(max(nomes)) # Renata

# A primeira lista trabalha com números, então a função min() retorna o menor valor dela, enquanto que a função max() retorna o maior valor. Já a segunda lista contém strings, o que faz com que as funções trabalhem com comparações alfabéticas. Portanto, nesse exemplo o menor valor é Alexe o maior Renata.



# A função sum(), é usada para retornar a soma de todos os elementos da coleção.

numeros = [1, 3, 6]

print(sum(numeros)) # 10



#A função len() é usada para retornar o tamanho de um objeto. Quando usada com coleções, retorna o total de itens que a coleção possui. 
paises = ['Argentina', 'Brasil', 'Colômbia', 'Uruguai']

print(len(paises)) # 4