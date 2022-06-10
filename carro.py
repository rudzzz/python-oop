from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, cor, marca, tanque):
        Veiculo.__init(self, cor, 4, marca, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print('Tanque cheio')
        else:
            self.tanque += litros
