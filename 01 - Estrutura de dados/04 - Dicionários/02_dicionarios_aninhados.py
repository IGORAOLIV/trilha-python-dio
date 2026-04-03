# Dicionários aninhados são dicionários que contêm outros dicionários como valores. Eles são úteis para representar estruturas de dados mais complexas, como informações de contato, onde cada contato pode ter vários atributos, como nome, telefone e endereço. Para acessar os valores em um dicionário aninhado, utilizamos múltiplos colchetes [] para navegar pelas camadas do dicionário.

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

