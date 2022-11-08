from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
import customtkinter

class View:

    def __init__(self, master=None):
        self.master = master
        self.opcion_generar = IntVar()
        self.opcion_entrenar = IntVar()
        self.opcion_letra = IntVar()  
        self.labels = {}
        self.entries = {}
        self.buttons = {}
        self.scales = {}
        self.radios = {}
        self.frames = {}
        self.text_font = "default_theme"
        self.master.title("Perceptron")
        self.master.geometry("1000x600")
        
        self.createview()
        self.style = ttk.Style()
        self.style.configure("TScale", background="#505050")
    # adding elements of UI to window

    def createviewConfiguration(self):
        frame = customtkinter.CTkFrame(self.master, corner_radius=0) 
        frame.config(width=500,height=700)
        frame.grid_propagate(False)
        #frame.rowconfigure((0,1,2), weight=1)
        frame.grid(column=0, row=0, rowspan=2)
        self.frames["configuration"] = frame

    def createviewLetra(self):
        frame = customtkinter.CTkFrame(self.master, corner_radius=0)
        frame.config(width=500,height=700)
        frame.grid_propagate(False)
        frame.grid(column=1, row=0)
        self.frames["letra"] = frame
        
    def createviewConfigPerceptron(self):
        frame = customtkinter.CTkFrame(self.frames["configuration"], corner_radius=0) 
        frame.config(width=500,height=350)
        frame.grid_propagate(False)
        frame.grid(column=0, row=0, pady=0)
        self.frames["configPerceptron"] = frame

    def createviewTrain(self):
        frame = customtkinter.CTkFrame(self.frames["configuration"], corner_radius=0)
        frame.config(width=500,height=100)
        frame.grid_propagate(False)
        frame.columnconfigure((0, 1, 2, 3), weight=1)
        frame.grid(column=0, row=1)
        self.frames["train"] = frame

        
    def createviewPrediction(self):
        frame = customtkinter.CTkFrame(self.frames["configuration"], corner_radius=0)
        frame.config(width=500,height=150)
        frame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        frame.grid(column=0, row=2)
        frame.grid_propagate(False)
        self.frames["prediction"] = frame

    
    def createviewMatriz(self):
        frame = customtkinter.CTkFrame(self.frames["letra"], corner_radius=0)
        frame.config(width=500,height=360)
        frame.grid(column=0, row=0)
        frame.grid_propagate(False)
        self.frames["matriz"] = frame
        return self.frames["matriz"]
    
    def createviewLetraMatriz(self):
        frame = customtkinter.CTkFrame(self.frames["matriz"], corner_radius=0)
        frame.configure(width=500,height=400)
        
        frame.grid(column=0, row=1, columnspan=3)
        self.frames["letraMatriz"] = frame
        return self.frames["letraMatriz"]
    
    def createviewLetrasPrediction(self):
        frame = customtkinter.CTkFrame(self.frames["letra"], corner_radius=0)
        frame.config(width=500,height=240)
        frame.grid_propagate(False)
        frame.grid(column=0, row=1)
        self.frames["letrasPrediction"] = frame
        return self.frames["letrasPrediction"]


    def createview(self):

        self.createviewConfiguration()
        self.createviewLetra()
        #self.createviewGeneration()
        self.createviewConfigPerceptron()
        self.createviewTrain()
        self.createviewPrediction()
        self.createviewMatriz()
        self.createviewLetraMatriz()
        self.createTableroVacio()
        self.createviewLetrasPrediction()

        self.create_label("CONFIGURACION DEL PERCEPTRON", row=0, column=0, columnspan=3, master=self.frames["configPerceptron"])
        self.create_label("Cantidad neuronas 1era capa oculta", row=3, master=self.frames["configPerceptron"])
        self.create_entry(row=3,column=1, master=self.frames["configPerceptron"], varname="neuronas_capa_1")
        self.create_label("Cantidad neuronas 2da capa oculta", row=4, master=self.frames["configPerceptron"])
        self.create_entry(row=4,column=1, master=self.frames["configPerceptron"], varname="neuronas_capa_2")
        self.create_label("Coeficiente de aprendizaje", row=5, master=self.frames["configPerceptron"])
        self.create_scale(row=5, column=1,varname="aprendizaje", from_=0, to=1, orient=HORIZONTAL,resolution=0.01, master=self.frames["configPerceptron"])
        self.create_label("Momento", row=6, master=self.frames["configPerceptron"])
        self.create_scale(row=6, column=1,varname="momento", from_=0, to=1, orient=HORIZONTAL,resolution=0.01, master=self.frames["configPerceptron"])
        self.create_label("Cantidad de epocas", row=7, master=self.frames["configPerceptron"])
        self.create_entry(row=7,column=1, master=self.frames["configPerceptron"], varname="epocas")
        self.create_button("Crear", row=8, column=0,columnspan=3,varname="create_perceptron", master=self.frames["configPerceptron"])


        self.create_label("DATASET DE ENTRENAMIENTO", row=0, column=0,columnspan=3, master=self.frames["train"])
        self.create_radio("100", row=1, column=0, value=100, variable=self.opcion_entrenar, master=self.frames["train"])
        self.create_radio("500", row=1, column=1,value=500, variable=self.opcion_entrenar, master=self.frames["train"])
        self.create_radio("1000", row=1, column=2, value=1000, variable=self.opcion_entrenar, master=self.frames["train"])
        self.create_button("Entrenar", row=1, column=3, varname="train", master=self.frames["train"])
        

        self.create_label("PREDECIR LETRA", row=0, column=0, columnspan=3, master=self.frames["prediction"])
        self.create_label("Elegir letra", row=1, column=0, columnspan=3, master=self.frames["prediction"])
        self.create_radio("B", row=2, column=0, value=1, variable=self.opcion_letra, master=self.frames["prediction"])
        self.create_radio("D", row=2, column=1,value=2, variable=self.opcion_letra, master=self.frames["prediction"])
        self.create_radio("F", row=2, column=2, value=3, variable=self.opcion_letra, master=self.frames["prediction"])
        self.create_label("Distorsion", row=1, column=3, master=self.frames["prediction"])
        self.create_scale(row=2, column=3,varname="distorsion",from_=0, to=0.3, orient=HORIZONTAL,resolution=0.01, master=self.frames["prediction"])
        
        self.create_button("Predecir", row=2, column=4, varname="predecir", master=self.frames["prediction"])

        self.create_label("VISUALIZACION DE LETRA", row=0, column=0, columnspan=3, master=self.frames["matriz"])

        self.create_label("PREDICCIONES", row=0, column=0, columnspan=3, master=self.frames["letrasPrediction"])

    def create_label(self, text="", textvar=None, row=0, column=0, columnspan=1, pady=10, padx=20, varname="", master=None):
        if varname == "":
            varname = text
        self.labels[varname] = customtkinter.CTkLabel(master=master, text=text, textvariable=textvar)
        self.labels[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=padx)

    def create_entry(self, row, column, varname, columnspan=1, pady=10, padx=20,master=None):
        self.entries[varname] = customtkinter.CTkEntry(master=master)
        self.entries[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=padx)

    def create_button(self, text, row=0, column=0, columnspan=1, varname="", state=NORMAL, pady=10, padx=5, master=None):
        if varname == "":
            varname = text
        self.buttons[varname] = customtkinter.CTkButton(master=master, text=text, state=state)
        self.buttons[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=padx)

    def create_separator(self, row, columnspan, orient="horizontal", pady=10, padx=0, master=None):
        ttk.Separator(master=master, orient=orient).grid(row=row, columnspan=columnspan, sticky="ew", pady=pady, padx=padx)

    def create_scale(self, row=0, column=0, columnspan=1, varname="", from_=0, to=1, orient=HORIZONTAL, resolution=1, master=None):
        self.scales[varname] = tk.Scale(master=master, from_=from_, to=to, orient=orient, resolution=resolution, background = "#353638", activebackground="#353638", bd=0, troughcolor="#2b6593", fg="white", length=120, relief=GROOVE, highlightthickness=0) 
        self.scales[varname].grid(row=row, column=column, columnspan=columnspan) 
        #self.scales[varname].configure(style="TScale")
    
    def create_radio(self, text, row, column, columnspan=1, value=None, variable=None, master=None):
        radio_button = customtkinter.CTkRadioButton(master=master, text=text, value=value, variable=variable)
        radio_button.grid(row=row, column=column, columnspan=columnspan)


    def set_command(self, varname, command):
        self.buttons[varname].configure(command=command)

    def set_button_normal(self, varname):
        self.get_button(varname)["state"] = NORMAL

    def createTableroVacio(self):
        list_btn = []
        for i in range(10):
            list_btn.append([])
            for j in range(10):
                list_btn[i].append(customtkinter.CTkButton(self.frames["letraMatriz"], relief="solid", corner_radius=0, hover=False, text="", border_width =1, border_color="#FFFFFF"))
                list_btn[i][j].pack()
                list_btn[i][j].place(relx = 0.06 + 0.06*j, rely = 0.07 + 0.07*i, relwidth= 0.06, relheight=0.07) 


    