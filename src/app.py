from view import View
from controller import Controller
from tkinter import Tk


class App:
    def __init__(self):
        root = Tk()
        root.option_add('*Font', 'OpenSans')
        view = View(root)
        #controller = Controller(view)
        root.mainloop()


app = App()