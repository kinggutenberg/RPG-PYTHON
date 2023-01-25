from personagem import Personagem

class Mago(Personagem):

    def __init__(self, nome):
        super().__init__(nome)
        self.magia = []
        self.magiadisponivel = [['🐉', 4], ['👻​', 2], ['☃', 2]]
        self.categoria=2
     
    def aprendermagia(self, nome, forca):
        self.nome = nome
        self.forca = forca
        if(nome in self.magia):
            print("ja aprendi essa")
            return False
        else:
            print(self.forca)
            self.magia.append(nome)
            self.forca 