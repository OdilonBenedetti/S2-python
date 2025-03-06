def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

import tkinter as tk
racine = tk.Tk()
C = tk.Canvas(racine, height = 256, width = 256, bg = 'black')
B1 = tk.Button(racine, text = 'Aléatoire')
B2 = tk.Button(racine, text = 'Dégradé de gris')
B3 = tk.Button(racine, text = 'Dégradé 2D')

C.grid(row = 0, column = 1, rowspan = 3)
B1.grid(row = 0, column = 0)
B2.grid(row = 3, column = 0)
B3.grid(row = 2, column = 0)
racine.mainloop