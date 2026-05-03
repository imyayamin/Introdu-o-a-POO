#Leia um número e mostre a soma de todos os números de 1 até ele.

numero = int(input())

total = 0

for i in range(1, numero + 1):
    total = total + 1

print(total)