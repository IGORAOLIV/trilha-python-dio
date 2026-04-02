# sorted() é uma função embutida em Python que retorna uma nova lista ordenada a partir de um iterável. Ela pode receber dois parâmetros opcionais: reverse e key.

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

# a função sorted() também pode ser usada sem o parâmetro key para ordenar os elementos em ordem alfabética. O parâmetro reverse pode ser usado para ordenar em ordem decrescente.
print(sorted(linguagens))  # ["c", "csharp", "java", "js", "python"]
print(linguagens)  # ["python", "js", "c", "java", "csharp"]
print(sorted(linguagens, reverse=True))  # ["python", "js", "java", "csharp", "c"]