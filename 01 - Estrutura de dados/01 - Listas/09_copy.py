# O método copy() é utilizado para criar uma cópia rasa (shallow copy) de uma lista. Ele retorna uma nova lista que contém os mesmos elementos da lista original, mas as referências aos objetos dentro da lista são compartilhadas. Isso significa que se a lista contiver objetos mutáveis, como outras listas, as alterações feitas nesses objetos afetarão ambas as listas.

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(l2), id(lista))  # id(l2) e id(lista) são diferentes, pois são objetos distintos   

l2[0] = 100 # a alteração em l2 não afeta a lista original, pois l2 é uma cópia da lista original

print(lista)  # [1, "Python", [40, 30, 20]] - a alteração em l2 não afeta a lista original
print(l2)     # [100, "Python", [40, 30, 20]] - a alteração em l2 afeta apenas a cópia