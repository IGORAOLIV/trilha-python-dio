# A classe define o molde para criar objetos, ou seja, é a estrutura que define os atributos e comportamentos comuns a todos os objetos de um determinado tipo. Já o objeto é uma instância concreta de uma classe, ou seja, é um elemento específico criado a partir da classe, com seus próprios valores para os atributos e a capacidade de executar os comportamentos definidos pela classe.

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # O método __init__ é um método especial em Python que é chamado automaticamente quando um objeto é criado a partir de uma classe. Ele é usado para inicializar os atributos do objeto com os valores fornecidos como argumentos durante a criação do objeto.
        self.cor = cor # O self é uma referência ao próprio objeto que está sendo criado. Ele é usado para acessar os atributos e métodos do objeto dentro da classe. Ao usar self, você pode atribuir valores aos atributos do objeto e chamar seus métodos.
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self): # O método buzinar é um comportamento definido para a classe Bicicleta. Ele é um método de instância, o que significa que pode ser chamado em objetos específicos da classe. Quando o método buzinar é chamado, ele executa as ações definidas dentro do método, que neste caso são imprimir "Buzinando..." e "Plim plim...". Isso simula o som de uma buzina de bicicleta.
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self): # O método __str__ é um método especial em Python que é usado para definir a representação em string de um objeto. Ele é chamado quando você tenta imprimir um objeto ou convertê-lo para uma string. No exemplo fornecido, o método __str__ foi implementado para retornar uma string formatada que inclui o nome da classe e os atributos do objeto. Isso permite que, ao imprimir um objeto da classe Bicicleta, seja exibida uma representação legível e informativa do objeto, mostrando seus atributos e valores.
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
