from mago import Mago
from personagem import Personagem
from tabuleiromedieval import Tabuleiromedieval
from tabuleiro import Tabuleiro
from anao import Anao
import time



mage = Mago("🧙‍♂️")
anao = Anao("🤖")



 
tabuleiro = Tabuleiromedieval(2, 6, 8, 8)
tabuleiro.iniciliza(mage, anao)
tabuleiro.colocarpersonagem(mage, anao)
print()
for i in range (0, 3):
 tabuleiro.colocararmas(mage.magiadisponivel[i][0], "lança", anao.armadisponivel[i][0])
tabuleiro.printTab()
print()

tabuleiro.printTab()
movimentar=input('quem vai se movimentar primeiro?')

while True:
    if movimentar=='mago':


        tabuleiro.movimentar(mage)
        time.sleep(3)
        tabuleiro.printTab()
        print()
        movimentar="anao"
    elif movimentar=="anao":
        tabuleiro.movimentar(anao)

        time.sleep(6)
        tabuleiro.printTab()
        print()
        movimentar="mago"