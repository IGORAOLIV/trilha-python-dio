# iterar tuplas segue a mesma lógica de iterar listas, ou seja, podemos usar o for para iterar os elementos da tupla e a função enumerate para obter o índice e o valor de cada elemento da tupla

carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
