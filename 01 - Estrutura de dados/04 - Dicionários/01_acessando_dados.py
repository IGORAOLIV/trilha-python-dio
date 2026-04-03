# Para acessar os valores armazenados em um dicionário, utilizamos as chaves correspondentes. Podemos acessar os valores usando a sintaxe de colchetes [] ou o método get(). A sintaxe de colchetes é a forma mais comum de acessar os valores, mas o método get() é útil quando queremos evitar erros caso a chave não exista no dicionário.

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
