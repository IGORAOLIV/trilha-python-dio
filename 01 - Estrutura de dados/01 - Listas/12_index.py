# O método index é utilizado para encontrar o índice de um elemento em uma lista. Ele retorna o índice da primeira ocorrência do elemento na lista. Se o elemento não for encontrado, ele levanta um ValueError.

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

# caso exista mais de uma ocorrência do elemento na lista, o index irá retornar o índice da primeira ocorrência.
linguagens.append("java") # adicionando mais uma ocorrência de "java" usando o append
print(linguagens)  # ["python", "js", "c", "java", "csharp", "java"]
print(linguagens.index("java"))  # 3

# usando counte é possível contar quantas vezes um elemento aparece na lista, o que pode ser útil para saber quantas vezes um elemento foi adicionado usando o extend, por exemplo.
print(linguagens.count("java"))  # 2