# Função é um bloco de código que só é executado quando é chamado. Você pode passar dados, conhecidos como parâmetros, para uma função. Uma função pode retornar dados como resultado. É uma maneira de organizar o código em blocos reutilizáveis.

def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Igor")
exibir_mensagem_2("Igor")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
