# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:18:16 2020

@author: -
"""
#Pour importer depuis un autre fichier (pratique pour simplifier le code)
#Faire import(fichier sans le .py) 


import menu
from tkinter import*
import modecarte
import fenetre




def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
