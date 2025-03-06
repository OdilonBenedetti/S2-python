import tkinter as tk
import random as rd
racine = tk.Tk()
racine.title('Mon dessin')
fond = tk.Canvas(racine, width = 600, height = 600, bg = 'black')
S = 'blue'
couleur = ['blue','red','green','yellow','white','black']
def choix():
    global S
    S = input("Choisis une couleur")

BB = tk.Button(racine, text = 'Choisir une couleur', command = choix)

def Ce():
    R1 = rd.randint(0,500)
    R2 = rd.randint(0,500)
    fond.create_oval((R1,R2),(R1+100,R2+100), fill = S, width=0)

def Ca():
    R1 = rd.randint(0,500)
    R2 = rd.randint(0,500)
    fond.create_rectangle((R1,R2),(R1+100,R2+100), fill = S, width=0)

def Cr():
    R1 = rd.randint(0,500)
    R2 = rd.randint(0,500)
    fond.create_rectangle((R1,R2),(R1+100,R2+100))
    fond.create_line((R1+50,R2+15),(R1+50,R2+85), fill = S, width = 5)
    fond.create_line((R1+15,R2+50),(R1+85,R2+50), fill = S, width = 5)

b1 = tk.Button(racine, text = 'cercle', command = Ce)
b2 = tk.Button(racine, text = 'carré', command = Ca)
b3 = tk.Button(racine, text = 'croix', command = Cr)

fond.grid(row = 1, column = 1, rowspan = 3)
BB.grid(row = 0 , column = 1)
b1.grid(row = 1 , column = 0)
b2.grid(row = 2 , column = 0)
b3.grid(row = 3 , column = 0)
racine.mainloop()
