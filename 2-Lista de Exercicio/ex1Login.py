'''Crie um algoritmo que verifique se um usuário pode acessar um sistema. O login só
deve ser considerado válido se:
● O usuário for "admin" E a senha for "1234".
Use operadores lógicos para verificar se o login é válido. Armazene o resultado em
uma variável chamada login_valido e exiba o resultado.
'''

usuario = input("Qual seu tipo de usuario? Ex: comum, admin: ")

senha = input('Digite a chave de acesso: ')

login_valido = (usuario == 'admin') and (senha == '1234')

print('Login valido?', login_valido)
 