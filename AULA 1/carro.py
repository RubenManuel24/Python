class Carro:
    def __init__(self, marca, cor, combustivel):
        self.marca = marca
        self.cor = cor
        self.combustivel = combustivel

        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if (self.ligado):
            print(f"O carro {self.marca} já está ligado")
        else:
            self.ligado = True
            print(f"O carro {self.marca} foi ligado")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O carro {self.marca} foi desligado")
        else:
            print(f"O carro {self.marca}já está desligaado")
    
    def acelerar(self):
        if self.ligado:
            self.velocidade = self.velocidade + 1
        else:
            print("Não pode acelerar porque o carro está desligado")

    def desacelerar(self):
        if self.ligado:
            self.velocidade = self.velocidade - 1
        else:
            print("Não pode desacelerar porque o carro está desligado")

    def mudarCor(self, novaCor):
        if novaCor == 1:
            self.cor = "Preto"
        elif novaCor == 2:
            self.cor = "Branco"
        elif novaCor == 3:
            self.cor = "Vermelho"
        else:
            self.cor = "Azul"


    def dados(self):
        print(F"Marca: {self.marca}\nCor: {self.cor}\nVelocidade: {self.velocidade}km/h\nCombustível: {self.combustivel} Litros")