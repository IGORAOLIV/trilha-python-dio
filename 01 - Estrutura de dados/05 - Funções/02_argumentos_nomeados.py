# Argumentos nomeados são uma forma de passar argumentos para uma função usando o nome do parâmetro em vez da posição. Isso torna o código mais legível e permite que os argumentos sejam passados em qualquer ordem.

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # nomear argumentos dessa formna pode gerar erros com relação a ordem dos argumentos.

salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # nomear argumentos dessa forma é mais legível e não gera erros com relação a ordem dos argumentos. porem ele ainda é inseguro caso o nome do argumento seja digitado errado ou modificado, o que pode gerar erros de argumento inesperado.

salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # usando os dois asteriscos podemos passar um dicionário como argumentos nomeados, o que é útil quando os dados estão em um formato de dicionário e queremos passá-los para uma função que espera argumentos nomeados.
