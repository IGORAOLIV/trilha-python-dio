# A diferença de conjuntos é uma operação que retorna um novo conjunto contendo os elementos que estão presentes em um conjunto, mas não estão presentes no outro conjunto. Em Python, podemos usar o método difference() ou o operador - para realizar a diferença de conjuntos.

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)
