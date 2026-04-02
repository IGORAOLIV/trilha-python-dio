# O método remove é utilizado para remover a primeira ocorrência de um elemento específico da lista. Ele recebe o elemento a ser removido como argumento e remove a primeira ocorrência desse elemento da lista. Se o elemento não for encontrado, ele levanta um ValueError.

linguagens = ["python", "js", "c", "java", "csharp", "java"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp", "java"]

# caso exista mais de uma ocorrência do elemento na lista, o remove irá remover apenas a primeira ocorrência do elemento.

linguagens.remove("java")

print(linguagens)  # ["python", "js", "csharp", "java"]

