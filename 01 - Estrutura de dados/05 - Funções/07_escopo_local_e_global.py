# Escopo local e global se referem à visibilidade e acessibilidade de variáveis em diferentes partes do código. O escopo local é o contexto dentro de uma função onde as variáveis são definidas e acessíveis apenas dentro dessa função. O escopo global, por outro lado, é o contexto fora de todas as funções, onde as variáveis são acessíveis em todo o código. Usar a palavra-chave global não é recomendado, pois pode levar a código difícil de entender e manter. Em vez disso, é melhor passar variáveis como argumentos para funções ou usar classes para encapsular dados e comportamentos relacionados.

salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


novo_salario = salario_bonus(500)  # 2500
print(novo_salario)
