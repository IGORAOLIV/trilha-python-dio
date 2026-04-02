# O método issubset() é usado para verificar se um conjunto é um subconjunto de outro conjunto. Ele retorna True se todos os elementos do conjunto atual estiverem presentes no conjunto especificado, caso contrário, retorna False.

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)
