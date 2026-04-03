# metodo popitem() - remove e retorna um par chave-valor aleatório do dicionário, ou um erro caso o dicionário esteja vazio,a diferença para o método pop() é que o popitem() não recebe a chave como argumento, ele remove e retorna um par chave-valor aleatório do dicionário

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError
