# -*- coding: utf-8 -*-
"""
@author: TIM
"""

from tkinter import *

PICT_SIZE=142
PAD=20 #Espacement enrte les cartes
SIDE=PICT_SIZE+PAD

NB_LINES=4 #Nombre de ligne à modifier selon le mode
NB_COLS=5 #Nombre de colones à modifier selon le mode

WIDTH=SIDE*NB_COLS
HEIGHT=SIDE*NB_LINES
X0=Y0=SIDE//2

root=Tk()
root.title('Fenetre des cartes')
cnv=Canvas(root, width=WIDTH, height=HEIGHT, bg='red')
cnv.pack()

cover = PhotoImage(file="./images/carte.png") #Image des cartes

# Placement des images
def affichage_cartes():
    for line in range(NB_LINES):
        for col in range(NB_COLS):
            centre=(X0+col*SIDE, Y0+line*SIDE)
            cnv.create_image(centre, image=cover)

#def supprime_cartes():
#Je cherche pour quand on clique sur un canvas on le supprime

BoutonCarte = Button(root, text ='Afficher les carte', command = affichage_cartes, relief=GROOVE)
BoutonCarte.pack(side = TOP, padx = 5, pady = 5)

root.mainloop()
