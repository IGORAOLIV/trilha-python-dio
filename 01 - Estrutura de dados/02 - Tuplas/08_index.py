# a função index() é usada para obter o índice do primeiro elemento encontrado na tupla, ela recebe como argumento o elemento que queremos encontrar e retorna o índice do primeiro elemento encontrado na tupla, caso o elemento não seja encontrado, a função index() lança uma exceção ValueError

linguagens = ("python", "js", "c", "java", "csharp",)

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0
