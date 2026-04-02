# O método discard() é usado para remover um elemento específico de um conjunto. Ele aceita um argumento, que é o elemento a ser removido. Se o elemento estiver presente no conjunto, ele será removido. Se o elemento não estiver presente, o método não fará nada e não gerará um erro.

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
