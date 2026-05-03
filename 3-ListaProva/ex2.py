#Leia números inteiros até que a soma ultrapasse 100.
#Mostre: Quantos números foram necessários

soma = 0

contador = 0

while soma <= 100:
    numero = int(input("Digite um numero: "))
    soma = soma + numero
    contador += 1

print(contador)  