from tkinter import *
import tkinter as tk
from tkinter import ttk

class View:

    def __init__(self, master=None):
        self.master = master
        self.figure = None
        self.canvas = None
        self.opcion_generar = IntVar()
        self.opcion_entrenar = IntVar()
        self.opcion_letra = IntVar()  
        self.labels = {}
        self.entries = {}
        self.buttons = {}
        self.scales = {}
        self.radios = {}
        self.frames = {}
        self.master.title("Perceptron")
        self.master.geometry("1000x500")
        self.master.resizable(width=0, height=0)
        self.createviewConfiguration()
        self.createviewPrediction()
        self.createviewGeneration()
        self.createviewPerceptron()
        self.createviewTrain()
        self.createview()

    # adding elements of UI to window

    def createviewConfiguration(self):
        frame1 = tk.Frame(self.master) 
        frame1.config(width=500,height=600, borderwidth=1, relief="solid")
        frame1.grid(column=0, row=0, rowspan=2)
        self.frame1 = frame1

    def createviewPrediction(self):
        frame2 = tk.Frame(self.master)
        frame2.config(width=500,height=600)
        frame2.grid(column=1, row=0)
        self.frame2 = frame2
    
    def createviewGeneration(self):
        frame = tk.Frame(self.frame1)
        frame.config(width=500,height=150)
        frame.grid(column=0, row=0)
        self.frame4 = frame

    def createviewPerceptron(self):
        frame3 = tk.Frame(self.frame1) 
        frame3.config(width=500,height=300)
        frame3.grid(column=0, row=1)
        self.frame3 = frame3

    def createviewTrain(self):
        frame = tk.Frame(self.frame1)
        frame.config(width=500,height=300)
        frame.grid(column=0, row=2)
        self.frame5 = frame

    def createview(self):
            

        self.create_label("GENERACION DE DATASET", row=0, column=0, columnspan=3, master=self.frame4)
        self.create_radio("100", row=1, column=0, value=100, variable=self.opcion_generar, master=self.frame4)
        self.create_radio("500", row=1, column=1, value=500, variable=self.opcion_generar, master=self.frame4)
        self.create_radio("1000", row=1, column=2, value=1000, variable=self.opcion_generar, master=self.frame4)
        self.create_button("Generar", row=1, column=3,varname="generate", master=self.frame4)


        self.create_label("CONFIGURACION DEL PERCEPTRON", row=0, column=0, columnspan=3, master=self.frame3)
        self.create_label("Cantidad neuronas 1era capa oculta", row=3, master=self.frame3)
        self.create_entry(row=3,column=1, master=self.frame3, varname="neuronas_capa_1")
        self.create_label("Cantidad neuronas 2da capa oculta", row=4, master=self.frame3)
        self.create_entry(row=4,column=1, master=self.frame3, varname="neuronas_capa_2")
        self.create_label("Coeficiente de aprendizaje", row=5, master=self.frame3)
        self.create_scale(row=5, column=1,varname="aprendizaje", from_=0, to=1, orient=HORIZONTAL,resolution=0.05, master=self.frame3)
        self.create_label("Momento", row=6, master=self.frame3)
        self.create_scale(row=6, column=1,varname="momento", from_=0, to=1, orient=HORIZONTAL,resolution=0.05, master=self.frame3)
        
        
        self.create_button("Crear", row=7, column=0,columnspan=3,varname="create_perceptron", master=self.frame3)


        self.create_label("DATASET DE ENTRENAMIENTO", row=0, column=0,columnspan=3, master=self.frame5)
        self.create_radio("100", row=1, column=0, value=100, variable=self.opcion_entrenar, master=self.frame5)
        self.create_radio("500", row=1, column=1,value=500, variable=self.opcion_entrenar, master=self.frame5)
        self.create_radio("1000", row=1, column=2, value=1000, variable=self.opcion_entrenar, master=self.frame5)
        self.create_button("Entrenar", row=1, column=3, varname="train", master=self.frame5)
        

        self.create_label("PREDECIR LETRA", row=0, column=0, columnspan=3, master=self.frame2)
        self.create_label("Elegir letra", row=1, column=0, columnspan=3, master=self.frame2)
        self.create_radio("B", row=2, column=1, value=1, variable=self.opcion_letra, master=self.frame2)
        self.create_radio("D", row=2, column=2,value=2, variable=self.opcion_letra, master=self.frame2)
        self.create_radio("F", row=2, column=3, value=3, variable=self.opcion_letra, master=self.frame2)
        self.create_label("Distorsion", row=3, column=0, columnspan=3, master=self.frame2)
        self.create_scale(row=4, column=1, columnspan=2,varname="distorsion", from_=0, to=0.3, orient=HORIZONTAL,resolution=0.01, master=self.frame2)

        self.create_button("PREDECIR", row=5, column=1, columnspan=3, varname="predecir", master=self.frame2)

    def create_label(self, text="", textvar=None, row=0, column=0, columnspan=1, pady=10, padx=20, varname="", master=None):
        if varname == "":
            varname = text
        self.labels[varname] = Label(master=master, text=text, textvariable=textvar)
        self.labels[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=padx)

    def create_entry(self, row, column, varname, columnspan=1, pady=10, padx=20,master=None):
        self.entries[varname] = Entry(master=master)
        self.entries[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=padx)

    def create_button(self, text, row=0, column=0, columnspan=1, varname="", state=NORMAL, pady=10, padx=5, master=None):
        if varname == "":
            varname = text
        self.buttons[varname] = Button(master=master, text=text, state=state, pady=5)
        self.buttons[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=padx)

    def create_separator(self, row, columnspan, orient="horizontal", pady=10, padx=0, master=None):
        ttk.Separator(master=master, orient=orient).grid(row=row, columnspan=columnspan, sticky="ew", pady=pady, padx=padx)

    def create_scale(self, row=0, column=0, columnspan=1, varname="", from_=0, to=1, orient=HORIZONTAL, resolution=1, master=None):
        self.scales[varname] = Scale(master=master, from_=from_, to=to, orient=orient, resolution=resolution) 
        self.scales[varname].grid(row=row, column=column, columnspan=columnspan) 
    
    def create_radio(self, text, row, column, columnspan=1, value=None, variable=None, master=None):
        radio_button = Radiobutton(master=master, text=text, value=value, variable=variable)
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