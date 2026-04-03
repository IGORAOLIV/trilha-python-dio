# Em Python, as funções são objetos de primeira classe, o que significa que elas podem ser tratadas como qualquer outro objeto. Isso inclui a capacidade de serem passadas como argumentos para outras funções, retornadas como valores de outras funções e atribuídas a variáveis.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida."


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação é = 20
exibir_resultado(10, 10, subtrair)  # O resultado da operação é = 0
exibir_resultado(10, 10, multiplicar)  # O resultado da operação é = 100
exibir_resultado(10, 10, dividir)  # O resultado da operação é = 1.0