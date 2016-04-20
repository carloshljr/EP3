import numpy as np
class jogo():  
    def __init__(self):
        self.velha = np.array([[1,2,3],[4,5,6],[7,8,9]])
        self.vez = 0
    def recebe_jogada(self,linha,coluna):
        if self.vez == 0:
            self.velha[linha][coluna] = 2
            self.vez = 1
        elif self.vez == 1:
            self.velha[linha][coluna] = 0
            self.vez = 0
            
    def verifica_ganhador(self):
        soma1 = self.velha[0][0] + self.velha[0][1] + self[0][2]
        soma2 = self.velha[1][0] + self.velha[1][1] + self[1][2]
        soma3 = self.velha[2][0] + self.velha[2][1] + self[2][2]
        soma4 = self.velha[0][0] + self.velha[1][0] + self[2][0]
        soma5 = self.velha[0][1] + self.velha[1][1] + self[2][1]
        soma6 = self.velha[0][2] + self.velha[1][2] + self[2][2]
        soma7 = self.velha[0][0] + self.velha[1][1] + self[2][2]
        soma8 = self.velha[2][0] + self.velha[1][1] + self[0][2]
        somas = [soma1,soma2,soma3,soma4,soma5,soma6,soma7,soma8]
        for t in somas:
            while not t == 0 or t == 6:
                return(-1)
            if t == 6: 
                return(1)
            elif t == 0:
                return(2)
            else:
                return(0)
    def limpa_jogadas(self):
        soma1 = self.velha[0][0] + self.velha[0][1] + self[0][2]
        soma2 = self.velha[1][0] + self.velha[1][1] + self[1][2]
        soma3 = self.velha[2][0] + self.velha[2][1] + self[2][2]
        soma4 = self.velha[0][0] + self.velha[1][0] + self[2][0]
        soma5 = self.velha[0][1] + self.velha[1][1] + self[2][1]
        soma6 = self.velha[0][2] + self.velha[1][2] + self[2][2]
        soma7 = self.velha[0][0] + self.velha[1][1] + self[2][2]
        soma8 = self.velha[2][0] + self.velha[1][1] + self[0][2]
        somas = [soma1,soma2,soma3,soma4,soma5,soma6,soma7,soma8]
        for t in somas:
            if t == 0 or t == 6:
                return(self.velha)