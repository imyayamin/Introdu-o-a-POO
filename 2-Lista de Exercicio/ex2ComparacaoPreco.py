'''Crie um algoritmo que receba o preço de dois produtos, verifique e exiba:
● Se o produto A é mais caro que o produto B
● Se os dois produtos têm o mesmo preço
'''

ProdutoA = float(input("Qual o valor do produto A? "))
ProdutoB = float(input("Qual o valor do produto B? "))

if(ProdutoA > ProdutoB):
    print("Produto A é mais caro que o B")

elif(ProdutoA == ProdutoB):
    print("Os produtos tem o mesmo valor!")

else: 
    print("O Produto B é mais caro")    
