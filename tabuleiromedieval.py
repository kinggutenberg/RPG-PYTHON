from ctypes import LittleEndianStructure
from operator import truediv
from pickle import TRUE
import random
import os
from tabuleiro import Tabuleiro
from personagem import Personagem




class Tabuleiromedieval(Tabuleiro):

    def __init__(self, numdados, top_dados, linhas, colunas):
        self.numdados = numdados
        self.topdado = top_dados
        self.dimensao = [linhas, colunas]
        self.tab = []
        
        for i in range(0, self.dimensao[0]):
            c = []
            for j in range(0, self.dimensao[1]):

                c.append('⬜')
            self.tab.append(c)

    def printTab(self):
        for i in range(0, self.dimensao[0]):
            for j in range(0, self.dimensao[1]):
                print(self.tab[i][j], end=" ")
            print("")

    def lancardados(self):
        res = []
        for i in range(0, self.numdados):
            res.append(random.randint(1,self.topdado+1))
            return res

    def colocarpersonagem(self, personagem1, personagem2):

        linha = random.randint(0, 7)
        coluna = random.randint(0, 7)    
        if self.tab[linha][coluna]=='⬜':
            self.tab[linha][coluna]=personagem1.nome
            personagem1.posicao=[linha, coluna]
            while self.tab[linha][coluna]!='⬜':
               linha = random.randint(0, 7)
               coluna = random.randint(0, 7) 
        
            self.tab[linha][coluna]=personagem2.nome
            personagem2.posicao=[linha, coluna]

    def colocararmas(self, magia, arma, machado):
        linha = random.randint(0, 7)
        coluna = random.randint(0, 7)
        if self.tab[linha][coluna]=="⬜":
            self.tab[linha][coluna]= magia
            while self.tab[linha][coluna]!= "⬜":
                linha= random.randint(0, 7)
                coluna= random.randint(0, 7)
            self.tab[linha][coluna]=machado

    def movimentar(self, personagem):
        linha = random.randint(0, 7)
        coluna = random.randint(0, 7)
        
        if self.tab[linha][coluna]=="⬜":
            self.tab[linha][coluna] = personagem.nome 
            self.tab[personagem.posicao[0]][personagem.posicao[1]] = "⬜"
            personagem.posicao=[linha, coluna]
            
        elif self.tab[linha][coluna]!="⬜":
            
            if self.tab[linha][coluna]==self.j1.nome:
                if personagem.lutar(self.j1) == personagem.nome:
                    self.tab[linha][coluna] = personagem.nome
                    self.tab[personagem.posicao[0]][personagem.posicao[1]] = "⬜"


                    print("fim de jogo")
                else:
                    self.tab[linha][coluna] = self.j1.nome
                    self.tab[personagem.posicao[0]][personagem.posicao[1]] = "⬜"
                   

                    print("fim de jogo")

            elif self.tab[linha][coluna]==self.j2.nome:
                if personagem.lutar(self.j2) == personagem.nome:

                    self.tab[personagem.posicao[0]][personagem.posicao[1]] = "⬜"
                    self.tab[linha][coluna] = personagem.nome
                    

                    print("fim de jogo")
                else:
                    self.tab[personagem.posicao[0]][personagem.posicao[1]] = "⬜"
                    self.tab[linha][coluna] = self.j2.nome
                    
                    print("fim de jogo")

            #elif personagem.categoria == 2:
            #    for i in range(3, 0):
            #     if self.tab[linha][coluna] == personagem.magiadisponivel[i][0]:
            #        self.tab[personagem.posicao[0]][personagem.posicao[1]] = "⬜"
            #        self.tab[linha][coluna] = personagem.nome

        