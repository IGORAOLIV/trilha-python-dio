# metodo pop() - remove o item com a chave especificada e retorna o valor correspondente, ou um valor padrão caso a chave não exista no dicionário

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# caso a chave não exista no dicionário, podemos definir um valor padrão para ser retornado
resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
