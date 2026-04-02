# a lista é passada como uma pilha (LIFO - Last In First Out), ou seja, o último elemento adicionado é o primeiro a ser removido. O método pop é utilizado para remover e retornar o último elemento da lista. Ele também pode receber um índice como argumento para remover e retornar um elemento específico da lista.

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python
