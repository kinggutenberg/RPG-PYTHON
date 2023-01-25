import random



class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.forca = 0
        self.posicao = []

    def lutar(self, personagem):
        if self.forca == 0 and personagem.forca == 0:
            p = 50
            dado = random.randint(0,100)
            if p > dado:
                print('O JOGADOR {} GANHOU!'.format(self.nome))
                return self.nome

            else:
                print('O JOGADOR {} GANHOU!'.format(personagem.nome))
                return personagem.nome
        else:
            S = self.forca + personagem.forca
            p = (self.forca*100)/S
            dado = random.randint(0, 100)
            if p > dado:
                print('O JOGADOR {} GANHOU!'.format(self.nome))
                return self.nome

            else:
                print('O JOGADOR {} GANHOU!'.format(personagem.nome))
                return personagem.nome
        
    


        

        
 