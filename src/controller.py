import data_functions as df
from Perceptron import Perceptron
from Distorsionador import Distorsionador
import numpy as np
from tkinter import messagebox as MessageBox
from tkinter import *
import customtkinter
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 

class Controller:

    def __init__(self, view):
        self.view = view
        view.set_command("create_perceptron", self.create_perceptron)
        view.set_command("train", self.train)
        view.set_command("predecir", self.predecir_letra)

    def train(self):
        
        try:
            cantidad = str(self.view.opcion_entrenar.get())
            df.generar_data_letras(cantidad)
            df.generar_data_distorsionadas(cantidad)
            letras = df.get_letras_distorsionadas(cantidad)
            data_train = letras[:int(len(letras)*0.8)]
            data_test = letras[int(len(letras)*0.8)+1:int(len(letras)*0.8)+int(len(letras)*0.15)]
            data_validation = letras[int(len(letras)*0.8)+int(len(letras)*0.15)+1:99]
            self.perceptron.train(data_train)
            MessageBox.showinfo("", "MLP ENTRENADO")
        except:
            MessageBox.showerror("", "Elegir un dataset para entrenar")
        

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
    
        newWindow.geometry("500x500") 
        
        Label(newWindow,  
            text ="This is a new window").pack()
  
        perceptron = self.perceptron
        epocas = self.perceptron.epocas
        percentage_error_training = 0
        percentage_error_validation = 0

        fig = Figure(figsize = (5, 5), 
                    dpi = 100) 
        
        y = [i**2 for i in range(101)] 
            
        plot1 = fig.add_subplot(111) 
    
        plot1.plot(y) 
        
        canvas = FigureCanvasTkAgg(fig, 
                                master = newWindow)   
        canvas.draw() 
    
        canvas.get_tk_widget().pack() 
        
        toolbar = NavigationToolbar2Tk(canvas, 
                                    newWindow) 

        toolbar.update() 
        
        canvas.get_tk_widget().pack() 



    def predecir_letra(self):
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

            letras_predicciones = self.perceptron.predecir(letra_distorsionada)
            self.mostrarLetra(letra_distorsionada, letras_predicciones)
            self.view.create_button("Ver grafica de error", row=4, column=0, varname="show_grafica",master=self.view.frames["letrasPrediction"])
            self.view.set_command("show_grafica", self.plot)
        except:
            MessageBox.showerror("", "Elegir una letra para predecir")
        

    
    def mostrarLetra(self, letra_distorsionada, letras_predicciones):
        
        if self.view.frames["letraMatriz"].winfo_exists() == 1:
            print("Se destruyo el tablero")
            self.view.frames["letraMatriz"].destroy()
        
        frameLetraMatriz = self.view.createviewLetraMatriz()
        frameLetraPredictions = self.view.createviewLetrasPrediction()
        self.view.create_label("PREDICCIONES", row=0, column=0, columnspan=3, master=self.view.frames["letrasPrediction"])
        for i, letra in enumerate(letras_predicciones.keys()):
            if i == 0:
                texto_prediccion = f"Letra predecida: {letra} con un acierto del {letras_predicciones[letra]}%"
                label_prediccion = customtkinter.CTkLabel(master=self.view.frames["letrasPrediction"], text=texto_prediccion, text_font='Helvetica 16 bold', fg_color="blue")
            else:
                texto_prediccion = f"Letra: {letra} con un acierto del {letras_predicciones[letra]}%"
                label_prediccion = customtkinter.CTkLabel(master=self.view.frames["letrasPrediction"], text=texto_prediccion)
            label_prediccion.grid(row=i+1, column=0)
        


        letra_2d = np.reshape(letra_distorsionada, (10,10))
        list_btn = []
        for i in range(10):
            list_btn.append([])
            for j in range(10):
                list_btn[i].append(customtkinter.CTkButton(frameLetraMatriz, relief="solid", corner_radius=0, hover=False, text="", border_width =1, border_color="#FFFFFF"))
                list_btn[i][j].pack()
                if (letra_2d[i][j] ==1 ):
                    list_btn[i][j].configure(bg="blue", fg_color="black")
                list_btn[i][j].place(relx = 0.06 + 0.06*j, rely = 0.07 + 0.07*i, relwidth= 0.06, relheight=0.07) 
        

        
        
    