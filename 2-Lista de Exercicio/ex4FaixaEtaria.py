'''Crie um algoritmo que receba a idade de uma pessoa e determine booleanamente se
ela pertence a cada faixa etária:
● É criança? (idade < 12)
● É adolescente? (12 ≤ idade ≤ 17)
● É adulto? (18 ≤ idade ≤ 64)
● É idoso? (idade ≥ 65)
Mostre o resultado de cada variável ao final.
'''

idade = int(input("Digite sua idade: "))

crianca = idade <= 12
adolescente =  12 <= idade and idade <= 17
adulto = 18 <= idade and idade <= 64
idoso = idade >= 65

print('É criança?', crianca)
print('É adolescente?', adolescente)
print('É adulto?', adulto)
print('É idoso?', idoso)