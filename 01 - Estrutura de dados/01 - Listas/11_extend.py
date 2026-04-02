# Extend é um método utilizado para adicionar elementos de uma lista a outra lista. Ele é diferente do append, pois o append adiciona um elemento como um todo, enquanto o extend adiciona cada elemento da lista individualmente.

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

# caso elementos sejam adicionados de forma repetida, o extend irá adicionar os elementos normalmente, sem se preocupar com a repetição.
linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp", "java", "csharp"]