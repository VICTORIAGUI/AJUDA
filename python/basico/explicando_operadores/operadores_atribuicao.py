#Operador	   Exemplo	      Equivalente a
#   =	        x = 1             x = 1
#  +=           x += 1	        x = x + 1
#  -=	        x -= 1	        x = x - 1
#  *=	        x *= 1	        x = x * 1
#  /=           x /= 1	        x = x / 1
#  %=	        x %= 1	        x = x % 1


# Atribuindo valor 
numero_1 = 5

numero_1 += 5

print(numero_1) # O resultado será 10


# Atrubindo diminuição
numero_1 -= 5

print(numero_1) # O resultado será 5


# Atribuindo multiplicação
numero_1 *= 5

print(numero_1) # O resultado será 25


# Atribuindo divisão
numero_1 /= 5 # O resultado será 5.0

print(numero_1)


# Atribuindo modulo
numero_1 %= 5 

print(numero_1) # O resultado será 0.0



# Declarando as variaveis
saldo1 = 5000
saldo2 = 8000

# Imprimindo as variaveis
print(saldo1)
print(saldo2)

# Usando a operador aritmetico de adição (+=)
saldo2 += saldo1
print(saldo2)

# Usando as operações de adição (+=) e subtração (-=)
saldo3 = 2000
saldo4 = 5000 

saldo4 += saldo3
print(saldo3)

saldo3 -= saldo4
print(saldo4)

# Usando a multiplicação (*=) 
saldo5 = 30
saldo6 = 5

saldo5 *= saldo6
print(saldo5)

# Usando a divisão (/=)
saldo7 = 40
saldo8 = 3

saldo7 /= saldo8
print(saldo7)

# Usando a divisão inteira (//=) Ela sempre trunca o MENOR valor mais proximo.
saldo7 //= saldo8
print (saldo7)