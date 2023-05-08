num1 = int(input("Digite um número1: "))
num2 = int(input("Digite um número2: "))
num3 = int(input("Digite um número3: "))

if num1 == num2 == num3:
    print("Os números são iguais.")
elif num1 > num2 and num1 > num3:
    print("O primeiro número é o maior")
elif num2 > num1 and num2 > num3:
    print("O segundo número é maior")
else:
    print("O terceiro número é maior")