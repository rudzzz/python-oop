class Veiculo:
    def __init__(self, cor, marca, rodas, tanque):
        self.cor = cor
        self.rodas = rodas
        self. marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros