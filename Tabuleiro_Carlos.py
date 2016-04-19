# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 09:49:28 2016

@author: Carlosjunior
"""
import tkinter as tk
from tkinter import ttk

class Tabuleiro():
    "Classe tabuleiro"
    
    def __init__(self,nome):
        self.root = tk.Tk()
        self.Canvas = tk.Canvas(self.root,width = 200, height = 200)
        self.nome = self.root.title(nome)
        def callback1():
            print(1)  
        def callback2():
            print(2) 
        def callback3():
            print(3) 
        def callback4():
            print(4) 
        def callback5():
            print(5) 
        def callback6():
            print(6) 
        def callback7():
            print(7) 
        def callback8():
            print(8) 
        def callback9():
            print(9) 
        self.b1 = tk.Button(self.root, text="OK1", command=callback1, width = 10, height = 5)
        self.b2 = tk.Button(self.root, text="OK2", command=callback2, width = 10, height = 5)
        self.b3 = tk.Button(self.root, text="OK3", command=callback3, width = 10, height = 5)        
        self.b4 = tk.Button(self.root, text="OK4", command=callback4, width = 10, height = 5)
        self.b5 = tk.Button(self.root, text="OK5", command=callback5, width = 10, height = 5)
        self.b6 = tk.Button(self.root, text="OK6", command=callback6, width = 10, height = 5)
        self.b7 = tk.Button(self.root, text="OK7", command=callback7, width = 10, height = 5)
        self.b8 = tk.Button(self.root, text="OK8", command=callback8, width = 10, height = 5)
        self.b9 = tk.Button(self.root, text="OK9", command=callback9, width = 10, height = 5)
        
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
    
      
    
         
a = Tabuleiro("jogo da velha")
tk.mainloop()