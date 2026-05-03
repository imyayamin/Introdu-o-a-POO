#Leia um número inteiro n e conte quantos números de 1 até n são:
#múltiplos de 3
#múltiplos de 5

numero = int(input("Numero: "))
contador3 = 0
contador5 = 0

for i in range(1, numero + 1):
    if i % 3 == 0:
        contador3 += 1
        
    if i % 5 == 0:
        contador5 +=1

print(f"3:{contador3}, 5:{contador5}")
