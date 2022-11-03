from tkinter import *
from tkinter import ttk

class View:

    def __init__(self, master=None):
        self.master = master
        self.figure = None
        self.canvas = None
        self.opcion_generar = IntVar()
        self.opcion_entrenar = IntVar()  
        self.labels = {}
        self.entries = {}
        self.buttons = {}
        self.scales = {}
        self.radios = {}

        self.createview()

    # adding elements of UI to window
    def createview(self):
        self.master.title("Perceptron")
        self.master.geometry("1000x600")
        

        self.create_label("GENERACION DE DATASET", row=0)
        self.create_label("CONFIGURACION DEL PERCEPTRON", row=4)
        self.create_label("DATASET DE ENTRENAMIENTO", row=10)
        self.create_label("Neuronas por capa oculta (Separarlos por coma)", row=5)
        self.create_label("Coeficiente de aprendizaje", row=6)
        self.create_label("Momento", row=7)

        self.create_entry(5, 1, "tamaño")

        self.create_radio("100", row=1, column=0, value=100, variable=self.opcion_generar)
        self.create_radio("500", row=1, column=0, columnspan=10,value=500, variable=self.opcion_generar)
        self.create_radio("1000", row=1, column=1, value=1000, variable=self.opcion_generar)

        self.create_radio("100", row=11, column=0, value=100, variable=self.opcion_entrenar)
        self.create_radio("500", row=11, column=0, columnspan=10,value=500, variable=self.opcion_entrenar)
        self.create_radio("1000", row=11, column=1, value=1000, variable=self.opcion_entrenar)

        self.create_button("Generar", row=1, column=2, columnspan=10,varname="generate")
        self.create_button("Crear", row=8, column=0,varname="create_perceptron")
        self.create_button("Entrenar", row=11, column=2, columnspan=10, varname="train")
        
        self.create_scale(row=6, column=1,varname="aprendizaje", from_=0, to=1, orient=HORIZONTAL,resolution=0.05)
        self.create_scale(row=7, column=1,varname="momento", from_=0, to=1, orient=HORIZONTAL,resolution=0.05)

        self.create_separator(3, 2)
        self.create_separator(9, 2)


    def create_label(self, text="", textvar=None, row=0, column=0, columnspan=1, pady=10, padx=20, varname=""):
        if varname == "":
            varname = text
        self.labels[varname] = Label(master=self.master, text=text, textvariable=textvar)
        self.labels[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=padx)

    def create_entry(self, row, column, varname, columnspan=1, pady=10, padx=20,):
        self.entries[varname] = Entry(self.master)
        self.entries[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=padx)

    def create_button(self, text, row=0, column=0, columnspan=1, varname="", state=NORMAL, pady=10, padx=5,):
        if varname == "":
            varname = text
        self.buttons[varname] = Button(self.master, text=text, state=state, pady=5)
        self.buttons[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=padx)

    def create_separator(self, row, columnspan, orient="horizontal", pady=10, padx=0,):
        ttk.Separator(self.master, orient=orient).grid(row=row, columnspan=columnspan, sticky="ew", pady=pady, padx=padx)

    def create_scale(self, row=0, column=0, columnspan=1, varname="", from_=0, to=1, orient=HORIZONTAL, resolution=1):
        self.scales[varname] = Scale(self.master, from_=from_, to=to, orient=orient, resolution=resolution) 
        self.scales[varname].grid(row=row, column=column, columnspan=columnspan) 
    
    def create_radio(self, text, row, column, columnspan=1, value=None, variable=None):
        radio_button = Radiobutton(self.master, text=text, value=value, variable=variable)
        radio_button.grid(row=row, column=column, columnspan=columnspan)


    def set_command(self, varname, command):
        self.buttons[varname]["command"] = command

    def set_button_normal(self, varname):
        self.get_button(varname)["state"] = NORMAL

    def get_label(self, varname):
        return self.labels[varname]

    def get_entry(self, varname):
        return self.entries[varname]

    def get_button(self, varname):
        return self.buttons[varname]