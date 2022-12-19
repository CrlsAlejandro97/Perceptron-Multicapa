import data_functions as df
from Perceptron import Perceptron
from Distorsionador import Distorsionador
import numpy as np
from tkinter import messagebox as MessageBox
from tkinter import *
import customtkinter
from matplotlib.figure import Figure 
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 

class Controller:

    def __init__(self, view):
        self.view = view
        view.set_command("create_perceptron", self.create_perceptron)
        view.set_command("train", self.train)
        view.set_command("visualizar", self.visualizar_letra)
        view.set_command("predecir", self.predecir_letra)


    def visualizar_letra(self):
        try:
            opcion_letra = self.view.opcion_letra.get()
            if opcion_letra == 1:
                letra="B"
            elif opcion_letra == 2:
                letra="D"
            elif opcion_letra==3:
                letra = "F"
            
            distorsion = float(self.view.scales["distorsion"].get())
            distorsionador = Distorsionador(0, 0.3)
            letra_codigo = df.generar_letra(letra)
            letra_distorsionada = distorsionador._dist_letra(letra_codigo, distorsion)
            self.letra_distorsionada = letra_distorsionada
            self.mostrarLetra(letra_distorsionada)
        except:
            MessageBox.showerror("", "Elegir una letra a visualizar")

    def train(self):

        try:
            perceptron = self.perceptron
        
            try:
                cantidad = str(self.view.opcion_entrenar.get())
                df.generar_data_letras(cantidad)
                df.generar_data_distorsionadas(cantidad)
                letras = df.get_letras_distorsionadas(cantidad)
                data_train = letras[:int(len(letras)*0.8)]
                data_test = letras[int(len(letras)*0.8)+1:int(len(letras)*0.8)+int(len(letras)*0.15)]
                data_validation = letras[int(len(letras)*0.8)+int(len(letras)*0.15)+1:99]
                perceptron.train(data_train)
                MessageBox.showinfo("", "MLP ENTRENADO")
                self.view.create_button("Ver grafica de error", row=1, column=2, varname="show_grafica",master=self.view.frames["train"])
                self.view.set_command("show_grafica", self.plot)

            except:
                MessageBox.showerror("", "Elegir un dataset para entrenar")

        except:
            MessageBox.showerror("", "No se ha creado un modelo")

    def create_perceptron(self):
        try:
            neuronas_capa_1 = int(self.view.entries["neuronas_capa_1"].get())
            neuronas_capa_2 = int(self.view.entries["neuronas_capa_2"].get())
            aprendizaje = float(self.view.scales["aprendizaje"].get())
            momento = float(self.view.scales["momento"].get())
            epocas = int(self.view.entries["epocas"].get())
            if neuronas_capa_1 == 0:
                sizes = [neuronas_capa_2]
            elif neuronas_capa_2 == 0:
                sizes = [neuronas_capa_1]
            else:
                sizes = [neuronas_capa_1, neuronas_capa_2]
            perceptron = Perceptron(sizes, aprendizaje, momento, epocas)
            w, b = perceptron.init_params()
            capas = perceptron.init_layers()
            MessageBox.showinfo("", "PERCEPTRON CREADO")
            self.perceptron = perceptron
        except:
            MessageBox.showerror("", "Rellenar todos los campos")
        
        
    def plot(self): 

        newWindow = Toplevel(self.view.master) 
        newWindow.title("Grafica de error") 
        newWindow.geometry("600x600") 
        
        perceptron = self.perceptron
        epocas = self.perceptron.epocas
        errores = self.perceptron.error_train
        cant_epocas = []
        for i in range(epocas):
            cant_epocas.append(i)

        fig = Figure(figsize = (6, 6), 
                    dpi = 100) 

    
        plot1 = fig.add_subplot(111) 

        plot1.set_title("Error de salida por Epoca")
        
        default_x_ticks = range(1, len(cant_epocas)+1)
        plot1.plot(default_x_ticks, errores)
        
        canvas = FigureCanvasTkAgg(fig, 
                                master = newWindow)   
        canvas.draw() 
    
        canvas.get_tk_widget().pack() 
        
        toolbar = NavigationToolbar2Tk(canvas, 
                                    newWindow) 

        toolbar.update() 
        
        canvas.get_tk_widget().pack() 

        plot1.set_xlabel( 'EPOCAS' )
        plot1.set_ylabel( 'ERROR (%)' )



    def predecir_letra(self):
        
        try:
            perceptron = self.perceptron
            try:
                letra_distorsionada = self.letra_distorsionada
                letras_predicciones = self.perceptron.predecir(letra_distorsionada)

                for i, letra in enumerate(letras_predicciones.keys()):
                    if i == 0:
                        texto_prediccion = f"Letra predecida: {letra} con un acierto del {letras_predicciones[letra]}%"
                        label_prediccion = customtkinter.CTkLabel(master=self.view.frames["letrasPrediction"], text=texto_prediccion, text_font='Helvetica 16 bold', fg_color="blue")
                    else:
                        texto_prediccion = f"Letra: {letra} con un acierto del {letras_predicciones[letra]}%"
                        label_prediccion = customtkinter.CTkLabel(master=self.view.frames["letrasPrediction"], text=texto_prediccion)
                    label_prediccion.place(relx=0, rely=0.25 + 0.15*i) 
            except:
                MessageBox.showerror("", "No se ha elegido una letra para predecir")
        except:
                MessageBox.showerror("", "No se ha creado un perceptron")

        
           
        
        

    
    def mostrarLetra(self, letra_distorsionada):
        
        if self.view.frames["letraMatriz"].winfo_exists() == 1:
            self.view.frames["letraMatriz"].destroy()
        
        frameLetraMatriz = self.view.createviewLetraMatriz()
        
        letra_2d = np.reshape(letra_distorsionada, (10,10))
        list_btn = []
        for i in range(10):
            list_btn.append([])
            for j in range(10):
                list_btn[i].append(customtkinter.CTkButton(frameLetraMatriz, relief="solid", corner_radius=0, hover=False, text="", border_width =1, border_color="#FFFFFF"))
                list_btn[i][j].pack()
                if (letra_2d[i][j] ==1 ):
                    list_btn[i][j].configure(bg="blue", fg_color="black")
                list_btn[i][j].place(relx = 0.18 + 0.06*j, rely = 0.04 + 0.07*i, relwidth= 0.06, relheight=0.07)

        
        
        
       
        


        
        

        
        
    