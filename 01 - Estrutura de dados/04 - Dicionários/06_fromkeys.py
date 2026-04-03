# metodo fromkeys() - retorna um novo dicionário com as chaves especificadas e os valores definidos como None ou como um valor especificado

resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

# podemos definir um valor para as chaves do dicionário que será o mesmo para todas as chaves
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
