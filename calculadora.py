def somar(n1, n2):
    resultado = n1 + n2
    print(f'O resultado da soma é: {resultado}')
    return resultado

def subtrair(n1, n2):
    resultado = n1 - n2
    print(f'O resultado da subtração é: {resultado}')
    return resultado

def multiplicar(n1, n2):
    resultado = n1 * n2
    print(f'O resultado da multiplicação é: {resultado}')
    return resultado

def dividir(n1, n2):
    if n2 == 0:
        print('Divisão inválida!')
        
    else:   
        resultado = n1 / n2
        print(f'O resultado da divisão é: {resultado}')
        return resultado
    
def potencia(n1, n2):
    resultado = n1 ** n2
    print(f'O resultado da exponenciação é: {resultado}')
    return resultado
    
def modulo(n1, n2):
    resultado = n1 % n2
    print(f'O resultado do modulo é: {resultado}')
    return resultado
                
def calculadora(n1, n2, operacao):
    if operacao == '+':
        return somar(n1, n2)
    
    elif operacao == '-':
        return subtrair(n1, n2)
    
    elif operacao == '*':
        return multiplicar(n1, n2)
    
    elif operacao == '/':
        return dividir(n1, n2)
    
    elif operacao == '**':
        return potencia(n1, n2)
    
    elif operacao == '%':
        return modulo(n1, n2)
    
    else:
        print("Operação inválida!")
        
        
def ativa():
    
    while True:    
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        operacao = input("Selecione uma das operações (+, -, *, /, **, %): ")

        calculadora(n1, n2, operacao)
        
ativa()                 
