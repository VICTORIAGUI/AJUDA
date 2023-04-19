#Operador                      	Conceito	                                          Exemplo
#   is	       Retorna True se as variáveis comparadas forem o mesmo objeto	nome     is ‘Marcos’
# is not	   Retorna True se as variáveis comparadas não forem o mesmo objeto	x   is not ‘Python’

time_carlos = 'Botafogo'
time_luciano = 'Flamengo'
time_fabricia = 'Botafogo'

if time_carlos is time_luciano:
    print("time_carlos - time_luciano = mesmo objeto")
else:
    print("time_carlos - time_luciano = objetos diferentes")

if time_carlos is time_fabricia:
    print("time_carlos - time_fabricia = mesmo objeto")
else:
    print("time_carlos - time_fabricia = objetos diferentes")