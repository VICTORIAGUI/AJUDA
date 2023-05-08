# A extrutura de repetição serve para que o algoritmo seja executado o número de vezes desejado (repetidas em um loop continuo), funciona até que a condição (no caso a variavel cont sendo maior ou igual a variavel numero) esteja satisfeita.

# Na estrutura while precisamos ESTABELECER uma condição, no caso essa condição é que a variavel cont seja maior ou igual a variavel numero.

# Quando essa condição for falsa ela se encerra ou não será executada.

cont = 1 # Iniciando a contagem com o contador
numero = int(input("Digite um número: ")) # Entrada de dados que vai se tornar a condição do while 

while cont <= numero: # A estrutura de repetição funciona se a variavel contador for maior ou igual a variavel número. 
   print("Victória") # Algoritmo que vai ser executado.
   cont += 1 # Como a estrutura while não tem um fim definido o cont += 1 é usado para que o algoritmo não seja executado de forma infinita.
print("Fim")