# No "TODO", abaixo: Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:

def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = (2, 5, 6, 7, 9)
# No "TODO", abaixo: Defina tupla para receber os números inteiros:
    elementos = tuple(map(int, entrada))
    
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")