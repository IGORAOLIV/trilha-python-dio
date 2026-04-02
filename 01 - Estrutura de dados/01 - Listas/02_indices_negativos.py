# Índices negativos em listas permitem acessar os elementos a partir do final da lista. O índice -1 se refere ao último elemento, o índice -2 se refere ao penúltimo elemento, e assim por diante. Isso é útil quando você quer acessar os elementos mais recentes de uma lista sem precisar conhecer o comprimento da lista.

frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[-1])  # pera
print(frutas[-3])  # laranja
print(frutas[-2])  # uva
print(frutas[-4])  # maçã
