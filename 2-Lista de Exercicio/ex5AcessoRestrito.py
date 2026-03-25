'''Um sistema de acesso só permite entrada se certas condições forem atendidas,
combinando idade, senha e status especial. Critérios:
● A pessoa deve ter idade maior ou igual a 18 OU possuir autorização especial
(autorizacao = True).
● A senha digitada não pode ser "123".
● O usuário não pode estar bloqueado (bloqueado = True).
Use apenas operadores lógicos (and, or, not) e comparações para criar a variável
acesso_permitido. Exiba o resultado booleano.'''

idade = int(input("Digite sua idade: "))

autorizacao = input("Se for menor, possui autorização? (True/False): ")

senha = input("Digite sua senha: ")

bloquado = input("Seu usuario esta bloqueado? (True/False): ")

acesso_liberado = (idade >= 18 or autorizacao == 'True') and senha != '123' and bloquado == 'False'

print('Acesso liberado?', acesso_liberado)
