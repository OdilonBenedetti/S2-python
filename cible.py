import tkinter as tk
racine = tk.Tk()
H = 1000
C = tk.Canvas(racine, height=H, width=H, bg = 'black')
a = 0
Co = ['blue','green','black','yellow','magenta','red']
for i in range(5):
    for j in range(6):
        C.create_oval((a,a),(H-a,H-a), fill = Co[j], width=0)
        a = a + 5

C.grid(row = 0, column = 0)
racine.mainloop
