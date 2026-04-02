# Conjuntos são uma coleção de itens únicos e não ordenados. Eles são úteis para armazenar elementos distintos e realizar operações matemáticas como união, interseção e diferença.

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

linguagens = {"Python", "Java", "C++", "Python"}  
print(linguagens) # {"Python", "Java", "C++"}