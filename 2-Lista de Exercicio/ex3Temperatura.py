'''Crie um algoritmo que receba uma temperatura em graus Celsius e mostre:
● Se a temperatura é maior que 30
● Se a temperatura é menor ou igual a 0'''

temperatura = float(input("Digite a temperatura atual em graus Celsius: "))

if(temperatura > 30):
    print("A temperatura é maior que 30")

elif(temperatura <= 0):
        print("A temperatura é menor ou igual a 0")

else:
      print("A temperatura é de : ", temperatura, 'graus celsius')
              