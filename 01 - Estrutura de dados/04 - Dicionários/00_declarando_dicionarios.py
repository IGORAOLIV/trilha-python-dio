# Dicionários são estruturas de dados que armazenam pares de chave-valor. Eles são mutáveis, o que significa que podem ser alterados após a criação. Os dicionários são úteis para armazenar informações relacionadas, como atributos de um objeto ou dados de configuração.

# Os dicionários são criados usando chaves {} e os pares de chave-valor são separados por dois pontos (:). As chaves devem ser únicas dentro do dicionário, e os valores podem ser de qualquer tipo de dado. {"chave1": "valor1", "chave2": "valor2"}
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

# Os dicionários também podem ser criados usando a função dict(), que aceita pares de chave-valor como argumentos nomeados. Isso é útil para criar dicionários de forma mais legível e concisa.
pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

# Os dicionários são mutáveis, o que significa que podemos adicionar, modificar ou remover pares de chave-valor após a criação do dicionário. Para adicionar um novo par de chave-valor, basta atribuir um valor a uma nova chave.
pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
