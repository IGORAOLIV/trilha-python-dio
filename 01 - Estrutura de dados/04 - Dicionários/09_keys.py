# metodo keys() - retorna uma lista de chaves do dicionário

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)

novo_dicionario = {"a": "teste", 1: "teste2", "b": "Python"}
print(novo_dicionario.keys())  # dict_keys(['a', 1, 'b'])