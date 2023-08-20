import tkinter
import data_functions as df
from Perceptron import Perceptron
from Distorsionador import Distorsionador
import numpy as np
from tkinter import messagebox as MessageBox
from tkinter import *
import customtkinter
from matplotlib.figure import Figure 
from functools import partial
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 

class Controller:

    def __init__(self, view):
        self.view = view
        #view.buttons["create_perceptron"].configure(command=partial(self.create_perceptron))
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
                porc_train = 0.8
                porc_validation = 0.1
                data_train = letras[:int(len(letras)*porc_train)]
                data_validation = letras[int(len(letras)*porc_train)+1:int(len(letras)*porc_train)+int(len(letras)*porc_validation)]
                data_test = letras[int(len(letras)*porc_train)+int(len(letras)*porc_validation)+1:len(letras)-1]
                errores_train, errores_validation = perceptron.train(data_train, data_validation)
                pred_total, pred_b, pred_d, pred_f, cant_b, cant_d, cant_f = perceptron.test_train(data_test)
                MessageBox.showinfo("", "MLP ENTRENADO")
                self.view.create_button("Ver resultados", row=1, column=2, varname="show_grafica",master=self.view.frames["train"])
                self.view.buttons["show_grafica"].configure(command = partial(self.plot, errores_train, errores_validation, pred_total, pred_b, pred_d, pred_f, cant_b, cant_d, cant_f, len(data_test)))

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
        
        
    def plot(self, errores_train, errores_validation, pred_total, pred_b, pred_d, pred_f, cant_b, cant_d, cant_f, cant_total): 

        newWindow = Toplevel(self.view.master) 
        newWindow.title("Resultados") 
        newWindow.geometry("900x600")
        frameGrafico = customtkinter.CTkFrame(newWindow, corner_radius=0, bg_color="black")
        frameGrafico.configure(width=600,height=600)
        frameGrafico.grid_propagate(False)
        frameGrafico.grid(column=0, row=0)
      
        perceptron = self.perceptron
        epocas = self.perceptron.epocas
        cant_epocas = []
        for i in range(epocas):
            cant_epocas.append(i)

        fig = Figure(figsize = (6, 6), 
                    dpi = 100) 

    
        plot1 = fig.add_subplot(111) 

        plot1.set_title("MSE vs Epocas")
        
        x = range(1, len(cant_epocas)+1)
        plot1.plot(x, errores_train, linestyle='-', marker='.', color = 'r')
        plot1.plot(x, errores_validation, linestyle='-', marker='.', color = 'g')
        plot1.legend( ('Entrenamiento', 'Validacion'), loc = 'upper left')
        canvas = FigureCanvasTkAgg(fig, 
                                master = frameGrafico)   
        canvas.draw() 
    
        canvas.get_tk_widget().pack() 
        
        plot1.set_xlabel( 'Epocas' )
        plot1.set_ylabel( 'MSE' )


        frameTest = customtkinter.CTkFrame(newWindow, corner_radius=0, bg_color="#505050")
        frameTest.configure(width=300,height=600)
        frameTest.grid_propagate(False)
        frameTest.grid(column=1, row=0)
        titulo = customtkinter.CTkLabel(master=frameTest, text="TESTEO")  
        titulo.grid(row=0, column=0)
        text_subtitulo = f"Predicciones hechas en {cant_total} letras de testeo"
        subtitulo = customtkinter.CTkLabel(master=frameTest, text=text_subtitulo)  
        subtitulo.grid(row=1, column=0)
        text_total = f"TOTAL: {pred_total} predicciones correctas"
        l_total = customtkinter.CTkLabel(master=frameTest, text=text_total)  
        l_total.grid(row=2, column=0)
        text_b = f"Letra B: {pred_b} de {cant_b}"
        l_b = customtkinter.CTkLabel(master=frameTest, text=text_b)  
        l_b.grid(row=3, column=0)
        text_d = f"Letra D: {pred_d} de {cant_d}"
        l_d = customtkinter.CTkLabel(master=frameTest, text=text_d)  
        l_d.grid(row=4, column=0)
        text_f = f"Letra F: {pred_f} de {cant_f}"
        l_f = customtkinter.CTkLabel(master=frameTest, text=text_f)  
        l_f.grid(row=5, column=0)


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

        
        
        
       
        


        
        

        
        
    