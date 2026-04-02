# Para acessar os dados de um conjunto, é necessário convertê-lo para uma estrutura de dados que permita indexação, como uma lista ou tupla. Isso ocorre porque os conjuntos são não ordenados e não suportam acesso por índice.

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
