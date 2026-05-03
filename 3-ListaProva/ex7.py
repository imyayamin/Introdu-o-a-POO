#Leia um número inteiro e verifique se ele é igual ao seu reverso.
#121 → Sim
#123 → Não

numero = int(input("Numero: "))
original = numero
reverso = 0

while numero > 0:
    digito = numero % 10
    reverso = reverso * 10 + digito
    numero //= 10

if original == reverso:
    print("Sim")
else:
    print("Não")