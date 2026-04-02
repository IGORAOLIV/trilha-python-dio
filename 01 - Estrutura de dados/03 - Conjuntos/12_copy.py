# O método copy() é usado para criar uma cópia superficial de um conjunto. Ele retorna um novo conjunto que contém os mesmos elementos do conjunto original. A cópia é independente do conjunto original, o que significa que alterações feitas em um conjunto não afetarão o outro.

sorteio = {1, 23}

print(sorteio)  # {1, 23}

sorteio.copy()

print(sorteio)  # {1, 23}
