# Desafio Smart Home: Crie uma classe SmartTV que tenha os seguintes atributos: marca, tamanho, canal (padrão 1), volume (padrão 10) e ligada (booleano padrão False). Além disso, a classe deve ter os seguintes métodos: ligar_desligar (altera oo estado de ligada),  mudar_canal (recebe um número de canal e imprime "Canal mudado para {número do canal}", só deve funcionar quando a TV estiver ligada), ajustar_volume (aumenta ou diminui o volume, garantindo que fique entre 0 e 100) e __str__ (retorna uma string com as informações da TV). Implemente a classe e crie um objeto para testar seus métodos.

class SmartTV:
    def __init__(self, marca, tamanho, canal=1, volume=10, ligada=False):
        self.marca = marca
        self.tamanho = tamanho
        self.canal = canal
        self.volume = volume
        self.ligada = ligada
    
    def ligar_desligar(self):
        self.ligada = not self.ligada
        estado = "ligada" if self.ligada else "desligada"
        print(f"A TV está agora {estado}.")
    
    def mudar_canal(self, numero_canal):
        if self.ligada:
            self.canal = numero_canal
            print(f"Canal mudado para {self.canal}.")
        else:
            print("A TV está desligada. Ligue a TV para mudar o canal.")

    def ajustar_volume(self, quantidade):
        if self.ligada:
            self.volume = max(0, min(100, self.volume + quantidade))
            print(f"Volume ajustado para {self.volume}.")
        else:
            print("A TV está desligada. Ligue a TV para ajustar o volume.")

    def __str__(self):
        return f"SmartTV: {self.marca}, {self.tamanho} polegadas, Canal: {self.canal}, Volume: {self.volume}, Ligada: {self.ligada}"
    
tv = SmartTV("Samsung", 55)
print(tv)

tv.ligar_desligar()
tv.mudar_canal(5)
tv.ajustar_volume(15)
print(tv)   
tv.ajustar_volume(-30)
print(tv)   
tv.ligar_desligar()
tv.mudar_canal(10)