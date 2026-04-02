# a função count() é usada para contar o número de vezes que um elemento aparece em uma tupla, ela recebe como argumento o elemento que queremos contar e retorna o número de vezes que ele aparece na tupla

cores = (
    "vermelho",
    "azul",
    "verde",
    "azul",
)

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1
