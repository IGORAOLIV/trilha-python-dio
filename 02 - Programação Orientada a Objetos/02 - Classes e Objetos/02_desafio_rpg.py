# Desafio: Crie uma classe Personagem para um jogo de RPG. A classe deve ter os seguintes atributos: nome, classe, nível e pontos de vida (HP). Além disso, a classe deve ter os seguintes métodos: treinar (aumenta o nível do personagem), receber dano (diminui os pontos de vida) e atacar (causa dano a outro personagem). Implemente a classe e crie dois personagens para testar seus métodos.

class Personagem:
    def __init__(self, nome, classe, nivel=1, hp=100):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.hp = hp
    
    def treinar(self):
        self.nivel += 1
        print(f"{self.nome} subiu para o nivel {self.nivel}!")
    
    def recebe_dano(self, dano):
        self.hp -= dano
        print(f"{self.nome} recebeu {dano} de dano e agora tem {self.hp} de HP.")

    def atacar(self, alvo):
        dano = self.nivel * 10
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        alvo.recebe_dano(dano)
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
p1 = Personagem("Aragorn", "Guerreiro")
p2 = Personagem("Gandalf", "Mago")

print(p1)
print(p2)

p1.treinar()
p1.atacar(p2)
print(p1)
print(p2)