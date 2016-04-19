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
        def callback(w):
            print(str(w))  
        self.b1 = tk.Button(self.root, text="OK1", command=callback(1), width = 10, height = 5)
        self.b2 = tk.Button(self.root, text="OK2", command=callback(2), width = 10, height = 5)
        self.b3 = tk.Button(self.root, text="OK3", command=callback(3), width = 10, height = 5)        
        self.b4 = tk.Button(self.root, text="OK4", command=callback(4), width = 10, height = 5)
        self.b5 = tk.Button(self.root, text="OK5", command=callback(5), width = 10, height = 5)
        self.b6 = tk.Button(self.root, text="OK6", command=callback(6), width = 10, height = 5)
        self.b7 = tk.Button(self.root, text="OK7", command=callback(7), width = 10, height = 5)
        self.b8 = tk.Button(self.root, text="OK8", command=callback(8), width = 10, height = 5)
        self.b9 = tk.Button(self.root, text="OK9", command=callback(9), width = 10, height = 5)
        
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
    
      
    
         
a = Tabuleiro()
tk.mainloop()