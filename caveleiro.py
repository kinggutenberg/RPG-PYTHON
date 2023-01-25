from asyncio.format_helpers import _format_callback
from traceback import format_stack
from personagem import Personagem


class Cavaleiro(Personagem):
    mao_esquerda = 0
    mao_direita = 0
    destro = False

    def __init__(self, nome, destro):
        super().__init__(nome)
        self.destro = destro
        self.mao_esquerda = 0
        self.mao_direita = 0
        self.arma=[]
        self.armadisponivel = [["espadalonga", 5], ["espadapequena", 3]]
    def lutar(self, personagem):
        if (self.forca > personagem.forca):
            return self
        else:
            if (self.forca)
        

    def equipar(self, mao, forca):
        if(mao  == "E"):
            if not(self.destro):
                forca = forca + (1.5*forca)
                self.forca = self.forca - self.mao_esquerda
                self.mao_esquerda = forca
            else:
                    if (self.destro):
                    forca = (1.5*forca)
                    self.forca = self.forca - self.mao_direita
                    self.mao_direita = forca

                    self.forca = self.forca + forca
    def comoEstou(self):
                    print(self.nome)

