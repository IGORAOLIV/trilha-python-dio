# sort() é um método de lista que ordena os elementos da própria lista. Ele não retorna uma nova lista, mas sim modifica a lista original. O método sort() pode receber dois parâmetros opcionais: reverse e key.

# O parâmetro reverse é um booleano que indica se a ordenação deve ser feita em ordem decrescente (True) ou crescente (False). O padrão é False.
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# O parâmetro key é uma função que recebe um elemento da lista e retorna um valor que será usado para a ordenação. Por exemplo, podemos usar a função len() para ordenar as linguagens de acordo com o tamanho do nome. Passando a função anonima lambda x: len(x) como argumento para o parâmetro key, a ordenação será feita com base no comprimento de cada string.
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
