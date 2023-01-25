from abc import ABC, abstractmethod
import random

class Tabuleiro:
    def iniciliza(self, j1, j2):
        self.j1 = j1
        self.j2 = j2
        

    @abstractmethod

    def jogardados(self, tabuleiro):
        dado = random.randint(1, 12)
        print(dado)
        
