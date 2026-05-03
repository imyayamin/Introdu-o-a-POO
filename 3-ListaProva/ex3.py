#Leia um número inteiro positivo e divida ele por 2 sucessivamente até chegar em 1.
#Mostre todos os valores.

numero = int(input())

sequencia = f'{numero}'

while True:
    numero = numero // 2

    sequencia = f"{sequencia}  {numero}"

    if numero == 1:
        break

print(sequencia)