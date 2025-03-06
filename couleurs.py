def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

import tkinter as tk
import random as rd

racine = tk.Tk()
C = tk.Canvas(racine, height = 256, width = 256, bg = 'black')

def draw_pixel(i,j,color):
    C.create_rectangle(i,j,i+1,j+1, width=0, fill = color)

def ecran_aleatoire():
    for i in range(256):
        for j in range(256):
            draw_pixel(i,j,get_color(rd.randint(0,256),rd.randint(0,256),rd.randint(0,256)))

def degrade_gris():
    a = 0
    for i in range(256):
        for j in range(256):
            draw_pixel(i,j,get_color(a,a,a))
        a = a + 1

def degrade_2D():
    a = 0
    for i in range(256):
        b = 0
        for j in range(256):
            draw_pixel(i,j,get_color(a,0,b))
            b = b + 1
        a = a + 1

B1 = tk.Button(racine, text = 'Aléatoire', command = ecran_aleatoire)
B2 = tk.Button(racine, text = 'Dégradé de gris', command = degrade_gris)
B3 = tk.Button(racine, text = 'Dégradé 2D', command = degrade_2D)

C.grid(row = 0, column = 1, rowspan = 3)
B1.grid(row = 0, column = 0)
B2.grid(row = 3, column = 0)
B3.grid(row = 2, column = 0)
racine.mainloop