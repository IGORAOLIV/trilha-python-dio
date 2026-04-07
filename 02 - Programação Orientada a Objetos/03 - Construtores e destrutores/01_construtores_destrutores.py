# Construtores e destrutores são métodos especiais em Python que são chamados automaticamente quando um objeto é criado ou destruído, respectivamente. O construtor é definido usando o método __init__, enquanto o destruidor é definido usando o método __del__. O construtor é usado para inicializar os atributos do objeto, enquanto o destruidor é usado para liberar recursos ou realizar ações de limpeza quando o objeto é destruído.

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()
