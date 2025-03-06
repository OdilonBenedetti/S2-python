import tkinter as tk
racine = tk.Tk()
H = 800
C = tk.Canvas(racine, height=H, width=H, bg='black')
a = 0
couleurs = ['blue','green','black','yellow','magenta','red']
for i in range(5):
    for j in range(6):
        C.create_oval((a,a),(H-a,H-a), fill = couleurs[j], width = 0)
        a = a + 10

C.grid()
racine.mainloop()
