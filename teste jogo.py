import numpy as np
class jogo():  
    def __init__(self):
        self.velha = [[4,4,4],[4,4,4],[4,4,4]]
        self.vez = 0
    def recebe_jogada(self,linha,coluna):
        if self.vez == 0:
            self.velha[linha][coluna] = 2
            self.vez = 1
        elif self.vez == 1:
            self.velha[linha][coluna] = -1
            self.vez = 0
            
    def verifica_ganhador(self):
        soma1 = self.velha[0][0] + self.velha[0][1] + self.velha[0][2]
        soma2 = self.velha[1][0] + self.velha[1][1] + self.velha[1][2]
        soma3 = self.velha[2][0] + self.velha[2][1] + self.velha[2][2]
        soma4 = self.velha[0][0] + self.velha[1][0] + self.velha[2][0]
        soma5 = self.velha[0][1] + self.velha[1][1] + self.velha[2][1]
        soma6 = self.velha[0][2] + self.velha[1][2] + self.velha[2][2]
        soma7 = self.velha[0][0] + self.velha[1][1] + self.velha[2][2]
        soma8 = self.velha[2][0] + self.velha[1][1] + self.velha[0][2]
        if soma1 == 6 or soma2 == 6 or soma3 == 6 or soma4 == 6 or soma5 == 6 or soma7 == 6 or soma8 == 6 or soma6 == 6: 
            return(1)
        elif soma1 == -3 or soma2 == -3 or soma3 == -3 or soma4 == -3 or soma5 == -3 or soma6 == -3 or soma7 == -3 or soma8 == -3:
            return(2)
        else:
            return(0)
                
    def limpa_jogadas(self):
         self.velha = np.array([[4,4,4],[4,4,4],[4,4,4]])
         
import tkinter as tk

class Tabuleiro():
    "Classe tabuleiro"
    
    def __init__(self,nome):
        self.game = jogo()
        self.root = tk.Tk()
        self.nome = self.root.title(nome)
        self.vez = 0
        self.label1 = tk.Label()
        self.label2 =tk.Label()
        self.label3 = tk.Label()
        self.label1.grid(row = 0, column = 0)
        self.label2.grid(row = 1, column = 0)
        self.label3.grid(row = 2, column = 0)
        self.Canvas = tk.Canvas(self.label1,width = 200, height = 20, bg = "black")
        self.Canvas.create_text(80,10,text = "{0}".format(nome), fill = "white")
        self.Canvas.pack()
        self.Canvas2 = tk.Canvas(self.label3,width = 200, height = 20, bg = "black")
        def callback1():
            if self.vez == 0:
                self.b1.configure(text = "X")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:O", fill = "white")
                self.vez = 1
                self.game.velha[0][0] = 0
            else:
                self.b1.configure(text = "O")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:X", fill = "white")
                self.vez = 0
                self.game.velha[0][0] = 2
            self.game.recebe_jogada(0,0)
            ganhador = self.game.verifica_ganhador()
            if ganhador == 1:
                print("X ganhou")
                self.game.limpa_jogadas()
            if ganhador == 2:
                print("O ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            print(1)
        def callback2():
            if self.vez == 0:
                self.b2.configure(text = "X")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:O", fill = "white")
                self.game.velha[0][1] = 0                
                self.vez = 1
            else:
                self.b2.configure(text = "O")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:X", fill = "white")
                self.game.velha[0][1] = 2                
                self.vez = 0
            self.game.recebe_jogada(0,1)
            ganhador = self.game.verifica_ganhador()
            if ganhador == 1:
                print("X ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            if ganhador == 2:
                print("O ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            print(2)
        def callback3():
            if self.vez == 0:
                self.b3.configure(text = "X")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:O", fill = "white")
                self.game.velha[0][2] = 0                
                self.vez = 1
            else:
                self.b3.configure(text = "O")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:X", fill = "white")
                self.game.velha[0][2] = 2      
                self.vez = 0
            self.game.recebe_jogada(0,2)
            ganhador = self.game.verifica_ganhador()
            if ganhador == 1:
                print("X ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            if ganhador == 2:
                print("O ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            print(3)
        def callback4():
            if self.vez == 0:
                self.b4.configure(text = "X")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:O", fill = "white")
                self.game.velha[1][0] = 0      
                self.vez = 1
            else:
                self.b4.configure(text = "O")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:X", fill = "white")
                self.game.velha[1][0] = 2      
                self.vez = 0
            self.game.recebe_jogada(1,0)
            ganhador = self.game.verifica_ganhador()
            if ganhador == 1:
                print("X ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            if ganhador == 2:
                print("O ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            print(4)
        def callback5():
            if self.vez == 0:
                self.b5.configure(text = "X")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:O", fill = "white")
                self.game.velha[1][1] = 0      
                self.vez = 1
            else:
                self.b5.configure(text = "O")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:X", fill = "white")
                self.game.velha[1][1] = 2      
                self.vez = 0
            self.game.recebe_jogada(1,1)
            ganhador = self.game.verifica_ganhador()
            if ganhador == 1:
                print("X ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            if ganhador == 2:
                print("O ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            print(5)
        def callback6():
            if self.vez == 0:
                self.b6.configure(text = "X")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:O", fill = "white")
                self.game.velha[1][2] = 0      
                self.vez = 1
            else:
                self.b6.configure(text = "O")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:X", fill = "white")
                self.game.velha[1][2] = 2      
                self.vez = 0
            self.game.recebe_jogada(1,2)
            ganhador = self.game.verifica_ganhador()
            if ganhador == 1:
                print("X ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            if ganhador == 2:
                print("O ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            print(6)        
        def callback7():
            if self.vez == 0:
                self.b7.configure(text = "X")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:O", fill = "white")
                self.game.velha[2][0] = 0     
                self.vez = 1
            else:
                self.b7.configure(text = "O")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:X", fill = "white")
                self.game.velha[2][0] = 2      
                self.vez = 0
            self.game.recebe_jogada(2,0)
            ganhador = self.game.verifica_ganhador()
            if ganhador == 1:
                print("X ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            if ganhador == 2:
                print("O ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            print(7)
        def callback8():
            if self.vez == 0:
                self.b8.configure(text = "X")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:O", fill = "white")
                self.game.velha[2][1] = 0      
                self.vez = 1
            else:
                self.b8.configure(text = "O")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:X", fill = "white")
                self.game.velha[2][1] = 2      
                self.vez = 0
            self.game.recebe_jogada(2,1)
            ganhador = self.game.verifica_ganhador()
            if ganhador == 1:
                print("X ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            if ganhador == 2:
                print("O ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            print(8)
        def callback9():
            if self.vez == 0:
                self.b9.configure(text = "X")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:O", fill = "white")
                self.game.velha[2][2] = 0      
                self.vez = 1
            else:
                self.b9.configure(text = "O")
                self.Canvas2.create_text(80,10,text = "Proxima jogada:X", fill = "white")
                self.game.velha[2][2] = 2      
                self.vez = 0
            self.game.recebe_jogada(2,2)
            ganhador = self.game.verifica_ganhador()
            if ganhador == 1:
                print("X ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            if ganhador == 2:
                print("O ganhou")
                self.game.limpa_jogadas()
                self.b1.configure(text = "")
                self.b2.configure(text = "")
                self.b3.configure(text = "")
                self.b4.configure(text = "")
                self.b5.configure(text = "")
                self.b6.configure(text = "")                
                self.b7.configure(text = "")
                self.b8.configure(text = "")
                self.b9.configure(text = "")
            print(9)
        
        self.b1 = tk.Button(self.label2, text="", width = 10, height = 5)
        self.b2 = tk.Button(self.label2, text="",width = 10, height = 5)
        self.b3 = tk.Button(self.label2, text="", width = 10, height = 5)        
        self.b4 = tk.Button(self.label2, text="",  width = 10, height = 5)
        self.b5 = tk.Button(self.label2, text="", width = 10, height = 5)
        self.b6 = tk.Button(self.label2, text="", width = 10, height = 5)
        self.b7 = tk.Button(self.label2, text="", width = 10, height = 5)
        self.b8 = tk.Button(self.label2, text="", width = 10, height = 5)
        self.b9 = tk.Button(self.label2, text="", width = 10, height = 5)
        
        
        self.b1.configure(command = callback1)
        self.b2.configure(command = callback2)
        self.b3.configure(command = callback3)
        self.b4.configure(command = callback4)
        self.b5.configure(command = callback5)
        self.b6.configure(command = callback6)
        self.b7.configure(command = callback7)
        self.b8.configure(command = callback8)
        self.b9.configure(command = callback9)
        

        
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
        self.b4.pack()
        self.b5.pack()
        self.b6.pack()
        self.b7.pack()
        self.b8.pack()
        self.b9.pack()
        
               
        
        self.b1.grid(row = 0, column = 0)
        self.b2.grid(row = 0, column = 1)
        self.b3.grid(row = 0, column = 2)
        self.b4.grid(row = 1, column = 0)
        self.b5.grid(row = 1, column = 1)
        self.b6.grid(row = 1, column = 2)
        self.b7.grid(row = 2, column = 0)
        self.b8.grid(row = 2, column = 1)
        self.b9.grid(row = 2, column = 2)
        
    
        self.Canvas2.pack()
        
    def iniciar(self):
        tk.mainloop()
    
a = Tabuleiro("Jogo da velha")
tk.mainloop()