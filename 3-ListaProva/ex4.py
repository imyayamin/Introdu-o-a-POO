#Leia números inteiros até o usuário digitar um número negativo.
#Mostre: Soma apenas dos números ímpares

impar = 0
soma = 0

while True:
    numero = int(input("Numero: "))

    if numero < 0:
        break
    
    elif numero % 2:
        impar = numero
        soma = soma + impar

print(soma)

    