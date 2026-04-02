# Índices negativos em tuplas são usados para acessar elementos a partir do final da tupla. O índice -1 se refere ao último elemento, -2 ao penúltimo, e assim por diante.

frutas = (
    "maçã",
    "laranja",
    "uva",
    "pera",
)

print(frutas[-1])  # pera
print(frutas[-3])  # laranja
