'''numero = int(input())
soma = 0
sequencia = ''

for i in range(1, numero + 1):
    if i % 2 == 0:
        soma -= i
        
    else:
        soma +=i
    
    sequencia = f"{sequencia} {soma}"
    
print(sequencia)    
print(soma)'''

numero = int(input())
soma = 0
sequencia = ''

for i in range(1, numero + 1):
    if i % 2 == 0:
        soma -= i
        sequencia = f"{sequencia} - {i}"
    else:
        soma += i
        if i == 1:
            sequencia = f"{i}"
        else:
            sequencia = f"{sequencia} + {i}"

print(sequencia)
print(soma)