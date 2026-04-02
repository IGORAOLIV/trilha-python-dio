# Fatiamento de listas é uma técnica que permite acessar uma parte específica de uma lista, criando uma nova lista com os elementos selecionados. O fatiamento é feito usando a sintaxe [início:fim:passo], onde início é o índice do primeiro elemento a ser incluído, fim é o índice do primeiro elemento a ser excluído, e passo é o intervalo entre os elementos selecionados. Se início ou fim forem omitidos, eles assumirão os valores padrão de 0 e o comprimento da lista, respectivamente. Se passo for omitido, ele assumirá o valor padrão de 1.

lista = ["p", "y", "t", "h", "o", "n"]

# Fatiamento usando somente o índice de início
print(lista[2:])  # ["t", "h", "o", "n"]

# Fatiamento usando somente o índice de fim
print(lista[:2])  # ["p", "y"]

# Fatiamento usando o índice de início e o índice de fim
print(lista[1:3])  # ["y", "t"]

# Fatiamento usando o índice de início, o índice de fim e o passo
print(lista[0:3:2])  # ["p", "t"]

# Fatiamento usando o passo para selecionar elementos em intervalos regulares
print(lista[::2])  # ["p", "t", "o"]    

# Fatiamento sem especificar o início, o fim e o passo, o que retorna uma cópia da lista original
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]

# Fatiamento usando o passo negativo para selecionar elementos em ordem reversa
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
