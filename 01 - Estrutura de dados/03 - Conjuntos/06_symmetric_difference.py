# A diferença simétrica de conjuntos é uma operação que retorna um novo conjunto contendo os elementos que estão presentes em um dos conjuntos, mas não estão presentes em ambos os conjuntos. Em Python, podemos usar o método symmetric_difference() ou o operador ^ para realizar a diferença simétrica de conjuntos.

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)
