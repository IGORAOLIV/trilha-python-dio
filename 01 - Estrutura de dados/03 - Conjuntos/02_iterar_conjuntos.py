# Para iterar sobre os elementos de um conjunto, podemos usar um loop for. No entanto, como os conjuntos são não ordenados, a ordem dos elementos pode variar a cada execução do programa.

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

# Se quisermos acessar os elementos do conjunto com um índice, podemos usar a função enumerate() para obter o índice e o valor ao mesmo tempo.
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
