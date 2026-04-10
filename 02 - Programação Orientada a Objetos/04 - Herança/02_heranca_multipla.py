# Herança Múltipla - é quando uma classe herda de mais de uma classe pai. A classe filha pode acessar os atributos e métodos de todas as classes pai, além de poder adicionar seus próprios atributos e métodos. No exemplo abaixo, a classe Ornitorrinco herda tanto da classe Mamifero quanto da classe Ave, o que permite que ela tenha características de ambos os tipos de animais.

class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): # O construtor da classe Mamifero é definido para receber um parâmetro adicional chamado cor_pelo, que indica a cor do pelo do mamífero. O **kw é usado para aceitar quaisquer outros argumentos adicionais que possam ser passados para o construtor, permitindo que ele seja flexível e possa ser usado em classes filhas que herdam de Mamifero.
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
