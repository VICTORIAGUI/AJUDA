#Tupla é uma estrutura de dados semelhante a lista. Porém, ela tem a característica de ser imutável, ou seja, após uma tupla ser criada, ela não pode ser alterada.

times_rj = ( 'Vasco', 'Botafogo', 'Flamengo', 'Fluminense')

print(type(times_rj)) # class= ’tuple’
print(times_rj) # ('Vasco', 'Botafogo', 'Flamengo', 'Fluminense')

# Acessando item pelo index

print(times_rj[3]) # Fluminense


# Na tupla é necessario por uma virgula entre os intens para que não seja atribuido á uma string.

objeto_string = ('tesoura')
objeto_tupla = ('tesoura',)

print(type(objeto_string)) # class 'str'
print(type(objeto_tupla)) # class 'tuple'