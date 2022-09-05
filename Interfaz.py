import tkinter as tk
from tkinter import Button, Frame, ttk
from managercsv import readcsv,blur

root = tk.Tk()
root.geometry("900x700")
frame=Frame(root, width=600,height=600)
#frame.pack(padx=10,pady=10)
frame.place(relx=0,rely=0)
#Generamos la letra b apartir del csv
patron = readcsv('data/letra_f.csv')
list_btn = []

for i in range(int(10)):
    list_btn.append([])
    for j in range(int(10)):
        list_btn[i].append(Button(frame))
        list_btn[i][j].pack()
        if (patron[i][j] =='1' ):
         list_btn[i][j].config(bg="blue", borderwidth ="1", activebackground="orange", relief="solid")

        list_btn[i][j].place(relx = 0.08 + 0.08*j, rely = 0.09 + 0.09*i, relwidth= 0.08, relheight=0.09)
      
blur(patron,30)
root.mainloop()


