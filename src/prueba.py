from tkinter import Tk
import customtkinter

class App:
    def __init__(self):
        customtkinter.set_appearance_mode("Dark")  
        customtkinter.set_default_color_theme("blue") 
        root = customtkinter.CTk()
        root.resizable(False, False)
        root.mainloop()

app = App()