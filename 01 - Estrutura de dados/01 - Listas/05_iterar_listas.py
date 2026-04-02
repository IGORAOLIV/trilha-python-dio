# Iterar listas é uma técnica que permite percorrer cada elemento de uma lista e realizar uma ação específica para cada elemento. A maneira mais comum de iterar uma lista em Python é usando um loop for, onde você pode acessar cada elemento da lista em cada iteração do loop. Além disso, a função enumerate() pode ser usada para obter o índice de cada elemento junto com o valor do elemento durante a iteração.

carros = ["gol", "celta", "palio"]

# Iterando a lista de carros usando um loop for
for carro in carros:
    print(carro)

# Iterando a lista de carros usando a função enumerate() para obter o índice e o valor de cada elemento
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
