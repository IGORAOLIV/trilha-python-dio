# tuplas aninhadas, ou seja, tuplas dentro de tuplas, podem ser usadas para criar estruturas de dados mais complexas, como matrizes. Uma matriz é uma coleção de elementos organizados em linhas e colunas.

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

alunos = (
    ("João", 20, "Engenharia"),
    ("Maria", 22, "Medicina"),
    ("Pedro", 19, "Direito"),
)

print(alunos[1])  # ("Maria", 22, "Medicina")
print(alunos[1][0])  # "Maria"
print(alunos[1][-1])  # "Medicina"
print(alunos[2][1])  # 19

