# O método add() é usado para adicionar um elemento a um conjunto. Se o elemento já estiver presente no conjunto, ele não será adicionado novamente, pois os conjuntos não permitem elementos duplicados.

sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)
