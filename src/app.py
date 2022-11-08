from view import View
from controller import Controller
from tkinter import Tk
import customtkinter


class App:
    def __init__(self):
        customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        root = customtkinter.CTk()
        root.resizable(False, False)
        view = View(root)
        controller = Controller(view)
        root.mainloop()


app = App()

""" 
capp = 
capp.geometry("400x240")
def button_function():
    print("button pressed")

button = customtkinter.CTkButton(master=capp, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

capp.mainloop() """