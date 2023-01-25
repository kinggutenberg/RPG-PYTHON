from personagem import Personagem

class Anao(Personagem):

    def __init__(self,nome):
     super().__init__(nome)
     self.machado = 0.0
     self.agilidade = 10
     self.arma = []
     self.armadisponivel =[['🔨', 5], ['🦾​', 3], ['🔧', 1]]
     self.categoria= 1


    def equipar(self, forca):
        self.machado
        self.agilidade = 10-self.machado
        self.forca = self.machado*self.agilidade/10
