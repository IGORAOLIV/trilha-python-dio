# Para iterar sobre os itens de um dicionário, podemos utilizar uma estrutura de repetição for. O método items() do dicionário retorna uma lista de tuplas, onde cada tupla contém um par de chave-valor. Podemos usar essa estrutura para acessar tanto as chaves quanto os valores durante a iteração. porem esse metodo e mais utilizado para acessar os itens de um dicionario aninhado, onde cada valor e um dicionario, como no exemplo abaixo:

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

# O método items() é uma maneira mais eficiente e legível de iterar sobre os itens de um dicionário, especialmente quando precisamos acessar tanto as chaves quanto os valores. Ele retorna uma visão dos itens do dicionário, permitindo que possamos iterar diretamente sobre os pares de chave-valor sem precisar acessar os valores usando as chaves.

for chave, valor in contatos.items():
    print(chave, valor)
