# O método isdisjoint() é usado para verificar se dois conjuntos não possuem elementos em comum. Ele retorna True se os conjuntos forem disjuntos (ou seja, não tiverem elementos em comum), caso contrário, retorna False.

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)
