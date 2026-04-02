# Compreensão de listas é uma técnica que permite criar uma nova lista a partir de uma sequência existente, aplicando uma expressão para cada elemento da sequência. A sintaxe para compreensão de listas é [expressão for item in sequência if condição], onde expressão é a operação que será aplicada a cada item da sequência, item é a variável que representa cada elemento da sequência, e condição é uma expressão opcional que filtra os elementos da sequência com base em um critério específico.

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]

# usando a função for para criar uma nova lista contendo apenas os números pares da lista original
for_pares = []
for numero in numeros:
    if numero % 2 == 0:
        for_pares.append(numero)
print(for_pares)

# usando a compeensão de listas para criar uma nova lista contendo apenas os números pares da lista original de forma mais concisa e legível
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]

# usando a função for para criar uma nova lista contendo o quadrado de cada número da lista original
for_quadrado = []  
for numero in numeros:
    for_quadrado.append(numero**2)
print(for_quadrado)

# usando a compreensão de listas para criar uma nova lista contendo o quadrado de cada número da lista original de forma mais concisa e legível
quadrado = [numero**2 for numero in numeros]
print(quadrado)
