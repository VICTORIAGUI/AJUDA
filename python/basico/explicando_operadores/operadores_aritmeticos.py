numero_1 = 5 # Váriavel 1
numero_2 = 2 # Váriavel 2

soma = numero_1 + numero_2 # Somando as variaveis 

subtracao = numero_1 - numero_2 # Subtraindo  as variaveias

multiplicacao = numero_1 * numero_2 # Multiplicando as variaveis 

divisao = numero_1 / numero_2 # Dividindo as variaveis com resto 

divisao_inteira = numero_1 // numero_2 # Dividindo as varias sem resto = inteira.

modulo = numero_1 % numero_2 # Retorna o resto da divisão

exponenciacao = numero_1 ** numero_2 #	Retorna um número elevado a potência de outro

print(soma) # 7
print(subtracao) # 3
print(multiplicacao)  # 10
print(divisao) # 2.5
print(divisao_inteira) # 2
print(modulo)  # 1
print(exponenciacao) # 25


# As expressões contidas em parênteses têm a precedência maior na linguagem Python. Isso permite que uma expressão execute antes de outra. Ex.:
print((2 + 5) * 3) # O resultado será 21


# Após os parênteses, o próximo operador com maior precedência é o de exponenciação. Ex.:
print( 1 + 5**2 ) # O resultado será 26


# Multiplicação e divisão têm precedência sobre a adição e subtração: como já é conhecido na matemática, divisão e multiplicação são executadas antes das operações de adição e subtração. Ex.:
print(5 * 3 + 8) # O resultado será 23


# Ordem de precedência é avaliada da esquerda para a direita. Portanto, após os operadores anteriores, a sequência da execução será da esquerda para a direita. Ex.:
print(8 + 5 - 10) # O resultado será 3