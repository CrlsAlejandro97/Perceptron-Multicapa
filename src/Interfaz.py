import tkinter as tk
from tkinter import Button, Frame, ttk
import numpy as np

class Interfaz:
    def __init__(self, geometry, width, height):
        self.geometry = geometry
        self.width = width
        self.height = height
    
    def mostrar(self, letra, distorsion):
        root = tk.Tk() 
        root.geometry(self.geometry)
        frame=Frame(root, width=self.width,height=self.height)

        frame.place(relx=0,rely=0)

        # Transformo el arreglo de una letra a una matriz de 10x10
        letra_2d = np.reshape(letra, (10,10))
        list_btn = []
        for i in range(10):
            list_btn.append([])
            for j in range(10):
                list_btn[i].append(Button(frame))
                list_btn[i][j].pack()
                if (letra_2d[i][j] ==1 ):
                    list_btn[i][j].config(bg="blue", borderwidth ="1", activebackground="orange", relief="solid")
                list_btn[i][j].place(relx = 0.08 + 0.08*j, rely = 0.09 + 0.09*i, relwidth= 0.08, relheight=0.09) 
        print("Distorsion de letra: ", distorsion)
        root.mainloop()


      