# TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:
def elementos_comuns(lista1, lista2): # essa função recebe duas listas de números inteiros e retorna uma lista com os elementos comuns entre elas.
    set1 = set(map(int, lista1)) # converte as listas em conjuntos (set) para facilitar a comparação e encontrar os elementos comuns. O map(int, lista) é usado para converter cada elemento da lista de string para inteiro.
    set2 = set(map(int, lista2))
    return list(set1.intersection(set2)) # a função intersection() é usada para encontrar os elementos comuns entre os dois conjuntos. O resultado é convertido de volta para uma lista antes de ser retornado.

# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")
    