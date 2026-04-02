# Matriz é uma estrutura de dados bidimensional, ou seja, é uma lista de listas. Cada elemento da matriz é uma lista que representa uma linha da matriz. Para acessar um elemento específico da matriz, basta usar o nome da matriz seguido do índice da linha e do índice da coluna entre colchetes [].

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1

# A matriz também pode ser acessada usando índices negativos, onde o índice -1 se refere à última linha ou coluna, o índice -2 se refere à penúltima linha ou coluna, e assim por diante.

print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"
