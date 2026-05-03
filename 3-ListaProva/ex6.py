#Crie uma função que recebe um número inteiro e retorna quantos divisores ele possui.

def divisores(n):
    divisor = 0

    for i in range(1, n + 1):

        if n % i == 0:
            divisor +=1

    return divisor
        
numero = int(input("Numero: "))

print(divisores(numero))
        
