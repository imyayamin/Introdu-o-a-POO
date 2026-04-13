'''Enunciado:
Crie um programa em Python que simule um caixa de mercado.
Regras:
- O usuário digita o valor dos produtos
- O programa soma tudo
- Quando digitar 0, encerra
No final:
- Mostre o valor total
- Pergunte o valor pago
- Calcule o troco
- Se o valor pago for menor que o total, peça novamente novamente o valor pago'''

valor = 0
i = 1
while True:
    produto = float(input(f"Digite o valor do produto comprado{i}: "))
    if produto > 0:
        i += 1
        valor += produto
    else:
        break
        
print(f"O valor total é de: R$ {valor}")

while True:
    pago = float(input("Qual sera o valor pago?"))
    if pago > valor:
        troco = pago - valor
        print(f"O seu troco é de R$ {troco}")
        break
        
    elif pago == valor:
        print("O pagamento foi confirmado!")
        break
        
    else:
        print(f"Realize o pagamento novamente")
       
            
    

            
    