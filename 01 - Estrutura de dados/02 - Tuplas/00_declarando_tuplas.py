# Tuplas são estruturas de dados parecidas com listas, porém são imutáveis, ou seja, não podem ser alteradas após a sua criação. Elas são definidas usando parênteses ().

frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",) # a virgula no final é utilizada para o caso de tuplas com um único elemento, para que o Python reconheça como uma tupla e não como um valor comum.
print(pais)
