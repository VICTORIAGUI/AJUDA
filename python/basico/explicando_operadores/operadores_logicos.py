#  Operador	                     Conceito	                                                                Exemplo
#   and	     Retorna True se todas as condições forem verdadeiras, caso contrário retorna False	       x > 1 and x < 5
#    or	     Retorna True se uma das condições for verdadeiras, caso contrário retorna False	       x > 1 or x < 5
#   not	     Inverte o resultado: se o resultado da expressão for True, o operador retorna false	not(x > 1 and x < 5)


idade_lucas = 21
idade_carolina = 19

# OPERADOR OR
if idade_lucas >= 18 or idade_carolina >= 18:
    print("Pelo menos um dos dois é maior de idade")
else:
    print("Lucas e Carolina não são maiores de idade")

# OPERADOR AND
if idade_lucas >= 18 and idade_carolina >= 18:
    print("Lucas e Carolina são maiores de idade")
else:
    print("Pelo menos um dos dois não é maior de idade")